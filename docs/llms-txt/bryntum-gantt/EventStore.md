# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/data/EventStore.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/EventStore.md

# [EventStore](https://bryntum.com/docs/gantt/api/Scheduler/data/EventStore)

A store holding all the [events](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) to be rendered into a [Scheduler](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler).

This store only accepts a model class inheriting from [EventModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel).

An EventStore is usually connected to a project, which binds it to other related stores (AssignmentStore, ResourceStore and DependencyStore). The project also handles normalization/calculation of the data on the records in the store. For example if a record is added with a `startDate` and an `endDate`, it will calculate the `duration`.

The calculations happens async, records are not guaranteed to have up to date data until they are finished. To be certain that calculations have finished, call `await project.commitAsync()` after store actions. Or use one of the `xxAsync` functions, such as `loadDataAsync()`.

Using `commitAsync()`:

```
eventStore.data = [{ startDate, endDate }, ...];

// duration of the record is not yet calculated

await eventStore.project.commitAsync();

// now it is
```

Using `loadDataAsync()`:

```
await eventStore.loadDataAsync([{ startDate, endDate }, ...]);

// duration is calculated
```

Using recurring events
----------------------

When recurring events are in the database, **all recurring event definitions** which started before the requested start date, and have not yet finished recurring MUST be loaded into the EventStore.

Only the **base** recurring event **definitions** are stored in the EventStore. You do not need to calculate the future occurrence dates of these events. This is all handled by the EventStore.

When asked to yield a set of events for a certain date range for creating a UI through [getEvents](https://bryntum.com/docs/gantt/api/#Scheduler/data/EventStore#function-getEvents), the EventStore _automatically_ interpolates any occurrences of recurring events into the results. They do not occupy slots in the EventStore for every date in their repetition range (that would be very inefficient, and _might_ be infinite).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[modelClass](https://bryntum.com/docs/gantt/api/Scheduler/data/EventStore#config-modelClass)
Class used to represent records

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventStore](https://bryntum.com/docs/gantt/api/Scheduler/data/EventStore#property-isEventStore)
Identifies an object as an instance of [EventStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/EventStore) class, or subclass thereof.

[isEventStore](https://bryntum.com/docs/gantt/api/Scheduler/data/EventStore#property-isEventStore-static)
Identifies an object as an instance of [EventStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/EventStore) class, or subclass thereof.
