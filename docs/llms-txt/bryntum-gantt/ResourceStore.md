# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/data/ResourceStore.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/ResourceStore.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/data/ResourceStore.md

# [ResourceStore](https://bryntum.com/docs/gantt/api/Gantt/data/ResourceStore)

A class representing the collection of the resources - [ResourceModel](https://bryntum.com/docs/gantt/api/#Gantt/model/ResourceModel) records.

```
const resourceStore = new ResourceStore({
    data : [
        { "id" : 1, "name" : "John Doe" },
        { "id" : 2, "name" : "Jane Doe" }
    ]
})
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceStore](https://bryntum.com/docs/gantt/api/Gantt/data/ResourceStore#property-isResourceStore)
Identifies an object as an instance of [ResourceStore](https://bryntum.com/docs/gantt/api/#Gantt/data/ResourceStore) class, or subclass thereof.

[isResourceStore](https://bryntum.com/docs/gantt/api/Gantt/data/ResourceStore#property-isResourceStore-static)
Identifies an object as an instance of [ResourceStore](https://bryntum.com/docs/gantt/api/#Gantt/data/ResourceStore) class, or subclass thereof.

[loadPriority](https://bryntum.com/docs/gantt/api/Gantt/data/ResourceStore#property-loadPriority)
CrudManager must load stores in the correct order. Lowest first.

[syncPriority](https://bryntum.com/docs/gantt/api/Gantt/data/ResourceStore#property-syncPriority)
CrudManager must sync stores in the correct order. Lowest first.
