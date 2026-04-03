# Mac Automation Scripting Guide: Parsing HTML

## Parsing HTML

The process of reading an HTML file is no different than the process of reading a standard text fileâseeReading a Fileto learn how to do it. However, itâs often necessary to extract specific bits of information from HTML files, such as links, images, and table data, for further processing.

### Parsing an HTML File

The handler inListing 33-1extracts specific tags and their content from HTML text. Provide an HTML file to read, a closing and ending tag, and indicate whether to return only content between the tags, or the tags with their enclosed content. If no closing tag is provided, the handler extracts the opening tag data only. This feature could be used to extract image tags from HTML content, for example, which donât have a separate closing tag.
APPLESCRIPT
Open in Script Editor

- on parseHTMLFile(theFile, theOpeningTag, theClosingTag, returnContentsOnly)
- try
- set theFile to theFile as string
- set theFile to open for access file theFile
- set theCombinedResults to ""
- set theCurrentOpeningTag to ""
- repeat
- read theFile before "<"
- set theCurrentTag to read theFile until ">"
- if theCurrentTag does not start with "<" then set theCurrentTag to ("<" & theCurrentTag) as string
- if theCurrentTag begins with theOpeningTag then
- set theCurrentOpeningTag to theCurrentTag
- if theClosingTag is "" then
- if theCombinedResults is "" then
- set theCombinedResults to theCombinedResults & theCurrentOpeningTag
- else
- set theCombinedResults to theCombinedResults & return & theCurrentOpeningTag
- end if
- else
- set theTextBuffer to ""
- repeat
- set theTextBuffer to theTextBuffer & (read theFile before "<")
- set theTagBuffer to read theFile until ">"
- if theTagBuffer does not start with "<" then set theTagBuffer to ("<" & theTagBuffer)
- if theTagBuffer is theClosingTag then
- if returnContentsOnly is false then
- set theTextBuffer to theCurrentOpeningTag & theTextBuffer & theTagBuffer
- end if
- if theCombinedResults is "" then
- set theCombinedResults to theCombinedResults & theTextBuffer
- else
- set theCombinedResults to theCombinedResults & return & theTextBuffer
- end if
- exit repeat
- else
- set theTextBuffer to theTextBuffer & theTagBuffer
- end if
- end repeat
- end if
- end if
- end repeat
- close access theFile
- on error theErrorMessage number theErrorNumber
- try
- close access theFile
- end try
- if theErrorNumber is not -39 then return false
- end try
- return theCombinedResults
- end parseHTMLFile
Listing 33-2shows how to call the handler inListing 33-1to extract all hyperlinks within a chosen HTML file.
APPLESCRIPT
Open in Script Editor

- set theFile to choose file with prompt "Select an HTML file:"
- parseHTMLFile(theFile, "<A HREF=", "</A>", false)
- --> Example of Result: "<A HREF="http://www.apple.com/fileA.html">Click here to view fileA.</A>
- <A HREF="http://www.apple.com/fileB.html">Click here to view fileB.</A>"
Listing 33-3shows how to call the handler inListing 33-1to extract the destinations of all hyperlinks within a chosen HTML file.
APPLESCRIPT
Open in Script Editor

- set theFile to choose file with prompt "Select an HTML file:"
- parseHTMLFile(theFile, "<A HREF=", "</A>", true)
- --> Example of Result: "Click here to view fileA.
- Click here to view fileB."
Listing 33-4shows how to call the handler inListing 33-1to extract all images within a chosen HTML file.
APPLESCRIPT
Open in Script Editor

- set theFile to choose file with prompt "Select an HTML file:"
- parseHTMLFile(theFile, "<IMG ", "", false)
- --> Example of Result: "<IMG SRC="gfx/clipboard.gif" BORDER="0">
- <IMG SRC="printer_stopped.gif" ALIGN=TOP WIDTH="32" HEIGHT="32" BORDER="0">
- <IMG SRC="printer_on.gif" ALIGN=TOP WIDTH="32" HEIGHT="32" BORDER="0">"
Listing 33-5shows how to call the handler inListing 33-1to extract any tables within a file.
APPLESCRIPT
Open in Script Editor

- set theFile to choose file with prompt "Select an HTML file:"
- parseHTMLFile(theFile, "<TABLE", "</TABLE>", false)
- --> Example of Result:"<TABLE WIDTH="440">
- <TR>
- <TD ALIGN="CENTER" VALIGN="TOP">
- <IMG SRC="gfx/clipboard.gif" BORDER="0">
- </TD>
- </TR>
- </TABLE>"

### Parsing an HTML Tag

The handler inListing 33-6extracts the contentsâfirst instance of text contained within quotesâof an HTML tag.
APPLESCRIPT
Open in Script Editor

- on parseHTMLTag(theHTMLTag)
- set AppleScript's text item delimiters to "\""
- set theHTMLTagElements to text items of theHTMLTag
- set AppleScript's text item delimiters to ""
- if length of theHTMLTagElements is greater than 1 then return item 2 of theHTMLTagElements
- return ""
- end parseHTMLTag
Listing 33-7shows how to call the handler inListing 33-6to extract the destination of a hyperlink tag.
APPLESCRIPT
Open in Script Editor

- set theHTMLTag to "<A HREF=\"http://www.apple.com/fileA.html\">Click here to view fileA.</A>"
- parseHTMLTag(theHTMLTag)
- --> Result: "http://www.apple.com/fileA.html"
Encoding and Decoding Text
Removing HTML Markup from Text
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13
