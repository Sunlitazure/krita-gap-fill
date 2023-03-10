from krita import *

# https://docs.krita.org/en/user_manual/python_scripting/krita_python_plugin_howto.html
# https://scripting.krita.org/lessons/plugins-extensions

class GapFill(Extension):
	def __init__(self, parent):
		super().__init__(parent)
		
		self.app = parent
		self.currentDoc = self.app.activeDocument()

	def setup(self):
		pass

	def createActions(self, window):
		action = window.createAction("gapFillAction", "Gap Fill", "tools/scripts")
		action.triggered.connect(self.gapFillMethod)
		
	def gapFillMethod(self):
		#for layer in self.currentDoc.topLevelNodes():
		#   if layer == self.currentDoc.activeNode():
		#        lineArtLayer = layer
		 #   if 
		 
		self.currentDoc = self.app.activeDocument()
		 
		lineArtLayer = self.currentDoc.activeNode()
		
		gapFillLayer = self.currentDoc.createNode("Gap Fill", "paintlayer")    
		self.currentDoc.rootNode().addChildNode(gapFillLayer, None)
		
		self.currentDoc.waitForDone ( )
		self.currentDoc.refreshProjection()
		
		selection = Selection()
		self.currentDoc.setSelection(selection)
		
		if type(lineArtLayer) == GroupLayer:
			parent = lineArtLayer
			if len(parent.childNodes()) != 0:
				bottomLayer = parent.childNodes()[0]
		else:
			bottomLayer = lineArtLayer
			parent = bottomLayer.parentNode()

		self.currentDoc.setActiveNode(lineArtLayer)

		self.app.action("selectopaque").trigger() 
		self.currentDoc.waitForDone ( )
		self.currentDoc.refreshProjection()
				
		for layer in self.currentDoc.topLevelNodes():
			if type(layer) == SelectionMask:
				self.currentDoc.setActiveNode(layer)
				self.thresholdFilter(layer)
				self.currentDoc.refreshProjection()
				break

		selection.grow(9, 9)
		self.currentDoc.refreshProjection()
		
		selection.shrink(9, 9, False)
		self.currentDoc.refreshProjection()
		
		self.currentDoc.setActiveNode(gapFillLayer)
		self.currentDoc.refreshProjection()
		
		
		eraseAction = self.app.action("erase_action")
		if eraseAction.isChecked():
			eraseAction.trigger()
			self.currentDoc.waitForDone ( )
			self.currentDoc.refreshProjection()

		self.app.action('fill_selection_foreground_color').trigger()
		self.currentDoc.waitForDone ( )
		self.currentDoc.refreshProjection()
		
		self.currentDoc.setActiveNode(lineArtLayer)
		self.currentDoc.refreshProjection()
		
		self.app.action("selectopaque").trigger() 

		self.currentDoc.waitForDone ( )
		self.currentDoc.refreshProjection()
		
		for layer in self.currentDoc.topLevelNodes():
			if type(layer) == SelectionMask:
				self.currentDoc.setActiveNode(layer)
				self.thresholdFilter(layer)
				self.currentDoc.refreshProjection()
				break
				
		self.currentDoc.setActiveNode(gapFillLayer)
		self.currentDoc.refreshProjection()
		
		#Krita.instance().action("clear").trigger()
		#self.currentDoc.setActiveNode(gapFillLayer)
		#self.currentDoc.refreshProjection()
		
		selection.cut(gapFillLayer)
		self.currentDoc.refreshProjection()
		
		self.app.action("selectopaque").trigger()
		
		self.currentDoc.waitForDone ( )
		self.currentDoc.refreshProjection()
		
		selection.border(1,1)
		selection.invert()
		selection.cut(gapFillLayer)
		self.app.action("deselect").trigger()
		self.currentDoc.waitForDone ( )
		self.currentDoc.refreshProjection()
		
		self.currentDoc.rootNode().removeChildNode(gapFillLayer)
		parent.addChildNode(gapFillLayer, bottomLayer)
		parent.removeChildNode(bottomLayer)
		parent.addChildNode(bottomLayer, gapFillLayer)
		self.currentDoc.refreshProjection()
		
		gapFillLayer.setOpacity(3)
		self.currentDoc.refreshProjection()
		
		lineArtLayer.setColorLabel(8) #gray label
		for layer in lineArtLayer.childNodes():
			layer.setColorLabel(8)
		self.currentDoc.refreshProjection()
		
		
		
	def thresholdFilter(self, layer):
		filter = self.app.filter('threshold')
		filterConfig = filter.configuration()
		#print(filterConfig.properties())
		filterConfig.setProperty('threshold', 0)
		filter.setConfiguration(filterConfig)
		filter.apply(layer, 0, 0, self.currentDoc.width(), self.currentDoc.height())
		self.currentDoc.refreshProjection()



#
# If krita crashes w/o report, start commenting stuff until it does start, problem is probably trying to access something that hasn't loaded yet
# If krita starts but nothing shows up, look at Settings->Configure Krita->Addons, if your addon is greyed out mouse over it to see the error
#



