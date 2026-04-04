# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/ColumnRename.md

# [ColumnRename](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnRename)

Allows user to rename columns by either right-clicking column header or using keyboard shortcuts when column header is focused.

To get notified about column renaming listen to `change` event on [columns](https://bryntum.com/docs/gantt/api/#Grid/data/ColumnStore) store.

Right click column header and click "Rename" or press F2 when column header is focused:

\* This feature is **disabled** by default.

Keyboard shortcuts
------------------

This feature has the following default keyboard shortcuts:

Keys

Action

Action description

`F2`

_startEdit_

Starts editing focused column header text

Please note that `Ctrl` is the equivalent to `Command` and `Alt` is the equivalent to `Option` for Mac users

For more information on how to customize keyboard shortcuts, please see [our guide](https://bryntum.com/docs/gantt/api/#Grid/guides/customization/keymap.md)

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[keyMap](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnRename#config-keyMap)
See [Keyboard shortcuts](https://bryntum.com/docs/gantt/api/#Grid/feature/ColumnRename#keyboard-shortcuts) for details

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isColumnRename](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnRename#property-isColumnRename)
Identifies an object as an instance of [ColumnRename](https://bryntum.com/docs/gantt/api/#Grid/feature/ColumnRename) class, or subclass thereof.

[isColumnRename](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnRename#property-isColumnRename-static)
Identifies an object as an instance of [ColumnRename](https://bryntum.com/docs/gantt/api/#Grid/feature/ColumnRename) class, or subclass thereof.
