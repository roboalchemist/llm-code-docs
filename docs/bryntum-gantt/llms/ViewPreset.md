# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/preset/ViewPreset.md

# [ViewPreset](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset)

A ViewPreset is a record of [PresetStore](https://bryntum.com/docs/gantt/api/#Scheduler/preset/PresetStore) which describes the granularity of the timeline view of a [Scheduler](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler) and the layout and subdivisions of the timeline header.

You can create a new instance by specifying all fields:

```
const myViewPreset = new ViewPreset({
    id   : 'myPreset',              // Unique id value provided to recognize your view preset. Not required, but having it you can simply set new view preset by id: scheduler.viewPreset = 'myPreset'

    name : 'My view preset',        // A human-readable name provided to be used in GUI, e.i. preset picker, etc.

    tickWidth  : 24,                // Time column width in horizontal mode
    tickHeight : 50,                // Time column height in vertical mode
    displayDateFormat : 'HH:mm',    // Controls how dates will be displayed in tooltips etc

    shiftIncrement : 1,             // Controls how much time to skip when calling shiftNext and shiftPrevious.
    shiftUnit      : 'day',         // Valid values are 'millisecond', 'second', 'minute', 'hour', 'day', 'week', 'month', 'quarter', 'year'.
    defaultSpan    : 12,            // By default, if no end date is supplied to a view it will show 12 hours

    timeResolution : {              // Dates will be snapped to this resolution
        unit      : 'minute',       // Valid values are 'millisecond', 'second', 'minute', 'hour', 'day', 'week', 'month', 'quarter', 'year'.
        increment : 15
    },

    headers : [                     // This defines your header rows from top to bottom
        {                           // For each row you can define 'unit', 'increment', 'dateFormat', 'renderer', 'align', and 'thisObj'
            unit       : 'day',
            dateFormat : 'ddd DD/MM'
        },
        {
            unit       : 'hour',
            dateFormat : 'HH:mm'
        }
    ],

    columnLinesFor : 1              // Defines header level column lines will be drawn for. Defaults to the last level.
});
```

Or you can extend one of view presets registered in [PresetManager](https://bryntum.com/docs/gantt/api/#Scheduler/preset/PresetManager):

```
const myViewPreset2 = new ViewPreset({
    id   : 'myPreset',                  // Unique id value provided to recognize your view preset. Not required, but having it you can simply set new view preset by id: scheduler.viewPreset = 'myPreset'
    name : 'My view preset',            // A human-readable name provided to be used in GUI, e.i. preset picker, etc.
    base : 'hourAndDay',                // Extends 'hourAndDay' view preset provided by PresetManager. You can pick out any of PresetManager's view presets: PresetManager.records

    timeResolution : {                  // Override time resolution
        unit      : 'minute',
        increment : 15                  // Make it increment every 15 mins
    },

    headers : [                         // Override headers
        {
            unit       : 'day',
            dateFormat : 'DD.MM.YYYY'   // Use different date format for top header 01.10.2020
        },
        {
            unit       : 'hour',
            dateFormat : 'LT'
        }
    ]
});
```

See [PresetManager](https://bryntum.com/docs/gantt/api/#Scheduler/preset/PresetManager) for the list of base presets. You may add your own presets to this global list:

```
PresetManager.add(myViewPreset);     // Adds new preset to the global scope. All newly created scheduler instances will have it too.

const scheduler = new Scheduler({
    viewPreset : 'myPreset'
    // other configs...
});
```

Or add them on an individual basis to Scheduler instances:

```
const scheduler = new Scheduler({...});

scheduler.presets.add(myViewPreset); // Adds new preset to the scheduler instance only. All newly created scheduler instances will **not** have it.

scheduler.viewPreset = 'myPreset';
```

Defining custom header rows
---------------------------

You can have any number of header rows by specifying [headers](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#field-headers), see [ViewPresetHeaderRow](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#typedef-ViewPresetHeaderRow) for the config object format and [DateHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper) for the supported date formats, or use to render custom contents into the row cells.

```
 headers : [
     {
         unit       : 'month',
         dateFormat : 'MM.YYYY'
     },
     {
         unit       : 'week',
         renderer   : ({ startDate }) => `Week ${DateHelper.format(startDate, 'WW')}`
     }
 ]
```

This live demo shows a custom ViewPreset with AM/PM time format:

### Using embedded text inside format string

Arbitrary text can be embedded in the format string by wrapping it with {}:

```
 headers : [
     {
         unit       : 'month',
         dateFormat : '{It is }MMMM{, yay!}' -> It is January, yay!
     },
     {
         unit       : 'week',
         renderer   : ({ startDate }) => `Week ${DateHelper.format(startDate, 'WW')}`
     }
 ]
```

## Fields

Fields belong to a Model class and define the Model data structure

[base](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#field-base)
The name of an existing view preset to extend

[name](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#field-name)
The name of the view preset

[rowHeight](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#field-rowHeight)
The height of the row in horizontal orientation

[tickWidth](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#field-tickWidth)
The width of the time tick column in horizontal orientation

[tickHeight](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#field-tickHeight)
The height of the time tick column in vertical orientation

[displayDateFormat](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#field-displayDateFormat)
Defines how dates will be formatted in tooltips etc

[shiftUnit](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#field-shiftUnit)
The unit to shift when calling shiftNext/shiftPrevious to navigate in the chart. Valid values are "millisecond", "second", "minute", "hour", "day", "week", "month", "quarter", "year".

[shiftIncrement](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#field-shiftIncrement)
The amount to shift (in shiftUnits)

[defaultSpan](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#field-defaultSpan)
The amount of time to show by default in a view (in the unit defined by [mainUnit](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#field-mainUnit))

[mainUnit](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#field-mainUnit)
Initially set to a unit. Defaults to the unit defined by the middle header.

[start](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#field-start)
Note: Currently, this field only applies when changing viewPreset with the [ViewPresetCombo](https://bryntum.com/docs/gantt/api/#Scheduler/widget/ViewPresetCombo).

Set to a number and that amount of [mainUnit](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#field-mainUnit) will be added to the startDate. For example: A start value of `5` together with the mainUnit `hours` will add 5 hours to the startDate. This can achieve a "day view" that starts 5 AM.

Set to a string unit (for example week, day, month) and the startDate will be the start of that unit calculated from current startDate. A start value of `week` will result in a startDate in the first day of the week.

If set to a number or not set at all, the startDate will be calculated at the beginning of current mainUnit.

[timeResolution](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#field-timeResolution)
An object containing a unit identifier and an increment variable. This value means minimal task duration you can create using UI. For example when you drag create a task or drag & drop a task, if increment is 5 and unit is 'minute' that means that you can create a 5-minute-long task, or move it 5 min forward/backward. This config maps to scheduler's [timeResolution](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineDateMapper#property-timeResolution) config.

```
timeResolution : {
  unit      : 'minute',  //Valid values are "millisecond", "second", "minute", "hour", "day", "week", "month", "quarter", "year".
  increment : 5
}
```

[headers](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#field-headers)
An array containing one or more [ViewPresetHeaderRow](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#typedef-ViewPresetHeaderRow) config objects, each of which defines a level of headers for the scheduler. The `main` unit will be the last header's unit, but this can be changed using the [mainHeaderLevel](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#field-mainHeaderLevel) field.

[mainHeaderLevel](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#field-mainHeaderLevel)
Index of the [headers](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#field-headers) array to define which header level is the `main` header. Defaults to the bottom header.

[columnLinesFor](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#field-columnLinesFor)
Index of a header level in the [headers](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#field-headers) array for which column lines are drawn. See [ColumnLines](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ColumnLines). Defaults to the bottom header.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isViewPreset](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#property-isViewPreset)
Identifies an object as an instance of [ViewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) class, or subclass thereof.

[isViewPreset](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#property-isViewPreset-static)
Identifies an object as an instance of [ViewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) class, or subclass thereof.

## Typedefs

Typedefs are type definitions for the class

[ViewPresetTimeResolution](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#typedef-ViewPresetTimeResolution)
An object containing a unit identifier and an increment variable, used to define the `timeResolution` of a `ViewPreset`.

[ViewPresetHeaderRow](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPreset#typedef-ViewPresetHeaderRow)
Defines a header level for a ViewPreset.

A sample header configuration can look like below

```
headers    : {
    {
        unit        : "month",
        renderer : function(start, end, headerConfig, index) {
            var month = start.getMonth();
            // Simple alternating month in bold
            if (start.getMonth() % 2) {
                return '<strong>' + month + '</strong>';
            }
            return month;
        },
        align       : 'start' // `start` or `end`, omit to center content (default)
    },
    {
        unit        : "week",
        increment   : 1,
        renderer    : function(start, end, headerConfig, index) {
            return 'foo';
        }
    },
}
```
