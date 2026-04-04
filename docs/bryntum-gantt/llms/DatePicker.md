# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/DatePicker.md

# [DatePicker](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker)

A Panel which can display a month of date cells, which navigates between the cells, fires events upon user selection actions, optionally navigates to other months in response to UI gestures, and optionally displays information about each date cell. Appearance in the built-in themes:

A date is selected (meaning a single value is selected if [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-multiSelect) is not set, or added to the [selection](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#property-selection) if [if set](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-multiSelect)) by clicking a cell or by pressing `ENTER` when focused on a cell.

The `SHIFT` and `CTRL` keys modify selection behaviour depending on the value of [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-multiSelect).

This class is used as a [picker](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-picker) by the [DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField) class.

Styling cell content via CSS
----------------------------

Several different CSS classes are applied to date cells depending on their state. These can be used to style contents of cells via CSS.

* `b-disabled-date` - Applied to disabled days
* `b-weekend` - Applied to weekend days
* `b-past-date` - Applied to dates before today
* `b-today` - Applied to today's date
* `b-non-working-day` - Applied to dates which are [nonWorkingDays](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-nonWorkingDays)

By default, disabled dates in a lighter color. You can override this in your own CSS, using the CSS variable API of this class.

Custom cell rendering
---------------------

You can easily control the content of each date cell using the [cellRenderer](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-cellRenderer). The example below shows a view typically seen when booking hotel rooms or apartments.

Multi selection
---------------

You can select multiple date ranges or a single date range using the [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-multiSelect) config.

Configuring toolbar buttons
---------------------------

The datepicker includes a few useful navigation buttons by default. Through the DatePicker´s [toolbar](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-tbar), you can manipulate these, via the toolbar´s [items](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar#config-items) config.

There are four buttons by default, each of which can be reconfigured using an object, or disabled by configuring them as `null`.

```
new DatePicker({
   tbar : {
      // Remove all navigation buttons
      items : {
          prevYear  : null,
          prevMonth : null,
          nextYear  : null,
          nextMonth : null
      }
   },
   bbar : {
       items : {
           todayButton : {
               text     : 'Today',
               style    : 'margin-inline:auto',
               onClick  : 'up.onTodayClick'
           }
       }
   },
   onTodayClick() {
       this.date = new Date();
   }
})
```

Provided toolbar widgets include:

* `prevMonth` Navigates to previous month
* `nextMonth` Navigates to next month
* `prevYear` Navigates to previous year
* `nextYear` Navigates to next year

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[cellRenderer](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-cellRenderer)
A function (or the name of a function) which creates content in, and may mutate a day cell element.

The intention of this function is to allow you to augment the existing cell with additional information about the date.

The cell structure passed in the `cell` property is as follows:

```
<div class="b-calendar-panel-cell" data-date="2024-09-15">
    <div class="b-date-picker-cell-inner" role="presentation">15</div>
    <div class="b-date-picker-cell-payload"></div>
</div>
```

The `b-calendar-panel-cell` element is the cell element itself. It contains two child elements:

* `b-date-picker-cell-inner`: This element contains the date number.
* `b-date-picker-cell-payload`: This element is empty by default and can be used to augment the cell content.

The payload element is absolutely positioned, docked to the bottom of the cell. You may add content to this element, and target it with CSS to augment the cell content.

If you return content, textual HTML will _replace_ the contents of the `cell` element. A [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object will be used by [sync](https://bryntum.com/docs/gantt/api/#Core/helper/DomSync#function-sync-static) to update the `cell` element. If you want to augment the cell, it is recommended to add content to the `cellPayload` element.

[activeDate](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-activeDate)
The date that the user has navigated to using the UI _prior_ to setting the widget's value by selecting it. The initial default is today's date. Can also be supplied as a `YYYY-MM-DD` date string.

This may be changed using keyboard navigation. The [date](https://bryntum.com/docs/gantt/api/#Core/widget/CalendarPanel#property-date) is set by pressing `ENTER` when the desired date is reached.

Programmatically setting the [date](https://bryntum.com/docs/gantt/api/#Core/widget/CalendarPanel#config-date), or using the UI to select the date by clicking it also sets the `activeDate`

[date](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-date)
The initially selected date (or a `YYYY-MM-DD` date string).

[minDate](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-minDate)
The minimum selectable date. Selection of and navigation to dates prior to this date will not be possible.

[maxDate](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-maxDate)
The maximum selectable date. Selection of and navigation to dates after this date will not be possible.

[focusDisabledDates](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-focusDisabledDates)
By default, disabled dates cannot be navigated to, and they are skipped over during keyboard navigation. Configure this as `true` to enable navigation to disabled dates.

[multiSelect](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-multiSelect)
Configure as `true` to enable selecting multiple discontiguous date ranges using click and Shift+click to create ranges and Ctrl+click to select/deselect individual dates.

Configure as `'simple'` to enable selecting a single date range by clicking a start date followed by the end date. If you configure multiSelect `range` on touch-devices, `simple` will be the mode used.

Configure as `'range'` to enable selecting a single date range by selecting a start and end date. Hold "SHIFT" button to select date range. Ctrl+click may add or remove dates to/from either end of the range.

If `'range'` is used, then the [dragSelect](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-dragSelect) config may be used to enable range selection by dragging the mouse pointer across date cells while holding the primary mouse button down.

[dragSelect](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-dragSelect)
This property is only valid if [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-multiSelect) is set to `'range'` or `true`.

Configure as `true` to enable selecting a date range by dragging the mouse pointer across date cells while holding the primary mouse button down.

If [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-multiSelect) is set to `true`, use CTRL (CMD on Mac) while dragging to select multiple ranges.

[selection](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-selection)
If [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-multiSelect) is configured as `true`, this is an array of dates which are selected. There may be multiple, discontiguous date ranges.

If [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-multiSelect) is configured as `'range'` or `'simple'`, this is a two element array specifying the first and last selected dates in a range.

You can also provide the selected dates as an array of `YYYY-MM-DD` date strings

[editMonth](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-editMonth)
By default, the month and year are editable. Configure this as `false` to prevent that.

[includeYear](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-includeYear)
By default, the year is visible. Configure this as `false` to prevent that.

[dayNameFormat](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-dayNameFormat)
The [DateHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper) format string to format the day names.

[alwaysRefreshOnMonthChange](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-alwaysRefreshOnMonthChange)
By default, when the [date](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#property-date) changes, the UI will only refresh if it doesn't contain a cell for that date, so as to keep a stable UI when navigating.

Configure this as `true` to refresh the UI whenever the month changes, even if the UI already shows that date.

[highlightSelectedWeek](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-highlightSelectedWeek)
Configure as `true` to add a highlighted border and background to the week row which encapsulates the selected date.

[outOfRangeCls](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-outOfRangeCls)
The class name to add to the calendar cell whose date which is outside the [minDate](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-minDate)/[maxDate](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-maxDate) range.

[activeCls](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-activeCls)
The class name to add to the currently focused calendar cell.

[selectedCls](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-selectedCls)
The class name to add to selected calendar cells.

[monthButtonFormat](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#config-monthButtonFormat)
The format string to use to create the text of the month button.

It defaults to showing the full localized month name.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDatePicker](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#property-isDatePicker)
Identifies an object as an instance of [DatePicker](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker) class, or subclass thereof.

[isDatePicker](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#property-isDatePicker-static)
Identifies an object as an instance of [DatePicker](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker) class, or subclass thereof.

[dragSelect](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#property-dragSelect)
This property is only valid if [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-multiSelect) is set to `'range'` or `true`.

Configure as `true` to enable selecting a date range by dragging the mouse pointer across date cells while holding the primary mouse button down.

If [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-multiSelect) is set to `true`, use CTRL (CMD on Mac) while dragging to select multiple ranges.

[highlightSelectedWeek](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#property-highlightSelectedWeek)
Configure as `true` to add a highlighted border and background to the week row which encapsulates the selected date.

[selection](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#property-selection)
The selected Date(s).

When [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-multiSelect) is `'range'`, then this yields a two element array representing the start and end of the selected range.

When [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-multiSelect) is `true`, this yields an array containing every selected Date.

## Functions

Functions are methods available for calling on the class

[onUIDateSelect](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#function-onUIDateSelect)
Called when the user uses the UI to select the current activeDate. So ENTER when focused or clicking a date cell.

[isSelected](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#function-isSelected)
Checks whether a date is selected.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[selectionChange](https://bryntum.com/docs/gantt/api/Core/widget/DatePicker#event-selectionChange)
Fires when a date or date range is selected. If [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker#config-multiSelect) is specified, this will fire upon deselection and selection of dates.
