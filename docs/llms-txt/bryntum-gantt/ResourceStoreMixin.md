# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/mixin/ResourceStoreMixin.md

# [ResourceStoreMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ResourceStoreMixin)

This is a mixin for the ResourceStore functionality. It is consumed by the [ResourceStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/ResourceStore).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceStoreMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ResourceStoreMixin#property-isResourceStoreMixin)
Identifies an object as an instance of [ResourceStoreMixin](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/ResourceStoreMixin) class, or subclass thereof.

[isResourceStoreMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ResourceStoreMixin#property-isResourceStoreMixin-static)
Identifies an object as an instance of [ResourceStoreMixin](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/ResourceStoreMixin) class, or subclass thereof.

[data](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ResourceStoreMixin#property-data)
Applies a new dataset to the ResourceStore. Use it to plug externally fetched data into the store.

NOTE: References (events, assignments) on the resources are determined async by a calculation engine. Thus they cannot be directly accessed after assigning the new dataset.

For example:

```
resourceStore.data = [{ id }];
// resourceStore.first.events is not yet available
```

To guarantee references are available, wait for calculations for finish:

```
resourceStore.data = [{ id }];
await resourceStore.project.commitAsync();
// resourceStore.first.events is available
```

Alternatively use `loadDataAsync()` instead:

```
await resourceStore.loadDataAsync([{ id }]);
// resourceStore.first.events is available
```

[loadPriority](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ResourceStoreMixin#property-loadPriority)
CrudManager must load stores in the correct order. Lowest first.

[syncPriority](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ResourceStoreMixin#property-syncPriority)
CrudManager must sync stores in the correct order. Lowest first.

## Functions

Functions are methods available for calling on the class

[add](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ResourceStoreMixin#function-add)
Add resources to the store.

NOTE: References (events, assignments) on the resources are determined async by a calculation engine. Thus they cannot be directly accessed after using this function.

For example:

```
const [resource] = resourceStore.add({ id });
// resource.events is not yet available
```

To guarantee references are set up, wait for calculations for finish:

```
const [resource] = resourceStore.add({ id });
await resourceStore.project.commitAsync();
// resource.events is available (assuming EventStore is loaded and so on)
```

Alternatively use `addAsync()` instead:

```
const [resource] = await resourceStore.addAsync({ id });
// resource.events is available (assuming EventStore is loaded and so on)
```

[addAsync](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ResourceStoreMixin#function-addAsync)
Add resources to the store and triggers calculations directly after. Await this function to have up to date references on the added resources.

```
const [resource] = await resourceStore.addAsync({ id });
// resource.events is available (assuming EventStore is loaded and so on)
```

[loadDataAsync](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ResourceStoreMixin#function-loadDataAsync)
Applies a new dataset to the ResourceStore and triggers calculations directly after. Use it to plug externally fetched data into the store.

```
await resourceStore.loadDataAsync([{ id }]);
// resourceStore.first.events is available
```

[getAvailableResources](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ResourceStoreMixin#function-getAvailableResources)
Returns all resources that have no events assigned during the specified time range.
