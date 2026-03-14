# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/view/mixin/GanttDom.md

# [GanttDom](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttDom)

Mixin with TaskModel <-> HTMLElement mapping functions

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGanttDom](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttDom#property-isGanttDom)
Identifies an object as an instance of [GanttDom](https://bryntum.com/docs/gantt/api/#Gantt/view/mixin/GanttDom) class, or subclass thereof.

[isGanttDom](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttDom#property-isGanttDom-static)
Identifies an object as an instance of [GanttDom](https://bryntum.com/docs/gantt/api/#Gantt/view/mixin/GanttDom) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[resolveTaskRecord](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttDom#function-resolveTaskRecord)
Returns the task record for a DOM element

[resolveRowRecord](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttDom#function-resolveRowRecord)
Product agnostic method which yields the [TaskModel](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel) record which underpins the row which encapsulates the passed element. The element can be a grid cell, or an event element, and the result will be a [TaskModel](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel)

[onElementKeyDown](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttDom#function-onElementKeyDown)
Relays keydown events as taskKeyDown if we have a selected task(s).

[onElementKeyUp](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttDom#function-onElementKeyUp)
Relays keyup events as taskKeyUp if we have a selected task(s).

[getElementFromTaskRecord](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttDom#function-getElementFromTaskRecord)
Returns the HTMLElement representing a task record.

[getEventRenderId](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttDom#function-getEventRenderId)
Generates the element `id` for a task element. This is used when recycling an event div which has been moved from one resource to another. The event is assigned its new render id _before_ being returned to the free pool, so that when the render engine requests a div from the free pool, the same div will be returned and it will smoothly transition to its new position.

[getEventData](https://bryntum.com/docs/gantt/api/Gantt/view/mixin/GanttDom#function-getEventData)
In Gantt, the task is the row, so it's valid to resolve a mouse event on a task to the TimeAxisColumn's cell.

This method find the cell location of the passed event. It returns an object describing the cell.
