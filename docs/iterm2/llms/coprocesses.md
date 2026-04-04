# Source: https://iterm2.com/documentation-coprocesses.html

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

# Coprocesses

iTerm2 offers support for "coprocesses". This very powerful feature will allow you to interact with your terminal session in a new way.

#### What is a Coprocess?

A coprocess is a job, such as a shell script, that has a special relationship with a particular iTerm2 session. All output in a terminal window (that is, what you see on the screen) is also input to the coprocess. All output from the coprocess acts like text that the user is typing at the keyboard.

One obvious use of this feature is to automate interaction. For instance, suppose you want to automate your presence in a chat room. The following script could be used as a coprocess:

```
#!/usr/bin/python
import sys
while True:
  line = raw_input()
  if line.strip() == "Are you there?":
    print "Yes"
  sys.stdout.flush()

```

You could disappear for years before your friends discover you're gone.

#### How Do I Start a Coprocess?

There are two ways to start a coprocess.

- 
Select "Run Coprocess..." from the Session menu. Enter the name of a command to run as a coprocess.

- 
Create a Trigger in Prefs>Profiles>Advanced and select Run Coprocess... as the action. Give the script to run as a parameter. Triggers also have Silent Coprocesses, which prevent any output from going to the screen. This is useful for ZModem, for example.

#### Usage

A session can not have more than one coprocess at a time. When a coprocess is active, an icon will indicate that in the top right of the session.

#### Technical Details

The coprocess's stdin is a byte-for-byte copy of the input from the session's pty, beginning at the time the coprocess starts. In the case of a trigger-started coprocess, the line of input that triggered it MAY be the first line of input to the coprocess, but this is not guaranteed. If a coprocess is running, triggers with a Run Coprocess action will not fire. The coprocess's stdout stream will be treated the same as keyboard input. A small amount of buffering is provided for both input and output of the coprocess. When a buffer fills, the coprocess will block.