# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/mixin/DayIndexMixin.md

# [DayIndexMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DayIndexMixin)

Mixing handling Calendars day indices.

Consumed by EventStore in Scheduler & Scheduler Pro and TaskStore in Gantt.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDayIndexMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DayIndexMixin#property-isDayIndexMixin)
Identifies an object as an instance of [DayIndexMixin](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/DayIndexMixin) class, or subclass thereof.

[isDayIndexMixin](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DayIndexMixin#property-isDayIndexMixin-static)
Identifies an object as an instance of [DayIndexMixin](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/DayIndexMixin) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[onDataChange](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DayIndexMixin#function-onDataChange)
Responds to mutations of the underlying storage Collection.

Maintain indices for fast finding of events by date.

[invalidateDayIndices](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DayIndexMixin#function-invalidateDayIndices)
Invalidates associated day indices.

[registerDayIndex](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DayIndexMixin#function-registerDayIndex)
Registers a `DayTime` instance, creating an `EventDayIndex` for each distinct `startShift`. This index is maintained until all instances with a matching `startShift` are [unregistered](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/DayIndexMixin#function-unregisterDayIndex).

[unregisterDayIndex](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DayIndexMixin#function-unregisterDayIndex)
Removes a registered `DayTime` instance. If this is the last instance registered to an `EventDayIndex`, that index is removed.

[useDayIndex](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/DayIndexMixin#function-useDayIndex)
Returns the `EventDayIndex` to use for the given `DayTime` instance. This may be the primary instance or a child instance created by [registerDayIndex](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/DayIndexMixin#function-registerDayIndex).
