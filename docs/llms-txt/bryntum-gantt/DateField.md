# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/DateField.md

# [DateField](https://bryntum.com/docs/gantt/api/Core/widget/DateField)

A Date field widget consisting of a date input field + a [date picker](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker).

It can be configured to allow user typing dates, or to only allow selection from the date picker (see [editable](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-editable)). It can also validate that the date is within a specified range (see [min](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-min) -> [max](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-max)). It also optionally show step triggers to increment or decrement the date (see [step](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-step) & [stepTriggers](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-stepTriggers)):

This field can be used as an [editor](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-editor) for a grid [column](https://bryntum.com/docs/gantt/api/#Grid/column/Column). It is used as the default editor for the [DateColumn](https://bryntum.com/docs/gantt/api/#Grid/column/DateColumn) class.

```
// minimal DateField config with date format specified
const dateField = new DateField({
  format: 'YYMMDD'
});
```

Accessibility
-------------

This widget can be operated using the keyboard. When the field is focused, `ArrowDown` opens the date picker, which itself is keyboard navigable. `Shift+ArrowDown` activates the [step](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-step) back trigger. `Shift+ArrowUp` activates the [step](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-step) forwards trigger.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[format](https://bryntum.com/docs/gantt/api/Core/widget/DateField#config-format)
Format for date displayed in field. Defaults to using long date format, as defined by current locale (`L`)

[strictParsing](https://bryntum.com/docs/gantt/api/Core/widget/DateField#config-strictParsing)
A flag which indicates whether the date parsing should be strict - meaning if the date is missing a year/month/day part - parsing fails.

Turned off by default, meaning default values are substituted for missing parts.

[keepTime](https://bryntum.com/docs/gantt/api/Core/widget/DateField#config-keepTime)
A flag which indicates what time should be used for selected date. `false` by default which means time is reset to midnight.

Possible options are:

* `false` to reset time to midnight
* `true` to keep original time value
* `'17:00'` a string which is parsed automatically
* `new Date(2020, 0, 1, 17)` a date object to copy time from
* `'entered'` to keep time value entered by user (in case [format](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-format) includes time info)

[pickerFormat](https://bryntum.com/docs/gantt/api/Core/widget/DateField#config-pickerFormat)
Format for date in the [picker](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-picker). Uses localized format per default

[validateDateOnly](https://bryntum.com/docs/gantt/api/Core/widget/DateField#config-validateDateOnly)
Set to `true` to first clear time of the field's value before comparing it to the max value

[triggers](https://bryntum.com/docs/gantt/api/Core/widget/DateField#config-triggers)
Widgets that trigger functionality upon click. Each trigger icon is a [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget) instance which may be hidden, shown and observed and styled just like any other widget.

[min](https://bryntum.com/docs/gantt/api/Core/widget/DateField#config-min)
Min value

[max](https://bryntum.com/docs/gantt/api/Core/widget/DateField#config-max)
Max value

[step](https://bryntum.com/docs/gantt/api/Core/widget/DateField#config-step)
Time increment duration value. If specified, `forward` and `back` triggers are displayed. The value is taken to be a string consisting of the numeric magnitude and the units. The units may be a recognised unit abbreviation of this locale or the full local unit name. For example `'1d'` or `'1w'` or `'1 week'`. This may be specified as an object containing two properties: `magnitude`, a Number, and `unit`, a String

[stepTriggers](https://bryntum.com/docs/gantt/api/Core/widget/DateField#config-stepTriggers)
Set to `false` to hide the forward and backward date step triggers. These triggers are only shown when [step](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-step) is set.

[weekStartDay](https://bryntum.com/docs/gantt/api/Core/widget/DateField#config-weekStartDay)
The week start day in the [picker](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-picker), 0 meaning Sunday, 6 meaning Saturday. Uses localized value per default.

[picker](https://bryntum.com/docs/gantt/api/Core/widget/DateField#config-picker)
A config object used to configure the [datePicker](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker).

```
dateField = new DateField({
    picker : {
        tbar : {
            items : {
                // Remove the prev year and next year buttons by setting them to null.
                // Move the prev month button to just before the next month button by increasing its weight
                prevYear  : null,
                nextYear  : null,
                prevMonth : {
                    weight : 390
                }
            }
        }
    }
```

[value](https://bryntum.com/docs/gantt/api/Core/widget/DateField#config-value)
Value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-format)

[partner](https://bryntum.com/docs/gantt/api/Core/widget/DateField#config-partner)
A reference to a partner TimeField which this DateField should sync its value with. When the TimeField's value is changed, this DateField's value is updated to match. When this DateField's value is changed, the TimeField's value is updated to match.

When a string is passed, this is taken to be the widget's [reference](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-ref) property and the actual TimeField is looked up in the same [owner](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-owner) container as this TimeField. If the reference cannot be found there, the string is used as a widget `id`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDateField](https://bryntum.com/docs/gantt/api/Core/widget/DateField#property-isDateField)
Identifies an object as an instance of [DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField) class, or subclass thereof.

[isDateField](https://bryntum.com/docs/gantt/api/Core/widget/DateField#property-isDateField-static)
Identifies an object as an instance of [DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField) class, or subclass thereof.

[format](https://bryntum.com/docs/gantt/api/Core/widget/DateField#property-format)
Get / set format for date displayed in field (see [format](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-format-static) for formatting options).

[triggers](https://bryntum.com/docs/gantt/api/Core/widget/DateField#property-triggers)
Widgets that trigger functionality upon click. Each trigger icon is a [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget) instance which may be hidden, shown and observed and styled just like any other widget.

[min](https://bryntum.com/docs/gantt/api/Core/widget/DateField#property-min)
Get/set min value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-format).

[max](https://bryntum.com/docs/gantt/api/Core/widget/DateField#property-max)
Get/set max value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-format).

[step](https://bryntum.com/docs/gantt/api/Core/widget/DateField#property-step)
The `step` property may be set in object form specifying two properties, `magnitude`, a Number, and `unit`, a String.

If a Number is passed, the step's current unit is used (or `day` if no current step set) and just the magnitude is changed.

If a String is passed, it is parsed by [parseDuration](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-parseDuration-static), for example `'1d'`, `'1 d'`, `'1 day'`, or `'1 day'`.

Upon read, the value is always returned in object form containing `magnitude` and `unit`.

[value](https://bryntum.com/docs/gantt/api/Core/widget/DateField#property-value)
Get/set value, which can be set as a Date or a string but always returns a Date. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-format)

[partner](https://bryntum.com/docs/gantt/api/Core/widget/DateField#property-partner)
A reference to a partner TimeField which this DateField should sync its value with. When the TimeField's value is changed, this DateField's value is updated to match. When this DateField's value is changed, the TimeField's value is updated to match.

When a string is passed, this is taken to be the widget's [reference](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-ref) property and the actual TimeField is looked up in the same [owner](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-owner) container as this TimeField. If the reference cannot be found there, the string is used as a widget `id`.

## Functions

Functions are methods available for calling on the class

[changePicker](https://bryntum.com/docs/gantt/api/Core/widget/DateField#function-changePicker)
Creates default picker widget

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[change](https://bryntum.com/docs/gantt/api/Core/widget/DateField#event-change)
Fired when this field's value changes.
