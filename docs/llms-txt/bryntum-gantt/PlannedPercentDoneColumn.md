# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/column/PlannedPercentDoneColumn.md

# [PlannedPercentDoneColumn](https://bryntum.com/docs/gantt/api/Gantt/column/PlannedPercentDoneColumn)

A column representing the [planned % complete](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-getPlannedPercentDone) of the task.

Please refer to the [getPlannedPercentDone](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-getPlannedPercentDone) method's docs for details.

Note, that if you would like to filter, sort, or group by this column, you need to define the [statusDate](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-statusDate) on the project and not as a config for this column. This is because filtering/sorting/grouping code generally does not have access to the UI.

## Fields

Fields belong to a Model class and define the Model data structure

[statusDate](https://bryntum.com/docs/gantt/api/Gantt/column/PlannedPercentDoneColumn#field-statusDate)
A reference date, to track the progress from. If not provided, the project's [status date](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-statusDate) is used.

Note, that if you would like to filter, sort, or group by this column, you need to define the [statusDate](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#field-statusDate) on the project and not as this config. This is because filtering/sorting/grouping code generally does not have access to the UI.

[baselineVersion](https://bryntum.com/docs/gantt/api/Gantt/column/PlannedPercentDoneColumn#field-baselineVersion)
An index (1-based) of the baseline version to be used for planned percent done calculation.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPlannedPercentDoneColumn](https://bryntum.com/docs/gantt/api/Gantt/column/PlannedPercentDoneColumn#property-isPlannedPercentDoneColumn)
Identifies an object as an instance of [PlannedPercentDoneColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/PlannedPercentDoneColumn) class, or subclass thereof.

[isPlannedPercentDoneColumn](https://bryntum.com/docs/gantt/api/Gantt/column/PlannedPercentDoneColumn#property-isPlannedPercentDoneColumn-static)
Identifies an object as an instance of [PlannedPercentDoneColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/PlannedPercentDoneColumn) class, or subclass thereof.
