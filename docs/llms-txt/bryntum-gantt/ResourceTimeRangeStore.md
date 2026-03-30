# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/ResourceTimeRangeStore.md

# [ResourceTimeRangeStore](https://bryntum.com/docs/gantt/api/Scheduler/data/ResourceTimeRangeStore)

A class representing a collection of resource time ranges. Contains a collection of [ResourceTimeRangeModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceTimeRangeModel) records. The class is used by the [ResourceTimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ResourceTimeRanges) feature.

Recurring ranges support
------------------------

This class supports recurrence:

```
const store = new ResourceTimeRangeStore({
    data : [{        {
        id             : 1,
        resourceId     : 'r1',
        startDate      : '2019-01-01T11:00',
        endDate        : '2019-01-01T13:00',
        name           : 'Coffee break',
        // this time range should repeat every day
        recurrenceRule : 'FREQ=DAILY'
    }]
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[resourceStore](https://bryntum.com/docs/gantt/api/Scheduler/data/ResourceTimeRangeStore#config-resourceStore)
This store should be linked to a ResourceStore to link the time ranges to resources

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceTimeRangeStore](https://bryntum.com/docs/gantt/api/Scheduler/data/ResourceTimeRangeStore#property-isResourceTimeRangeStore)
Identifies an object as an instance of [ResourceTimeRangeStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/ResourceTimeRangeStore) class, or subclass thereof.

[isResourceTimeRangeStore](https://bryntum.com/docs/gantt/api/Scheduler/data/ResourceTimeRangeStore#property-isResourceTimeRangeStore-static)
Identifies an object as an instance of [ResourceTimeRangeStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/ResourceTimeRangeStore) class, or subclass thereof.

[loadPriority](https://bryntum.com/docs/gantt/api/Scheduler/data/ResourceTimeRangeStore#property-loadPriority)
CrudManager must load stores in the correct order. Lowest first.

[syncPriority](https://bryntum.com/docs/gantt/api/Scheduler/data/ResourceTimeRangeStore#property-syncPriority)
CrudManager must sync stores in the correct order. Lowest first.

## Functions

Functions are methods available for calling on the class

[getRanges](https://bryntum.com/docs/gantt/api/Scheduler/data/ResourceTimeRangeStore#function-getRanges)
Get resource time ranges intersecting the specified date range for a resource.

The result is sorted by `startDate`.
