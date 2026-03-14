# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/util/recurrence/DailyRecurrenceIterator.md

# [DailyRecurrenceIterator](https://bryntum.com/docs/gantt/api/Scheduler/data/util/recurrence/DailyRecurrenceIterator)

A class which provides iteration to call a function for dates specified by a [RecurrenceModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/RecurrenceModel) over a specified date range.

## Functions

Functions are methods available for calling on the class

[forEachDate](https://bryntum.com/docs/gantt/api/Scheduler/data/util/recurrence/DailyRecurrenceIterator#function-forEachDate-static)
Iterates over the passed date range, calling the passed callback on each date on which starts a recurring event which matches the passed recurrence rule and overlaps the start and end dates and is not an [exceptionDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#field-exceptionDates) in the recurring event.
