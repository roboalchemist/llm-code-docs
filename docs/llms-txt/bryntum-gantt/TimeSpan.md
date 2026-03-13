# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/model/TimeSpan.md

# [TimeSpan](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan)

This class represent a simple date range. It is being used in various subclasses and plugins which operate on date ranges.

It's a subclass of [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model). Please refer to documentation of those classes to become familiar with the base interface of this class.

A TimeSpan has the following fields:

* [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-startDate) - start date of the task in the ISO 8601 format
* [endDate](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-endDate) - end date of the task in the ISO 8601 format (not inclusive)
* [duration](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-duration) - duration, time between start date and end date
* [durationUnit](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-durationUnit) - unit used to express the duration
* [name](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-name) - an optional name of the range
* [cls](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-cls) - an optional CSS class to be associated with the range.

The data source of any field can be customized in the subclass. Please refer to [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) for details. To specify another date format:

```
class MyTimeSpan extends TimeSpan {
  static get fields() {
     { name: 'startDate', type: 'date', dateFormat: 'DD/MM/YY' }
  }
}
```

## Fields

Fields belong to a Model class and define the Model data structure

[startDate](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#field-startDate)
The start date of a time span (or Event / Task).

Uses [DateHelper.defaultFormat](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-defaultFormat-static) to convert a supplied string to a Date. To specify another format, either change that setting or subclass TimeSpan and change the dateFormat for this field.

Note that the field always returns a `Date`.

[endDate](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#field-endDate)
The end date of a time span (or Event / Task).

Uses [DateHelper.defaultFormat](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-defaultFormat-static) to convert a supplied string to a Date. To specify another format, either change that setting or subclass TimeSpan and change the dateFormat for this field.

Note that the field always returns a `Date`.

[duration](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#field-duration)
The numeric part of the timespan's duration (the number of units).

[durationUnit](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#field-durationUnit)
The unit part of the TimeSpan duration, defaults to "d" (days). Valid values are:

* "millisecond" - Milliseconds
* "second" - Seconds
* "minute" - Minutes
* "hour" - Hours
* "day" - Days
* "week" - Weeks
* "month" - Months
* "quarter" - Quarters
* "year"- Years

This field is readonly after creation, to change durationUnit use #setDuration().

[fullDuration](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#field-fullDuration)
Calculated field which encapsulates the duration's magnitude and unit. This field will not be persisted, setting it will update the [duration](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-duration) and [durationUnit](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-durationUnit) fields.

[cls](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#field-cls)
An encapsulation of the CSS classes to add to the rendered time span element.

Always returns a [DomClassList](https://bryntum.com/docs/gantt/api/#Core/helper/util/DomClassList), but may still be treated as a string. For granular control of adding and removing individual classes, it is recommended to use the [DomClassList](https://bryntum.com/docs/gantt/api/#Core/helper/util/DomClassList) API.

[iconCls](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#field-iconCls)
CSS class specifying an icon to apply to the rendered time span element. **Note**: In case event is a milestone, using `iconCls` with dependency feature might slightly decrease performance because feature will refer to the DOM to get exact size of the element.

[style](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#field-style)
A CSS style string (applied to `style.cssText`) or object (applied to `style`)

```
record.style = 'color: red;font-weight: 800';
```

[name](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#field-name)
The name of the time span (or Event / Task)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimeSpan](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#property-isTimeSpan)
Identifies an object as an instance of [TimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan) class, or subclass thereof.

[isTimeSpan](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#property-isTimeSpan-static)
Identifies an object as an instance of [TimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan) class, or subclass thereof.

[eventStore](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#property-eventStore)
Returns the event store this event is part of, if any.

[dates](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#property-dates)
Returns an array of dates in this range. If the range starts/ends not at the beginning of day, the whole day will be included.

[durationMS](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#property-durationMS)
Returns the duration of this Event in milliseconds.

[rawDurationMS](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#property-rawDurationMS)
Returns the event raw duration in milliseconds. Calculated as a simple distance between the event start and end dates in milliseconds. And thus this value (in Scheduler Pro and Gantt) doesn't take into account non-working time nor the project conversion rates.

[isMilestone](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#property-isMilestone)
Returns true if record is a milestone.

[isScheduled](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#property-isScheduled)
Checks if the range record has both start and end dates set and start <= end

[wbsCode](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#property-wbsCode)
Returns the WBS code of this model (e.g '2.1.3'). Only relevant when part of a tree store, as in the Gantt chart.

## Functions

Functions are methods available for calling on the class

[setDuration](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#function-setDuration)
Sets duration and durationUnit in one go. Only allowed way to change durationUnit, the durationUnit field is readonly after creation

[getDurationInUnit](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#function-getDurationInUnit)
Returns duration of the event in given unit. This is a wrapper for [getDurationInUnit](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-getDurationInUnit-static)

[setStartDate](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#function-setStartDate)
Sets the range start date

[setEndDate](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#function-setEndDate)
Sets the range end date

[setStartEndDate](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#function-setStartEndDate)
Sets the event start and end dates

[forEachDate](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#function-forEachDate)
Iterates over the [dates](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#property-dates)

[shift](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#function-shift)
Shift the dates for the date range by the passed amount and unit

[split](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#function-split)
Splits this event into two pieces at the desired position.

[exportToICS](https://bryntum.com/docs/gantt/api/Scheduler/model/TimeSpan#function-exportToICS)
Triggers a download of this time span in ICS format (for import in Outlook etc.)

```
timeSpan.downloadAsICS({
     LOCATION : timeSpan.location
 });
```
