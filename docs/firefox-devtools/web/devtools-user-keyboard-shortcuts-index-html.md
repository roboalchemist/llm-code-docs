# Source: https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html

Title: All keyboard shortcuts — Firefox Source Docs documentation

URL Source: https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html

Markdown Content:
This page lists all keyboard shortcuts used by the developer tools built into Firefox.

The first section lists the shortcut for opening each tool and the second section lists shortcuts that are applicable to the Toolbox itself. After that there’s one section for each tool, which lists the shortcuts that you can use within that tool.

Because access keys are locale-dependent, they’re not documented in this page.

Opening and closing tools[](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#opening-and-closing-tools "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

These shortcuts work in the main browser window to open the specified tool. The same shortcuts will work to close tools hosted in the Toolbox, if the tool is active. For tools like the Browser Console that open in a new window, you have to close the window to close the tool.

| **Command** | **Windows** | **macOS** | **Linux** |
| --- | --- | --- | --- |
| Open Toolbox (with the most recent tool activated) | Ctrl + Shift + I | Cmd + Opt + I | Ctrl + Shift + I |
| Bring Toolbox to foreground (if the Toolbox is in a separate window and not in foreground) | Ctrl + Shift + I or F12 | Cmd + Opt + I or F12 | Ctrl + Shift + I or F12 |
| Close Toolbox (if the Toolbox is in a separate window and in foreground) | Ctrl + Shift + I or F12 | Cmd + Opt + I or F12 | Ctrl + Shift + I or F12 |
| Open Web Console [[1]](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#id2) | Ctrl + Shift + K | Cmd + Opt + K | Ctrl + Shift + K |
| Toggle “Pick an element from the page” (opens the Toolbox and/or focus the Inspector tab) | Ctrl + Shift + C | Cmd + Opt + C | Ctrl + Shift + C |
| Open Style Editor | Shift + F7 | Shift + F7 | Shift + F7 |
| Open Profiler | Shift + F5 | Shift + F5 | Shift + F5 |
| Open Network Monitor | Ctrl + Shift + E | Cmd + Opt + E | Ctrl + Shift + E |
| Toggle Responsive Design Mode | Ctrl + Shift + M | Cmd + Opt + M | Ctrl + Shift + M |
| Open Browser Console | Ctrl + Shift + J | Cmd + Opt + J | Ctrl + Shift + J |
| Open Browser Toolbox | Ctrl + Alt + Shift + I | Cmd + Opt + Shift + I | Ctrl + Alt + Shift + I |
| Storage Inspector | Shift + F9 | Shift + F9 | Shift + F9 |
| Open Debugger | Ctrl + Shift + Z | Cmd + Opt + Z | Ctrl + Shift + Z |

Toolbox[](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#toolbox "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------

Keyboard shortcuts for the [Toolbox](https://firefox-source-docs.mozilla.org/devtools-user/tools_toolbox/index.html)

These shortcuts work whenever the toolbox is open, no matter which tool is active.

| **Command** | **Windows** | **macOS** | **Linux** |
| --- | --- | --- | --- |
| Cycle through tools left to right | Ctrl + ] | Cmd + ] | Ctrl + ] |
| Cycle through tools right to left | Ctrl + [ | Cmd + [ | Ctrl + [ |
| Toggle between active tool and settings. | F1 | F1 | F1 |
| Toggle toolbox between the last 2 [docking modes](https://firefox-source-docs.mozilla.org/devtools-user/tools_toolbox/index.html#tools-toolbox-docking-mode) | Ctrl + Shift + D | Cmd + Shift + D | Ctrl + Shift + D |
| Toggle split console (except if console is the currently selected tool) | Esc | Esc | Esc |

These shortcuts work in all tools that are hosted in the toolbox.

| **Command** | **Windows** | **macOS** | **Linux** |
| --- | --- | --- | --- |
| Increase font size | Ctrl + + | Cmd + + | Ctrl + + |
| Decrease font size | Ctrl + - | Cmd + - | Ctrl + - |
| Reset font size | Ctrl + 0 | Cmd + 0 | Ctrl + 0 |

Source editor[](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#source-editor "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------

This table lists the default shortcuts for the source editor.

In the [Editor Preferences](https://firefox-source-docs.mozilla.org/devtools-user/settings/index.html#settings-editor-preferences) section of the developer tools settings, you can choose to use Vim, Emacs, or Sublime Text key bindings instead.

To select these, visit `about:config`, select the setting `devtools.editor.keymap`, and assign “vim” or “emacs”, or “sublime” to that setting. If you do this, the selected bindings will be used for all the developer tools that use the source editor. You need to reopen the editor for the change to take effect.

The key binding preference is exposed in the [Editor Preferences](https://firefox-source-docs.mozilla.org/devtools-user/settings/index.html#settings-editor-preferences) section of the developer tools settings, and you can set it there instead of `about:config`.

| **Command** | **Windows** | **macOS** | **Linux** |
| --- | --- | --- | --- |
| Go to line | Ctrl + J, Ctrl + G | Cmd + J, Cmd + G | Ctrl + J, Ctrl + G |
| Find in file | Ctrl + F | Cmd + F | Ctrl + F |
| Select all | Ctrl + A | Cmd + A | Ctrl + A |
| Cut | Ctrl + X | Cmd + X | Ctrl + X |
| Copy | Ctrl + C | Cmd + C | Ctrl + C |
| Paste | Ctrl + V | Cmd + V | Ctrl + V |
| Undo | Ctrl + Z | Cmd + Z | Ctrl + Z |
| Redo | Ctrl + Shift + Z / Ctrl + Y | Cmd + Shift + Z / Cmd + Y | Ctrl + Shift + Z / Ctrl + Y |
| Indent | Tab | Tab | Tab |
| Unindent | Shift + Tab | Shift + Tab | Shift + Tab |
| Move line(s) up | Alt + Up | Alt + Up | Alt + Up |
| Move line(s) down | Alt + Down | Alt + Down | Alt + Down |
| Comment/uncomment line(s) | Ctrl + / | Cmd + / | Ctrl + / |

Page Inspector[](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#page-inspector "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

Keyboard shortcuts for the [Page inspector](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/index.html).

| **Command** | **Windows** | **macOS** | **Linux** |
| --- | --- | --- | --- |
| Inspect Element | Ctrl + Shift + C | Cmd + Shift + C | Ctrl + Shift + C |

Node picker[](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#node-picker "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------

These shortcuts work while the [node picker](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/select_an_element/index.html#page-inspector-how-to-select-an-element-with-the-node-picker) is active.

| **Command** | **Windows** | **macOS** | **Linux** |
| --- | --- | --- | --- |
| Select the element under the mouse and cancel picker mode | Click | Click | Click |
| Select the element under the mouse and stay in picker mode | Ctrl + Click | Cmd + Click | Ctrl + Click |
| Select the element under the mouse, even if it can’t consume pointer events | Shift + Click | Shift + Click | Shift + Click |

HTML pane[](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#html-pane "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

These shortcuts work while you’re in the [Inspector’s HTML pane](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/examine_and_edit_html/index.html).

| **Command** | **Windows** | **macOS** | **Linux** |
| --- | --- | --- | --- |
| Delete the selected node | Delete | Delete | Delete |
| Undo delete of a node | Ctrl + Z | Cmd + Z | Ctrl + Z |
| Redo delete of a node | Ctrl + Shift + Z / Ctrl + Y | Cmd + Shift + Z / Cmd + Y | Ctrl + Shift + Z / Ctrl + Y |
| Move to next node (expanded nodes only) | ↓ | ↓ | ↓ |
| Move to previous node | ↑ | ↑ | ↑ |
| Move to first node in the tree. | Home | Home | Home |
| Move to last node in the tree. | End | End | End |
| Expand currently selected node | → | → | → |
| Collapse currently selected node | ← | ← | ← |
| (When a node is selected) move inside the node so you can start stepping through attributes. | Enter | Return | Enter |
| Step forward through the attributes of a node | Tab | Tab | Tab |
| Step backward through the attributes of a node | Shift + Tab | Shift + Tab | Shift + Tab |
| (When an attribute is selected) start editing the attribute | Enter | Return | Enter |
| Hide/show the selected node | H | H | H |
| Focus on the search box in the HTML pane | Ctrl + F | Cmd + F | Ctrl + F |
| Edit as HTML | F2 | F2 | F2 |
| Stop editing HTML | F2 / Ctrl + Enter | F2 / Cmd + Return | F2 / Ctrl + Enter |
| Copy the selected node’s outer HTML | Ctrl + C | Cmd + C | Ctrl + C |
| Scroll the selected node into view | S | S | S |
| Find the next match in the markup, when searching is active | Enter | Return | Enter |
| Find the previous match in the markup, when searching is active | Shift + Enter | Shift + Return | Shift + Enter |

CSS pane[](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#css-pane "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------

These shortcuts work when you’re in the [Inspector’s CSS panel](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/examine_and_edit_css/index.html)

| **Command** | **Windows** | **macOS** | **Linux** |
| --- | --- | --- | --- |
| Focus on the search box in the CSS pane | Ctrl + F | Cmd + F | Ctrl + F |
| Clear search box content (only when the search box is focused, and content has been entered) | Esc | Esc | Esc |
| Step forward through properties and values | Tab | Tab | Tab |
| Step backward through properties and values | Shift + Tab | Shift + Tab | Shift + Tab |
| Start editing property or value (Rules view only, when a property or value is selected, but not already being edited) | Enter or Space | Return or Space | Enter or Space |
| Cycle up and down through auto-complete suggestions (Rules view only, when a property or value is being edited) | ↑ , ↓ | ↑ , ↓ | ↑ , ↓ |
| Choose current auto-complete suggestion (Rules view only, when a property or value is being edited) | Enter or Tab | Return or Tab | Enter or Tab |
| Increment selected value by 1 | ↑ | ↑ | ↑ |
| Decrement selected value by 1 | ↓ | ↓ | ↓ |
| Increment selected value by 100 | Shift + PageUp | Shift + PageUp | Shift + PageUp |
| Decrement selected value by 100 | Shift + PageDown | Shift + PageDown | Shift + PageDown |
| Increment selected value by 10 | Shift + ↑ | Shift + ↑ | Shift + ↑ |
| Decrement selected value by 10 | Shift + ↓ | Shift + ↓ | Shift + ↓ |
| Increment selected value by 0.1 | Ctrl + ↑ | Alt + ↑ | Ctrl + ↑ |
| Decrement selected value by 0.1 | Ctrl + ↓. | Alt + ↓ | Ctrl + ↓. |
| Show/hide more information about current property (Computed view only, when a property is selected) | Enter or Space | Return or Space | Enter or Space |
| Open MDN reference page about current property (Computed view only, when a property is selected) | F1 | F1 | F1 |
| Open current CSS file in Style Editor (Computed view only, when more information is shown for a property and a CSS file reference is focused). | Enter | Return | Enter |

Debugger[](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#debugger "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------

Keyboard shortcuts for the [Firefox JavaScript Debugger](https://firefox-source-docs.mozilla.org/devtools-user/debugger/index.html).

| **Command** | **Windows** | **macOS** | **Linux** |
| --- | --- | --- | --- |
| Close current file | Ctrl + W | Cmd + W | Ctrl + W |
| Search for a string in the current file | Ctrl + F | Cmd + F | Ctrl + F |
| Search for a string in all files | Ctrl + Shift + F | Cmd + Shift + F | Ctrl + Shift + F |
| Find next in the current file | Ctrl + G | Cmd + G | Ctrl + G |
| Search for scripts by name | Ctrl + P | Cmd + P | Ctrl + P |
| Resume execution when at a breakpoint | F8 | F8[[4]](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#id7) | F8 |
| Step over | F10 | F10[[4]](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#id7) | F10 |
| Step into | F11 | F11[[4]](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#id7) | F11 |
| Step out | Shift + F11 | Shift + F11[[4]](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#id7) | Shift + F11 |
| Toggle breakpoint on the currently selected line | Ctrl + B | Cmd + B | Ctrl + B |
| Toggle conditional breakpoint on the currently selected line | Ctrl + Shift + B | Cmd + Shift + B | Ctrl + Shift + B |

Web Console[](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#web-console "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------

Keyboard shortcuts for the [Web Console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/index.html).

| **Command** | **Windows** | **macOS** | **Linux** |
| --- | --- | --- | --- |
| Open the Web Console | Ctrl + Shift + K | Cmd + Opt + K | Ctrl + Shift + K |
| Search in the message display pane | Ctrl + F | Cmd + F | Ctrl + F |
| Open the [object inspector pane](https://firefox-source-docs.mozilla.org/devtools-user/web_console/rich_output/index.html#web-console-rich-output-examining-object-properties) | Ctrl + Click | Ctrl + Click | Ctrl + Click |
| Clear the [object inspector pane](https://firefox-source-docs.mozilla.org/devtools-user/web_console/rich_output/index.html#web-console-rich-output-examining-object-properties) | Esc | Esc | Esc |
| Focus on the command line | Ctrl + Shift + K | Cmd + Opt + K | Ctrl + Shift + K |
| Clear output | Ctrl + Shift + L | Ctrl + L Cmd + K | Ctrl + Shift + L |

Command line interpreter[](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#command-line-interpreter "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

These shortcuts apply when you’re in the [command line interpreter](https://firefox-source-docs.mozilla.org/devtools-user/web_console/the_command_line_interpreter/index.html).

| **Command** | **Windows** | **macOS** | **Linux** |
| --- | --- | --- | --- |
| Scroll to start of console output (only if the command line is empty) | Home | Home | Home |
| Scroll to end of console output (only if the command line is empty) | End | End | End |
| Page up through console output | PageUp | PageUp | PageUp |
| Page down through console output | PageDown | PageDown | PageDown |
| Go backward through [command history](https://firefox-source-docs.mozilla.org/devtools-user/web_console/the_command_line_interpreter/index.html#command-line-interpreter-execution-history) | ↑ | ↑ | ↑ |
| Go forward through command history | ↓ | ↓ | ↓ |
| Initiate reverse search through command history/step backwards through matching commands | F9 | Ctrl + R | F9 |
| Step forward through matching command history (after initiating reverse search) | Shift + F9 | Ctrl + S | Shift + F9 |
| Move to the beginning of the line | Home | Ctrl + A | Ctrl + A |
| Move to the end of the line | End | Ctrl + E | Ctrl + E |
| Execute the current expression | Enter | Return | Enter |
| Add a new line, for entering multiline expressions | Shift + Enter | Shift + Return | Shift + Enter |

Style Editor[](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#style-editor "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

Keyboard shortcuts for the [Style editor](https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html).

| **Command** | **Windows** | **macOS** | **Linux** |
| --- | --- | --- | --- |
| Open the Style Editor | Shift + F7 | Shift + F7 | Shift + F7 |
| Open autocomplete popup | Ctrl + Space | Cmd + Space | Ctrl + Space |
| Find Next | Ctrl + G | Cmd + G | Ctrl + G |
| Find Previous | Shift + Ctrl + G | Shift + Cmd + G | Shift + Ctrl + G |
| Replace | Shift + Ctrl + F | Cmd + Option + F | Shift + Ctrl + F |
| Focus the filter input | Ctrl + P | Cmd + P | Ctrl + P |
| Save file to disk | Ctrl + S | Cmd + S | Ctrl + S |

Eyedropper[](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#eyedropper "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

Keyboard shortcuts for the [Eyedropper](https://firefox-source-docs.mozilla.org/devtools-user/eyedropper/index.html).

| **Command** | **Windows** | **macOS** | **Linux** |
| --- | --- | --- | --- |
| Select the current color | Enter | Return | Enter |
| Dismiss the Eyedropper | Esc | Esc | Esc |
| Move by 1 pixel | ArrowKeys | ArrowKeys | ArrowKeys |
| Move by 10 pixels | Shift + ArrowKeys | Shift + ArrowKeys | Shift + ArrowKeys |
