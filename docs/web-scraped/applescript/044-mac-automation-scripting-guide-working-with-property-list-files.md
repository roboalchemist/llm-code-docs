# Mac Automation Scripting Guide: Working with Property List Files

## Working with Property List Files
Many apps store settings in property list files (also called plists). Scripts can also store and retrieve data in plists. The terminology for interacting with plists is found in the Property List Suite of the System Events scripting dictionary (seeFigure 35-1).

### Creating a New Property List File
Listing 35-1demonstrates how to create a new property list file. First, an empty plist file (classproperty list file) is created. Next, individual property list items (classproperty list item) of varying type (Boolean, date, list, number, record, string) are added to the file.
APPLESCRIPT
Open in Script Editor
- tell application "System Events"
- -- Create an empty property list dictionary item
- set theParentDictionary to make new property list item with properties {kind:record}
- -- Create a new property list file using the empty dictionary list item as contents
- set thePropertyListFilePath to "~/Desktop/Example.plist"
- set thePropertyListFile to make new property list file with properties {contents:theParentDictionary, name:thePropertyListFilePath}
- -- Add a Boolean key
- tell property list items of thePropertyListFile
- make new property list item at end with properties {kind:boolean, name:"booleanKey", value:true}
- -- Add a date key
- make new property list item at end with properties {kind:date, name:"dateKey", value:current date}
- -- Add a list key
- make new property list item at end with properties {kind:list, name:"listKey"}
- -- Add a number key
- make new property list item at end with properties {kind:number, name:"numberKey", value:5}
- -- Add a record/dictionary key
- make new property list item at end with properties {kind:record, name:"recordKey"}
- -- Add a string key
- make new property list item at end with properties {kind:string, name:"stringKey", value:"string value"}
- end tell
- end tell
Listing 35-2shows the contents of a property list file created by the script inListing 35-1.
- <?xml version="1.0" encoding="UTF-8"?>
- <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
- <plist version="1.0">
- <dict>
- <key>booleanKey</key>
- <true/>
- <key>dateKey</key>
- <date>2016-01-28T19:34:13Z</date>
- <key>listKey</key>
- <array/>
- <key>numberKey</key>
- <integer>5</integer>
- <key>recordKey</key>
- <dict/>
- <key>stringKey</key>
- <string>string value</string>
- </dict>
- </plist>

### Reading a Property List Key Value
Listing 35-3shows how to read a value of a key in a property list file.
Open in Script Editor
- tell application "System Events"
- tell property list file thePropertyListFilePath
- return value of property list item "stringKey"
- end tell
- end tell
- --> Result: "string value"

### Changing a Property List Key Value
Listing 35-4shows how to change the value of a key in a property list file.
Open in Script Editor
- tell application "System Events"
- tell property list file thePropertyListFilePath
- set value of property list item "stringKey" to "new string value"
- end tell
- end tell

### Adding a New Property List Item
Listing 35-3shows how to add a new key and value to a property list file.
Open in Script Editor
- tell application "System Events"
- tell property list items of property list file thePropertyListFilePath
- make new property list item at end with properties {kind:string, name:"newStringKey", value:"new string value"}
- end tell
- end tell
Removing HTML Markup from Text
Working with XML
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13