# Mac Automation Scripting Guide: Processing Dropped Files and Folders

## Processing Dropped Files and Folders

Droplets are applets configured to process dropped files and folders. A droplet is distinguishable from a normal applet because its icon includes a downward pointing arrow, as shown inFigure 17-1.
To create an AppleScript droplet, include anopenevent handler in your script and save the script as an application. To create a JavaScript droplet, include anopenDocumentsfunction in your script and save the script as an application. The presence of this handler or function automatically renders the saved application as a droplet, allowing it to accept dropped files and folders in the Finder. Theopenhandler andopenDocumentsfunction accept a single parameterâa list of dropped files or foldersâwhich are passed to the handler when the script is activated by dropping something onto it. In AppleScript, these dropped files and folders arealiasobjects. In JavaScript, theyârePathobjects. For more information about these types of objects, seeReferencing Files and Folders.
An AppleScriptopenhandler is formatted as shown inListing 17-1.
APPLESCRIPT
Open in Script Editor

- on open theDroppedItems
- -- Process the dropped items here
- end open
A JavaScriptopenDocumentsfunction is formatted as shown inListing 17-2.
JAVASCRIPT
Open in Script Editor

- function openDocuments(droppedItems) {
- // Process the dropped items here
- }
Typically, a droplet loops through items dropped onto it, processing them individually, as inListing 17-3andListing 17-4.
APPLESCRIPT
Open in Script Editor

- on open theDroppedItems
- repeat with a from 1 to length of theDroppedItems
- set theCurrentDroppedItem to item a of theDroppedItems
- -- Process each dropped item here
- end repeat
- end open
JAVASCRIPT
Open in Script Editor

- function openDocuments(droppedItems) {
- for (var item of droppedItems) {
- // Process each dropped item here
- }
- }
To run a droplet, drop files or folders onto it in the Finder. To test a droplet in Script Editor, add the following line(s) of code to the root levelâtherunhandler portionâof the script.Listing 17-5andListing 17-6prompt you to select a file and then passes it to theopenhandler oropenDocumentsfunction.
APPLESCRIPT
Open in Script Editor

- open {choose file}
JAVASCRIPT
Open in Script Editor

- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var file = app.chooseFile()
- openDocuments([file])

### Creating an AppleScript Droplet from a Script Editor Template

Script Editor includes several preconfigured AppleScript droplet templates, which solve the majority of droplet use cases.
Note
Script Editor does not include JavaScript templates at this time.

- Launch Script Editor from/Applications/Utilities/.
Launch Script Editor from/Applications/Utilities/.

- Select File > New from Template > Droplets.
Select File > New from Template > Droplets.

- Choose a droplet template.Options include:Droplet with Settable PropertiesâThis template processes dropped files based on file type, extension, or type identifier. It also demonstrates how to include a user-configurable setting, which affects the behavior of the script.Recursive File Processing DropletâThis template processes dropped files based on file type, extension, or type identifier. It is configured to detect files within dropped folders and their subfolders.Recursive Image File Processing DropletâThis template processes image files matching specific file types, extensions, or type identifiers. It is configured to detect images within dropped folders and their subfolders.All of these templates are designed to serve as starting points for creating a droplet, and can be customized, as needed.
Choose a droplet template.
Options include:

- Droplet with Settable PropertiesâThis template processes dropped files based on file type, extension, or type identifier. It also demonstrates how to include a user-configurable setting, which affects the behavior of the script.
Droplet with Settable PropertiesâThis template processes dropped files based on file type, extension, or type identifier. It also demonstrates how to include a user-configurable setting, which affects the behavior of the script.

- Recursive File Processing DropletâThis template processes dropped files based on file type, extension, or type identifier. It is configured to detect files within dropped folders and their subfolders.
Recursive File Processing DropletâThis template processes dropped files based on file type, extension, or type identifier. It is configured to detect files within dropped folders and their subfolders.

- Recursive Image File Processing DropletâThis template processes image files matching specific file types, extensions, or type identifiers. It is configured to detect images within dropped folders and their subfolders.
Recursive Image File Processing DropletâThis template processes image files matching specific file types, extensions, or type identifiers. It is configured to detect images within dropped folders and their subfolders.
All of these templates are designed to serve as starting points for creating a droplet, and can be customized, as needed.

### Creating a Droplet to Process Files

InListing 17-7andListing 17-8, theopenhandler  andopenDocumentsfunction process dropped files based on file type, extension, or type identifier. The file types, extensions, and type identifiers supported by the handler are configurable in properties at the top of the script. If a dropped file matches the criteria you configure, then the file is passed to theprocessItem()handler, where you can add custom file processing code. These examples are not configured to process dropped folders.
APPLESCRIPT
Open in Script Editor

- property theFileTypesToProcess : {} -- For example: {"PICT", "JPEG", "TIFF", "GIFf"}
- property theExtensionsToProcess : {} -- For example: {"txt", "text", "jpg", "jpeg"}, NOT: {".txt", ".text", ".jpg", ".jpeg"}
- property theTypeIdentifiersToProcess : {} -- For example: {"public.jpeg", "public.tiff", "public.png"}
- on open theDroppedItems
- repeat with a from 1 to count of theDroppedItems
- set theCurrentItem to item a of theDroppedItems
- tell application "System Events"
- set theExtension to name extension of theCurrentItem
- set theFileType to file type of theCurrentItem
- set theTypeIdentifier to type identifier of theCurrentItem
- end tell
- if ((theFileTypesToProcess contains theFileType) or (theExtensionsToProcess contains theExtension) or (theTypeIdentifiersToProcess contains theTypeIdentifier)) then
- processItem(theCurrentItem)
- end if
- end repeat
- end open
- on processItem(theItem)
- -- NOTE: The variable theItem is a file reference in AppleScript alias format
- -- Add item processing code here
- end processItem
JAVASCRIPT
Open in Script Editor

- var SystemEvents = Application("System Events")
- var fileTypesToProcess = [] // For example: {"PICT", "JPEG", "TIFF", "GIFf"}
- var extensionsToProcess = [] // For example: {"txt", "text", "jpg", "jpeg"}, NOT: {".txt", ".text", ".jpg", ".jpeg"}
- var typeIdentifiersToProcess = [] // For example: {"public.jpeg", "public.tiff", "public.png"}
- function openDocuments(droppedItems) {
- for (var item of droppedItems) {
- var alias = SystemEvents.aliases.byName(item.toString())
- var extension = alias.nameExtension()
- var fileType = alias.fileType()
- var typeIdentifier = alias.typeIdentifier()
- if (fileTypesToProcess.includes(fileType) || extensionsToProcess.includes(extension) || typeIdentifiersToProcess.includes(typeIdentifier)) {
- processItem(item)
- }
- }
- }
- function processItem(item) {
- // NOTE: The variable item is an instance of the Path object
- // Add item processing code here
- }

### Creating a Droplet to Process Files and Folders

InListing 17-9andListing 17-10, theopenhandler andopenDocumentsfunction loop through any dropped files and folders.
For each dropped file, the script calls theprocessFile()handler, which determines whether the file matches specific file types, extensions, and type identifiers. The file types, extensions, and type identifiers supported by the handler are configurable in properties at the top of the script. If thereâs a match, then any custom file processing code you add runs.
The script passes each dropped folder to theprocessFolder(), which retrieves a list of files and subfolders within the dropped folder. TheprocessFolder()handler recursively calls itself to process any additional subfolders. It calls theprocessFile()handler to process any detected files. If necessary, you can add custom folder processing code to theprocessFolder()handler.
APPLESCRIPT
Open in Script Editor

- property theFileTypesToProcess : {} -- I.e. {"PICT", "JPEG", "TIFF", "GIFf"}
- property theExtensionsToProcess : {} -- I.e. {"txt", "text", "jpg", "jpeg"}, NOT: {".txt", ".text", ".jpg", ".jpeg"}
- property theTypeIdentifiersToProcess : {} -- I.e. {"public.jpeg", "public.tiff", "public.png"}
- on open theDroppedItems
- repeat with a from 1 to count of theDroppedItems
- set theCurrentItem to item a of theDroppedItems
- tell application "Finder"
- set isFolder to folder (theCurrentItem as string) exists
- end tell
- -- Process a dropped folder
- if isFolder = true then
- processFolder(theCurrentItem)
- -- Process a dropped file
- else
- processFile(theCurrentItem)
- end if
- end repeat
- end open
- on processFolder(theFolder)
- -- NOTE: The variable theFolder is a folder reference in AppleScript alias format
- -- Retrieve a list of any visible items in the folder
- set theFolderItems to list folder theFolder without invisibles
- -- Loop through the visible folder items
- repeat with a from 1 to count of theFolderItems
- set theCurrentItem to ((theFolder as string) & (item a of theFolderItems)) as alias
- open {theCurrentItem}
- end repeat
- -- Add additional folder processing code here
- end processFolder
- on processFile(theItem)
- -- NOTE: variable theItem is a file reference in AppleScript alias format
- tell application "System Events"
- set theExtension to name extension of theItem
- set theFileType to file type of theItem
- set theTypeIdentifier to type identifier of theItem
- end tell
- if ((theFileTypesToProcess contains theFileType) or (theExtensionsToProcess contains theExtension) or (theTypeIdentifiersToProcess contains theTypeIdentifier)) then
- -- Add file processing code here
- display dialog theItem as string
- end if
- end processFile
JAVASCRIPT
Open in Script Editor

- var SystemEvents = Application("System Events")
- var fileManager = $.NSFileManager.defaultManager
- var currentApp = Application.currentApplication()
- currentApp.includeStandardAdditions = true
- var fileTypesToProcess = [] // For example: {"PICT", "JPEG", "TIFF", "GIFf"}
- var extensionsToProcess = [] // For example: {"txt", "text", "jpg", "jpeg"}, NOT: {".txt", ".text", ".jpg", ".jpeg"}
- var typeIdentifiersToProcess = [] // For example: {"public.jpeg", "public.tiff", "public.png"}
- function openDocuments(droppedItems) {
- for (var item of droppedItems) {
- var isDir = Ref()
- if (fileManager.fileExistsAtPathIsDirectory(item.toString(), isDir) && isDir[0]) {
- processFolder(item)
- }
- else {
- processFile(item)
- }
- }
- }
- function processFolder(folder) {
- // NOTE: The variable folder is an instance of the Path object
- var folderString = folder.toString()
- // Retrieve a list of any visible items in the folder
- var folderItems = currentApp.listFolder(folder, { invisibles: false })
- // Loop through the visible folder items
- for (var item of folderItems) {
- var currentItem = `${folderString}/${item}`
- openDocuments([currentItem])
- }
- // Add additional folder processing code here
- }
- function processFile(file) {
- // NOTE: The variable file is an instance of the Path object
- var fileString = file.toString()
- var alias = SystemEvents.aliases.byName(fileString)
- var extension = alias.nameExtension()
- var fileType = alias.fileType()
- var typeIdentifier = alias.typeIdentifier()
- if (fileTypesToProcess.includes(fileType) || extensionsToProcess.includes(extension) || typeIdentifiersToProcess.includes(typeIdentifier)) {
- // Add file processing code here
- }
- }
Reading and Writing Files
Watching Folders
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13
