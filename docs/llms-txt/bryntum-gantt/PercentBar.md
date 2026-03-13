# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/PercentBar.md

# [PercentBar](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/PercentBar)

This feature visualizes the [percentDone](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/mixin/PercentDoneMixin#field-percentDone) field as a progress bar on the event elements. Each progress bar also optionally has a drag handle which users can drag can change the value.

You can customize data source for the feature with [valueField](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/PercentBar#config-valueField) and [displayField](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/PercentBar#config-displayField) configs.

Restricting resizing for certain tasks
--------------------------------------

You can prevent certain tasks from having their percent done value changed by overriding the [isEditable](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#function-isEditable) method on your EventModel or TaskModel.

```
class MyTaskModel extends TaskModel {
    isEditable(field) {
        // Add any condition here, `this` refers to the a task instance
        return this.field !== 'percentDone' && super.isEditable(field);
    }
};

gantt = new Gantt({
    project : {
        taskModelClass : MyTaskModel
    }
});
```

This feature is **enabled** by default in Gantt, but **off** by default in Scheduler Pro.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[allowResize](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/PercentBar#config-allowResize)
`true` to allow drag drop resizing to set the % done

[showPercentage](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/PercentBar#config-showPercentage)
`true` to show a small % done label within the event while drag changing its value

[instantUpdate](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/PercentBar#config-instantUpdate)
By default, the underlying task record is updated live as the user drags the handle. Set to `false` to only update the record upon drop.

[valueField](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/PercentBar#config-valueField)
Field name to use as the data source

[displayField](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/PercentBar#config-displayField)
Field name to use to display the value

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPercentBar](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/PercentBar#property-isPercentBar)
Identifies an object as an instance of [PercentBar](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/PercentBar) class, or subclass thereof.

[isPercentBar](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/PercentBar#property-isPercentBar-static)
Identifies an object as an instance of [PercentBar](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/PercentBar) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[onInternalPaint](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/PercentBar#function-onInternalPaint)
Called when scheduler is painted. Sets up drag and drop and hover tooltip.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[percentBarDragStart](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/PercentBar#event-percentBarDragStart)
Fired on the owning Scheduler or Gantt widget when percent bar dragging starts

[percentBarDrag](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/PercentBar#event-percentBarDrag)
Fired on the owning Scheduler or Gantt widget when dragging the percent bar

[percentBarDrop](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/PercentBar#event-percentBarDrop)
Fired on the owning Scheduler or Gantt widget when dropping the percent bar

[percentBarDragAbort](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/PercentBar#event-percentBarDragAbort)
Fired on the owning Scheduler or Gantt widget if a percent bar drag-drop operation is aborted
