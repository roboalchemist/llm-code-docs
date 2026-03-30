# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/util/DayTime.md

# [DayTime](https://bryntum.com/docs/gantt/api/Core/util/DayTime)

This class encapsulates time of day calculations.

The goal is to describe a "day" (a 24-hour period) that starts at a specific time (other than midnight). In a calendar day view, this would look like this:

```
             startShift=0                          startShift='12:00'
      00:00  +-------+                      12:00  +-------+
             |       |                             |       |
      01:00  |- - - -|                      13:00  |- - - -|
                ...                                   ...
             |       |                             |       |
      08:00  |- - - -|   <-- timeStart -->  20:00  |- - - -|
             |       |                             |       |
      09:00  |- - - -|                      21:00  |- - - -|
             |       |                             |       |
      10:00  |- - - -|                      22:00  |- - - -|
             |       |                             |       |
      11:00  |- - - -|                      23:00  |- - - -|
             |       |                             |       |
      12:00  |- - - -|                      00:00  |- - - -|
             |       |                             |       |
      13:00  |- - - -|                      01:00  |- - - -|
             |       |                             |       |
      14:00  |- - - -|                      02:00  |- - - -|
             |       |                             |       |
      15:00  |- - - -|                      03:00  |- - - -|
             |       |                             |       |
      16:00  |- - - -|                      04:00  |- - - -|
             |       |                             |       |
      17:00  |- - - -|    <-- timeEnd -->   05:00  |- - - -|
             |       |                             |       |
                ...                                   ...
             |       |                             |       |
      23:00  |- - - -|                      11:00  |- - - -|
             |       |                             |       |
      00:00  +-------+                      12:00  +-------+
```

In a horizontal format with X for times to render:

```
 startShift = 0

     +---+---+---  --+---+---+---+--   --+---+---+---+--   --+---+
     |   |   |  ...  |   |XXX|XXX|  ...  |XXX|XXX|   |  ...  |   |
     +---+---+---  --+---+---+---+--   --+---+---+---+--   --+---+
     00  01  02      07  08  09  10      15  16  17  18      23  00
                         ^                       ^
                     timeStart               timeEnd

 startShift = '12:00'

     +---+---+---  --+---+---+---+--   --+---+---+---+--   --+---+
     |   |   |  ...  |   |XXX|XXX|X ... X|XXX|XXX|   |  ...  |   |
     +---+---+---  --+---+---+---+--   --+---+---+---+--   --+---+
     12  13  14      19  20  21  22      03  04  05  06      11  12
                         ^                       ^
                     timeStart               timeEnd
```

When the day wraps over midnight, it is describing this (note timeEnd < timeStart):

```
     +---+---+---  --+---+---+---+--   --+---+---+---+--   --+---+
     |XXX|XXX|X ... X|XXX|   |   |  ...  |   |   |XXX|X ... X|XXX|
     +---+---+---  --+---+---+---+--   --+---+---+---+--   --+---+
     00  01  02      04  05  06  07      18  19  20  21      23  00
                         ^                       ^
                     timeEnd                 timeStart
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[startShift](https://bryntum.com/docs/gantt/api/Core/util/DayTime#config-startShift)
Either the hour number or a _24 hour_ `HH:MM` string denoting the start time for the day. This is midnight by default.

[timeStart](https://bryntum.com/docs/gantt/api/Core/util/DayTime#config-timeStart)
Either the hour number or a _24 hour_ `HH:MM` string denoting the first visible time of day. You can also set this value to a ms timestamp representing time from midnight.

[timeEnd](https://bryntum.com/docs/gantt/api/Core/util/DayTime#config-timeEnd)
Either the hour number or a _24 hour_ `HH:MM` string denoting the last visible time of day. You can also set this value to a ms timestamp representing time from midnight.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[startTimeOffsetMs](https://bryntum.com/docs/gantt/api/Core/util/DayTime#property-startTimeOffsetMs)
The number of milliseconds from the day's `startShift` to its `timeStart`.

[today](https://bryntum.com/docs/gantt/api/Core/util/DayTime#property-today)
The `Date` object for the most recently started, shifted day. The time of this `Date` will be the `startShift`. It is possible for this date to be yesterday on a midnight-based calendar. For example, if the `startShift` is 6PM and the current time is 6AM on May 20, this value will be 6PM of May 19 (the most recently started day).

[MIDNIGHT](https://bryntum.com/docs/gantt/api/Core/util/DayTime#property-MIDNIGHT-static)
The `DayTime` instance representing a canonical calendar day (starting at midnight).

## Functions

Functions are methods available for calling on the class

[format](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-format-static)
Returns a string of "HH:MM" for a given time of day in milliseconds.

[parse](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-parse-static)
Parses a time of day which may be a number (0-24 for the hour of the day) or a string in "H:MM" format and returns the time of day as a number of milliseconds.

If `time` is a `Date` instance, its time of day is returned.

[ceil](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-ceil)
Returns `Date` object for the nearest (shifted) day ending after the given `date`. The time of this `Date` will be the `startShift`.

It is possible for this date to be in the next day on a midnight-based calendar. For example, if the `startShift` is 6PM and `date` is 7PM on May 20, this method will return 6PM of May 21 (the nearest day ending).

[contains](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-contains)
Returns `true` if the time of day for the given `date` is between `timeStart` and `timeEnd`.

[dateKey](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-dateKey)
Returns a "YYYY-MM-DD" string for the given `date`. This value will match the `date` if the time of day is at or after `startShift`, but will be the prior date otherwise.

[dayOfDate](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-dayOfDate)
Returns a `Date` instance with `startShift` as the time of day and the Y/M/D of the given `date`.

[dayOfWeek](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-dayOfWeek)
Returns the day of week (0-8) for the given `date`. This value will match the `date` if the time of day is at or after `startShift`, but will be the prior day otherwise.

[delta](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-delta)
Returns the difference between the time of day of the given `date` and `timeStart` in the specified time `unit`.

[duration](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-duration)
Returns the duration of the visible day (between `timeStart` and `timeEnd`) in the specified time `unit`.

[equals](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-equals)
Returns `true` if this instance describes the same day as the `other`.

[intersects](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-intersects)
Returns `true` if the times of day described by `startDate` and `endDate` intersect the visible time of this day.

[isIntraDay](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-isIntraDay)
Returns `true` if the given date range is contained within one day.

[isInterDay](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-isInterDay)
Returns `true` if the given date range or event crosses the day boundary.

[outside](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-outside)
Returns -1, 0, or 1 based on whether the time of day for the given `date` is before `timeStart` (-1), or after `timeEnd` (1), or between these times (0).

[shiftDate](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-shiftDate)
Returns the given `date` shifted forward (`direction` > 0) or backward (`direction` < 0) by the `startShift`.

[sortEvents](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-sortEvents)
Sorts the given set of `events` by the maximum of `startDate` and `startOfDay` for the given `date`, followed by `duration` in case of a tie.

[startOfDay](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-startOfDay)
Returns `Date` object for the nearest started (shifted) day prior to the given `date`. The time of this `Date` will be the `startShift`.

It is possible for this date to be in the prior day on a midnight-based calendar. For example, if the `startShift` is 6PM and `date` is 6AM on May 20, this method will return 6PM of May 19 (the nearest started day).

[timeRange](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-timeRange)
Returns a range of [times of day](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-getTimeOfDay-static) for the given date range.

[_dateRangeArgs](https://bryntum.com/docs/gantt/api/Core/util/DayTime#function-_dateRangeArgs)
Decodes the arguments and returns a pair of `Date` objects for the start and end of the date range.
