# Mac Automation Scripting Guide: Displaying Progress

## Displaying Progress

Many scripts perform large and time-consuming processing operations. All too often, they do this invisibly; they simply run and the user has no idea how long processing will take. A more user-friendly approach is to provide progress information during script operation. At a basic level, this can be done by displaying periodic dialogs or notifications. SeeDisplaying Dialogs and AlertsandDisplaying Notifications. At a complex level, this can be done by designing a fully-custom interface that provides processing feedback.
AppleScript and JavaScript can also report progress graphically and textually. For script apps, this progress reporting takes the form of a dialog window containing a progress bar, descriptive text, and a Stop button. SeeFigure 30-1.
For scripts running in Script Editor, this progress reporting appears at the bottom of the script window. SeeFigure 30-2.
For scripts running from the systemwide script menu, this progress reporting appears in the menu bar, beneath a temporarily displayed gear icon. SeeFigure 30-3.
AppleScript has several language-level properties and JavaScript has aProgressobject with properties that are used to produce this type of progress reporting. SeeTable 30-1.
AppleScript Property
JavaScript Property
Value Type
Description
progress total steps
Progress.totalUnitCount
Integer
Configures the total number of steps to be reported in the progress. For example, if the script will process 5 images, then the value forprogress total stepswould be5.
progress completed steps
Progress.completedUnitCount
Integer
Configures the number of steps completed so far. For example, if the script has processed 3 of 5 images, then the value ofprogress completed stepswould be3.
progress description
Progress.description
Integer
Text to display when reporting progress. Use this is an opportunity to let the user know whatâs happening. For example, it could indicate that images are being processed.
progress additional description
Progress.additionalDescription
Integer
Additional text to display when reporting progress. Use this is an opportunity to provide even more detailed information about whatâs happening. For example, it could indicate the specific task being performed, and how much more processing is remaining.
Listing 30-1andListing 30-2demonstrate how these properties can be used to provide progress information while processing a set of images.
APPLESCRIPT
Open in Script Editor

- set theImages to choose file with prompt "Please select some images to process:" of type {"public.image"} with multiple selections allowed
- -- Update the initial progress information
- set theImageCount to length of theImages
- set progress total steps to theImageCount
- set progress completed steps to 0
- set progress description to "Processing Images..."
- set progress additional description to "Preparing to process."
- repeat with a from 1 to length of theImages
- -- Update the progress detail
- set progress additional description to "Processing image " & a & " of " & theImageCount
- -- Process the image
- -- Increment the progress
- set progress completed steps to a
- -- Pause for demonstration purposes, so progress can be seen
- delay 1
- end repeat
- -- Reset the progress information
- set progress total steps to 0
- set progress completed steps to 0
- set progress description to ""
- set progress additional description to ""
JAVASCRIPT
Open in Script Editor

- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var images = app.chooseFile({
- withPrompt: "Please select some images to process:",
- ofType: ["public.image"],
- multipleSelectionsAllowed: true
- })
- // Update the initial progress information
- var imageCount = images.length
- Progress.totalUnitCount = imageCount
- Progress.completedUnitCount = 0
- Progress.description = "Processing Images..."
- Progress.additionalDescription = "Preparing to process."
- for (i = 0; i < imageCount; i++) {
- // Update the progress detail
- Progress.additionalDescription = "Processing image " + i + " of " + imageCount
- // Process the image
- // Increment the progress
- Progress.completedUnitCount = i
- // Pause for demonstration purposes, so progress can be seen
- delay(1)
- }
Clicking the Stop button in a progress dialog results in a user cancelled error.
For additional information, seeProgress ReportinginAppleScript Release NotesandProgressinJavaScript for Automation Release Notes.
Note
Thereâs no need to call a dedicated command to actually display progress information. The act of setting values for the progress properties mentioned above automatically results in progress information being displayed in a dialog, Script Editor, or the menu bar.
Prompting for a Color
Converting RGB to HTML Color
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13
