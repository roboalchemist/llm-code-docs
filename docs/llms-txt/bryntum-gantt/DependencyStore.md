# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/data/DependencyStore.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/DependencyStore.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/data/DependencyStore.md

# [DependencyStore](https://bryntum.com/docs/gantt/api/Gantt/data/DependencyStore)

A class representing a collection of dependencies between tasks in the [TaskStore](https://bryntum.com/docs/gantt/api/#Gantt/data/TaskStore). Contains a collection of [DependencyModel](https://bryntum.com/docs/gantt/api/#Gantt/model/DependencyModel) records.

```
const dependencyStore = new DependencyStore({
    data : [
        {
            "id"       : 1,
            "fromTask" : 11,
            "toTask"   : 15,
            "lag"      : 2
        },
        {
            "id"       : 2,
            "fromTask" : 12,
            "toTask"   : 15
        }
    ]
})
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDependencyStore](https://bryntum.com/docs/gantt/api/Gantt/data/DependencyStore#property-isDependencyStore)
Identifies an object as an instance of [DependencyStore](https://bryntum.com/docs/gantt/api/#Gantt/data/DependencyStore) class, or subclass thereof.

[isDependencyStore](https://bryntum.com/docs/gantt/api/Gantt/data/DependencyStore#property-isDependencyStore-static)
Identifies an object as an instance of [DependencyStore](https://bryntum.com/docs/gantt/api/#Gantt/data/DependencyStore) class, or subclass thereof.

[loadPriority](https://bryntum.com/docs/gantt/api/Gantt/data/DependencyStore#property-loadPriority)
CrudManager must load stores in the correct order. Lowest first.

[syncPriority](https://bryntum.com/docs/gantt/api/Gantt/data/DependencyStore#property-syncPriority)
CrudManager must sync stores in the correct order. Lowest first.
