# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/TaskDragCreate.md

# [TaskDragCreate](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDragCreate)

A feature that allows the user to schedule tasks by dragging in the empty parts of the gantt timeline row. Note, this feature is only applicable for unscheduled tasks.

This feature is **enabled** by default

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTaskDragCreate](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDragCreate#property-isTaskDragCreate)
Identifies an object as an instance of [TaskDragCreate](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskDragCreate) class, or subclass thereof.

[isTaskDragCreate](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDragCreate#property-isTaskDragCreate-static)
Identifies an object as an instance of [TaskDragCreate](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskDragCreate) class, or subclass thereof.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[dragCreateEnd](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDragCreate#event-dragCreateEnd)
Fires on the owning Gantt after the task has been scheduled.

[beforeDragCreate](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDragCreate#event-beforeDragCreate)
Fires on the owning Gantt at the beginning of the drag gesture

[dragCreateStart](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDragCreate#event-dragCreateStart)
Fires on the owning Gantt after the drag start has created a proxy element.

[beforeDragCreateFinalize](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDragCreate#event-beforeDragCreateFinalize)
Fires on the owning Gantt to allow implementer to prevent immediate finalization by setting `data.context.async = true` in the listener, to show a confirmation popup etc

```
 scheduler.on('beforedragcreatefinalize', ({context}) => {
     context.async = true;
     setTimeout(() => {
         // async code don't forget to call finalize
         context.finalize();
     }, 1000);
 })
```

[afterDragCreate](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDragCreate#event-afterDragCreate)
Fires on the owning Gantt at the end of the drag create gesture whether or not a task was scheduled by the gesture.
