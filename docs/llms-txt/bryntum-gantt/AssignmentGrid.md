# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/widget/AssignmentGrid.md

# [AssignmentGrid](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentGrid)

This grid visualizes and lets users edit assignments of an [event](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentGrid#config-projectEvent). Used by the [AssignmentField](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentField). This grid shows one column showing the resource name, and one showing the units assigned. You can add additional columns by providing a [columns](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-columns) array in your grid config.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[resourceColumn](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentGrid#config-resourceColumn)
A [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column) config object for the resource column. You can pass a `renderer` which gives you access to the `resource` record.

[unitsColumn](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentGrid#config-unitsColumn)
A config object for the units column

[projectEvent](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentGrid#config-projectEvent)
Event model to manipulate assignments of, the task should be part of a task store. Either task or [store](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-store) should be given.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAssignmentGrid](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentGrid#property-isAssignmentGrid)
Identifies an object as an instance of [AssignmentGrid](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentGrid) class, or subclass thereof.

[isAssignmentGrid](https://bryntum.com/docs/gantt/api/Gantt/widget/AssignmentGrid#property-isAssignmentGrid-static)
Identifies an object as an instance of [AssignmentGrid](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentGrid) class, or subclass thereof.
