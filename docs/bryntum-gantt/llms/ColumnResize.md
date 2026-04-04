# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/ColumnResize.md

# [ColumnResize](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnResize)

Enables user to resize columns by dragging a handle on the right hand side of the header. To get notified about column resize listen to `change` event on [columns](https://bryntum.com/docs/gantt/api/#Grid/data/ColumnStore) store.

This feature is **enabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[liveResize](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnResize#config-liveResize)
Resize all cells below a resizing header during dragging. `'auto'` means `true` on non-mobile platforms.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isColumnResize](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnResize#property-isColumnResize)
Identifies an object as an instance of [ColumnResize](https://bryntum.com/docs/gantt/api/#Grid/feature/ColumnResize) class, or subclass thereof.

[isColumnResize](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnResize#property-isColumnResize-static)
Identifies an object as an instance of [ColumnResize](https://bryntum.com/docs/gantt/api/#Grid/feature/ColumnResize) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[onResizing](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnResize#function-onResizing)
Handle drag event - resize the column live unless it's a touch gesture

[onResize](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnResize#function-onResize)
Handle drop event (only used for touch)

[onCancel](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnResize#function-onCancel)
Restore column width on cancel (ESC)

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeColumnResize](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnResize#event-beforeColumnResize)
This event is fired prior to starting a column resize gesture. The resize is canceled if a listener returns `false`.

[columnResizeStart](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnResize#event-columnResizeStart)
This event is fired when a column resize gesture starts.

[columnResize](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnResize#event-columnResize)
This event is fired after a resize gesture is completed.
