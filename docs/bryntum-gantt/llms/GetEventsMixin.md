# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/mixin/GetEventsMixin.md

# [GetEventsMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/GetEventsMixin)

A mixin containing functionality for retrieving a range of events, mainly used during rendering.

Consumed by EventStore in Calendar, Scheduler & Scheduler Pro and TaskStore in Gantt.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGetEventsMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/GetEventsMixin#property-isGetEventsMixin)
Identifies an object as an instance of [GetEventsMixin](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/GetEventsMixin) class, or subclass thereof.

[isGetEventsMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/GetEventsMixin#property-isGetEventsMixin-static)
Identifies an object as an instance of [GetEventsMixin](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/GetEventsMixin) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[getEvents](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/GetEventsMixin#function-getEvents)
Returns an array of events for the date range specified by the `startDate` and `endDate` options.

By default, for any date, this includes any event which _intersects_ that date.

To only include events that are fully contained _within_ the date range, pass the `allowPartial` option as `false`.

By default, any occurrences of recurring events are included in the resulting array (not applicable in Gantt). If that is not required, pass the `includeOccurrences` option as `false`.

Note that if `includeOccurrences` is `true`, the start date and end date options are mandatory. The method must know what range of occurrences needs to be generated and returned.

Example:

```
 visibleEvents = eventStore.getEvents({
     resourceRecord : myResource,
     startDate      : scheduler.timeAxis.startDate,
     endDate        : scheduler.timeAxis.endDate
 });
```

[getEventsAsArray](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/GetEventsMixin#function-getEventsAsArray)
Internal implementation for [getEvents](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/GetEventsMixin#function-getEvents) to use when not using dateMap.

[getEventsAsMap](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/GetEventsMixin#function-getEventsAsMap)
Internal implementation for [getEvents](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/GetEventsMixin#function-getEvents) to use when using dateMap.

[isDateRangeAvailable](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/GetEventsMixin#function-isDateRangeAvailable)
Checks if a date range is available for a given resource.

Note that when asked to check a 0 duration range, any 0 duration events at the same point in time will be considered overlapping.

[getNextAvailableDateRange](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/GetEventsMixin#function-getNextAvailableDateRange)
This function will find the next available start date where the provided duration fits without causing any conflicts. It begins by checking the provided `resources` on the provided `startDate`. And if any conflicting events is found, it restarts searching from the last of the conflicting events and continues like this until a matching time slot is found.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[loadDateRange](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/GetEventsMixin#event-loadDateRange)
Fired when a range of events is requested from the [getEvents](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/GetEventsMixin#function-getEvents) method.

This event fires every time a range of events is requested from the store.

An application may have one of two levels of interest in events being read from a store.  

1. To be notified when **any** event block is requested regardless of what the date range is.
2. To be notified when a **new date range** is requested.

This event allows both types of application to be written. The `changed` property is set if a different date range is requested.

```
new Scheduler({
    eventStore : {
        listeners : {
            loadDateRange({ new : { startDate, endDate }, changed }) {
                // Load new data if user is requesting a different time window.
                if (changed) {
                    fetch(...);
                }
            }
        }
    },
    ...
});
```
