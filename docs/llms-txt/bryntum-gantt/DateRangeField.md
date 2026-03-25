# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/DateRangeField.md

# [DateRangeField](https://bryntum.com/docs/gantt/api/Core/widget/DateRangeField)

A widget to edit a start/end date pair. The two `Date`s are stored in the [value](https://bryntum.com/docs/gantt/api/#Core/widget/DateRangeField#config-value) property.

By default, the picker displays below the fields and edits the value "live":

The [confirmable](https://bryntum.com/docs/gantt/api/#Core/widget/DateRangeField#config-confirmable) config instructs the picker to display on top of the field with OK and Cancel buttons:

Cells in the month calendars presented in the picker can be customized with a [cellRenderer](https://bryntum.com/docs/gantt/api/#Core/widget/MultiDatePicker#config-cellRenderer):

Click on the calendars in the picker, or typing arrow keys will adjust the date range based on which of the individual [date fields](https://bryntum.com/docs/gantt/api/#Core/widget/DateField) has the input focus.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[confirmable](https://bryntum.com/docs/gantt/api/Core/widget/DateRangeField#config-confirmable)
Enables OK/Cancel button bar to accept date range changes. A value of `true` shows the OK and Cancel buttons.

See [confirmable](https://bryntum.com/docs/gantt/api/#Core/widget/DateRangePicker#config-confirmable)

[keepTime](https://bryntum.com/docs/gantt/api/Core/widget/DateRangeField#config-keepTime)
A flag which indicates what time should be used for selected date. `false` by default which means time is reset to midnight.

Possible options are:

* `false` to reset time to midnight
* `true` to keep original time value
* `'17:00'` a string which is parsed automatically
* `new Date(2020, 0, 1, 17)` a date object to copy time from
* `'entered'` to keep time value entered by user (in case [format](https://bryntum.com/docs/gantt/api/#Core/widget/DateRangeField#config-format) includes time info)

[max](https://bryntum.com/docs/gantt/api/Core/widget/DateRangeField#config-max)
Max value

[min](https://bryntum.com/docs/gantt/api/Core/widget/DateRangeField#config-min)
Min value

[picker](https://bryntum.com/docs/gantt/api/Core/widget/DateRangeField#config-picker)
A config object used to configure the [datePicker](https://bryntum.com/docs/gantt/api/#Core/widget/DateRangePicker).

```
dateField = new DateRangeField({
     picker    : {
         multiSelect : true
     }
 });
```

[pickerCls](https://bryntum.com/docs/gantt/api/Core/widget/DateRangeField#config-pickerCls)
An optional extra CSS class to add to the picker container element.

[pickTime](https://bryntum.com/docs/gantt/api/Core/widget/DateRangeField#config-pickTime)
Set to `true` to include time fields to allow the user to pick the time of day. When this config is set, `keepTime` is no longer used.

[weekStartDay](https://bryntum.com/docs/gantt/api/Core/widget/DateRangeField#config-weekStartDay)
The week start day in the [picker](https://bryntum.com/docs/gantt/api/#Core/widget/DateRangeField#config-picker), 0 meaning Sunday, 6 meaning Saturday. Uses localized value per default.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDateRangeField](https://bryntum.com/docs/gantt/api/Core/widget/DateRangeField#property-isDateRangeField)
Identifies an object as an instance of [DateRangeField](https://bryntum.com/docs/gantt/api/#Core/widget/DateRangeField) class, or subclass thereof.

[isDateRangeField](https://bryntum.com/docs/gantt/api/Core/widget/DateRangeField#property-isDateRangeField-static)
Identifies an object as an instance of [DateRangeField](https://bryntum.com/docs/gantt/api/#Core/widget/DateRangeField) class, or subclass thereof.

[confirmable](https://bryntum.com/docs/gantt/api/Core/widget/DateRangeField#property-confirmable)
Enables OK/Cancel button bar to accept date range changes. A value of `true` shows the OK and Cancel buttons.

See [confirmable](https://bryntum.com/docs/gantt/api/#Core/widget/DateRangePicker#config-confirmable)

[max](https://bryntum.com/docs/gantt/api/Core/widget/DateRangeField#property-max)
Get/set max value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/DateRangeField#config-format).

[min](https://bryntum.com/docs/gantt/api/Core/widget/DateRangeField#property-min)
Get/set min value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/DateRangeField#config-format).

[pickerCls](https://bryntum.com/docs/gantt/api/Core/widget/DateRangeField#property-pickerCls)
An optional extra CSS class to add to the picker container element.
