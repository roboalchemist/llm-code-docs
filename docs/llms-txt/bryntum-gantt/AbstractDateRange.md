# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/mixin/AbstractDateRange.md

# [AbstractDateRange](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange)

A mixin to manage a start and end [DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField) pair. This mixin is not intended to be used directly but rather by [DateRangeField](https://bryntum.com/docs/gantt/api/#Core/widget/DateRangeField) and [DateRangePicker](https://bryntum.com/docs/gantt/api/#Core/widget/DateRangePicker).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[dateFieldDefaults](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#config-dateFieldDefaults)
The default configuration for [fieldStartDate](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/AbstractDateRange#config-fieldStartDate) and [fieldEndDate](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/AbstractDateRange#config-fieldEndDate).

[fieldEndDate](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#config-fieldEndDate)
The field for the end date.

[fieldStartDate](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#config-fieldStartDate)
The field for the start date.

[dateStepTriggers](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#config-dateStepTriggers)
Specifies which date fields ([fieldStartDate](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/AbstractDateRange#config-fieldStartDate) or [fieldEndDate](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/AbstractDateRange#config-fieldEndDate)) should display their forward/backward date step triggers. See [stepTriggers](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-stepTriggers).

[format](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#config-format)
Format for date displayed in the [fieldStartDate](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/AbstractDateRange#config-fieldStartDate) and [fieldEndDate](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/AbstractDateRange#config-fieldEndDate).

[pickingStartDate](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#config-pickingStartDate)
This config is used to track when the focus is in the `fieldStartDate` widget. It is `true` in this case, and `false` otherwise.

[validateDateOnly](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#config-validateDateOnly)
Set to `true` to first clear time of the field's value before comparing it to the min/max value

[value](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#config-value)
Value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/AbstractDateRange#config-format)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAbstractDateRange](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#property-isAbstractDateRange)
Identifies an object as an instance of [AbstractDateRange](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/AbstractDateRange) class, or subclass thereof.

[isAbstractDateRange](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#property-isAbstractDateRange-static)
Identifies an object as an instance of [AbstractDateRange](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/AbstractDateRange) class, or subclass thereof.

[altFormats](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#property-altFormats)
One or more format for parsing date values that don't match [format](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/AbstractDateRange#config-format).

[fieldEndDate](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#property-fieldEndDate)
The field for the end date.

[fieldStartDate](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#property-fieldStartDate)
The field for the start date.

[format](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#property-format)
Get / set format for date displayed in field (see [format](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-format-static) for formatting options).

[pickingStartDate](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#property-pickingStartDate)
This config is used to track when the focus is in the `fieldStartDate` widget. It is `true` in this case, and `false` otherwise.

[value](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#property-value)
Value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/AbstractDateRange#config-format)

## Functions

Functions are methods available for calling on the class

[adjustByKey](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#function-adjustByKey)
Adjusts the date range using the provided keyboard `event` based on the focused date field. If `fieldStartDate` is focused, the start date is adjusted. If `fieldEndDate` is focused, the end date is adjusted. If neither field is focused, the date range is not adjusted.

[checkMinMax](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#function-checkMinMax)
Checks the given `Date` or array of `Date`s to see if any are out of the allow min/max range. Returns 0 if all dates are in range, -1 if a date is below the minimum, or 1 if a date is above the maximum.

[checkValid](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#function-checkValid)
Checks the given `Date` or array of `Date`s to see if any are out of the allow min/max range. Returns `true` if all dates are in range, or `false` otherwise.

[defaultDate](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#function-defaultDate)
Returns a date in the range of `minDate and` maxDate`. This is called when a field's current value is` null\` and a default value is needed.

[syncValue](https://bryntum.com/docs/gantt/api/Core/widget/mixin/AbstractDateRange#function-syncValue)
Synchronizes the widget's state to a new `value`.
