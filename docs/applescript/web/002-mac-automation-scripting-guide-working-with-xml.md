# Mac Automation Scripting Guide: Working with XML

## Working with XML

The XML Suite of the System Events scripting dictionary defines several classes that make it quick and easy to read and parse XML data. TheXML fileclass represents any text file containing structured XML like the example data shown inListing 36-1.

- <books>
- <book country="US">
- <name>The Secret Lives of Cats</name>
- <publisher>Feline Press</publisher>
- </book>
- </books>

At the top level, an XML file contains anXML dataobject thatâs comprised of nestedXML elementobjects. EachXML elementobject has anameand avalueproperty, and may also containXML attributeobjects that define additional metadata. The example code inListing 36-2demonstrates how to access these classes to read and parse the contents of an XML file on the Desktop that contains the XML data fromListing 36-1.
APPLESCRIPT
Open in Script Editor

- tell application "System Events"
- tell XML file "~/Desktop/Book Data.xml"
- tell XML element "books"
- set theBookElements to every XML element whose name = "book"
- --> {XML element 1 of XML element 1 of contents of XML file "Macintosh HD:Users:YourUserName:Desktop:Book Data.xml" of application "System Events"}
- repeat with a from 1 to length of theBookElements
- set theCurrentBookElement to item a of theBookElements
- --> XML element 1 of XML element 1 of contents of XML file "Macintosh HD:Users:YourUserName:Desktop:Book Data.xml" of application "System Events"
- tell theCurrentBookElement
- name of theCurrentBookElement
- --> "book"
- name of every XML element
- --> {"name", "publisher"}
- name of every XML attribute
- --> {"country"}
- value of every XML attribute
- --> {"US"}
- set theBookName to value of XML element "name"
- --> "The Secret Lives of Cats"
- set thePublisher to value of XML element "publisher"
- --> "Feline Press"
- end tell
- end repeat
- end tell
- end tell
- end tell
Working with Property List Files
Automating the User Interface
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13
