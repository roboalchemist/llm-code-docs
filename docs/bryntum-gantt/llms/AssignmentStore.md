# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/data/AssignmentStore.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/AssignmentStore.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/data/AssignmentStore.md

# [AssignmentStore](https://bryntum.com/docs/gantt/api/Gantt/data/AssignmentStore)

A class representing a collection of assignments between tasks in the [TaskStore](https://bryntum.com/docs/gantt/api/#Gantt/data/TaskStore) and resources in the [ResourceStore](https://bryntum.com/docs/gantt/api/#Gantt/data/ResourceStore).

```
const assignmentStore = new AssignmentStore({
    data : [
        { "id" : 1, "event" : 11,  "resource" : 1 },
        { "id" : 2, "event" : 12,  "resource" : 1 },
    ]
})
```

Contains a collection of the [AssignmentModel](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel) records.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAssignmentStore](https://bryntum.com/docs/gantt/api/Gantt/data/AssignmentStore#property-isAssignmentStore)
Identifies an object as an instance of [AssignmentStore](https://bryntum.com/docs/gantt/api/#Gantt/data/AssignmentStore) class, or subclass thereof.

[isAssignmentStore](https://bryntum.com/docs/gantt/api/Gantt/data/AssignmentStore#property-isAssignmentStore-static)
Identifies an object as an instance of [AssignmentStore](https://bryntum.com/docs/gantt/api/#Gantt/data/AssignmentStore) class, or subclass thereof.

[loadPriority](https://bryntum.com/docs/gantt/api/Gantt/data/AssignmentStore#property-loadPriority)
CrudManager must load stores in the correct order. Lowest first.

[syncPriority](https://bryntum.com/docs/gantt/api/Gantt/data/AssignmentStore#property-syncPriority)
CrudManager must sync stores in the correct order. Lowest first.

## Functions

Functions are methods available for calling on the class

[getAssignmentsForEvent](https://bryntum.com/docs/gantt/api/Gantt/data/AssignmentStore#function-getAssignmentsForEvent)
Returns all assignments for a given task.
