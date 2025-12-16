# Source: https://iterm2.com/documentation-web.html

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

# Web Browser

## Overview

iTerm2 includes built-in web browsing capabilities. Web browser sessions fit into iTerm2's existing window > tab > split pane hierarchy just like terminal sessions, allowing you to browse the web alongside your terminal work.

## Getting Started

### Enabling the Browser

- Install the [browser plugin](https://iterm2.com/browser-plugin.html) to enable full functionality

- Create a new profile

- Go to **Settings > Profiles > General**

- Set **Profile Type** to **Web Browser**

**Note for Enterprise Users:** Administrators can block the browser plugin by restricting bundle ID `com.googlecode.iterm2.iTermBrowserPlugin`.

### Disabling Browser Features

If you prefer not to use browser features, you can completely hide them by setting **Settings > Advanced > Enable browser-style profiles** to **No**.

## Core Features

### Navigation and Window Management

- Browser profiles work within iTerm2's standard window/tab/split pane hierarchy.

- Use hotkey windows, Open Quickly, navigation shortcuts, and per-session hotkeys as with terminal sessions.

- **Exception:** â-[ and â-] perform Back/Forward navigation instead of pane switching in browser sessions.

- **Cmd+click** opens links in new tabs.

- **Cmd+Shift+click** opens links in new vertical split panes.

- **Cmd+Shift+Option+click** opens links in new horizontal split panes.

### Text and Selection

- **Copy on selection** works identically to terminal windows.

- **Smart Selection** works identically to terminal windows. Smart Selection Actions appear in the context menu.

- **Copy Mode** uses the same keystrokes as terminal sessions.

- **Jump to Selection** functions as in terminal sessions.

- **Find** supports regular expressions and case-sensitive search, just like in a terminal.

### AI Integration

- Link browser sessions to AI chat to discuss web pages.

- Click hamburger menu â **Ask AI** to create a new AI chat with the reader-mode content of the current page attached.

- Summarize, analyze, or ask questions about the current page.

### Privacy and Security

- **/dev/null mode** is a mode for browsing privately that prevents any data from being saved to disk.

- Built-in popup blocking blocks popups not initiated by user action.

- Simple ad blocking using WebKit content blocker rules (configure via hamburger menu â **Settings**).

- CONNECT proxy support for proxy-based adblockers.

- The existing password manager has been integrated. Browser passwords are stored separately from terminal passwords.

- Password manager integration for 1Password, and LastPass will use your existing web passwords.

### Remote Access

- View files on remote hosts via SSH Integration using URLs like: `iterm2-ssh://example.com/home/user/file.jpg`

## Advanced Features

### Bookmarks and Organization

- **Named Marks** act as bookmarks for specific page sections (right-click â Add Named Mark).

- Standard bookmarks available via hamburger menu.

- Named Marks and Bookmarks work with Open Quickly and the Named Marks Toolbelt tool.

### Recording and History

- **Instant Replay** captures browser sessions using macOS Screen Capture API.

- Like instant replay in terminal windows, the RAM limit is respected.

- **Global Search** can search across browser sessions.

### Automation and Customization

- **Key Bindings** work in browser profiles (some terminal-specific actions are unavailable).

- **Triggers** match when pages finish loading with web-specific actions.

- **Pointer bindings** and **Actions** available, minus some terminal-specific options.

- **Snippets** insert text into a focused form field.

- **Broadcast Input** works across browser sessions.

- **Advanced Paste** available, minus some terminal-specific features.

- **Composer** functions in browser sessions.

### Content Management

- **Reader Mode** is avilable in the hamburger menu.

- **Distraction removal mode** similar to Safari's is also in the hamburger menu.

- Right-click â **Remove Element** to hide cookie panels or other unwanted elements.

- **Shell > Save Contents** saves web pages with resources.

- Basic auto-fill of form fields is available, using your contact card information.

- Search suggestions in URL bar.

- Automatic audio detection and muting.

## Technical Details

The browser is built on WKWebView and identifies as Safari to ensure compatibility with most websites.

## Limitations

- **Python API** No browser-specific APIs yet. [File a feature request](https://iterm2.com/bugs) if you have ideas.

- **Passkeys** Not supported due to Apple-imposed WKWebView restrictions.

- **Advanced ad blocking:** Limited by Apple's resource fetching API restrictions.

## About This Feature

This feature exists because:
- Many iTerm2 features translate well to web browsing
- It provides a unified terminal and browser experience
- A former colleague suggested this idea in 2014 and I haven't been able to stop thinking about it.
- I am maybe having a midlife crisis and this is cheaper than a sports car.

While not intended as a primary browser, iTerm2's web capabilities provide a useful tool for integrated terminal and web workflows.