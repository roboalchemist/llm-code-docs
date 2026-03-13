# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/DelayedRecordsRendering.md

# [DelayedRecordsRendering](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/DelayedRecordsRendering)

Mixin that implements scheduling/unscheduling a delayed row refresh.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDelayedRecordsRendering](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/DelayedRecordsRendering#property-isDelayedRecordsRendering)
Identifies an object as an instance of [DelayedRecordsRendering](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/DelayedRecordsRendering) class, or subclass thereof.

[isDelayedRecordsRendering](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/DelayedRecordsRendering#property-isDelayedRecordsRendering-static)
Identifies an object as an instance of [DelayedRecordsRendering](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/DelayedRecordsRendering) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[unscheduleRecordRefresh](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/DelayedRecordsRendering#function-unscheduleRecordRefresh)
Cancels scheduled rows refresh.

[scheduleRecordRefresh](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/DelayedRecordsRendering#function-scheduleRecordRefresh)
Schedules the provided record row refresh.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[scheduledRecordsRender](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/DelayedRecordsRendering#event-scheduledRecordsRender)
This event fires when records which rendering was previously scheduled is finally done.
