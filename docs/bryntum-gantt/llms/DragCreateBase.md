# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/base/DragCreateBase.md

# [DragCreateBase](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/DragCreateBase)

Base class for EventDragCreate (Scheduler) and TaskDragCreate (Gantt) features. Contains shared code. Not to be used directly.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[showTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/DragCreateBase#config-showTooltip)
true to show a time tooltip when dragging to create a new event

[dragTolerance](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/DragCreateBase#config-dragTolerance)
Number of pixels the drag target must be moved before dragging is considered to have started. Defaults to 2.

[validatorFnThisObj](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/DragCreateBase#config-validatorFnThisObj)
`this` reference for the validatorFn

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDragCreateBase](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/DragCreateBase#property-isDragCreateBase)
Identifies an object as an instance of [DragCreateBase](https://bryntum.com/docs/gantt/api/#Scheduler/feature/base/DragCreateBase) class, or subclass thereof.

[isDragCreateBase](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/DragCreateBase#property-isDragCreateBase-static)
Identifies an object as an instance of [DragCreateBase](https://bryntum.com/docs/gantt/api/#Scheduler/feature/base/DragCreateBase) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[onElementContextMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/DragCreateBase#function-onElementContextMenu)
Prevent right click when drag creating
