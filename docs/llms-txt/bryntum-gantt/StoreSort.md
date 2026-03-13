# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/mixin/StoreSort.md

# [StoreSort](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort)

Mixin for Store that handles simple sorting as well as multi-level sorting.

```
// single sorter
store.sort('age');

// single sorter as object, descending order
store.sort({ field : 'age', ascending : false });

// multiple sorters
store.sort(['age', 'name']);

// using custom sorting function
store.sort({
    fn : (recordA, recordB) => {
        // apply custom logic, for example:
        return recordA.name.length < recordB.name.length ? -1 : 1;
    }
});

// using locale specific sort (slow)
store.sort({ field : 'name', useLocaleSort : 'sv-SE' });
```

If the store is configured with [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad), only remote sorting is supported. See AjaxStore [sorting](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#remote-sorting) for more details about remote sorting.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[useLocaleSort](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#config-useLocaleSort)
Use `localeCompare()` when sorting, which lets the browser sort in a locale specific order. Set to `true`, a locale string or a locale config to enable.

Enabling this has big negative impact on sorting performance. For more info on `localeCompare()`, see [MDN](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare).

Examples:

```
const store = new Store({
    // Swedish sorting
    useLocaleSort : 'sv-SE'
});

const store = new Store({
    // Swedish sorting with custom casing order
    useLocaleSort : {
        locale    : 'sv-SE',
        caseFirst : 'upper'
    }
});
```

Can also be configured on a per-sorter basis:

```
store.sort({ field: 'name', useLocaleSort : 'sv-SE' });
```

[sorters](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#config-sorters)
Initial sorters, format is:

```
{ sorters : [{ field: 'name', ascending: false }, ...] }
// or
{ sorters : ['name', ...] }
```

[reapplySortersOnAdd](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#config-reapplySortersOnAdd)
Specify true to sort this store after records are added.

[reapplySortersOnUpdate](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#config-reapplySortersOnUpdate)
Specify `true` to reapply sorting when a record is updated in the store. You can also provide an array of field names, to only trigger sort when certain data fields are updated.

If the app processes many records or many record fields in a loop or similar, be sure to temporarily disable this setting. Otherwise, each change will trigger a sort, which will make the processing slow

[remoteSort](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#config-remoteSort)
Set this to `true` to activate remote sorting in this Store. This makes it possible to use the built-in sorting features of the Store and corresponding UI functionality, without using local data.

For a non-[AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore), data will be requested by the Store by calling a by the app implemented [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-requestData) function. Data can also be provided by listening to the [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#event-requestData) event, and updating the [data](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-data) property with new data.

For [AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore), data will be loaded via the configured [readUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-readUrl).

[sortParamName](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#config-sortParamName)
The name of the parameter to use to pass any sorters when loading data remotely.

**Note:** When this is set, sorters must be defined using a field name and an ascending flag, **not** a sort function.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStoreSort](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#property-isStoreSort)
Identifies an object as an instance of [StoreSort](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreSort) class, or subclass thereof.

[isStoreSort](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#property-isStoreSort-static)
Identifies an object as an instance of [StoreSort](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreSort) class, or subclass thereof.

[reapplySortersOnUpdate](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#property-reapplySortersOnUpdate)
Specify `true` to reapply sorting when a record is updated in the store. You can also provide an array of field names, to only trigger sort when certain data fields are updated.

If the app processes many records or many record fields in a loop or similar, be sure to temporarily disable this setting. Otherwise, each change will trigger a sort, which will make the processing slow

[sorters](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#property-sorters)
Currently applied sorters

[isSorted](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#property-isSorted)
Is store sorted?

[sorterFn](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#property-sorterFn)
The sorter function for sorting records in the store.

## Functions

Functions are methods available for calling on the class

[sort](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#function-sort)
Sort records, either by replacing current sorters or by adding to them. A sorter can specify a **_custom sorting function_** which will be called with arguments (recordA, recordB). Works in the same way as a standard array sorter, except that returning `null` triggers the stores normal sorting routine.

```
// single sorter
store.sort('age');

// single sorter as object, descending order
store.sort({ field : 'age', ascending : false });

// multiple sorters
store.sort(['age', 'name']);

// using custom sorting function
store.sort((recordA, recordB) => {
    // apply custom logic, for example:
    return recordA.name.length < recordB.name.length ? -1 : 1;
});

// using locale specific sort (slow)
store.sort({ field : 'name', useLocaleSort : 'sv-SE' });
```

[addSorter](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#function-addSorter)
Add a sorting level (a sorter).

[removeSorter](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#function-removeSorter)
Remove a sorting level (a sorter)

[clearSorters](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#function-clearSorters)
Removes all sorters, turning store sorting off.

[createSorterFn](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#function-createSorterFn)
Creates a function used with Array#sort when sorting the store. Override to use your own custom sorting logic.

[performSort](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#function-performSort)
Perform sorting according to the [sorters](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreSort#config-sorters) configured. This is the internal implementation which is overridden in [AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore) and must not be overridden.

[performRemoteSort](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#function-performRemoteSort)
Internal sort method, only called if [remoteSort](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remoteSort) is set on store. Should not be used in application code directly.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeSort](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#event-beforeSort)
Fired before sorting

[sort](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#event-sort)
Fired after sorting

## Typedefs

Typedefs are type definitions for the class

[Sorter](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSort#typedef-Sorter)
An immutable object representing a store sorter.
