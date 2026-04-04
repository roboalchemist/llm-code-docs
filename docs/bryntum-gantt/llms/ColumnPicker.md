# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/ColumnPicker.md

# [ColumnPicker](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnPicker)

Displays a column picker (to show/hide columns) in the header context menu. Columns can be displayed in sub menus by region or tag. Grouped headers are displayed as menu hierarchies.

This feature is **enabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[groupByRegion](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnPicker#config-groupByRegion)
Groups columns in the picker by region (each region gets its own sub menu)

[groupByTag](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnPicker#config-groupByTag)
Groups columns in the picker by tag, each column may be shown under multiple tags. See [tags](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-tags)

[createColumnsFromModel](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnPicker#config-createColumnsFromModel)
Configure this as `true` to have the fields from the Grid's [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store)'s [modelClass](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-modelClass) added to the menu to create **new** columns to display the fields.

This may be combined with the [stateful](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridState) ability of the grid to create a self-configuring grid.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isColumnPicker](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnPicker#property-isColumnPicker)
Identifies an object as an instance of [ColumnPicker](https://bryntum.com/docs/gantt/api/#Grid/feature/ColumnPicker) class, or subclass thereof.

[isColumnPicker](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnPicker#property-isColumnPicker-static)
Identifies an object as an instance of [ColumnPicker](https://bryntum.com/docs/gantt/api/#Grid/feature/ColumnPicker) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[getColumnPickerItems](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnPicker#function-getColumnPickerItems)
Get menu items, either a straight list of columns or sub menus per subgrid

[getColumnsForTag](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnPicker#function-getColumnsForTag)
Get all columns that has the specified tag.

[refreshTagMenu](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnPicker#function-refreshTagMenu)
Refreshes checked status for a tag menu. Needed since columns can appear under multiple tags.

[buildColumnMenu](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnPicker#function-buildColumnMenu)
Traverses columns to build menu items for the column picker.

[populateHeaderMenu](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnPicker#function-populateHeaderMenu)
Populates the header context menu items.

[onColumnToggle](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnPicker#function-onColumnToggle)
Handler for column hide/show menu checkitems.

[getColumnDragToolbarItems](https://bryntum.com/docs/gantt/api/Grid/feature/ColumnPicker#function-getColumnDragToolbarItems)
Supply items to ColumnDragToolbar
