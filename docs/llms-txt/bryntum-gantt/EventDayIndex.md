# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/util/EventDayIndex.md

# [EventDayIndex](https://bryntum.com/docs/gantt/api/Scheduler/data/util/EventDayIndex)

This utility class is used by event stores to index events by their day (a "YYYY-MM-DD" value, also known as a "date key"). This key is produced by a [DayTime](https://bryntum.com/docs/gantt/api/#Core/util/DayTime) instance. If two `DayTime` instances have a common `startShift`, they can share an index.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[dayTime](https://bryntum.com/docs/gantt/api/Scheduler/data/util/EventDayIndex#property-dayTime)
The `DayTime` definition for this index. This is set to the initial DayTime instance but can be used for any other [registered](https://bryntum.com/docs/gantt/api/#Scheduler/data/util/EventDayIndex#function-register) `DayTime` instances since they all posses the same value for `startShift`.

This defaults to [MIDNIGHT](https://bryntum.com/docs/gantt/api/#Core/util/DayTime#property-MIDNIGHT-static).

[store](https://bryntum.com/docs/gantt/api/Scheduler/data/util/EventDayIndex#property-store)
The owning store instance of this index.

[users](https://bryntum.com/docs/gantt/api/Scheduler/data/util/EventDayIndex#property-users)
The `DayTime` instances [registered](https://bryntum.com/docs/gantt/api/#Scheduler/data/util/EventDayIndex#function-register) with this index instance. As instances are [unregistered](https://bryntum.com/docs/gantt/api/#Scheduler/data/util/EventDayIndex#function-unregister) they are removed from this array. Once this array is empty, this index can be discarded.

## Functions

Functions are methods available for calling on the class

[add](https://bryntum.com/docs/gantt/api/Scheduler/data/util/EventDayIndex#function-add)
Adds an event record to the specified index (either "startDate" or "date") for a given `date`.

[addEvent](https://bryntum.com/docs/gantt/api/Scheduler/data/util/EventDayIndex#function-addEvent)
Adds an event record to all indexes for all dates which the event overlaps.

[clear](https://bryntum.com/docs/gantt/api/Scheduler/data/util/EventDayIndex#function-clear)
Clear this index.

[get](https://bryntum.com/docs/gantt/api/Scheduler/data/util/EventDayIndex#function-get)
Returns an object that has properties named by the [dateKey](https://bryntum.com/docs/gantt/api/#Core/util/DayTime#function-dateKey) method, or the array of event records if a `date` is specified, or the event record array and the date key in a 2-element array if `returnKey` is `true`.

[initialize](https://bryntum.com/docs/gantt/api/Scheduler/data/util/EventDayIndex#function-initialize)
Called when this index is first used. Once called, further store changes will be used to maintain this index.

[matches](https://bryntum.com/docs/gantt/api/Scheduler/data/util/EventDayIndex#function-matches)
Returns `true` if the given `dayTime` matches this index.

[remove](https://bryntum.com/docs/gantt/api/Scheduler/data/util/EventDayIndex#function-remove)
Removes an event record from the specified index (either "startDate" or "date") for a given `date`.

[removeEvent](https://bryntum.com/docs/gantt/api/Scheduler/data/util/EventDayIndex#function-removeEvent)
Removes an event record from all indexes for all dates which the event overlaps.

[register](https://bryntum.com/docs/gantt/api/Scheduler/data/util/EventDayIndex#function-register)
This method registers a `dayTime` instance with this index in the `users` array.

[unregister](https://bryntum.com/docs/gantt/api/Scheduler/data/util/EventDayIndex#function-unregister)
This method unregisters a `dayTime` instance, removing it from the `users` array. This method returns `true` if this was the last registered instance and this index is no longer needed.
