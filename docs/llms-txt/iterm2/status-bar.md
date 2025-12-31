# Source: https://iterm2.com/documentation-status-bar.html

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

# Status Bar

iTerm2 offers a configurable, scriptable status bar. The purpose of the status bar is to show up-to-date information about the environment you're working in and to offer useful interactions where appropriate.

### Setup

Go to **Settings > Profiles > Session**. Turn on **Status bar enabled**. Then click **Configure Status Bar** to begin setting up your status bar configuration.

### Components

A status bar is composed of components. iTerm2 ships with a number of components:

#### System Resource Monitors

- **Battery Level** - Shows a graph of battery level over time as well as a charging indicator.

- **CPU Utilization** - Shows a graph of CPU utilization over time.

- **Memory Utilization** - Shows a graph of RAM utilization over time.

- **Network Throughput** - Shows a graph of upload and download throughput over time.

#### Shell Information

- **Current Directory** - Shows the current working directory. Use Shell Integration to keep this accurate when sshing.

- **Host Name** - Shows the current hostname. Use Shell Integration to keep this accurate when sshing.

- **User Name** - Shows the current username. Use Shell Integration to keep this accurate when sshing.

- **Job Name** - Shows the name of the current foreground job and its parent processes.

- **git state** - Shows the current git branch, whether it's dirty, and the number of commits ahead or behind of `origin`.

#### Miscellaneous

- **Clock** - Shows the current time and date.

- **Custom Action** - A button that performs a configurable action.

#### UI Affordances

- **Composer** - A field for editing commands before sending them to the shell.

- **Search Tool** - A search field for performing searches over terminal history.

- **Filter** - A field for filtering terminal contents.

- **Action** - A button that activates a programmable action, much like a key-binding action.

- **Snippet** - A button that pastes text from Snippets, as configured in *Prefs>Shortcuts>Snippets*.

- **Triggers** - A button that activates a menu allowing you to enable or disable triggers.

#### Spacers

- **Empty Space** - An empty component. NOTE: This is only available when using the "stable positioning" layout algorithm.

- **Fixed-size Spacer** - Adds a fixed amount of space between components

- **Spring** - Adds a variable amount of space between components. NOTE: This is only available when using the "tight packing" layout algorithm.

#### Python API Hooks

- **Interpolated String** - Shows the value of an [interpolated string](documentation-scripting-fundamentals.html).

- **Call Script Function** - Shows the result of a [Python API function call](documentation-scripting-fundamentals.html).

You can also write your own components in Python. See the examples section of the Python API docs for a [working demo](https://iterm2.com/python-api/examples/statusbar.html). Custom components show up at the end of the list (you may need to scroll down to see them).

### Adding and Removing

To add a component to the status bar, drag it from the top section to the *Active Components* section.

To remove a status bar component, select and press backspace. You can also drag it out of the *Active Components* section.

### Configure Component

Many components can be configured. To modify a component's settings, select it in the *Active Components* section. Then click **Configure Component**.

Some settings are common to all or most components:

- **Background Color** - If set, this overrides the default background color.

- **Text Color** - If set, this overrides the default text color.

- **Priority** - When there isn't enough space to show all the components, they will be removed from lowest to highest priority. All components default to priority 5.

- **Compression Resistance** - When using the "tight packing" layout algorithm, the compression resistance acts like a spring constant. A higher value means the allocated space will shrink more slowly than for components with lower compression resistance.

- **Size Multiple** - When using the "stable positioning" layout algorithm, the size multiple sets how wide this component is relative to the standard width. It can be a floating-point value.

- **Minimum Width** - Gives the minimum width of the component in points.

- **Maximum Width** - Gives the maximum width of the component in points.

#### Clock Component

The clock component has a **Date Format** setting. It defaults to `M-DD h:mm`. See [Unicode TR 35-1](http://www.unicode.org/reports/tr35/tr35-31/tr35-dates.html#Date_Format_Patterns) for the syntax.

#### git status Component

The git status component lets you configure the polling interval in seconds. It periodically runs git commands in the current directory to check its status, and this determines the time between updates. The git command is run in a sandbox that does not allow writing to the filesystem outside of `/tmp` and `/var` to avoid side-effects.

#### Interpolated String

The interpolated string component has a `String Value` parameter where you can enter the interpolated string you wish to display. It is evaluated in the context of the current session.

#### Function Call

The function call component has a `Label` that is displayed in the status bar and a `Function call` parameter that gives the Python API function call to invoke when the component is clicked.

### Interactions

Some components allow user interaction.

#### git status

Click the `git status` component to get the following options:

- **Commit** - Runs `git commit`. A window will open for you to enter the commit message if needed.

- **Add & Commit** - Runs `git commit -a`. A window will open for you to enter the commit message if needed.

- **Stash** - Runs `git stash`

- **Log** - Runs `git log` and shows the result in a popover.

- **Pull origin master** - Runs `git pull origin master` and opens a window if necessary.

- **Push origin master** - Runs `git push origin master` and opens a window if necessary.

- **Check out recent branches** - Runs `git checkout <branch>`. The most recently used branches are listed.

#### Job Name

Click the component to open a popover showing the job tree in this session. This feature is only available on macOS 10.14 and later.

#### Working Directory

Click the component to view the recent working directories on this host. Select one to issue a `cd` command to enter it.

### Advanced Settings

The **Advanced** button lets you configure settings that affect the status bar as a whole. You can set the separator color, background color, and default text color. When unset, these take reasonable values. You can also change the font. Not all fonts will look good because of size and alignment issues.

You can also adjust the layout algorithm.

#### Tight Packing Algorithm

The tight packing algorithm treats each component as a spring which is more or less compressible and has a minimum (and sometimes maximum) size. It begins by trying to show all components. If their minimum sizes cannot all be satisfied then they are removed from lowest to highest priority. In the case of a tie the leftmost component with the lowest priority is removed. Once the set of visible components has been thus determined, their widths are set in proportion to their spring constants.

This algorithm gets the highest density of status bar components at the cost of their jumping around whenever a value changes.

#### Stable Positioning Algorithm

The stable positioning algorithm first determines which components will be visible by adding them from highest to lowest priority. Every component is allocated the base width times its size multiple (which defaults to 1). The base width is no less than the largest minimum width of all the visible components. Spacers adjacent to components that are not visible will also be removed to make the best use of space.

This is the default algorithm.

### Auto-Rainbow

Pressing this buton assigns text colors to the active components in a pleasing variety of rainbow colors. No unicorns were harmed in the making of this feature.