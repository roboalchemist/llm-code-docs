# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/Group.md

# [Group](https://bryntum.com/docs/gantt/api/Grid/feature/Group)

Enables rendering and handling of row groups. The actual grouping is done in the store, but triggered by shift + clicking headers, or by using the context menu, or by using two finger tap (one on header, one anywhere on grid). Use shift + alt + click, or the context menu, to remove a column grouper.

Groups can be expanded/collapsed by clicking on the group row or pressing \[space\] when group row is selected. The actual grouping is done by the store, see [group](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreGroup#function-group).

Grouping by a field performs sorting by the field automatically. It's not possible to prevent sorting. If you group, the records have to be sorted so that records in a group stick together. You can either control sorting direction, or provide a custom sorting function called [groupSortFn](https://bryntum.com/docs/gantt/api/#Grid/feature/Group#config-groupSortFn) to your feature config object.

For info on programmatically handling grouping, see [StoreGroup](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreGroup).

Example snippets:

```
// grouping feature is enabled, no default value though
let grid = new Grid({
    features : {
        group : true
    }
});

// use initial grouping
let grid = new Grid({
    features : {
        group : 'city'
    }
});

// default grouper and custom renderer, which will be applied to each cell except the "group" cell
let grid = new Grid({
    features : {
      group : {
          field : 'city',
          ascending : false,
          renderer : ({ isFirstColumn, count, groupRowFor, record }) => isFirstColumn ? `${groupRowFor} (${count})` : ''
      }
    }
});

// group using custom sort function
let grid = new Grid({
    features : {
        group       : {
            field       : 'city',
            groupSortFn : (a, b) => a.city.length < b.city.length ? -1 : 1
        }
    }
});

// can also be specified on the store
let grid = new Grid({
    store : {
        groupers : [
            { field : 'city', ascending : false }
        ]
    }
});

// custom sorting function can also be specified on the store
let grid = new Grid({
    store : {
        groupers : [{
            field : 'city',
            fn : (recordA, recordB) => {
                // apply custom logic, for example:
                return recordA.city.length < recordB.city.length ? -1 : 1;
            }
        }]
    }
});
```

Currently, grouping is not supported when using pagination, the underlying store cannot group data that is split into pages.

You can control the group header heights using the [headerHeight](https://bryntum.com/docs/gantt/api/#Grid/feature/Group#property-headerHeight). Custom height for specific group header rows cannot be set with CSS, should instead be defined in a renderer function using the `size` param. See the [renderer](https://bryntum.com/docs/gantt/api/#Grid/feature/Group#config-renderer) config for details.

This feature will not work properly when Store uses [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad)

Toggling a group collapsed state programmatically
-------------------------------------------------

You can easily toggle a group´s collapsed state, by passing a group member record like so:

```
// collapse the group for a certain record
grid.features.group.toggleCollapse(record, true);
```

Grouping by multi-value fields
------------------------------

The group field's value may be an array. This means that one record can be a member of more than one group. When this is the case, the second and subsequent generated groups contain a [linked record](https://bryntum.com/docs/gantt/api/#Core/data/Model#function-link) which is a copy of the original record. Please note that some of the linked records fields are not shared, like `id` (which is always generated).

Keyboard shortcuts
------------------

This feature has the following default keyboard shortcuts:

Keys

Action

Action description

`Space`

_toggleGroup_

When a group header is focused, this expands or collapses the grouped rows

For more information on how to customize keyboard shortcuts, please see the [Customizing keyboard shortcuts guide](https://bryntum.com/docs/gantt/api/#Grid/guides/customization/keymap.md)

This feature is **enabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[field](https://bryntum.com/docs/gantt/api/Grid/feature/Group#config-field)
The name of the record field to group by.

[expandIconCls](https://bryntum.com/docs/gantt/api/Grid/feature/Group#config-expandIconCls)
The icon to use for the expand icon in collapsed state. Not applicable when using Scheduler in vertical mode.

[collapseIconCls](https://bryntum.com/docs/gantt/api/Grid/feature/Group#config-collapseIconCls)
The icon to use for the collapse icon in expanded state. Not applicable when using Scheduler in vertical mode.

[ascending](https://bryntum.com/docs/gantt/api/Grid/feature/Group#config-ascending)
The sort direction of the groups.

[headerHeight](https://bryntum.com/docs/gantt/api/Grid/feature/Group#config-headerHeight)
The height of group header rows. Can also be set on a per-group-header basis using the [renderer](https://bryntum.com/docs/gantt/api/#Grid/feature/Group#config-renderer). Not applicable when using Scheduler in vertical mode.

[showCount](https://bryntum.com/docs/gantt/api/Grid/feature/Group#config-showCount)
Set to `true` to show the number of members of each group in the group header. Not applicable when using Scheduler in vertical mode.

[groupSortFn](https://bryntum.com/docs/gantt/api/Grid/feature/Group#config-groupSortFn)
A function used to sort the groups. When grouping, the records have to be sorted so that records in a group stick together. Technically that means that records having the same [field](https://bryntum.com/docs/gantt/api/#Grid/feature/Group#config-field) value should go next to each other. And this function (if provided) is responsible for applying such grouping order.

```
const grid = new Grid({
    features : {
        group : {
            // group by category
            field       : 'category',
            groupSortFn : (a, b) => {
                const
                    aCategory = a.category || '',
                    bCategory = b.category || '';

                // 1st sort by "calegory" field
                return aCategory > bCategory ? -1 :
                    aCategory < bCategory ? 1 :
                    // inside calegory groups we sort by "name" field
                    (a.name > b.name ? -1 : 1);
            }
        }
    }
});
```

[renderer](https://bryntum.com/docs/gantt/api/Grid/feature/Group#config-renderer)
A function which produces the HTML for a group header. The function is called in the context of this Group feature object. Default group renderer displays the `groupRowFor` and `count`.

You should never modify any records inside this method.

[keyMap](https://bryntum.com/docs/gantt/api/Grid/feature/Group#config-keyMap)
See [Keyboard shortcuts](https://bryntum.com/docs/gantt/api/#Grid/feature/Group#keyboard-shortcuts) for details. Not applicable when using Scheduler in vertical mode.

[toggleOnRowClick](https://bryntum.com/docs/gantt/api/Grid/feature/Group#config-toggleOnRowClick)
By default, clicking anywhere in a group row toggles its expanded/collapsed state. Not applicable when using Scheduler in vertical mode.

Configure this as `false` to limit this to only toggling on click of the expanded/collapsed state icon.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGroup](https://bryntum.com/docs/gantt/api/Grid/feature/Group#property-isGroup)
Identifies an object as an instance of [Group](https://bryntum.com/docs/gantt/api/#Grid/feature/Group) class, or subclass thereof.

[isGroup](https://bryntum.com/docs/gantt/api/Grid/feature/Group#property-isGroup-static)
Identifies an object as an instance of [Group](https://bryntum.com/docs/gantt/api/#Grid/feature/Group) class, or subclass thereof.

[field](https://bryntum.com/docs/gantt/api/Grid/feature/Group#property-field)
The name of the record field to group by.

[ascending](https://bryntum.com/docs/gantt/api/Grid/feature/Group#property-ascending)
The sort direction of the groups.

[headerHeight](https://bryntum.com/docs/gantt/api/Grid/feature/Group#property-headerHeight)
The height of group header rows. Can also be set on a per-group-header basis using the [renderer](https://bryntum.com/docs/gantt/api/#Grid/feature/Group#config-renderer). Not applicable when using Scheduler in vertical mode.

[showCount](https://bryntum.com/docs/gantt/api/Grid/feature/Group#property-showCount)
Set to `true` to show the number of members of each group in the group header. Not applicable when using Scheduler in vertical mode.

[toggleOnRowClick](https://bryntum.com/docs/gantt/api/Grid/feature/Group#property-toggleOnRowClick)
By default, clicking anywhere in a group row toggles its expanded/collapsed state. Not applicable when using Scheduler in vertical mode.

Configure this as `false` to limit this to only toggling on click of the expanded/collapsed state icon.

## Functions

Functions are methods available for calling on the class

[toggleCollapse](https://bryntum.com/docs/gantt/api/Grid/feature/Group#function-toggleCollapse)
Collapses or expands a group header record (you can also pass a record that is part of a group) depending on its current state.

[internalToggleCollapse](https://bryntum.com/docs/gantt/api/Grid/feature/Group#function-internalToggleCollapse)
Collapses or expands a group depending on its current state

[collapseAll](https://bryntum.com/docs/gantt/api/Grid/feature/Group#function-collapseAll)
Collapse all groups. This function is exposed on Grid and can thus be called as `grid.collapseAll()`

[expandAll](https://bryntum.com/docs/gantt/api/Grid/feature/Group#function-expandAll)
Expand all groups. This function is exposed on Grid and can thus be called as `grid.expandAll()`

[onBeforeRenderRow](https://bryntum.com/docs/gantt/api/Grid/feature/Group#function-onBeforeRenderRow)
Called before rendering row contents, used to reset rows no longer used as group rows

[renderCell](https://bryntum.com/docs/gantt/api/Grid/feature/Group#function-renderCell)
Called when a cell is rendered, styles the group rows first cell.

[renderHeader](https://bryntum.com/docs/gantt/api/Grid/feature/Group#function-renderHeader)
Called when a header is rendered, adds grouping icon if grouped by that column.

[populateHeaderMenu](https://bryntum.com/docs/gantt/api/Grid/feature/Group#function-populateHeaderMenu)
Supply items for headers context menu.

[getColumnDragToolbarItems](https://bryntum.com/docs/gantt/api/Grid/feature/Group#function-getColumnDragToolbarItems)
Supply items to ColumnDragToolbar

[onStoreGroup](https://bryntum.com/docs/gantt/api/Grid/feature/Group#function-onStoreGroup)
Called when store grouping changes. Reflects on header and rerenders rows.

[onElementTouchStart](https://bryntum.com/docs/gantt/api/Grid/feature/Group#function-onElementTouchStart)
Store touches when user touches header, used in onElementTouchEnd.

[onElementClick](https://bryntum.com/docs/gantt/api/Grid/feature/Group#function-onElementClick)
React to click on headers (to group by that column if \[alt\] is pressed) and on group rows (expand/collapse).

[toggleGroup](https://bryntum.com/docs/gantt/api/Grid/feature/Group#function-toggleGroup)
Toggle groups with \[space\].

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeToggleGroup](https://bryntum.com/docs/gantt/api/Grid/feature/Group#event-beforeToggleGroup)
Fired when a group is going to be expanded or collapsed using the UI. Returning `false` from a listener prevents the operation

[toggleGroup](https://bryntum.com/docs/gantt/api/Grid/feature/Group#event-toggleGroup)
Fired when one or more groups are expanded or collapsed

## Typedefs

Typedefs are type definitions for the class

[GroupRecord](https://bryntum.com/docs/gantt/api/Grid/feature/Group#typedef-GroupRecord)
A record representing a group header.

In addition to the `groupChildren` property, there is only one field defined in this record. The name of the field is the same as the [field](https://bryntum.com/docs/gantt/api/#Grid/feature/Group#config-field) used for grouping.
