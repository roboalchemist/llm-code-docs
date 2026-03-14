# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/state/StateProvider.md

# [StateProvider](https://bryntum.com/docs/gantt/api/Core/state/StateProvider)

Instances of this class are used to manage data storage for objects that use the [State](https://bryntum.com/docs/gantt/api/#Core/mixin/State) mixin, i.e. stateful components. When such components change their [stateful](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateful) properties, they notify the associated [stateProvider](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateProvider), which will save the changes after a short delay (to allow multiple changes to coalesce into a single save operation).

There are two (2) built-in types of storage supported by `StateProvider`:

* `local` : Stores data in the browser's `localStorage`. Because of this, all `StateProvider` instances share their state data if they have the same [prefix](https://bryntum.com/docs/gantt/api/#Core/state/StateProvider#config-prefix).
* `memory` : Stores data in the provider's memory. Each instance has its own storage. This is typically used when the state data is saved to a backend server.

Using `local` Storage
---------------------

The global `StateProvider` is typically to use `localStorage` for the page or application like so:

```
 StateProvider.setup('local');
```

With this provider in place, all [stateful components](https://bryntum.com/docs/gantt/api/#Core/mixin/State) will save their [state](https://bryntum.com/docs/gantt/api/#Core/mixin/State#property-state) to this provider by default.

This is the most typical, and recommended, strategy for proving data to stateful components. This approach allows various widgets on the page to simply declare their [stateId](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateId) to participate in the saving and restoring of application state.

Because this storage type uses `localStorage`, the `StateProvider` applies a string prefix to isolate its data from other users of `localStorage`. The default prefix is `'bryntum-state:'`, but this can be configured to a different value. This could be desired, for example, to isolate state data from multiple pages or for version changes.

```
 StateProvider.setup({
     storage : 'local',
     prefix  : 'myApp-v1:'
 });
```

Using `memory` Storage
----------------------

In some applications it may be desirable to save state to a server and restore it on other devices for the user. Because state data is consumed synchronously, and server I/O is asynchronous, the `StateProvider` can be configured to use `'memory'` storage and the actual state data can be loaded/saved by the application.

Two factors are important to consider before deciding to save application state on the server (beyond the async adaptation):

* State properties are often more of a reflection of the user's device than they are application preferences and, therefore, may not apply well on other devices.
* Potentially undesired application state will not be cleared by clearing local browser user data (a common troubleshooting strategy) and will follow the user to other browsers (another common troubleshooting technique).

The use this type of storage, the global `StateProvider` is configured like so:

```
StateProvider.setup('memory');
```

In this scenario, application code would download the user's state and use [data](https://bryntum.com/docs/gantt/api/#Core/state/StateProvider#property-data) to populate the [StateProvider.instance](https://bryntum.com/docs/gantt/api/#Core/state/StateProvider#property-instance-static). In this case, the [save](https://bryntum.com/docs/gantt/api/#Core/state/StateProvider#event-save) event is used to save the data back to the server when it changes.

See [state](https://bryntum.com/docs/gantt/api/https://bryntum.com/products/grid/examples/state/) demo for a usage example.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[prefix](https://bryntum.com/docs/gantt/api/Core/state/StateProvider#config-prefix)
The key prefix applied when using the `'local'` [storage](https://bryntum.com/docs/gantt/api/#Core/state/StateProvider#config-storage) type.

[storage](https://bryntum.com/docs/gantt/api/Core/state/StateProvider#config-storage)
One of the following storage types:

* `local` : Stores data in the browser's `localStorage` using the [prefix](https://bryntum.com/docs/gantt/api/#Core/state/StateProvider#config-prefix).
* `memory` : Stores data in the provider's memory.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[storage](https://bryntum.com/docs/gantt/api/Core/state/StateProvider#property-storage)
Storage instance

[instance](https://bryntum.com/docs/gantt/api/Core/state/StateProvider#property-instance-static)
The default [stateProvider](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateProvider) for stateful objects.

[data](https://bryntum.com/docs/gantt/api/Core/state/StateProvider#property-data)
On read, this property returns all state data stored in the provider. On write, this property _adds_ all the given values to the state provider's data. To replace the data, call [clear](https://bryntum.com/docs/gantt/api/#Core/state/StateProvider#function-clear) before assigning this property. This is used to bulk populate this `StateProvider` with data for stateful components.

## Functions

Functions are methods available for calling on the class

[setup](https://bryntum.com/docs/gantt/api/Core/state/StateProvider#function-setup-static)
Initializes the default `StateProvider` instance for the page. This method can be passed an instance or one of the following type aliases:

* `'local'` : use `localStorage` to store application state (most common)
* `'memory'` : holds application state in the `StateProvider` instance (used when state is saved to a server)

Once the `StateProvider` is initialized, components that use [State](https://bryntum.com/docs/gantt/api/#Core/mixin/State) and assign components a [stateId](https://bryntum.com/docs/gantt/api/#Core/mixin/State#config-stateId) will use this default provider to automatically save and restore their state.

[clear](https://bryntum.com/docs/gantt/api/Core/state/StateProvider#function-clear)
Clears all state date

[saveStateful](https://bryntum.com/docs/gantt/api/Core/state/StateProvider#function-saveStateful)
This method is called to schedule saving the given `stateful` object.

[writeStatefuls](https://bryntum.com/docs/gantt/api/Core/state/StateProvider#function-writeStatefuls)
A delayable method that flushes pending stateful objects.

[getValue](https://bryntum.com/docs/gantt/api/Core/state/StateProvider#function-getValue)
Returns the stored state given its `key`.

[setValue](https://bryntum.com/docs/gantt/api/Core/state/StateProvider#function-setValue)
Stores the given state `value` under the specified `key`.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[save](https://bryntum.com/docs/gantt/api/Core/state/StateProvider#event-save)
Triggered after one or more stateful objects save their state to the state provider. This event can be used to save state to a backend server.

For example, to save the page's state object as a single object on the server:

```
 StateProvider.instance.on({
     save() {
         const data = StateProvider.instance.data;
         // Save "data" to server
     }
 });
```

Or, to save individual stateful components to the server:

```
 StateProvider.instance.on({
     save({ stateIds }) {
         for (const stateId of stateIds) {
             const data = StateProvider.instance.getValue(stateId);

             if (data == null) {
                 // Remove "stateId" from the server
             }
             else {
                 // Save new "data" for "stateId" to the server
             }
         }
     }
 });
```

Multi-page applications should probably include a page identifier in addition to the `stateId` to prevent state from one page affecting other pages. If there are common components across all (or many) pages, the `stateId` values would need to be assigned with all pages in mind.

[set](https://bryntum.com/docs/gantt/api/Core/state/StateProvider#event-set)
Triggered after an item is stored to the state provider.

[remove](https://bryntum.com/docs/gantt/api/Core/state/StateProvider#event-remove)
Triggered after an item is removed from the state provider.
