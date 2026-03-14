# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/TimeRangeStore.md

# [TimeRangeStore](https://bryntum.com/docs/gantt/api/Scheduler/data/TimeRangeStore)

A class representing a collection of time ranges. Contains a collection of [TimeRangeModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeRangeModel) records. The class is used by the [TimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeRanges) feature.

Recurring ranges support
------------------------

This class supports recurrence:

```
const store = new TimeRangeStore({
    data : [{        {
        id             : 1,
        startDate      : '2019-01-01T11:00',
        endDate        : '2019-01-01T13:00',
        name           : 'Coffee break',
        // this time range should repeat every day
        recurrenceRule : 'FREQ=DAILY'
    }]
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimeRangeStore](https://bryntum.com/docs/gantt/api/Scheduler/data/TimeRangeStore#property-isTimeRangeStore)
Identifies an object as an instance of [TimeRangeStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/TimeRangeStore) class, or subclass thereof.

[isTimeRangeStore](https://bryntum.com/docs/gantt/api/Scheduler/data/TimeRangeStore#property-isTimeRangeStore-static)
Identifies an object as an instance of [TimeRangeStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/TimeRangeStore) class, or subclass thereof.

[loadPriority](https://bryntum.com/docs/gantt/api/Scheduler/data/TimeRangeStore#property-loadPriority)
CrudManager must load stores in the correct order. Lowest first.

[syncPriority](https://bryntum.com/docs/gantt/api/Scheduler/data/TimeRangeStore#property-syncPriority)
CrudManager must sync stores in the correct order. Lowest first.
