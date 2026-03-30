# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/DateRangePicker.md

# [DateRangePicker](https://bryntum.com/docs/gantt/api/Core/widget/DateRangePicker)

This widget is used by [DateRangeField](https://bryntum.com/docs/gantt/api/#Core/widget/DateRangeField) to present a range of selected dates across multiple months.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[confirmable](https://bryntum.com/docs/gantt/api/Core/widget/DateRangePicker#config-confirmable)
Enables OK/Cancel button bar to accept date range changes. A value of `true` shows the OK and Cancel buttons.

[multiSelect](https://bryntum.com/docs/gantt/api/Core/widget/DateRangePicker#config-multiSelect)
Unlike its base class [MultiDatePicker](https://bryntum.com/docs/gantt/api/#Core/widget/MultiDatePicker), this config must be set to `'range'`.

[selection](https://bryntum.com/docs/gantt/api/Core/widget/DateRangePicker#config-selection)
The `selection` defined by [selection](https://bryntum.com/docs/gantt/api/#Core/widget/MultiDatePicker#config-selection) and the `value` defined by [value](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/AbstractDateRange#config-value) are synchronized. Use of `value` is preferred since this widget is used together with [DateRangeField](https://bryntum.com/docs/gantt/api/#Core/widget/DateRangeField) which also uses `value`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDateRangePicker](https://bryntum.com/docs/gantt/api/Core/widget/DateRangePicker#property-isDateRangePicker)
Identifies an object as an instance of [DateRangePicker](https://bryntum.com/docs/gantt/api/#Core/widget/DateRangePicker) class, or subclass thereof.

[isDateRangePicker](https://bryntum.com/docs/gantt/api/Core/widget/DateRangePicker#property-isDateRangePicker-static)
Identifies an object as an instance of [DateRangePicker](https://bryntum.com/docs/gantt/api/#Core/widget/DateRangePicker) class, or subclass thereof.

[confirmable](https://bryntum.com/docs/gantt/api/Core/widget/DateRangePicker#property-confirmable)
Enables OK/Cancel button bar to accept date range changes. A value of `true` shows the OK and Cancel buttons.

## Functions

Functions are methods available for calling on the class

[syncSelection](https://bryntum.com/docs/gantt/api/Core/widget/DateRangePicker#function-syncSelection)
Synchronizes the `selection` and `value` configs with each date pickers' selection.

[syncValue](https://bryntum.com/docs/gantt/api/Core/widget/DateRangePicker#function-syncValue)
Synchronizes the widget's state to a new `value`.
