# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/EventSegmentDrag.md

# [EventSegmentDrag](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentDrag)

Allows user to drag and drop event segments within the row.

This feature is **enabled** by default

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventSegmentDrag](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentDrag#property-isEventSegmentDrag)
Identifies an object as an instance of [EventSegmentDrag](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegmentDrag) class, or subclass thereof.

[isEventSegmentDrag](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentDrag#property-isEventSegmentDrag-static)
Identifies an object as an instance of [EventSegmentDrag](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegmentDrag) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[updateRecords](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentDrag#function-updateRecords)
Update events being dragged.

[updateSegment](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentDrag#function-updateSegment)
Update assignments being dragged

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeEventSegmentDropFinalize](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentDrag#event-beforeEventSegmentDropFinalize)
Fired on the owning Scheduler to allow implementer to use asynchronous finalization by setting `context.async = true` in the listener, to show a confirmation popup etc.

```
 scheduler.on('beforeEventSegmentDropFinalize', ({ context }) => {
     context.async = true;
     setTimeout(() => {
         // async code don't forget to call finalize
         context.finalize();
     }, 1000);
 })
```

For synchronous one-time validation, simply set `context.valid` to true or false.

```
 scheduler.on('beforeEventSegmentDropFinalize', ({ context }) => {
     context.valid = false;
 })
```

[afterEventSegmentDrop](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentDrag#event-afterEventSegmentDrop)
Fired on the owning Scheduler after an event segment is dropped

[eventSegmentDrop](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentDrag#event-eventSegmentDrop)
Fired on the owning Scheduler when an event segment is dropped

[beforeEventSegmentDrag](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentDrag#event-beforeEventSegmentDrag)
Fired on the owning Scheduler before event segment dragging starts. Return `false` to prevent the action.

[eventSegmentDragStart](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentDrag#event-eventSegmentDragStart)
Fired on the owning Scheduler when event segment dragging starts

[eventSegmentDrag](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentDrag#event-eventSegmentDrag)
Fired on the owning Scheduler when event segments are dragged

[eventSegmentDragAbort](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentDrag#event-eventSegmentDragAbort)
Fired on the owning Scheduler after an event segment drag operation has been aborted

[eventSegmentDragReset](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentDrag#event-eventSegmentDragReset)
Fired on the owning Scheduler after an event segment drag operation regardless of the operation being cancelled or not
