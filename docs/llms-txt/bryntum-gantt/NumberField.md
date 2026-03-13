# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/NumberField.md

# [NumberField](https://bryntum.com/docs/gantt/api/Core/widget/NumberField)

Number field widget. Similar to native `<input type="number">`, but implemented as `<input type="text">` to support formatting.

This field can be used as an [editor](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-editor) for the [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column). It is used as the default editor for the [NumberColumn](https://bryntum.com/docs/gantt/api/#Grid/column/NumberColumn), [PercentColumn](https://bryntum.com/docs/gantt/api/#Grid/column/PercentColumn), [AggregateColumn](https://bryntum.com/docs/gantt/api/#Grid/column/AggregateColumn).

```
const number = new NumberField({
    min   : 1,
    max   : 5,
    value : 3
});
```

Provide a [NumberFormat](https://bryntum.com/docs/gantt/api/#Core/helper/util/NumberFormat) config as [format](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField#config-format) to be able to show currency. For example:

```
new NumberField({
  format : {
     style    : 'currency',
     currency : 'USD'
  }
});
```

Provide a pattern as [format](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField#config-format) to display a value as percentage. The presence of a percent sign in the format string turns the percentage handling on. Note that the value passed as config or set programmatically has to be a decimal number. Numbers entered into the field are divided by 100. Excess digits will be rounded up or down.

#### Pattern description

* `0-9`: Significant digit
* `#`: Insignificant digit, will be omitted when zero
* `.`: Decimal separator
* `%`: Percent designator.

```
new NumberField({
  format : '0.0#%',
  value  : 0.125
});
```

The resulting value displayed will be `12.5%`.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[wrapAround](https://bryntum.com/docs/gantt/api/Core/widget/NumberField#config-wrapAround)
Reset to min value when max value is reached using steppers, and vice-versa.

[min](https://bryntum.com/docs/gantt/api/Core/widget/NumberField#config-min)
Min value

[max](https://bryntum.com/docs/gantt/api/Core/widget/NumberField#config-max)
Max value

[step](https://bryntum.com/docs/gantt/api/Core/widget/NumberField#config-step)
Step size for spin button clicks. Also used when pressing up/down keys in the field. Note that when percent formatting [format](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField#config-format) is configured, the step size is divided by 100 because the internal value is a fractional number. Incrementing/decrementing by `step : 1` changes the value by 0.01, which equals 1%.

[largeStep](https://bryntum.com/docs/gantt/api/Core/widget/NumberField#config-largeStep)
Large step size, defaults to 10 \* `step`. Applied when pressing SHIFT and stepping either by click or using keyboard. Note that when percent formatting [format](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField#config-format) is configured, the step size is divided by 100 because the internal value is a fractional number. Incrementing/decrementing by `largeStep : 10` changes the value by 0.1, which equals 10%.

[value](https://bryntum.com/docs/gantt/api/Core/widget/NumberField#config-value)
Initial value

[format](https://bryntum.com/docs/gantt/api/Core/widget/NumberField#config-format)
The format to use for rendering numbers.

For example:

```
 format: '9,999.00##'
```

The above enables digit grouping and will display at least 2 (but no more than 4) fractional digits.

[triggers](https://bryntum.com/docs/gantt/api/Core/widget/NumberField#config-triggers)
Widgets that trigger functionality upon click. Each trigger icon is a [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget) instance which may be hidden, shown and observed and styled just like any other widget.

[changeOnSpin](https://bryntum.com/docs/gantt/api/Core/widget/NumberField#config-changeOnSpin)
Controls how change events are triggered when stepping the value up or down using either spinners or arrow keys.

Configure with:

* `true` to trigger a change event per step
* `false` to not trigger change while stepping. Will trigger on blur/Enter
* A number of milliseconds to buffer the change event, triggering when no steps are performed during that period of time.

[inputType](https://bryntum.com/docs/gantt/api/Core/widget/NumberField#config-inputType)
This can be set to `'number'` to enable the numeric virtual keyboard on mobile devices. Doing so limits this component's ability to handle keystrokes and format properly as the user types, so this is not recommended for desktop applications. This will also limit similar features of automated testing tools that mimic user input.

[rendition](https://bryntum.com/docs/gantt/api/Core/widget/NumberField#config-rendition)
Predefined style to use for the field. Possible values are:

* `'outlined'` (default)
* `'filled'`

The supplied value will be part of the field's class list, as `b-text-field-{rendition}`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isNumberField](https://bryntum.com/docs/gantt/api/Core/widget/NumberField#property-isNumberField)
Identifies an object as an instance of [NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField) class, or subclass thereof.

[isNumberField](https://bryntum.com/docs/gantt/api/Core/widget/NumberField#property-isNumberField-static)
Identifies an object as an instance of [NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField) class, or subclass thereof.

[step](https://bryntum.com/docs/gantt/api/Core/widget/NumberField#property-step)
Step size for spin button clicks.

[triggers](https://bryntum.com/docs/gantt/api/Core/widget/NumberField#property-triggers)
Widgets that trigger functionality upon click. Each trigger icon is a [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget) instance which may be hidden, shown and observed and styled just like any other widget.

[rendition](https://bryntum.com/docs/gantt/api/Core/widget/NumberField#property-rendition)
Predefined style to use for the field. Possible values are:

* `'outlined'` (default)
* `'filled'`

The supplied value will be part of the field's class list, as `b-text-field-{rendition}`.

## Functions

Functions are methods available for calling on the class

[changeValue](https://bryntum.com/docs/gantt/api/Core/widget/NumberField#function-changeValue)
Get/set the NumberField's value, or `undefined` if the input field is empty
