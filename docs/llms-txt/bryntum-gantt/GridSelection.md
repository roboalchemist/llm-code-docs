# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/view/mixin/GridSelection.md

# [GridSelection](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection)

A mixin for Grid that handles row and cell selection. See [selectionMode](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridSelection#config-selectionMode) for details on how to control what should be selected (rows, cells, columns) and how the selection should work.

```
// select a row
grid.selectedRow = 7;

// select a cell
grid.selectedCell = { id: 5, columnId: 'column1' }

// select a record
grid.selectedRecord = grid.store.last;

// select multiple records by ids
grid.selectedRecords = [1, 2, 4, 6]
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[selectionMode](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#config-selectionMode)
Selection configuration settings, change these properties to control how selection works and what can be selected.

When _configuring_ (creating an instance), set this to an object containing only those properties you want to _change_.

```
new Grid({
    selectionMode : {
       // Enables cell selection
       cell       : true,
       // Enabled cell and record selection by dragging
       dragSelect : true,
       // Enables selection of a column's cells by clicking the column header
       column     : true,
       // Shows a row number column which, when clicked, selected the row/record
       rowNumber  : true
    }
});
```

After the configuring is done, these properties will be monitored for changes, making it possible to alter the selection configuration at any time.

```
// Adds a selection checkbox column and makes that the only way to select
grid.selectionMode.checkboxOnly = true;

// Deactivates the auto selection of rows and cells when keyboard navigating
grid.selectionMode.selectOnKeyboardNavigation = false;
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGridSelection](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#property-isGridSelection)
Identifies an object as an instance of [GridSelection](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridSelection) class, or subclass thereof.

[isGridSelection](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#property-isGridSelection-static)
Identifies an object as an instance of [GridSelection](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridSelection) class, or subclass thereof.

[selectionMode](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#property-selectionMode)
Selection configuration settings, change these properties to control how selection works and what can be selected.

When _configuring_ (creating an instance), set this to an object containing only those properties you want to _change_.

```
new Grid({
    selectionMode : {
       // Enables cell selection
       cell       : true,
       // Enabled cell and record selection by dragging
       dragSelect : true,
       // Enables selection of a column's cells by clicking the column header
       column     : true,
       // Shows a row number column which, when clicked, selected the row/record
       rowNumber  : true
    }
});
```

After the configuring is done, these properties will be monitored for changes, making it possible to alter the selection configuration at any time.

```
// Adds a selection checkbox column and makes that the only way to select
grid.selectionMode.checkboxOnly = true;

// Deactivates the auto selection of rows and cells when keyboard navigating
grid.selectionMode.selectOnKeyboardNavigation = false;
```

[selectedRecord](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#property-selectedRecord)
The last selected record. Set to select a row or use Grid#selectRow. Set to null to deselect all

[selectedRecords](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#property-selectedRecords)
Selected records.

If [deselectFilteredOutRecords](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridSelection#config-selectionMode) is `false` (default) this will include selected records which has been filtered out.

If [preserveSelectionOnPageChange](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridSelection#config-selectionMode) is `true` (defaults to `false`) this will include selected records on all pages.

If [selectRecordOnCell](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridSelection#config-selectionMode) is `true` (default) this will include any record which has at least one cell selected.

Can be set as array of ids:

```
grid.selectedRecords = [1, 2, 4, 6]
```

[selectedRows](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#property-selectedRows)
Selected records. Records selected via cell selection is excluded.

If [deselectFilteredOutRecords](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridSelection#config-selectionMode) is `false` (default) this will include selected records which has been filtered out.

If [preserveSelectionOnPageChange](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridSelection#config-selectionMode) is `true` (defaults to `false`) this will include selected records on all pages.

if [selectRecordOnCell](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridSelection#config-selectionMode) is `false` this will return same records as [selectedRecords](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridSelection#property-selectedRecords).

Can be set as array of ids:

```
grid.selectedRecords = [1, 2, 4, 6]
```

[selectedCell](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#property-selectedCell)
In cell selection mode, this will get the cell selector for the (last) selected cell. Set to an available cell selector to select only that cell. Or use [selectCell()](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridSelection#function-selectCell) instead.

[selectedCells](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#property-selectedCells)
In cell selection mode, this will get the cell selectors for all selected cells. Set to an array of available cell selectors. Or use [selectCells()](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridSelection#function-selectCells) instead.

[selectedCellCSSSelector](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#property-selectedCellCSSSelector)
CSS selector for the currently selected cell. Format is "\[data-index=index\] \[data-column-id=column\]".

## Functions

Functions are methods available for calling on the class

[onStoreRecordIdChange](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-onStoreRecordIdChange)
Triggered from Grid view when the id of a record has changed. Update the collection indices.

[onStoreRemove](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-onStoreRemove)
Triggered from Grid view when records get removed from the store. Deselects all records which have been removed.

[onStoreDataChange](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-onStoreDataChange)
Triggered from Grid view when the store changes. This might happen if store events are batched and then resumed. Deselects all records which have been removed.

[onStoreRemoveAll](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-onStoreRemoveAll)
Triggered from Grid view when all records get removed from the store. Deselects all records.

[isSelected](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-isSelected)
Checks whether a row is selected. Will not check if any of a row's cells are selected.

[isCellSelected](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-isCellSelected)
Checks whether a cell is selected.

[isSelectable](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-isSelectable)
Checks whether a cell or row can be selected.

[spliceSelectedRecords](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-spliceSelectedRecords)
Removes and adds records to/from the selection at the same time. Analogous to the `Array` `splice` method.

Note that if records that are specified for removal are also in the `toAdd` array, then those records are _not_ removed and then appended. They remain in the same position relative to all remaining records.

[selectRow](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-selectRow)
Select one row

[selectRows](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-selectRows)
Select one or more rows

[selectAll](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-selectAll)
This selects all rows. If store is filtered, this will merge the selection of all visible rows with any selection made prior to filtering.

[deselectAll](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-deselectAll)
Deselects all selected rows and cells. If store is filtered, this will unselect all visible rows only. Any selections made prior to filtering remains.

[deselectRow](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-deselectRow)
Deselect one row

[deselectRows](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-deselectRows)
Deselect one or more rows

[selectRange](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-selectRange)
Selects rows corresponding to a range of records (from fromId to toId)

[selectCell](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-selectCell)
If in cell selection mode, this selects one cell. If not, this selects the cell's record.

[selectCells](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-selectCells)
If in cell selection mode, this selects a number of cells. If not, this selects corresponding records.

[deselectCell](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-deselectCell)
If in cell selection mode, this deselects one cell. If not, this deselects the cell's record.

[deselectCells](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-deselectCells)
If in cell selection mode, this deselects a number of cells. If not, this deselects corresponding records.

[selectCellRange](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-selectCellRange)
Selects a range of cells, from a cell selector (`GridLocation`) to another

[prepareSelection](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-prepareSelection)
Used internally to prepare a number of cells or records for selection/deselection depending on if cell selectionMode is activated. This function will not select/deselect anything by itself (that's done in performSelection).

[internalSelectRange](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-internalSelectRange)
Used internally to select a range of cells or records depending on selectionMode. Used in both shift-selection and for drag selection. Will remember current selection range and replace it with new one when it changes. But a range which is completed (drag select mouse up or a new shift range starting point has been set) will remain. This function will not update UI (that's done in refreshGridSelectionUI).

[getRange](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#function-getRange)
Used internally to get a range of cell selectors from a start selector to an end selector.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[selectionModeChange](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#event-selectionModeChange)
The selectionMode configuration has been changed.

[selectionChange](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#event-selectionChange)
The selection has been changed.

[beforeSelectionChange](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#event-beforeSelectionChange)
Fires before the selection changes. Returning `false` from a listener prevents the change

[dragSelecting](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#event-dragSelecting)
Fires while drag selecting. UI will update with current range, but the cells will not be selected until mouse up. This event can be listened for to perform actions while drag selecting.

## Typedefs

Typedefs are type definitions for the class

[GridSelectionMode](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridSelection#typedef-GridSelectionMode)
