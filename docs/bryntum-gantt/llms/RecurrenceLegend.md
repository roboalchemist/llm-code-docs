# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/util/recurrence/RecurrenceLegend.md

# [RecurrenceLegend](https://bryntum.com/docs/gantt/api/Scheduler/data/util/recurrence/RecurrenceLegend)

A static class allowing to get a human readable description of the provided recurrence.

```
const event = new EventModel({
     startDate : new Date(2018, 6, 3),
     endDate   : new Date(2018, 6, 4)
});
const recurrence = new RecurrenceModel({
     frequency : 'WEEKLY',
     days : ['MO', 'TU', 'WE']
});
event.recurrence = recurrence;
// "Weekly on Mon, Tue and Wed"
RecurrenceLegend.getLegend(recurrence);
```

## Functions

Functions are methods available for calling on the class

[getLegend](https://bryntum.com/docs/gantt/api/Scheduler/data/util/recurrence/RecurrenceLegend#function-getLegend-static)
Returns the provided recurrence description. The recurrence might be assigned to a timespan model, in this case the timespan start date should be provided in the second argument.
