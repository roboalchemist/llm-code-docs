# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/mixin/DependencyStoreMixin.md

# [DependencyStoreMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DependencyStoreMixin)

This is a mixin, containing functionality related to managing dependencies.

It is consumed by the regular [DependencyStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/DependencyStore) class and Scheduler Pros counterpart.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[allowedDependencyTypes](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DependencyStoreMixin#config-allowedDependencyTypes)
An array of allowed dependency types. When set, only the specified dependency types can be created. Use values from [DependencyModel.Type](https://bryntum.com/docs/gantt/api/#Scheduler/model/DependencyBaseModel#property-Type-static):

* `0` - StartToStart (SS)
* `1` - StartToEnd (SF)
* `2` - EndToStart (FS)
* `3` - EndToEnd (FF)

```
const scheduler = new Scheduler({
    project : {
        dependencyStore : {
            // Only allow Finish-to-Start and Start-to-Start dependencies
            allowedDependencyTypes : [DependencyModel.Type.EndToStart, DependencyModel.Type.EndToEnd]
        }
    }
});
```

When `null` (default), all dependency types are allowed.

This config affects:

* Drag-creating dependencies (invalid types will be rejected)
* The dependency editor type combo (only allowed types are shown)
* The Predecessors and Successors tabs in the Task Editor

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDependencyStoreMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DependencyStoreMixin#property-isDependencyStoreMixin)
Identifies an object as an instance of [DependencyStoreMixin](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/DependencyStoreMixin) class, or subclass thereof.

[isDependencyStoreMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DependencyStoreMixin#property-isDependencyStoreMixin-static)
Identifies an object as an instance of [DependencyStoreMixin](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/DependencyStoreMixin) class, or subclass thereof.

[data](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DependencyStoreMixin#property-data)
Applies a new dataset to the DependencyStore. Use it to plug externally fetched data into the store.

NOTE: References (fromEvent, toEvent) on the dependencies are determined async by a calculation engine. Thus they cannot be directly accessed after assigning the new dataset.

For example:

```
dependencyStore.data = [{ from, to }];
// dependencyStore.first.fromEvent is not yet available
```

To guarantee references are available, wait for calculations for finish:

```
dependencyStore.data = [{ from, to }];
await dependencyStore.project.commitAsync();
// dependencyStore.first.fromEvent is available
```

Alternatively use `loadDataAsync()` instead:

```
await dependencyStore.loadDataAsync([{ from, to }]);
// dependencyStore.first.fromEvent is available
```

[loadPriority](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DependencyStoreMixin#property-loadPriority)
CrudManager must load stores in the correct order. Lowest first.

[syncPriority](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DependencyStoreMixin#property-syncPriority)
CrudManager must sync stores in the correct order. Lowest first.

## Functions

Functions are methods available for calling on the class

[add](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DependencyStoreMixin#function-add)
Add dependencies to the store.

NOTE: References (fromEvent, toEvent) on the dependencies are determined async by a calculation engine. Thus they cannot be directly accessed after using this function.

For example:

```
const [dependency] = dependencyStore.add({ from, to });
// dependency.fromEvent is not yet available
```

To guarantee references are set up, wait for calculations for finish:

```
const [dependency] = dependencyStore.add({ from, to });
await dependencyStore.project.commitAsync();
// dependency.fromEvent is available (assuming EventStore is loaded and so on)
```

Alternatively use `addAsync()` instead:

```
const [dependency] = await dependencyStore.addAsync({ from, to });
// dependency.fromEvent is available (assuming EventStore is loaded and so on)
```

[addAsync](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DependencyStoreMixin#function-addAsync)
Add dependencies to the store and triggers calculations directly after. Await this function to have up to date references on the added dependencies.

```
const [dependency] = await dependencyStore.addAsync({ from, to });
// dependency.fromEvent is available (assuming EventStore is loaded and so on)
```

[loadDataAsync](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DependencyStoreMixin#function-loadDataAsync)
Applies a new dataset to the DependencyStore and triggers calculations directly after. Use it to plug externally fetched data into the store.

```
await dependencyStore.loadDataAsync([{ from, to }]);
// dependencyStore.first.fromEvent is available
```

[getEventDependencies](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DependencyStoreMixin#function-getEventDependencies)
Returns all dependencies for a certain event (both incoming and outgoing)

[getDependencyForSourceAndTargetEvents](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DependencyStoreMixin#function-getDependencyForSourceAndTargetEvents)
Returns dependency model instance linking tasks with given ids. The dependency can be forward (from 1st task to 2nd) or backward (from 2nd to 1st).

[getEventsLinkingDependency](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DependencyStoreMixin#function-getEventsLinkingDependency)
Returns a dependency model instance linking given events if such dependency exists in the store. The dependency can be forward (from 1st event to 2nd) or backward (from 2nd to 1st).

[isValidDependency](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DependencyStoreMixin#function-isValidDependency)
Validation method used to validate a dependency. Override and return `true` to indicate that an existing dependency between two tasks is valid. For a new dependency being created please see [isValidDependencyToCreate](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/DependencyStoreMixin#function-isValidDependencyToCreate).

[isValidDependencyToCreate](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DependencyStoreMixin#function-isValidDependencyToCreate)
Validation method used to validate a dependency while creating. Override and return `true` to indicate that a new dependency is valid to be created.

[isDependencyTypeAllowed](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DependencyStoreMixin#function-isDependencyTypeAllowed)
Returns `true` if the specified dependency type is allowed according to the [allowedDependencyTypes](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/DependencyStoreMixin#config-allowedDependencyTypes) configuration.

[getHighlightedDependencies](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DependencyStoreMixin#function-getHighlightedDependencies)
Returns all dependencies highlighted with the given CSS class
