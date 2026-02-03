# Mac Automation Scripting Guide: Speaking Text

## Speaking Text
Spoken text is another way to provide feedback to users during script execution; instead of reading a message visually, the user can listen to it audibly.Listing 25-1andListing 25-2show how the Standard Additions scripting additionâssaycommand can be used to speak a phrase.
APPLESCRIPT
Open in Script Editor
- say "Processing is complete."
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- app.say("Processing is complete.")
Thesaycommand has a number of optional parameters, some of which allow you to specify a voice and attributes such as speaking rate, pitch, and modulation. SeeListing 25-3andListing 25-4.
APPLESCRIPT
Open in Script Editor
- say "Just what do you think you're doing Dave?" using "Alex" speaking rate 140 pitch 42 modulation 60
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- app.say("Just what do you think you're doing Dave?", {
- using: "Alex",
- speakingRate: 140,
- pitch: 42,
- modulation: 60
- })

### Saving Text as an Audio File
Thesaycommandâssaving asparameter adds another level of power, enabling text to be converted to audio format and saved as an.aifffile for later listening. This technique could be used, for example, to save email messages in audio format, as demonstrated byListing 25-5andListing 25-6.
APPLESCRIPT
Open in Script Editor
- tell application "Mail"
- tell message 1 of inbox
- set theSubject to subject
- set theBody to content
- end tell
- end tell
- set theOutputFile to (path to desktop as string) & "message.aiff"
- set theAudio to "Message Subject: " & theSubject & return & "Body: " & theBody
- say theAudio saving to theOutputFile
JAVASCRIPT
Open in Script Editor
- var Mail = Application("Mail")
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- message = Mail.inbox.messages[0]
- subject = message.subject()
- body = message.content()
- outputFile = ((app.pathTo("desktop").toString()) + "/message.aiff")
- audio = "Message Subject: " + subject + "\nBody: " + body
- app.say(audio, {savingTo: outputFile})

### Speaking Text While Displaying a Dialog
Typically, a script executes a single command at a time, waiting for a command to complete before moving onto the next.Listing 25-7andListing 25-8demonstrate how to display a dialog message, while simultaneously using theNSTaskclass in the Foundation framework to read the message out loud.
APPLESCRIPT
Open in Script Editor
- use framework "Foundation"
- use scripting additions
- set theStatusText to "Processing is complete."
- set theTask to (current application's NSTask's launchedTaskWithLaunchPath:"/usr/bin/say" arguments:{theStatusText})
- try
- display dialog theStatusText
- theTask's terminate()
- on error
- try
- theTask's terminate()
- end try
- end try
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var statusText = "Processing is complete."
- var task = $.NSTask.launchedTaskWithLaunchPathArguments("/usr/bin/say", [statusText])
- try {
- app.displayDialog(statusText)
- task.terminate
- }
- catch(error){
- task.terminate
- }
Displaying Notifications
Prompting for Files or Folders
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13