# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/widget/DayButtons.md

# [DayButtons](https://bryntum.com/docs/gantt/api/Scheduler/widget/DayButtons)

A segmented button field allowing you to pick one or more days of the week.

This live demo shows the default look + the "padded" rendition:

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[value](https://bryntum.com/docs/gantt/api/Scheduler/widget/DayButtons#config-value)
The value for this button group can be set as either an array of strings (e.g., \[‘SU’, ‘WE’, ‘TH’\]), or an array of day numbers (where 0 represents Sunday).

```
new DayButtons({
   appendTo : document.body,
   value : [0,1]
})
```

[pressedCls](https://bryntum.com/docs/gantt/api/Scheduler/widget/DayButtons#config-pressedCls)
A CSS class to add to the pressed state of the buttons.

[dayNameLength](https://bryntum.com/docs/gantt/api/Scheduler/widget/DayButtons#config-dayNameLength)
Number of chars to display for each day

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDayButtons](https://bryntum.com/docs/gantt/api/Scheduler/widget/DayButtons#property-isDayButtons)
Identifies an object as an instance of [DayButtons](https://bryntum.com/docs/gantt/api/#Scheduler/widget/DayButtons) class, or subclass thereof.

[isDayButtons](https://bryntum.com/docs/gantt/api/Scheduler/widget/DayButtons#property-isDayButtons-static)
Identifies an object as an instance of [DayButtons](https://bryntum.com/docs/gantt/api/#Scheduler/widget/DayButtons) class, or subclass thereof.

[value](https://bryntum.com/docs/gantt/api/Scheduler/widget/DayButtons#property-value)
The value for this button group can be set as either an array of strings (e.g., \[‘SU’, ‘WE’, ‘TH’\]), or an array of day numbers (where 0 represents Sunday).

```
new DayButtons({
   appendTo : document.body,
   value : [0,1]
})
```

[valueAsDayNumbers](https://bryntum.com/docs/gantt/api/Scheduler/widget/DayButtons#property-valueAsDayNumbers)
An array of the selected days, represented as JS day numbers (0 - Sunday, 1 - Monday etc.).
