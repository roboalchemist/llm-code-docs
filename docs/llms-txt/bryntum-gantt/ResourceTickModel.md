# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/model/ResourceTickModel.md

# [ResourceTickModel](https://bryntum.com/docs/gantt/api/Scheduler/model/ResourceTickModel)

This class represents a named resource tick. It is used by the [TickCells](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TickCells) feature.

This class inherits most of its fields from [TimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan). The most important of these fields are the following:

* [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceTickModel#field-startDate) - start date of the tick in the ISO 8601 format
* [endDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceTickModel#field-endDate) - end date of the tick in the ISO 8601 format (not inclusive)
* [duration](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceTickModel#field-duration) - duration, time between start date and end date
* [durationUnit](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceTickModel#field-durationUnit) - unit used to express the duration

It's an indirect subclass of [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model). Please refer to documentation of those classes to become familiar with the base interface of this class. The data source of any field can be customized in the subclass. Please refer to [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) for details.

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

## Fields

Fields belong to a Model class and define the Model data structure

[resourceId](https://bryntum.com/docs/gantt/api/Scheduler/model/ResourceTickModel#field-resourceId)
Id of the resource this tick is associated with

[value](https://bryntum.com/docs/gantt/api/Scheduler/model/ResourceTickModel#field-value)
Value of the resource tick

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceTickModel](https://bryntum.com/docs/gantt/api/Scheduler/model/ResourceTickModel#property-isResourceTickModel)
Identifies an object as an instance of [ResourceTickModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceTickModel) class, or subclass thereof.

[isResourceTickModel](https://bryntum.com/docs/gantt/api/Scheduler/model/ResourceTickModel#property-isResourceTickModel-static)
Identifies an object as an instance of [ResourceTickModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceTickModel) class, or subclass thereof.
