# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/TaskSegmentResize.md

# [TaskSegmentResize](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentResize)

Feature that allows resizing a task segment by dragging its end.

This feature is **enabled** by default.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTaskSegmentResize](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentResize#property-isTaskSegmentResize)
Identifies an object as an instance of [TaskSegmentResize](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskSegmentResize) class, or subclass thereof.

[isTaskSegmentResize](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentResize#property-isTaskSegmentResize-static)
Identifies an object as an instance of [TaskSegmentResize](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskSegmentResize) class, or subclass thereof.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeTaskSegmentResize](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentResize#event-beforeTaskSegmentResize)
Fired on the owning Gantt before resizing starts. Return `false` to prevent the action.

[taskSegmentResizeStart](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentResize#event-taskSegmentResizeStart)
Fires on the owning Gantt when event resizing starts

[taskSegmentPartialResize](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentResize#event-taskSegmentPartialResize)
Fires on the owning Gantt on each resize move event

[beforeTaskSegmentResizeFinalize](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentResize#event-beforeTaskSegmentResizeFinalize)
Fired on the owning Gantt to allow implementer to prevent immediate finalization by setting `data.context.async = true` in the listener, to show a confirmation popup etc.

```
 gantt.on('beforeTaskSegmentResizeFinalize', ({context}) => {
     context.async = true;
     setTimeout(() => {
         // async code don't forget to call finalize
         context.finalize();
     }, 1000);
 })
```

[taskSegmentResizeEnd](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentResize#event-taskSegmentResizeEnd)
Fires on the owning Gantt after the resizing gesture has finished.
