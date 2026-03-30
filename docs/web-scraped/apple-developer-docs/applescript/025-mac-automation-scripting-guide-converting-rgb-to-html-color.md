# Mac Automation Scripting Guide: Converting RGB to HTML Color

## Converting RGB to HTML Color

In HTML documents, colors are typically represented as hex values. The handlers inListing 31-1andListing 31-2show how to convert 8-bit or 256 color-based RGB values to hex values. Provide an RGB color represented by a list of three numbers, each with a value between0and65535.
APPLESCRIPT
Open in Script Editor

- on convertRGBColorToHexValue(theRGBValues)
- set theHexList to {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"}
- set theHexValue to ""
- repeat with a from 1 to count of theRGBValues
- set theCurrentRGBValue to (item a of theRGBValues) div 256
- if theCurrentRGBValue is 256 then set theCurrentRGBValue to 255
- set theFirstItem to item ((theCurrentRGBValue div 16) + 1) of theHexList
- set theSecondItem to item (((theCurrentRGBValue / 16 mod 1) * 16) + 1) of theHexList
- set theHexValue to (theHexValue & theFirstItem & theSecondItem) as string
- end repeat
- return ("#" & theHexValue) as string
- end convertRGBColorToHexValue
JAVASCRIPT
Open in Script Editor

- function convertRGBColorToHexValue(rgbValues) {
- var r = parseInt(rgbValues[0], 10).toString(16).slice(-2)
- if (r.length == 1)
- r = "0" + r
- var g = parseInt(rgbValues[1], 10).toString(16).slice(-2)
- if (g.length == 1)
- g = "0" + g
- var b = parseInt(rgbValues[2], 10).toString(16).slice(-2)
- if (b.length == 1)
- b = "0" + b
- return ("#" + r + g + b)
- }
Listing 31-3shows how to call the handlers inListing 31-1to convert a specified RGB color to a hex value for use in HTML.
APPLESCRIPT
Open in Script Editor

- set theRGBValues to (choose color default color {65535, 0, 0})
- convertRGBColorToHexValue(theRGBValues)
- --> Result: "#FF0000"
JAVASCRIPT
Open in Script Editor

- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var color = app.chooseColor({defaultColor: [1, 0, 0]})
- color = [Math.trunc(color[0] * 65535), Math.trunc(color[1] * 65535), Math.trunc(color[2] * 65535)]
- convertRGBColorToHexValue(color)
- // Result: "#FF0000"
Note
In AppleScript, thechoose colorcommand produces RGB values ranging from0through65535. In JavaScript, the RGB values range between0and1. These values must be converted to match the AppleScript values to be used.Listing 31-4demonstrates this conversion.
Displaying Progress
Encoding and Decoding Text
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13
