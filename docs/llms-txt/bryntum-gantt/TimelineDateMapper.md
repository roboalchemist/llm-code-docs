# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/TimelineDateMapper.md

# [TimelineDateMapper](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDateMapper)

Mixin that contains functionality to convert between coordinates and dates etc.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[snap](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDateMapper#config-snap)
Set to `true` to snap to the current time resolution increment while interacting with scheduled events.

The time resolution increment is either determined by the currently applied view preset, or it can be overridden using [timeResolution](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineDateMapper#property-timeResolution).

If you also want to snap to resources while dragging events, set the [snapToResource](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDrag#config-snapToResource) config of the EventDrag feature to `true`.

When the [fillTicks](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineEventRendering#config-fillTicks) option is enabled, snapping will align to full ticks, regardless of the time resolution.

[timeResolution](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDateMapper#config-timeResolution)
Gets/sets the current time resolution object, which contains a unit identifier and an increment count `{ unit, increment }`. This value means minimal task duration you can create using UI.

For example when you drag create a task or drag & drop a task, if increment is 5 and unit is 'minute' that means that you can create tasks in 5 minute increments, or move it in 5 minute steps.

This value is taken from viewPreset [timeResolution](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#field-timeResolution) config by default. When supplying a `Number` to the setter only the `increment` is changed and the `unit` value remains untouched.

```
timeResolution : {
  unit      : 'minute',  //Valid values are "millisecond", "second", "minute", "hour", "day", "week", "month", "quarter", "year".
  increment : 5
}
```

When the [fillTicks](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineEventRendering#config-fillTicks) option is enabled, the resolution will be in full ticks regardless of configured value.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimelineDateMapper](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDateMapper#property-isTimelineDateMapper)
Identifies an object as an instance of [TimelineDateMapper](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineDateMapper) class, or subclass thereof.

[isTimelineDateMapper](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDateMapper#property-isTimelineDateMapper-static)
Identifies an object as an instance of [TimelineDateMapper](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineDateMapper) class, or subclass thereof.

[snap](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDateMapper#property-snap)
Set to `true` to snap to the current time resolution increment while interacting with scheduled events.

The time resolution increment is either determined by the currently applied view preset, or it can be overridden using [timeResolution](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineDateMapper#property-timeResolution).

If you also want to snap to resources while dragging events, set the [snapToResource](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDrag#config-snapToResource) config of the EventDrag feature to `true`.

When the [fillTicks](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineEventRendering#config-fillTicks) option is enabled, snapping will align to full ticks, regardless of the time resolution.

[timeResolution](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDateMapper#property-timeResolution)
Gets/sets the current time resolution object, which contains a unit identifier and an increment count `{ unit, increment }`. This value means minimal task duration you can create using UI.

For example when you drag create a task or drag & drop a task, if increment is 5 and unit is 'minute' that means that you can create tasks in 5 minute increments, or move it in 5 minute steps.

This value is taken from viewPreset [timeResolution](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#field-timeResolution) config by default. When supplying a `Number` to the setter only the `increment` is changed and the `unit` value remains untouched.

```
timeResolution : {
  unit      : 'minute',  //Valid values are "millisecond", "second", "minute", "hour", "day", "week", "month", "quarter", "year".
  increment : 5
}
```

When the [fillTicks](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineEventRendering#config-fillTicks) option is enabled, the resolution will be in full ticks regardless of configured value.

[viewportCenterDate](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDateMapper#property-viewportCenterDate)
Returns the center date of the currently visible timespan of scheduler.

## Functions

Functions are methods available for calling on the class

[getDateFromCoordinate](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDateMapper#function-getDateFromCoordinate)
Gets the date for an X or Y coordinate, either local to the view element or the page based on the 3rd argument. If the coordinate is not in the currently rendered view, null will be returned unless the `allowOutOfRange` parameter is passed a `true`.

[getDateFromXY](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDateMapper#function-getDateFromXY)
Gets the date for an XY coordinate regardless of the orientation of the time axis.

[getDateFromDomEvent](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDateMapper#function-getDateFromDomEvent)
Gets the time for a DOM event such as 'mousemove' or 'click' regardless of the orientation of the time axis.

[getStartEndDatesFromRectangle](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDateMapper#function-getStartEndDatesFromRectangle)
Gets the start and end dates for an element Region

[getDisplayEndDate](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDateMapper#function-getDisplayEndDate)
Method to get a displayed end date value, see [getFormattedEndDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineDateMapper#function-getFormattedEndDate) for more info.

[getFormattedEndDate](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDateMapper#function-getFormattedEndDate)
Method to get a formatted end date for a scheduled event, the grid uses the "displayDateFormat" property defined in the current view preset. End dates are formatted as 'inclusive', meaning when an end date falls on midnight and the date format doesn't involve any hour/minute information, 1ms will be subtracted (e.g. 2010-01-08T00:00:00 will first be modified to 2010-01-07 before being formatted).

[getCoordinateFromDate](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDateMapper#function-getCoordinateFromDate)
Gets the x or y coordinate relative to the scheduler element, or page coordinate (based on the 'local' flag) If the coordinate is not in the currently rendered view, -1 will be returned.

[getTimeSpanDistance](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDateMapper#function-getTimeSpanDistance)
Returns the distance in pixels for the time span in the view.
