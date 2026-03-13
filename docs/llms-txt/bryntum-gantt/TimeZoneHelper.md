# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/TimeZoneHelper.md

# [TimeZoneHelper](https://bryntum.com/docs/gantt/api/Core/helper/TimeZoneHelper)

Helper for time zone manipulation.

## Functions

Functions are methods available for calling on the class

[toTimeZone](https://bryntum.com/docs/gantt/api/Core/helper/TimeZoneHelper#function-toTimeZone-static)
Adjusts the time of the specified date to match the specified time zone. i.e. "what time is it now in this timezone?"

JavaScript dates are always in the local time zone. This function adjusts the time to match the time in the specified time zone, without altering the time zone. Thus, it won't hold the same time as the original date.

Note that this time zone calculation relies on the browsers built-in functionality to convert a local date to a string in a given time zone and then converting the string back into a date. If browsers time zone information or interpretation is inaccurate or lacks data, the conversion will probably be inaccurate as well.

```
const localDate = new Date(2020, 7, 31, 7); // UTC+2 ('Europe/Stockholm')
const cstDate   = TimeZoneHelper.toTimezone(localDate, 'America/Chicago'); // 2020, 7, 31, 0 (still UTC+2, but
// appear as UTC-6)
```

[fromTimeZone](https://bryntum.com/docs/gantt/api/Core/helper/TimeZoneHelper#function-fromTimeZone-static)
Adjusts the time of the specified date to match local system time zone in the specified time zone. i.e. "what time in my timezone would match time in this timezone?"

JavaScript dates are always in the local time zone. This function adjusts the time to match the time in the specified time zone, without altering the time zone. Thus, it won't hold the same time as the original date.

Note that this time zone calculation relies on the browsers built-in functionality to convert a date from a given timezone into a local date by calculating specified time zone UTC offsets and using those to perform the date conversion. If browsers time zone information or interpretation is inaccurate or lacks data, the conversion will probably be inaccurate as well.

```
const cstDate   = new Date(2022, 8, 27, 4); // CST 'America/Chicago'
const localDate = TimeZoneHelper.fromTimeZone(cstDate, 'America/Chicago'); // 2022, 8, 27, 11 (UTC+2 Europe/Stockholm)
```

[toUtcOffset](https://bryntum.com/docs/gantt/api/Core/helper/TimeZoneHelper#function-toUtcOffset-static)
Adjusts the time of the specified date with provided UTC offset in minutes

JavaScript dates are always in the local time zone. This function adjusts the time to match the time in the specified time zone, without altering the time zone. Thus, it won't hold the same time as the original date.

```
const localDate = new Date(2020, 7, 31, 7); // UTC+2
const utcDate   = TimeZoneHelper.toUtcOffset(localDate, 0); // 2020, 7, 31, 5 (still UTC+2, but appear as UTC+0)
```

[fromUtcOffset](https://bryntum.com/docs/gantt/api/Core/helper/TimeZoneHelper#function-fromUtcOffset-static)
Adjusts the time of the specified date by removing the provided UTC offset in minutes.

JavaScript dates are always in the local time zone. This function adjusts the time to match the time in the specified time zone, without altering the time zone. Thus, it won't hold the same time as the original date.

```
const utcDate = new Date(2020, 7, 31, 7); // UTC
const utcDate = TimeZoneHelper.fromUtcOffset(localDate, 0); // 2020, 7, 31, 9 (matches 2020-08-31 07:00+00:00)
```
