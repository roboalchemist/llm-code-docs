# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/MultiDatePicker.md

# [MultiDatePicker](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker)

This widget allows date selection presented across multiple [date pickers](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker). The API matches closely to a `DatePicker` since the only meaningful difference in functionality is the use of a carousel to present multiple months at the same time. This widget is a part of `DateRangePicker`.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[baseDate](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#config-baseDate)
The date that corresponds to carousel slot index 0.

[cellRenderer](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#config-cellRenderer)
A function (or the name of a function) which creates content in, and may mutate a day cell element.

See [cellRenderer](https://bryntum.com/docs/gantt/api/#Core/widget/CalendarPanel#config-cellRenderer).

[headerRenderer](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#config-headerRenderer)
A function (or the name of a function) which creates content in, and may mutate a day header element.

See [headerRenderer](https://bryntum.com/docs/gantt/api/#Core/widget/CalendarPanel#config-headerRenderer).

[weekRenderer](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#config-weekRenderer)
A function (or the name of a function) which creates content in, and may mutate the week cell element at the start of a week row.

See [weekRenderer](https://bryntum.com/docs/gantt/api/#Core/widget/CalendarPanel#config-weekRenderer).

[weekStartDay](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#config-weekStartDay)
The week start day, 0 meaning Sunday, 6 meaning Saturday. Defaults to [weekStartDay](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-weekStartDay-static).

[date](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#config-date)
The initially selected date.

[minDate](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#config-minDate)
The minimum selectable date. Selection of and navigation to dates prior to this date will not be possible.

[maxDate](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#config-maxDate)
The maximum selectable date. Selection of and navigation to dates after this date will not be possible.

[datePickerDefaults](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#config-datePickerDefaults)
The configuration defaults for all date pickers in the carousel.

[includeYear](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#config-includeYear)
Set to `false` to hide the year indicator field, or a function that accepts a `Date` and returns the desired visibility of the year field (`true` or `false`).

[multiSelect](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#config-multiSelect)
Configure as `true` to enable selecting multiple discontiguous date ranges using click and Shift+click to create ranges and Ctrl+click to select/deselect individual dates.

Configure as `'range'` to enable selecting a single date range by selecting a start and end date. Hold "SHIFT" button to select date range. Ctrl+click may add or remove dates to/from either end of the range.

Set to `false` to not allow multiple date selection.

[navButtons](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#config-navButtons)
Set to `false` to hide the next and previous month buttons.

[selection](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#config-selection)
The current date range selection as an array of two `Date` objects.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isMultiDatePicker](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#property-isMultiDatePicker)
Identifies an object as an instance of [MultiDatePicker](https://bryntum.com/docs/gantt/api/#Core/widget/MultiDatePicker) class, or subclass thereof.

[isMultiDatePicker](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#property-isMultiDatePicker-static)
Identifies an object as an instance of [MultiDatePicker](https://bryntum.com/docs/gantt/api/#Core/widget/MultiDatePicker) class, or subclass thereof.

[selection](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#property-selection)
The current date range selection as an array of two `Date` objects.

[datePickers](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#property-datePickers)
Returns all date picker child widgets.

## Functions

Functions are methods available for calling on the class

[ensureVisible](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#function-ensureVisible)
Ensures that the given slot `date` is visible, scrolling if necessary to make it so.

[ensurePlan](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#function-ensurePlan)
Decodes the `options` passed to [ensureVisible](https://bryntum.com/docs/gantt/api/#Core/widget/MultiDatePicker#function-ensureVisible) and ensures the object has the properties needed by [ensureVisible](https://bryntum.com/docs/gantt/api/#Core/widget/Carousel#function-ensureVisible).

[syncSelection](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#function-syncSelection)
Synchronizes the `selection` config with each date pickers' selection.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[selectionChange](https://bryntum.com/docs/gantt/api/Core/widget/MultiDatePicker#event-selectionChange)
Fires when a date or date range is selected. If [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/MultiDatePicker#config-multiSelect) is specified, this will fire upon deselection and selection of dates.
