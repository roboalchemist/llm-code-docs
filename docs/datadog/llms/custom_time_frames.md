# Source: https://docs.datadoghq.com/dashboards/guide/custom_time_frames.md

---
title: Custom Time Frames
description: >-
  Use custom time frame syntaxes including fixed dates, relative dates, and
  calendar aligned periods in Datadog dashboards.
breadcrumbs: Docs > Dashboards > Graphing Guides > Custom Time Frames
---

# Custom Time Frames

## Overview{% #overview %}

{% alert level="info" %}
Queries are run in UTC time, but the query time frame is selected according to your **browser's time zone**. Toggle between displaying the default time zone or UTC from the dashboard configure action. For more information, see the [Dashboard configuration documentation](https://docs.datadoghq.com/dashboards/configure/#configuration-actions).
{% /alert %}

Many views in Datadog can be scoped to a specific time frame. Time controls include a list of common time frames and a calendar picker for quick selection.

To increment by month, day, year, hour, or minute, highlight a portion of the time frame and use the `[â]` and `[â]` keys:

{% video
   url="https://datadog-docs.imgix.net/images/dashboards/guide/custom_time_frames/increment_with_arrow_keys.mp4" /%}

## Supported syntaxes{% #supported-syntaxes %}

### Fixed dates{% #fixed-dates %}

{% video
   url="https://datadog-docs.imgix.net/images/dashboards/guide/custom_time_frames/custom_fixed_time_frame.mp4" /%}

| Format                       | Examples                                     |
| ---------------------------- | -------------------------------------------- |
| `{MMM/MMMM} D`               | Jan 1January 1                               |
| `M/D`                        | 1â/â1                                        |
| `M-D`                        | 1-1                                          |
| `M/D/{YY/YYYY}`              | 1/1/191/1/2019                               |
| `M-D-{YY/YYYY}`              | 1-1-191-1-2019                               |
| `{MMM/MMMM} D, h:mm a`       | Jan 1, 1:00 pmJanuary 1, 1:00 pm             |
| `{MMM/MMMM} D, YYYY, h:mm a` | Jan 1, 2019, 1:00 pmJanuary 1, 2019, 1:00 pm |
| `h:mm a`                     | 1:00 pm                                      |
| Unix seconds timestamp       | 1577883600                                   |
| Unix milliseconds timestamp  | 1577883600000                                |

Any fixed date can be entered as part of a range. For example:

- `1577883600 - 1578009540`
- `Jan 1 - Jan 2`
- `6:00 am - 1:00 pm`

### Relative dates{% #relative-dates %}

Relative dates update over time; they are calculated from the current time.

{% video
   url="https://datadog-docs.imgix.net/images/dashboards/guide/custom_time_frames/custom_relative_time_frame.mp4" /%}

| Format                                        | Description                                                          |
| --------------------------------------------- | -------------------------------------------------------------------- |
| `N{unit}`See the list of accepted units below | Displays the past N units. For example, **3 mo** (the past 3 months) |
| `today`                                       | Displays the current calendar day until present                      |
| `yesterday`                                   | Displays the full previous calendar day                              |
| `this month`                                  | Displays the current calendar month until present                    |
| `last month`                                  | Displays the full previous calendar month                            |
| `this year`                                   | Displays the current calendar year until present                     |
| `last year`                                   | Displays the full previous calendar year                             |

The following strings are accepted for any `{unit}` in a relative date:

- Minutes: `m`, `min`, `mins`, `minute`, `minutes`
- Hours: `h`, `hr`, `hrs`, `hour`, `hours`
- Days: `d`, `day`, `days`
- Weeks: `w`, `week`, `weeks`
- Months: `mo`, `mos`, `mon`, `mons`, `month`, `months`

### Calendar aligned dates{% #calendar-aligned-dates %}

Calendar aligned dates update to reflect the current day.

| Format          | Description                                      |
| --------------- | ------------------------------------------------ |
| `week to date`  | Displays the week from 12AM Monday until present |
| `month to date` | Displays the 1st of the month until present      |

## URLs{% #urls %}

You can manipulate time queries in the URL of a dashboard.

Consider the following dashboard URL:

```
https://app.datadoghq.com/dash/host/<DASHBOARD_ID>?from_ts=<QUERY_START>&to_ts=<QUERY_END>&live=true
```

- The `from_ts` parameter is the Unix milliseconds timestamp of the query starting time. For example, `1683518770980`.
- The `to_ts` parameter is the Unix milliseconds timestamp of the query ending time. For example, `1683605233205`.
- `live=true` indicates that relative time specifications are retained when a query is saved or shared. You can also use `live=false`.
