# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/crud/AbstractCrudManagerMixin.md

# [AbstractCrudManagerMixin](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin)

An abstract mixin that supplies most of the CrudManager functionality. It implements basic mechanisms of collecting stores to organize batch communication with a server. It does not contain methods related to _data transfer_ nor _encoding_. These methods are to be provided in sub-classes. Out of the box there are mixins implementing [support of AJAX for data transferring](https://bryntum.com/docs/gantt/api/#Scheduler/crud/transport/AjaxTransport) and [JSON for data encoding system](https://bryntum.com/docs/gantt/api/#Scheduler/crud/encoder/JsonEncoder). For example this is how we make a model that will implement CrudManager protocol and use AJAX/JSON to pass the data to the server:

```
class SystemSettings extends JsonEncode(AjaxTransport(AbstractCrudManagerMixin(Model))) {
    ...
}
```

Data transfer and encoding methods
----------------------------------

These are methods that must be provided by subclasses of this class:

* [sendRequest](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-sendRequest)
* [cancelRequest](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-cancelRequest)
* [encode](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-encode)
* [decode](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-decode)

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[crudStores](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-crudStores)
Sets the list of stores controlled by the CRUD manager.

When adding a store to the CrudManager, make sure the server response format is correct for `load` and `sync` requests. Learn more in the [Working with data](https://bryntum.com/docs/gantt/api/#Scheduler/guides/data/crud_manager_in_depth.md#loading-data) guide.

Store can be provided by itself, its id or as a _store descriptor_.

[storeIdProperty](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-storeIdProperty)
Name of a store property to retrieve store identifiers from. Make sure you have an instance of a store to use it by id. Store identifier is used as a container name holding corresponding store data while transferring them to/from the server. By default, `id` property is used. And in case a container identifier has to differ this config can be used:

```
class CatStore extends Store {
    static configurable = {
        // store id is "meow" but for sending/receiving store data
        // we want to have "cats" container in JSON, so we create a new property "storeIdForCrud"
        id             : 'meow',
        storeIdForCrud : 'cats'
    }
});

// create an instance to use a store by id
new CatStore();

class MyCrudManager extends CrudManager {
    ...
    crudStores           : ['meow'],
    // crud manager will get store identifier from "storeIdForCrud" property
    storeIdProperty  : 'storeIdForCrud'
});
```

The `storeIdProperty` property can also be specified directly on a store:

```
class CatStore extends Store {
    static configurable = {
        // storeId is "meow" but for sending/receiving store data
        // we want to have "cats" container in JSON
        id              : 'meow',
        // so we create a new property "storeIdForCrud"..
        storeIdForCrud  : 'cats',
        // and point CrudManager to use it as the store identifier source
        storeIdProperty  : 'storeIdForCrud'
    }
});

class DogStore extends Store {
    static configurable = {
        // storeId is "dogs" and it will be used as a container name for the store data
        storeId : 'dogs',
        // id is set to get a store by identifier
        id      : 'dogs'
    }
});

// create an instance to use a store by id
new CatStore();
new DogStore();

class MyCrudManager extends CrudManager {
    ...
    crudStores : ['meow', 'dogs']
});
```

[trackResponseType](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-trackResponseType)
When `true` forces the CRUD manager to process responses depending on their `type` attribute. So `load` request may be responded with `sync` response for example. Can be used for smart server logic allowing the server to decide when it's better to respond with a complete data set (`load` response) or it's enough to return just a delta (`sync` response).

[supportShortSyncResponse](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-supportShortSyncResponse)
When `true` the Crud Manager does not require all updated and removed records to be mentioned in the _sync_ response. In this case response should include only server side changes.

**Please note that added records should still be mentioned in response to provide real identifier instead of the phantom one.**

[phantomIdField](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-phantomIdField)
Field name to be used to transfer a phantom record identifier.

[phantomParentIdField](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-phantomParentIdField)
Field name to be used to transfer a phantom parent record identifier.

[autoLoad](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-autoLoad)
Specify `true` to automatically call [load](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-load) method on the next frame after creation.

Called on the next frame to allow a Scheduler (or similar) linked to a standalone CrudManager to register its stores before loading starts.

[autoSyncTimeout](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-autoSyncTimeout)
The timeout in milliseconds to wait before persisting changes to the server. Used when [autoSync](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#config-autoSync) is set to `true`.

[autoSync](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-autoSync)
`true` to automatically persist store changes after edits are made in any of the stores monitored. Please note that sync request will not be invoked immediately but only after [autoSyncTimeout](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#config-autoSyncTimeout) interval.

[resetIdsBeforeSync](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-resetIdsBeforeSync)
`True` to reset identifiers (defined by `idField` config) of phantom records before submitting them to the server.

[syncApplySequence](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-syncApplySequence)
An array of store identifiers sets an alternative sync responses apply order. By default, the order in which sync responses are applied to the stores is the same as they registered in. But in case of some tricky dependencies between stores this order can be changed:

```
class MyCrudManager extends CrudManager {
    // register stores (will be loaded in this order: 'store1' then 'store2' and finally 'store3')
    crudStores : ['store1', 'store2', 'store3'],
    // but we apply changes from server to them in an opposite order
    syncApplySequence : ['store3', 'store2', 'store1']
});
```

[writeAllFields](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-writeAllFields)
`true` to write all fields from the record to the server. If set to `false` it will only send the fields that were modified. Note that any fields that have [persist](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-persist) set to `false` will still be ignored and fields having [alwaysWrite](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-alwaysWrite) set to `true` will always be included.

[loadUrl](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-loadUrl)
Convenience shortcut to set only the url to load from, when you do not need to supply any other config options in the `load` section of the `transport` config.

Using `loadUrl`:

```
{
    loadUrl : 'read.php
}
```

Equals the following `transport` config:

```
{
    transport : {
        load : {
            url : 'read.php'
        }
    }
}
```

When read at runtime, it will return the value from `transport.load.url`.

[syncUrl](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-syncUrl)
Convenience shortcut to set only the url to sync to, when you do not need to supply any other config options in the `sync` section of the `transport` config.

Using `loadUrl`:

```
{
    syncUrl : 'sync.php
}
```

Equals the following `transport` config:

```
{
    transport : {
        load : {
            url : 'sync.php'
        }
    }
}
```

When read at runtime, it will return the value from `transport.sync.url`.

[forceSync](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-forceSync)
Specify as `true` to force sync requests to be sent when calling `sync()`, even if there are no local changes. Useful in a polling scenario, to keep client up to date with the backend.

[ignoreRemoteChangesInSTM](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-ignoreRemoteChangesInSTM)
Set to `true` to make STM ignore changes coming from the backend. This will allow user to only undo redo local changes.

[includeChildrenInRemoveRequest](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-includeChildrenInRemoveRequest)
Set to `false` to only include the id of a removed parent node in the request to the backend (also affects programmatic calls to get [changes](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#property-changes) etc.), and not the ids of its children.

Consider the following scenario, removing parent 1:

```
{
  id : 1,
  children : [
    { id : 11 },
    { id : 12 }
  ]
}
```

With `includeChildrenInRemoveRequest : false`, the backend will only receive the removal of id 1.

With `includeChildrenInRemoveRequest : true` (the default), the backend will receive the removal of id 1, 11 and 12.

[syncConflictResolution](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#config-syncConflictResolution)
Specifies the way to handle conflicts happening when applying `sync` responses to served stores, The conflicts could happen when remote coming changes interfere with local changes made after sending the request.

Supported values are:

* `local` local modifications are preserved and corresponding remote changes get rejected
* `remote` remote changes gets applied overriding the local modifications.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAbstractCrudManagerMixin](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#property-isAbstractCrudManagerMixin)
Identifies an object as an instance of [AbstractCrudManagerMixin](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin) class, or subclass thereof.

[isAbstractCrudManagerMixin](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#property-isAbstractCrudManagerMixin-static)
Identifies an object as an instance of [AbstractCrudManagerMixin](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin) class, or subclass thereof.

[crudRevision](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#property-crudRevision)
The server revision stamp. The _revision stamp_ is a number which should be incremented after each server-side change. This property reflects the current version of the data retrieved from the server and gets updated after each [load](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-load) and [sync](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-sync) call.

[crudStores](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#property-crudStores)
A list of registered stores whose server communication will be collected into a single batch. Each store is represented by a _store descriptor_.

[syncApplySequence](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#property-syncApplySequence)
An array of stores presenting an alternative sync responses apply order. Each store is represented by a _store descriptor_.

[loadUrl](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#property-loadUrl)
Convenience shortcut to set only the url to load from, when you do not need to supply any other config options in the `load` section of the `transport` config.

Using `loadUrl`:

```
{
    loadUrl : 'read.php
}
```

Equals the following `transport` config:

```
{
    transport : {
        load : {
            url : 'read.php'
        }
    }
}
```

When read at runtime, it will return the value from `transport.load.url`.

[syncUrl](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#property-syncUrl)
Convenience shortcut to set only the url to sync to, when you do not need to supply any other config options in the `sync` section of the `transport` config.

Using `loadUrl`:

```
{
    syncUrl : 'sync.php
}
```

Equals the following `transport` config:

```
{
    transport : {
        load : {
            url : 'sync.php'
        }
    }
}
```

When read at runtime, it will return the value from `transport.sync.url`.

[forceSync](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#property-forceSync)
Specify as `true` to force sync requests to be sent when calling `sync()`, even if there are no local changes. Useful in a polling scenario, to keep client up to date with the backend.

[ignoreRemoteChangesInSTM](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#property-ignoreRemoteChangesInSTM)
Set to `true` to make STM ignore changes coming from the backend. This will allow user to only undo redo local changes.

[isChangeTrackingSuspended](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#property-isChangeTrackingSuspended)
Returns `true` if changes tracking is suspended

[isCrudManagerLoading](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#property-isCrudManagerLoading)
Returns true if the crud manager is currently loading data

[isCrudManagerSyncing](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#property-isCrudManagerSyncing)
Returns true if the crud manager is currently syncing data

[changes](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#property-changes)
Returns current changes as an object consisting of added/modified/removed arrays of records for every managed store, keyed by each store's `id`. Returns `null` if no changes exist. Format:

```
{
    resources : {
        added    : [{ name : 'New guy' }],
        modified : [{ id : 2, name : 'Mike' }],
        removed  : [{ id : 3 }]
    },
    events : {
        modified : [{  id : 12, name : 'Cool task' }]
    },
    ...
}
```

[requestId](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#property-requestId)
Generates unique request identifier.

[crudStoresJSON](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#property-crudStoresJSON)
Returns the data from all CrudManager `crudStores` in a format that can be consumed by `inlineData`.

## Functions

Functions are methods available for calling on the class

[sendRequest](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-sendRequest)
Sends request to the server.

[cancelRequest](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-cancelRequest)
Cancels request to the server.

[encode](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-encode)
Encodes request to the server.

[decode](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-decode)
Decodes response from the server.

[getStoreDescriptor](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-getStoreDescriptor)
Returns a registered store descriptor.

[getCrudStore](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-getCrudStore)
Returns a registered store.

[addCrudStore](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-addCrudStore)
Adds a store to the collection.

```
// append stores to the end of collection
crudManager.addCrudStore([
    store1,
    // storeId
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

[removeCrudStore](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-removeCrudStore)
Removes a store from collection. If the store was registered in alternative sync sequence list it will be removed from there as well.

```
// remove store having storeId equal to "foo"
crudManager.removeCrudStore("foo");

// remove store3
crudManager.removeCrudStore(store3);
```

[addStoreToApplySequence](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-addStoreToApplySequence)
Adds a store to the alternative sync responses apply sequence. By default, the order in which sync responses are applied to the stores is the same as they registered in. But this order can be changes either on construction step using [syncApplySequence](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#config-syncApplySequence) option or by calling this method.

**Please note**, that if the sequence was not initialized before this method call then you will have to do it yourself like this for example:

```
// alternative sequence was not set for this crud manager
// so let's fill it with existing stores keeping the same order
crudManager.addStoreToApplySequence(crudManager.crudStores);

// and now we can add our new store

// we will load its data last
crudManager.addCrudStore(someNewStore);
// but changes to it will be applied first
crudManager.addStoreToApplySequence(someNewStore, 0);
```

add registered stores to the sequence along with the store(s) you want to add

[removeStoreFromApplySequence](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-removeStoreFromApplySequence)
Removes a store from the alternative sync sequence.

```
// remove store having storeId equal to "foo"
crudManager.removeStoreFromApplySequence("foo");
```

[suspendAutoSync](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-suspendAutoSync)
Suspends automatic sync upon store changes. Can be called multiple times (it uses an internal counter).

[resumeAutoSync](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-resumeAutoSync)
Resumes automatic sync upon store changes. Will schedule a sync if the internal counter is 0.

[suspendChangeTracking](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-suspendChangeTracking)
Suspends [hasChanges](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#event-hasChanges) and [noChanges](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#event-noChanges) events.

[resumeChangeTracking](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-resumeChangeTracking)
Resumes [hasChanges](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#event-hasChanges) and [noChanges](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#event-noChanges) events. By default, it will check for changes and if there are any, `hasChanges` or `noChanges` event will be triggered.

[crudStoreHasChanges](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-crudStoreHasChanges)
Returns `true` if any of registered stores (or some particular store) has non persisted changes.

```
// if we have any unsaved changes
if (crudManager.crudStoreHasChanges()) {
    // persist them
    crudManager.sync();
// otherwise
} else {
    alert("There are no unsaved changes...");
}
```

[loadCrudManagerData](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-loadCrudManagerData)
Loads data to the Crud Manager

[load](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-load)
Loads data to the stores registered in the crud manager. For example:

```
crudManager.load(
    // here are request parameters
    {
        store1 : { append : true, page : 3, smth : 'foo' },
        store2 : { page : 2, bar : '!!!' }
    }
).then(
    () => alert('OMG! It works!'),
    ({ response, cancelled }) => console.log(`Error: ${cancelled ? 'Cancelled' : response.message}`)
);
```

\*\* Note: \*\* If there is an incomplete load request in progress then system will try to cancel it by calling [cancelRequest](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-cancelRequest).

[applyChangeset](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-applyChangeset)
Applies a set of changes, as an object keyed by store id, to the affected stores. This function is intended to use in apps that handle their own data syncing, it is not needed when using the CrudManager approach.

Example of a changeset:

```
project.applyChangeset({
    events : {
        added : [
            { id : 10, name : 'Event 10', startDate : '2022-06-07' }
        ],
        updated : [
            { id : 5, name : 'Changed' }
        ],
        removed : [
            { id : 1 }
        ]
    },
    resources : { ... },
    ...
});
```

Optionally accepts a `transformFn` to convert an incoming changeset to the expected format. See [applyChangeset](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-applyChangeset) for more details.

Setting `clearChanges` param to `false` will result in restoring the changes on the store applied using the `applyChangeset` method. By default, it has been set to `true` to clear all the applied changes on the store.

For example, following will restore the changes on the store:

```
// Apply these changes using the applyChangeset method
project.applyChangeset({
    events : {
        added : [
            { id : 10, name : 'Event 10', startDate : '2022-06-07' }
        ],
        updated : [
            { id : 5, name : 'Changed' }
        ],
        removed : [
            { id : 1 }
        ]
    },
    resources : { ... },
    ...
}, null, '$PhantomId', false);
```

In SchedulerPro and Gantt, when [autoSync](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#config-autoSync) is enabled, and client wants to apply changes without triggering a sync request, **applyProjectChanges** method should be used instead of this. It helps maintain current behavior while providing flexibility for scenarios where syncing is not required.

[sync](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-sync)
Persists changes made on the registered stores to the server and/or receives changes made on the backend. Usage:

```
// persist and run a callback on request completion
crud.sync().then(
    () => console.log("Changes saved..."),
    ({ response, cancelled }) => console.log(`Error: ${cancelled ? 'Cancelled' : response.message}`)
);
```

\*\* Note: \*\* If there is an incomplete sync request in progress then system will queue the call and delay it until previous request completion. In this case [syncDelayed](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#event-syncDelayed) event will be fired.

\*\* Note: \*\* Please take a look at [autoSync](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#config-autoSync) config. This option allows to persist changes automatically after any data modification.

\*\* Note: \*\* By default a sync request is only sent if there are any local [changes](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#property-changes). To always send a request when calling this function, configure [forceSync](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#config-forceSync) as `true`.

[acceptChanges](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-acceptChanges)
Accepts all changes in all stores, resets the modification tracking:

* Clears change tracking for all records
* Clears added
* Clears modified
* Clears removed Leaves the store in an "unmodified" state.

[revertChanges](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-revertChanges)
Reverts all changes in all stores and re-inserts any records that were removed locally. Any new uncommitted records will be removed.

[doDestroy](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#function-doDestroy)
Removes all stores and cancels active requests.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeResponseApply](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#event-beforeResponseApply)
Fires before server response gets applied to the stores. Return `false` to prevent data applying. This event can be used for server data preprocessing. To achieve it user can modify the `response` object.

[beforeLoadApply](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#event-beforeLoadApply)
Fires before loaded data get applied to the stores. Return `false` to prevent data applying. This event can be used for server data preprocessing. To achieve it user can modify the `response` object.

[beforeSyncApply](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#event-beforeSyncApply)
Fires before sync response data get applied to the stores. Return `false` to prevent data applying. This event can be used for server data preprocessing. To achieve it user can modify the `response` object.

[hasChanges](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#event-hasChanges)
Fires when data in any of the registered data stores is changed.

```
    crudManager.on('hasChanges', function (crud) {
        // enable persist changes button when some store gets changed
        saveButton.enable();
    });
```

You can suspend this event with [suspendChangeTracking](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-suspendChangeTracking) API call.

[requestFail](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#event-requestFail)
Fires when a request fails.

[loadFail](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#event-loadFail)
Fires when a [load request](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-load) fails.

[syncFail](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#event-syncFail)
Fires when a [sync request](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-sync) fails.

[requestDone](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#event-requestDone)
Fires on successful request completion after data gets applied to the stores.

[load](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#event-load)
Fires on successful [load request](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-load) completion after data gets loaded to the stores.

[sync](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#event-sync)
Fires on successful [sync request](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-sync) completion.

[noChanges](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#event-noChanges)
Fires when registered stores get into state when they don't have any not persisted change. This happens after [load](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-load) or [sync](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-sync) request completion. Or this may happen after a record update which turns its fields back to their original state.

```
crudManager.on('nochanges', function (crud) {
    // disable persist changes button when there is no changes
    saveButton.disable();
});
```

You can suspend this event with [suspendChangeTracking](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-suspendChangeTracking) API call.

[beforeLoad](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#event-beforeLoad)
Fires before [load request](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-load) is sent. Return `false` to cancel load request.

[loadCanceled](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#event-loadCanceled)
Fired after [load request](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-load) was canceled by some [beforeLoad](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#event-beforeLoad) listener or due to incomplete prior load request.

[syncDelayed](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#event-syncDelayed)
Fires after [sync request](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-sync) was delayed due to incomplete previous one.

[beforeSync](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#event-beforeSync)
Fires before [sync request](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-sync) is sent. Return `false` to cancel sync request.

```
crudManager.on('beforesync', function() {
    // cannot persist changes before at least one record is added
    // to the `someStore` store
    if (!someStore.getCount()) return false;
});
```

[syncCanceled](https://bryntum.com/docs/gantt/api/Scheduler/crud/AbstractCrudManagerMixin#event-syncCanceled)
Fires after [sync request](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-sync) was canceled by some [beforeSync](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#event-beforeSync) listener.
