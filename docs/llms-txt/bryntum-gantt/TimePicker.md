# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/TimePicker.md

# [TimePicker](https://bryntum.com/docs/gantt/api/Core/widget/TimePicker)

A Container which displays hour and minute (and optionally second) lists to pick values from.

```
new TimeField({
    label     : 'Time field',
    appendTo  : document.body,
    // Configure the time picker
    picker    : {
        cls : 'my-picker.class
    }
});
```

Contained widgets
-----------------

The default widgets contained in this picker are:

Widget ref

Type

Description

`hour`

[List](https://bryntum.com/docs/gantt/api/#Core/widget/List)

The hour picker

`minute`

[List](https://bryntum.com/docs/gantt/api/#Core/widget/List)

The minute picker

`second`

[List](https://bryntum.com/docs/gantt/api/#Core/widget/List)

The second picker

This class is not intended for use in applications. It is used internally by the [TimeField](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField) class.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[value](https://bryntum.com/docs/gantt/api/Core/widget/TimePicker#config-value)
Time value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/TimePicker#config-format)

[format](https://bryntum.com/docs/gantt/api/Core/widget/TimePicker#config-format)
Time format. Used to set appropriate 12/24 hour format to display. See [DateHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-format-static) for formatting options.

[max](https://bryntum.com/docs/gantt/api/Core/widget/TimePicker#config-max)
Max value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/TimePicker#config-format)

[min](https://bryntum.com/docs/gantt/api/Core/widget/TimePicker#config-min)
Min value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/TimePicker#config-format)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimePicker](https://bryntum.com/docs/gantt/api/Core/widget/TimePicker#property-isTimePicker)
Identifies an object as an instance of [TimePicker](https://bryntum.com/docs/gantt/api/#Core/widget/TimePicker) class, or subclass thereof.

[isTimePicker](https://bryntum.com/docs/gantt/api/Core/widget/TimePicker#property-isTimePicker-static)
Identifies an object as an instance of [TimePicker](https://bryntum.com/docs/gantt/api/#Core/widget/TimePicker) class, or subclass thereof.

[value](https://bryntum.com/docs/gantt/api/Core/widget/TimePicker#property-value)
Time value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/TimePicker#config-format)

[format](https://bryntum.com/docs/gantt/api/Core/widget/TimePicker#property-format)
Time format. Used to set appropriate 12/24 hour format to display. See [DateHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-format-static) for formatting options.

[max](https://bryntum.com/docs/gantt/api/Core/widget/TimePicker#property-max)
Max value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/TimePicker#config-format)

[min](https://bryntum.com/docs/gantt/api/Core/widget/TimePicker#property-min)
Min value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/TimePicker#config-format)

[initialValue](https://bryntum.com/docs/gantt/api/Core/widget/TimePicker#property-initialValue)
Initial value, which can be a Date or a string. If a string is specified, it will be converted using the specified [format](https://bryntum.com/docs/gantt/api/#Core/widget/TimePicker#config-format). Initial value is restored on Escape click

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[timeChange](https://bryntum.com/docs/gantt/api/Core/widget/TimePicker#event-timeChange)
Fires when a time is changed.
