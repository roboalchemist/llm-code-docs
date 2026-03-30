# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/model/TimePhasedProjectModel.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/model/TimePhasedProjectModel.md

# [TimePhasedProjectModel](https://bryntum.com/docs/gantt/api/Gantt/model/TimePhasedProjectModel)

The class extends the default [ProjectModel](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel) with time-phased assignments support. It changes the default related models to [TimePhasedTaskModel](https://bryntum.com/docs/gantt/api/#Gantt/model/TimePhasedTaskModel) for tasks and [TimePhasedAssignmentModel](https://bryntum.com/docs/gantt/api/#Gantt/model/TimePhasedAssignmentModel) for assignments.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[taskModelClass](https://bryntum.com/docs/gantt/api/Gantt/model/TimePhasedProjectModel#config-taskModelClass)
The constructor of the event model class, to be used in the project. Will be set as the [modelClass](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-modelClass) property of the [eventStore](https://bryntum.com/docs/gantt/api/#Gantt/model/TimePhasedProjectModel#property-eventStore)

[assignmentModelClass](https://bryntum.com/docs/gantt/api/Gantt/model/TimePhasedProjectModel#config-assignmentModelClass)
The constructor of the assignment model class, to be used in the project. Will be set as the [modelClass](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-modelClass) property of the [assignmentStore](https://bryntum.com/docs/gantt/api/#Gantt/model/TimePhasedProjectModel#property-assignmentStore)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimePhasedProjectModel](https://bryntum.com/docs/gantt/api/Gantt/model/TimePhasedProjectModel#property-isTimePhasedProjectModel)
Identifies an object as an instance of [TimePhasedProjectModel](https://bryntum.com/docs/gantt/api/#Gantt/model/TimePhasedProjectModel) class, or subclass thereof.

[isTimePhasedProjectModel](https://bryntum.com/docs/gantt/api/Gantt/model/TimePhasedProjectModel#property-isTimePhasedProjectModel-static)
Identifies an object as an instance of [TimePhasedProjectModel](https://bryntum.com/docs/gantt/api/#Gantt/model/TimePhasedProjectModel) class, or subclass thereof.
