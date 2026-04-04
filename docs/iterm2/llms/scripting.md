# Source: https://iterm2.com/documentation-scripting.html

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

# Applescript

iTerm2 features Applescript support which allows you to automate many aspects of its behavior. Quite a bit of customization is also possible by writing shell scripts.

### Applescript

iTerm2 has sophisticated Applescript support allowing one to write stand-alone scripts to launch the application and open multiple sessions with profiles into either new tabs or new windows. You can also set some other parameters for a session such as foreground and background colors, and transparency.

These scripts can then be saved as stand-alone executable applications.

#### Autolaunching Scripts

iTerm2 also supports autolaunching of an Applescript on startup. On startup, iTerm2 looks for an Applescript file in "~/Library/Application Support/iTerm2/Scripts/AutoLaunch.scpt". If it is found, the "AutoLaunch.scpt" script is launched and executed.

If that folder does not exist, the legacy path of "~/Library/Application Support/iTerm/Scripts/AutoLaunch.scpt" will be used.

#### User-Defined Scripts

iTerm2 also supports launching of user defined scripts from the "Scripts" menu. The scripts need to be stored under the ~/Library/Application Support/iTerm/Scripts directory. You can create this directory if it does not already exist. iTerm2 checks this directory on startup. Scripts must be named with the extension .scpt or .app.

# Reference

## Objects

The basic objects are: window, tab, and session. The application has zero or more windows, each window has one or more tabs, and each tab has one or more sessions. Multiple sessions in a tab happen when there are split panes.

### Application

The application exposes various properties and provides functions that are described in this section. For example:

```
tell application "iTerm2"
  create window with default profile
end tell

```

create hotkey window with profile "*name*"

Creates a hotkey window with the specified profile. The profile must be configured to have a hotkey.

Example:

    create hotkey window with profile "Hotkey Window"

create window with default profile

create window with default profile command "*command*"

These commands create a window with the default profile. If you specify a command, it overrides the profile's command (which by default is to invoke `login`).

Examples:

    set newWindow to (create window with default profile)
    set newWindow to (create window with default profile command "ls -l -R /")

create window with profile "*name*"

create window with profile "*name*" command "*command*"

These commands create a window with a named profile. If you specify a command, it overrides the profile's command (which by default is to invoke `login`).

Returns a reference to the new window.

Examples:

    set newWindow to (create window with profile "Name Of Some Profile")
    set newWindow to (create window with profile "Name Of Some Profile" command "ls -l -R /")

current window

A reference to the window that most recently had keyboard focus.

    tell current window
    ...
    end tell

windows

A `windows` property exposes an array of terminal windows. Other windows, like the Settings panel, are not included.
The following are standard Applescript idioms for accessing elements of an array of objects:

```
tell first window
...
end tell

repeat with aWindow in windows
...
end repeat

```

### Windows

These functions and properties are provided by windows. For example:

```
tell application "iTerm2"
  tell current window
    create tab with default profile
  end tell
end tell

```

There are many standard Applescript functions (e.g., to get the window's size and position) that are not documented here.

create tab with default profile

create tab with default profile command "*command*"
create tab with profile "*name*"
create tab with profile "*name*" command "*command*"

Creates a tab with the default profile or a profile by name. If the command is specified, it is run instead of the profile's command/login shell.

Returns a reference to the new tab.

current session

The `current session` is the session that would receive keyboard input if the window had keyboard focus.

current tab

The `current tab` is the tab that is selected in the window.

hide hotkey window

If this is a hotkey window, it hides it with the standard hotkey window animation and makes the previously active application active, if appropriate.

hotkey window profile

Returns the name of the hotkey window profile associated with this window, if any.

id

The window ID. Useful for commands like `screencapture`.

is hotkey window

Returns a boolean value which is true if the window is a hotkey window associated with a profile.

name

The window's name, as appears in the title bar.

reveal hotkey window

If this is a hotkey window, it reveals it with the standard hotkey window animation and makes it key and the application active.

select

Gives the window keyboard focus and brings it to the front.

tabs

An array of tabs. See the methods on Tab, below.

toggle hotkey window

Either shows or hides the hotkey window, if this is a hotkey window, using the standard animation. May make the app active or inactive.

### Sessions

These functions and properties are provided by sessions. For example:

```
tell application "iTerm2"
  tell current session of current window
    split horizontally with default profile
  end tell
end tell

```

background image

This is a string property that gives a path to the background image of the session.

close

Terminates the session and closes its pane.

Color properties

Various properties which are readable and settable affect the session's colors:

- background color

- bold color

- cursor color

- cursor text color

- foreground color

- selected text color

- selection color

- ANSI black color

- ANSI red color

- ANSI green color

- ANSI yellow color

- ANSI blue color

- ANSI magenta color

- ANSI cyan color

- ANSI white color

- ANSI bright black color

- ANSI bright red color

- ANSI bright green color

- ANSI bright yellow color

- ANSI bright blue color

- ANSI bright magenta color

- ANSI bright cyan color

- ANSI bright white color

An example:

```
set foreground color to {65535, 0, 0, 0}

```

Because Applescript is kind of a dumpster fire, the standard syntax for a color is `{red, green, blue, alpha}` where each value is a number between 0 and 65535.

answerback string

The string sent when the `ENQ` escape sequence is received.

columns

The width of the session in character cells.

contents

Returns the visible contents of the session as a string. Each row is terminated with a newline.

id

Returns the session's unique identifier.

is at shell prompt

Indicates if the session is at a shell prompt accepting a command. Only works if [Shell Integration](https://iterm2.com/shell_integration.html) is installed; if not it will return false.

is processing

Returns a boolean indicating if the session received output recently.

name

A string property with the session's name as seen in its title bar.

profile name

The name of the profile the session was created with. A string. Read-only.

rows

The height of the session in character cells.

set columns to *number*

set rows to *number*

Changes the size of the session.

split horizontally with default profile

split vertically with default profile

split horizontally with default profile command "*command*"

split vertically with default profile command "*command*"

Splits the session either horizontally or vertically. If the optional *command* is provided then it is run in place of the profile's command. A horizontal split has a horizontal divider, while a vertical split has a vertical divider.

Returns a reference to a session.

split horizontally with profile "*name*"

split vertically with profile "*name*"

split horizontally with profile "*name*" command "*command*"

split vertically with profile "*name*" command "*command*"

Like the "default profile" commands, but uses a named profile instead of the default profile.

split horizontally with same profile

split vertically with same profile

split horizontally with same profile command "*command*"

split vertically with same profile command "*command*"

Like the "default profile" commands, but uses the current session's profile.

select

Makes the session active in its tab. Does not affect which tab is selected or which window has keyboard focus.

text

A synonym for `contents`.

transparency

A floating-point value from 0 to 1 giving how transparent the session is.

tty

The name of the session's tty (e.g., /dev/ttys01). Returns a string.

unique id

A string uniquely identifying the session.

variable "*name*"

set variable named "*name*" to "*value*"

Gets and sets the value of a variable by name. Variables are described in [Badges](https://iterm2.com/badges.html). You may only set user-defined variables, whose names always begin with "user.".

write text "*text*"

write text "*text*" newline NO

Writes text to the session, as though you had typed it. Optionally without a newline.

write contents of file "*filename*"

Writes the contents of a file to the session as though you had typed it.

### Tabs

These functions and properties are provided by tabs. For example:

```
tell application "iTerm2"
  tell current tab of current window
    select
  end tell
end tell

```

close

Closes the tab.

current session

The session in this tab that most recently had keyboard focus.

index

The index of the tab in the window, starting from 0.

select

Selects the tab, making it the current tab for the window.

sessions

An array of sessions.

sessions

An array of sessions in this tab.

The index from 0 of the tab in its window.

## Supporting both old and new versions of iTerm2

If your application needs to support both the old and new Applescript syntax, this is the recommended technique:

```

on theSplit(theString, theDelimiter)
    set oldDelimiters to AppleScript's text item delimiters
    set AppleScript's text item delimiters to theDelimiter
    set theArray to every text item of theString
    set AppleScript's text item delimiters to oldDelimiters
    return theArray
end theSplit

on IsModernVersion(version)
    set myArray to my theSplit(version, ".")
    set major to item 1 of myArray
    set minor to item 2 of myArray
    set veryMinor to item 3 of myArray
    
    if major  2 then
        return true
    end if
    if minor  9 then
        return true
    end if
    if veryMinor < 20140903 then
        return false
    end if
    return true
end IsModernVersion

on NewScript()
    -- Return the modern script as a string here; what follows is an example.
    return "create window with default profile"
end NewScript

on OldScript()
    -- Return the legacy script as a string here; what follows is an example.
    return "
    set myTerm to (make new terminal)
    tell myTerm
        launch session \"Default\"
    end tell"
end OldScript

tell application "iTerm"
    if my IsModernVersion(version) then
        set myScript to my NewScript()
    else
        set myScript to my OldScript()
    end if
end tell

set fullScript to "tell application \"iTerm\"
" & myScript & "
end tell"

run script fullScript

```