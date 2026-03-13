# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/SchedulerDomEvents.md

# [SchedulerDomEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents)

Mixin that handles dom events (click etc) for scheduler and rendered events.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulerDomEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#property-isSchedulerDomEvents)
Identifies an object as an instance of [SchedulerDomEvents](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerDomEvents) class, or subclass thereof.

[isSchedulerDomEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#property-isSchedulerDomEvents-static)
Identifies an object as an instance of [SchedulerDomEvents](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerDomEvents) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[onElementKeyDown](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#function-onElementKeyDown)
Relays keydown events as eventkeydown if we have a selected task.

[onElementKeyUp](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#function-onElementKeyUp)
Relays keyup events as eventkeyup if we have a selected task.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[scheduleMouseDown](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#event-scheduleMouseDown)
Triggered when user mousedowns over an empty area in the schedule.

[scheduleMouseEnter](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#event-scheduleMouseEnter)
Triggered when mouse enters an empty area in the schedule.

[scheduleMouseLeave](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#event-scheduleMouseLeave)
Triggered when mouse leaves an empty area in the schedule.

[scheduleMouseUp](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#event-scheduleMouseUp)
Triggered when user mouseups over an empty area in the schedule.

[scheduleMouseMove](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#event-scheduleMouseMove)
Triggered when user moves mouse over an empty area in the schedule.

[scheduleClick](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#event-scheduleClick)
Triggered when user clicks an empty area in the schedule.

[scheduleDblClick](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#event-scheduleDblClick)
Triggered when user double-clicks an empty area in the schedule.

[scheduleContextMenu](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#event-scheduleContextMenu)
Triggered when user right-clicks an empty area in the schedule.

[eventMouseDown](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#event-eventMouseDown)
Triggered for mouse down on an event.

[eventMouseUp](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#event-eventMouseUp)
Triggered for mouse up on an event.

[eventClick](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#event-eventClick)
Triggered for click on an event.

[eventDblClick](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#event-eventDblClick)
Triggered for double-click on an event.

[eventContextMenu](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#event-eventContextMenu)
Triggered for right-click on an event.

[eventMouseEnter](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#event-eventMouseEnter)
Triggered when the mouse enters an event bar.

[eventMouseLeave](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#event-eventMouseLeave)
Triggered when the mouse leaves an event bar.

[eventMouseOver](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#event-eventMouseOver)
Triggered for mouse over events when moving into and within an event bar.

Note that `mouseover` events bubble, therefore this event will fire while moving from element to element _within_ an event bar.

_If only an event when moving into the event bar is required, use the [eventMouseEnter](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerDomEvents#event-eventMouseEnter) event._

[eventMouseOut](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerDomEvents#event-eventMouseOut)
Triggered for mouse out events within and when moving out of an event bar.

Note that `mouseout` events bubble, therefore this event will fire while moving from element to element _within_ an event bar.

_If only an event when moving out of the event bar is required, use the [eventMouseLeave](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerDomEvents#event-eventMouseLeave) event._
