# Mac Automation Scripting Guide: Manipulating Text

## Manipulating Text
Manipulating text is one of the most common tasks performed in scripts. AppleScript and JavaScript both possess some basic text manipulation functions and properties that allow you to concatenate text, get the length of a string, and more. Overall, JavaScript has a much wider-range of built-in language-level text manipulation functions. Custom scripting is usually required to manipulate text with AppleScript.
Note
For general information about working with text in AppleScript, see thetextclass reference documentation inAppleScript Language Guide.
In JavaScript, theStringobject provides a range of text processing functions. Information about this object can be foundhere. JavaScript also provides aRegExpconstructor, which can be used for pattern matching. Information about this constructor can be foundhere.

### Changing the Case of Text
The handlers inListing 19-1andListing 19-2convert text to uppercase or lowercase. To use these handlers, provide some source text and a case to applyâupperorlower.
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
Listing 19-3andListing 19-4show how to call the handlers inListing 19-1andListing 19-2to convert text to uppercase.
APPLESCRIPT
Open in Script Editor
- changeCaseOfText("scripting is awesome!", "upper")
- --> Result: "SCRIPTING IS AWESOME!"
JAVASCRIPT
Open in Script Editor
- changeCaseOfText("scripting is awesome!", "upper")
- // Result: "SCRIPTING IS AWESOME!"
Listing 19-5andListing 19-6show how to call the handlers inListing 19-1andListing 19-2to convert text to lowercase.
APPLESCRIPT
Open in Script Editor
- changeCaseOfText("DOING REPETITIVE WORK IS BORING", "lower")
- --> Result: "doing repetitive work is boring"
JAVASCRIPT
Open in Script Editor
- changeCaseOfText("DOING REPETITIVE WORK IS BORING", "lower")
- // Result: "doing repetitive work is boring"
Note
When you use AppleScriptObjC or JavaScriptObjC, you can use methods of theNSStringclass to change the case of text.Listing 19-7andListing 19-8demonstrate how to do this.
APPLESCRIPT
Open in Script Editor
- use framework "Foundation"
- on changeCaseOfText(theText, theCase)
- -- Create an NSString object from the passed text
- set theText to stringWithString_(theText) of NSString of current application
- -- Apply the appropriate transformation to the NSString object
- if theCase contains "lower" then
- set theNewText to lowercaseString() of theText
- else if theCase contains "upper" then
- set theNewText to uppercaseString() of theText
- else
- set theNewText to capitalizedString() of theText
- end if
- -- Convert the NSString to an AppleScript string
- return (theNewText as string)
- end changeCaseOfText
JAVASCRIPT
Open in Script Editor
- function changeCaseOfText(text, caseToSwitchTo) {
- // Convert the passed text to an NSString object
- var alteredText = $(text)
- // Apply the appropriate transformation to the NSString object
- if (caseToSwitchTo === "lower") {
- alteredText = alteredText.lowercaseString
- }
- else if (caseToSwitchTo === "upper") {
- alteredText = alteredText.uppercaseString
- }
- // Convert the NSString to an AppleScript string
- return alteredText.js
- }

### Finding and Replacing Text in a String
The handler inListing 19-9can be used to find and replace text in a string. To use it, provide some source text, a string to find, and a replacement string. This handler replaces any found instances of the specified search string.
APPLESCRIPT
Open in Script Editor
- on findAndReplaceInText(theText, theSearchString, theReplacementString)
- set AppleScript's text item delimiters to theSearchString
- set theTextItems to every text item of theText
- set AppleScript's text item delimiters to theReplacementString
- set theText to theTextItems as string
- set AppleScript's text item delimiters to ""
- return theText
- end findAndReplaceInText
Listing 19-10shows how to call the handler inListing 19-9.
APPLESCRIPT
Open in Script Editor
- set theText to "On Tuesday, I told you to have the report ready by next Tuesday."
- set theText to findAndReplaceInText(theText, "Tuesday", "Friday")
- --> Result: "On Friday, I told you to have the report ready by next Friday."
In JavaScript, theStringobjectâsreplace()method is used to find and replace text in a string, as shown inListing 19-11. Unlike the previous AppleScript example, this function replaces only the first occurrence of the found text.
JAVASCRIPT
Open in Script Editor
- var text = "On Tuesday, I told you to have the report ready by next Tuesday."
- text = text.replace("Tuesday", "Friday")
- // Result: "On Friday, I told you to have the report ready by next Tuesday."
Thereplace()method can be combined with a regular expression to replace every occurrence of the found text, as shown inListing 19-12.
JAVASCRIPT
Open in Script Editor
- var text = "On Tuesday, I told you to have the report ready by next Tuesday."
- text = text.replace(/Tuesday/g, "Friday")
- // Result: "On Friday, I told you to have the report ready by next Friday."
Note
When you use AppleScriptObjC or JavaScriptObjC, you can use methods of theNSStringclass to perform a find and replace in text. The handlers inListing 19-13andListing 19-14demonstrate how to do this.
APPLESCRIPT
Open in Script Editor
- use framework "Foundation"
- on findAndReplaceInText(theText, theSearchString, theReplacementString)
- -- Create an NSString object from the passed AppleScript string
- set theText to stringWithString_(theText) of NSString of current application
- -- Call an NSString replacement method on the newly created NSString object
- set theText to stringByReplacingOccurrencesOfString_withString_(theSearchString, theReplacementString) of theText
- -- Convert from an NSString to an AppleScript string
- return (theText as string)
- end findAndReplaceInText
JAVASCRIPT
Open in Script Editor
- function findAndReplaceInText(text, searchString, replacementString) {
- // Create an NSString object from the passed string
- var alteredText = $(text)
- // Call an NSString replacement method on the newly created NSString object
- alteredText = alteredText.stringByReplacingOccurrencesOfStringWithString(searchString, replacementString)
- // Convert from an NSString to a JavaScript string
- return alteredText.js
- }

### Getting the Characters of a String
Listing 19-15andListing 19-16show how to get a list of characters in a string.
APPLESCRIPT
Open in Script Editor
- set theText to "The quick brown fox jumps over a lazy dog."
- characters of theText
- --> Result: {"T", "h", "e", " ", "q", "u", "i", "c", "k", " ", "b", "r", "o", "w", "n", " ", "f", "o", "x", " ", "j", "u", "m", "p", "s", " ", "o", "v", "e", "r", " ", "a", " ", "l", "a", "z", "y", " ", "d", "o", "g", "."}
JAVASCRIPT
Open in Script Editor
- var text = "The quick brown fox jumps over a lazy dog."
- text.split("")
- // Result: ["T", "h", "e", " ", "q", "u", "i", "c", "k", " ", "b", "r", "o", "w", "n", " ", "f", "o", "x", " ", "j", "u", "m", "p", "s", " ", "o", "v", "e", "r", " ", "a", " ", "l", "a", "z", "y", " ", "d", "o", "g", "."]

### Getting the Length of String
Listing 19-17andListing 19-18show how to get the length ofâthe number of characters inâa string.
APPLESCRIPT
Open in Script Editor
- set theText to "The quick brown fox jumps over a lazy dog."
- length of theText
- --> Result: 42
JAVASCRIPT
Open in Script Editor
- var text = "The quick brown fox jumps over a lazy dog."
- text.length
- // Result: 42

### Getting the Paragraphs of a String
Listing 19-19andListing 19-20show how to get a list of paragraphs in a string.
APPLESCRIPT
Open in Script Editor
- set theText to "* Sal
- * Ben
- * Chris
- * David"
- paragraphs of theText
- --> Result: {"* Sal", "* Ben", "* Chris", "* David"}
JAVASCRIPT
Open in Script Editor
- var text = `* Sal
- * Ben
- * Chris
- * David`
- text.split("\n")
- // Result: ["* Sal", "* Ben", "* Chris", "* David"]

### Getting the Position of Text in a String
To determine the position of text within a string in AppleScript, request itsoffset, as shown inListing 19-21. This provides the character number where the first instance of the text begins.
APPLESCRIPT
Open in Script Editor
- set theText to "The quick brown fox jumps over a lazy dog."
- offset of "quick" in theText
- --> Result: 5
Note
In AppleScript, character positions start at1; the first character in a string has an offset of1. If the string doesnât include the text provided, then an offset of0is returned.
To determine the position of text within a string in JavaScript, call theindexOf()method of the text object, as shown inListing 19-22.
JAVASCRIPT
Open in Script Editor
- var text = "The quick brown fox jumps over a lazy dog."
- text.indexOf("quick")
- // Result: 4
Note
In JavaScript, character positions start at0; the first character in a string has an index of0. If the string doesnât include the text provided, then an offset of-1is returned.

### Splitting Text
The handler inListing 19-23splits text into a list, based on a specific delimiter.
APPLESCRIPT
Open in Script Editor
- on splitText(theText, theDelimiter)
- set AppleScript's text item delimiters to theDelimiter
- set theTextItems to every text item of theText
- set AppleScript's text item delimiters to ""
- return theTextItems
- end splitText
Listing 19-24shows how to call the handler inListing 19-23.
APPLESCRIPT
Open in Script Editor
- set theText to "The quick brown fox jumps over a lazy dog."
- splitText(theText, space)
- --> Result: {"The", "quick", "brown", "fox", "jumps", "over", "a", "lazy", "dog."}
In JavaScript, theStringobjectâssplit()method is used to split text based on a delimiter, as shown inListing 19-25.
JAVASCRIPT
Open in Script Editor
- var text = "The quick brown fox jumps over a lazy dog."
- text.split(" ")
- // Result: ["The", "quick", "brown", "fox", "jumps", "over", "a", "lazy", "dog."]
Note
SeeConverting a List to a Stringto learn how to merge strings back together.

### Trimming Text
The handlers inListing 19-26andListing 19-27trim text from the beginning or end of a string. To use these examples, provide some source text, characters to trim, and a trim directionâbeginning(trim from the beginning),end(trim from the end), orboth(trim from both the beginning and end).
APPLESCRIPT
Open in Script Editor
- on trimText(theText, theCharactersToTrim, theTrimDirection)
- set theTrimLength to length of theCharactersToTrim
- if theTrimDirection is in {"beginning", "both"} then
- repeat while theText begins with theCharactersToTrim
- try
- set theText to characters (theTrimLength + 1) thru -1 of theText as string
- on error
- -- text contains nothing but trim characters
- return ""
- end try
- end repeat
- end if
- if theTrimDirection is in {"end", "both"} then
- repeat while theText ends with theCharactersToTrim
- try
- set theText to characters 1 thru -(theTrimLength + 1) of theText as string
- on error
- -- text contains nothing but trim characters
- return ""
- end try
- end repeat
- end if
- return theText
- end trimText
JAVASCRIPT
Open in Script Editor
- function trimText(text, charsToTrim, direction) {
- var result = text
- var regexString = charsToTrim.replace(/[\-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|]/g, "\\$&");
- if (direction === "beginning" || direction === "both") {
- var regex = new RegExp(`^(?:${regexString})*`)
- result = result.replace(regex, "")
- }
- if (direction === "end" || direction === "both") {
- var regex = new RegExp(`(?:${regexString})*$`)
- result = result.replace(regex, "")
- }
- return result
- }
Listing 19-28andListing 19-29show how to call the handlers inListing 19-26andListing 19-27to trim text from the beginning of a string.
APPLESCRIPT
Open in Script Editor
- trimText("----1----", "-", "beginning")
- --> Result: "1----"
JAVASCRIPT
Open in Script Editor
- trimText("----1----", "-", "beginning")
- // Result: "1----"
Listing 19-30andListing 19-31show how to call the handlers inListing 19-26andListing 19-27to trim text from the end of a string.
APPLESCRIPT
Open in Script Editor
- trimText("12345.txt", ".txt", "end")
- --> Result: "12345"
JAVASCRIPT
Open in Script Editor
- trimText("12345.txt", ".txt", "end")
- // Result: "12345"
Listing 19-32andListing 19-33show how to call the handlers inListing 19-26andListing 19-27to trim text from the beginning and end of a string.
APPLESCRIPT
Open in Script Editor
- trimText("*-*-Ben*-*-", "*-", "both")
- --> Result: "Ben"
JAVASCRIPT
Open in Script Editor
- trimText("*-*-Ben*-*-", "*-", "both")
- // Result: "Ben"
Note
When you use AppleScriptObjC or JavaScriptObjC, you can use methods of theNSStringclass to remove whitespace around text. The handlers inListing 19-34andListing 19-35demonstrate how to do this.
APPLESCRIPT
Open in Script Editor
- use framework "Foundation"
- on trimWhiteSpaceAroundString(theText)
- -- Create an NSString object from an AppleScript string
- set theText to stringWithString_(theText) of NSString of current application
- -- Trim white space around the NSString
- set theWhitespaceCharacterSet to whitespaceCharacterSet of NSCharacterSet of current application
- set theText to stringByTrimmingCharactersInSet_(theWhitespaceCharacterSet) of theText
- -- return result coerced to an AppleScript string
- return (theText as string)
- end trimWhiteSpaceAroundString
JAVASCRIPT
Open in Script Editor
- function trimWhiteSpaceAroundString(text) {
- // Create an NSString object from the text
- var alteredText = $(text)
- // Trim white space around the NSString and return the result
- var whitespace = $.NSCharacterSet.whitespaceCharacterSet
- return alteredText.stringByTrimmingCharactersInSet(whitespace).js
- }

### Trimming Paragraphs of Text
The handlers inListing 19-36andListing 19-37remove unwanted characters from multiple paragraphs.
Note
This handler calls thetrimText()handler. SeeListing 19-26.
APPLESCRIPT
Open in Script Editor
- on trimParagraphsOfText(theText, theCharactersToTrim, theTrimDirection)
- set theParagraphs to every paragraph of theText
- repeat with a from 1 to count of paragraphs of theText
- set theCurrentParagraph to item a of theParagraphs
- set item a of theParagraphs to trimText(theCurrentParagraph, theCharactersToTrim, theTrimDirection)
- end repeat
- set AppleScript's text item delimiters to return
- set theText to theParagraphs as string
- set AppleScript's text item delimiters to ""
- return theText
- end trimParagraphsOfText
JAVASCRIPT
Open in Script Editor
- function trimParagraphsOfText(text, charsToTrim, direction) {
- var paragraphs = text.split("\n")
- for (var i = 0; i < paragraphs.length; i++) {
- var currentParagraph = paragraphs[i]
- paragraphs[i] = trimText(currentParagraph, charsToTrim, direction)
- }
- return paragraphs.join("\n")
- }
Listing 19-38andListing 19-39show how to call the handlers inListing 19-36andListing 19-37.
APPLESCRIPT
Open in Script Editor
- set theText to "* Sal
- * Ben
- * Chris
- * David"
- trimParagraphsOfText(theText, "* ", "beginning")
- --> Result:
- (*
- "Sal
- Ben
- Chris
- David"
- *)
JAVASCRIPT
Open in Script Editor
- var text = `* Sal
- * Ben
- * Chris
- * David`
- trimParagraphsOfText(text, "* ", "beginning")
- // Result: "Sal\nBen\nChris\nDavid"
Note
In JavaScript,\nrepresents a newline character.
Watching Folders
Manipulating Numbers
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13