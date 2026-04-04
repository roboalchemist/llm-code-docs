# Source: https://iterm2.com/documentation-touch-bar.html

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

# Touch Bar

As with many applications, you may customize the controls on the touch bar with **View > Customize Touch Bar**. The following controls are available:

#### Man Page

Opens the manpage for the command behind the cursor.

#### Color Preset

When selected, this opens a scrollable list of color presets. Choosing one changes the current terminal's colors to use the preset.

#### Function Keys

There are two function keys controls. The first, labeled *Function Keys Popover*, opens a scrollable list of function keys when pressed. It is compact but requires two taps to press a function key. The second, labeled *Function Keys*, shows a scrollable list of function keys at all times. It takes more space but is quicker to use.

If you install [Shell Integration](https://www.iterm2.com/documentation-shell-integration.html) and [Utilities](https://www.iterm2.com/documentation-utilities.html), then you'll get a command *it2setkeylabel* that lets you configure what each function key's label says. You can configure each application you use (such as vim or emacs) to set the labels appropriately.

#### Add Mark

The *Add Mark* touch bar control saves the current location in history. You can navigate among marks with Cmd-Shift-Up and Cmd-Shift-Down. There are also touch bar controls to navigate marks.

#### Next/Previous Mark

Navigates to the next or previous mark. If you have [Shell Integration](https://www.iterm2.com/documentation-shell-integration.html) installed, each command prompt inserts a mark, so the previous mark is usually the previous shell prompt.

#### Autocomplete Suggestions

If you have [Shell Integration](https://www.iterm2.com/documentation-shell-integration.html) installed, iTerm2 can remember you command history. That history is used to make suggestions for commands, which appear in this touch bar control.

#### Status

The status touch bar control shows a user-configurable message. If you install [Shell Integration](https://www.iterm2.com/documentation-shell-integration.html) and [Utilities](https://www.iterm2.com/documentation-utilities.html), then you'll get a command *it2setkeylabel* that lets you configure what the status control says. For example, it could display the git branch of the current directory. Tapping it scrolls to the location where the status was last changed.

For example, suppose you want to show your current git branch in the touch bar.

- Select the menu item **View > Customize Touch Bar**

- Drag "Your Message Here" button into the touch bar

- Modify PS1 to include `\[$(it2setkeylabel set status "$message")\]`. For example:

```

PS1='\s-\v\$\[$(~/.iterm2/it2setkeylabel set status \
"$(test -d .git && (git rev-parse --abbrev-ref HEAD) || (echo -n "Not a repo"))")\] '

```

#### Custom Buttons

You can define custom touch bar buttons in **Prefs > Keys > Add Touch Bar Item**. You can then add the item to your touch bar from **View > Customize Touch Bar**.