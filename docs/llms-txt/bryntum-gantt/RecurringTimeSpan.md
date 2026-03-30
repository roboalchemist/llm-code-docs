# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/model/mixin/RecurringTimeSpan.md

# [RecurringTimeSpan](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan)

This mixin class provides recurrence related fields and methods to a [TimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan) model. This class is used to support recurring events (and time ranges) in the Scheduler and Calendar components.

Data structure
--------------

The mixin introduces two types of timespans: the **recurring timespan** and its **occurrences**. A **recurring timespan** is a timespan having a [recurrenceRule](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#field-recurrenceRule) specified and its **occurrences** are "fake" dynamically generated timespans. You can also provide [exceptionDates](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#field-exceptionDates) to the data to exclude certain dates. See sample data below,

```
{
    id: 7,
    startDate: '2021-10-12T14:00:00',
    endDate: '2021-10-12T15:00:00',
    name: 'Lunch',
    resourceId: 'hotel',
    recurrenceRule: 'FREQ=DAILY;COUNT=5',
    exceptionDates: ['2021-10-14']
}
```

Useful API methods
------------------

There are few methods allowing to distinguish a recurring event and an occurrence: [isRecurring](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#property-isRecurring), [isOccurrence](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#property-isOccurrence) and [recurringTimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#property-recurringTimeSpan) (returns the event this record is an occurrence of).

The [recurrence rule](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#field-recurrenceRule) defined for the event is parsed and represented with [RecurrenceModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/RecurrenceModel) class (can be changed by setting [recurrenceModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#property-recurrenceModel) property) instance. See: [recurrence](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#property-recurrence) property.

To query the ocurrences for a specific timespan, use the [getOccurrencesForDateRange](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#function-getOccurrencesForDateRange) method:

```
// Get all occurrences between Feb 1-10
timespan.getOccurrencesForDateRange(new Date(2024, 1, 1), new Date(2024, 1, 10));
```

## Fields

Fields belong to a Model class and define the Model data structure

[recurrenceRule](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#field-recurrenceRule)
The timespan recurrence rule. A string in [RFC-5545](https://bryntum.com/docs/gantt/api/https://tools.ietf.org/html/rfc5545#section-3.3.10) described format ("RRULE" expression).

[exceptionDates](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#field-exceptionDates)
A string (either a single date or multiple dates separated by comma) or an array of strings containing the timespan exception dates. The dates that must be skipped when generating occurrences for a repeating timespan. This is used to modify only individual occurrences of the timespan so the further regenerations won't create another copy of this occurrence again.

```
{
    id: 7,
    startDate: '2021-10-12T14:00:00',
    endDate: '2021-10-12T15:00:00',
    name: 'Lunch',
    resourceId: 'hotel',
    recurrenceRule: 'FREQ=DAILY;COUNT=5',
    exceptionDates: ['2021-10-14']
}
```

Use [addExceptionDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#function-addExceptionDate) method to add an individual entry to the dates array:

```
// Break the link between the occurrence and its base.
// This also adds the occurrence date as an exception date
// so that the base timespan knows that this date should be skipped when regenerating its occurrences.
occurrence.recurringTimeSpan = null;

// now the occurrence is an individual record that can be changed & persisted freely
occurrence.setStartEndDate(new Date(2018, 6, 2), new Date(2018, 6, 3));
```

**Note:** The dates in this field get automatically removed when the event changes its [start date](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-startDate).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRecurringTimeSpan](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#property-isRecurringTimeSpan)
Identifies an object as an instance of [RecurringTimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan) class, or subclass thereof.

[isRecurringTimeSpan](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#property-isRecurringTimeSpan-static)
Identifies an object as an instance of [RecurringTimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan) class, or subclass thereof.

[supportsRecurring](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#property-supportsRecurring)
Returns `true` if this timespan supports recurring.

[recurrenceModel](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#property-recurrenceModel)
Name of the class representing the recurrence model, defaults to [RecurrenceModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/RecurrenceModel)

[recurrence](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#property-recurrence)
The recurrence model used for the timespan.

[isRecurring](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#property-isRecurring)
Indicates if the timespan is recurring.

[isOccurrence](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#property-isOccurrence)
Indicates if the timespan is an occurrence of another recurring timespan.

[recurringTimeSpan](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#property-recurringTimeSpan)
The "main" timespan this model is an occurrence of. For non-occurrences returns `null`.

[occurrences](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#property-occurrences)
Array of this recurring timespan's cached occurrences. **Not including the owning recurring event**.

Empty if the timespan is not recurring.

**Note that this is an internal accessor and is cleared whenever changes are made to the owning recurring event**.

[occurrenceMap](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#property-occurrenceMap)
A Map, keyed by each date an occurrence intersects, of occurrences of this event.

[occurrenceDate](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#property-occurrenceDate)
The original {@lScheduler.model.TimeSpan#field-startDate startDate} of this event before any modifications took place. Used by [removeOccurrence](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#function-removeOccurrence) and [detachFromRecurringEvent](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#function-detachFromRecurringEvent)

[occurrenceIndex](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#property-occurrenceIndex)
If this event is an [occurrence](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#property-isOccurrence) of a recurring event, then this property yields its zero-based occurrence index in the sequence.

[newExceptionDate](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#property-newExceptionDate)
The setter used by Model#inSet when [addExceptionDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#function-addExceptionDate) is called. Adding an exception must trigger change processing in a recurring event, so it must be changed through a [set](https://bryntum.com/docs/gantt/api/#Core/data/Model#function-set) call. Also, the change must be batchable with other changes.

## Functions

Functions are methods available for calling on the class

[remove](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#function-remove)
Override of [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model)'s method. If an [isOccurrence](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#property-isOccurrence) is passed, it is detached from its parent recurring event. If it still has a recurrence then the recurring event is changed to stop at the occurrence date. If it has no recurrence an exception is added at the occurrence date.

[setRecurrence](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#function-setRecurrence)
Sets a recurrence for the timespan with a given frequency, interval, and end.

[getOccurrencesForDateRange](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#function-getOccurrencesForDateRange)
Returns the occurrences of this event over the specified time range. If the first occurrence is in the time range `*this*` record is included in that position.

[removeOccurrence](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#function-removeOccurrence)
Removes an occurrence from this recurring timespan's cached occurrences.

[removeOccurrencesFrom](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#function-removeOccurrencesFrom)
Removes all cached occurrences on or after the passed date from this recurring timespan's cached occurrences.

[removeOccurrences](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#function-removeOccurrences)
Removes this recurring timespan's cached occurrences.

[onRecurrenceChanged](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#function-onRecurrenceChanged)
The method is triggered when the timespan recurrence settings get changed. It updates the [recurrenceRule](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#field-recurrenceRule) field in this case.

[buildOccurrence](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#function-buildOccurrence)
Builds an occurrence of this recurring event by cloning the timespan data. The method is used internally by the **RecurringTimeSpans** mixin. Override it if you need to customize the generated occurrences.

If the date requested is the start date of the event sequence, `this` record is returned. All runs of recurring events begin with the base record.

[detachFromRecurringEvent](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#function-detachFromRecurringEvent)
Detaches an occurrence from its owning recurring event so that it can be added to the eventStore either as an exception, or as the start of a new recurring sequence.

[addExceptionDate](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#function-addExceptionDate)
Adds an exception date that should be skipped when generating occurrences for the timespan. The method adds an entry to the array kept in [exceptionDates](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan#field-exceptionDates) field.

[hasException](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/RecurringTimeSpan#function-hasException)
Does this recurring event have an exception on the passed date.
