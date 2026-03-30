# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/util/GridLocation.md

# [GridLocation](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation)

This class encapsulates a reference to a specific navigable grid location.

This encapsulates a grid cell based upon the record and column, but in addition, it could represent an actionable location _within a cell_\* if the [target](https://bryntum.com/docs/gantt/api/#Grid/util/GridLocation#property-target) is not the grid cell in question.

A `GridLocation` is immutable. That is, once instantiated, the record and column, which it references cannot be changed. The [move](https://bryntum.com/docs/gantt/api/#Grid/util/GridLocation#function-move) method returns a new instance.

A `GridLocation` that encapsulates a cell within the body of a grid will have the following read-only properties:

* grid : `Grid` The Grid that owns the `GridLocation`.
* record : `Model` The record of the row that owns the GridLocation. (`null` if the header).
* rowIndex : `Number` The zero-based index of the row that owns the GridLocation. (-1 means the header).
* column : `Column` The Column that owns the GridLocation.
* columnIndex : `Number` The zero-based index of the column that owns the GridLocation.
* cell : `HTMLElement` The referenced cell element.
* target : `HTMLElement` The focusable element. This may be the cell, or a child of the cell.

If the location is a column _header_, the `record` will be `null`, and the `rowIndex` will be `-1`.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[grid](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#config-grid)
The grid which this `GridLocation` references.

[record](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#config-record)
The record which this `GridLocation` references. (unless [rowIndex](https://bryntum.com/docs/gantt/api/#Grid/util/GridLocation#config-rowIndex) is used to configure)

[rowIndex](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#config-rowIndex)
The row index which this `GridLocation` references. (unless [record](https://bryntum.com/docs/gantt/api/#Grid/util/GridLocation#config-record) is used to configure).

`-1` means the header row, in which case the [record](https://bryntum.com/docs/gantt/api/#Grid/util/GridLocation#config-record) will be `null`.

[column](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#config-column)
The Column which this `GridLocation` references. (unless [columnIndex](https://bryntum.com/docs/gantt/api/#Grid/util/GridLocation#config-columnIndex) or [columnId](https://bryntum.com/docs/gantt/api/#Grid/util/GridLocation#config-columnId) is used to configure)

[columnId](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#config-columnId)
The column id which this `GridLocation` references. (unless [column](https://bryntum.com/docs/gantt/api/#Grid/util/GridLocation#config-column) or [columnIndex](https://bryntum.com/docs/gantt/api/#Grid/util/GridLocation#config-columnIndex) is used to configure)

[columnIndex](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#config-columnIndex)
The column index which this `GridLocation` references. (unless [column](https://bryntum.com/docs/gantt/api/#Grid/util/GridLocation#config-column) or [columnId](https://bryntum.com/docs/gantt/api/#Grid/util/GridLocation#config-columnId) is used to configure)

[field](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#config-field)
The field of the column index which this `GridLocation` references. (unless another column identifier is used to configure)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[grid](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#property-grid)
The grid which this `GridLocation` references.

[rowIndex](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#property-rowIndex)
Yields the row index of this location.

[visibleRowIndex](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#property-visibleRowIndex)
Used by GridNavigation.

[isSelectable](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#property-isSelectable)
Yields `true` if the cell and row are selectable.

That is if the record is present in the grid's store and it's not a group summary or group header record.

[record](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#property-record)
Yields the [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) of this location, or `null` if the location is a column header.

[column](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#property-column)
Yields the [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column) of this location.

[columnIndex](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#property-columnIndex)
Yields the column index of this location.

[cell](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#property-cell)
The cell DOM element which this `GridLocation` references.

[target](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#property-target)
The DOM element which encapsulates the focusable target of this `GridLocation`.

This is usually the [cell](https://bryntum.com/docs/gantt/api/#Grid/util/GridLocation#property-cell), but if this is an actionable location, this may be another DOM element within the cell.

[containsFocus](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#property-containsFocus)
This property is `true` if the focus is inside the cell, not _on_ the cell.

[isActionable](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#property-isActionable)
This property is `true` if the focus target is not the cell itself.

[isColumnHeader](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#property-isColumnHeader)
This property is `true` if this location represents a column header.

[isCell](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#property-isCell)
This property is `true` if this location represents a cell in the grid body.

## Functions

Functions are methods available for calling on the class

[constructor](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#function-constructor)
Initializes a new GridLocation.

[move](https://bryntum.com/docs/gantt/api/Grid/util/GridLocation#function-move)
Returns a **\*new \*** `GridLocation` instance having moved from the current location in the mode specified.
