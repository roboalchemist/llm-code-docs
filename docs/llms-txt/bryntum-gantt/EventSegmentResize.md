# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/EventSegmentResize.md

# [EventSegmentResize](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentResize)

Feature that allows resizing an event segment by dragging its end.

This feature is **enabled** by default

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventSegmentResize](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentResize#property-isEventSegmentResize)
Identifies an object as an instance of [EventSegmentResize](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegmentResize) class, or subclass thereof.

[isEventSegmentResize](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentResize#property-isEventSegmentResize-static)
Identifies an object as an instance of [EventSegmentResize](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegmentResize) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[highlightHandle](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentResize#function-highlightHandle)
Highlights handles (applies css that changes cursor).

[unHighlightHandle](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentResize#function-unHighlightHandle)
Unhighlight handles (removes css).

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeEventSegmentResize](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentResize#event-beforeEventSegmentResize)
Fired on the owning Scheduler Pro before resizing starts. Return `false` to prevent the action.

[eventSegmentResizeStart](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentResize#event-eventSegmentResizeStart)
Fires on the owning Scheduler Pro when segment resizing starts

[eventSegmentPartialResize](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentResize#event-eventSegmentPartialResize)
Fires on the owning Scheduler Pro on each segment resize move event

[beforeEventSegmentResizeFinalize](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentResize#event-beforeEventSegmentResizeFinalize)
Fired on the owning Scheduler Pro to allow implementer to prevent immediate finalization by setting `data.context.async = true` in the listener, to show a confirmation popup etc

```
 scheduler.on('beforeEventSegmentResizeFinalize', ({context}) => {
     context.async = true;
     setTimeout(() => {
         // async code don't forget to call finalize
         context.finalize();
     }, 1000);
 })
```

[eventSegmentResizeEnd](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegmentResize#event-eventSegmentResizeEnd)
Fires on the owning Scheduler Pro after the resizing gesture has finished.
