# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/TimelineEventRendering.md

# [TimelineEventRendering](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering)

Functions to handle event rendering (EventModel -> dom elements).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[managedEventSizing](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#config-managedEventSizing)
When `true`, events are sized and positioned based on rowHeight, resourceMargin and barMargin settings. Set this to `false` if you want to control height and vertical position using CSS instead.

Note that events always get an absolute top position, but when this setting is enabled that position will match row's top. To offset within the row using CSS, use `translate : 0 y`.

[generatedIdCls](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#config-generatedIdCls)
The CSS class added to an event/assignment when it is newly created in the UI and unsynced with the server.

[dirtyCls](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#config-dirtyCls)
The CSS class added to an event when it has unsaved modifications

[committingCls](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#config-committingCls)
The CSS class added to an event when it is currently committing changes

[endsOutsideViewCls](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#config-endsOutsideViewCls)
The CSS class added to an event/assignment when it ends outside of the visible time range.

[startsOutsideViewCls](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#config-startsOutsideViewCls)
The CSS class added to an event/assignment when it starts outside of the visible time range.

[fixedEventCls](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#config-fixedEventCls)
The CSS class added to an event/assignment when it is not draggable.

[barMargin](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#config-barMargin)
Controls how much space to leave between stacked event bars in px.

Value will be constrained by half the row height in horizontal mode.

[fillTicks](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#config-fillTicks)
Specify `true` to force rendered events/tasks to fill entire ticks. This only affects rendering, start and end dates retain their value on the data level.

When enabling `fillTicks`, drag-drop interactions use the same granularity as the bottom time axis "ticks". This means if you are viewing a day schedule, and you move an event starting 8am from Monday to Tuesday, it will still always start at 8am. Enabling [snap](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineDateMapper#config-snap) might also improve the UX.

[eventColor](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#config-eventColor)
Event color used by default. Events and resources can specify their own color, with priority order being: Event -> Resource -> Scheduler default.

Specify `null` to use the current primary color, and allow easier control using custom CSS.

For available standard colors, see [EventColor](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#typedef-EventColor).

[eventStyle](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#config-eventStyle)
Event style used by default. Events and resources can specify their own style, with priority order being: Event -> Resource -> Scheduler default. Determines the appearance of the event by assigning a CSS class to it. Available styles are:

* `'tonal'` (default) - flat pale look with text in darker shade of events color
* `'filled'` flat look
* `'bordered'` - has border in darker shade of events color
* `'traced'` - has border in darker shade of events color with a pale fill
* `'outlined'` - only border + text until hovered
* `'indented'` - has colored text and wide left border in same color
* `'rounded'` - minimalistic style with rounded corners
* `'line'` - as a line with the text below it
* `'dashed'` - as a dashed line with the text below it
* `'minimal'` - as a thin line with small text above it
* `'gantt'` - The default style used for Gantt task bars
* `null` - do not apply a default style and take control using custom CSS (easily overridden basic styling will be used).

In addition, there are two styles intended to be used when integrating with Bryntum Calendar. To match the look of Calendar events, you can use:

* `'calendar'` - a variation of the "colored" style matching the default style used by Calendar
* `'interday'` - a variation of the "plain" style, for interday events

[tickSize](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#config-tickSize)
The width/height (depending on vertical / horizontal mode) of all the time columns.

There is a limit for the tick size value. Its minimal allowed value is calculated so ticks would fit the available space. Only applicable when [forceFit](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-forceFit) is set to `false`. To set `tickSize` freely skipping that limitation please set [suppressFit](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-suppressFit) to `true`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimelineEventRendering](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#property-isTimelineEventRendering)
Identifies an object as an instance of [TimelineEventRendering](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineEventRendering) class, or subclass thereof.

[isTimelineEventRendering](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#property-isTimelineEventRendering-static)
Identifies an object as an instance of [TimelineEventRendering](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineEventRendering) class, or subclass thereof.

[barMargin](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#property-barMargin)
Controls how much space to leave between stacked event bars in px.

Value will be constrained by half the row height in horizontal mode.

[fillTicks](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#property-fillTicks)
Specify `true` to force rendered events/tasks to fill entire ticks. This only affects rendering, start and end dates retain their value on the data level.

When enabling `fillTicks`, drag-drop interactions use the same granularity as the bottom time axis "ticks". This means if you are viewing a day schedule, and you move an event starting 8am from Monday to Tuesday, it will still always start at 8am. Enabling [snap](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineDateMapper#config-snap) might also improve the UX.

[eventColor](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#property-eventColor)
Event color used by default. Events and resources can specify their own color, with priority order being: Event -> Resource -> Scheduler default.

Specify `null` to use the current primary color, and allow easier control using custom CSS.

For available standard colors, see [EventColor](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#typedef-EventColor).

[eventStyle](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#property-eventStyle)
Event style used by default. Events and resources can specify their own style, with priority order being: Event -> Resource -> Scheduler default. Determines the appearance of the event by assigning a CSS class to it. Available styles are:

* `'tonal'` (default) - flat pale look with text in darker shade of events color
* `'filled'` flat look
* `'bordered'` - has border in darker shade of events color
* `'traced'` - has border in darker shade of events color with a pale fill
* `'outlined'` - only border + text until hovered
* `'indented'` - has colored text and wide left border in same color
* `'rounded'` - minimalistic style with rounded corners
* `'line'` - as a line with the text below it
* `'dashed'` - as a dashed line with the text below it
* `'minimal'` - as a thin line with small text above it
* `'gantt'` - The default style used for Gantt task bars
* `null` - do not apply a default style and take control using custom CSS (easily overridden basic styling will be used).

In addition, there are two styles intended to be used when integrating with Bryntum Calendar. To match the look of Calendar events, you can use:

* `'calendar'` - a variation of the "colored" style matching the default style used by Calendar
* `'interday'` - a variation of the "plain" style, for interday events

[tickSize](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#property-tickSize)
The width/height (depending on vertical / horizontal mode) of all the time columns.

There is a limit for the tick size value. Its minimal allowed value is calculated so ticks would fit the available space. Only applicable when [forceFit](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-forceFit) is set to `false`. To set `tickSize` freely skipping that limitation please set [suppressFit](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-suppressFit) to `true`.

[eventColors](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#property-eventColors-static)
Predefined event colors, useful in combos etc.

[eventStyles](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#property-eventStyles-static)
Predefined event styles , useful in combos etc.

## Functions

Functions are methods available for calling on the class

[getTickSnappedDate](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#function-getTickSnappedDate)
Snaps a date to tick boundaries when fillTicks is enabled. Used by both horizontal and vertical rendering to ensure consistent behavior.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[tickSizeChange](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineEventRendering#event-tickSizeChange)
Fired when the tick size changes.

```
listeners : {
    tickSizeChange({ source, tickSize }) {
        ....
    },
}
```
