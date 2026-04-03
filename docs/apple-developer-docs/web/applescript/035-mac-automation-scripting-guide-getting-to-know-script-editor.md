# Mac Automation Scripting Guide: Getting to Know Script Editor

## Getting to Know Script Editor

Script Editor, found in/Applications/Utilities/, is an app for writing AppleScripts and JavaScripts. It provides the ability to edit, compile, and run scripts, browse scripting terminology, and save scripts in a variety of formats including compiled scripts, apps, and plain text.
Note
Xcode can also be used to write AppleScriptObjC and JavaScriptObjC apps.

### Navigating Script Editor Documents

A Script Editor document window includes the following main areas, as shown inFigure 5-1:

- ToolbarâUse this to compile, run, and stop your script. Buttons are also available for showing and hiding the accessory view pane and the bundle contents pane. Select View > Customize Toolbar, or Control-click on the toolbar and choose Customize Toolbar, to choose what buttons displayed in the toolbar.The toolbar also includes a Record button, which converts manual mouse clicks and keystrokes into script code. However, recording is not supported in JavaScript and few apps support AppleScript recording.
ToolbarâUse this to compile, run, and stop your script. Buttons are also available for showing and hiding the accessory view pane and the bundle contents pane. Select View > Customize Toolbar, or Control-click on the toolbar and choose Customize Toolbar, to choose what buttons displayed in the toolbar.
The toolbar also includes a Record button, which converts manual mouse clicks and keystrokes into script code. However, recording is not supported in JavaScript and few apps support AppleScript recording.

- Navigation barâUse this bar to select a scripting language, target an app, or navigate through the handlers in your script.The navigation bar currently only supports navigation of AppleScript handlers.
Navigation barâUse this bar to select a scripting language, target an app, or navigate through the handlers in your script.
The navigation bar currently only supports navigation of AppleScript handlers.

- Editor paneâWrite your script code here.
Editor paneâWrite your script code here.

- Accessory View paneâView and edit your scriptâs description here, or browse the result and events produced when your script runs.
Accessory View paneâView and edit your scriptâs description here, or browse the result and events produced when your script runs.

- Bundle Contents paneâ Edit the identifier, version, and copyright info for your script here. You can also use this pane to add, remove, or manage resources contained within the bundle. This pane is accessible only when your script is saved in script bundle or app format.
Bundle Contents paneâ Edit the identifier, version, and copyright info for your script here. You can also use this pane to add, remove, or manage resources contained within the bundle. This pane is accessible only when your script is saved in script bundle or app format.

### Targeting a Scripting Language

When you create a Script Editor document, select a scripting language in the navigation bar. SeeFigure 5-2.
If you always use the same language, set it as the default in the General pane of Script Editor preferences. SeeFigure 5-3.

### Viewing Script Events and Results

Script Editor can display the result of executing a script, as well as a log of events sent and received during execution.
Note
Aresultis a value generated when a script statement executes. For example, executing themakecommand to create a folder in the Finder produces the newly created folder object as its result. The result of a script is the result of the scriptâs last statement. If the scriptâs last statement doesnât produce a result, then the script has no result.

### Viewing the Script Result

The result of executing your scriptâif a result was producedâis found in the Accessory View pane. SeeFigure 5-4.
Do one of the following:

- Press Command-2.
Press Command-2.

- Choose View > Show Result.
Choose View > Show Result.

- Click the Show Result () button at the bottom of the Accessory View pane.
Click the Show Result () button at the bottom of the Accessory View pane.

### Viewing the Script Log

The Accessory View pane also contains a script log. SeeFigure 5-5.
The script log displays the following information.

- ResultâThe result of executing your script.
ResultâThe result of executing your script.

- MessagesâIncludes log messages generated as your script runs, as well as the scriptâs result.
MessagesâIncludes log messages generated as your script runs, as well as the scriptâs result.

- EventsâIncludes log messages, the scriptâs result, and eventsâcommandsâsent to applications.
EventsâIncludes log messages, the scriptâs result, and eventsâcommandsâsent to applications.

- RepliesâIncludes log messages, the scriptâs result, events sent to applications, and event replies.
RepliesâIncludes log messages, the scriptâs result, events sent to applications, and event replies.
Do one of the following:

- Press Command-3.
Press Command-3.

- Choose View > Show Log.
Choose View > Show Log.

- Click the Show Log () button at the bottom of the Accessory View pane.
Click the Show Log () button at the bottom of the Accessory View pane.
Note
In AppleScript, log messages are generated using thelogcommand. SeeListing 5-1.
APPLESCRIPT
Open in Script Editor

- log "My log entry."
Since thelogcommand targets the script itself, you must explicitly use themekeyword to direct it to the script when calling it within a tell statement. SeeListing 5-2.
APPLESCRIPT
Open in Script Editor

- tell app "Finder"
- tell me to log "My log entry."
- end tell
In JavaScript, log messages are generated by calling theconsole.log()method anywhere in your script. SeeListing 5-3.
JAVASCRIPT
Open in Script Editor

- console.log("My log entry.")

### Viewing the Log History

The result and script log areas in the Accessory View pane reset each time you run your script. However, you can view historical logs for an opened script in the Log History window. SeeFigure 5-6.
Do one of the following:

- Press Option-Command-L.
Press Option-Command-L.

- Choose View > Log History.
Choose View > Log History.

- Click the Log History button () in the top right of the Accessory View pane.
Click the Log History button () in the top right of the Accessory View pane.
About this Guide
Creating a Script
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13