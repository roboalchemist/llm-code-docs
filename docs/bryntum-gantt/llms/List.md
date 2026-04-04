# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/List.md

# [List](https://bryntum.com/docs/gantt/api/Core/widget/List)

Displays a list of items which the user can navigate using the keyboard and select using either pointer gestures or the keyboard. Appearance in the built-in themes:

Multi-selection
---------------

Set the [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-multiSelect) flag to `true` to allow multiple items to be selected:

Grouped list
------------

To group the list contents, simply group your store using [groupers](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreGroup#config-groupers). You can decide if clicking a header should toggle all group children (or if it should do nothing) with the [allowGroupSelect](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-allowGroupSelect) flag.

```
const list = new List({
    width            : 400,
    displayField     : 'name',
    multiSelect      : true,
    allowGroupSelect : false,
    // Show icon based on group name
    groupHeaderTpl   : (record, groupName) => `
        <i class="icon-${groupName}"></i>${groupName}
    `,
    value : [1, 4],
    store : new Store({
        fields : [
            'type'
        ],
        groupers : [
            { field : 'type', ascending : true }
        ],
        data : [
            { id : 1, name : 'pizza', type : 'food' },
            { id : 2, name : 'bacon', type : 'food' },
            { id : 3, name : 'egg', type : 'food' },
            { id : 4, name : 'Gin tonic', type : 'drinks' },
            { id : 5, name : 'Wine', type : 'drinks' },
            { id : 6, name : 'Beer', type : 'drinks' }
        ]
    })
});
```

Keyboard shortcuts
------------------

A List has the following default keyboard shortcuts:

Keys

Action description

`Ctrl+a`

Select all

`ArrowRight`

Expands a group item

`ArrowLeft`

Collapses a group item

`Space`

Toggles selection of currently focused item

`Enter`

Toggles selection of currently focused item

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[items](https://bryntum.com/docs/gantt/api/Core/widget/List#config-items)
An array of Objects which are converted into records and used to create this List's [store](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-store)

[displayField](https://bryntum.com/docs/gantt/api/Core/widget/List#config-displayField)
The model field to render into each list item

[store](https://bryntum.com/docs/gantt/api/Core/widget/List#config-store)
A [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store) which provides the records which map to List items. Each record is passed through the [itemTpl](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-itemTpl) to produce the DOM structure of the List. May be generated from an array of [items](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-items).

The store may also be configured as an array of records, or record data objects from which records may be constructed.

[multiSelect](https://bryntum.com/docs/gantt/api/Core/widget/List#config-multiSelect)
Configure as `true` to allow multi select and add checkboxes to the items

[toggleAllIfCtrlPressed](https://bryntum.com/docs/gantt/api/Core/widget/List#config-toggleAllIfCtrlPressed)
Select/deselect all if `CMD`/`CTRL` is pressed when clicking

[collapsibleGroups](https://bryntum.com/docs/gantt/api/Core/widget/List#config-collapsibleGroups)
True to add a collapse icon to toggle groups being collapsed or expanded

[selectAllItem](https://bryntum.com/docs/gantt/api/Core/widget/List#config-selectAllItem)
Set to `true` to add a "Select all" item to the list to select/unselect all items at once. Only applies when [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-multiSelect) mode is enabled.

[itemTpl](https://bryntum.com/docs/gantt/api/Core/widget/List#config-itemTpl)
Template function (or name of a template function), which, when passed a record, returns the textual HTML for that item. Defaults to a function returning the value of the record´s [displayField](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-displayField)

[tooltipTemplate](https://bryntum.com/docs/gantt/api/Core/widget/List#config-tooltipTemplate)
Template function to provide a tooltip (textual, will be automatically HTML-encoded) shown when hovering an item.

[getItemStyle](https://bryntum.com/docs/gantt/api/Core/widget/List#config-getItemStyle)
Configure this as a function or the name of a function, which when passed a record in the list, returns a style string to apply to its list item.

[getItemCls](https://bryntum.com/docs/gantt/api/Core/widget/List#config-getItemCls)
Configure this as a function or the name of a function, which when passed a record in the list, returns a CSS class name string to apply to its list item.

[groupHeaderTpl](https://bryntum.com/docs/gantt/api/Core/widget/List#config-groupHeaderTpl)
Template function which is passed a group record and the uppercased group field name. The text returned will be rendered as the group header.

[allowGroupSelect](https://bryntum.com/docs/gantt/api/Core/widget/List#config-allowGroupSelect)
Configure as `true` to allow selecting groups (all the group child records will be toggled). Only applicable when the store is grouped.

[clearSelectionOnEmptySpaceClick](https://bryntum.com/docs/gantt/api/Core/widget/List#config-clearSelectionOnEmptySpaceClick)
Configure as `true` to clear selection when clicking on empty space inside the List´s element.

[selected](https://bryntum.com/docs/gantt/api/Core/widget/List#config-selected)
A [Collection](https://bryntum.com/docs/gantt/api/#Core/util/Collection), or Collection config object to use to contain this List's selected records.

Or, an array encapsulating the initial selection which this List is to have upon Store load. This may be an array of `id`s , or an array of objects with an `id` property:

```
new List({
    // initially select record IDs 1 and 5 when store loads
    selected : [1, 5]
});
```

[activateOnMouseover](https://bryntum.com/docs/gantt/api/Core/widget/List#config-activateOnMouseover)
Configure as `true` to activate items on mouseover. This is used by the Combo field when using a List as its dropdown.

[title](https://bryntum.com/docs/gantt/api/Core/widget/List#config-title)
The title to show at the top of the list.

[virtualize](https://bryntum.com/docs/gantt/api/Core/widget/List#config-virtualize)
Controls virtualization of list items using the `IntersectionObserver` API to render items only when scrolled into view. This is only useful for lists with complex markup, for simple lists it likely adds overhead.

* `false` or `null` - Virtualization disabled (default)
* `true` - Always virtualize, regardless of item count
* `{Number}` - Virtualize only when item count exceeds this threshold (e.g., `1000`)

Set to `false` to explicitly disable virtualization. This is useful in environments where `IntersectionObserver` is not available (e.g., Salesforce Locker Service).

Note that the overhead from virtualization is most of the time not worth it. Only enable it if you have really large lists with complex item templates.

[listItemHeight](https://bryntum.com/docs/gantt/api/Core/widget/List#config-listItemHeight)
Minimum estimated height of an item in the list. This value is used to estimate how many elements are initially visible when the list is rendered, so initial render with virtualization turned on also displays elements, and is not empty.

[isSelectable](https://bryntum.com/docs/gantt/api/Core/widget/List#config-isSelectable)
A function, or the name of a function in the ownership hierarchy which is used to determine whether a record is selectable. By default, all records are selectable except group header records in a grouped store.

[emptyText](https://bryntum.com/docs/gantt/api/Core/widget/List#config-emptyText)
The text to show when the list is empty. If not set, the list will be empty.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isList](https://bryntum.com/docs/gantt/api/Core/widget/List#property-isList)
Identifies an object as an instance of [List](https://bryntum.com/docs/gantt/api/#Core/widget/List) class, or subclass thereof.

[isList](https://bryntum.com/docs/gantt/api/Core/widget/List#property-isList-static)
Identifies an object as an instance of [List](https://bryntum.com/docs/gantt/api/#Core/widget/List) class, or subclass thereof.

[store](https://bryntum.com/docs/gantt/api/Core/widget/List#property-store)
A [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store) which provides the records which map to List items. Each record is passed through the [itemTpl](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-itemTpl) to produce the DOM structure of the List. May be generated from an array of [items](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-items).

The store may also be configured as an array of records, or record data objects from which records may be constructed.

[multiSelect](https://bryntum.com/docs/gantt/api/Core/widget/List#property-multiSelect)
Configure as `true` to allow multi select and add checkboxes to the items

[toggleAllIfCtrlPressed](https://bryntum.com/docs/gantt/api/Core/widget/List#property-toggleAllIfCtrlPressed)
Select/deselect all if `CMD`/`CTRL` is pressed when clicking

[collapsibleGroups](https://bryntum.com/docs/gantt/api/Core/widget/List#property-collapsibleGroups)
True to add a collapse icon to toggle groups being collapsed or expanded

[allowGroupSelect](https://bryntum.com/docs/gantt/api/Core/widget/List#property-allowGroupSelect)
Configure as `true` to allow selecting groups (all the group child records will be toggled). Only applicable when the store is grouped.

[clearSelectionOnEmptySpaceClick](https://bryntum.com/docs/gantt/api/Core/widget/List#property-clearSelectionOnEmptySpaceClick)
Configure as `true` to clear selection when clicking on empty space inside the List´s element.

[title](https://bryntum.com/docs/gantt/api/Core/widget/List#property-title)
The title to show at the top of the list.

[emptyText](https://bryntum.com/docs/gantt/api/Core/widget/List#property-emptyText)
The text to show when the list is empty. If not set, the list will be empty.

[count](https://bryntum.com/docs/gantt/api/Core/widget/List#property-count)
The number of rendered items in the list, including group headers and the select all item if present.

[items](https://bryntum.com/docs/gantt/api/Core/widget/List#property-items)
May be _set_ as an array of Objects which are converted into records and used to create this List's [store](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-store)

[selected](https://bryntum.com/docs/gantt/api/Core/widget/List#property-selected)
Gets/sets the collection of selected records.

When used as a setter, a record, or record `id` or array of same may be passed to set the selected records.

[allSelected](https://bryntum.com/docs/gantt/api/Core/widget/List#property-allSelected)
Yields `true` if all the available items are selected.

## Functions

Functions are methods available for calling on the class

[getItem](https://bryntum.com/docs/gantt/api/Core/widget/List#function-getItem)
Returns the DOM element representing the passed record (or record id)

[getRecordFromElement](https://bryntum.com/docs/gantt/api/Core/widget/List#function-getRecordFromElement)
Searches up from the specified element for a list item and returns the associated record.

[restoreActiveItem](https://bryntum.com/docs/gantt/api/Core/widget/List#function-restoreActiveItem)
Sets the passed record as the current focused record for keyboard navigation and selection purposes.

[onClick](https://bryntum.com/docs/gantt/api/Core/widget/List#function-onClick)
Selects list items on click.

[onInternalKeyDown](https://bryntum.com/docs/gantt/api/Core/widget/List#function-onInternalKeyDown)
Key events which are not navigation are delegated up to here by the Navigator

[onInternalSelectionChange](https://bryntum.com/docs/gantt/api/Core/widget/List#function-onInternalSelectionChange)
Handles items being added or removed from the selected Collection

[selectAll](https://bryntum.com/docs/gantt/api/Core/widget/List#function-selectAll)
Selects all items in this list.

[deselectAll](https://bryntum.com/docs/gantt/api/Core/widget/List#function-deselectAll)
Deselects all selected items

[select](https://bryntum.com/docs/gantt/api/Core/widget/List#function-select)
Selects the passed item(s).

An item to select may be the `id` of a record in this List's [store](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-store), or it may be an object with an `id` **property** which is the `id` of a record in this List's [store](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-store) (For example one of the records).

[deselect](https://bryntum.com/docs/gantt/api/Core/widget/List#function-deselect)
Deselects the passed item(s).

An item to deselect may be the `id` of a record in this List's [store](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-store), or it may be an object with an `id` **property** which is the `id` of a record in this List's [store](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-store) (For example one of the records).

[toggleCollapse](https://bryntum.com/docs/gantt/api/Core/widget/List#function-toggleCollapse)
Toggles the collapsed state of a group header or tree parent node record

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[item](https://bryntum.com/docs/gantt/api/Core/widget/List#event-item)
User activated an item in the list either by pointer or keyboard. The active record, list item index, and the triggering event are passed.

[beforeItem](https://bryntum.com/docs/gantt/api/Core/widget/List#event-beforeItem)
User going to activate an item in the list either by pointer or keyboard. The active record, list item index, and the triggering event are passed. It is preventable by returning `false`

[selectionChange](https://bryntum.com/docs/gantt/api/Core/widget/List#event-selectionChange)
Fired when selection changes

[toggleGroup](https://bryntum.com/docs/gantt/api/Core/widget/List#event-toggleGroup)
Group item expanded or collapsed

[toggleNode](https://bryntum.com/docs/gantt/api/Core/widget/List#event-toggleNode)
Tree parent node expanded or collapsed
