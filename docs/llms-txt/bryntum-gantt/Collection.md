# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/util/Collection.md

# [Collection](https://bryntum.com/docs/gantt/api/Core/util/Collection)

A class which encapsulates a [keyed](https://bryntum.com/docs/gantt/api/#Core/util/Collection#function-get), [filterable](https://bryntum.com/docs/gantt/api/#Core/util/Collection#function-addFilter), [sortable](https://bryntum.com/docs/gantt/api/#Core/util/Collection#function-addSorter) collection of objects. Entries may not be atomic data types such as `string` or `number`.

The entries are keyed by their `id` which is determined by interrogating the [idProperty](https://bryntum.com/docs/gantt/api/#Core/util/Collection#config-idProperty).

To filter a Collection, add a [CollectionFilter](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter) using the [addFilter](https://bryntum.com/docs/gantt/api/#Core/util/Collection#function-addFilter) method. A Filter config object may be specified here which will be promoted to a CollectionFilter instance.

To sort a Collection, add a [CollectionSorter](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter) using the [addSorter](https://bryntum.com/docs/gantt/api/#Core/util/Collection#function-addSorter) method. A Sorter config object may be specified here which will be promoted to a CollectionSorter instance.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[idProperty](https://bryntum.com/docs/gantt/api/Core/util/Collection#config-idProperty)
Specify the name of the property of added objects which provides the lookup key

[extraKeys](https://bryntum.com/docs/gantt/api/Core/util/Collection#config-extraKeys)
Specify the names or index configs of properties which are to be indexed for fast lookup.

Index configs use the format `{ property : string, unique : boolean }`. Unique indices stores one index per entry, non-unique stores a `Set`. If left out, `unique` defaults to `true`

[autoFilter](https://bryntum.com/docs/gantt/api/Core/util/Collection#config-autoFilter)
Automatically apply filters on item add.

[sorters](https://bryntum.com/docs/gantt/api/Core/util/Collection#config-sorters)
A [Sorter](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter), or Sorter config object, or an array of these, to use to sort this Collection.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[generation](https://bryntum.com/docs/gantt/api/Core/util/Collection#property-generation)
A counter which is incremented whenever the Collection is mutated in a meaningful way.

If a [splice](https://bryntum.com/docs/gantt/api/#Core/util/Collection#function-splice) call results in no net replacement, removal or addition, then the `generation` will not be incremented.

[values](https://bryntum.com/docs/gantt/api/Core/util/Collection#property-values)
The set of values of this Collection. If this Collection [isFiltered](https://bryntum.com/docs/gantt/api/#Core/util/Collection#property-isFiltered), this yields the filtered data set.

Setting this property replaces the data set.

[filteredValues](https://bryntum.com/docs/gantt/api/Core/util/Collection#property-filteredValues)
The set of filtered values of this Collection (those matching the current filters).

[allValues](https://bryntum.com/docs/gantt/api/Core/util/Collection#property-allValues)
The set of all values of this Collection regardless of filters applied.

[addedValues](https://bryntum.com/docs/gantt/api/Core/util/Collection#property-addedValues)
The set of values added to this Collection since the last sort or replaceValues operation.

[count](https://bryntum.com/docs/gantt/api/Core/util/Collection#property-count)
The number of items in this collection. Note that this honours filtering. See [totalCount](https://bryntum.com/docs/gantt/api/#Core/util/Collection#property-totalCount);

[totalCount](https://bryntum.com/docs/gantt/api/Core/util/Collection#property-totalCount)
The number of items in this collection regardless of filtering.

[idProperty](https://bryntum.com/docs/gantt/api/Core/util/Collection#property-idProperty)
The property name used to extract item `id`s from added objects.

[sorters](https://bryntum.com/docs/gantt/api/Core/util/Collection#property-sorters)
The Collection of [Sorters](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter) for this Collection.

[isSorted](https://bryntum.com/docs/gantt/api/Core/util/Collection#property-isSorted)
A flag which is `true` if this Collection has active [sorters](https://bryntum.com/docs/gantt/api/#Core/util/Collection#property-sorters).

[sortFunction](https://bryntum.com/docs/gantt/api/Core/util/Collection#property-sortFunction)
A sorter function which encapsulates the [Sorters](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter) for this Collection.

[filters](https://bryntum.com/docs/gantt/api/Core/util/Collection#property-filters)
The Collection of [Filters](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter) for this Collection.

[isFiltered](https://bryntum.com/docs/gantt/api/Core/util/Collection#property-isFiltered)
A flag which is `true` if this Collection has active [filters](https://bryntum.com/docs/gantt/api/#Core/util/Collection#property-filters).

[filterFunction](https://bryntum.com/docs/gantt/api/Core/util/Collection#property-filterFunction)
A filter function which encapsulates the [Filters](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter) for this Collection.

## Functions

Functions are methods available for calling on the class

[clear](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-clear)
Clears this collection.

[equals](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-equals)
Compares the content of this Collection with the content of the passed Collection or with the passed array. Order insensitive. This returns `true` if the two objects passed contain the same set of items.

[replaceValues](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-replaceValues)
Replaces the internal `values` array with the passed `values`, or `filteredValues` array with the passed `filteredValues`. If `filteredValues` are not passed explicitly, but storage is filtered, decides internally `values` or `filteredValues` should be replaced by passed `values`.

Note that this takes ownership of the array, and the array must not be mutated by outside code.

This is an internal utility method, not designed for use by application code.

[forEach](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-forEach)
Executes the passed function for each item in this Collection, passing in the item, ths index, and the full item array.

[map](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-map)
Extracts ths content of this Collection into an array based upon the passed value extraction function.

[reduce](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-reduce)
Returns an accumulated value based on the passed function similar to `Array.reduce`.

[find](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-find)
Returns the first item in this Collection which elicits a _truthy_ return value from the passed function.

[match](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-match)
This method ensures that every item in this Collection is replaced by the matched by `id` item in the other Collection.

By default, any items in this Collection which are **not** in the other Collection are removed.

If the second parameter is passed as `false`, then items which are not in the other Collection are not removed.

This can be used for example when updating a selected record Collection when a new Store or new store dataset arrives. The selected Collection must reference the latest versions of the selected record `id`s

[add](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-add)
Adds items to this Collection. Multiple new items may be passed.

By default, new items are appended to the existing values.

Any [sorters](https://bryntum.com/docs/gantt/api/#Core/util/Collection#property-sorters) [sorters](https://bryntum.com/docs/gantt/api/#Core/util/Collection#property-sorters) present are re-run.

Any [filters](https://bryntum.com/docs/gantt/api/#Core/util/Collection#property-filters) [filters](https://bryntum.com/docs/gantt/api/#Core/util/Collection#property-filters) present are re-run.

_Note that if application functionality requires add and remove, the [splice](https://bryntum.com/docs/gantt/api/#Core/util/Collection#function-splice) operation is preferred as it performs both operations in an atomic manner_

[remove](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-remove)
Removes items from this Collection. Multiple items may be passed.

Any [sorters](https://bryntum.com/docs/gantt/api/#Core/util/Collection#property-sorters) [sorters](https://bryntum.com/docs/gantt/api/#Core/util/Collection#property-sorters) present are re-run.

Any [filters](https://bryntum.com/docs/gantt/api/#Core/util/Collection#property-filters) [filters](https://bryntum.com/docs/gantt/api/#Core/util/Collection#property-filters) present are re-run.

_Note that if application functionality requires add and remove, the [splice](https://bryntum.com/docs/gantt/api/#Core/util/Collection#function-splice) operation is preferred as it performs both operations in an atomic manner_

[move](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-move)
Moves an individual item, or a block of items to another location.

[splice](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-splice)
The core data set mutation method. Removes and adds at the same time. Analogous to the `Array` `splice` method.

Note that if items that are specified for removal are also in the `toAdd` array, then those items are _not_ removed then appended. They remain in the same position relative to all remaining items.

[changeId](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-changeId)
Change the id of an existing member by mutating its [idProperty](https://bryntum.com/docs/gantt/api/#Core/util/Collection#config-idProperty).

[get](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-get)
Returns the item with the passed `id`. By default, filtered are honoured, and if the item with the requested `id` is filtered out, nothing will be returned.

To return the item even if it has been filtered out, pass the second parameter as `true`.

[getBy](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-getBy)
Returns the item with passed property name equal to the passed value. By default, filtered are honoured, and if the item with the requested `id` is filtered out, nothing will be returned.

To return the item even if it has been filtered out, pass the third parameter as `true`.

[addSorter](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-addSorter)
Adds a Sorter to the Collection of Sorters which are operating on this Collection.

A Sorter may be specified as an instantiated [CollectionSorter](https://bryntum.com/docs/gantt/api/#Core/util/CollectionSorter), or a config object for a CollectionSorter of the form

```
{
    property  : 'age',
    direction : 'desc'
}
```

Note that by default, a Sorter _replaces_ a Sorter with the same `property` to make it easy to change existing Sorters. A Sorter's `id` is its `property` by default. You can avoid this and add multiple Sorters for one property by configuring Sorters with `id`s.

A Sorter may also be specified as a function which compares two objects eg:

```
(lhs, rhs) => lhs.customerDetails.age - rhs.customerDetails.age
```

[addFilter](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-addFilter)
Adds a Filter to the Collection of Filters which are operating on this Collection.

A Filter may be an specified as an instantiated [CollectionFilter](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter), or a config object for a CollectionFilter of the form

```
{
    property : 'age',
    operator : '>=',
    value    : 21
}
```

Note that by default, a Filter _replaces_ a Filter with the same `property` to make it easy to change existing Filters. A Filter's `id` is its `property` by default. You can avoid this and add multiple Filters for one property by configuring Filters with `id`s.

A Filter may also be specified as a function which filters candidate objects eg:

```
candidate => candidate.customerDetails.age >= 21
```

[addIndex](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-addIndex)
Adds a lookup index for the passed property name or index config. The index is built lazily when an index is searched

[findIndex](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-findIndex)
Return the index of the item with the specified key having the specified value.

By default, filtering is taken into account and this returns the index in the filtered dataset if present. To bypass this, pass the third parameter as `true`.

Only useful for indices configured with `unique: true`.

[findItem](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-findItem)
Return the item with the specified key having the specified value.

By default, filtering is taken into account. To bypass this, pass the third parameter as `true`.

For indices configured with `unique: false`, a Set of items will be returned.

[indexOf](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-indexOf)
Returns the index of the item with the same `id` as the passed item.

By default, filtering is honoured, so if the item in question has been added, but is currently filtered out of visibility, `-1` will be returned.

To find the index in the master, unfiltered dataset, pass the second parameter as `true`;

[includes](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-includes)
Returns `true` if this Collection includes an item with the same `id` as the passed item.

By default, filtering is honoured, so if the item in question has been added, but is currently filtered out of visibility, `false` will be returned.

To query inclusion in the master, unfiltered dataset, pass the second parameter as `true`;

[rebuildIndices](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-rebuildIndices)
Called when the Collection is mutated and the indices have been flagged as invalid.

Rebuilds the indices object to allow lookup by keys.

[addToIndices](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-addToIndices)
Add an item to all indices

[removeFromIndices](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-removeFromIndices)
Remove an item from all indices

[removeIndexEntry](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-removeIndexEntry)
Remove an entry from an index, and if filtering is used also from the filtered index.

[addIndexEntry](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-addIndexEntry)
Add a new entry to an index, and if filtering is used also to the filtered index.

[onItemMutation](https://bryntum.com/docs/gantt/api/Core/util/Collection#function-onItemMutation)
Call externally to update indices on item mutation (from Store)

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[change](https://bryntum.com/docs/gantt/api/Core/util/Collection#event-change)
Fired when items are added, replace or removed

[noChange](https://bryntum.com/docs/gantt/api/Core/util/Collection#event-noChange)
Fired when a [splice](https://bryntum.com/docs/gantt/api/#Core/util/Collection#function-splice) operation is requested but the operation is a no-op and has caused no change to this Collection's dataset. The splice method's parameters are passed for reference.
