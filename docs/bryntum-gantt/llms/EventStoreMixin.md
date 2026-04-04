# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/mixin/EventStoreMixin.md

# [EventStoreMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin)

This is a mixin, containing functionality related to managing events.

It is consumed by the regular [EventStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/EventStore) class and the Scheduler Pro's `EventStore` class.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[removeUnassignedEvent](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#config-removeUnassignedEvent)
Configure with `true` to also remove the event when removing the last assignment from the linked AssignmentStore. This config has no effect when using EventStore in legacy `resourceId`\-mode.

[singleAssignment](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#config-singleAssignment)
Configure with `true` to force single-resource mode, an event can only be assigned to a single resource. If not provided, the mode will be inferred from

1. presence of an assignment store (i.e. multi-assignment)
2. presence of `resourceId` in the event store data (i.e. single assignment mode)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventStoreMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#property-isEventStoreMixin)
Identifies an object as an instance of [EventStoreMixin](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/EventStoreMixin) class, or subclass thereof.

[isEventStoreMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#property-isEventStoreMixin-static)
Identifies an object as an instance of [EventStoreMixin](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/EventStoreMixin) class, or subclass thereof.

[data](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#property-data)
Applies a new dataset to the EventStore. Use it to plug externally fetched data into the store.

NOTE: Dates, durations and relations (assignments, resources) on the events are determined async by a calculation engine. Thus they cannot be directly accessed after assigning the new dataset.

For example:

```
eventStore.data = [{ startDate, duration }];
// eventStore.first.endDate is not yet calculated
```

To guarantee data is in a calculated state, wait for calculations for finish:

```
eventStore.data = [{ startDate, duration }];
await eventStore.project.commitAsync();
// eventStore.first.endDate is calculated
```

Alternatively use `loadDataAsync()` instead:

```
await eventStore.loadDataAsync([{ startDate, duration }]);
// eventStore.first.endDate is calculated
```

[modelClass](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#property-modelClass)
Class used to represent records. Defaults to class EventModel.

[loadPriority](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#property-loadPriority)
CrudManager must load stores in the correct order. Lowest first.

[syncPriority](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#property-syncPriority)
CrudManager must sync stores in the correct order. Lowest first.

## Functions

Functions are methods available for calling on the class

[add](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-add)
Add events to the store.

NOTE: Dates, durations and references (assignments, resources) on the events are determined async by a calculation engine. Thus they cannot be directly accessed after using this function.

For example:

```
eventStore.add({ startDate, duration });
// endDate is not yet calculated
```

To guarantee data is in a calculated state, wait for calculations for finish:

```
eventStore.add({ startDate, duration });
await eventStore.project.commitAsync();
// endDate is calculated
```

Alternatively use `addAsync()` instead:

```
await eventStore.addAsync({ startDate, duration });
// endDate is calculated
```

[addAsync](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-addAsync)
Add events to the store and triggers calculations directly after. Await this function to have up to date data on the added events.

```
await eventStore.addAsync({ startDate, duration });
// endDate is calculated
```

[loadDataAsync](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-loadDataAsync)
Applies a new dataset to the EventStore and triggers calculations directly after. Use it to plug externally fetched data into the store.

```
await eventStore.loadDataAsync([{ startDate, duration }]);
// eventStore.first.endDate is calculated
```

[getEventCounts](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-getEventCounts)
Returns a `Map`, keyed by `YYYY-MM-DD` date keys containing event counts for all the days between the passed `startDate` and `endDate`. Occurrences of recurring events are included.

Example:

```
 eventCounts = eventStore.getEventCounts({
     startDate : scheduler.timeAxis.startDate,
     endDate   : scheduler.timeAxis.endDate
 });
```

[forEachScheduledEvent](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-forEachScheduledEvent)
Calls the supplied iterator function once for every scheduled event, providing these arguments

* event : the event record
* startDate : the event start date
* endDate : the event end date

Returning false cancels the iteration.

[getTotalTimeSpan](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-getTotalTimeSpan)
Returns an object defining the earliest start date and the latest end date of all the events in the store.

[isEventPersistable](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-isEventPersistable)
Checks if given event record is persistable. By default it always is, override EventModels `isPersistable` if you need custom logic.

[filterEventsForResource](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-filterEventsForResource)
Filters the events associated with a resource, based on the function provided. An array will be returned for those events where the passed function returns true.

[getResourcesForEvent](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-getResourcesForEvent)
Returns all resources assigned to an event.

[getEventsForResource](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-getEventsForResource)
Returns all events assigned to a resource. _NOTE:_ this does not include occurrences of recurring events. Use the [getEvents](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/GetEventsMixin#function-getEvents) API to include occurrences of recurring events.

[getAssignmentsForEvent](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-getAssignmentsForEvent)
Returns all assignments for a given event.

[getAssignmentsForResource](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-getAssignmentsForResource)
Returns all assignments for a given resource.

[assignEventToResource](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-assignEventToResource)
Creates and adds assignment record for a given event and a resource.

[unassignEventFromResource](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-unassignEventFromResource)
Removes assignment record for a given event and a resource.

[reassignEventFromResourceToResource](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-reassignEventFromResourceToResource)
Reassigns an event from an old resource to a new resource

[isEventAssignedToResource](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-isEventAssignedToResource)
Checks whether an event is assigned to a resource.

[removeAssignmentsForEvent](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-removeAssignmentsForEvent)
Removes all assignments for given event

[removeAssignmentsForResource](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-removeAssignmentsForResource)
Removes all assignments for given resource

[append](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/EventStoreMixin#function-append)
Appends a new record to the store
