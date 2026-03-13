# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/RowNumberColumn.md

# [RowNumberColumn](https://bryntum.com/docs/gantt/api/Grid/column/RowNumberColumn)

A column that displays the row number in each cell.

There is no `editor`, since the value is read-only.

```
const grid = new Grid({
  appendTo : targetElement,
  width    : 300,
  columns  : [
    { type : 'rownumber' }
  ]
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRowNumberColumn](https://bryntum.com/docs/gantt/api/Grid/column/RowNumberColumn#property-isRowNumberColumn)
Identifies an object as an instance of [RowNumberColumn](https://bryntum.com/docs/gantt/api/#Grid/column/RowNumberColumn) class, or subclass thereof.

[isRowNumberColumn](https://bryntum.com/docs/gantt/api/Grid/column/RowNumberColumn#property-isRowNumberColumn-static)
Identifies an object as an instance of [RowNumberColumn](https://bryntum.com/docs/gantt/api/#Grid/column/RowNumberColumn) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[defaultRenderer](https://bryntum.com/docs/gantt/api/Grid/column/RowNumberColumn#function-defaultRenderer)
Renderer that displays the row number in the cell.

[resizeToFitContent](https://bryntum.com/docs/gantt/api/Grid/column/RowNumberColumn#function-resizeToFitContent)
Resizes the column to match the widest string in it.
