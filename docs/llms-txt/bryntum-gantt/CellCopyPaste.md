# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/CellCopyPaste.md

# [CellCopyPaste](https://bryntum.com/docs/gantt/api/Grid/feature/CellCopyPaste)

Allows using `[Ctrl/CMD + C]`, `[Ctrl/CMD + X]` and `[Ctrl/CMD + V]` to cut, copy and paste cell or cell ranges. Also makes cut, copy and paste actions available via the cell context menu.

Requires [selectionMode.cell](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-selectionMode) to be activated. Also, if the [CellEdit](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit) feature is disabled, the [copyOnly](https://bryntum.com/docs/gantt/api/#Grid/feature/CellCopyPaste#config-copyOnly) config will default to \`true\` which prevents cut-and-paste actions completely. Set [copyOnly](https://bryntum.com/docs/gantt/api/#Grid/feature/CellCopyPaste#config-copyOnly) to \`false\` to prevent this behaviour.

This feature will work alongside with [RowCopyPaste](https://bryntum.com/docs/gantt/api/#Grid/feature/RowCopyPaste) but there is differences on functionality.

* Context menu actions, and keyboard shortcuts, will be processed by either feature depending on what is selected and where the context menu was triggered. Set [rowOptionsOnCellContextMenu](https://bryntum.com/docs/gantt/api/#Grid/feature/RowCopyPaste#config-rowOptionsOnCellContextMenu) to `true` to show two sets of options when context menu is triggered on a selected cell.
* They share clipboard, so even when the internal clipboard is used, it is not possible to have rows and cells copied or cut at the same time.

If the [Clipboard API](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API) is available, that will be used. This enables copying and pasting between different Bryntum products or completely different applications. Please note that only string values are supported.

This feature is **disabled** by default

```
const grid = new Grid({
    features : {
        cellCopyPaste : true
    }
});
```

Keyboard shortcuts
------------------

The feature has the following default keyboard shortcuts:

Keys

Action

Action description

`Ctrl`+`C`

_copy_

Calls [copy](https://bryntum.com/docs/gantt/api/#Grid/feature/CellCopyPaste#function-copy) which copies selected cell values into the clipboard.

`Ctrl`+`X`

_cut_

Calls [cut](https://bryntum.com/docs/gantt/api/#Grid/feature/CellCopyPaste#function-cut) which cuts out selected cell values and saves in clipboard.

`Ctrl`+`V`

_paste_

Calls [paste](https://bryntum.com/docs/gantt/api/#Grid/feature/CellCopyPaste#function-paste) which inserts string values from the clipboard.

Please note that `Ctrl` is the equivalent to `Command` and `Alt` is the equivalent to `Option` for Mac users

For more information on how to customize keyboard shortcuts, please see [this guide](https://bryntum.com/docs/gantt/api/#Grid/guides/customization/keymap.md).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[useNativeClipboard](https://bryntum.com/docs/gantt/api/Grid/feature/CellCopyPaste#config-useNativeClipboard)
Set this to `false` to not use native Clipboard API even if it is available

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCellCopyPaste](https://bryntum.com/docs/gantt/api/Grid/feature/CellCopyPaste#property-isCellCopyPaste)
Identifies an object as an instance of [CellCopyPaste](https://bryntum.com/docs/gantt/api/#Grid/feature/CellCopyPaste) class, or subclass thereof.

[isCellCopyPaste](https://bryntum.com/docs/gantt/api/Grid/feature/CellCopyPaste#property-isCellCopyPaste-static)
Identifies an object as an instance of [CellCopyPaste](https://bryntum.com/docs/gantt/api/#Grid/feature/CellCopyPaste) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[cut](https://bryntum.com/docs/gantt/api/Grid/feature/CellCopyPaste#function-cut)
Cuts selected cells to clipboard (native if accessible) to paste later

[copy](https://bryntum.com/docs/gantt/api/Grid/feature/CellCopyPaste#function-copy)
Copies selected cells to clipboard (native if accessible) to paste later

[paste](https://bryntum.com/docs/gantt/api/Grid/feature/CellCopyPaste#function-paste)
Pastes string data into a cell or a range of cells. Either from native clipboard if that is accessible or from a fallback clipboard that is only available to the owner Grid.

The string data will be split on `\n` and `\t` and put in different rows and columns accordingly.

Note that there must be a selected cell to paste the data into.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[copy](https://bryntum.com/docs/gantt/api/Grid/feature/CellCopyPaste#event-copy)
Fires on the owning Grid after a copy action is performed.

[beforeCopy](https://bryntum.com/docs/gantt/api/Grid/feature/CellCopyPaste#event-beforeCopy)
Fires on the owning Grid before a copy action is performed, return `false` to prevent the action

[paste](https://bryntum.com/docs/gantt/api/Grid/feature/CellCopyPaste#event-paste)
Fires on the owning Grid after a paste action is performed.

[beforePaste](https://bryntum.com/docs/gantt/api/Grid/feature/CellCopyPaste#event-beforePaste)
Fires on the owning Grid before a paste action is performed, return `false` to prevent the action
