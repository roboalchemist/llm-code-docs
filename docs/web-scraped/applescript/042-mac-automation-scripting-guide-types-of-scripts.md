# Mac Automation Scripting Guide: Types of Scripts

## Types of Scripts
There are many different types of scripts on the Mac.
AppletsâA script thatâs been saved as an app. It behaves like other apps. Double-click it to launch and run it. When an applet is launched, any code in itsrunhandler executes. If a script doesnât contain an explicitrunhandler, then the top level of the script is treated as an implicitrunhandler and any code there executes.
DropletsâA script applet that has been configured to accept dropped files and folders. Double-click it to launch and run itâexecute itsrunhandler. Or, drag and drop files and folders onto it to process them. In a droplet, dropped files and folders are passed directly to an AppleScriptopenhandler or JavaScriptopenDocumentsfunction for processing.
ScriptsâA script document file. Double-click it to open it for editing. Some apps and processes can load and run scripts. For example, Mail rules can execute scripts to process messages matching specific criteria. Scripts are sometimes referred to ascompiled scripts.
Script bundlesâA script document thatâs been saved inbundleformat. A bundle is a directory with a standardized, hierarchical structure that holds executable code and the resources used by that code.
Stay-open scriptsâBy default, applets and droplets run and quit after launch. When configured as stay-open, however, they remain open until explicitly ordered to quit. Often, stay-open scripts include anidlehandler, which initiates periodic actions.
For detailed information aboutrun,open, andidlehandlers in AppleScript, seeHandlers in Script ApplicationsinAppleScript Language Guide. For information aboutrun,openDocuments, andidlefunctions in JavaScript, seeAppletsinJavaScript for Automation Release Notes. For information about bundles, seeBundle Programming Guide.
How Mac Scripting Works
About this Guide
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13