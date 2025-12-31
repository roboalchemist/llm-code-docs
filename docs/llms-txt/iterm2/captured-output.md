# Source: https://iterm2.com/documentation-captured-output.html

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

# Captured Output

iTerm2 has a feature called "Captured Output" which helps you find and track important lines of output from logs, build processes, and such.

### What does it do?

Captured Output is a tool that may be added to iTerm2's toolbelt (a view on the right side of terminal windows). It works in conjunction with user-defined [Triggers](https://www.iterm2.com/triggers.html). A Trigger whose action is *Capture Output* looks for lines of output that match its regular expression. When one is found, the entire line is added to the Captured Output tool. When the user clicks on a line in the Captured Output tool, iTerm2 scrolls to reveal that line. Double-clicking on a line in the Captured Output tools run a user-defined [Coprocess](https://www.iterm2.com/coprocesses.html).

### Shell Integration Required

[Shell Integration](https://www.iterm2.com/shell_integration.html) must be installed because Captured Output ties in to command history.

Ensure you have enough scrollback history to contain the full output of your build command. The default of 1000 may not be sufficient. You can adjust this in **Prefs > Profiles > Terminal > Scrollback lines**.

### Example

One way to use Captured Output is to view compiler output. Suppose you run *make* and get thousands of lines of output, some of which may contain errors or warnings. You'd like to examine each one and take some action on it. Here's how you would use Captured Output to assist with this task:

#### Step 1: Create Triggers

[Create a Trigger](https://iterm2.com/documentation-triggers.html) with the **Capture Output** action that matches your compiler's errors and warnings. Clang's errors look like this:

```

filename.c:54:9: error: use of undeclared identifier 'foo'

```

The following regular expression matches errors and warnings from Clang:

```

^([_a-zA-Z0-9+/.-]+):([0-9]+):[0-9]+: (?:error|warning):

```

There are two capture groups defined. We'll come back to those later.

#### Step 2: Open the Toolbelt

Open the Toolbelt by selecting the menu item Toolbelt > Show Toolbelt. Enable the Toolbelt > Captured Output menu item to ensure it is visible.

#### Step 3: Run make

Kick off the build by running make. It spits out thousands of lines of output.

#### Step 4: Examine the Captured Output tool

Any errors or warnings that appear in the compiler output will appear in the Captured Output tool.

Select an entry in the tool. iTerm2 scrolls to display the line and briefly highlights it in blue.

#### Step 5: Open the file containing the error

The Trigger created in step 1 takes an optional parameter. It is a command for iTerm2 to execute as a [Coprocess](https://www.iterm2.com/coprocesses.html) when you double-click an entry in the Captured Output tool. An example command is:

```

echo vim \1; sleep 0.5; echo \2G

```

This coprocess command assumes you are at the command line, and it enters a command to open the offending file to the line number with an error. This is where the capture groups in the regular expression from step 1 become useful. For example, if the filename was "filename.c" and the error was on line 20, as in this error message:

```

filename.c:20:9 error: use of undeclared identifier 'foo'

```

The coprocess would:

  - Type "vim filename.c", followed by enter, as though you were typing it at the keyboard.

  - Wait half a second.

  - Type "20G".

#### Step 6: Check it off the list

You can right-click on an entry in Captured Output to open a menu, which contains a single item: "Toggle Checkmark". This helps you remember which entries have been dealt with as you go through errors and warnings in your compiler output.

### Navigation

Captured Output is linked to the Command History tool. If no command is selected in the Command History tool, then the most recent captured output is displayed. Otherwise, the captured output from the selected command is displayed. You can remove a selection from the Command History tool by cmd-clicking on it.

## Clearing Captured Output

You can use the `ClearCapturedOutput` control sequence to remove captured output. This is useful to do before starting a compilation which may produce errors. Doing so ensures the only captured errors are from the most recent build. Use the following command in bash to produce the control sequence:

`printf "\e]1337;ClearCapturedOutput\e\\"`