# Source: https://docs.datadoghq.com/dashboards/functions/timeshift.md

---
title: Timeshift
description: >-
  Compare current metric values with historical data using timeshift, calendar
  shift, and time-based comparison functions.
breadcrumbs: Docs > Dashboards > Functions > Timeshift
---

# Timeshift

Here is a set of functions performing a time shift of your data. These functions display the values from the corresponding time period on the graph. On their own, they may not be of high value, but together with the current values they may provide useful insight into the performance of your application.

## Timeshift{% #timeshift %}

| Function      | Description                                                                                    | Example                                          |
| ------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| `timeshift()` | Graph values from an arbitrary `<TIME_IN_SECOND>` before the current timestamp for the metric. | `timeshift(<METRIC_NAME>{*}, -<TIME_IN_SECOND>)` |

For example, if you wanted to use this to compare current system load with load from 2 weeks ago (60*60*24*14 = 1209600), your query would be:

```text
timeshift(avg:system.load.1{*}, -1209600)
```

## Calendar shift{% #calendar-shift %}

| Function           | Description                                                                                   | Example                                                                       |
| ------------------ | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `calendar_shift()` | Graph values from the previous day, week, or month from the current timestamp for the metric. | `calendar_shift(<METRIC_NAME>{*}, "<TIME_SHIFT_STRING>", "<TIME_ZONE_CODE>")` |

To access the `calendar_shift()` function click the **Add function** button, select **Timeshift > Month before**. The calendar shift allows you to compare the same metric across equivalent time frames. Below is an example of cloud cost metric `aws.cost.net.amortized` with the calendar_shift() value from two weeks ago compared to the current value.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/timeshift/calendar_shift_two_weeks.64f0013006ef1fce8c666842f79fa7d4.png?auto=format"
   alt="Example of a calendar_shift() function used to compare the `aws.cost.net.amortized ` metric value from two weeks ago and the present" /%}

Valid `TIME_SHIFT_STRING` values are negative integers followed by "d" for days, "w" for weeks, or "mo" for months. Some examples are `-1d`, `-7d`, `-1mo`, `-30d`, and `-4w`.

Valid `TIME_ZONE_CODE` values are the IANA time zone codes for a specific city, or `UTC`. For example, `UTC`, `America/New_York`, `Europe/Paris`, or `Asia/Tokyo`.

## Hour before{% #hour-before %}

| Function        | Description                                                            | Example                         |
| --------------- | ---------------------------------------------------------------------- | ------------------------------- |
| `hour_before()` | Graph values from an hour before the current timestamp for the metric. | `hour_before(<METRIC_NAME>{*})` |

Here is an example of `system.load.1` with the `hour_before()` value shown as a dotted line. In this particular example, you can see the machine was started at 6:30am and the `hour_before()` values show up at the 7:30 mark. Of course, this example was created specifically so that you can see the `hour_before()` values match up with the actual values.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/timeshift/simple_hour_before_example.d8de9bd32de9202697c168daad2293c9.png?auto=format"
   alt="simple hour before example" /%}

## Day before{% #day-before %}

{% alert level="warning" %}
The day before feature is being deprecated. Use calendar shift with a value of "-1d" instead.
{% /alert %}

| Function       | Description                                                          | Example                        |
| -------------- | -------------------------------------------------------------------- | ------------------------------ |
| `day_before()` | Graph values from a day before the current timestamp for the metric. | `day_before(<METRIC_NAME>{*})` |

Here is an example of `nginx.net.connections` with the `day_before()` value shown as a lighter, thinner line. In this example, you can see a week's worth of data, which makes the `day_before()` data easier to identify.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/timeshift/simple_day_before_example.ac2199149a3c384da77ed4f8232cc104.png?auto=format"
   alt="simple day before example" /%}

## Week before{% #week-before %}

{% alert level="warning" %}
The week before feature is being deprecated. Use calendar shift with a value of "-7d" instead.
{% /alert %}

| Function        | Description                                                                    | Example                         |
| --------------- | ------------------------------------------------------------------------------ | ------------------------------- |
| `week_before()` | Graph values from a week (7 days) before the current timestamp for the metric. | `week_before(<METRIC_NAME>{*})` |

Here is an example of `cassandra.db.read_count` with the `week_before()` value shown as a dotted line. In this example, you can see about three weeks' worth of data, which makes the `week_before()` data easier to identify.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/timeshift/simple_week_before_example.76798b198f09ee2ffc4476e5ed5fc582.png?auto=format"
   alt="simple week before example" /%}

## Month before{% #month-before %}

{% alert level="warning" %}
The month before feature is being deprecated. Use calendar shift with a value of "-1mo", "-30d" or "-4w" instead, depending on your use case.
{% /alert %}

| Function         | Description                                                                                | Example                          |
| ---------------- | ------------------------------------------------------------------------------------------ | -------------------------------- |
| `month_before()` | Graph values from a month (28 days / 4 weeks) before the current timestamp for the metric. | `month_before(<METRIC_NAME>{*})` |

Here is an example of `aws.ec2.cpuutilization` with the `month_before()` value shown as a thin, solid line.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/timeshift/simple_month_before_example.c3d0fa39315edf3d8c7b8a97fd5df25f.png?auto=format"
   alt="simple month before example" /%}

## Other functions{% #other-functions %}

- [Algorithmic: Implement Anomaly or Outlier detection on your metric.](https://docs.datadoghq.com/dashboards/functions/algorithms)
- [Arithmetic: Perform Arithmetic operation on your metric.](https://docs.datadoghq.com/dashboards/functions/arithmetic)
- [Count: Count non zero or non null value of your metric.](https://docs.datadoghq.com/dashboards/functions/count)
- [Exclusion: Exclude certain values of your metric.](https://docs.datadoghq.com/dashboards/functions/exclusion)
- [Interpolation: Fill or set default values for your metric.](https://docs.datadoghq.com/dashboards/functions/interpolation)
- [Rank: Select only a subset of metrics.](https://docs.datadoghq.com/dashboards/functions/rank)
- [Rate: Calculate custom derivative over your metric.](https://docs.datadoghq.com/dashboards/functions/rate)
- [Regression: Apply some machine learning function to your metric.](https://docs.datadoghq.com/dashboards/functions/regression)
- [Rollup: Control the number of raw points used in your metric.](https://docs.datadoghq.com/dashboards/functions/rollup)
- [Smoothing: Smooth your metric variations.](https://docs.datadoghq.com/dashboards/functions/smoothing)

## Further Reading{% #further-reading %}

- [Graph the percentage change between an earlier value and a current value.](https://docs.datadoghq.com/dashboards/faq/how-can-i-graph-the-percentage-change-between-an-earlier-value-and-a-current-value/)
