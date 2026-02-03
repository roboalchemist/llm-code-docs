# Mac Automation Scripting Guide: Configuring Scripting Preferences

## Configuring Scripting Preferences
Script Editor preferences allows you to configure a variety of aspects of scripting behavior.

### General Preferences
In the General pane of Script Editor preferences (Figure 9-1), you can configure settings such as the following.
Default LanguageâThe default scripting language when you create new Script Editor documents.
Show âtellâ application menuâThis setting can be enabled to add a tell application menu to the navigation bar. Selecting an app in this menu allows you to direct script execution to the chosen app. InFigure 9-2, the tell application menu is set to the Finder. As a result, the script itself doesnât need to include atell application "Finder"statement. It automatically understands the Finderâs terminology and sends events to the Finder.
In addition, the current application objectâwhich refers to the application currently executing the scriptâreflects the selected application, rather than Script Editor. SeeListing 9-1andListing 9-2.
APPLESCRIPT
Open in Script Editor
- name of current application
- --> Result: "Finder"
JAVASCRIPT
Open in Script Editor
- Application.currentApplication().name()
- // Result: "Finder"
Show inherited itemsâThis setting can be enabled to display inherited object properties in the dictionary viewer. For example, in the Finder, afileobject inherits the attributes of anitemobject. Without this setting enabled, the dictionary entry forfilesimply provide a a pointer to theitementry to view theitemattributes. SeeFigure 9-3. With this option enabled, thefileentry in the Finderâs scripting dictionary includes the attributes of anitem. SeeFigure 9-4.
Script MenuâThese settings allow you to enable and configure a systemwide script menu (Figure 9-5). This menu can be used to organize your scripts and provide access to them in any app.

### Editing Preferences
In the Editing pane of Script Editor preferences, shown inFigure 9-6, you can configure settings such as the following.
Code completionâWhen this option is enabled, Script Editor suggest code completions as you type a script (Figure 9-7).
To accept and insert a code completion suggestion, press the F5 key or the Esc (Escape) key. If multiple code completion choices are available, a code completion dialog appears, allowing you to select a suggestion (seeFigure 9-8).
Tab width and line wrappingâAdjust how indentation and line wrapping occurs in the editor pane of Script Editor documents.
Escape tabs and line breaks in stringsâThis setting only affects AppleScripts. When this option is disabled, tabs and line breaks appear normally in a text string, as shown inFigure 9-9.
When this option is enabled, tabs and line breaks are replaced with escaped character equivalentsâ/tfor a tab, and/rfor a line break. SeeFigure 9-10.

### Formatting Preferences
In the Formatting pane of Script Editor window (Figure 9-11), you can configure the styleâfont, point size, and colorâof various script attributes, including new text, language keywords, comments, and variables. Formatting options are language-specific. Select a language from the Language popup menu to view that languageâs formatting settings.

### History Preferences
In the History pane of Script Editor preferences (Figure 9-12), you can enable or disable the log history, adjust the quantity of log history entries, and enable logging only when the log is visible.

### Plug-ins Preferences
The Plug-ins pane of Script Editor preferences (Figure 9-13) lists any installed Script Editor plug-ins.
Running a Script
About Scripting Terminology
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13