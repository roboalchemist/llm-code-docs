# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/view/mixin/GanttRegions.md

# [GanttRegions](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttRegions)

Functions to get regions (bounding boxes) for gantt, tasks etc.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGanttRegions](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttRegions#property-isGanttRegions)
Identifies an object as an instance of [GanttRegions](https://bryntum.com/docs/gantt/api/#Gantt/view/mixin/GanttRegions) class, or subclass thereof.

[isGanttRegions](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttRegions#property-isGanttRegions-static)
Identifies an object as an instance of [GanttRegions](https://bryntum.com/docs/gantt/api/#Gantt/view/mixin/GanttRegions) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[getScheduleRegion](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttRegions#function-getScheduleRegion)
Gets the region represented by the timeline and optionally only for a single task. Returns `null` if passed a task that is filtered out or not part of the task store.

[getTaskBox](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttRegions#function-getTaskBox)
Get the region for a specified task
