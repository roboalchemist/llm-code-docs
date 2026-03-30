# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/util/Month.md

# [Month](https://bryntum.com/docs/gantt/api/Core/util/Month)

A class which encapsulates a calendar view of a month, and offers information about the weeks and days within that calendar view.

```
  // December 2018 using Monday as week start
  const m = new Month({
      date         : '2018-12-01',
      weekStartDay : 1
  });

  m.eachWeek((week, dates) => console.log(dates.map(d => d.getDate())))
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[date](https://bryntum.com/docs/gantt/api/Core/util/Month#config-date)
The date which the month should encapsulate. May be a `Date` object, or a `YYYY-MM-DD` format string.

Mutating a passed `Date` after initializing a `Month` object has no effect on the `Month` object.

[weekStartDay](https://bryntum.com/docs/gantt/api/Core/util/Month#config-weekStartDay)
The week start day, 0 meaning Sunday, 6 meaning Saturday. Defaults to [weekStartDay](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-weekStartDay-static).

[hideNonWorkingDays](https://bryntum.com/docs/gantt/api/Core/util/Month#config-hideNonWorkingDays)
Configure as `true` to have the visibleDayColumnIndex and visibleColumnCount properties respect the configured [nonWorkingDays](https://bryntum.com/docs/gantt/api/#Core/util/Month#config-nonWorkingDays).

[nonWorkingDays](https://bryntum.com/docs/gantt/api/Core/util/Month#config-nonWorkingDays)
Non-working days as an object where keys are day indices, 0-6 (Sunday-Saturday), and the value is `true`. Defaults to [nonWorkingDays](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-nonWorkingDays-static).

[sixWeeks](https://bryntum.com/docs/gantt/api/Core/util/Month#config-sixWeeks)
Configure as `true` to always have the month encapsulate six weeks. This is useful for UIs which must be a fixed height.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[sixWeeks](https://bryntum.com/docs/gantt/api/Core/util/Month#property-sixWeeks)
Configure as `true` to always have the month encapsulate six weeks. This is useful for UIs which must be a fixed height.

[canonicalDayNumbers](https://bryntum.com/docs/gantt/api/Core/util/Month#property-canonicalDayNumbers)
For use when this Month's `weekStartDay` is non-zero.

An array to map the days of the week 0-6 of this Calendar to the canonical day numbers used by the Javascript [Date](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) object.

[visibleDayColumnIndex](https://bryntum.com/docs/gantt/api/Core/util/Month#property-visibleDayColumnIndex)
An array to map a canonical day number to a _visible_ column index. For example, if we have `weekStartDay` as Monday which is 1, and non working days as Wednesday, and `hideNonWorkingDays : true`, then the calendar would look like

```
┌────┬────┬────┬────┬────┬────┐
| Mo | Tu | Th | Fr | Sa | Su |
└────┴────┴────┴────┴────┴────┘
```

So we'd need this array: `[ 5, 0, 1, undefined, 2, 3, 4]`

[dayColumnIndex](https://bryntum.com/docs/gantt/api/Core/util/Month#property-dayColumnIndex)
An array to map a canonical day number to a 0-6 column index. For example, if we have `weekStartDay` as Monday which is 1, then the calendar would look like

```
┌────┬────┬────┬────┬────┬────┬────┐
| Mo | Tu | We | Th | Fr | Sa | Su |
└────┴────┴────┴────┴────┴────┴────┘
```

So we'd need this array: `[ 6, 0, 1, 2, 3, 4, 5]`

[weekLength](https://bryntum.com/docs/gantt/api/Core/util/Month#property-weekLength)
The number of visible days in the week as defined by the `nonWorkingDays` and `hideNonWorkingDays` options.

[dayCount](https://bryntum.com/docs/gantt/api/Core/util/Month#property-dayCount)
The number of days in the calendar for this month. This will always be a multiple of 7, because this represents the number of calendar cells occupied by this month.

[weekCount](https://bryntum.com/docs/gantt/api/Core/util/Month#property-weekCount)
The number of weeks in the calendar for this month.

[startDate](https://bryntum.com/docs/gantt/api/Core/util/Month#property-startDate)
The date of the first cell in the calendar view of this month.

[endDate](https://bryntum.com/docs/gantt/api/Core/util/Month#property-endDate)
The date of the last cell in the calendar view of this month.

[firstDate](https://bryntum.com/docs/gantt/api/Core/util/Month#property-firstDate)
The first date of the current month.

[lastDate](https://bryntum.com/docs/gantt/api/Core/util/Month#property-lastDate)
The last date of the current month.

## Functions

Functions are methods available for calling on the class

[getWeekStart](https://bryntum.com/docs/gantt/api/Core/util/Month#function-getWeekStart)
Returns the week start date, based on the configured [weekStartDay](https://bryntum.com/docs/gantt/api/#Core/util/Month#config-weekStartDay) of the passed week.

[eachDay](https://bryntum.com/docs/gantt/api/Core/util/Month#function-eachDay)
Iterates through all calendar cells in this month, calling the passed function for each date.

[eachWeek](https://bryntum.com/docs/gantt/api/Core/util/Month#function-eachWeek)
Iterates through all weeks in this month, calling the passed function for each week.

[getWeekNumber](https://bryntum.com/docs/gantt/api/Core/util/Month#function-getWeekNumber)
Returns the week of the year for the passed date. This returns an array containing _two_ values, the year **and** the week number are returned.

The week number is calculated according to ISO rules, meaning that if the first week of the year contains less than four days, it is considered to be the last week of the preceding year.

The configured [weekStartDay](https://bryntum.com/docs/gantt/api/#Core/util/Month#config-weekStartDay) is honoured in this calculation. So if the weekStartDay is **NOT** the ISO standard of `1`, (Monday), then the weeks do not coincide with ISO weeks.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[dateChange](https://bryntum.com/docs/gantt/api/Core/util/Month#event-dateChange)
Fired when setting the [date](https://bryntum.com/docs/gantt/api/#Core/util/Month#config-date) property causes the encapsulated date to change in **any** way, date, week, month or year.

[weekChange](https://bryntum.com/docs/gantt/api/Core/util/Month#event-weekChange)
Fired when setting the [date](https://bryntum.com/docs/gantt/api/#Core/util/Month#config-date) property causes a change of week. Note that weeks are calculated in the ISO standard form such that if there are fewer than four days in the first week of a year, then that week is owned by the previous year.

The [weekStartDay](https://bryntum.com/docs/gantt/api/#Core/util/Month#config-weekStartDay) is honoured when making this calculation and this is a locale-specific value which defaults to the ISO standard of 1 (Monday) in provided European locales and 0 (Sunday) in the provided US English locale.

[monthChange](https://bryntum.com/docs/gantt/api/Core/util/Month#event-monthChange)
Fired when setting the [date](https://bryntum.com/docs/gantt/api/#Core/util/Month#config-date) property causes a change of month. This will fire when changing to the same month in a different year.

[yearChange](https://bryntum.com/docs/gantt/api/Core/util/Month#event-yearChange)
Fired when setting the [date](https://bryntum.com/docs/gantt/api/#Core/util/Month#config-date) property causes a change of year.
