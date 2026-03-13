# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/TaskDrag.md

# [TaskDrag](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag)

Allows user to drag and drop tasks within Gantt, to change their start date.

Constraining the drag drop area
-------------------------------

You can constrain how the dragged task is allowed to move by using [getDateConstraints](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#config-getDateConstraints). This method is configured on the Gantt instance and lets you define the date range for the dragged task programmatically.

Drag drop tasks from outside
----------------------------

Dragging unplanned tasks from an external grid is a very popular use case. Please refer to the [Drag from grid demo](https://bryntum.com/docs/gantt/api/../examples/drag-from-grid) and study the [Drag from grid guide](https://bryntum.com/docs/gantt/api/#Gantt/guides/dragdrop/drag_tasks_from_grid.md) to learn more.

Validating a drag drop operation
--------------------------------

It is easy to programmatically decide what is a valid drag drop operation. Use the [validatorFn](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskDrag#config-validatorFn) and return either `true` / `false` (optionally a message to show to the user).

```
features : {
    taskDrag : {
       validatorFn(draggedTaskRecords, newStartDate) {
           const valid = Date.now() >= newStartDate;

           return {
               valid,
               message : valid ? '' : 'Not allow to drag a task into the past'
           };
       }
    }
}
```

If you instead want to do a single validation upon drop, you can listen to [beforeTaskDropFinalize](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskDrag#event-beforeTaskDropFinalize) and set the `valid` flag on the context object provided.

```
const gantt = new Gantt({
    listeners : {
        beforeTaskDropFinalize({ context }) {
            const { taskRecords } = context;
            // Don't allow dropping a task in the past
            context.valid = Date.now() <= eventRecords[0].startDate;
        }
    }
});
```

Preventing drag of certain tasks
--------------------------------

To prevent certain tasks from being dragged, you have two options. You can set [draggable](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-draggable) to `false` in your data, or you can listen for the [beforeTaskDrag](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#event-beforeTaskDrag) event and return `false` to block the drag.

```
new Gantt({
    listeners : {
        beforeTaskDrag({ taskRecord }) {
            // Only allow dragging tasks that has not started
            return taskRecord.percentDone === 0;
        }
    }
})
```

Customizing the drag drop tooltip
---------------------------------

To show custom HTML in the tooltip, please see the [tooltipTemplate](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskDrag#config-tooltipTemplate) config. Example:

```
features: {
    taskDrag: {
        // A minimal start date tooltip
        tooltipTemplate : ({ taskRecord, startDate }) => {
            return DateHelper.format(startDate, 'HH:mm');
        }
    }
}
```

This feature is **enabled** by default

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[validatorFn](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#config-validatorFn)
An empty function by default, but provided so that you can perform custom validation on the item being dragged. This function is called during the drag and drop process and also after the drop is made. Return true if the new position is valid, false to prevent the drag.

[validatorFnThisObj](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#config-validatorFnThisObj)
`this` reference for the validatorFn

[pinSuccessors](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#config-pinSuccessors)
Set to `true` to enable dragging task while pinning dependent tasks. By default, this behavior is activated if you hold CTRL key during drag. Alternatively, you may provide key name to use. Supported values are:

* 'ctrl'
* 'shift'
* 'alt'
* 'meta'

**Note**: Only supported in forward-scheduled project

[dragAllSelectedTasks](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#config-dragAllSelectedTasks)
Set to `true` to drag all selected tasks. Set to `false` to only drag one task at a time

[tooltipTemplate](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#config-tooltipTemplate)
Template used to generate drag tooltip contents.

```
const gantt = new Gantt({
    features : {
        taskDrag : {
            tooltipTemplate({taskRecord, startText}) {
                return `${taskRecord.name}: ${startText}`
            }
        }
    }
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTaskDrag](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#property-isTaskDrag)
Identifies an object as an instance of [TaskDrag](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskDrag) class, or subclass thereof.

[isTaskDrag](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#property-isTaskDrag-static)
Identifies an object as an instance of [TaskDrag](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskDrag) class, or subclass thereof.

[pinSuccessors](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#property-pinSuccessors)
Gets or sets special key to activate successor pinning behavior. Supported values are:

* 'ctrl'
* 'shift'
* 'alt'
* 'meta'

Assign false to disable it.

[dragAllSelectedTasks](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#property-dragAllSelectedTasks)
Set to `true` to drag all selected tasks. Set to `false` to only drag one task at a time

## Functions

Functions are methods available for calling on the class

[getCoordinate](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#function-getCoordinate)
Get correct axis coordinate.

[isValidDrop](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#function-isValidDrop)
Checks if a task can be dropped on the specified location

[updateRecords](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#function-updateRecords)
Update tasks being dragged.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeTaskDrag](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#event-beforeTaskDrag)
Fires on the owning Gantt before task dragging starts. Return false to prevent the action.

[taskDragStart](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#event-taskDragStart)
Fires on the owning Gantt when task dragging starts

[taskDrag](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#event-taskDrag)
Fires on the owning Gantt while a task is being dragged

[beforeTaskDropFinalize](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#event-beforeTaskDropFinalize)
Fires on the owning Gantt to allow implementer to prevent immediate finalization by setting `data.context.async = true` in the listener, to show a confirmation popup etc

```
gantt.on('beforetaskdropfinalize', ({ context }) => {
    context.async = true;
    setTimeout(() => {
        // async code don't forget to call finalize
        context.finalize();
    }, 1000);
})
```

[taskDrop](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#event-taskDrop)
Fires on the owning Gantt after a valid task drop

[afterTaskDrop](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#event-afterTaskDrop)
Fires on the owning Gantt after a task drop, regardless if the drop validity

## Typedefs

Typedefs are type definitions for the class

[ValidationMessage](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskDrag#typedef-ValidationMessage)
