# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/widget/DependencyField.md

# [DependencyField](https://bryntum.com/docs/gantt/api/Gantt/widget/DependencyField)

Chooses dependencies, connector sides and lag time for dependencies of a Task.

This field can be used as an editor for a [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column). It is used as the default editor for the [DependencyColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/DependencyColumn).

The contextual task is the `record` property of this field's [owner](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-owner).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[delimiter](https://bryntum.com/docs/gantt/api/Gantt/widget/DependencyField#config-delimiter)
Delimiter between dependency ids in the field

[dependencyStore](https://bryntum.com/docs/gantt/api/Gantt/widget/DependencyField#config-dependencyStore)
The dependency store

[otherSide](https://bryntum.com/docs/gantt/api/Gantt/widget/DependencyField#config-otherSide)
The other task's relationship with this field's contextual task. This will be `'from'` if we are editing predecessors, and `'to'` if we are editing successors.

[ourSide](https://bryntum.com/docs/gantt/api/Gantt/widget/DependencyField#config-ourSide)
This field's contextual task's relationship with the other task. This will be `'to'` if we are editing predecessors, and `'from'` if we are editing successors.

[dependencyIdField](https://bryntum.com/docs/gantt/api/Gantt/widget/DependencyField#config-dependencyIdField)
A task field (id, wbsCode, sequenceNumber etc) that will be used when displaying and editing linked tasks. Defaults to [Gantt#dependencyIdField](https://bryntum.com/docs/gantt/api/#Gantt/view/GanttBase#config-dependencyIdField)

[eventRecord](https://bryntum.com/docs/gantt/api/Gantt/widget/DependencyField#config-eventRecord)
The task whose dependencies are being edited (used to filter out invalid options)

[sorters](https://bryntum.com/docs/gantt/api/Gantt/widget/DependencyField#config-sorters)
The sorters defining how to sort tasks in the drop down list, defaults to sorting by `name` field ascending. See [StoreSort](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreSort) for more information.

[filterable](https://bryntum.com/docs/gantt/api/Gantt/widget/DependencyField#config-filterable)
Set to `false` to hide the filter field

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDependencyField](https://bryntum.com/docs/gantt/api/Gantt/widget/DependencyField#property-isDependencyField)
Identifies an object as an instance of [DependencyField](https://bryntum.com/docs/gantt/api/#Gantt/widget/DependencyField) class, or subclass thereof.

[isDependencyField](https://bryntum.com/docs/gantt/api/Gantt/widget/DependencyField#property-isDependencyField-static)
Identifies an object as an instance of [DependencyField](https://bryntum.com/docs/gantt/api/#Gantt/widget/DependencyField) class, or subclass thereof.

[allowedDependencyTypes](https://bryntum.com/docs/gantt/api/Gantt/widget/DependencyField#property-allowedDependencyTypes)
Returns the allowed dependency types from the dependency store.
