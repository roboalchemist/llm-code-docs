# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/mixin/AssignmentStoreMixin.md

# [AssignmentStoreMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin)

This is a mixin, containing functionality related to managing assignments.

It is consumed by the regular [AssignmentStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/AssignmentStore) class and Scheduler Pros counterpart.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAssignmentStoreMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#property-isAssignmentStoreMixin)
Identifies an object as an instance of [AssignmentStoreMixin](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/AssignmentStoreMixin) class, or subclass thereof.

[isAssignmentStoreMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#property-isAssignmentStoreMixin-static)
Identifies an object as an instance of [AssignmentStoreMixin](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/AssignmentStoreMixin) class, or subclass thereof.

[data](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#property-data)
Applies a new dataset to the AssignmentStore. Use it to plug externally fetched data into the store.

NOTE: References (assignments, resources) on the assignments are determined async by a calculation engine. Thus they cannot be directly accessed after assigning the new dataset.

For example:

```
assignmentStore.data = [{ eventId, resourceId }];
// assignmentStore.first.event is not yet available
```

To guarantee references are available, wait for calculations for finish:

```
assignmentStore.data = [{ eventId, resourceId  }];
await assignmentStore.project.commitAsync();
// assignmentStore.first.event is available
```

Alternatively use `loadDataAsync()` instead:

```
await assignmentStore.loadDataAsync([{ eventId, resourceId }]);
// assignmentStore.first.event is available
```

[loadPriority](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#property-loadPriority)
CrudManager must load stores in the correct order. Lowest first.

[syncPriority](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#property-syncPriority)
CrudManager must sync stores in the correct order. Lowest first.

## Functions

Functions are methods available for calling on the class

[add](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#function-add)
Add assignments to the store.

NOTE: References (event, resource) on the assignments are determined async by a calculation engine. Thus they cannot be directly accessed after using this function.

For example:

```
const [assignment] = assignmentStore.add({ eventId, resourceId });
// assignment.event is not yet available
```

To guarantee references are set up, wait for calculations for finish:

```
const [assignment] = assignmentStore.add({ eventId, resourceId });
await assignmentStore.project.commitAsync();
// assignment.event is available (assuming EventStore is loaded and so on)
```

Alternatively use `addAsync()` instead:

```
const [assignment] = await assignmentStore.addAsync({ eventId, resourceId });
// assignment.event is available (assuming EventStore is loaded and so on)
```

[addAsync](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#function-addAsync)
Add assignments to the store and triggers calculations directly after. Await this function to have up to date references on the added assignments.

```
const [assignment] = await assignmentStore.addAsync({ eventId, resourceId });
// assignment.event is available (assuming EventStore is loaded and so on)
```

[loadDataAsync](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#function-loadDataAsync)
Applies a new dataset to the AssignmentStore and triggers calculations directly after. Use it to plug externally fetched data into the store.

```
await assignmentStore.loadDataAsync([{ eventId, resourceId }]);
// assignmentStore.first.event is available
```

[getOccurrence](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#function-getOccurrence)
Returns a "fake" assignment used to identify a certain occurrence of a recurring event. If passed the original event, it returns `originalAssignment`.

[mapAssignmentsForEvent](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#function-mapAssignmentsForEvent)
Maps over event assignments.

[mapAssignmentsForResource](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#function-mapAssignmentsForResource)
Maps over resource assignments.

[removeAssignmentsForEvent](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#function-removeAssignmentsForEvent)
Removes all assignments for given event

[getAssignmentsForResource](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#function-getAssignmentsForResource)
Returns all assignments for a given resource.

[removeAssignmentsForResource](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#function-removeAssignmentsForResource)
Removes all assignments for given resource

[getResourcesForEvent](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#function-getResourcesForEvent)
Returns all resources assigned to an event.

[getEventsForResource](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#function-getEventsForResource)
Returns all events assigned to a resource

[assignEventToResource](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#function-assignEventToResource)
Creates and adds assignment record(s) for a given event and resource(s).

[unassignEventFromResource](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#function-unassignEventFromResource)
Removes assignment record for a given event and resource.

[isEventAssignedToResource](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#function-isEventAssignedToResource)
Checks whether an event is assigned to a resource.

[getAssignmentForEventAndResource](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/AssignmentStoreMixin#function-getAssignmentForEventAndResource)
Returns an assignment record for a given event and resource
