# Mac Automation Scripting Guide: Saving a Script

## Saving a Script
After you write a script, you can save it for future reference or to be run outside of Script Editor.

### Saving a Script or Script Bundle
Scripts and script bundles open in Script Editor when double-clicked in the Finder.
- Choose File > Save (or press Command-S) to display the save dialog.
Choose File > Save (or press Command-S) to display the save dialog.
- Type a name for the script and choose an output folder.
Type a name for the script and choose an output folder.
- Choose Script or Script Bundle from the File Format popup menu.
Choose Script or Script Bundle from the File Format popup menu.
- Click Save.
Click Save.

### Saving a Script Application
Script applications, known as applets, work like other apps on your Mac. Double-click an applet to run it.
- Choose File > Save (or press Command-S) to display the save dialog.
Choose File > Save (or press Command-S) to display the save dialog.
- Type a name for the applet and choose an output folder.
Type a name for the applet and choose an output folder.
- Choose Application from the File Format popup menu.
Choose Application from the File Format popup menu.
- If you want the scriptâs descriptionâdefined in the Accessory View paneâto display when the applet launches, select the âShow startup screenâ checkbox.
If you want the scriptâs descriptionâdefined in the Accessory View paneâto display when the applet launches, select the âShow startup screenâ checkbox.
- If you want to create a stay-open applet, select the âStay open after run handlerâ checkbox.
If you want to create a stay-open applet, select the âStay open after run handlerâ checkbox.
- Click Save.
Click Save.
Note
To open a saved script applet or droplet for editing, drag it onto the Script Editor app or choose File > Open in Script Editor.
To convert a previously saved script or script bundle to an applet, choose File > Duplicate, press Shift-Command-S, or choose File > Export. Then, perform the steps above.
If an AppleScript applet contains anopenevent handler, or a JavaScript applet contains anopenDocumentsfunction, it automatically becomes a drag and drop application known as a droplet. Drag files and folders onto the droplet to process them, or double-click the droplet to run it. To learn about creating droplets, seeProcessing Dropped Files and Folders.

### Protecting a Scriptâs Source Code
If you plan to distribute your script, you may wish to protect is source code. This is done by exporting the script in run-only format.
- Choose File > Export to display the export dialog.
Choose File > Export to display the export dialog.
- Type a name for the applet and choose an output folder.
Type a name for the applet and choose an output folder.
- Choose a format from the File Format popup menu.
Choose a format from the File Format popup menu.
- If youâre saving in application format, choose whether you want a startup screen or a stay-open script.
If youâre saving in application format, choose whether you want a startup screen or a stay-open script.
- Select the Run-only checkbox.
Select the Run-only checkbox.
- Click Save.
Click Save.
Important
When saving a script in run-only format, make sure you retain a backup of your editable script.

### Code Signing a Script
By default, the security settings in OSÂ X only allow the launching of apps (including applets and droplets) that have been created by you, downloaded from the Mac App Store, or created by developers identified by Apple. If you plan to distribute your scripts to others, you should consider code signing your scripts with an Apple developer ID.
You obtain a Developer ID certificate fromCertificates, Identifiers & Profilesin your developer account and import it on your Mac. For detailed information about obtaining and importing a certificate, seeMaintaining Your Signing Identities and CertificatesinApp Distribution Guide.
- If the Bundle Contents pane isnât visible, choose View > Show Bundle, press Command-0, or click the bundle contents button () in the toolbar.
If the Bundle Contents pane isnât visible, choose View > Show Bundle, press Command-0, or click the bundle contents button () in the toolbar.
- Make sure the following highlighted fields are populated in the Bundle Contents pane.NameâThe name of your script.IdentifierâA uniform type identifier for your script. For information, seeUniform Type Identifiers Overview.Short VersionâThe version number for your script.CopyrightâThe copyright string for your script.
Make sure the following highlighted fields are populated in the Bundle Contents pane.
- NameâThe name of your script.
NameâThe name of your script.
- IdentifierâA uniform type identifier for your script. For information, seeUniform Type Identifiers Overview.
IdentifierâA uniform type identifier for your script. For information, seeUniform Type Identifiers Overview.
- Short VersionâThe version number for your script.
Short VersionâThe version number for your script.
- CopyrightâThe copyright string for your script.
CopyrightâThe copyright string for your script.
- Choose File > Export to display the export dialog.
Choose File > Export to display the export dialog.
- Type a name for the applet and choose an output folder.
Type a name for the applet and choose an output folder.
- Choose a format from the File Format popup menu.
Choose a format from the File Format popup menu.
- If youâre saving in application format, choose whether you want a startup screen or a stay-open script.
If youâre saving in application format, choose whether you want a startup screen or a stay-open script.
- Choose whether you want to save the script as run-only.
Choose whether you want to save the script as run-only.
- Choose your developer identity from the Code Sign popup menu.
Choose your developer identity from the Code Sign popup menu.
- Click Save.
Click Save.
Creating a Script
Running a Script
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13