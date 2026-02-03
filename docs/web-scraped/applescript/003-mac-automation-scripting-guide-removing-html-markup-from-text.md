# Mac Automation Scripting Guide: Removing HTML Markup from Text

## Removing HTML Markup from Text
When parsing HTML content, itâs often necessary to remove markup entirely. The handler inListing 34-1removes all HTML tags from the text provided, returning only the remaining textâthe contents of the tags.
APPLESCRIPT
Open in Script Editor
- on removeMarkupFromText(theText)
- set tagDetected to false
- set theCleanText to ""
- repeat with a from 1 to length of theText
- set theCurrentCharacter to character a of theText
- if theCurrentCharacter is "<" then
- set tagDetected to true
- else if theCurrentCharacter is ">" then
- set tagDetected to false
- else if tagDetected is false then
- set theCleanText to theCleanText & theCurrentCharacter as string
- end if
- end repeat
- return theCleanText
- end removeMarkupFromText
Listing 34-2shows how to call the handler inListing 34-1.
APPLESCRIPT
Open in Script Editor
- set theText to "<a href=\"http://www.apple.com/mac\">This is a <B>great</B> time to own a Mac!</a>"
- removeMarkupFromText(theText)
- --> Result: "This is a great time to own a Mac!"
Parsing HTML
Working with Property List Files
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13