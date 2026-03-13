# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/RowCopyPaste.md

# [RowCopyPaste](https://bryntum.com/docs/gantt/api/Grid/feature/RowCopyPaste)

Allow using \[Ctrl/CMD + C/X\] and \[Ctrl/CMD + V\] to copy/cut-and-paste rows. Also makes cut, copy and paste actions available via the cell context menu.

You can configure how a newly pasted record is named using [generateNewName](https://bryntum.com/docs/gantt/api/#Grid/feature/RowCopyPaste#config-generateNewName)

This feature is **enabled** by default

```
const grid = new Grid({
    features : {
        rowCopyPaste : true
    }
});
```

This feature will work alongside with CellCopyPaste but there is differences on functionality.

* Context menu actions, and keyboard shortcuts, will be processed by either feature depending on what is selected and where the context menu was triggered. Set [rowOptionsOnCellContextMenu](https://bryntum.com/docs/gantt/api/#Grid/feature/RowCopyPaste#config-rowOptionsOnCellContextMenu) to `true` to show two sets of options when context menu is triggered on a selected cell.
* They share clipboard, so even when the internal clipboard is used, it is not possible to have rows and cells copied or cut at the same time.

Keyboard shortcuts
------------------

The feature has the following default keyboard shortcuts:

Keys

Action

Weight ¹

Action description

`Ctrl`+`C`

_copy_

10

Calls [copyRows](https://bryntum.com/docs/gantt/api/#Grid/feature/RowCopyPaste#function-copyRows) which copies selected row(s) into the clipboard.

`Ctrl`+`X`

_cut_

10

Calls [copyRows](https://bryntum.com/docs/gantt/api/#Grid/feature/RowCopyPaste#function-copyRows) which cuts out selected row(s) and saves in clipboard.

`Ctrl`+`V`

_paste_

10

Calls [pasteRows](https://bryntum.com/docs/gantt/api/#Grid/feature/RowCopyPaste#function-pasteRows) which inserts copied or cut row(s) from the clipboard.

**¹** Customization of keyboard shortcuts that has a `weight` can affect other features that also uses that particular keyboard shortcut. Read more in [our guide](https://bryntum.com/docs/gantt/api/#Grid/guides/customization/keymap.md).

Please note that `Ctrl` is the equivalent to `Command` and `Alt` is the equivalent to `Option` for Mac users

For more information on how to customize keyboard shortcuts, please see [our guide](https://bryntum.com/docs/gantt/api/#Grid/guides/customization/keymap.md).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[nameField](https://bryntum.com/docs/gantt/api/Grid/feature/RowCopyPaste#config-nameField)
The field to use as the name field when updating the name of copied records

[rowOptionsOnCellContextMenu](https://bryntum.com/docs/gantt/api/Grid/feature/RowCopyPaste#config-rowOptionsOnCellContextMenu)
Adds `Cut (row)`, `Copy (row)` and `Paste (row)` options when opening a context menu on a selected cell when [cellSelection](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridSelection#config-selectionMode) and [CellCopyPaste](https://bryntum.com/docs/gantt/api/#Grid/feature/CellCopyPaste) is active. Default behaviour will only provide row copy/paste actions on a selected row.

[cutOnly](https://bryntum.com/docs/gantt/api/Grid/feature/RowCopyPaste#config-cutOnly)
If `true`, this translates copy actions to cut actions and removes the context menu `Copy` option.

[columnTypesToIgnore](https://bryntum.com/docs/gantt/api/Grid/feature/RowCopyPaste#config-columnTypesToIgnore)
Specifies which column types should be omitted from copying.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRowCopyPaste](https://bryntum.com/docs/gantt/api/Grid/feature/RowCopyPaste#property-isRowCopyPaste)
Identifies an object as an instance of [RowCopyPaste](https://bryntum.com/docs/gantt/api/#Grid/feature/RowCopyPaste) class, or subclass thereof.

[isRowCopyPaste](https://bryntum.com/docs/gantt/api/Grid/feature/RowCopyPaste#property-isRowCopyPaste-static)
Identifies an object as an instance of [RowCopyPaste](https://bryntum.com/docs/gantt/api/#Grid/feature/RowCopyPaste) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[copyRows](https://bryntum.com/docs/gantt/api/Grid/feature/RowCopyPaste#function-copyRows)
Copy or cut selected rows to clipboard to paste later

[monitorCellCopyPaste](https://bryntum.com/docs/gantt/api/Grid/feature/RowCopyPaste#function-monitorCellCopyPaste)
Listens to CellCopyPaste beforePaste events If user is trying to paste a string representation of a record from RowCopyPaste It will return false and paste the record instead

[stringConverter](https://bryntum.com/docs/gantt/api/Grid/feature/RowCopyPaste#function-stringConverter)
Called from Clipboardable after writing a non-string value to the clipboard

[pasteRows](https://bryntum.com/docs/gantt/api/Grid/feature/RowCopyPaste#function-pasteRows)
Paste rows below selected or passed record

[stringParser](https://bryntum.com/docs/gantt/api/Grid/feature/RowCopyPaste#function-stringParser)
Called from Clipboardable after reading from clipboard, and it is determined that the clipboard data is "external"

[extractParents](https://bryntum.com/docs/gantt/api/Grid/feature/RowCopyPaste#function-extractParents)
Iterates over passed pre-sorted list of records and reassembles hierarchy of records.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[copy](https://bryntum.com/docs/gantt/api/Grid/feature/RowCopyPaste#event-copy)
Fires on the owning Grid after a copy action is performed.

[beforeCopy](https://bryntum.com/docs/gantt/api/Grid/feature/RowCopyPaste#event-beforeCopy)
Fires on the owning Grid before a copy action is performed, return `false` to prevent the action

[paste](https://bryntum.com/docs/gantt/api/Grid/feature/RowCopyPaste#event-paste)
Fires on the owning Grid after a paste action is performed.

[beforePaste](https://bryntum.com/docs/gantt/api/Grid/feature/RowCopyPaste#event-beforePaste)
Fires on the owning Grid before a paste action is performed, return `false` to prevent the action
