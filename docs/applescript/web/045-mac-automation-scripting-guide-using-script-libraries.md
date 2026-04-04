# Mac Automation Scripting Guide: Using Script Libraries

## Using Script Libraries

A script library is a collection of handlers, which can be loaded and used by other scripts. For example, a scripter might compile a set of commonly-used text-processing handlers into a text library. This library could then be shared by multiple scripts that need to perform text processing operations.

### Writing Script Libraries

To write a script library, create a Script Editor document that contains one or more handlers, such as the one shown inListing 14-1andListing 14-2, and save it inscriptformat, as shown inFigure 14-1.
APPLESCRIPT
Open in Script Editor

- on changeCaseOfText(theText, theCaseToSwitchTo)
- if theCaseToSwitchTo contains "lower" then
- set theComparisonCharacters to "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
- set theSourceCharacters to "abcdefghijklmnopqrstuvwxyz"
- else if theCaseToSwitchTo contains "upper" then
- set theComparisonCharacters to "abcdefghijklmnopqrstuvwxyz"
- set theSourceCharacters to "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
- else
- return theText
- end if
- set theAlteredText to ""
- repeat with aCharacter in theText
- set theOffset to offset of aCharacter in theComparisonCharacters
- if theOffset is not 0 then
- set theAlteredText to (theAlteredText & character theOffset of theSourceCharacters) as string
- else
- set theAlteredText to (theAlteredText & aCharacter) as string
- end if
- end repeat
- return theAlteredText
- end changeCaseOfText
JAVASCRIPT
Open in Script Editor

- function changeCaseOfText(text, caseToSwitchTo) {
- var alteredText = text
- if (caseToSwitchTo === "lower") {
- alteredText = alteredText.toLowerCase()
- }
- else if (caseToSwitchTo === "upper") {
- alteredText = alteredText.toUpperCase()
- }
- return alteredText
- }
Move the saved script to one of the following folders on your Mac, creating the folder if it doesnât already exist:

- ~/Library/Script Libraries/
~/Library/Script Libraries/

- /Library/Script Libraries/
/Library/Script Libraries/

- /Resources/folder inside a script or app bundle.
/Resources/folder inside a script or app bundle.
For additional information about writing script libraries, seeCreating a LibraryinAppleScript Language GuideandLibrariesinJavaScript for Automation Release Notes.

### Using Script Libraries

Once a script library is installed, your other scripts can target its handlers at any time.
To target a script library in AppleScript, use atellstatement, as shown inListing 14-3.
APPLESCRIPT
Open in Script Editor

- tell script "My Text Processor"
- changeCaseOfText("scripting is awesome!", "upper")
- end tell
- --> Result: "SCRIPTING IS AWESOME!"
To target a script library in JavaScript, use theLibrarycommand to reference the library. Then, you can target handlers in the referenced library, as shown inListing 14-4.
JAVASCRIPT
Open in Script Editor

- textProcessor = Library("My Text Processor")
- textProcessor.changeCaseOfText("scripting is awesome!", "upper")
- // Result: "SCRIPTING IS AWESOME!"
Using Handlers/Functions
Referencing Files and Folders
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13