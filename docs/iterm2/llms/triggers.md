# Source: https://iterm2.com/documentation-triggers.html

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

# Triggers

A trigger is an action that is performed when text matching some regular expression is received in a terminal session.

#### How to Create a Trigger

To create a trigger, open the **Settings** panel. Select the **Profiles** tab. Choose the profile to which you wish to add a trigger. Then select the **Advanced** tab. Click the **Edit** button in the **Triggers** section. A panel opens that displays any existing triggers. You can click the **+** button to add a new trigger.

Triggers have a regular expression, an action, an optional parameter, and may be marked as *Instant*.

#### Regular Expression

Regular expressions conform to the [ICU regular expressions](https://unicode-org.github.io/icu/userguide/strings/regexp.html) rules. Text that is written to the screen including the BEL control code are sent to the regex matcher for evaluation. Only one line at a time is matched. By default, matching is performed when a newline or cursor-moving escape code is processed. If a line is very long, then only the *last* three wrapped lines are used (that is, the last three lines as seen on the display). This is done for performance reasons. You can change this limit in Advanced Settings > Number of screen lines to match against trigger regular expressions.

#### Actions

The following actions are available:

        - Annotate: Associates a note with a matching text.

        - Bounce Dock Icon: Makes the dock icon bounce until the iTerm2 window becomes key.

        - Capture Output: Save the line to the Captured Output toolbelt tool. See [Captured Output](documentation-captured-output.html). The parameter is text to send (as though it had been typed) when you double-click on an entry in the Captured Output tool.

        - Change Style: Modifies the style of matching text.
        Fold to Named Mark: Collapses all lines between the matching line and a preceding named mark with a given name.

        - Highlight Line: The entire line containing text matching the regex in the trigger will change color. The parameter sets the color.

        - Highlight Text: The text matching the regex in the trigger will change color. The parameter sets the color.

        - Inject Data: Inserts bytes into the input stream. These can be text or control sequences.

        - Invoke Script Function: Executes a function call defined using the Python API.

        - Make Hyperlink: The text matching the regex in the trigger will become a hyperlink which you can open with Cmd-Click. The parameter sets the URL.

        - Open Password Manager: Opens the password manager. You can specify which account to select by default.

        - Post Notification: Posts a notification with Notification Center.

        - Prompt Detected: Informs iTerm2 that the shell prompt begins at the start of the match. Used to emulate Shell Integration features. If the prompt is one line long then use Instant.

        - Report Directory: Tells iTerm2 what your current directory is. You can use this to enable [Shell Integration](documentation-shell-integration.html) features without installing the scripts. The parameter is your current directory.

        - Report User & Host: Tells iTerm2 what your user or host name is. You can use this to enable [Shell Integration](documentation-shell-integration.html) features without installing the scripts. To specify just a user name, say `user@`. For just a host, say `@host`. For both, say `user@host`.

        - Ring Bell: Plays the standard system bell sound once.

        - Run Command: Runs a user-defined command.

        - Run Coprocess: Runs a [Coprocess](documentation-coprocesses.html).

        - Run Silent Coprocess: Runs a [Coprocess](documentation-coprocesses.html) but do not show text that's being received (it only goes to the coprocess).

        - Send Text: Sends user-defined text back to the terminal as though the user had typed it.

        - Set Mark: Sets a mark. You can specify whether you'd like the display to stop scrolling after the trigger fires.

        - Set Named Mark: Associates a name with the matching range. Various features help you navigate to named marks such as the Toolbelt tool and Open Quickly.

        - Set Title: Sets the session's title.

        - Set User Variable: Assigns a value to a user-defined [variable](https://iterm2.com/documentation-variables.html).

        - Show Alert: Shows an alert box with user-defined text.

        - Stop Processing Triggers: When this action is invoked no triggers further down the list will be invoked for the current text.

#### Parameter?

Various actions (Run Command, Run Coprocess, Post Notification, Send Text, and Show Alert) require additional information. This is specified in the "Parameters" field. When the paramter is a text field with freeform entry, some special values are defined:

                        Value
                        Meaning

                        \0
                        The entire value matched by the regular expression.

                        \1, \2, ..., \9
                        The nth value captured by the regular expression.

                        \a
                        A BEL character (^G).

                        \b
                        A backspace character ^H.

                        \e
                        An ESC character (ascii 27).

                        \n
                        A newline character.

                        \r
                        A linefeed character.

                        \t
                        A tab character.

                        \xNN
                        A hex value NN (for example: \x1b sends ascii code 27, an ESC).

#### Instant

When *Instant* is set, the trigger will fire once per line as soon as the match occurs, without waiting for a newline. This was added for the benefit of the *Open Password Manager* trigger, since password prompts usually are not followed by a newline. This may cause certain regular expressions (for example, ".*") to match less than they otherwise might.

#### Example

The [iTerm2-zmodem](https://github.com/RobberPhex/iTerm2-zmodem) project demonstrates hooking up iTerm2 to zmodem upload and download.