# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/CellEdit.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/CellEdit.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/CellEdit.md

# [CellEdit](https://bryntum.com/docs/gantt/api/Gantt/feature/CellEdit)

Extends the [CellEdit](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit) to encapsulate Gantt functionality. This feature is enabled by **default**

Editing can be started by a user by double-clicking an editable cell in the gantt's data grid, or it can be started programmatically by calling [startEditing](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit#function-startEditing) and providing it with correct cell context.

See [doAddNewAtEnd](https://bryntum.com/docs/gantt/api/#Gantt/feature/CellEdit#function-doAddNewAtEnd).

Instant update
--------------

If [instantUpdate](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-instantUpdate) on the column is set to `true`, record will be updated instantly as value in the editor is changed. In combination with [autoSync](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#config-autoSync) it could result in excessive requests to the backend.

Instant update is enabled for these columns by default:

* [DurationColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/DurationColumn)
* [StartDateColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/StartDateColumn)
* [EndDateColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/EndDateColumn)
* [ConstraintDateColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/ConstraintDateColumn)
* [DeadlineDateColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/DeadlineDateColumn)
* [EarlyStartDateColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/EarlyStartDateColumn)
* [EarlyEndDateColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/EarlyEndDateColumn)
* [LateStartDateColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/LateStartDateColumn)
* [LateEndDateColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/LateEndDateColumn)

To disable instant update on the column set config to false:

```
new Gantt({
    columns: [
        {
            type: 'startdate',
            instantUpdate: false
        }
    ]
})
```

This feature is **enabled** by default.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCellEdit](https://bryntum.com/docs/gantt/api/Gantt/feature/CellEdit#property-isCellEdit)
Identifies an object as an instance of [CellEdit](https://bryntum.com/docs/gantt/api/#Gantt/feature/CellEdit) class, or subclass thereof.

[isCellEdit](https://bryntum.com/docs/gantt/api/Gantt/feature/CellEdit#property-isCellEdit-static)
Identifies an object as an instance of [CellEdit](https://bryntum.com/docs/gantt/api/#Gantt/feature/CellEdit) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[doAddNewAtEnd](https://bryntum.com/docs/gantt/api/Gantt/feature/CellEdit#function-doAddNewAtEnd)
Adds a new, empty record at the end of the TaskStore with the initial data specified by the [addNewAtEnd](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit#config-addNewAtEnd) setting.
