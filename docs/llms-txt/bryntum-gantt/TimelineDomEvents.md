# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/TimelineDomEvents.md

# [TimelineDomEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDomEvents)

Mixin that handles dom events (click etc) for scheduler and rendered events.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[ignoreDomEventsWhileScrolling](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDomEvents#config-ignoreDomEventsWhileScrolling)
Set to `true` to ignore reacting to DOM events (mouseover/mouseout etc) while scrolling. Useful if you want to maximize scroll performance.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimelineDomEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDomEvents#property-isTimelineDomEvents)
Identifies an object as an instance of [TimelineDomEvents](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineDomEvents) class, or subclass thereof.

[isTimelineDomEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDomEvents#property-isTimelineDomEvents-static)
Identifies an object as an instance of [TimelineDomEvents](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineDomEvents) class, or subclass thereof.

[timelineContext](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDomEvents#property-timelineContext)
The currently hovered timeline context. This is updated as the mouse or pointer moves over the timeline.

## Functions

Functions are methods available for calling on the class

[initDomEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDomEvents#function-initDomEvents)
Adds listeners for DOM events for the scheduler and its events. Which events is specified in Scheduler#schedulerEvents.

[handleScheduleEvent](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDomEvents#function-handleScheduleEvent)
Wraps dom Events for the scheduler and event bars and fires as our events. For example click -> scheduleClick or eventClick

[onScheduleScroll](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDomEvents#function-onScheduleScroll)
This handles the scheduler being scrolled below the mouse by trackpad or keyboard events. The context, if present needs to be recalculated.

[getTimelineEventContext](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDomEvents#function-getTimelineEventContext)
Gathers contextual information about the schedule contextual position of the passed event.

Used by schedule mouse event handlers, but also by the scheduleContext feature.

[onElementMouseOver](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDomEvents#function-onElementMouseOver)
Relays mouseover events as eventmouseenter if over rendered event. Also adds Scheduler#overScheduledEventClass to the hovered element.

[onElementMouseOut](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDomEvents#function-onElementMouseOut)
Relays mouseout events as eventmouseleave if out from rendered event. Also removes Scheduler#overScheduledEventClass from the hovered element.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[timeAxisHeaderClick](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDomEvents#event-timeAxisHeaderClick)
Fires after a click on a time axis cell

[timeAxisHeaderDblClick](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDomEvents#event-timeAxisHeaderDblClick)
Fires after a double click on a time axis cell

[timeAxisHeaderContextMenu](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDomEvents#event-timeAxisHeaderContextMenu)
Fires after a right click on a time axis cell

[timelineContextChange](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineDomEvents#event-timelineContextChange)
Fired when the pointer-activated [timelineContext](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineDomEvents#property-timelineContext) has changed.
