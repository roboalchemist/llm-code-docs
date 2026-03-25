# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/model/Baseline.md

# [Baseline](https://bryntum.com/docs/gantt/api/Gantt/model/Baseline)

This class represents a baseline of a Task.

Records based on this model are initially created when tasks are loaded into the TaskStore. If dates (startDate and endDate) are left out, the task's dates will be used. If dates are `null`, dates will be empty and the baseline bar won't be displayed in the UI.

## Fields

Fields belong to a Model class and define the Model data structure

[task](https://bryntum.com/docs/gantt/api/Gantt/model/Baseline#field-task)
The owning Task of the Baseline

[startDate](https://bryntum.com/docs/gantt/api/Gantt/model/Baseline#field-startDate)
Start date of the baseline in ISO 8601 format.

Note that the field always returns a `Date`.

[endDate](https://bryntum.com/docs/gantt/api/Gantt/model/Baseline#field-endDate)
End date of the baseline in ISO 8601 format.

Note that the field always returns a `Date`.

[cls](https://bryntum.com/docs/gantt/api/Gantt/model/Baseline#field-cls)
An encapsulation of the CSS classes to be added to the rendered baseline element.

Always returns a [DomClassList](https://bryntum.com/docs/gantt/api/#Core/helper/util/DomClassList), but may still be treated as a string. For granular control of adding and removing individual classes, it is recommended to use the [DomClassList](https://bryntum.com/docs/gantt/api/#Core/helper/util/DomClassList) API.

[fullEffort](https://bryntum.com/docs/gantt/api/Gantt/model/Baseline#field-fullEffort)
Calculated field which encapsulates the effort's magnitude and unit. This field will not be persisted, setting it will update the [effort](https://bryntum.com/docs/gantt/api/#Gantt/model/Baseline#field-effort) and [effortUnit](https://bryntum.com/docs/gantt/api/#Gantt/model/Baseline#field-effortUnit) fields.

[effort](https://bryntum.com/docs/gantt/api/Gantt/model/Baseline#field-effort)
The numeric part of the baseline effort (the number of units).

[effortUnit](https://bryntum.com/docs/gantt/api/Gantt/model/Baseline#field-effortUnit)
The unit part of the baseline effort. Valid values are:

* "millisecond" - Milliseconds
* "second" - Seconds
* "minute" - Minutes
* "hour" - Hours
* "day" - Days
* "week" - Weeks
* "month" - Months
* "quarter" - Quarters
* "year"- Years

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isBaseline](https://bryntum.com/docs/gantt/api/Gantt/model/Baseline#property-isBaseline)
Identifies an object as an instance of [Baseline](https://bryntum.com/docs/gantt/api/#Gantt/model/Baseline) class, or subclass thereof.

[isBaseline](https://bryntum.com/docs/gantt/api/Gantt/model/Baseline#property-isBaseline-static)
Identifies an object as an instance of [Baseline](https://bryntum.com/docs/gantt/api/#Gantt/model/Baseline) class, or subclass thereof.

[startVariance](https://bryntum.com/docs/gantt/api/Gantt/model/Baseline#property-startVariance)
Baseline start variance in the task's duration unit.

[endVariance](https://bryntum.com/docs/gantt/api/Gantt/model/Baseline#property-endVariance)
Baseline end variance in the task's duration unit.

[durationVariance](https://bryntum.com/docs/gantt/api/Gantt/model/Baseline#property-durationVariance)
Baseline duration variance in the task's duration unit.

[plannedPercentDone](https://bryntum.com/docs/gantt/api/Gantt/model/Baseline#property-plannedPercentDone)
Planned percent done for this baseline.

## Functions

Functions are methods available for calling on the class

[convertToMilestone](https://bryntum.com/docs/gantt/api/Gantt/model/Baseline#function-convertToMilestone)
Converts this baseline to a milestone (start date will match the end date).

[convertToRegular](https://bryntum.com/docs/gantt/api/Gantt/model/Baseline#function-convertToRegular)
Converts a milestone baseline to a regular baseline with a duration of 1 (keeping current `durationUnit`).
