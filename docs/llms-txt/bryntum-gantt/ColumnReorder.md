# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/ColumnReorder.md

# [ColumnReorder](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnReorder)

Allows user to reorder columns by dragging headers. To get notified about column reorder listen to `change` event on [columns](https://bryntum.com/docs/gantt/api/#Grid/data/ColumnStore) store.

This feature is **enabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[stretchedDragProxy](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnReorder#config-stretchedDragProxy)
Set to `true` to stretch the column drag proxy element to cover the full height of the grid.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isColumnReorder](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnReorder#property-isColumnReorder)
Identifies an object as an instance of [ColumnReorder](https://bryntum.com/docs/gantt/api/#Grid/feature/ColumnReorder) class, or subclass thereof.

[isColumnReorder](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnReorder#property-isColumnReorder-static)
Identifies an object as an instance of [ColumnReorder](https://bryntum.com/docs/gantt/api/#Grid/feature/ColumnReorder) class, or subclass thereof.

[stretchedDragProxy](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnReorder#property-stretchedDragProxy)
Set to `true` to stretch the column drag proxy element to cover the full height of the grid.

[isReordering](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnReorder#property-isReordering)
Returns true if a reorder operation is active

## Functions

Functions are methods available for calling on the class

[init](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnReorder#function-init)
Initialize drag & drop (called from render)

[onDrop](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnReorder#function-onDrop)
Handle drop

[onInvalidDrop](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnReorder#function-onInvalidDrop)
Handle invalid drop

[renderContents](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnReorder#function-renderContents)
Updates DragHelper with updated headers when grid contents is rerendered

[onInternalPaint](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnReorder#function-onInternalPaint)
Initializes this feature on grid paint.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeColumnDragStart](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnReorder#event-beforeColumnDragStart)
This event is fired prior to starting a column drag gesture. The drag is canceled if a listener returns `false`.

[columnDragStart](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnReorder#event-columnDragStart)
This event is fired when a column drag gesture has started.

[columnDrag](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnReorder#event-columnDrag)
This event is fired when a column is being dragged, and you can set the `valid` flag on the `context` object to indicate whether the drop position is valid or not.

[beforeColumnDropFinalize](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnReorder#event-beforeColumnDropFinalize)
This event is fired when a column is dropped, and you can return false from a listener to abort the operation.

[columnDrop](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnReorder#event-columnDrop)
This event is always fired after a column is dropped. The `valid` param is `true` if the operation was not vetoed and the column was moved in the column store.
