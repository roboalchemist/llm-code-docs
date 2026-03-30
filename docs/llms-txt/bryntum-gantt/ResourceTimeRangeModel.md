# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/model/ResourceTimeRangeModel.md

# [ResourceTimeRangeModel](https://bryntum.com/docs/gantt/api/Scheduler/model/ResourceTimeRangeModel)

This class represent a single resource time range in your schedule. To style the rendered elements, use [cls](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-cls) or [timeRangeColor](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceTimeRangeModel#field-timeRangeColor) field. The class is used by the [ResourceTimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ResourceTimeRanges) feature.

Recurring ranges support
------------------------

You can also make ranges recurring by adding a [recurrenceRule](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceTimeRangeModel#field-recurrenceRule) to the range data.

```

// Make new store that supports time ranges recurrence
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

## Fields

Fields belong to a Model class and define the Model data structure

[resourceId](https://bryntum.com/docs/gantt/api/Scheduler/model/ResourceTimeRangeModel#field-resourceId)
Id of the resource this time range is associated with

[timeRangeColor](https://bryntum.com/docs/gantt/api/Scheduler/model/ResourceTimeRangeModel#field-timeRangeColor)
Controls this time range's primary color, defaults to using current themes default time range color.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceTimeRangeModel](https://bryntum.com/docs/gantt/api/Scheduler/model/ResourceTimeRangeModel#property-isResourceTimeRangeModel)
Identifies an object as an instance of [ResourceTimeRangeModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceTimeRangeModel) class, or subclass thereof.

[isResourceTimeRangeModel](https://bryntum.com/docs/gantt/api/Scheduler/model/ResourceTimeRangeModel#property-isResourceTimeRangeModel-static)
Identifies an object as an instance of [ResourceTimeRangeModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceTimeRangeModel) class, or subclass thereof.

[resource](https://bryntum.com/docs/gantt/api/Scheduler/model/ResourceTimeRangeModel#property-resource)
The associated resource, retrieved using a relation to a ResourceStore determined by the value assigned to `resourceId`. The relation also lets you access all time ranges on a resource through [timeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel#property-timeRanges)\`.
