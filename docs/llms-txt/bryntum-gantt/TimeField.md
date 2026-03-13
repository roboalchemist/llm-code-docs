# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/TimeField.md

# [TimeField](https://bryntum.com/docs/gantt/api/Core/widget/TimeField)

The time field widget is a text input field with a time picker drop down. It shows left/right arrows to increase or decrease time by the [step value](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField#config-step).

This field can be used as an [editor](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-editor) for the [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column). It is used as the default editor for the [TimeColumn](https://bryntum.com/docs/gantt/api/#Grid/column/TimeColumn).

Configuring forward / backward step size
----------------------------------------

The [step](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField#config-step) configuration controls how the time value changes when using the forward and backward buttons at the start and end of the field. The step value is also used to configure the appropriate picker:

* For steps in minutes (e.g. '5m'), the minute picker will use this step value
* For steps in hours (e.g. '2h'), the hour picker will use this step value

```
new TimeField({
    label     : 'Time field',
    appendTo  : document.body,
    step      : '5 minutes'  // Controls both field buttons and minute picker
});
```

This widget may be operated using the keyboard. `ArrowDown` opens the time picker, which itself is keyboard navigable. `Shift+ArrowDown` activates the [step](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField#config-step) back trigger. `Shift+ArrowUp` activates the [step](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField#config-step) forwards trigger.

```
let field = new TimeField({
  format: 'HH'
});
```

Salesforce users will not see this form of the TimeField and picker because this uses custom elements which are not supported in Salesforce. Instead, the last released version of the 6.0.0 TimePicker is used. The public API is not changed.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[format](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#config-format)
Format for date displayed in field (see Core.helper.DateHelper#function-format-static for formatting options).

[triggers](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#config-triggers)
Widgets that trigger functionality upon click. Each trigger icon is a [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget) instance which may be hidden, shown and observed and styled just like any other widget.

[min](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#config-min)
Min time value

[max](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#config-max)
Max time value

[step](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#config-step)
Time increment duration value. Defaults to 5 minutes. The value is taken to be a string consisting of the numeric magnitude and the units. The units may be a recognised unit abbreviation of this locale or the full local unit name. For example `"10m"` or `"5min"` or `"2 hours"`

[stepTriggers](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#config-stepTriggers)
Set to `false` to hide the forward and backward time step triggers.

[value](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#config-value)
Value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField#config-format).

When converted to a [Date](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date), the date part is set to January 1st of the year 2020.

[keepDate](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#config-keepDate)
Set to true to not clean up the date part of the passed value. Set to false to reset the date part to January 1st

[partner](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#config-partner)
A reference to a partner DateField which this TimeField should sync its value with. When the DateField's value is changed, this TimeField's value is updated to match. When this TimeField's value is changed, the DateField's value is updated to match.

When a string is passed, this is taken to be the widget's [reference](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-ref) property and the actual DateField is looked up in the same [owner](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-owner) container as this TimeField. If the reference cannot be found there, the string is used as a widget `id`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimeField](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#property-isTimeField)
Identifies an object as an instance of [TimeField](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField) class, or subclass thereof.

[isTimeField](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#property-isTimeField-static)
Identifies an object as an instance of [TimeField](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField) class, or subclass thereof.

[format](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#property-format)
Get/Set format for time displayed in field (see [format](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-format-static) for formatting options).

[triggers](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#property-triggers)
Widgets that trigger functionality upon click. Each trigger icon is a [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget) instance which may be hidden, shown and observed and styled just like any other widget.

[min](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#property-min)
Get/set min value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField#config-format).

[max](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#property-max)
Get/set max value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField#config-format).

[step](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#property-step)
The `step` property may be set in Object form specifying two properties, `magnitude`, a Number, and `unit`, a String.

If a Number is passed, the steps's current unit is used and just the magnitude is changed.

If a String is passed, it is parsed by [parseDuration](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-parseDuration-static), for example `'5m'`, `'5 m'`, `'5 min'`, `'5 minutes'`.

Upon read, the value is always returned in object form containing `magnitude` and `unit`.

[value](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#property-value)
Get/set value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField#config-format).

This value is a [Date](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) object. As such it contains the date part. When set using a string, the date part is set to January 1st of the year 2020.

[keepDate](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#property-keepDate)
Set to true to not clean up the date part of the passed value. Set to false to reset the date part to January 1st

[partner](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#property-partner)
A reference to a partner DateField which this TimeField should sync its value with. When the DateField's value is changed, this TimeField's value is updated to match. When this TimeField's value is changed, the DateField's value is updated to match.

When a string is passed, this is taken to be the widget's [reference](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-ref) property and the actual DateField is looked up in the same [owner](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-owner) container as this TimeField. If the reference cannot be found there, the string is used as a widget `id`.

## Functions

Functions are methods available for calling on the class

[showPicker](https://bryntum.com/docs/gantt/api/Core/widget/TimeField#function-showPicker)
Show picker
