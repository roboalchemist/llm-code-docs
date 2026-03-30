# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/DurationField.md

# [DurationField](https://bryntum.com/docs/gantt/api/Core/widget/DurationField)

A specialized field allowing a user to also specify duration unit when editing the duration value.

This field can be used as an [editor](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-editor) for the [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column). It is used as the default editor for the `DurationColumn`.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[value](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#config-value)
The `value` may be set either in object form specifying two properties, a numerical `magnitude` and a string `unit`:

```
new DurationField({
   value : {
     magnitude : 1,
     unit      : 'day'
   }
});
```

Or as a string, that is parsed in accordance with current locale rules. The string is taken to be the numeric magnitude, followed by whitespace, then an abbreviation, or name of the unit:

```
new DurationField({
   value : '1 day'
});
```

If a Number is passed, the field's current unit is used and just the magnitude is changed.

When the passed value includes a unit, that unit will override the [unit](https://bryntum.com/docs/gantt/api/#Core/widget/DurationField#config-unit) configured on the field.

Upon read, the value is always a [Duration](https://bryntum.com/docs/gantt/api/#Core/data/Duration) object containing `magnitude` and `unit`.

[useAbbreviation](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#config-useAbbreviation)
When set to `true` the field will use short names of unit durations (as returned by [getShortNameOfUnit](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-getShortNameOfUnit-static)) when creating the input field's display value.

[allowNegative](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#config-allowNegative)
Set to `true` to allow negative duration

[decimalPrecision](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#config-decimalPrecision)
The number of decimal places to allow. Defaults to no constraint.

[triggers](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#config-triggers)
Widgets that trigger functionality upon click. Each trigger icon is a [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget) instance which may be hidden, shown and observed and styled just like any other widget.

[min](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#config-min)
Minimum duration value (e.g. 1d)

[max](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#config-max)
Max duration value (e.g. 10d)

[allowedUnits](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#config-allowedUnits)
Comma-separated list of units to allow in this field, e.g. "day,hour,year". Leave blank to allow all valid units (the default)

[step](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#config-step)
Step size for spin button clicks. The `step` property may be set in object form specifying two properties, `magnitude`, a Number, and `unit`, a String.

If a Number is passed, the step's current unit is used (or `day` if no current step set) and just the magnitude is changed.

If a String is passed, it is parsed by [parseDuration](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-parseDuration-static), for example `'1d'`, `'1 d'`, `'1 day'`, or `'1 day'`.

[unit](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#config-unit)
The duration unit to use with the current magnitude value.

Note that setting a [value](https://bryntum.com/docs/gantt/api/#Core/widget/DurationField#config-value) that includes a unit will override the configured unit.

[magnitude](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#config-magnitude)
The duration magnitude to use with the current unit value. Can be either an integer or a float value. Both "," and "." are valid decimal separators.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDurationField](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#property-isDurationField)
Identifies an object as an instance of [DurationField](https://bryntum.com/docs/gantt/api/#Core/widget/DurationField) class, or subclass thereof.

[isDurationField](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#property-isDurationField-static)
Identifies an object as an instance of [DurationField](https://bryntum.com/docs/gantt/api/#Core/widget/DurationField) class, or subclass thereof.

[value](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#property-value)
The `value` may be set either in object form specifying two properties, a numerical `magnitude` and a string `unit`:

```
new DurationField({
   value : {
     magnitude : 1,
     unit      : 'day'
   }
});
```

Or as a string, that is parsed in accordance with current locale rules. The string is taken to be the numeric magnitude, followed by whitespace, then an abbreviation, or name of the unit:

```
new DurationField({
   value : '1 day'
});
```

If a Number is passed, the field's current unit is used and just the magnitude is changed.

When the passed value includes a unit, that unit will override the [unit](https://bryntum.com/docs/gantt/api/#Core/widget/DurationField#config-unit) configured on the field.

Upon read, the value is always a [Duration](https://bryntum.com/docs/gantt/api/#Core/data/Duration) object containing `magnitude` and `unit`.

[triggers](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#property-triggers)
Widgets that trigger functionality upon click. Each trigger icon is a [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget) instance which may be hidden, shown and observed and styled just like any other widget.

[min](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#property-min)
Get/set the min value (e.g. 1d)

[max](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#property-max)
Get/set the max value

[allowedUnits](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#property-allowedUnits)
Get/set the allowed units, e.g. "day,hour,year".

[unit](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#property-unit)
The duration unit to use with the current magnitude value.

Note that setting a [value](https://bryntum.com/docs/gantt/api/#Core/widget/DurationField#config-value) that includes a unit will override the configured unit.

[magnitude](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#property-magnitude)
The duration magnitude to use with the current unit value. Can be either an integer or a float value. Both "," and "." are valid decimal separators.

[milliseconds](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#property-milliseconds)
The `milliseconds` property is a read-only property which returns the number of milliseconds in this field's value

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[change](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#event-change)
Fired when this field's value changes.

[action](https://bryntum.com/docs/gantt/api/Core/widget/DurationField#event-action)
User performed the default action (typed into this field or hit the triggers).
