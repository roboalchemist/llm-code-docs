# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/widget/GridFieldFilterPickerGroup.md

# [GridFieldFilterPickerGroup](https://bryntum.com/docs/gantt/api/Grid/widget/GridFieldFilterPickerGroup)

Extends [FieldFilterPickerGroup](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPickerGroup) to allow providing a [Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid) from which available fields will be read. This is useful when a grid is already configured with a set of columns containing display names and type information.

The grid should have a [ColumnStore](https://bryntum.com/docs/gantt/api/#Grid/data/ColumnStore) configured (see [columns](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-columns)) and a [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store) whose [modelClass](https://bryntum.com/docs/gantt/api/#Core/data/Store#property-modelClass) contains fields with specific data types.

Optionally, you can also use [allowedFieldNames](https://bryntum.com/docs/gantt/api/#Grid/widget/GridFieldFilterPickerGroup#config-allowedFieldNames) to restrict the set of fields shown in the widget.

For example:

```
new GridFieldFilterPickerGroup({
    appendTo : domElement,

    grid : myGrid,

    filters : [{
        property : 'startDate',
        operator : '<=',
        value    : new Date()
    }]
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[grid](https://bryntum.com/docs/gantt/api/Grid/widget/GridFieldFilterPickerGroup#config-grid)
[Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid) from which to read the available field list. In order to appear as a selectable property for a filter, a column must have a `field` property. If the column has a `text` property, that will be shown as the displayed text in the selector; otherwise, the `field` property will be shown as-is.

The grid's [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store)'s [modelClass](https://bryntum.com/docs/gantt/api/#Core/data/Store#property-modelClass) will be examined to find field data types.

You can limit available fields to a subset of the grid's columns using the [allowedFieldNames](https://bryntum.com/docs/gantt/api/#Grid/widget/GridFieldFilterPickerGroup#config-allowedFieldNames) configuration property.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGridFieldFilterPickerGroup](https://bryntum.com/docs/gantt/api/Grid/widget/GridFieldFilterPickerGroup#property-isGridFieldFilterPickerGroup)
Identifies an object as an instance of [GridFieldFilterPickerGroup](https://bryntum.com/docs/gantt/api/#Grid/widget/GridFieldFilterPickerGroup) class, or subclass thereof.

[isGridFieldFilterPickerGroup](https://bryntum.com/docs/gantt/api/Grid/widget/GridFieldFilterPickerGroup#property-isGridFieldFilterPickerGroup-static)
Identifies an object as an instance of [GridFieldFilterPickerGroup](https://bryntum.com/docs/gantt/api/#Grid/widget/GridFieldFilterPickerGroup) class, or subclass thereof.
