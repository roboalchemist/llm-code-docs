# Mac Automation Scripting Guide: Referencing Files and Folders

## Referencing Files and Folders

### Referencing Files and Folders in AppleScript
In AppleScript, file and folder paths are typically represented usingalias,file, andPOSIX fileobjects.
Note
Additional information about working with file and folder paths in AppleScript can be found inAliases and FilesinAppleScript Language Guide.

### Alias Objects
Analiasobject dynamically points to an existing item in the file system. Since an alias is dynamic, it continues pointing to the item even if the item is renamed or moved, the same way an alias file works when you manually create one in the Finder. With an AppleScript alias, the original item must exist at run time or an error will occur.
Analiasobject is displayed as a colon-delimited path preceded by analiasspecifier, in the format shown inListing 15-1.
APPLESCRIPT
Open in Script Editor
- alias "VolumeName:FolderName:SubfolderName:FileName"
Listing 15-2shows an example of analiasobject that references the Desktop folder.
APPLESCRIPT
Open in Script Editor
- alias "Macintosh HD:Users:yourUserName:Desktop:"
Listing 15-3is an example of analiasobject that references an existing file on the Desktop.
APPLESCRIPT
Open in Script Editor
- alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"
To create an alias, add the alias specifier prefix to a colon-delimited path string, as shown inListing 15-4.
APPLESCRIPT
Open in Script Editor
- set thePath to alias "Macintosh HD:Users:yourUserName:Desktop:"
Many commands accept an alias as a parameter and/or return an alias as a result. InListing 15-5, thechoose filecommand accepts a folderaliasobject in itsdefault locationparameter. The command then returns analiasobject that points to the chosen file.
APPLESCRIPT
Open in Script Editor
- set theDefaultFolder to alias "Macintosh HD:Users:yourUserName:Desktop:"
- choose file default location theDefaultFolder
- --> Result: alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"

### File Objects
Afileobject is a static reference to an item at a specific location in the file system. Itâs not dynamic, and can even refer to an item that doesnât exist yet. For example, asavecommand may accept a file reference when saving to a new file.
Afileobject is displayed as a colon-delimited path preceded by afilespecifier, in the format shown inListing 15-6.
APPLESCRIPT
Open in Script Editor
- file "VolumeName:FolderName:SubfolderName:FileName"
Listing 15-7shows an example of afileobject that references a file that may or may not exist on the Desktop.
APPLESCRIPT
Open in Script Editor
- file "Macintosh HD:Users:yourUserName:Desktop:My File.txt"
Unlike the way analiasobject works, you canât create afileobject simply by prefixing a path string with thefilespecifier. For example,Listing 15-7errors when run within a script.
APPLESCRIPT
Open in Script Editor
- set theFile to file "Macintosh HD:Users:yourUserName:Desktop:My File.txt"
Instead, you must prefix the path with thefilespecifier at the time the file is targeted by a command, as shown inListing 15-8.
APPLESCRIPT
Open in Script Editor
- set theFile to "Macintosh HD:Users:yourUserName:Desktop:My File.txt"
- read file theFile
Note
Afileobject can refer to either a file or a folder, despite thefilespecifier prefix.

### POSIX File Objects
Some scriptable apps are designed to work with POSIX-style paths, rather than AppleScriptaliasandfileobjects. Like afileobject, aPOSIX fileobject is not dynamic and can also refer to an item that doesnât exist yet.
APOSIX fileobject is displayed as a slash-delimited path preceded by aPOSIX filespecifier, in the format shown inListing 15-10.
APPLESCRIPT
Open in Script Editor
- POSIX file "/FolderName/SubfolderName/FileName"
Listing 15-11is an example of aPOSIX fileobject that references a file that may or may not exist on the Desktop.
APPLESCRIPT
Open in Script Editor
- POSIX file "/Users/yourUserName/Desktop/My File.txt"
Note
APOSIX fileobject can refer to either a file or a folder, despite thePOSIX filespecifier prefix.
In a POSIX path, the startup diskâs name is omitted and represented by a leading slash. Other disks are referenced in relation to theVolumesdirectory of the startup disk, for example:/Volumes/DiskName/FolderName/SubFolderName/FileName.

### App-Specific References to Files and Folders
Some apps, such as the Finder and System Events, have their own syntax for referring to files and folders.Listing 15-12shows how a Finder file reference appears.
APPLESCRIPT
Open in Script Editor
- document file "My File.txt" of folder "Desktop" of folder "yourUserName" of folder "Users" of startup disk of application "Finder"
Listing 15-13shows how a System Events folder reference appears.
APPLESCRIPT
Open in Script Editor
- folder "Macintosh HD:Users:yourUserName:Desktop:" of application "System Events"
Since this terminology is app-specific, it doesnât work in other apps. For example, you canât write a script that tries to import a Finder reference to an audio file into iTunes because iTunes doesnât understand Finder file references. In this case, you must coerce the Finder file reference to something iTunes can understand, like an alias. SeeConverting Between Path Formatsbelow. In most cases, apps with their own path syntax also support standard AppleScript path types.

### Converting Between Path Formats
Since different situations may result in paths appearing in different formats, you may need to regularly convert one path format to another. Sometimes, this can be done by using theascoercion operator, as shown inListing 15-14,Listing 15-15,Listing 15-16, andListing 15-17.
APPLESCRIPT
Open in Script Editor
- set theFilePath to "Macintosh HD:Users:yourUserName:Desktop:My File.txt"
- set theFilePath to theFilePath as alias
- --> Result: alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"
APPLESCRIPT
Open in Script Editor
- set theFilePath to choose file
- --> Result: alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"
- set theFilePath to theFilePath as string
- --> Result: "Macintosh HD:Users:yourUserName:Desktop:My File.txt"
APPLESCRIPT
Open in Script Editor
- set theFilePath to POSIX file "/Users/yourUserName/Desktop/My File.txt"
- set theFilePath to theFilePath as alias
- --> Result: alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"
APPLESCRIPT
Open in Script Editor
- tell application "Finder"
- set theFilePath to file "My File.txt" of desktop
- end tell
- --> Result: document file "My File.txt" of folder "Desktop" of folder "yourUserName" of folder "Users" of startup disk of application "Finder"
- set theFilePath to theFilePath as alias
- --> Result: alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"
Converting from a string or alias to a POSIX path canât be done through coercion. Instead, you must access thePOSIX pathproperty of the path to convert, as shown inListing 15-18.
APPLESCRIPT
Open in Script Editor
- set theFilePath to choose file
- --> Result: alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"
- set theFilePath to POSIX path of theFilePath
- --> Result: "/Users/yourUserName/Desktop/My File.txt"

### Using Conversion Handlers
Running paths through a conversion handler is a good way to ensure the format you expect.

### Converting a Path to an Aliases
The handler inListing 15-19converts strings,pathobjects,POSIX fileobjects, Finder paths, and System Events paths toaliasformat.
APPLESCRIPT
Open in Script Editor
- on convertPathToAlias(thePath)
- tell application "System Events"
- try
- return (path of disk item (thePath as string)) as alias
- on error
- return (path of disk item (path of thePath) as string) as alias
- end try
- end tell
- end convertPathToAlias
Listing 15-19shows how to call the handler inListing 15-19to convert a POSIX-style path string to an alias.
APPLESCRIPT
Open in Script Editor
- set thePath to "/Users/yourUserName/Desktop/My File.txt"
- set thePath to convertPathToAlias(thePath)
- --> Result: alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"

### Converting a Path to a String
The handler inListing 15-21converts a path to string format.
APPLESCRIPT
Open in Script Editor
- on convertPathToString(thePath)
- tell application "System Events"
- try
- return path of disk item (thePath as string)
- on error
- return path of thePath
- end try
- end tell
- end convertPathToString
Listing 15-22shows how to call the handler inListing 15-21to convert an alias to a path string.
APPLESCRIPT
Open in Script Editor
- set thePath to alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"
- set thePath to convertPathToString(thePath)
- --> Result: "Macintosh HD:Users:yourUserName:Desktop:My File.txt"

### Converting a Path to a POSIX Path String
The handler inListing 15-23converts a path to POSIX path string format.
APPLESCRIPT
Open in Script Editor
- on convertPathToPOSIXString(thePath)
- tell application "System Events"
- try
- set thePath to path of disk item (thePath as string)
- on error
- set thePath to path of thePath
- end try
- end tell
- return POSIX path of thePath
- end convertPathToPOSIXString
Listing 15-24shows how to call the handler inListing 15-23to convert an alias to a path string.
APPLESCRIPT
Open in Script Editor
- set thePath to alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"
- set thePath to convertPathToPOSIXString(thePath)
- --> Result: "/Users/yourUserName/Desktop/My File.txt"

### Referencing Files and Folders in JavaScript
In JavaScript, file and folder paths are represented usingPathobjects.
To create a path, pass a POSIX-style string to thePathobject, as shown inListing 15-25.
JAVASCRIPT
- Path("/FolderName/SubfolderName/FileName")
To convert a path to a string, call thetoString()method on the path, as shown inListing 15-26.
JAVASCRIPT
Open in Script Editor
- var path = Path("/Users/yourUserName/Desktop/My File.txt")
- var string = path.toString()
- string
- // Result: "/Users/yourUserName/Desktop/My File.txt"
Using Script Libraries
Reading and Writing Files
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13