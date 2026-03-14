# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/column/DependencyColumn.md

# [DependencyColumn](https://bryntum.com/docs/gantt/api/Gantt/column/DependencyColumn)

A column which displays the dependencies which either link to the contextual task from other preceding tasks, or dependencies which link the contextual task to successor tasks.

Default editor is a [DependencyField](https://bryntum.com/docs/gantt/api/#Gantt/widget/DependencyField).

The [field](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-field) MUST be either `predecessors` or `successors` in order for this column to know what kind of dependency it is showing.

By default predecessors and successors have a task ID as a value. But it's configurable and any field may be used to display there (as example: wbsCode or sequenceNumber) using [dependencyIdField](https://bryntum.com/docs/gantt/api/#Gantt/column/DependencyColumn#config-dependencyIdField)

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[delimiter](https://bryntum.com/docs/gantt/api/Gantt/column/DependencyColumn#config-delimiter)
Delimiter used for displayed value and editor

[dependencyIdField](https://bryntum.com/docs/gantt/api/Gantt/column/DependencyColumn#config-dependencyIdField)
A task field (id, wbsCode, sequenceNumber etc) that will be used when displaying and editing linked tasks. Defaults to [dependencyIdField](https://bryntum.com/docs/gantt/api/#Gantt/view/GanttBase#config-dependencyIdField)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDependencyColumn](https://bryntum.com/docs/gantt/api/Gantt/column/DependencyColumn#property-isDependencyColumn)
Identifies an object as an instance of [DependencyColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/DependencyColumn) class, or subclass thereof.

[isDependencyColumn](https://bryntum.com/docs/gantt/api/Gantt/column/DependencyColumn#property-isDependencyColumn-static)
Identifies an object as an instance of [DependencyColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/DependencyColumn) class, or subclass thereof.

[delimiter](https://bryntum.com/docs/gantt/api/Gantt/column/DependencyColumn#property-delimiter)
Delimiter used for displayed value and editor

[dependencyIdField](https://bryntum.com/docs/gantt/api/Gantt/column/DependencyColumn#property-dependencyIdField)
A task field (id, wbsCode, sequenceNumber etc) that will be used when displaying and editing linked tasks. Defaults to [dependencyIdField](https://bryntum.com/docs/gantt/api/#Gantt/view/GanttBase#config-dependencyIdField)
