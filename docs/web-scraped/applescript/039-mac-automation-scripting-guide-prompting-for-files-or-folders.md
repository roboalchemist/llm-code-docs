# Mac Automation Scripting Guide: Prompting for Files or Folders

## Prompting for Files or Folders

Itâs generally good practice to avoid hard-coding file and folder paths in a script. Prompting the user to select files and folders makes for a more dynamic script that wonât break when paths change.

### Prompting for a File

Use the Standard Additions scripting additionâschoose filecommand to prompt the user to select a file.Listing 26-1andListing 26-2demonstrate how to use this command to display the simple file selection dialog with a custom prompt shown inFigure 26-1.
APPLESCRIPT
Open in Script Editor

- set theDocument to choose file with prompt "Please select a document to process:"
- --> Result: alias "Macintosh HD:Users:yourUserName:Documents:ImportantDoc.pages"
JAVASCRIPT
Open in Script Editor

- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var document = app.chooseFile({
- withPrompt: "Please select a document to process:"
- })
- document
- // Result: Path("/Users/yourUserName/Documents/ImportantDoc.pages")

### Prompting for a Specific Type of File

If your script requires specific types of files for processing, you can use thechoose filecommandâs optionalof typeparameter to provide a list of acceptable types. Types may be specified as extension strings without the leading period (such as"jpg"or"png") or as uniform type identifiers (such as"public.image"or"com.apple.iwork.pages.sffpages").Listing 26-3andListing 26-4show how to prompt for an image.
APPLESCRIPT
Open in Script Editor

- set theImage to choose file with prompt "Please select an image to process:" of type {"public.image"}
- --> Result: alias "Macintosh HD:Users:yourUserName:Pictures:IMG_0024.jpg"
JAVASCRIPT
Open in Script Editor

- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var image = app.chooseFile({
- withPrompt: "Please select an image to process:",
- ofType: ["public.image"]
- })
- image
- // Result: Path("/Users/yourUserName/Pictures/IMG_0024.jpg")

### Prompting for Multiple Files

To let the user choose more than one file, include thechoose filecommandâs optionalmultiple selections allowedparameter.Listing 26-5andListing 26-6display a prompt asking for multiple images, as shown inFigure 26-2.
APPLESCRIPT
Open in Script Editor

- set theImages to choose file with prompt "Please select some images to process:" of type {"public.image"} with multiple selections allowed
- --> Result: {alias "Macintosh HD:Users:yourUserName:Pictures:IMG_0024.jpg", alias "Macintosh HD:Users:yourUserName:Pictures:IMG_0025.jpg", alias "Macintosh HD:Users:yourUserName:Pictures:IMG_0026.jpg"}
JAVASCRIPT
Open in Script Editor

- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var images = app.chooseFile({
- withPrompt: "Please select some images to process:",
- ofType: ["public.image"],
- multipleSelectionsAllowed: true
- })
- images
- // Result: [Path("/Users/yourUserName/Pictures/IMG_0024.jpg"), Path("/Users/yourUserName/Pictures/IMG_0025.jpg"), Path("/Users/yourUserName/Pictures/IMG_0026.jpg")]

### Prompting for a Folder

Use the Standard Additions scripting additionâschoose foldercommand to prompt the user to select a folder, such as an output folder or folder of images to process.Listing 26-7andListing 26-8demonstrate how to use this command to display the simple folder selection dialog with a custom prompt shown inFigure 26-3.
APPLESCRIPT
Open in Script Editor

- set theOutputFolder to choose folder with prompt "Please select an output folder:"
- --> Result: alias "Macintosh HD:Users:yourUserName:Desktop:"
JAVASCRIPT
Open in Script Editor

- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var outputFolder = app.chooseFolder({
- withPrompt: "Please select an output folder:"
- })
- outputFolder
- // Result: Path("/Users/yourUserName/Desktop")

### Prompting for Multiple Folders

To let the user choose more than one folder, include thechoose foldercommandâs optionalmultiple selections allowedparameter, as shown inListing 26-9andListing 26-10.
APPLESCRIPT
Open in Script Editor

- set theFoldersToProcess to choose folder with prompt "Please select the folders containing images to process:" with multiple selections allowed
- --> Result: {alias "Macintosh HD:Users:yourUserName:Desktop:", alias "Macintosh HD:Users:yourUserName:Documents:"}
JAVASCRIPT
Open in Script Editor

- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var foldersToProcess = app.chooseFolder({
- withPrompt: "Please select an output folder:",
- multipleSelectionsAllowed: true
- })
- foldersToProcess
- // Result: [Path("/Users/yourUserName/Desktop"), Path("/Users/yourUserName/Documents")]
Speaking Text
Prompting for a File Name
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13