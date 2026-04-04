# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/CalendarPanel.md

# [CalendarPanel](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel)

A Panel which displays a month of date cells.

This is a base class for UI widgets like [DatePicker](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker) which need to display a calendar layout.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[date](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-date)
The date which this CalendarPanel encapsulates.

[month](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-month)
A [Month](https://bryntum.com/docs/gantt/api/#Core/util/Month) Month utility object which encapsulates this Panel's month and provides contextual information and navigation services.

[weekStartDay](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-weekStartDay)
The week start day, 0 meaning Sunday, 6 meaning Saturday. Defaults to [weekStartDay](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-weekStartDay-static).

[sixWeeks](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-sixWeeks)
Configure as `true` to always show a six-week calendar.

[showWeekColumn](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-showWeekColumn)
Configure as `true` to show a week number column at the start of the calendar block.

[disabledDates](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-disabledDates)
Either an array of `Date` objects which are to be disabled (or date strings), or a function (or the name of a function), which, when passed a `Date` returns `true` if the date is disabled. Disabled dates cannot be interacted with.

[headerRenderer](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-headerRenderer)
A function (or the name of a function) which creates content in, and may mutate a day header element.

The cell element may be mutated, or an HTML string or [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object may be returned.

[weekRenderer](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-weekRenderer)
A function (or the name of a function) which creates content in, and may mutate the week cell element at the start of a week row.

```
weekRenderer(wekkCell, week) {
    // week[0] is the year
    // week[1] is the week number
    cell.innerText = week[1];
}
```

The cell element may be mutated, or an HTML string or [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object may be returned.

[cellRenderer](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-cellRenderer)
A function (or the name of a function) which creates content in, and may mutate a day cell element.

[disableWeekends](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-disableWeekends)
Configure as `true` to render Saturdays and Sundays as [disabledDates](https://bryntum.com/docs/gantt/api/#Core/widget/CalendarPanel#config-disabledDates).

[shadePastDates](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-shadePastDates)
Configure as `true` to render past dates in a lighter text color.

[disableNonWorkingDays](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-disableNonWorkingDays)
Configure as `true` to render non working days as [disabledDates](https://bryntum.com/docs/gantt/api/#Core/widget/CalendarPanel#config-disabledDates).

Note, that by default, non working days are read from the locale, and are normally Saturday and Sunday. But they can be set to other days than weekend days.

[nonWorkingDays](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-nonWorkingDays)
Non-working days as an object where keys are day indices, 0-6 (Sunday-Saturday), and the value is `true`. Defaults to [nonWorkingDays](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-nonWorkingDays-static).

[tip](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-tip)
A config object to create a tooltip which will show on hover of a date cell including disabled, weekend, and "other month" cells.

It is the developer's responsibility to hook the `beforeshow` event to either veto the show by returning `false` or provide contextual content for the date.

The tip instance will be primed with a `date` property.

[disabledCls](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-disabledCls)
The class name to add to disabled calendar cells.

[otherMonthCls](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-otherMonthCls)
The class name to add to calendar cells which are in the previous or next month.

[weekendCls](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-weekendCls)
The class name to add to calendar cells which are weekend dates.

[todayCls](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-todayCls)
The class name to add to the calendar cell which contains today's date.

[nonWorkingDayCls](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-nonWorkingDayCls)
The class name to add to calendar cells which are [nonWorkingDays](https://bryntum.com/docs/gantt/api/#Core/widget/CalendarPanel#config-nonWorkingDays).

[dayNameFormat](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-dayNameFormat)
The [DateHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper) format string to format the day names in the header row above the calendar cells.

[minRowHeight](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-minRowHeight)
By default, week rows flex to share available Panel height equally.

Set this config if the available height is too small, and the cell height needs to be larger to show events.

Setting this config causes the month grid to become scrollable in the `Y` axis.

May be specified as a number in which case it will be taken to mean pixels, or a length in standard CSS units.

[minColumnWidth](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-minColumnWidth)
By default, day cells flex to share available Panel width equally.

Set this config if the available width is too small, and the cell width needs to be larger to show events.

Setting this config causes the month grid to become scrollable in the `X` axis.

[disableOtherMonthCells](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-disableOtherMonthCells)
Configure this as true to disable pointer interaction with cells which are outside the range of the current month.

[hideOtherMonthCells](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-hideOtherMonthCells)
Configure this as `true` to hide cells which are outside the range of the current month.

[animateTimeShift](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-animateTimeShift)
By default, when navigating through time, the next time block will be animated in from the appropriate direction.

Configure this as `false` to disable this.

[weekColumnHeader](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#config-weekColumnHeader)
The header text for the week number column, if shown.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCalendarPanel](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#property-isCalendarPanel)
Identifies an object as an instance of [CalendarPanel](https://bryntum.com/docs/gantt/api/#Core/widget/CalendarPanel) class, or subclass thereof.

[isCalendarPanel](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#property-isCalendarPanel-static)
Identifies an object as an instance of [CalendarPanel](https://bryntum.com/docs/gantt/api/#Core/widget/CalendarPanel) class, or subclass thereof.

[date](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#property-date)
Gets or sets the date that orientates the panel to display a particular month. Changing this causes the content to be refreshed.

[showWeekColumn](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#property-showWeekColumn)
Configure as `true` to show a week number column at the start of the calendar block.

[shadePastDates](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#property-shadePastDates)
Configure as `true` to render past dates in a lighter text color.

[animateTimeShift](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#property-animateTimeShift)
By default, when navigating through time, the next time block will be animated in from the appropriate direction.

Configure this as `false` to disable this.

[weekColumnHeader](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#property-weekColumnHeader)
The header text for the week number column, if shown.

[startDate](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#property-startDate)
The date of the first day cell in this panel. Note that this may _not_ be the first of this panel's current month.

[endDate](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#property-endDate)
The end date of this view. Note that in terms of full days, this is exclusive, ie: 2020-01-012 to 2020-01-08 is _seven_ days. The end is 00:00:00 on the 8th.

Note that this may _not_ be the last date of this panel's current month.

[visibleWeekCount](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#property-visibleWeekCount)
The number of rows displayed in this month. If [sixWeeks](https://bryntum.com/docs/gantt/api/#Core/widget/CalendarPanel#config-sixWeeks) is not set, this may be from 4 to 6.

## Functions

Functions are methods available for calling on the class

[updateDate](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#function-updateDate)
The date which this CalendarPanel encapsulates. Setting this causes the content to be refreshed.

[updateWeekStartDay](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#function-updateWeekStartDay)
Set to 0 for Sunday (the default), 1 for Monday etc.

Set to `null` to use the default value from [DateHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper).

[refresh](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#function-refresh)
Refreshes the UI after changing a config that would affect the UI.

[doRefresh](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#function-doRefresh)
Implementation of the UI refresh.

[getCell](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#function-getCell)
Returns the cell associated with the passed date.

To exclude dates which are outside of the panel's current month, pass the `strict` parameter as `true`

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[cellClick](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#event-cellClick)
Fired when a date cell is clicked.

[weekCellClick](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#event-weekCellClick)
Fired when a week number cell is clicked.

[dateChange](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#event-dateChange)
Fires when the date of this CalendarPanel is set.

[beforeRefresh](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#event-beforeRefresh)
Fires before this CalendarPanel refreshes in response to changes in its month.

[refresh](https://bryntum.com/docs/gantt/api/Core/widget/CalendarPanel#event-refresh)
Fires when this CalendarPanel refreshes.
