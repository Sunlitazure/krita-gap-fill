
# GapFill Krita Addon

Automatically fills gaps in line art (and groups of line art layers) by creating a new layer containing just the automatically filled gaps

For use with the "Enclose and Fill Tool" that currently doesn't support gap filling

## Installation

On Windows:

1. Place GapFill folder and GapFill.desktop in C:\Users\\%USERPROFILE%\AppData\Roaming\krita\pykrita 
2. Place GapFill.action in C:\Users\\%USERPROFILE%\AppData\Roaming\krita\actions

If the pykrita or actions folder don't already exist, create them.

## Use

Addon is found in Tools -> Scripts -> Gap Fill

1. Open Krita and open a document
2. Enable addon in Settings -> Configure Krita -> Python Plugin Manager -> check "Gap Fill", click OK
3. Select the paint layer or group layer containing your line art
	- If selecting a group layer, gaps will be filled as if everything inside the group is a single layer
4. Click "Gap Fill" in Tools -> Scripts
	- Process may take several seconds, don't do anything until it generates the "Gap Fill" layer
5. When the tool completes it will turn the line art layer(s) light gray and create a new "Gap Fill" layer with 1% opacity below it. (If you selected a group layer it will be in the group at the bottom)
	- you can change the opacity to 100% to check the success of the gap fill
	- use the paint tool to fill in any missed gaps
6. You can now fill in the line art on any layer by using the "Enclose and Fill Tool" with the following settings
	- What to fill: All regions
	- Adjustments:
		- set to -2 to -4 to prevent it from spilling outside the lines
	- Reference: Tag icon (Obtain the region using a merged copy of the selected color-labeled layers)
		- click the gray label color box


## Future improvements

- If lots of gaps are missed in real use cases, I may add a dialog box to choose gap distance
- Remove excessive screen refreshing to speed up process







































