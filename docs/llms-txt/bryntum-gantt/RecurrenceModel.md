# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/model/RecurrenceModel.md

# [RecurrenceModel](https://bryntum.com/docs/gantt/api/Scheduler/model/RecurrenceModel)

This class encapsulates the recurrence information of a [RecurringTimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan). The [rule](https://bryntum.com/docs/gantt/api/#Scheduler/model/RecurrenceModel#property-rule) describes how the timespan will repeat, and is based on [RFC-5545](https://bryntum.com/docs/gantt/api/https://tools.ietf.org/html/rfc5545#section-3.3.10).

Examples:

```
const recurrenceModel = new RecurrenceModel();
// every weekday
recurrenceModel.rule = 'FREQ=WEEKLY;INTERVAL=1;BYDAY=MO,TU,WE,TH,FR';

// every other week
recurrenceModel.rule = 'FREQ=WEEKLY;INTERVAL=2';

// every 5th day, until May 31st, 2025
recurrenceModel.rule = 'FREQ=DAILY;INTERVAL=5;UNTIL=20250531T000000';
```

It is a subclass of [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) class. Please refer to the documentation for that class to become familiar with the base interface of this class.

The data source for the fields in this class can be customized by subclassing this class.

## Fields

Fields belong to a Model class and define the Model data structure

[frequency](https://bryntum.com/docs/gantt/api/Scheduler/model/RecurrenceModel#field-frequency)
Field defines the recurrence frequency. Supported values are: `DAILY`, `WEEKLY`, `MONTHLY`, `YEARLY`.

[interval](https://bryntum.com/docs/gantt/api/Scheduler/model/RecurrenceModel#field-interval)
Field defines how often the recurrence repeats. For example, if the recurrence is weekly its interval is 2, then the timespan repeats every two weeks.

[endDate](https://bryntum.com/docs/gantt/api/Scheduler/model/RecurrenceModel#field-endDate)
End date of the recurrence. Specifies when the recurrence ends. The value is optional, the recurrence can as well be stopped using [count](https://bryntum.com/docs/gantt/api/#Scheduler/model/RecurrenceModel#field-count) field value.

[count](https://bryntum.com/docs/gantt/api/Scheduler/model/RecurrenceModel#field-count)
Specifies the number of occurrences after which the recurrence ends. The value includes the associated timespan itself so values less than 2 make no sense. The field is optional, the recurrence as well can be stopped using [endDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/RecurrenceModel#field-endDate) field value.

[days](https://bryntum.com/docs/gantt/api/Scheduler/model/RecurrenceModel#field-days)
Specifies days of the week on which the timespan should occur. An array of string values `SU`, `MO`, `TU`, `WE`, `TH`, `FR`, `SA` corresponding to Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday days of the week. Each value can also be preceded by a positive (+n) or negative (-n) integer. If present, this indicates the nth occurrence of a specific day within the monthly or yearly recurrence.

**Not applicable** for daily [frequency](https://bryntum.com/docs/gantt/api/#Scheduler/model/RecurrenceModel#field-frequency).

[monthDays](https://bryntum.com/docs/gantt/api/Scheduler/model/RecurrenceModel#field-monthDays)
Specifies days of the month on which the timespan should occur. An array of integer values (-31..-1 - +1..+31, negative values mean counting backwards from the month end). **Applicable only** for monthly and yearly [frequency](https://bryntum.com/docs/gantt/api/#Scheduler/model/RecurrenceModel#field-frequency).

[months](https://bryntum.com/docs/gantt/api/Scheduler/model/RecurrenceModel#field-months)
Specifies months of the year on which the timespan should occur. An array of integer values (1 - 12). **Applicable only** for yearly [frequency](https://bryntum.com/docs/gantt/api/#Scheduler/model/RecurrenceModel#field-frequency).

[positions](https://bryntum.com/docs/gantt/api/Scheduler/model/RecurrenceModel#field-positions)
The positions to include in the recurrence. The values operate on a set of recurrence instances **in one interval** of the recurrence rule. An array of integer values (valid values are 1 to 366 or -366 to -1, negative values mean counting backwards from the end of the built list of occurrences). **Not applicable** for daily [frequency](https://bryntum.com/docs/gantt/api/#Scheduler/model/RecurrenceModel#field-frequency).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRecurrenceModel](https://bryntum.com/docs/gantt/api/Scheduler/model/RecurrenceModel#property-isRecurrenceModel)
Identifies an object as an instance of [RecurrenceModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/RecurrenceModel) class, or subclass thereof.

[isRecurrenceModel](https://bryntum.com/docs/gantt/api/Scheduler/model/RecurrenceModel#property-isRecurrenceModel-static)
Identifies an object as an instance of [RecurrenceModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/RecurrenceModel) class, or subclass thereof.

[timeSpan](https://bryntum.com/docs/gantt/api/Scheduler/model/RecurrenceModel#property-timeSpan)
The timespan this recurrence is associated with.

[rule](https://bryntum.com/docs/gantt/api/Scheduler/model/RecurrenceModel#property-rule)
The recurrence rule. A string in [RFC-5545](https://bryntum.com/docs/gantt/api/https://tools.ietf.org/html/rfc5545#section-3.3.10) described format ("RRULE" expression).

## Functions

Functions are methods available for calling on the class

[forEachOccurrence](https://bryntum.com/docs/gantt/api/Scheduler/model/RecurrenceModel#function-forEachOccurrence)
Iterate occurrences for the owning timespan across the specified date range. This method can be called even if the timespan is not yet a member of a store, however, the occurrences returned will not be cached across subsequent calls to this method.

[sanitize](https://bryntum.com/docs/gantt/api/Scheduler/model/RecurrenceModel#function-sanitize)
Cleans up fields that do not make sense for the current [frequency](https://bryntum.com/docs/gantt/api/#Scheduler/model/RecurrenceModel#field-frequency) value.
