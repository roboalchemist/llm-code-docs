# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/RowResize.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/RowResize.md

# [RowResize](https://bryntum.com/docs/gantt/api/Grid/feature/RowResize)

Enables user to change row height by dragging the bottom row border. After a resize operation, the [rowHeight](https://bryntum.com/docs/gantt/api/#Grid/data/GridRowModel#field-rowHeight) field of the record is updated (when [applyToAllRows](https://bryntum.com/docs/gantt/api/#Grid/feature/RowResize#config-applyToAllRows) is `false`).

Try hovering the bottom row border in the grid below and use drag-drop to change the row height.

This feature is **disabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[applyToAllRows](https://bryntum.com/docs/gantt/api/Grid/feature/RowResize#config-applyToAllRows)
Set this to true to modify the global [rowHeight](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-rowHeight) which affects all grid rows.

[cellSelector](https://bryntum.com/docs/gantt/api/Grid/feature/RowResize#config-cellSelector)
Set this to a CSS selector to only trigger row resizing in cells for a specific column.

[minHeight](https://bryntum.com/docs/gantt/api/Grid/feature/RowResize#config-minHeight)
Minimum height when resizing

[maxHeight](https://bryntum.com/docs/gantt/api/Grid/feature/RowResize#config-maxHeight)
Max height when resizing

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRowResize](https://bryntum.com/docs/gantt/api/Grid/feature/RowResize#property-isRowResize)
Identifies an object as an instance of [RowResize](https://bryntum.com/docs/gantt/api/#Grid/feature/RowResize) class, or subclass thereof.

[isRowResize](https://bryntum.com/docs/gantt/api/Grid/feature/RowResize#property-isRowResize-static)
Identifies an object as an instance of [RowResize](https://bryntum.com/docs/gantt/api/#Grid/feature/RowResize) class, or subclass thereof.

[applyToAllRows](https://bryntum.com/docs/gantt/api/Grid/feature/RowResize#property-applyToAllRows)
Set this to true to modify the global [rowHeight](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-rowHeight) which affects all grid rows.

[minHeight](https://bryntum.com/docs/gantt/api/Grid/feature/RowResize#property-minHeight)
Minimum height when resizing

[maxHeight](https://bryntum.com/docs/gantt/api/Grid/feature/RowResize#property-maxHeight)
Max height when resizing

## Functions

Functions are methods available for calling on the class

[onCancel](https://bryntum.com/docs/gantt/api/Grid/feature/RowResize#function-onCancel)
Restore row size on cancel (ESC)
