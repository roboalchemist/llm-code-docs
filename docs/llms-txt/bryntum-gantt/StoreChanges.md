# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/mixin/StoreChanges.md

# [StoreChanges](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChanges)

Mixin for Store that handles applying changes (presumable from a backend)

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[applyChangesetFilterSortTarget](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChanges#config-applyChangesetFilterSortTarget)
Specifies target to filter and sort after applying changeset:

* `'changes'` - apply sort and filter to changeset only (see more below)
* `'none'` - do not apply sort and filter

### `changes` behavior

If the store has filters in effect when the changeset is applied, the following rules will determine how the filtered values are affected:

* Among added records, only those that match the filter will be included in the filtered set
* Among updated records, those that did not previously match the filter but now do will be added to the filtered set, and those that did match but no longer do will also remain in the filtered set. This means that new records may appear in the filtered set as a result of `applyChanges`, but records will not disappear until filters are re-applied.

Does not apply if the store is [remotely filtered](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remoteFilter).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStoreChanges](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChanges#property-isStoreChanges)
Identifies an object as an instance of [StoreChanges](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreChanges) class, or subclass thereof.

[isStoreChanges](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChanges#property-isStoreChanges-static)
Identifies an object as an instance of [StoreChanges](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreChanges) class, or subclass thereof.

[applyChangesetFilterSortTarget](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChanges#property-applyChangesetFilterSortTarget)
Specifies target to filter and sort after applying changeset:

* `'changes'` - apply sort and filter to changeset only (see more below)
* `'none'` - do not apply sort and filter

### `changes` behavior

If the store has filters in effect when the changeset is applied, the following rules will determine how the filtered values are affected:

* Among added records, only those that match the filter will be included in the filtered set
* Among updated records, those that did not previously match the filter but now do will be added to the filtered set, and those that did match but no longer do will also remain in the filtered set. This means that new records may appear in the filtered set as a result of `applyChanges`, but records will not disappear until filters are re-applied.

Does not apply if the store is [remotely filtered](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-remoteFilter).

## Functions

Functions are methods available for calling on the class

[applyChangesFromStore](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChanges#function-applyChangesFromStore)
Applies changes from another store to this store. Useful if cloning records in one store to display in a grid in a popup etc. to reflect back changes.

[applyChangeset](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChanges#function-applyChangeset)
Applies a set of changes (presumable from a backend) expressed as an object matching the format outputted by the [changes](https://bryntum.com/docs/gantt/api/#Core/data/Store#property-changes) property: `{ added : [], modified/updated : [], removed : [] }`

`added` is expected to be an array of raw data objects consumable by the stores model class for records to add to the store (see example snippet below).

`modified` (or `updated` for compatibility with Schedulers CrudManager) is expected to have the same format as `added`, but should always include the `id` of the record to update.

Records that have been created locally and gets assigned a proper id by the backend are expected to also pass a `phantomId` field (name of the field is configurable using the `phantomIdField` arg, more info on phantom ids below), to match it with the current id of a local record (`id` will contain the new id).

Note that it is also possible to pass this `phantomId` -> `id` mapping in the `added` array. When encountering a record in that array that already exists in the local store, it will be treated the same way as a record in the `modified` array.

`removed` is expected to be an array of objects with the `{ id : xx }` shape. Any matches on an id in the store will be removed, those and any non-matches will also be cleared from the change tracking of the store.

If the store has filters in effect when the changeset is applied, the following rules will determine how the filtered values are affected:

* Among added records, only those that match the filter will be included in the filtered set
* Among updated records, those that did not previously match the filter but now do will be added to the filtered set, and those that did match but no longer do will also remain in the filtered set. This means that new records may appear in the filtered set as a result of `applyChanges`, but records will not disappear until filters are re-applied.

As an example, consider a store with the following initial state and some operations performed on it:

```
// Load some data
store.data = [
    { id : 1, name : 'Minerva' },
    { id : 2, name : 'Mars' },
    { id : 3, name : 'Jupiter' }
];
// Add a new record. It gets assigned a generated id,
// for example, 'generated56'
store.add({ name : 'Artemis' });
// Remove Jupiter
store.remove(3);
```

After syncing those operations to a custom backend (however, you chose to solve it in your application), we might get the following response (see "Transforming a response to the correct format" below if your backend responds in another format):

```
const serverResponse = {
    added : [
        // Added by the backend, will be added locally
        { id : 5, name : 'Demeter' }
    ],

    updated : [
        // Will change the name of Minerva -> Athena
        { id : 1, name : 'Athena' },
        // Will set proper id 4 for Artemis
        { $PhantomId : 'generated56', id : 4 }
    ],

    removed : [
        // Confirmed remove of Jupiter
        { id : 3 },
        // Removed by the backend, Mars will be removed locally
        { id : 2 }
    ]
};
```

If that response is then passed to this function:

```
store.applyChangeset(serverResponse);
```

The result will be the following data in the store:

```
[
    { id : 1, name : 'Athena' }, // Changed name
    { id : 4, name : 'Artemis' }, // Got a proper id
    { id : 5, name : 'Demeter' } // Added by the backend
]
```

### Phantom ids

When a record is created locally, it is always assigned a generated id. That id is called a phantom id (note that it is assigned to the normal id field). When passing the new record to the backend, the id is sent with it. When the backend inserts the record into the database, it (normally) gets a proper id assigned. That id then needs to be passed back in the response, to update the local record with the correct id. Making sure that future updates match the correct row in the database.

For example, a newly created record should be passed similar to this to the backend (pseudo format, up to the application/backend to decide):

```
{
    "added" : {
        "id" : "generated79",
        "name" : "Hercules",
        ...
    }
}
```

For the backend response to be applicable for this function, it should then respond with:

```
{
    "updated" : {
        {
            "$PhantomId" : "generated79",
            "id" : 465
        }
    }
}
```

(Or, as stated above, it can also be passed in the "added" array. Whichever suits your backend best).

This function will then change the id of the local record using the phantom id `generated79` to `465`.

### Transforming a response to the correct format

This function optionally accepts a `transformFn`, a function that will be called with the `changes`. It is expected to return a changeset in the format described above (`{ added : [], updated : [], removed : [] }`), which then will be used to apply the changes.

Consider the following "non-standard" (made-up) changeset:

```
const changes = {
    // Database ids for records previously added locally
    assignedIds : {
        'phantom1' : 10,
        'phantom2' : 15
    },
    // Ids records removed by the backend
    removed : [11, 27],
    // Modified records, keyed by id
    altered : {
        12 : { name : 'Changed' }
    },
    // New records, keyed by id
    inserted : {
        20  : { name : 'New' }
    }
}
```

Since it does not match the expected format, it has to be transformed:

```
store.applyChangeset(changes, ({ assignedIds, inserted, altered, removed }) => ({
   // Convert inserted to [{ id : 20, name : 'New' }]
   added : Object.entries(inserted).map(([id, data] => ({ id, ...data }),
   updated : [
       // Convert assignedIds to [{ $PhantomId : 'phantom1', id : 10 }, ...]
      ...Object.entries(assignedIds).map(([phantomId, id])) => ({ $PhantomId : phantomId, id }),
      // Convert altered to [{ id : 12, name : 'Changed' }]
      ...Object.entries(modified).map(([id, data] => ({ id, ...data })
   ],
   // Convert removed to [{ id : 11 }, ...]
   removed : removed.map(id => ({ id }))
}));
```

The transform function above would output:

```
{
    added : [
        {  id : 20, name : 'New' }
    ],
    updated : [
        { $PhantomId : 'phantom1', id : 10 },
        { $PhantomId : 'phantom2', id : 15 },
        {  id : 12, name : 'Changed' }
    ],
    removed : [
       { id : 11 },
       { id : 12 }
    ]
}
```

And that format can then be applied.

### Preventing automatic commit of applied changes

By default, the `clearChanges` parameter is set to `true`, which automatically commits applied changes to the store. Setting this parameter to `false` prevents the automatic commit, keeping the store in a `dirty` state.

For example, the following will apply changes without committing them:

```
const changes = {
    added : [
        {  id : 20, name : 'New' }
    ],
    updated : [
        { id : 10, name : 'Fiona' },
    ],
    removed : [
       { id : 11 }
    ]
};

// Apply these changes using the applyChangeset method
store.applyChangeset(changes, null, '$PhantomId', false);
```

[filterChangeset](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChanges#function-filterChangeset)
Filters records that have been added/updated as part of a changeset. The `added` and `updated` parameters are arrays of values that have already been added/updated in the Collection's values. This method brings the Collection's `_filteredValues` in sync without performing a full sort or filter, using the following rules:

* Added records that do not match the filter are removed from \_filteredValues

* Updated records that now match the filter are inserted at the correct position in \_filteredValues if they were not formerly included

* Updated records, which formerly matched the filter, but now do not, are NOT removed from \_filteredValues

If the collection is sorted, either on its own or via a sort applied at the store level, that sort order is respected when adding items to \_filteredValues. If not, items are inserted in the same order they occur in \_values.

[filterTreeHierarchyChanges](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChanges#function-filterTreeHierarchyChanges)
This method is required to filter out unnecessary orderedParentIndex/parentIndex changes. Those change when we reorder nodes or append new records. If we reorder nodes, we need to apply those changes and then sort the local array according to contents. But if we added nodes, we should ignore such changes in siblings of the added nodes and should recalculate indices right away.

[includeInSubset](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreChanges#function-includeInSubset)
Given an array `all`, an array `subset` that is a subset of `all` in the same order, and another array `toInclude` that is a different subset of `all` disjoint with `subset`, add each item from `toInclude` to `subset`, in an order matching the order in `all`. The order of `subset` must match the order of `all`. The order of `toInclude` is unimportant.

Modifies `subset` in-place.
