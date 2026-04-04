# Source: https://iterm2.com/documentation-smart-selection.html

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

# Smart Selection

iTerm2 offers a Smart Selection feature that simplifies making selections on semantically recognizable objects.

#### How do I use Smart Selection?

A quad-click (four clicks of the left mouse button in quick succession) activates Smart Selection at the mouse cursor's position. By default, the following kinds of strings are recognized:

        - Words bounded by whitespace or line boundaries.

        - C++-style pairs of identifiers separated by double colons, such as "namespace::identifier".

        - Filesystem paths, such as "/foo/bar/baz.txt".

        - Quoted strings such as "foo bar".

        - Java or Python-style include paths, such as "foo.bar.baz".

        - URIs with the schemes: mailto, http, https, ssh, or telnet.

        - Objective-C selectors like "@selector(foo:bar:)".

        - Email addresses.

#### How do I Change Smart Selection Rules?

Under Settings>Profiles>Advanced, you may edit the smart selection rules. In addition to a regular expression, each rule also has a Precision attribute, which takes a value of Very Low, Low, Normal, High, or Very High. Intuitively, it refers to how sure one can be that when a rule's regular expression finds a match that it is what the user intended. For example, the "Word" rule is low precision (it matches almost every time), while the "HTTP URL" rule is very high precision (it almost never produces false positives). This allows the "HTTP URL" rule to take precedence when both match, unless the "Word" rule matches a much longer string. That might happen, for instance, if there were a non-URL character after a URL followed by a lot more text. The precision levels have a very strong effect, so it's very rare for a lower precision rule to take precedence over a higher precision rule.

When editing rules, it is advised that you experiment with different precision levels and different kinds of strings to find one that works well. A collection of test cases may be found at smart_selection_cases.txt.

When Smart Selection is activated, iTerm2 tries each regular expression. For a given regex, various strings on the screen are tested until the longest match is found. Only matches that include the character under the cursor are of interest. The longest such match is added to a pool of "selection candidates". Each candidate is assigned a score equal to its length in characters. Among the candidates in the highest precision class (where Very High is the highest class and Very Low is the lowest) with any matches, the higheset scoring one is used as the selection.

#### Actions

Actions may be associated with smart selection rules. When you right click in a terminal, smart selection is performed at the cursor's location. Any smart selection rule that matches that location will be searched for associated actions, and those actions will be added to the context menu. A cmd-click on text matching a smart selection rule will invoke the first rule.

The following actions are defined:

- Open File: Opens the file using the default system application.

- Open URL: Opens the URL using the default system browser.

- Run Command: Runs the command using `/bin/sh -c` in the background. Output goes to the Script Console.

- Run Coprocess: Starts a [coprocess](documentation-coprocesses.html).

- Send Text: Sends text as though it was typed by the user.

- Run Command in Window: Opens a new window and runs the command in it.

- Copy: Copies the string to the pasteboard.

Each action has a parameter. The meaning of the parameter depends on the action. For example, for the **Open URL** action the parameter should be a URL. The value you put in the `Parameter` field may contain special substrings which get substituted with values determined at runtime. By default, a legacy syntax is used with the following substitutions:

- `\0`: The full text of the match.

- `\1`: The first match group (captured using parentheses in the regular expression).

- `\2`...`\9`: Subsequent match groups.

- `\d`: The current directory.

- `\u`: The current user name. If you're sshed then you must install [Shell Integration](documentation-shell-integration.html) for this to be known.

- `\h`: The current host name. If you're sshed then you must install [Shell Integration](documentation-shell-integration.html) for this to be known.

- `\n`: Newline

- `\\`: Backslash

If you check the **Use interpolated strings for parameters** checkbox, then a more modern syntax is used. See the [interpolated string](documentation-scripting-fundamentals.html) documentation for details. For example, a parameter of `\(path)` is equivalent to the legacy syntax `\d`. In addition to the standard variables that are available in an interpolated string evaluated in a Session context, an array of strings called `matches` is defined. `matches[0]` is the full text of the match and `matches[i]` is the `i`th capture group for `i` > 0.

When using interpolated strings, the [usual escaping rules](documentation-scripting-fundamentals.html#interpolated-strings) apply.

#### Regular Expressions

Regular expressions conform to the [ICU regular expressions](https://unicode-org.github.io/icu/userguide/strings/regexp.html) rules.