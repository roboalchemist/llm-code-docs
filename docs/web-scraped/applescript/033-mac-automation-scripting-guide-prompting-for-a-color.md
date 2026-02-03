# Mac Automation Scripting Guide: Prompting for a Color

## Prompting for a Color
Use the Standard Additions scripting additionâschoose colorcommand to ask the user to select a color from a color picker dialog like the one shown inFigure 29-1. The command accepts an optionaldefault colorparameter, and produces an RGB color value as its result.Listing 29-1andListing 29-2display a color picker, create a TextEdit document containing some text, and apply the chosen color to the text.
APPLESCRIPT
Open in Script Editor
- set theColor to choose color default color {0, 65535, 0}
- --> Result: {256, 40421, 398}
- tell application "TextEdit"
- set theDocument to make new document
- set text of document 1 to "Colored Text"
- set color of text of document 1 to theColor
- end tell
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var color = app.chooseColor({defaultColor: [0, 1, 0]})
- // Result: [0.003753719385713339, 0.7206835746765137, 0.005828946363180876]
- color = [Math.trunc(color[0] * 65535), Math.trunc(color[1] * 65535), Math.trunc(color[2] * 65535)]
- var textedit = Application("TextEdit")
- var document = textedit.make({new: "document"})
- document.text = "Colored Text"
- document.text.color = [256, 40421, 398]
Note
In AppleScript, thechoose colorcommand produces RGB values ranging from0through65535. In JavaScript, the RGB values range between0and1. These values must be converted to match the AppleScript values to be used.Listing 29-2demonstrates this conversion.
Prompting for a Choice from a List
Displaying Progress
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13