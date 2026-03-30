# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/crud/AbstractCrudManager.md

# [AbstractCrudManager](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManager)

This is an abstract class serving as the base for the [CrudManager](https://bryntum.com/docs/gantt/api/#Scheduler/data/CrudManager) class. It implements basic mechanisms to organize batch communication with a server. Yet it does not contain methods related to _data transfer_ nor _encoding_. These methods are to be provided in sub-classes by consuming the appropriate mixins.

For example, this is how the class can be used to implement an JSON encoding system:

```
// let's make new CrudManager using AJAX as a transport system and JSON for encoding
class MyCrudManager extends JsonEncode(AjaxTransport(AbstractCrudManager)) {

}
```

Data transfer and encoding methods
----------------------------------

These are methods that must be provided by subclasses of this class:

* [#sendRequest](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-sendRequest)
* [#cancelRequest](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-cancelRequest)
* [#encode](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-encode)
* [#decode](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-decode)

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[stores](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManager#config-stores)
Sets the list of stores controlled by the CRUD manager.

When adding a store to the CrudManager, make sure the server response format is correct for `load` and `sync` requests. Learn more in the [Working with data](https://bryntum.com/docs/gantt/api/#Scheduler/guides/data/crud_manager_in_depth.md#loading-data) guide.

Store can be provided as in instance, using its `id` or as an [CrudManagerStoreDescriptor](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManager#typedef-CrudManagerStoreDescriptor) object.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAbstractCrudManager](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManager#property-isAbstractCrudManager)
Identifies an object as an instance of [AbstractCrudManager](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManager) class, or subclass thereof.

[isAbstractCrudManager](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManager#property-isAbstractCrudManager-static)
Identifies an object as an instance of [AbstractCrudManager](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManager) class, or subclass thereof.

[revision](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManager#property-revision)
The server revision stamp. The _revision stamp_ is a number which should be incremented after each server-side change. This property reflects the current version of the data retrieved from the server and gets updated after each [load](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-load) and [sync](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-sync) call.

[json](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManager#property-json)
Get or set data of [crudStores](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManager#property-crudStores) as a JSON string.

Get a JSON string:

```

const jsonString = scheduler.crudManager.json;

// returned jsonString:
'{"events":[...],"resources":[...],...}'

// object representation of the returned jsonString:
{
    resources    : [...],
    events       : [...],
    assignments  : [...],
    dependencies : [...],
    timeRanges   : [...],
    // data from other stores
}
```

Set a JSON string (to populate the CrudManager stores):

```
scheduler.crudManager.json = '{"events":[...],"resources":[...],...}'
```

The `xxData` properties are deprecated and will be removed in the future. Use `xx` instead. For example `eventsData` is deprecated, use `events` instead. For now, both naming schemes are included in the data object

[inlineData](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManager#property-inlineData)
Get or set data of CrudManager stores. The returned data is identical to what [toJSON](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManager#function-toJSON) returns:

```

const data = scheduler.crudManager.inlineData;

// data:
{
    events : [...],
    resources : [...],
    dependencies : [...],
    assignments : [...],
    timeRanges : [...],
    resourceTimeRanges : [...],
    ... other stores data
}


// Plug it back in later
scheduler.crudManager.inlineData = data;
```

The `xxData` properties are deprecated and will be removed in the future. Use `xx`instead. For example `eventsData` is deprecated, use `events` instead. For now, both naming schemes are included in the data object

[stores](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManager#property-stores)
A list of registered stores whose server communication will be collected into a single batch. Each store is represented by a _store descriptor_.

[isLoading](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManager#property-isLoading)
Returns true if the crud manager is currently loading data

## Functions

Functions are methods available for calling on the class

[toJSON](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManager#function-toJSON)
Returns the data from all CrudManager `crudStores` in a format that can be consumed by `inlineData`.

Used by JSON.stringify to correctly convert this CrudManager to json.

The returned data is identical to what [inlineData](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManager#property-inlineData) contains.

```

const json = scheduler.crudManager.toJSON();

// json:
{
    events : [...],
    resources : [...],
    dependencies : [...],
    assignments : [...],
    timeRanges : [...],
    resourceTimeRanges : [...],
    // ... other stores data
}
```

Output can be consumed by `inlineData`.

```
const json = scheduler.crudManager.toJSON();

// Plug it back in later
scheduler.crudManager.inlineData = json;
```

The `xxData` properties are deprecated and will be removed in the future. Use `xx`instead. For example `eventsData` is deprecated, use `events` instead. For now, both naming schemes are included in the data object

[addStore](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManager#function-addStore)
Adds a store to the collection.

```
// append stores to the end of collection
crudManager.addStore([
    store1,
    // store id
    'bar',
    // store descriptor
    {
        storeId : 'foo',
        store   : store3
    },
    {
        storeId         : 'bar',
        store           : store4,
        // to write all fields of modified records
        writeAllFields  : true
    }
]);
```

**Note:** Order in which stores are kept in the collection is very essential sometimes. Exactly in this order the loaded data will be put into each store.

When adding a store to the CrudManager, make sure the server response format is correct for `load` and `sync` requests. Learn more in the [Working with data](https://bryntum.com/docs/gantt/api/#Scheduler/guides/data/crud_manager_in_depth.md#loading-data) guide.

## Typedefs

Typedefs are type definitions for the class

[CrudManagerStoreDescriptor](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManager#typedef-CrudManagerStoreDescriptor)
