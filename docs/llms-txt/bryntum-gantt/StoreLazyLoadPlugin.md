# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/plugin/StoreLazyLoadPlugin.md

# [StoreLazyLoadPlugin](https://bryntum.com/docs/gantt/api/Core/data/plugin/StoreLazyLoadPlugin)

Plugin for Store that handles lazy loading.

## Functions

Functions are methods available for calling on the class

[getAt](https://bryntum.com/docs/gantt/api/Core/data/plugin/StoreLazyLoadPlugin#function-getAt)
Overrides the Store's `getAt` function. If the record at the provided `index` is already loaded, that record will be returned instantly. If not, a request for a range of records containing that index will be made and a promise that resolves to the requested record when the load completes.

[load](https://bryntum.com/docs/gantt/api/Core/data/plugin/StoreLazyLoadPlugin#function-load)
Only available if the store is configured as [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad). Calling will initiate a load request for 1 chunk of records starting from index 0. If the store has previously been loaded, it will be cleared of all records and all lazy loading cache.

[unload](https://bryntum.com/docs/gantt/api/Core/data/plugin/StoreLazyLoadPlugin#function-unload)
Only available if the store is configured as [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad).

For a flat Store, calling this method will remove the provided records from the store and reload them the next time they are rendered.

For a tree Store, calling this method will remove all child nodes of the provided parent nodes and reload the parent nodes the next time they are rendered or expanded.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[lazyLoadStarted](https://bryntum.com/docs/gantt/api/Core/data/plugin/StoreLazyLoadPlugin#event-lazyLoadStarted)
Fired when the store starts loading new chunks (the store enters a state of loading). This event will not be triggered if new records are requested when the store already is loading.

[lazyLoadEnded](https://bryntum.com/docs/gantt/api/Core/data/plugin/StoreLazyLoadPlugin#event-lazyLoadEnded)
Fired when the store finished loading new chunks (the store stops loading). This event will not be triggered if the store has loading requests pending response.
