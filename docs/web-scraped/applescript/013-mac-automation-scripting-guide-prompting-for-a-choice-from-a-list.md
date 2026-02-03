# Mac Automation Scripting Guide: Prompting for a Choice from a List

## Prompting for a Choice from a List

Use the Standard Additions scripting additionâschoose from listcommand to prompt the user to select from a list of strings.Listing 28-1andListing 28-2ask the user to select a favorite fruit, as seen inFigure 28-1.
APPLESCRIPT
Open in Script Editor

- set theFruitChoices to {"Apple", "Banana", "Orange"}
- set theFavoriteFruit to choose from list theFruitChoices with prompt "Select your favorite fruit:" default items {"Apple"}
- theFavoriteFruit
- --> Result: {"Apple"}
JAVASCRIPT
Open in Script Editor

- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var fruitChoices = ["Apple", "Banana", "Orange"]
- var favoriteFruit = app.chooseFromList(fruitChoices, {
- withPrompt: "Select your favorite fruit:",
- defaultItems: ["Apple"]
- })
- favoriteFruit
- // Result: ["Apple"]
Thechoose from listcommand can optionally let the user choose multiple items by setting themultiple selections allowedparameter totrue. For this reason, the result of the command is always a list of selected strings. This list may be empty if theempty selection allowedparameter has been specified and the user dismissed the dialog without making a selection.
Prompting for a File Name
Prompting for a Color
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13
