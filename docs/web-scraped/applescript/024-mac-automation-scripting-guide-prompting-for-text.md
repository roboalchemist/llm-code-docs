# Mac Automation Scripting Guide: Prompting for Text

## Prompting for Text

Use thedisplay dialogcommandâs optionaldefault answerparameter to collect text, such as a username or email address, as your script runs. As demonstrated byFigure 23-1,Listing 23-1, andListing 23-2, the inclusion of thedefault answerparameter automatically adds a text entry field to the resulting dialog. Any string you provide for the parameter appears in the text field when the dialog displays. Providing an empty string ("") produces an empty text field. When the dialog dismisses, any text from the field is returned in atext returnedproperty of thedisplay dialogcommandâs result.
APPLESCRIPT
Open in Script Editor

- set theResponse to display dialog "What's your name?" default answer "" with icon note buttons {"Cancel", "Continue"} default button "Continue"
- --> {button returned:"Continue", text returned:"Jen"}
- display dialog "Hello, " & (text returned of theResponse) & "."
JAVASCRIPT
Open in Script Editor

- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var response = app.displayDialog("What's your name?", {
- defaultAnswer: "",
- withIcon: "note",
- buttons: ["Cancel", "Continue"],
- defaultButton: "Continue"
- })
- // Result: {"buttonReturned":"Continue", "textReturned":"Jen"}
- app.displayDialog("Hello, " + (response.textReturned) + ".")
Note
Additional information about thedisplay dialogcommand can be found inDisplaying Dialogs and Alerts. For complete information about the command and its parameters, launch Script Editor, open the Standard Additions scripting additionâs dictionary, and navigate to the commandâs definition.

### Prompting for Hidden Text

Protect potentially sensitive information from prying eyes by using thedisplay dialogcommandâsdefault answerparameter in conjunction with thehidden answerparameter to show bullets instead of plain text in the dialogâs text field. SeeFigure 23-2,Listing 23-3, andListing 23-4.
APPLESCRIPT
Open in Script Editor

- display dialog "Please enter a passphrase to use this script." default answer "" with icon stop buttons {"Cancel", "Continue"} default button "Continue" with hidden answer
- --> Result: {button returned:"Continue", text returned:"MySecretPassphrase"}
JAVASCRIPT
Open in Script Editor

- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- app.displayDialog("Please enter a passphrase to use this script.", {
- defaultAnswer: "",
- withIcon: "stop",
- buttons: ["Cancel", "Continue"],
- defaultButton: "Continue",
- hiddenAnswer: true
- })
- // Result: {"buttonReturned":"Continue", "textReturned":"MySecretPassphrase"}
Warning
Always be cautious when requesting sensitive data, such as passwords. Hidden text is returned by thedisplay dialogcommand as plain, unencrypted text, so this command offers limited security.
Displaying Dialogs and Alerts
Displaying Notifications
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13
