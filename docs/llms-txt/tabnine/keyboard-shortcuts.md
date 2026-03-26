# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/features/keyboard-shortcuts.md

# Keyboard Shortcuts

Reference for all keyboard shortcuts in Tabnine CLI.

### Basic Controls

| Action                  | Keys                                     |
| ----------------------- | ---------------------------------------- |
| Confirm selection       | `Enter`                                  |
| Dismiss dialog          | `Esc` , `Ctrl+[`                         |
| Submit prompt           | `Enter`                                  |
| New line without submit | `Ctrl+Enter`, `Cmd+Enter`, `Shift+Enter` |

### Cursor Movement

| Action        | Keys                    |
| ------------- | ----------------------- |
| Start of line | `Ctrl+A`, `Home`        |
| End of line   | `Ctrl+E`, `End`         |
| Move left     | `Ctrl+B`, `Left Arrow`  |
| Move right    | `Ctrl+F`, `Right Arrow` |
| Word left     | `Ctrl+Left`, `Meta+B`   |
| Word right    | `Ctrl+Right`, `Meta+F`  |

### Editing

| Action                  | Keys                              |
| ----------------------- | --------------------------------- |
| Delete to end of line   | `Ctrl+K`                          |
| Delete to start of line | `Ctrl+U`                          |
| Clear input             | `Ctrl+C`                          |
| Delete previous word    | `Ctrl+Backspace`, `Cmd+Backspace` |
| Delete next word        | `Ctrl+Delete`, `Meta+Delete`      |
| Delete character left   | `Ctrl+H`, `Backspace`             |
| Delete character right  | `Ctrl+D`, `Delete`                |
| Undo                    | `Ctrl+Z`                          |
| Redo                    | `Ctrl+Shift+Z`                    |

### Screen Control

| Action                    | Keys                |
| ------------------------- | ------------------- |
| Clear screen              | `Ctrl+L`            |
| Toggle Markdown rendering | `Cmd+M`, `Option+M` |
| Toggle error details      | `F12`               |
| Expand response           | `Ctrl+S`            |

### Scrolling

| Action           | Keys         |
| ---------------- | ------------ |
| Scroll up        | `Shift+Up`   |
| Scroll down      | `Shift+Down` |
| Scroll to top    | `Home`       |
| Scroll to bottom | `End`        |
| Page up          | `Page Up`    |
| Page down        | `Page Down`  |

### History & Search

| Action               | Keys                                        |
| -------------------- | ------------------------------------------- |
| Previous history     | `Ctrl+P`, `Up Arrow` (at top of input)      |
| Next history         | `Ctrl+N`, `Down Arrow` (at bottom of input) |
| Reverse search       | `Ctrl+R`                                    |
| Accept search result | `Enter`, `Tab`                              |

### Navigation

| Action             | Keys              |
| ------------------ | ----------------- |
| Move up in lists   | `Up Arrow`, `K`   |
| Move down in lists | `Down Arrow`, `J` |

### Auto-Completion

| Action              | Keys                   |
| ------------------- | ---------------------- |
| Accept suggestion   | `Tab`, `Enter`         |
| Previous option     | `Up Arrow`, `Ctrl+P`   |
| Next option         | `Down Arrow`, `Ctrl+N` |
| Expand suggestion   | `Right Arrow`          |
| Collapse suggestion | `Left Arrow`           |

### External Tools

| Action               | Keys                   |
| -------------------- | ---------------------- |
| Open external editor | `Ctrl+X`, `Meta+Enter` |
| Paste from clipboard | `Ctrl+V`               |

### App Controls

| Action                   | Keys        |
| ------------------------ | ----------- |
| Toggle TODO list         | `Ctrl+T`    |
| Toggle IDE context       | `Ctrl+G`    |
| Toggle copy mode         | `Ctrl+S`    |
| Toggle shell/input focus | `Ctrl+F`    |
| Toggle YOLO mode         | `Ctrl+Y`    |
| Toggle Auto Edit         | `Shift+Tab` |

### Session Control

| Action                 | Keys        |
| ---------------------- | ----------- |
| Cancel request / quit  | `Ctrl+C`    |
| Exit (empty buffer)    | `Ctrl+D`    |
| Clear input (2x quick) | `Esc` `Esc` |

### Shell Mode

| Action            | Keys                  |
| ----------------- | --------------------- |
| Toggle shell mode | `!` (on empty prompt) |

### Vim Mode

When vim mode is enabled (via `/vim`):

#### NORMAL Mode

* Navigate: `h`, `j`, `k`, `l`
* Word jumps: `w`, `b`, `e`
* Line start/end: `0`, `$`, `^`
* Go to line: `gg`, `G`, `10G`
* Edit: `x`, `dd`, `cc`, `dw`, `cw`
* Insert: `i`, `a`, `o`, `O`
* Repeat: `.`

#### INSERT Mode

* Return to NORMAL: `Esc`

{% hint style="info" %}
Quick Tips:

* Multi-line input: Use `\` at end of line + `Enter` for newline in single-line mode
* Number shortcuts: In dialogs, type numbers `1-9` to jump to options
* TABNINE\_CLI variable: Shell commands run with `TABNINE_CLI=1` environment variable
  {% endhint %}
