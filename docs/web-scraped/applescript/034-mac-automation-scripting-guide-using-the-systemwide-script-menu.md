# Mac Automation Scripting Guide: Using the Systemwide Script Menu

## Using the Systemwide Script Menu
The OSÂ X script menu provides quick access to your collection of scripts. Simply select a script in the menu at any time to run it instantly. Within the script menu, scripts can be organized into subfolders and by application. SeeFigure 41-1.
Note
The script menu can run compiled scripts, as well as scripts saved as apps. It can also run UNIX shell scripts and Automator workflows.

### Enabling the Script Menu
The script menu is disabled by default in OSÂ X.
- Launch Script Editor, located in/Applications/Utilities/.
Launch Script Editor, located in/Applications/Utilities/.
- Select Script Editor > Preferences, or press Command-Comma (,), to open the preferences window.
Select Script Editor > Preferences, or press Command-Comma (,), to open the preferences window.
- Click General in the toolbar.
Click General in the toolbar.
- Enable the âShow Script menu in menu barâ checkbox.
Enable the âShow Script menu in menu barâ checkbox.
- Choose whether application scriptsâscripts that appear only when a corresponding app is in the frontâshould appear at the top or bottom of the script menu.
Choose whether application scriptsâscripts that appear only when a corresponding app is in the frontâshould appear at the top or bottom of the script menu.
The script menu displays scripts in the~/Library/Scripts/folder of your user directory. To include scripts at the computer-level (in the/Library/Scripts/folder), enable the âShow Computer scriptsâ checkbox.

### Adding User-Level Scripts to the Script Menu
User-level scripts are scripts that only you can see and use. They arenât available to other users on your Mac.
To add user-level scripts to the script menu, save them into the~/Library/Scripts/folder of your user directory. For quick access to this folder, select Open Scripts Folder > Open User Scripts Folder from the script menu. When you do this, the folder is automatically created if it doesnât already exist.

### Adding Computer-Level Scripts to the Script Menu
Computer-level scripts are scripts that any user on your Mac can see and use.
To add computer-level scripts to the script menu, save them into the/Library/Scripts/folder on your Mac. For quick access to this folder, select Open Scripts Folder > Open Computer Scripts Folder from the script menu. When you do this, the folder is automatically created if it doesnât already exist.

### Adding Application-Specific Scripts to the Script Menu
Application-specific scripts are only visible in the script menu when a specific app is in the front.
To add application-specific scripts to the script menu, save them into the~/Library/Scripts/Applications/Â«ApplicationNameÂ»folder in your user directory or the/Library/Scripts/Applications/Â«ApplicationNameÂ»folder on your Mac. For quick access to this folder, bring the app to the front, then select Open Scripts Folder > Open Â«ApplicationNameÂ» Scripts Folder from the script menu. When you do this, a folder for the application is automatically created if it doesnât already exist.

### Running Scripts in the Script Menu
Select a script from the script menu to run it. If the script is an application, it launches and runs normally. If the script is a compiled script, a progress indicator appears in the menu bar. SeeFigure 41-2.
Note
To reveal a script in the script menu, select it in the menu while pressing the Shift key.
To open a script menu script in Script Editor, select it in the menu while pressing the Option key.
Making a Systemwide Service
Using Dictation to Run Scripts
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13