# Source: https://iterm2.com/documentation-menu-items.html

[Table of Contents](#)

Introduction

- [Highlights for New Users](https://iterm2.com/documentation-highlights.html)

- [General Usage](https://iterm2.com/documentation-general-usage.html)

User Interface

- [Menu Items](https://iterm2.com/documentation-menu-items.html)

- [Settings](https://iterm2.com/documentation-preferences.html)

- [Touch Bar](https://iterm2.com/documentation-touch-bar.html)

- [Copy Mode](https://iterm2.com/documentation-copymode.html)

- [Fonts](https://iterm2.com/documentation-fonts.html)

- [Profile Search Syntax](https://iterm2.com/documentation-search-syntax.html)

- [Command Selection and Command URLs](https://iterm2.com/documentation-command-selection.html)

- [Status Bar](https://iterm2.com/documentation-status-bar.html)

Features

- [Automatic Profile Switching](https://iterm2.com/documentation-automatic-profile-switching.html)

- [Badges](https://iterm2.com/documentation-badges.html)

- [Buried Sessions](https://iterm2.com/documentation-buried-sessions.html)

- [Captured Output](https://iterm2.com/documentation-captured-output.html)

- [Coprocesses](https://iterm2.com/documentation-coprocesses.html)

- [Hotkeys](https://iterm2.com/documentation-hotkey.html)

- [Session Restoration](https://iterm2.com/documentation-restoration.html)

- [Shell Integration](https://iterm2.com/documentation-shell-integration.html)

- [Smart Selection](https://iterm2.com/documentation-smart-selection.html)

- [tmux Integration](https://iterm2.com/documentation-tmux-integration.html)

- [Triggers](https://iterm2.com/documentation-triggers.html)

- [Utilities](https://iterm2.com/documentation-utilities.html)

- [Web Browser](https://iterm2.com/documentation-web.html)

- [AI Chat](https://iterm2.com/documentation-ai-chat.html)

Scripting

- [Scripting Fundamentals](https://iterm2.com/documentation-scripting-fundamentals.html)

- [Scripting Variables](https://iterm2.com/documentation-variables.html)

- [Python API](https://iterm2.com/python-api)

- [Scripting with AppleScript (Deprecated)](https://iterm2.com/documentation-scripting.html)

Advanced

- [Dynamic Profiles](https://iterm2.com/documentation-dynamic-profiles.html)

- [Inline Images Protocol](https://iterm2.com/documentation-images.html)

- [Proprietary Escape Codes](https://iterm2.com/documentation-escape-codes.html)

# Menu Items

[&#x25b8; iTerm2 Menu](javascript:showId('menu-iterm2'))
[&#x25be; iTerm2 Menu](javascript:hideId('menu-iterm2'))

#### iTerm2 > Show Tip of the Day

When you start using iTerm2 it will offer to show you a daily tip describing a feature. You can show a tip immediately by selecting this item.

#### iTerm2 > Check for Updates

Checks to see if a new version of iTerm2 is available. If Settings > General > Prompt for test-release updates is turned on then this includes beta versions; otherwise only stable versions are downloaded.

#### iTerm2 > Toggle Debug Logging

This saves helpful debugging information in memory. When it is toggled off it is saved to /tmp/debuglog.txt.

#### iTerm2 > Copy Performance Stats

This copies information about drawing speed to the pasteboard. This is useful when reporting issues relating to poor performance.

#### iTerm2 > Capture GPU Frame

This saves information about how the current session is drawn. This is useful when reporting issues relating to drawing errors in the GPU renderer.

#### iTerm2 > Secure Keyboard Entry

When this is enabled, the operating system will prevent other programs running on your computer from being able to see what you are typing. If you're concerned that untrusted programs might try to steal your passwords, you can turn this on, but it may disable global hotkeys in other programs.

#### iTerm2 > Make iTerm2 Default Term

Makes iTerm2 the default terminal for opening .command, .tool, .zsh, .csh, and .pl files.

#### iTerm2 > Make Terminal Default Term

You must hold down Option for this entry to be visible. Makes Terminal.app the default terminal for opening .command, .tool, .zsh, .csh, and .pl files.

#### iTerm2 > Install Shell Integration

This opens a window that guides you through the installation of the [Shell Integration](https://iterm2.com/shell_integration.html) features.

[&#x25b8; Shell Menu](javascript:showId('menu-shell'))
[&#x25be; Shell Menu](javascript:hideId('menu-shell'))

#### Shell > New Window/Tab

This creates a new window or tab with the default profile. If the current session is a tmux integration session, then you will be prompted for whether to create a local or tmux session.

#### Shell > New Window/Tab with Current Profile

This creates a new tab using the same profile as the current session rather than the default profile.

#### Shell > Duplicate Tab/Window

Creates another tab with the same arrangement of split panes, profile, etc.

#### Shell > Split Vertically/Horizontally

These menu items allow you to divide a tab into two or more split panes. The panes can be adjusted by dragging the line that divides them. They will use the default profile.

#### Shell > Split Vertically/Horizontally with Current Profile

These menu items allow you to divide a tab into two or more split panes. The panes can be adjusted by dragging the line that divides them. They will use the profile of the current session.

#### Shell > Save Contents

Save the entire contents of the current session to a file.

#### Shell > Save Selected Text

Saves the selected text to a file.

#### Shell > Close

Terminates the current session.

#### Shell > Close Terminal Window

Terminates all sessions in the current window.

#### Shell > Close All Panes in Tab

Terminates all sessions in the current tab.

#### Shell > Undo Close

Undoes closing a session, tab, or window if the time limit has not expired yet. You can set the limit under **Settings > Profiles > Session > Undo can revive a session that has been closed for up to X seconds**.

#### Shell > Broadcast Input > ...

These options allow you to send keyboard input to more than one session. Be careful.

- **Send input to current session only**: The default setting.

- **Broadcast to all panes in all tabs**: Anything you type on the keyboard goes to all sessions in this window.

- **Broadcast to all panes in current tab**: Anything you type on the keyboard goes to all sessions in this tab.

- **Toggle broadcast input to current session**: Toggles whether this session receives broadcasted keystrokes within this window.

- **Show Background Pattern Indicator**: If selected, sessions receiving broadcast input get an obnoxious red-stripe background.

#### Shell > tmux > ...

These commands let you interact with the tmux integration

- **Detach**: Detaches from the tmux session associated with the current pane. It remains running in the tmux server.

- **New tmux Window/Tab**: Creates a new tmux window, which appears in either a native window or tab, as requested.
8 **Dashboard**: The tmux dashboard is a view that lets you see all your tmux sessions and windows at a glance, adjust which are visible, rename them, and change the current tmux session.

#### Shell > ssh > Disconnect

Closes an SSH integration SSH connection.

#### Shell > ssh > Download files

Available when SSH Integration is in use. Opens a file picker showing files on currently connected remote hosts. Selecting one or more files downloads them.

#### Shell > Print

[I'm thinking printers!](https://theonion.com/new-apple-ceo-tim-cook-im-thinking-printers-1819572893/)

[&#x25b8; Edit Menu](javascript:showId('menu-edit'))
[&#x25be; Edit Menu](javascript:hideId('menu-edit'))

#### Edit > Undo Close Session/Tab/Window

After you close a session, tab, or window then you have five seconds to undo it. The amount of time is configurable in Settings > Profiles > Session.

#### Edit > Copy (With Styles)

Hold down Option to turn Copy into Copy With Styles, which includes fonts and color information in the copied text.

#### Edit > Copy with Control Sequences

Copies the selected text, including control sequences that will reproduce the appearance (bold, colors, etc.) of the copied text when pasted into a terminal. Note that these will not be exactly the control sequences that were originally received, but instead a reconstruction that has the same effect.

#### Edit > Copy Mode

Enters *Copy Mode* which lets you make selections using the keyboard. See [Copy Mode](documentation-copymode.html) for details.

#### Edit > Paste Special > Advanced Paste

This opens the Advanced Paste window which lets you select a string from the pasteboard in recent history, select different representations of the current pasteboard, and modify the string before pasting it. You can modify it by appling a regex substitution, using various built-in modifiers (such as base-64 encoding), or edit it by hand.

#### Edit > Paste Special > Paste Selection

Pastes the currently selected text (which may differ from the text in the pasteboard).

#### Edit > Paste Special > Paste File Base64-Encoded

If there is a file on the pasteboard then this is enabled. When invoked, it base64-encodes the file and pastes the encoded value.

#### Edit > Paste Special > Paste Slowly

"Paste Slowly" pastes the current string in the clipboard, but it doesn't send the whole string at once. It is sent in batches of 16 bytes with a 125ms delay between batches.

#### Edit > Paste Special > Paste Faster/Slower

Adjusts the speed of pasting to be faster or slower.

#### Edit > Paste Special > Paste Slowly Faster/Slower

Adjusts the speed of slow pasting to be faster or slower. You must hold down option for this menu item to be visible.

#### Edit > Paste Special > Warn Before Multi-Line Paste

When enabled, you'll be warned before pasting more than one line.

#### Edit > Paste Special > Limit Multi-Line Paste To Shell Prompt

If *Warn Before Multi-Line Paste* is on, then this restricts it to warn only when you're at the shell prompt. It only works if shell integration is installed, since otherwise iTerm2 cannot tell when you're at the shell prompt.

#### Edit > Paste Special > Prompt to Convert Tabs to Spaces when Pasting

If *Prompt to Convert Tabs to Spaces when Pasting* is enabled, you'll be asked whether to convert tabs to spaces when pasting text containing tab characters.

#### Edit > Paste Special > Warn Before Pasting One Line Ending in a Newline at Shell Prompt

This requires shell integration to be installed to work. If you try to paste one line that ends in a newline while at the shell prompt and this is enabled, you'll get a confirmation dialog before the text is pasted.

#### Edit > Replace Selection > Render Selection Natively

Replaces the selection with a native rendering. For example, Markdown is replaced with formatted text with different font sizes, weights, etc.

#### Edit > Replace Selection > Replace with Pretty-Printed JSON

Replaces the selection with nicely formatted JSON. You can click in the margin to collapse sections.

#### Edit > Replace Selection > Replace with Base 64-Encoded/Decoded Value

Replaces the selection by encoding or decoding its value. Note the selection must be an entire line, not a portion of a line.

#### Edit > Engage Artificial Intelligence

Passes the value at the cursor to AI as a prompt. If there is no value, you'll be asked to provide a prompt. If you have shell integration installed and keyboard focus is on the terminal, then iTerm2 will use what you've typed so far at the command prompt as the input to the AI.

#### Edit > Explain Output with AI

This is available when there is a selection or a selected command. That text will be sent to AI to explain. The terminal contents will be modified, adding annotations detailing what parts of the text mean. The chat window will open so you can drill down more.

#### Edit > Snippets

Gives access to Snippets, which are saved bits of text that can be pasted quickly. You can change snippets in **Prefs>Shortcuts>Snippets**.

#### Edit > Actions

Gives access to Actions, which are user-defined actions similar to those that can be bound to a keystroke. You can change actions in **Prefs>Shortcuts>Actions**.

#### Edit > Open Selection

Opens the selected text using semantic history or as a URL, if it is URL-like.

#### Edit > Jump to Selection

Scrolls the selection to be visible.

#### Edit > Selection Respects Soft Boundaries

When enabled, vertical lines of pipe characters `|` will be interpreted as pane dividers (as in vim or emacs) and selection will wrap at them.

#### Edit > Select Output of Last Command

Requires shell integration to be installed. Selects the output of the last command.

#### Edit > Select Current Command

Requires shell integration to be installed. Selects the text of the current command entered at the command prompt.

#### Edit > Find > Find

Opens or focuses the find panel. Select the down arrow to the left of the search field to open the options menu, which lets you select case insensitivity and regular expression options. The default case sensitivity option of "Smart Case Sensitivity" performs a case-sensitive search if the search query contains any upper case letters. Otherwise, a case-insensitive search is performed.

#### Edit > Find > Find Next/Previous

Next and previous are, by default, reversed from the macOS standard because in a terminal you generally want to search backwards. You can use **Settings > Advanced > Swap Find Next and Find Previous** to get the standard behavior.

#### Edit > Find > Find Globally

Opens a window that lets you search all tabs at once.

#### Edit > Find > Select Matches

Converts Find matches into selections.

#### Edit > Find > Find URLs

Searches the current session for URLish looking strings.

#### Edit > Find > Find All Smart Selection Matches

Searches for all smart selection regular expressions at once.

#### Edit > Find > Pick Result to Open

Shows a shortcut next to each find match. Typing the shortcut opens it using smart selection or, if it is URL-like, using the default URL handler.

#### Edit > Find > Filter

Opens a panel where you can enter text to filter by. Non-matching lines are temporarily hidden until the filter panel is closed.

#### Edit > Marks and Annotations > Set Mark

Records the current scroll position. Use Edit > Jump to Mark to restore the scroll position.

#### Edit > Marks and Annotations > Jump to Mark

Makes the last mark (either created by **Set Mark** or by shell integration) visible by scrolling to it.

#### Edit > Marks and Annotations > Next/Previous Mark

Reveals the next/previous mark by scrolling and highlighting it in blue or red (red if it was tagged as a failing command).

#### Edit > Marks and Annotations > Add Annotation at Cursor

Adds an annotation to the word beginning at the cursor. An annotation is a scratchpad for you to write notes about a chunk of text in your history.

#### Edit > Marks and Annotations > Next/Previous Annotations

Reveals the next/previous annotation.

Adds an annotation to the word beginning at the cursor. An annotation is a scratchpad for you to write notes about a chunk of text in your history.

#### Edit > Marks and Annotations > Alerts > Alert on Next Mark

When a mark is set (typically by [Shell Integration](documentation-shell-integration.html) when the currently running shell command terminates) then show an alert.

#### Edit > Marks and Annotations > Alerts > Alert on Marks in Offscreen Sessions

When disabled, **Alert on Next Mark** alerts even if the session is not currently visible. When enabled, only visible sessions (those that are in a non-hidden window in a selected tab) will alert.

#### Edit > Clear Buffer

Clears the entire terminal history and the mutable area.

#### Edit > Clear Instant Replay

Erases instant replay history for the current session.

### Edit > Clear Scrollback Buffer

Clears scrollback history, preserving the mutable area.

#### Edit > Clear to Start Of Selection

Erases text between the start of the selection and the end.

#### Edit > Clear to Last Mark

Erases text between the last mark and the end.

[&#x25b8; View Menu](javascript:showId('menu-view'))
[&#x25be; View Menu](javascript:hideId('menu-view'))

#### View > Show Tabs in Fullscreen

If enabled, tabs are shown in fullscreen windows.

#### View > Toggle Full Screen

Enters or exists full screen mode. iTerm2 supports both the standard macoS full screen mode, where the window occupies its own Space, and its traditional full screen mode that shares a Space with other windows. You can control which is used in **Settings > General > Native full screen windows**.

#### View > Toolbelt > Set Default Width

Saves the current window's toolbelt width as the default width for new windows' toolbelts.

#### View > Toolbelt > Show Toolbelt

This toggles the visibility of the Toolbelt on the right side of all windows.

#### View > Toolbelt > Actions

This toggles the visibility of the Actions tool, which shows actions you have configured under **Settings > Shortcuts > Actions**.

#### View > Toolbelt > Captured Output

This toggles the visibilty of the Captured Output tool. It shows captured output located with the Capture Output trigger. See [Captured Output](documentation-captured-output.html) for more information.

#### View > Toolbelt > Codecierge

This toggle the visibility of an AI assitant that helps you complete tasks in the terminal.

#### View > Toolbelt > Command History

This toggles the visibility of the Command History tool. It shows recently used commands. You must install [Shell Integration](documentation-shell-integration.html) for this to know your command history.

#### View > Toolbelt > Jobs

This toggles the visibility of the Jobs tool, which shows the running jobs in the current session, and allows you to send them signals.

#### View > Toolbelt > Named Marks

This toggles the visibility of the Named Marks tool, which helps you navigate to saved locations in the current session's history. In browser sessions, named marks take you to saved locations on a web page.

#### View > Toolbelt > Notes

This toggles the visibility of the Notes tool, which provides a freeform scratchpad in the toolbelt. Notes persist across restarts of the app and are saved in `~/Library/Application Support/iTerm2/notes.rtfd`.

#### View > Toolbelt > Paste History

This toggles the visibility of the Paste History tool, which shows recently pasted strings in the toolbelt.

#### View > Toolbelt > Profiles

This toggles the visibility of the Profiles tool, which lets you select profiles to open new windows, tabs, and split panes.

#### View > Toolbelt > Recent Directories

This toggles the visibility of the Recent Directories tool. It shows recently used directories sorted by a combination of recency and frequency of use. You must install [Shell Integration](documentation-shell-integration.html) for this to know your directory history. You can right click a directory to open a context menu that allows you to "start" a directory. This keeps it pinned at the bottom of the list so it's easy to find.

#### View > Toolbelt > Snippets

This toggles the visibility of the Snippets tool, which helps you send frequently used text strings.

#### View > Use Transparency

This toggles transparency. It only has an effect if you have configured your session to be transparent under Settings > Profiles > Window > Transparency. When Full Screen mode is entered, transparency is turned off by default, but you can select this menu item to re-enable it.

#### View > Disable Transparency for Active Window

When enabled, the active window will never be transparent. Inactive windows will respect the transparency setting from **Settings > Profiles > Window > Transparency**.

#### View > Zoom In on Selection

When a selection is present this is enabled. Zooming on a selection removes all other text from the session and lets you focus on just the zoomed-in-on text. Pressing escape will invoke Zoom Out when you are in the Zoom In state.

#### View > Zoom Out

Exits the *Zoom In on Selection* mode.

#### View > Find Cursor

Reveals the current cursor position.

#### View > Show Cursor Guide

Toggles the visiblity of the cursor guide which is a horizontal rule showing the location of the cursor.

#### View > Show Timestamps

Indicate the time of last modification of each line on the screen.

#### View > Show Annotations

Toggles the visibility of annotations.

#### View > Show Composer

Toggles the visibility of the Composer, a text area that you can edit using native macOS keystrokes. This is convenient for preparing complex inputs.

#### View > Auto Command Completion

Automatically shows a window with command completion suggestions as you type. Only usable when you have command history built up with [Shell Integration](documentation-shell-integration.html).

#### View > Auto Composer

Replaces the shell prompt with a macOS native text editing control. It offers filename and command completion, including over ssh when using SSH Integration. It requires [Shell Integration](documentation-shell-integration.html) to be installed in order to work.

#### View > Open Quickly

If you have lots of sessions you can quickly find the one you're looking for with Open Quickly. Select the View > Open Quickly menu item (cmd-shift-O) and then enter a search query. You can search by tab title, command name, host name, user name, profile name, directory name, badge label, and more. Queries are scored according to relevance and sorted by score. Open Quickly also lets you create new tabs, change the current session's profile, and open arrangements. If you start your query with a / then that gives you a shortcut to various commands. /a followed by an arrangement name restores the arrangement. /f restricts the query to existing sessions, excluding options to open new tabs, etc. /p restrics the query to profile names to switch the current session to. /t restricts the results to "open new tab" for matching profile names.

#### View > Maximize Active Pane

When there are split panes present, this toggles whether a given pane expands to fill the tab. When a maximized pane is present, the tab will be inscribed with a dotted outline.

#### View > Size Changes Update Profile

If enabled, modifying the text size using **View > Make Text Bigger** or **View > Make Text Smaller** will cause the session's profile to be updated with the new font size.

#### View > Start Instant Replay

Stepping through time allows you to see what was on the screen at a previous time. This is different than going back through the scrollback buffer, as interactive programs sometimes overwrite the screen contents without having them scroll back. Once in this mode, you can use the left and right arrow keys to step back and forward, respectively. The "esc" key exits this mode, as does clicking the close button in the bar that appears on the bottom. You can adjust the amount of memory dedicated to this feature in Settings > Instant Replay uses xx MB per session. The more memory you assign, the further back in time you can step.

#### View > Tab Color

Allows you to select a tint color for the tab, to make it easier to distinguish. You can also change the tab color in Settings > Profiles > Colors.

[&#x25b8; Session Menu](javascript:showId('menu-session'))
[&#x25be; Session Menu](javascript:hideId('menu-session'))

#### Session > Edit Session

This opens a window that lets you change the settings of the current session without affecting any other sessions. Changes made in this panel will not be overridden by subsequent changes to the profile. Settings *not* cahnged in this panel will be affected by changes to the profile.

#### Session > Run/Stop Coprocess

Allows you to start and stop a coprocess linked to the current session. [Learn more about coprocesses](https://iterm2.com/documentation-coprocesses.html).

#### Session > Restart Session

After a session ends (e.g., because the shell exits) this menu item becomes enabled. It will re-run your profile's command in the same viewport as the terminated session.

#### Session > Duplicate Session

Creates a new session as similar as possible to the current session. The current directory is preserved and if you are using ssh integration it will connect to the same host.

#### Session > Open Autocomplete...

Shows the autocomplete window, which offers to finish typing a word that you've begun. [Learn more about autocomplete on highlights page](documentation-highlights.html).

#### Session > Open Command History...

If you use [Shell Integration](documentation-shell-integration.html) then Open Command History presents a list of recently used commands to select from.

#### Session > Open Recent Directories...

If you use [Shell Integration](documentation-shell-integration.html) then Open Recent Directories presents a list of recently used directories to select from.

#### Session > Open Paste History...

"Open Paste History" opens a window showing up to the last 20 values that were copied or pasted in iTerm2. You can search its contents by typing a (non-necessarily-consecutive) subsequence of characters that appear in the value. You can use arrow keys and enter to make a selection, or you can click on an item to choose it, and it will be pasted. If you enable the Save copy/pate history to disk preference then these values will persist across sessions of iTerm2.

#### Session > Open AI Chat

Creates a new AI chat and offers to link the current session to it.

#### Session > Triggers

The submenu contains the triggers defined for this session. You can enable or disable them by selecting a menu item. You can also add or edit triggers from here as well as control whether they are enabled for interactive applications. For more information see [Triggers](https://iterm2.com/documentation-triggers.html).

#### Session > Reset

Resets the internal state of the emulator and clears the screen. Use this if you get wedged in a bad state, like the wrong character set or mouse reporting mode is stuck.

#### Session > Log > Log to File

Logging saves all input received in a session to a file on disk.

#### Session > Log > Import/Export Recording

Lets you save or view an instant replay recording.

#### Session > Bury Session/Buried Sessions

Buries or unburies a session. See [Buried Sessions](documentation-buried-sessions.html) for details.

[&#x25b8; Scripts Menu](javascript:showId('menu-scripts'))
[&#x25be; Scripts Menu](javascript:hideId('menu-scripts'))

If you have scripts located in `$HOME/Library/Application Support/iTerm2/Scripts` they'll be added to this menu.

For backward compatibility, `$HOME/Library/Application Support/iTerm/Scripts` will be used if `$HOME/Library/Application Support/iTerm2/Scripts` does not exist.

#### Scripts > Manage > New Python Script

Opens a UI to help you create a new Python API script. See the [Python API](https://iterm2.com/python-api) for more information.

#### Scripts > Manage > Open Python REPL

Opens a window with a Python REPL to facilitate working with the Python API.

#### Scripts > Manage > Manage Dependencies

Opens a window that lets you adjust dependencies of Python API scripts. This is meant for people authoring a script who need to bring in a new PyPI dependency.

#### Scripts > Manage > Check for Updated Runtime

Checks to see if a new version of the Python API Runtime is available.

#### Scripts > Manage > Reveal Scripts in Finder

Opens a Finder window in the Scripts folder.

#### Scripts > Manage > Import

Opens a file picker so you can pick a script file to import. It should have the extension `.its`.

#### Scripts > Manage > Export

Opens a file picker so you can pick a script file to export. This is used for sharing scripts with others. The export file will have the extension `.its`.

#### Scripts > Manage > Console

Opens the Script Console which shows which scripts are running, lets you view their logs, and has other developer tools for authors of Python API scripts. If you are using browser profiles then Javascript logs appear here as well.

[&#x25b8; Profiles Menu](javascript:showId('menu-profiles'))
[&#x25be; Profiles Menu](javascript:hideId('menu-profiles'))

This menu contains a list of profiles. Selecting one opens it in a new tab. Hold option while selecting a profile to open it in a new window, instead.

#### Profiles > Open Profiles...

This opens the "Profiles Window" which allows you to create new windows, tabs, or panes from one or more profiles. You can perform a search by entering text in the search field. Profile names and tags are searched, and the listed profiles are filtered as you type. You can use the up and down arrow keys to make a selection. Pressing enter will open a new tab, while shift-enter will open a new window. You can make multiple selections by holding down shift or cmd and clicking on profiles. The "New Tabs in New Window" button is enabled only when more than one profile is selected: it will open a new window and create a new tab for each profile selected.

#### Profiles > Open All

Opens all profiles in tabs (or in windows, if Option is pressed).

[&#x25b8; Web Menu](javascript:showId('menu-web'))
[&#x25be; Web Menu](javascript:hideId('menu-web'))

The Web menu is only visible when the current session is a web browser profile.

#### Web > Open Location

Puts the cursor in the URL bar.

#### Back/Forward

Standard web back/forward navigation.

#### Web > Reload Page

Reloads the current p age.

#### Web > History

Opens the history page, which shows the sites you have visited in chronological order.

[&#x25b8; Window Menu](javascript:showId('menu-window'))
[&#x25be; Window Menu](javascript:hideId('menu-window'))

#### Window > Arrangements > Save Window Arrangement

Saves all of the window's positions, tabs, and split panes. You can opt to save them with contents to a file or to save them to the collection of window arrangements (without content) that can be restored later from **Window > Arrangements > Restore Window Arrangement (as Tabs) > (arrangement name)**.

#### Window > Arrangements > Load Arrangement From File...

Loads a saved arrangement file, which includes window contents.

#### Window > Change Profile in Arrangement

Use this to edit an existing arrangment. First, restore the arrangement. Then activate one of the sessions from the restored arrangement. Select **Change Profile in Arrangement** and you'll be asked to choose a profile. The arrangement will then be updated to use the selected profile for the corresponding session.

#### Window > Edit Window Title

Opens a dialog that lets you specify a window title as an interpolated string.

#### Window > Tab > Edit Tab Title

Opens a dialog that lets you specify a tab title as an interpolated string.

#### Window > Split Pane > Lock Split Pane Width

Toggles whether the active session's width is locked. A locked split pane does not change its width as the window is resized horizontally.

#### Window > Password Manager

Opens the password manager.

#### Window > AI Chat

Opens the AI Chat window.