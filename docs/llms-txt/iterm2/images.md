# Source: https://iterm2.com/documentation-images.html

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

# Inline Images Protocol

iTerm2 is able to display images within the terminal. Using a similar mechanism, it can also facilitate file transfers over any transport (such as ssh or telnet), even in a non-8-bit-clean environment.

Just want to try it out and don't care about the protocol? Use the imgcat tool. [Download imgcat here](https://iterm2.com/utilities/imgcat)

### Example: imgcat

Using the [imgcat](https://iterm2.com/utilities/imgcat) script, one or more images may be displayed in a terminal session. For example:

Critically, animated GIFs are supported as of version 2.9.20150512.

### Retina

Starting in iTerm2 version 3.2.0, Retina displays are properly supported. Previously, they would be double-size (one display "point" per image pixel rather than one display pixel per image pixel). If you prefer the old behavior, change **Prefs > Advanced > Show inline images at Retina resolution**.

### Protocol

iTerm2 extends the xterm protocol with a set of proprietary escape sequences. In general, the pattern is:

```
ESC ] 1337 ; key = value ^G
```

Whitespace is shown here for ease of reading: in practice, no spaces should be used. ^G is the BEL character. You can use ST in place of ^G anywhere it is mentioned in this document. ST is the standard terminator for OSC sequences, and is formed by `ESC \`.

For file transfer and inline images, there are two control sequences. The original one, which works on all remotely modern versions of iTerm2 is:

```
ESC ] 1337 ; File = [optional arguments] : base-64 encoded file contents ^G
```

The optional arguments are formatted as `key=value` with a semicolon between each key-value pair. They are described below.

A new way of sending files was introduced in iTerm2 version 3.5 which works in tmux integration mode by splitting the giant control sequence into a number of smaller ones:

First, send:

```
ESC ] 1337 ; MultipartFile = [optional arguments] ^G
```

Then, send one or more of:

```
ESC ] 1337 ; FilePart = base64 encoded file contents ^G
```

What size chunks should you use? Older versions of tmux have a limit of 256 bytes for the entire sequence. In newer versions of tmux, the limit is 1,048,576 bytes. iTerm2 also imposes a limit of 1,048,576 bytes.

Finally, send:

```
ESC ] 1337 ; FileEnd ^G
```

  KeyDescription of value

  name  base-64 encoded filename. Defaults to "Unnamed file".

size  File size in bytes. Optional; this is only used by the progress indicator.

width  Width to render. See notes below.

height  Height to render. See notes below.

preserveAspectRatio  If set to 0, then the image's inherent aspect ratio will not be respected; otherwise, it will fill the specified width and height as much as possible without stretching. Defaults to 1.

inline  If set to 1, the file will be displayed inline. Otherwise, it will be downloaded with no visual representation in the terminal session. Defaults to 0.

The width and height are given as a number followed by a unit, or the word "auto".

- *N*: *N* character cells.

- *N*px: *N* pixels.

- *N*%: *N* percent of the session's width or height.

- auto: The image's inherent size will be used to determine an appropriate dimension.

### More on File Transfers

By omitting the `inline` argument (or setting its value to 0), files will be downloaded and saved in the *Downloads* folder instead of being displayed inline. Any kind of file may be downloaded, but only images will display inline. Any image format that macOS supports will display inline, including PDF, PICT, or any number of bitmap data formats (PNG, GIF, etc.). A new menu item titled *Downloads* will be added to the menu bar after a download begins, where progress can be monitored and the file can be located, opened, or removed.

### Detection

Use the [Feature Reporting](https://iterm2.com/feature-reporting) protocol to detect the availability of inline images.

### Sample Code

Sample code for displaying images may be found here.

#### [imgls](https://iterm2.com/utilities/imgls)

Provides an augmented directory listing that includes a thumbnail of each image in a directory.

#### [imgcat](https://iterm2.com/utilities/imgcat)

Displays one or more images inline at their full size.

#### [it2dl](https://iterm2.com/utilities/it2dl)

Downloads a file, but does not display it inline.

#### [divider](https://raw.githubusercontent.com/gnachman/iTerm2/master/tests/divider)

Draws a full-width, one line-tall graphical divider.