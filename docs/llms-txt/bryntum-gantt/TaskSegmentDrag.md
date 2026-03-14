# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/TaskSegmentDrag.md

# [TaskSegmentDrag](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentDrag)

Allows user to drag and drop task segments, to change their start date.

This feature is **enabled** by default

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTaskSegmentDrag](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentDrag#property-isTaskSegmentDrag)
Identifies an object as an instance of [TaskSegmentDrag](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskSegmentDrag) class, or subclass thereof.

[isTaskSegmentDrag](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentDrag#property-isTaskSegmentDrag-static)
Identifies an object as an instance of [TaskSegmentDrag](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskSegmentDrag) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[updateRecords](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentDrag#function-updateRecords)
Update tasks being dragged.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeTaskSegmentDrag](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentDrag#event-beforeTaskSegmentDrag)
Fires on the owning Gantt before segment dragging starts. Return `false` to prevent the action.

[taskSegmentDragStart](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentDrag#event-taskSegmentDragStart)
Fires on the owning Gantt when segment dragging starts

[taskSegmentDrag](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentDrag#event-taskSegmentDrag)
Fires on the owning Gantt while a segment is being dragged

[beforeTaskSegmentDropFinalize](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentDrag#event-beforeTaskSegmentDropFinalize)
Fires on the owning Gantt to allow implementer to prevent immediate finalization by setting `data.context.async = true` in the listener, to show a confirmation popup etc

```
scheduler.on('beforetasksegmentdropfinalize', ({ context }) => {
    context.async = true;
    setTimeout(() => {
        // async code don't forget to call finalize
        context.finalize();
    }, 1000);
})
```

[taskSegmentDrop](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentDrag#event-taskSegmentDrop)
Fires on the owning Gantt after a valid task drop

[afterTaskSegmentDrop](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskSegmentDrag#event-afterTaskSegmentDrop)
Fires on the owning Gantt after a task drop, regardless if the drop validity
