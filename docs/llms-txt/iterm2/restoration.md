# Source: https://iterm2.com/documentation-restoration.html

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

# Session Restoration

Session restoration works by running your jobs within long-lived servers rather than as child processes of iTerm2. If iTerm2 crashes or upgrades, the servers keep going. When iTerm2 restarts, it searches for running servers and connects to them. The OS's window restoration feature preserves the content of your window, including scrollback history. iTerm2 marries the restored session to the appropriate server so you can pick up where you were.

tl;dr watch this:
[Demo Video](https://iterm2.com/misc/restoration-demo.mov)

### Notes

- 
You must turn off **System Prefs > Desktop & Dock > Close windows when quitting an application**. For more information on system window restoration, please see [Apple's docs](https://support.apple.com/en-us/HT204005).

- 
You must set **Prefs > General > Startup** to **Use system window restoration settings**.

- 
Force quitting iTerm2, causing it to crash, or upgrading it when prompted should restore your sessions. *NOTE: Quitting iTerm2 with Cmd-Q will terminate your jobs and they won't be restored.* There is an advanced preference to change this behavior, though.

- 
You can toggle this feature with **Prefs>Advanced>Enable session restoration.**, but you *must restart iTerm2 after changing this setting*.

- 
A session that has had only its window contents restored and not the running processes will get a reverse video *Session Restored* banner. A properly restored session will pick up right where you left it.

- 
If you reboot, your jobs will terminate and not be restored. The window contents should be restored.

If you prefer for sessions not to be terminated when you quit iTerm2, turn off **Prefs>Advanced>User-initiated quit (cmd-q) of iTerm2 will kill all running jobs.**