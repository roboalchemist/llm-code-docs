# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/CheckColumn.md

# [CheckColumn](https://bryntum.com/docs/gantt/api/Grid/column/CheckColumn)

A column that displays a checkbox in the cell. The value of the backing field is toggled by the checkbox.

Toggling of the checkboxes is disabled if a record is readOnly or if the CellEdit feature is not enabled.

This column renders a [Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox) into each cell, and it is not intended to be changed. If you want to hide certain checkboxes, you can use the [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/CheckColumn#config-renderer) method to access the checkbox widget as it is being rendered.

It is **mandatory** to configure this column with a [field](https://bryntum.com/docs/gantt/api/#Grid/column/CheckColumn#config-field) (except when this column is used as a selection column, then no field should be provided). This is because the checked/unchecked state needs to be backed up in a record since rows are recycled and the state will be lost when a row is reused.

```
new Grid({
    appendTo : document.body,

    columns : [
        {
             type: 'check',
             field: 'allow',
             // In the column renderer, we get access to the record and CheckBox widget
             renderer({ record, widgets }) {
                 // Hide checkboxes in certain rows
                 widgets[0].hidden = record.readOnly;
             }
        }
    ]
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[checkAriaLabel](https://bryntum.com/docs/gantt/api/Grid/column/CheckColumn#config-checkAriaLabel)
The `aria-label` used for the default checkbox widget in this column’s cells.

[checkCls](https://bryntum.com/docs/gantt/api/Grid/column/CheckColumn#config-checkCls)
CSS class name to add to checkbox

[showCheckAll](https://bryntum.com/docs/gantt/api/Grid/column/CheckColumn#config-showCheckAll)
`true` to show a checkbox in the column header to be able to select/deselect all rows

[useSlideToggle](https://bryntum.com/docs/gantt/api/Grid/column/CheckColumn#config-useSlideToggle)
`true` to display a SlideToggle instead of a Checkbox

[minWidth](https://bryntum.com/docs/gantt/api/Grid/column/CheckColumn#config-minWidth)
The minimum column width. If value is a `Number`, then the width is in pixels

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCheckColumn](https://bryntum.com/docs/gantt/api/Grid/column/CheckColumn#property-isCheckColumn)
Identifies an object as an instance of [CheckColumn](https://bryntum.com/docs/gantt/api/#Grid/column/CheckColumn) class, or subclass thereof.

[isCheckColumn](https://bryntum.com/docs/gantt/api/Grid/column/CheckColumn#property-isCheckColumn-static)
Identifies an object as an instance of [CheckColumn](https://bryntum.com/docs/gantt/api/#Grid/column/CheckColumn) class, or subclass thereof.

[checkAriaLabel](https://bryntum.com/docs/gantt/api/Grid/column/CheckColumn#property-checkAriaLabel)
The `aria-label` used for the default checkbox widget in this column’s cells.

[checkCls](https://bryntum.com/docs/gantt/api/Grid/column/CheckColumn#property-checkCls)
CSS class name to add to checkbox

[showCheckAll](https://bryntum.com/docs/gantt/api/Grid/column/CheckColumn#property-showCheckAll)
`true` to show a checkbox in the column header to be able to select/deselect all rows

[minWidth](https://bryntum.com/docs/gantt/api/Grid/column/CheckColumn#property-minWidth)
The minimum column width. If value is a `Number`, then the width is in pixels

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[toggleAll](https://bryntum.com/docs/gantt/api/Grid/column/CheckColumn#event-toggleAll)
Fired when the header checkbox is clicked to toggle its checked status.

[beforeToggle](https://bryntum.com/docs/gantt/api/Grid/column/CheckColumn#event-beforeToggle)
Fired when a cell is clicked to toggle its checked status. Returning `false` will prevent status change.

[toggle](https://bryntum.com/docs/gantt/api/Grid/column/CheckColumn#event-toggle)
Fired when a cell is clicked to toggle its checked status.
