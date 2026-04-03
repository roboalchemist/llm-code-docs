# Mac Automation Scripting Guide: Using Dictation to Run Scripts

## Using Dictation to Run Scripts

Dictation commands is a powerful accessibility feature in OS X that lets you control your Mac using your voice. With dictation commands enabled, simply speak a command and watch it execute. The system comes with dozens of built-in dictation commands for opening apps, selecting menus, and more. You can extend the capabilities of dictation even further by creating your own custom commands using scripting and Automator.

### Enabling Dictation Commands

You must enable dictation commands before you can use them.

- Launch System Preferences and open the Dictation & Speech preference pane.
Launch System Preferences and open the Dictation & Speech preference pane.

- Click the On radio button to enable dictation.
Click the On radio button to enable dictation.

- Click Use Enhanced Dictation.Enhanced dictation lets you perform dictation when your computer is offline, and is required to use dictation commands. Enabling this feature downloads some additional system content to your Mac.
Click Use Enhanced Dictation.
Enhanced dictation lets you perform dictation when your computer is offline, and is required to use dictation commands. Enabling this feature downloads some additional system content to your Mac.

- Open the Accessibility preference pane.
Open the Accessibility preference pane.

- In the list of accessibility features, click Dictation.
In the list of accessibility features, click Dictation.

- Click Dictation Commands.
Click Dictation Commands.

- Select theâEnabled advanced commandsâ checkbox.
Select theâEnabled advanced commandsâ checkbox.

### Creating a Dictation Command Script

Any script can serve as a dictation command. When the command is called, any code in the scriptâsrunhandler runs.

- Launch Script Editor and write a script that performs a task when run.
Launch Script Editor and write a script that performs a task when run.

- Save the script in script format to the~/Library/Speech/Speakable Items/folder in your Home directory.If you want the script to be available to other users on your Mac, save it to the/Library/Speech/Speakable Items/instead.
Save the script in script format to the~/Library/Speech/Speakable Items/folder in your Home directory.
If you want the script to be available to other users on your Mac, save it to the/Library/Speech/Speakable Items/instead.

- Launch System Preferences and open the Accessibility preference pane.
Launch System Preferences and open the Accessibility preference pane.

- In the list of accessibility features, click Dictation.
In the list of accessibility features, click Dictation.

- Click Dictation Commands.
Click Dictation Commands.

- Click + to adde a new dictation command.
Click + to adde a new dictation command.

- Enter a phrase to speak to invoke the script.
Enter a phrase to speak to invoke the script.

- Choose the application context for triggering the command, such as Any Application, Mail, or Safari.
Choose the application context for triggering the command, such as Any Application, Mail, or Safari.

- Choose Run Workflow > Other from the Perform pop-up menu.
Choose Run Workflow > Other from the Perform pop-up menu.

- Click Done.
Click Done.

### Running a Dictation Command Script

To run a dictation commandâscript or otherwiseâpress Fn key twice. When the dictation listener window (Figure 42-1) appears, say the name of the command you want to perform.
To make dictation even easier, select the âEnable the dictation keyword phraseâ checkbox and enter a phrase in System Preferences > Accessibility > Dictation. Once enabled, you donât need to press the Fn key twice anymore to trigger a command. Instead, just say the keyword phrase, followed by the name of the command. For example, if your keyword phrase isComputer, you might say âComputer, send my weekly status report.â

### Creating a Dictation Command Automator Workflow

Automator can also be used to create dictation commands.

- Launch Automator.
Launch Automator.

- Click Dictation Command in the template selection dialog.
Click Dictation Command in the template selection dialog.

- Add actions to the workflow.The Run AppleScript, Run JavaScript, and Run Shell Script actions can be used to initiate scripts from your workflow.
Add actions to the workflow.
The Run AppleScript, Run JavaScript, and Run Shell Script actions can be used to initiate scripts from your workflow.

- At the top of the workflow, enter a dictation command and select the Command Enabled checkbox.
At the top of the workflow, enter a dictation command and select the Command Enabled checkbox.

- Save the workflow and name it.
Save the workflow and name it.
Note
Automator dictation commands are automatically saved in the~/Library/Speech/Speakable Items/folder in your Home directory.
Using the Systemwide Script Menu
Objective-C to AppleScript Quick Translation Guide
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13
