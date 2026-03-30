# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/model/EventModel.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/model/EventModel.md

# [EventModel](https://bryntum.com/docs/gantt/api/Scheduler/model/EventModel)

This class represent a single event in your schedule, usually added to a [EventStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/EventStore).

It is a subclass of the [TimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan), which is in turn a subclass of [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model). Please refer to the documentation of that class to become familiar with the base interface of the event.

Recurrence
----------

This class mixes [RecurringTimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan) which provides recurrence support. Using the [recurrenceRule](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#field-recurrenceRule) and [exceptionDates](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#field-exceptionDates) you can express just about any recurrence pattern. Below is the data for a repeating event happening every weekday at 10am.

```
{
  "id"             : 1,
  "name"           : "Daily standup",
  "startDate"      : "2024-01-03 10:00",
  "duration"       : 1,
  "durationUnit"   : "hour",
  "recurrenceRule" : "FREQ=WEEKLY;INTERVAL=1;BYDAY=MO,TU,WE,TH,FR"
}
```

Async date calculations
-----------------------

A record created from an [EventModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) is normally part of an [EventStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/EventStore), which in turn is part of a project. When dates or the duration of an event is changed, the project performs async calculations to normalize the other fields. For example if [duration](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel#field-duration) is changed, it will calculate [endDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel#field-endDate).

As a result of this being an async operation, the values of other fields are not guaranteed to be up to date immediately after a change. To ensure data is up to date, await the calculations to finish.

For example, [endDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel#field-endDate) is not up to date after this operation:

```
eventRecord.duration = 5;
// endDate not yet calculated
```

But if calculations are awaited it is up to date:

```
eventRecord.duration = 5;
await eventRecord.project.commitAsync();
// endDate is calculated
```

As an alternative, you can also use `setAsync()` to trigger calculations directly after the change:

```
await eventRecord.setAsync({ duration : 5});
// endDate is calculated
```

Subclassing the Event model class
---------------------------------

The Event model has a few predefined fields as seen below. If you want to add new fields or change the options for the existing fields, you can do that by subclassing this class (see example below).

```
class MyEvent extends EventModel {

    static get fields() {
        return [
           // Add new field
           { name: 'myField', type : 'number', defaultValue : 0 }
        ];
    },

    myCheckMethod() {
        return this.myField > 0
    },

    ...
});
```

If you in your data want to use other names for the [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel#field-startDate), [endDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel#field-endDate), [resourceId](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel#field-resourceId) and name fields you can configure them as seen below:

```
class MyEvent extends EventModel {

    static get fields() {
        return [
           { name: 'startDate', dataSource : 'taskStart' },
           { name: 'endDate', dataSource : 'taskEnd', format: 'YYYY-MM-DD' },
           { name: 'resourceId', dataSource : 'userId' },
           { name: 'name', dataSource : 'taskTitle' },
        ];
    },
    ...
});
```

Please refer to [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) for additional details.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventModel](https://bryntum.com/docs/gantt/api/Scheduler/model/EventModel#property-isEventModel)
Identifies an object as an instance of [EventModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) class, or subclass thereof.

[isEventModel](https://bryntum.com/docs/gantt/api/Scheduler/model/EventModel#property-isEventModel-static)
Identifies an object as an instance of [EventModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel) class, or subclass thereof.
