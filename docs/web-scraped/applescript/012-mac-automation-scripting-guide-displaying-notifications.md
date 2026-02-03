# Mac Automation Scripting Guide: Displaying Notifications

## Displaying Notifications

Notification Center offers another opportunity for providing feedback during script execution. Use the Standard Additions scripting additionâsdisplay notificationcommand to show notifications, such as status updates as files are processed. Notifications are shown as alerts or banners, depending on the userâs settings in System Preferences > Notifications. SeeFigure 24-1andFigure 24-2.
To show a notification, provide thedisplay notificationcommand with a string to display. Optionally, provide values for thewith title,subtitle, andsound nameparameters to provide additional information and an audible alert when the notification appears, as shown inListing 24-1andListing 24-2.
APPLESCRIPT
Open in Script Editor

- display notification "All graphics have been converted." with title "My Graphic Processing Script" subtitle "Processing is complete." sound name "Frog"
JAVASCRIPT
Open in Script Editor

- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- app.displayNotification("All graphics have been converted.", {
- withTitle: "My Graphic Processing Script",
- subtitle: "Processing is complete.",
- soundName: "Frog"
- })
Note
After using a script to display a notification, the script or Script Editor (if the script is run from within Script Editor) is added to the list of notifying apps in System Preferences > Notifications. There, you can configure options, such as whether to display notifications as alerts or banners.
Clicking the Show button in an alert-style notification opens the app that displayed the notification. For a script app, the action of opening the app again triggers therunhandler of the script, potentially causing the script to begin processing a second time. Keep this in mind, and add code to your script to handle this scenario, if appropriate.
Prompting for Text
Speaking Text
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13
