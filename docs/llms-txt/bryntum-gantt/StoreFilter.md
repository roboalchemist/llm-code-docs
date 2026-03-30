# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/mixin/StoreFilter.md

# [StoreFilter](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter)

Mixin for Store that handles filtering. Filters are instances of [CollectionFilter](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter) class.

* Adding a filter for the same property will replace the current one (unless a unique [id](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-id) is specified), but will not clear any other filters.
* Adding a filter through the [filterBy](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreFilter#function-filterBy) function is ultimate. It will clear all the property based filters and replace the current filterBy function if present.
* Removing records from the store does not remove filters! The filters will be reapplied if [reapplyFilterOnAdd](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreFilter#config-reapplyFilterOnAdd)/[reapplyFilterOnUpdate](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreFilter#config-reapplyFilterOnUpdate) are true and you add new records or update current.

```
// Add a filter
store.filter({
    property : 'score',
    value    : 10,
    operator : '>'
});

// Add filter as a function
store.filter(record => record.score > 10);

// Add named filter as a function
store.filter({
    id : 'my filter',
    filterBy : record => record.score > 10
});

// Replace any filter set with new filters
store.filter({
    filters : {
        property : 'score',
        value    : 10,
        operator : '>'
    },
    replace : true
});

// Remove this one specific filter, leaving any possible others in place.
// A filter's id defaults to the `property-operator` value that it's filtering on.
store.removeFilter('score');

// Reapply filters without firing an event.
// Use if making multiple data mutations with the
// intention of updating UIs when all finished.
store.filter({
    silent : true
});
```

If the store is configured with [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad), only remote filtering is supported. See AjaxStore [filtering](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#remote-filtering) for more details about remote filtering.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[remoteFilter](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter#config-remoteFilter)
Set this to `true` to activate remote filtering in this Store. This makes it possible to use the built-in filtering features of the Store and corresponding UI functionality, without using local data.

For a non-[AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore), data will be requested by the Store by calling a by the app implemented [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-requestData) function. Data can also be provided by listening to the [requestData](https://bryntum.com/docs/gantt/api/#Core/data/Store#event-requestData) event, and updating the [data](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-data) property with new data.

For [AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore), data will be loaded via the configured [readUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-readUrl).

[filterParamName](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter#config-filterParamName)
The name of the parameter to use to pass any filters when loading data remotely.

**Note:** When this is set, filters must be defined using a field name, an operator and a value to compare, **not** a comparison function.

[filters](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter#config-filters)
Specify one or more [CollectionFilter](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter) config objects to apply initially.

For example:

```
 // Configure the store to filter in clients over the age of 30
 new Store({
     ...,
     filters : [{
         property : 'age',
         value    : 30,
         operator : '>'
     }],
     ...
 })
```

or:

```
 // Configure the store to filter based on a complex operation
 new Store({
     ...,
     filters : [{
         filterBy(record) {
             // Return true or false for filtering in or out
             return shouldClientBeVisible(record);
         }
     }],
     ...
 })
```

[reapplyFilterOnAdd](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter#config-reapplyFilterOnAdd)
Specify `true` to reapply filters when a record is added to or moved within the store. This includes tree node operations like indent/outdent in Gantt, or any move operation that changes a node's parent.

[reapplyFilterOnUpdate](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter#config-reapplyFilterOnUpdate)
Specify `true` to reapply filters when a record is updated in the store. You can also provide an array of field names, to only re-filter when certain data fields are updated.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStoreFilter](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter#property-isStoreFilter)
Identifies an object as an instance of [StoreFilter](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreFilter) class, or subclass thereof.

[isStoreFilter](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter#property-isStoreFilter-static)
Identifies an object as an instance of [StoreFilter](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreFilter) class, or subclass thereof.

[filters](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter#property-filters)
Currently applied filters. A collection of [CollectionFilter](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter) instances.

[isFiltered](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter#property-isFiltered)
Check if store is filtered

## Functions

Functions are methods available for calling on the class

[addFilter](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter#function-addFilter)
Adds a single filter to the [filters](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreFilter#config-filters) collection. By default, filters are reevaluated and a Store change event fired.

If the `silent` parameter is passed as `true`, multiple filters can be added without causing data changes.

When the filters are as required, call [filter](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreFilter#function-filter) with no parameters to apply the filters to the store.

[filter](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter#function-filter)
Filters the store by **adding** the specified filter(s) to the existing filters collection applied to this Store. If a filter has an [id](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-id) specified, or a [property](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-property) specified, it will search for corresponding filter(s) in the existing filters first and replace it with a new filter. **It will not remove other filters applied to the store!**

To **add** a new filter:

```
// Filter using simple object
store.filter({
    property : 'age',
    operator : '>',
    value    : 90
});

// Filter using function
store.filter(r => r.age < 90);

// Filter using a named filter as a function
store.filter({
    id : 'my-filter',
    filterBy : record => record.score > 10
});
```

To **remove** a specific filter, but keep other filters applied

```
// Remove by filter `id` or `property`. Filter `id` defaults to the `property-operator` value.
store.removeFilter('age');
store.removeFilter('my-filter');
```

To **replace** all existing filters with a new filter

```
// Remove all filters and filter using simple object
store.filter({
    filters : {
        property : 'age',
        operator : '<',
        value    : 90
    },
    replace : true
});

// Remove all filters and filter using function
store.filter({
    filters : r => r.age > 90,
    replace : true
});

// Remove all filters and filter using a named filter as a function
store.filter({
    filters : {
        id : 'my-filter',
        filterBy : record => record.score > 10
    },
    replace : true
});
```

Basically filters replacing is an equivalent of having two sequenced calls: [clearFilters](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreFilter#function-clearFilters) and [filter](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreFilter#function-filter).

Call without arguments to reapply filters.

```
// Re-filter the store
store.filter();
```

[performFilter](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter#function-performFilter)
Perform filtering according to the [filters](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreFilter#property-filters) Collection. This is the internal implementation which is overridden in [AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore) and must not be overridden.

[filterBy](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter#function-filterBy)
_Adds_ a function used to filter the store. Alias for calling `filter(fn)`. Return `true` from the function to include record in filtered set

```
store.filterBy(record => record.age > 25 && record.name.startsWith('A'));
```

[removeFilter](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter#function-removeFilter)
Removes the passed filter, or the filter by the passed ID from the [filters](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreFilter#config-filters) collection. By default, filters are reevaluated and a Store change event fired.

If the `silent` parameter is passed as `true`, multiple filters can be removed without causing data changes.

When the filters are as required, call [filter](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreFilter#function-filter) with no parameters to apply the filters to the store.

```
// Only view top priority events
myEventStore.filter({
    id       : 'priorityFilter',
    property : 'priority',
    value    : 1,
    operator : '='
});

// That individual filter can be removed like this
myEventStore.removeFilter('priorityFilter');

// Add named filter as a function
store.filter({
    id : 'my filter',
    filterBy : record => record.score > 10
});

// Remove named filter function
store.removeFilter('my filter');
```

[clearFilters](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter#function-clearFilters)
Removes all filters from the store. Filters that are marked as [internal](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-internal) will _not_ be removed.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeFilter](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter#event-beforeFilter)
Fired before filtering

[filter](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreFilter#event-filter)
Fired after applying filters to the store
