# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/ResourceTickStore.md

# [ResourceTickStore](https://bryntum.com/docs/gantt/api/Scheduler/data/ResourceTickStore)

A class representing a collection of resource ticks. Contains a collection of [ResourceTickModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceTickModel) records. The class is used by the [TickCells](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TickCells) feature.

```
const store = new ResourceTickStore({
    data : [{        {
        id             : 1,
        startDate      : '2019-01-01T11:00',
        value          : 2,
           resourceId     : 1,
           durationUnit   : 'day',
           duration       : 1
    }]
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceTickStore](https://bryntum.com/docs/gantt/api/Scheduler/data/ResourceTickStore#property-isResourceTickStore)
Identifies an object as an instance of [ResourceTickStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/ResourceTickStore) class, or subclass thereof.

[isResourceTickStore](https://bryntum.com/docs/gantt/api/Scheduler/data/ResourceTickStore#property-isResourceTickStore-static)
Identifies an object as an instance of [ResourceTickStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/ResourceTickStore) class, or subclass thereof.

[loadPriority](https://bryntum.com/docs/gantt/api/Scheduler/data/ResourceTickStore#property-loadPriority)
CrudManager must load stores in the correct order. Lowest first.

[syncPriority](https://bryntum.com/docs/gantt/api/Scheduler/data/ResourceTickStore#property-syncPriority)
CrudManager must sync stores in the correct order. Lowest first.
