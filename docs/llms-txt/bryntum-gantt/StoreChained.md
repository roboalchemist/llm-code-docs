# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/mixin/StoreChained.md

# [StoreChained](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained)

A chained Store contains a subset of records from a master store. Which records to include is determined by a filtering function, [chainedFilterFn](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreChained#config-chainedFilterFn).

```
masterStore.chain(record => record.percent < 10);

// or

new Store({
  masterStore     : masterStore,
  chainedFilterFn : record => record.percent < 10
});
```

Behavior of chained stores
--------------------------

By default, chained stores will be resorted when the master store is sorted. This can be disabled by setting [syncSort](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreChained#config-syncSort) to `false`:

```
store.chain(record => record.percent < 10, null, {
 syncSort : false
});
```

By default, reordering records in a flat chained store will not affect the order in the master store. This can be enabled by setting [syncOrder](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreChained#config-syncOrder) to `true`:

```
store.chain(record => record.percent < 10, null, {
  syncOrder : true
});
```

See [syncOrder](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreChained#config-syncOrder) for a note about the predictability of the outcome. Also note that reordering in a chained tree store will always affect the order in the master store.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[chainedFilterFn](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#config-chainedFilterFn)
Function used to filter records in the masterStore into a chained store. If not provided, all records from the masterStore will be included in the chained store. Return `true` to include the passed record, or a `false` to exclude it.

Only applies to chained stores

[chainedFields](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#config-chainedFields)
Array of field names that should trigger filtering of chained store when the fields are updated.

Only applies to chained stores

[masterStore](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#config-masterStore)
Master store that a chained store gets its records from.

Only applies to chained stores

[doRelayToMaster](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#config-doRelayToMaster)
Method names calls to which should be relayed to master store.

Only applies to chained stores

[dontRelayToMaster](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#config-dontRelayToMaster)
Method names calls to which shouldn't be relayed to master store.

Only applies to chained stores

[excludeCollapsedRecords](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#config-excludeCollapsedRecords)
If `true`, collapsed records in original tree will be excluded from the chained store.

Only applies to chained stores, and not when chaining using `chainTree()`

[syncSort](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#config-syncSort)
If `true`, chained stores will be sorted when the master store is sorted. Note that this replaces any existing sorters defined on the chained store.

Only applies to chained stores

[syncOrder](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#config-syncOrder)
If `true`, changing the order of records in a flat chained store (for example by using the `RowReorder` feature in a Grid-based widget) will also change the order of records in the master store.

Note that this config does not apply to chained tree stores (created using [chainTree](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreChained#function-chainTree)). Chained tree stores always sync the order of their records with the master store.

Example usage:

```
store.chain(record => record.percent < 10, null, {
  syncOrder : true
});
```

The predictability of the outcome depends on the order of the records in both stores, and if the subset of records in the chained store is contiguous. For example, if the master store has records `A B C D E`, and the chained store has `E C A`, it will be difficult for users to predict the outcome of moving `E` to between `C A`.

[ignoreLinkRecords](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#config-ignoreLinkRecords)
Set to true to prevent including links (when grouping by array field)

Only applies to chained stores

[chainFilters](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#config-chainFilters)
If `true`, chained stores will apply filters from the master store. Filters flagged with `ignoreForChain` will be ignored.

Only applies to chained stores

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStoreChained](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#property-isStoreChained)
Identifies an object as an instance of [StoreChained](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreChained) class, or subclass thereof.

[isStoreChained](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#property-isStoreChained-static)
Identifies an object as an instance of [StoreChained](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreChained) class, or subclass thereof.

[isChained](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#property-isChained)
Is this a chained store?

## Functions

Functions are methods available for calling on the class

[fillFromMaster](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#function-fillFromMaster)
Updates records available in a chained store by filtering the master store records using [chainedFilterFn](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreChained#config-chainedFilterFn)

[generateMasterFilterFn](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#function-generateMasterFilterFn)
Generates a filter function for filtering which records from the master store should be included in the chained store, based on the master store's filters, if [chainFilters](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreChained#config-chainFilters) is `true`.

Master store filters flagged with `ignoreForChain` will be ignored.

[commitToMaster](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#function-commitToMaster)
Commits changes back to master.

* the records deleted from chained store and present in master will be deleted from master
* the records added to chained store and missing in master will added to master Internally calls {Store#function-commit commit()}.

[relayToMaster](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#function-relayToMaster)
Relays some function calls to the master store

[onMasterDataChanged](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#function-onMasterDataChanged)
Handles changes in master stores data. Updates the chained store accordingly

[onMasterStoreRefresh](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#function-onMasterStoreRefresh)
Handles refresh events from the master store. During batch operations, individual change events are suppressed and only a refresh event with `action: 'batch'` fires after `endBatch()`. This ensures the chained store stays in sync after batch operations.

[chain](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#function-chain)
Creates a chained store, a new Store instance that contains a subset of the records from current store. Which records is determined by a filtering function, which is reapplied when data in the base store changes.

```
// Chain all records
const all = store.chain();

// Or a subset using a filter function
const oldies = store.chain(record => record.age > 50);
```

If you want to chain a tree store, consider using [chainTree](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-chainTree) instead. It will create a new tree store with links to the records in this store. This will let you expand/collapse and filter nodes in the chained store without affecting the original store.

If this store is a [tree](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreTree#property-isTree) store, then the resulting chained store will be a tree store sharing the same root node, but only child nodes which pass the `chainedFilterFn` will be considered when iterating the tree through the methods such as [traverse](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-traverse) or [forEach](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-forEach).

[chainTree](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChained#function-chainTree)
Creates a chained tree store, a new Store instance that contains a subset of the records from current store. Which records is determined by a filtering function, which is reapplied when data in the base store changes.

```
// Chain all nodes
const fullTree = store.chainTree();
// Or a subset
const oldies = store.chainTree(record => record.age > 50);
```

The resulting chained store will be a tree store with its own root node, under which all children are links to the nodes in this store. This allows for expanding/collapsing and filtering nodes in the chained store without affecting the original store.
