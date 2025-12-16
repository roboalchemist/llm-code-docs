# Source: https://iterm2.com/documentation-copymode.html

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

# Copy Mode

Copy Mode allows you to make selections using the keyboard. To enter or exit Copy Mode, select Edit > Copy Mode. You can also enter copy mode by pressing  immediately after making a selection with the mouse. A special cursor rendered as a downward-pointing arrow is visible while in Copy Mode.

While in Copy Mode, the sessionâs contents will not change. You can use the keyboard to move the cursor and modify the selection using these keystrokes:

Changing Modes

    Keystroke
    Action

    <C-Space>
    Stop selecting

    <Esc>, q, <C-c>, <C-g>
    Exit copy mode

    <C-v>
    Toggle rectangular selection

    <Space>, v
    Toggle selection by character

    V
    Toggle selection by line

Basic Movement

    Keystroke
    Action

    h, <Left>
    Move left

    j, <Down>
    Move down

    k, <Up>
    Move up

    l, <Right>
    Move right

Content-Based Movement

    Keystroke
    Action

    <M-Left>, <M-b>, <S-Tab>, b
    Move back one word, treating symbols as word breaks.

    <M-Right>, <M-f>, <Tab>, w
    Move forward one word, treating symbols as word breaks.

    B
    Move back one word, treating symbols as part of a word.

    W
    Move forward one word, treating symbols as part of a word.

    [
    Move to previous mark

    ]
    Move to next mark

Screen Movement

    Keystroke
    Action

    <C-b>, <PageUp>
    Move up one screen

    <C-f>, <PageDown>
    Move down one screen

    H
    Move to top of visible area

    M
    Move to middle of visible area

    L
    Move to bottom of visible area

Line Movement

    Keystroke
    Action

    ^, <M-m>
    Move to start of indentation

    0
    Move to start of line

    $
    Move to end of line

    <Return>
    Move to start of next line

Document Movement

    Keystroke
    Action

    g
    Move to start

    G
    Move to end

Other Commands

    Keystroke
    Action

    o
    Swap cursor and other selection endpoint

    <C-k>, y
    Copy selection