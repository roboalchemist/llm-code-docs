# Mac Automation Scripting Guide: Displaying Dialogs and Alerts

## Displaying Dialogs and Alerts
Dialogs and alerts are great ways to provide information about a scriptâs progress, report problems, and allow users to make decisions that affect script behavior.

### Displaying a Dialog
Use thedisplay dialogcommand, provided by the Standard Additions scripting addition to show a basic dialog message to the user, such as the one inFigure 22-1. This dialog was produced by the code inListing 22-1andListing 22-2. In these examples, a string is passed to thedisplay dialogcommand as a direct parameter. The result of the command is the button the user clicked in the dialog.
APPLESCRIPT
Open in Script Editor
- set theDialogText to "The curent date and time is " & (current date) & "."
- display dialog theDialogText
- --> Result: {button returned:"OK"}
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var dialogText = "The current date and time is " + (app.currentDate())
- app.displayDialog(dialogText)
- // Result: {"buttonReturned":"OK"}
Note
This chapter covers a portion of thedisplay dialogcommandâs capabilities. For example, thedisplay dialogcommand can also be used to collect text entered by the user. This is covered inPrompting for Text. For complete information about thedisplay dialogcommand and its parameters, launch Script Editor, open the Standard Additions scripting additionâs dictionary, and navigate to the commandâs definition.

### Customizing Dialog Buttons
By default, a dialog produced by thedisplay dialogcommand has two buttonsâCancel and OK (the default). However, the command also has numerous optional parameters, some of which can be used to customize the buttons.
Use thebuttonsparameter to provide a list of between one and three buttons. You can optionally use thedefault buttonparameter to configure one as the defaultâitâs highlighted and pressing the Return key activates it to close the dialog. You can also use thecancel buttonparameter to configure one as the cancel buttonâpressing Escape or Command-Period (.) activates it to close the dialog and produce a user cancelled error.
The dialog shown inFigure 22-2has been customized to include Donât Continue (the cancel button) and Continue (the default) buttons. This dialog was produced by the example code inListing 22-3andListing 22-4.
APPLESCRIPT
Open in Script Editor
- set theDialogText to "An error has occurred. Would you like to continue?"
- display dialog theDialogText buttons {"Don't Continue", "Continue"} default button "Continue" cancel button "Don't Continue"
- --> Result: {{button returned:"Continue"}
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var dialogText = "An error has occurred. Would you like to continue?"
- app.displayDialog(dialogText, {
- buttons: ["Don't Continue", "Continue"],
- defaultButton: "Continue",
- cancelButton: "Don't Continue"
- })
- // Result: {"buttonReturned":"Continue"}

### Adding an Icon to a Dialog
Dialogs can also include an icon, providing users with a visual clue to their importance. You can direct thedisplay dialogcommand to a specific icon by its file path, or resource name or ID if the icon is stored as a resource within your scriptâs bundle. You can also use the standard system iconsstop,note, andcaution.Listing 22-5andListing 22-6display a dialog that includes the system caution icon like the one shown inFigure 22-3.
APPLESCRIPT
Open in Script Editor
- set theDialogText to "The amount of available free space is dangerously low."
- display dialog theDialogText with icon caution
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var dialogText = "The amount of available free space is dangerously low."
- app.displayDialog(dialogText, {withIcon: "caution"})

### Automatically Dismissing a Dialog
Sometimes, you may want to continue with script execution if a dialog isnât dismissed by a user within a certain timeframe. In this case, you can specify an integer value for thedisplay dialogcommandâsgiving up afterparameter, causing the dialog togive upand close automatically after a specified period of inactivity.
Listing 22-7andListing 22-8display a dialog that automatically closes after five seconds of inactivity.
APPLESCRIPT
Open in Script Editor
- display dialog "Do, or do not. There is no try." giving up after 5
- --> Result: {button returned:"OK", gave up:true}
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var dialogText = "Do, or do not. There is no try."
- app.displayDialog(dialogText, {givingUpAfter: 5})
- // Result: {"buttonReturned":"OK", "gaveUp":true}
When using thegiving up afterparameter, the result of thedisplay dialogcommand includes agaveUpproperty, a Boolean value indicating whether the dialog was auto-dismissed. This information is useful if you want the script to take a different course of action based on whether a dialog is manually or automatically dismissed.

### Displaying an Alert
Thedisplay alertcommand is also provided by the Standard Additions scripting addition. Itâs similar to thedisplay dialogcommand, but with slightly different parameters. One of thedisplay alertcommandâs optional parameters ismessage, which lets you provide additional text to display in a separate text field, below the bolded alert text.Listing 22-9andListing 22-10show how to display the alert inFigure 22-4, which contains bolded alert text, plain message text, and custom buttons.
APPLESCRIPT
Open in Script Editor
- set theAlertText to "An error has occurred."
- set theAlertMessage to "The amount of available free space is dangerously low. Would you like to continue?"
- display alert theAlertText message theAlertMessage as critical buttons {"Don't Continue", "Continue"} default button "Continue" cancel button "Don't Continue"
- --> Result: {button returned:"Continue"}
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var alertText = "An error has occurred."
- var alertMessage = "The amount of available free space is dangerously low. Would you like to continue?"
- app.displayAlert(alertText, {
- message: alertMessage,
- as: "critical",
- buttons: ["Don't Continue", "Continue"],
- defaultButton: "Continue",
- cancelButton: "Don't Continue"
- })
- // Result: {"buttonReturned":"OK"}
Note
This chapter covers a portion of thedisplay alertcommandâs capabilities. For complete information about thedisplay alertcommand and its parameters, launch Script Editor, open the Standard Additions scripting additionâs dictionary, and navigate to the commandâs definition.
Manipulating Lists of Items
Prompting for Text
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13