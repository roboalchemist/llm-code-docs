# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/mixin/StoreGroup.md

# [StoreGroup](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup)

Mixin for Store that handles grouping.

```
// simple grouper
store.group('city');

// grouper as object, descending order
store.group({ field : 'city', ascending : false });

// using custom sorting function
store.group({
    field : 'city',
    fn : (recordA, recordB) => {
        // apply custom logic, for example:
        return recordA.city.length < recordB.city.length ? -1 : 1;
    }
});
```

Currently grouping is not supported when using pagination or if the store is configured with [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad). The underlying store cannot group data that is not fully loaded.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[groupers](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#config-groupers)
Initial groupers, specify to have store grouped automatically after initially setting data

[startGroupsCollapsed](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#config-startGroupsCollapsed)
To have all groups **initially loaded** start collapsed, configure this as `true`.

Note that this only affects the initial load of the store. Subsequent reloads maintain current group state where possible.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStoreGroup](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#property-isStoreGroup)
Identifies an object as an instance of [StoreGroup](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreGroup) class, or subclass thereof.

[isStoreGroup](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#property-isStoreGroup-static)
Identifies an object as an instance of [StoreGroup](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreGroup) class, or subclass thereof.

[groupers](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#property-groupers)
Currently used groupers. To set groupers when remote sorting is enabled by [sortParamName](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-sortParamName) you should use [setGroupers](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreGroup#function-setGroupers) instead to be able to wait for the operation to finish.

[isGrouped](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#property-isGrouped)
Is store currently grouped?

[groupHeaderRecords](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#property-groupHeaderRecords)
Returns all the group header records

## Functions

Functions are methods available for calling on the class

[setGroupers](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#function-setGroupers)
Set groupers.

[getGroupHeaderForRecord](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#function-getGroupHeaderForRecord)
Returns group header record for the passed record or last group header in the store

[group](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#function-group)
Group records, either by replacing current sorters or by adding to them. A grouper can specify a **_custom sorting function_** which will be called with arguments (recordA, recordB). Works in the same way as a standard array sorter, except that returning `null` triggers the stores normal sorting routine. Grouped store **must** always be sorted by the same field.

To clear groupers and stop grouping, use [clearGroupers](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreGroup#function-clearGroupers) method.

```
// simple grouper
store.group('city');

// grouper as object, descending order
store.group({ field : 'city', ascending : false });

// using custom sorting function
store.group({
    field : 'city',
    fn : (recordA, recordB) => {
        // apply custom logic, for example:
        return recordA.city.length < recordB.city.length ? -1 : 1;
    }
});

// Stop grouping
store.clearGroupers();
```

[addGrouper](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#function-addGrouper)
Add a grouping level (a grouper).

[removeGrouper](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#function-removeGrouper)
Removes a grouping level (a grouper)

[clearGroupers](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#function-clearGroupers)
Removes all groupers, turning store grouping off.

[isRecordInGroup](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#function-isRecordInGroup)
Check if a record belongs to a certain group (only for the first grouping level)

[getGroupRecords](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#function-getGroupRecords)
Returns all records in the group with specified groupValue.

[getGroupTitles](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#function-getGroupTitles)
Get all group titles.

[internalIncludeExcludeGroupRecords](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#function-internalIncludeExcludeGroupRecords)
Adds or removes records in a group from storage. Used when expanding/collapsing groups.

[excludeGroupRecords](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#function-excludeGroupRecords)
Removes records in a group from storage. Used when collapsing a group.

[includeGroupRecords](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#function-includeGroupRecords)
Adds records in a group to storage. Used when expanding a group.

[collectGroupRecords](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#function-collectGroupRecords)
Collects all group headers + children, whether expanded or not

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[group](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#event-group)
Fired when grouping changes

## Typedefs

Typedefs are type definitions for the class

[Grouper](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreGroup#typedef-Grouper)
An immutable object representing a store grouper.
