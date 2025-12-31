# Source: https://iterm2.com/documentation-command-selection.html

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

# Command Selection and Command URLs Syntax

If you have [Shell Integration](documentation-shell-integration.html) installed, you can click on a command or its output to select it.

The selection is indicated by drawing a colored line around the command and its output. Other areas are dimmed.

When a command is selected:

- Search is restricted to the selected region.

- Filtering is restricted to the selected region.

- **Select All** is restricted to the selected region.

- You can use Cmd-Up and Cmd-Down to navigate to the previous and next commands.

Additionally, various buttons appear at the top right of the selected region:

- An Info button, which opens the Command Info panel. This reveals information about the command such as how long it ran and its exit status and gives you controls to re-send, copy, share, and more.

- A Share button, which opens a menu allowing you to save, copy, or share the command.

- A bookmark button, which allows you to create a "named mark". You can find named marks under **Edit > Named Marks** or in the **Named Marks** tool in the toolbelt. This makes it easy to navigate back to a command later on.

- A copy button, which lets you copy the command or its output.

### Disabling

To disable command selection turn off **Settings > General > Selection > Clicking on a command selects it to restrict Find and Filter**. You can also select a command and click the settings button on the top right to open a menu that lets you disable the feature.

### Command URLs

The share button introduces the concept of command URLs. Here is a simple example of a command URL: `iterm2:/command?c=date`.

The scheme is always `iterm2` and the path is always `/command`.

If a hostname is present, iTerm2 will attempt to ssh to the host to run the command. For exmaple, `iterm2:[[email&#160;protected]](https://iterm2.com/cdn-cgi/l/email-protection)/command?c=date` runs `date` on host `example.com` as user `gnachman`.

The optional `d` query parameter gives a directory to change into prior to running the command.

Normally when you open a command URL you are presented with a window that describes what will be done and offers options on how to run it (e.g., in a new tab, a new window, or in the current session). The optional `silent` query parameter suppresses this window. A confirmation dialog is shown instead. If the user consents, the command runs in the background and its output is not shown. This query parameter does not take a value.