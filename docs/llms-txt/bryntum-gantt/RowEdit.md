# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/RowEdit.md

# [RowEdit](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit)

This feature allows editing of entire rows in a grid in a docked panel which by default slides out from the right.

By default, the editor is docked to the browser viewport, but it can be configured to be [local](https://bryntum.com/docs/gantt/api/#Grid/feature/RowEdit#config-local) to the grid.

The input fields are generated from the columns in the grid in the same way as the [CellEdit](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit), and the editor is a [Panel](https://bryntum.com/docs/gantt/api/#Core/widget/Panel).

By default, the editor works in batch mode. Fields are changed, and when the "Save" button is clicked (or the Enter key pressed), the record is updated with all the changes.

The editor can be configured to update the record as soon as a field is changed by setting the [instantUpdate](https://bryntum.com/docs/gantt/api/#Grid/feature/RowEdit#config-instantUpdate) config to `true`.

Note that the [revertOnEscape](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-revertOnEscape) property of columns is respected, so pressing Escape will revert the field to the value of the field _on focus_.

Pressing Escape on a field which has _not_ been changed will cancel the edit and close the editor.

To start editing a row, double-click a cell in the row, or press Enter or F2 when a cell is focused.

The start gesture can be configured by setting the [triggerEvent](https://bryntum.com/docs/gantt/api/#Grid/feature/RowEdit#config-triggerEvent) config to `'cellClick'` or `'cellDblClick'`.

Editing can be prevented by setting the [ignoreCSSSelector](https://bryntum.com/docs/gantt/api/#Grid/feature/RowEdit#config-ignoreCSSSelector) config to a CSS selector which matches elements that should not trigger editing.

Pressing Enter or clicking the "Save" button will save the changes and close the editor. Pressing Escape or clicking the "Cancel" button will close the editor without saving changes.

If [instantUpdate](https://bryntum.com/docs/gantt/api/#Grid/feature/RowEdit#config-instantUpdate) is `true`, the record will be updated as soon as a field is changed (on blur or when changed by trigger action such as spin up or down in a number or date or time field), so Escape and the "Cancel" button revert the changes before closing the editor.

Clicking outside the editor will normally cancel the ongoing edit and start a new one on the clicked cell. This can be prevented by setting the [continueEditingOnCellClick](https://bryntum.com/docs/gantt/api/#Grid/feature/RowEdit#config-continueEditingOnCellClick) config to `false`.

This feature is **disabled** by default

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[editor](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#config-editor)
The [Panel](https://bryntum.com/docs/gantt/api/#Core/widget/Panel) instance used as the editor.

[focusContextualField](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#config-focusContextualField)
By default, the editor field corresponding to the cell clicked will be focused when starting editing.

Set to `false` to prevent this. Focus will then go to the first field in the editor.

if [autoEdit](https://bryntum.com/docs/gantt/api/#Grid/feature/RowEdit#config-autoEdit) is `true`, starting editing by typing will always focus the contextual field in the editor.

[instantUpdate](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#config-instantUpdate)
Set to `true` to update the record as soon as a field is changed.

[editorSize](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#config-editorSize)
The width of the editor. (Or height if [side](https://bryntum.com/docs/gantt/api/#Grid/feature/RowEdit#config-side) is `'top'` or `'bottom'`).

May be specified as a number of pixels or a CSS length string.

[local](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#config-local)
Configure this as `true` to dock the editor to the grid's element instead of the browser viewport.

[revertButton](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#config-revertButton)
Configure this as `true` to show a "Revert" button in the editor which reverts any unsynced changes to the record.

This reverts all changes made since the data was loaded or synchronized with the server. This is different to just canceling an ongoing edit. This reverts the record to its loaded state.

The button is only shown when starting an edit on a record which has unsynced changes.

[side](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#config-side)
The side of the grid where the editor will be shown.

`'start'` means the `inline-start` side. `'end'` means the `inline-end` side.

[titleField](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#config-titleField)
The name of the field from the record to use when generating the title for the editor.

The default implementation returns "Editing " plus the value of the named field from the editing record.

[titleRenderer](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#config-titleRenderer)
A function (or the name of a function) which will be called passing the editing record to generate the title for the editor.

You should never modify any records inside this method.

The default implementation returns "Editing " (localized according to the current locale) plus the value of the field specified in [titleField](https://bryntum.com/docs/gantt/api/#Grid/feature/RowEdit#config-titleField).

This may be configured if a more sophisticated title is required.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRowEdit](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#property-isRowEdit)
Identifies an object as an instance of [RowEdit](https://bryntum.com/docs/gantt/api/#Grid/feature/RowEdit) class, or subclass thereof.

[isRowEdit](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#property-isRowEdit-static)
Identifies an object as an instance of [RowEdit](https://bryntum.com/docs/gantt/api/#Grid/feature/RowEdit) class, or subclass thereof.

[editor](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#property-editor)
The [Panel](https://bryntum.com/docs/gantt/api/#Core/widget/Panel) instance used as the editor.

## Functions

Functions are methods available for calling on the class

[startEditing](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#function-startEditing)
Start editing specified row. If no cellContext is given it edits the first visible row. This function is exposed on Grid and can thus be called as `grid.startEditing(...)`.

[finishEditing](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#function-finishEditing)
Finish editing, update the underlying record and hide the editor. This function is exposed on Grid and can thus be called as `grid.finishEditing(...)`

[cancelEditing](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#function-cancelEditing)
Cancel editing, hides the editor. This function is exposed on Grid and can thus be called as `grid.cancelEditing(...)`

[onElementClick](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#function-onElementClick)
Finish editing if clicking below rows (only applies when grid is higher than rows). Also finish if event target is the subgrid which can happen if the pointer is moved during mouse down.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeStartRowEdit](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#event-beforeStartRowEdit)
Fires on the owning Grid before editing starts, return `false` to prevent editing

[startRowEdit](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#event-startRowEdit)
Fires on the owning Grid when editing starts

[beforeFinishRowEdit](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#event-beforeFinishRowEdit)
Fires on the owning Grid before the row editing is finished, return false to signal that the value is invalid and editing should not be finalized.

Note that if [instantUpdate](https://bryntum.com/docs/gantt/api/#Grid/feature/RowEdit#config-instantUpdate) is `true`, the record will be updated as soon as a field is changed, so this event would not prevent the record from being updated, only the editor being hidden.

[finishRowEdit](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#event-finishRowEdit)
Fires on the owning Grid before the row editing is finished, return false to signal that the value is invalid and editing should not be finalized.

Note that if [instantUpdate](https://bryntum.com/docs/gantt/api/#Grid/feature/RowEdit#config-instantUpdate) is `true`, the record will be updated as soon as a field is changed, so this event would not prevent the record from being updated, only the editor being hidden.

[beforeCancelRowEdit](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#event-beforeCancelRowEdit)
Fires on the owning Grid before the row editing is canceled, return false to signal that the value is invalid and editing should not be finalized.

Note that if [instantUpdate](https://bryntum.com/docs/gantt/api/#Grid/feature/RowEdit#config-instantUpdate) is `true`, the record _will_ be reset to initial values on cancel of editing.

## Typedefs

Typedefs are type definitions for the class

[RowEditorContext](https://bryntum.com/docs/gantt/api/Grid/feature/RowEdit#typedef-RowEditorContext)
Row editing context
