# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/widget/UndoRedo.md

# [UndoRedo](https://bryntum.com/docs/gantt/api/Scheduler/widget/UndoRedo)

A widget which encapsulates undo/redo functionality for the [project](https://bryntum.com/docs/gantt/api/#Scheduler/model/ProjectModel) of a scheduling widget (`Scheduler`, `Gantt` or `Calendar`).

To make use of this, the project must be configured with a [State Tracking Manager](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/ProjectModelMixin#config-stm).

Note that this widget will automatically [enable](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager#function-enable) the `stm` instance, upon the `load` event of the project's crud manager.

If inserted into a scheduling widget (such as into a `tbar`, or `bbar`, or as an item in a context menu), the project of the encapsulating scheduling widget will be used.

If this widget is to be used "standalone" (rendered into the DOM outside of a scheduling widget), this must be configured with a reference to the project, or the scheduling widget which is using the project. This can be done with the [project](https://bryntum.com/docs/gantt/api/#Scheduler/widget/UndoRedo#config-project) and [scheduler](https://bryntum.com/docs/gantt/api/#Scheduler/widget/UndoRedo#config-scheduler) config options correspondingly.

There are three child widgets encapsulated which may be referenced through the [widgetMap](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-widgetMap):

* `undoBtn` - The button which operates the undo operation (CTRL+Z, or CMD+Z in Mac OS)
* `transactionsCombo` - A combobox into which is pushed the list of transactions,
* `redoBtn` - The button which operates the redo operation (CTRL+SHIFT+Z, + CMD+SHIFT+Z in Mac OS)

To disable keyboard shortcuts for undo/redo, set [enableUndoRedoKeys](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-enableUndoRedoKeys) to false.

The transactionsCombo may be configured away if only the buttons are required:

```
{
    type      : 'undoredo',
    items     : {
        transactionsCombo : null
    }
}
```

The example below illustrated how to embed an `undoredo` widget in the top toolbar of a Scheduler.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[scheduler](https://bryntum.com/docs/gantt/api/Scheduler/widget/UndoRedo#config-scheduler)
The Scheduling Widget (or its `id`) whose transaction to track.

This may be a `Scheduler`, a `Gantt` or a `Calendar`.

```
    {
        type      : 'undoredo',
        scheduler : myCalendar
    }
```

[project](https://bryntum.com/docs/gantt/api/Scheduler/widget/UndoRedo#config-project)
The Scheduling [project](https://bryntum.com/docs/gantt/api/#Scheduler/model/ProjectModel)'s whose transaction to track.

```
    {
        type    : 'undoredo',
        project : scheduler.project
    }
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isUndoRedo](https://bryntum.com/docs/gantt/api/Scheduler/widget/UndoRedo#property-isUndoRedo)
Identifies an object as an instance of [UndoRedo](https://bryntum.com/docs/gantt/api/#Scheduler/widget/UndoRedo) class, or subclass thereof.

[isUndoRedo](https://bryntum.com/docs/gantt/api/Scheduler/widget/UndoRedo#property-isUndoRedo-static)
Identifies an object as an instance of [UndoRedo](https://bryntum.com/docs/gantt/api/#Scheduler/widget/UndoRedo) class, or subclass thereof.

[project](https://bryntum.com/docs/gantt/api/Scheduler/widget/UndoRedo#property-project)
Get/set ProjectModel instance, containing the data visualized by the SchedulerPro.
