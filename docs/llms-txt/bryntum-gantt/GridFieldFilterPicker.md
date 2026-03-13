# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/widget/GridFieldFilterPicker.md

# [GridFieldFilterPicker](https://bryntum.com/docs/gantt/api/Grid/widget/GridFieldFilterPicker)

Subclass of [FieldFilterPicker](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker) allowing configuration using an existing [Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid).

See also [GridFieldFilterPickerGroup](https://bryntum.com/docs/gantt/api/#Grid/widget/GridFieldFilterPickerGroup).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[grid](https://bryntum.com/docs/gantt/api/Grid/widget/GridFieldFilterPicker#config-grid)
[Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid) from which to read the available field list. In order to appear as a selectable property for a filter, a column must have a `field` property. If the column has a `text` property, that will be shown as the displayed text in the selector; otherwise, the `field` property will be shown as-is.

The grid's [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store)'s [modelClass](https://bryntum.com/docs/gantt/api/#Core/data/Store#property-modelClass) will be examined to find field data types.

You can limit available fields to a subset of the grid's columns using the [allowedFieldNames](https://bryntum.com/docs/gantt/api/#Grid/widget/GridFieldFilterPicker#config-allowedFieldNames) configuration property.

[allowedFieldNames](https://bryntum.com/docs/gantt/api/Grid/widget/GridFieldFilterPicker#config-allowedFieldNames)
Optional array of field names that are allowed as selectable properties for filters. This is a subset of the field names found in the [grid](https://bryntum.com/docs/gantt/api/#Grid/widget/GridFieldFilterPicker#config-grid)'s columns. When supplied, only the named fields will be shown in the property selector combo.

Note that field names are case-sensitive and should match the data field name in the store model.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGridFieldFilterPicker](https://bryntum.com/docs/gantt/api/Grid/widget/GridFieldFilterPicker#property-isGridFieldFilterPicker)
Identifies an object as an instance of [GridFieldFilterPicker](https://bryntum.com/docs/gantt/api/#Grid/widget/GridFieldFilterPicker) class, or subclass thereof.

[isGridFieldFilterPicker](https://bryntum.com/docs/gantt/api/Grid/widget/GridFieldFilterPicker#property-isGridFieldFilterPicker-static)
Identifies an object as an instance of [GridFieldFilterPicker](https://bryntum.com/docs/gantt/api/#Grid/widget/GridFieldFilterPicker) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[getColumnFields](https://bryntum.com/docs/gantt/api/Grid/widget/GridFieldFilterPicker#function-getColumnFields-static)
Gets the filterable fields backing any of the configured `grid`'s columns, for those columns for which it is possible to do so.
