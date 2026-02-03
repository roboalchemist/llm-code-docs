# Mac Automation Scripting Guide: Using Handlers/Functions

## Using Handlers/Functions
Collections of script statements that can be invoked by name are referred to ashandlersin AppleScript,functionsormethodsin JavaScript, andsubroutinesin some other languages. Throughout this document, these terms are used interchangeably.
Handlers are generally written to perform a task multiple times throughout a script, such as displaying an alert, writing text to a file, or creating an email message. Instead of inserting the same code over and over, you write it once and give it a name. You can name a handler whatever you like as long as the name contains no special characters, such as punctuation, or spaces, and isnât a reserved language term. You thencall, or evoke, a handler whenever necessary by referring to it by name. Each time you do, any code in the handler runs. Handlers can optionally be written to receive information as input for processing (parameters), and can return information as output (resultorreturn value).
Handlers provide a way to organize your code by breaking it up into smaller, manageable, modular chunks. This can be useful when troubleshooting; you can narrow in on a single handler to resolve a problem, rather than sorting through a long, complex script. It also makes future script updates easier, as you can change behavior in one place to affect an entire script.
Note
AppleScript handlers are generally placed at the end of a script, while in JavaScript, theyâre usually placed at the top.

### AppleScript Handlers
In AppleScript, a handler begins with the wordonorto, followed by the handler name and its parameters, if any. It ends with the wordend, followed by the handler name. AppleScript handlers can be written with positional, labeled, or interleaved parameters.
Listing 13-1shows a simple one-line script that displays a hypothetical error message, which you might want to display numerous times as a script runs.
APPLESCRIPT
Open in Script Editor
- display dialog "The script encountered a problem."
InListing 13-1, the code fromListing 13-1has been converted to a handler nameddisplayError, which has no parameters.
APPLESCRIPT
Open in Script Editor
- on displayError()
- display dialog "The script encountered a problem."
- end displayError
Listing 13-3shows a variation of the handler inListing 13-1, which uses thetoprefix instead ofon. Either syntax is acceptable.
APPLESCRIPT
Open in Script Editor
- to displayError()
- display dialog "The script encountered a problem."
- end displayError
You can now call thedisplayErrorhandler any time you want to display an error, as shown inListing 13-4.
APPLESCRIPT
Open in Script Editor
- try
- -- Do something
- on error
- -- Notify the user that there's a problem
- displayError()
- end try
- try
- -- Do something else
- on error
- -- Notify the user that there's a problem
- displayError()
- end try
For detailed information about AppleScript handlers, seeAbout HandlersandHandler ReferenceinAppleScript Language Guide.
Note
To call a handler from within atellstatement, you must use the reserved wordsof meormy, as shown inListing 13-5.
APPLESCRIPT
Open in Script Editor
- tell application "Finder"
- try
- -- Do something
- on error
- -- Notify the user that there's a problem
- displayError() of me
- end try
- end tell
- tell application "Finder"
- try
- -- Do something else
- on error
- -- Notify the user that there's a problem
- my displayError()
- end try
- end tell

### AppleScript Handlers with Positional Parameters
Positional parameters are a series of comma-separated variables, contained within parentheses, following the handler name. InListing 13-6, thedisplayErrorhandler fromListing 13-1has been updated to accept two positional parametersâan error message and a list of buttons to display.
APPLESCRIPT
Open in Script Editor
- on displayError(theErrorMessage, theButtons)
- display dialog theErrorMessage buttons theButtons
- end displayError
To call the handler, refer to it by name and provide a value for each positional parameter, as shown inListing 13-7. The order of these values should match the parameter positions in the handler definition.
APPLESCRIPT
Open in Script Editor
- displayError("There's not enough available space. Would you like to continue?", {"Don't Continue", "Continue"})
For additional information about this style of handler, seeHandlers with Positional ParametersinAppleScript Language Guide.

### AppleScript Handlers with Interleaved Parameters
Interleaved parameters are a variation of positional parameters, in which the parameter name is split into pieces and interleaved with parameters using colons and spaces.Listing 13-8shows how the handler fromListing 13-6can be represented using interleaved parameters.
APPLESCRIPT
Open in Script Editor
- tell me to displayError:"There's not enough available space. Would you like to continue?" withButtons:{"Don't Continue", "Continue"}
- on displayError:theErrorMessage withButtons:theButtons
- display dialog theErrorMessage buttons theButtons
- end displayError:withButtons:
Interleaved parameters resemble Objective-C syntax. Therefore, they are typically used to call Objective-C methods in AppleScriptObjC scripts.
Objective-C to AppleScript Quick Translation Guidediscusses interleaved parameter use in AppleScriptObjC scripts. For additional information about this style of handler, seeHandlers with Interleaved ParametersinAppleScript Language Guide.

### AppleScript Handlers with Labeled Parameters
AppleScript also supports labeled parameters, although this style is rarely used when defining custom handlers. Most often, itâs a style used for event handlers. SeeEvent Handlers.Listing 13-9shows how thedisplayErrorhandler might appear if it were written using the labeled parameter style.
APPLESCRIPT
Open in Script Editor
- display of "There's not enough available space. Would you like to continue?" over {"Don't Continue", "Continue"}
- to display of theErrorMessage over theButtons
- display dialog theErrorMessage buttons theButtons
- end display
For additional information about this style of handler, seeHandlers with Labeled ParametersinAppleScript Language Guide.

### JavaScript Functions
In JavaScript, a function name is preceded by the wordfunctionand followed by a list of parameters, if any. The functionâs contents are contained within curly braces ({ ... }).
Listing 13-10shows a simple script that displays a hypothetical error message.
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- function displayError() {
- app.displayDialog("The script encountered a problem.")
- }
You can now call thedisplayErrorfunction any time you want to display an error, as shown inListing 13-11.
JAVASCRIPT
Open in Script Editor
- try {
- // Do something
- } catch (error) {
- // Notify the user that there's a problem
- displayError()
- }
- try {
- // Do something else
- } catch (error) {
- // Notify the user that there's a problem
- displayError()
- }

### Using Parameters
JavaScript functions are written with positional parameters, comma-separated variables, contained within parentheses, following the function name. InListing 13-12, thedisplayErrorfunction fromListing 13-10has been updated to accept two positional parametersâan error message and a list of buttons to display.
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- function displayError(errorMessage, buttons) {
- app.displayDialog(errorMessage, {
- buttons: buttons
- })
- }
To call the function, refer to it by name and provide a value for each positional parameter, as shown inListing 13-13. The order of these values should match the parameter positions in the function definition.
JAVASCRIPT
Open in Script Editor
- displayError("There's not enough available space. Would you like to continue?", ["Don't Continue", "Continue"])

### Exiting Handlers and Returning a Result
Often, handlers are used to process information and produce a result for further processing. To enable this functionality, add thereturncommand, followed by a value to provide, to the handler. InListing 13-14andListing 13-15, thedisplayErrorhandler returns a Boolean value, indicating whether processing should continue after an error has occurred.
APPLESCRIPT
Open in Script Editor
- set shouldContinueProcessing to displayError("There's not enough available space. Would you like to continue?")
- if shouldContinueProcessing = true then
- -- Continue processing
- else
- -- Stop processing
- end if
- on displayError(theErrorMessage)
- set theResponse to display dialog theErrorMessage buttons {"Don't Continue", "Continue"} default button "Continue"
- set theButtonChoice to button returned of theResponse
- if theButtonChoice = "Continue" then
- return true
- else
- return false
- end if
- end displayError
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- function displayError(errorMessage) {
- var response = app.displayDialog(errorMessage, {
- buttons: ["Don't Continue", "Continue"],
- defaultButton: "Continue"
- })
- var buttonChoice = response.buttonReturned
- if (buttonChoice == "Continue")
- return true
- else
- return false
- }
- var shouldContinueProcessing = displayError("There's not enough available space. Would you like to continue?")
- if (shouldContinueProcessing) {
- // Continue processing
- } else {
- // Stop processing
- }
Note
You can return a value at any time within a handler, not just at the end.

### Event Handlers
Some apps, including scripts themselves, can call handlers when certain events occur, such as when launched or quit. In Mail, you can set up a rule to look for incoming emails matching certain criteria. When a matching email is detected, Mail can call a handler in a specified script to process the email. Handlers like these are consideredevent handlersorcommand handlers.
Listing 13-16shows an example of a Mail rule event handler. It receives any detected messages as input, and can loop through them to process them.
APPLESCRIPT
Open in Script Editor
- using terms from application "Mail"
- on perform mail action with messages theDetectedMessages for rule theRule
- tell application "Mail"
- set theMessageCount to count of theDetectedMessages
- repeat with a from 1 to theMessageCount
- set theCurrentMessage to item a of theDetectedMessages
- -- Process the message
- end repeat
- end tell
- end perform mail action with messages
- end using terms from

### Script Event Handlers
As previously mentioned, scripts can contain event handlers too. These handlers run when certain events occur.

### Run Handlers
Therunevent handler is called when a script runs. By default, any executable code at the top level of a scriptâthat is, not contained within a handler orscriptobjectâis considered to be contained within an implicitrunhandler. SeeListing 13-17andListing 13-18.
APPLESCRIPT
Open in Script Editor
- display dialog "The script is running."
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- app.displayDialog("The script is running.")
Optionally, therunhandler can be explicitly defined.Listing 13-19andListing 13-20produce the exact same behavior asListing 13-17andListing 13-18.
APPLESCRIPT
Open in Script Editor
- on run
- display dialog "The script is running."
- end run
JAVASCRIPT
Open in Script Editor
- function run() {
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- app.displayDialog("The script is running.")
- }

### Quit Handlers
Thequitevent handler is optional, and is called when a script app quits. Use this as an opportunity to perform cleanup tasks, if necessary, such as removing temporary folders or logging progress.Listing 13-21andListing 13-22demonstrate the use of aquithandler.
APPLESCRIPT
Open in Script Editor
- on quit
- display dialog "The script is quitting."
- end quit
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- function quit() {
- app.displayDialog("The script is quitting.")
- }

### Open Handlers
The inclusion of anopenhandler oropenDocumentsmethod in a script app automatically makes the app drag-and-droppable. When launched in this way, theopenhandler receives a dropped list of files or folders as a direct parameter, as shown inListing 13-23andListing 13-24.
APPLESCRIPT
Open in Script Editor
- on open theDroppedItems
- -- Process the dropped items here
- end open
JAVASCRIPT
Open in Script Editor
- function openDocuments(droppedItems) {
- // Process the dropped items here
- }
For detailed information about using theopenhandler to create drop scripts, seeProcessing Dropped Files and Folders.

### Idle Handlers
When saving a script, you can optionally save it as a stay-open application. SeeFigure 13-1. In a stay-open script app, the script stays open after therunhandler completes, and anidlehandler is called every 30 seconds. Use theidlehandler to perform periodic processing tasks, such as checking a watched folder for new files to process. To change the duration betweenidlecalls, return a new duration, in seconds, as the result of theidlehandler.Listing 13-25andListing 13-26demonstrate anidlehandler that delays for five seconds between executions.
APPLESCRIPT
Open in Script Editor
- on idle
- display dialog "The script is idling."
- return 5
- end idle
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- function idle() {
- app.displayDialog("The script is idling.")
- return 5
- }
For information about using theidlehandler for folder watching, seeWatching Folders.
Navigating a Scripting Dictionary
Using Script Libraries
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13