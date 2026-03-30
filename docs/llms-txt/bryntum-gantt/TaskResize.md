# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/TaskResize.md

# [TaskResize](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskResize)

Feature that allows resizing a task by dragging its end date. Resizing a task by dragging its start date is not allowed.

This feature is **enabled** by default

This feature updates the event's `endDate` live in order to leverage the rendering pathway to always yield a correct appearance. The changes are done in [batched](https://bryntum.com/docs/gantt/api/#Core/data/Model#function-beginBatch) mode so that changes do not become eligible for data synchronization or propagation until the operation is completed.

Customizing the resize tooltip
------------------------------

To show custom HTML in the tooltip, please see the [tooltipTemplate](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskResize#config-tooltipTemplate) config. Example:

```
taskResize : {
    // A minimal end date tooltip
    tooltipTemplate : ({ record, endDate }) => {
        return DateHelper.format(endDate, 'MMM D');
    }
}
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[pinSuccessors](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskResize#config-pinSuccessors)
Set to `true` to enable resizing task while pinning dependent tasks. By default, this behavior is activated if you hold CTRL key during drag. Alternatively, you may provide key name to use. Supported values are:

* 'ctrl'
* 'shift'
* 'alt'
* 'meta'

**Note**: Only supported in forward-scheduled project

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTaskResize](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskResize#property-isTaskResize)
Identifies an object as an instance of [TaskResize](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskResize) class, or subclass thereof.

[isTaskResize](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskResize#property-isTaskResize-static)
Identifies an object as an instance of [TaskResize](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskResize) class, or subclass thereof.

[pinSuccessors](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskResize#property-pinSuccessors)
Gets or sets special key to activate successor pinning behavior. Supported values are:

* 'ctrl'
* 'shift'
* 'alt'
* 'meta'

Assign false to disable it.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeTaskResize](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskResize#event-beforeTaskResize)
Fires on the owning Gantt before resizing starts. Return `false` to prevent the operation.

[taskResizeStart](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskResize#event-taskResizeStart)
Fires on the owning Gantt when task resizing starts

[taskPartialResize](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskResize#event-taskPartialResize)
Fires on the owning Gantt on each resize move event

[beforeTaskResizeFinalize](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskResize#event-beforeTaskResizeFinalize)
Fires on the owning Gantt to allow implementer to prevent immediate finalization by setting `data.context.async = true` in the listener, to show a confirmation popup etc.

```
 gantt.on('beforeTaskResizeFinalize', ({context}) => {
     context.async = true;
     setTimeout(() => {
         // async code don't forget to call finalize
         context.finalize();
     }, 1000);
 })
```

[taskResizeEnd](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskResize#event-taskResizeEnd)
Fires on the owning Gantt after the resizing gesture has finished.

## Typedefs

Typedefs are type definitions for the class

[TaskResizeData](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskResize#typedef-TaskResizeData)
An object containing data related to task resize.
