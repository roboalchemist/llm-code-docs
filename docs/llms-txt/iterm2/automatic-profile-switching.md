# Source: https://iterm2.com/documentation-automatic-profile-switching.html

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

# Automatic Profile Switching

iTerm2 can use information it knows about your current path, host name, user name, and foreground job name to change profiles. For example, your window's background color or the terminal's character encoding could change when connecting to different hosts.

### Shell Integration Required

You must install [Shell Integration](documentation-shell-integration.html) on all machines and all user accounts where you plan to use Automatic Profile Switching (either by using the scripts or the Triggers workaround described in the Shell Integration docs).

#### Rule Syntax

In *Settings>Profiles>Advanced*, you may specify a set of rules.

When any session satisfies a rule in a given profile, it will switch to that profile. Rules consist of three optional components: the user name, the hostname, and the path. At least one component must be present, since an empty rule is not allowed. The hostname is required only when both a user name and a path are specified.

A user name is a unix accont name (e.g., *root*) followed by an `@`.

A path always begins with a `/`. Any time a hostname is followed by a path, they are separated by a `:`. For example, `iterm2.com:/users/george`. It may include `*` wildcards.

A hostname can be a DNS name, like `iterm2.com` or an IP address like `127.0.0.1`. A hostname may contain one or more `*` characters, which act as a wildcard (like globbing in Unix).

The job name is the name of the executable. For example, "vim" or "bash". It must be prefixed with an ampersand `&`. For example, `&emacs*`. Starting with version 3.6, the rule is matched against the full command line rather than only the job name.

Additionally, a rule may be designated as sticky by beginning with a `!`. This will be described below, in the *Automatic Reversion* section.

Some examples:

- `[[email&#160;protected]](https://iterm2.com/cdn-cgi/l/email-protection):/users/george`

- `george@*:/users/george`

- `*:/users/george`

- `*.iterm2.com:/users/george`

- `dev.*.com:/users/george`

- `[[email&#160;protected]](https://iterm2.com/cdn-cgi/l/email-protection)`

- `iterm2.com`

- `george@`

- `iterm2.com:/users/george`

- `/users/george`

- `/users/*`

- `&vim`

- `iterm2.com&vim`

- `!iterm2.com`

Because more than one rule may match at any given time, rules with higher
quality matches prevail over those with lower-quality matches. Quality is
determined by a rule's score, which is computed by summing the scores for its
matching parts. In order for a rule to be considered, all of its parts that are
specified must match the current state.

The scoring is defined as:

- An exact match for the hostname scores 16 points.

- A partial match for the hostname using a wildcard scores 8 points.

- A match on the job name (wildcard or not) scores 4 points.

- A match on the user name scores 2 points.

- An exact match on the path scores one point.

- A partial match on the path using a wildcard scores zero points, but does count as a match for the rule.

The highest scoring rule, if any, will be used and the session's profile will be switched.

The UI tries to prevent you from entering the same rule in two different profiles, but if that does happen then one profile is chosen arbitrarily.

### Automatic Reversion

After APS switches a session's profile, its rules may eventually cease to match
(for example, the hostname changes back to "localhost" because an ssh session
ends). If no profile has a matching rule, the session's original profile will
be restored. The exception is if the last-matched rule was "sticky". A sticky
rule is prefixed with an `!`.

#### Implementation

Each session maintains a stack of profiles. Initially, the stack contains the profile the session was created with. When the username, hostname, or path changes, iTerm2 finds the best-matching profile. If some profile has a matching rule, one of two things happens:

- If that profile is already on the stack, profiles above that one will be removed from the stack and the session will switch to that profile.

- Failing that, the profile will be pushed on the stack and the session will switch to that profile.

If no profile has a matching rule, the stack is emptied (except for the first entry, the original profile for the session) and the session reverts to its original profile.

Rules may begin with ! to indicate "stickiness". A sticky rule causes its profile to stay even after the rule no longer applies, so long as no other rule matches.

### Triggers

Since it's impractical to install shell integration everywhere (for example, as *root*), there will be times when you need to write a trigger to detect the current username or hostname. Please see the *Triggers* section of [Shell Integration](https://iterm2.com/shell_integration.html) for details.

### Troubleshooting

There are a few ways things can go wrong. Please see the [Why doesn't secure copy/automatic profile switching work?](https://gitlab.com/gnachman/iterm2/wikis/scp-not-connecting) document for help diagnosing and fixing these issues.