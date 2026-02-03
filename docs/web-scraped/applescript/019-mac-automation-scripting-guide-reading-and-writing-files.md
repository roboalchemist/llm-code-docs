# Mac Automation Scripting Guide: Reading and Writing Files

## Reading and Writing Files
Scripts are often designed to write data to files such as logs or backups. The Standard Additions scripting addition contains a number of commands that make it possible to read and write files.

### Writing to a File
The handlers inListing 16-1andListing 16-2safely write data to disk, creating a new file if the targeted file doesnât already exist. Provide the text to write, a target file path, and indicate whether to overwrite existing content. If you choose not to overwrite existing content, then the text provided is appended to any existing content.
APPLESCRIPT
Open in Script Editor
- on writeTextToFile(theText, theFile, overwriteExistingContent)
- try
- -- Convert the file to a string
- set theFile to theFile as string
- -- Open the file for writing
- set theOpenedFile to open for access file theFile with write permission
- -- Clear the file if content should be overwritten
- if overwriteExistingContent is true then set eof of theOpenedFile to 0
- -- Write the new content to the file
- write theText to theOpenedFile starting at eof
- -- Close the file
- close access theOpenedFile
- -- Return a boolean indicating that writing was successful
- return true
- -- Handle a write error
- on error
- -- Close the file
- try
- close access file theFile
- end try
- -- Return a boolean indicating that writing failed
- return false
- end try
- end writeTextToFile
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- function writeTextToFile(text, file, overwriteExistingContent) {
- try {
- // Convert the file to a string
- var fileString = file.toString()
- // Open the file for writing
- var openedFile = app.openForAccess(Path(fileString), { writePermission: true })
- // Clear the file if content should be overwritten
- if (overwriteExistingContent) {
- app.setEof(openedFile, { to: 0 })
- }
- // Write the new content to the file
- app.write(text, { to: openedFile, startingAt: app.getEof(openedFile) })
- // Close the file
- app.closeAccess(openedFile)
- // Return a boolean indicating that writing was successful
- return true
- }
- catch(error) {
- try {
- // Close the file
- app.closeAccess(file)
- }
- catch(error) {
- // Report the error is closing failed
- console.log(`Couldn't close file: ${error}`)
- }
- // Return a boolean indicating that writing was successful
- return false
- }
- }
Listing 16-3andListing 16-4show how to call the handlers inListing 16-1andListing 16-2to write text content to a file on the Desktop, replacing any existing content in the file.
APPLESCRIPT
Open in Script Editor
- set this_story to "Once upon a time in Silicon Valley..."
- set theFile to (((path to desktop folder) as string) & "MY STORY.txt")
- writeTextToFile(this_story, theFile, true)
JAVASCRIPT
Open in Script Editor
- var story = "Once upon a time in Silicon Valley..."
- var desktopString = app.pathTo("desktop").toString()
- var file = `${desktopString}/MY STORY.txt`
- writeTextToFile(story, file, true)
Listing 16-5andListing 16-6show howListing 16-1andListing 16-2could be called to insert dated log entries into a log file.
APPLESCRIPT
Open in Script Editor
- set theText to ((current date) as string) & space & "STATUS OK" & return
- set theFile to (((path to desktop folder) as string) & "MY LOG FILE.log")
- writeTextToFile(theText, theFile, false)
JAVASCRIPT
Open in Script Editor
- var dateString = Date().toString()
- var desktopString = app.pathTo("desktop").toString()
- var text = `${dateString} STATUS OK\n\n`
- var file = `${desktopString}/MY LOG FILE.log`
- writeTextToFile(text, file, false)
In practice, this technique could be used to maintain a log when script errors occur.Listing 16-7andListing 16-8are try statements, which can be wrapped around custom script code in order to log any script errors to a file in the~/Library/Logs/folder of the current userâs home directory.
APPLESCRIPT
Open in Script Editor
- try
- -- Your custom script code goes here
- on error theErrorMessage number theErrorNumber
- set theError to "Error: " & theErrorNumber & ". " & theErrorMessage & return
- set theLogFile to ((path to library folder from user domain) as string) & "Logs:Script Error Log.log"
- my writeTextToFile(theError, theLogFile, false)
- end try
JAVASCRIPT
Open in Script Editor
- try {
- // Your custom script code goes here
- }
- catch (error) {
- var errorString = `Error: ${error.message}\n\n`
- var logFile = app.pathTo("library folder", { from: "user domain" }).toString() + "/Logs/Script Error Log.log"
- writeTextToFile(errorString, logFile, false)
- }

### Reading a File
The handlers inListing 16-9andListing 16-10read the contents of a specified file.
APPLESCRIPT
Open in Script Editor
- on readFile(theFile)
- -- Convert the file to a string
- set theFile to theFile as string
- -- Read the file and return its contents
- return read file theFile
- end readFile
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- function readFile(file) {
- // Convert the file to a string
- var fileString = file.toString()
- // Read the file and return its contents
- return app.read(Path(fileString))
- }
Listing 16-11andListing 16-12show how to call the handlers inListing 16-9andListing 16-10to read a specified text file.
APPLESCRIPT
Open in Script Editor
- set theFile to choose file of type "txt" with prompt "Please select a text file to read:"
- readFile(theFile)
- --> Result: "Contents of the chosen file."
JAVASCRIPT
Open in Script Editor
- var file = app.chooseFile({
- ofType: "txt",
- withPrompt: "Please select a text file to read:"
- })
- readFile(file)
- // Result: "Contents of the chosen file."

### Reading and Splitting a File
The handlers inListing 16-13andListing 16-14read the contents of a specified text file, using a delimiter to split it into a list.
APPLESCRIPT
Open in Script Editor
- on readAndSplitFile(theFile, theDelimiter)
- -- Convert the file to a string
- set theFile to theFile as string
- -- Read the file using a specific delimiter and return the results
- return read file theFile using delimiter {theDelimiter}
- end readAndSplitFile
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- function readAndSplitFile(file, delimiter) {
- // Convert the file to a string
- var fileString = file.toString()
- // Read the file using a specific delimiter and return the results
- return app.read(Path(fileString), { usingDelimiter: delimiter })
- }
Listing 16-15andListing 16-16shows how to call the handlers inListing 16-13andListing 16-14to read the paragraphs of a chosen log file.
APPLESCRIPT
Open in Script Editor
- set theFile to choose file of type "log" with prompt "Please select a log file:"
- readAndSplitFile(theFile, return)
- --> Result: {"Log entry 1", "Log entry 2", ... }
JAVASCRIPT
Open in Script Editor
- var file = app.chooseFile({
- ofType: "log",
- withPrompt: "Please select a log file:"
- })
- readAndSplitFile(file, "\n")
- // Result: ["Log entry 1", "Log entry 2", ...]
Referencing Files and Folders
Processing Dropped Files and Folders
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13