# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/mixin/StoreSync.md

# [StoreSync](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSync)

Mixin that allows Store to sync a new dataset with its existing records, instead of fully replacing everything. Configure Store with `syncDataOnLoad: true` to activate the functionality. Sync is performed when a new dataset is loaded, either by directly assigning it to `store.data` or by loading it using Ajax (if using an AjaxStore).

```
const store = new Store({
  syncDataOnLoad : true,
  data           : [
    { id : 1, name : 'Saitama' },
    { id : 2, name : 'Genos' },
    { id : 3, name : 'Mumen Rider' }
  ]
});

// Sync a new dataset by assigning to data:
store.data = [
  { id : 1, name : 'Caped Baldy' },
  { id : 4, name : 'Horse-Bone' }
];

 // Result : Record 1 updated, record 2 & 3 removed, record 4 added
```

For more details, please see [syncDataOnLoad](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreSync#config-syncDataOnLoad).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[syncDataOnLoad](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSync#config-syncDataOnLoad)
Configure with `true` to sync loaded data instead of replacing existing with a new dataset.

By default (or when configured with `false`) assigning to `store.data` replaces the entire dataset with a new one, creating all new records:

```
store.data = [ { id : 1, name : 'Saitama' } ];

const first = store.first;

store.data = [ { id : 1, name : 'One-Punch man' } ];

// store.first !== first;
```

When configured with `true` the new dataset is instead synced against the old, figuring out what was added, removed and updated:

```
store.data = [ { id : 1, name : 'Saitama' } ];

const first = store.first;

store.data = [ { id : 1, name : 'One-Punch man' } ];

// store.first === first;
```

After the sync, any configured sorters, groupers and filters will be reapplied.

#### Threshold

The sync operation has a configurable threshold, above which the operation will be treated as a batch/refresh and only trigger a single `refresh` event. If threshold is not reached, individual events will be triggered (single `add`, `remove` and possible multiple `update`). To enable the threshold, supply a config object with a `threshold` property instead of `true`:

```
const store = new Store({
    syncDataOnLoad : {
        threshold : '20%'
    }
});
```

`threshold` accepts numbers or strings. A numeric threshold means number of affected records, while a string is used as a percentage of the whole dataset (appending `%` is optional). By default no threshold is used.

#### Missing fields

The value of any field not supplied in the new dataset is by default kept as is (if record is not removed by the sync). This behaviour is configurable, by setting `keepMissingValues : false` in a config object it will reset any unspecified field back to their default values:

```
const store = new Store({
    syncDataOnLoad : {
        keepMissingValues : false
    }
});
```

Considering the following sync operation:

```
// Existing data
{ id : 1, name : 'Saitama', powerLevel : 100 }
// Sync data
{ id : 1, name : 'One-Punch Man' }
```

The result would by default (or when explicitly configured with `true`) be:

```
{ id : 1, name : 'One-Punch Man', powerLevel : 100 }
```

If configured with `keepMissingValues : false` it would instead be:

```
{ id : 1, name : 'One-Punch Man' }
```

Never enable `syncDataOnLoad` on a chained store, it will create an infinite loop when it is populated from the main store (the main store can use the setting)

[shouldSyncDataset](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSync#config-shouldSyncDataset)
Experimental hook to allow app to determine if sync should be performed, and/or for which records.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStoreSync](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSync#property-isStoreSync)
Identifies an object as an instance of [StoreSync](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreSync) class, or subclass thereof.

[isStoreSync](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSync#property-isStoreSync-static)
Identifies an object as an instance of [StoreSync](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreSync) class, or subclass thereof.

[reorderOnSync](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSync#property-reorderOnSync)
When using [syncDataOnLoad](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreSync#config-syncDataOnLoad) and the store is neither sorted nor grouped, the order of the incoming dataset is respected. This has a cost, since records in the store might have to be moved around.

For stores where the order is not important, this behavior can be disabled to improve performance by configuring `reorderOnSync` as `false`.

## Functions

Functions are methods available for calling on the class

[syncDataset](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSync#function-syncDataset)
Syncs a new dataset against the already loaded one, only applying changes. Not intended to be called directly, please configure store with `syncDataOnLoad: true` and assign to `store.data` as usual instead.

```
const store = new Store({
   syncDataOnLoad : true,
   data : [
       // initial data
   ]
});

store.data = [ // new data ]; //  Difference between initial data and new data will be applied
```

## Typedefs

Typedefs are type definitions for the class

[SyncDataOnLoadOptions](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreSync#typedef-SyncDataOnLoadOptions)
Options available when supplying a config object to the `syncDataOnLoad` config.
