# Source: https://firebase.google.com/docs/perf-mon/console.md.txt

<br />

iOS+AndroidWeb  

<br />

To view real-time performance data, make sure that your app uses a Performance Monitoring SDK version that's compatible with real-time data processing.[Learn more about real-time performance data](https://firebase.google.com/docs/perf-mon/troubleshooting#faq-real-time-data).

## Track key metrics in your dashboard

To learn how your key metrics are trending, add them to your metrics board at the top of the*Performance*dashboard. You can quickly identify regressions by seeing week-over-week changes or verify that recent changes in your code are improving performance.
![an image of the metrics board in the <span class=](https://firebase.google.com/static/docs/perf-mon/images/perf-mon-metrics-board.png)Firebase Performance Monitoringdashboard" /\>

Here are some example trends that you could track:

- An increase in*app start time*since you added a new blocking API call to app start
- A drop in*response payload size*for a network request since you implemented resizing full-size images to thumbnails
- A decrease in network*success rate*for a third-party API call during an ecosystem outage

Each member of a Firebase project can configure their own metrics board. You can track metrics that are important to you, while other project members can track completely different sets of key metrics on their own boards.

To add a metric to your metrics board, follow these steps:

1. Go to the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance)in theFirebaseconsole.
2. Click an empty metric card, then select an existing metric to add to your board.
3. Clickmore_verton a populated metric card for more options, for example to replace or remove a metric.

<br />

The metrics board shows collected metric data over time, both in graphical form and as a numerical percentage change.

- Each metric card displays the percentage change in the metric's value over the selected time range, as well as the metric's most recently collected value. The statement at the top of the metrics board is an interpretation of the percentage change.

<!-- -->

- By default, the metrics board displays the metric's 90th percentile value, which aligns with[Android Vitals](https://support.google.com/googleplay/android-developer/answer/9844486#zippy=%2Cstart-up-time-time-to-initial-display%2Cexcessive-slow-frames%2Cexcessive-frozen-frames). If you'd like to view how different segments of your users experience your app, select a different percentile from the dropdown at the top of the dashboard page.
- If you have different versions of your app, you can view how the metric's value for one version is trending in comparison to another version and/or in comparison to*all*your versions. Select the versions from the dropdowns below the chart.

What do the red, green, and grey colors mean?

Most metrics have a desired trending direction, so the metrics board uses color to display an interpretion of whether the metric's data is trending in a good or bad direction.

For example, say you're tracking*app start time*for your app (a value that should be small). If this value is increasing, then the metrics board displays the metric's percentage change in red, calling attention to a possible issue. However, if the value is decreasing or unchanged, then the metrics board displays the percentage in green or grey, respectively.

If a metric doesn't have an obvious desired trending direction, like the*response payload size*for a network request, then the metrics board always displays the metric's percentage change in grey, regardless of how the data is trending.
What do the solid and dashed lines mean?

- dark blue solid line --- the metric's value over time for*all* versions of your app  
  This line can be considered the baseline for your app.

- light green solid line --- the metric's value over time for a specific version of your app  
  By default, the metrics board displays data for the*latest*version. To display a different version in the chart, use the first dropdown below the chart.

- grey solid line --- the metric's value over time for*another* specific version of your app  
  By default, the metrics board does not display data for a second version. To display a second version in the chart, use the second dropdown below the chart.

- light blue dashed line --- the metric's value for*all* versions at a specific time in the past  
  For example, if you select to show a chart of the last 7 days, and you hover over August 30, then the light blue dashed line tells you the metric's value for*all*versions on August 23.

<br />

*** ** * ** ***

<br />

## View traces and their data

You can view all traces for your app in the traces table, which is at the bottom of the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance/). The table groups each type of trace within an appropriate subtab. For example, all network request traces are listed under the*Network requests*subtab.

The traces table displays the values for some top metrics for each trace, along with the percentage change for each metric's value. These values are calculated based on the selections of percentile and time range set at the top of the*Dashboard*tab. Here are some examples:

- If you select a percentile of**90%** and a time range of**Last 7 days** , then the metric's value will be the*90th percentile* of collected data from the most recent*day*, and the percentage change will be the change since 7 days prior.

<!-- -->

- If you then change the time range to**Last 24 hours** , then the metric's value will be the*median* of collected data from the most recent*hour*, and the percentage change will be the change since 24 hours prior.

You can sort the list of traces in each subtab by the metric's value or by the percentage change for a specific metric. This can help you quickly identify potential problems in your app.

To view*all*the metrics and data for a specific trace, click the trace name in the traces table. The following sections of this page provide more details.

### View more data for a specific trace

Performance Monitoringprovides a troubleshooting page in theFirebaseconsole that highlights metric changes, making it easy to quickly address and minimize the impact of performance issues on your apps and users. You can use the troubleshooting page when you learn about potential performance issues, for example, in the following scenarios:

- You select relevant metrics on the dashboard and you notice a big delta.
- In the traces table you sort to display the largest deltas at the top, and you see a significant percentage change.
- You receive an email alert notifying you of a performance issue.

You can access the troubleshooting page in the following ways:

- On the metric dashboard, click the**View metric details**button.
- On any metric card, select**more_vert=\> View details**. The troubleshooting page displays information about the metric you selected.
- In the traces table, click a trace name or any metric value in the row associated with that trace.
- In an email alert, click**Investigate now**.

When you click a trace name in the traces table, you can then drill down into metrics of interest. Click the**Filteradd**button to filter the data by attribute, for example:
![an image of <span class=](https://firebase.google.com/static/docs/perf-mon/images/perf-mon-filter-by-attribute_native-1.png)Firebase Performance Monitoringdata being filtered by attribute" /\>

- Filter by*App version*to view data about a past release or your latest release
- Filter by*Device*to learn how older devices handle your app
- Filter by*Country*to make sure your database location isn't affecting a specific region

#### View all collected metrics for a trace

Once you click into a trace, you can drill down into metrics of interest:

- **Network request traces** --- The available metric tabs are*response time* ,*response payload size* ,*request payload size* , and*success rate*.
- **App start, app-in-foreground, app-in-background, and custom code traces** --- The*Duration*metric tab is always available (the default metric for these types of traces). For custom code traces, if you added any custom metrics to the trace, those metric tabs are also shown.

<!-- -->

- **Screen rendering traces** --- The available metric tabs are*Slow rendering* and*Frozen frames*.

You can find a performance summary for the selected metric right below the metric tabs. This includes a one-sentence overview of the metric's trend over time, and a chart to visualize the distribution of the data across the entire selected date range.
![an image of <span class=](https://firebase.google.com/static/docs/perf-mon/images/perf-mon-error-code-breakdown.png)Firebase Performance Monitoringerror code breakdown" /\>

For example, if the selected metric is**network success rate** , the chart shows a breakdown of all error codes and their percentages among all error responses (including the error codes[excluded on theFirebaseconsole](https://firebase.google.com/docs/perf-mon/custom-url-patterns#customize-success-rate-calculation)).

#### View in-depth information about the data

You can filter and segment the data by attribute, or you can click to view the data in the context of an app-usage session.

For example, to understand why your recent network response time is slow, and whether a country is affecting performance, follow these steps:

1. Select**Country**from the attributes dropdown.
2. In the table, sort by the latest value to see the countries that have the biggest impact on your network response times.
3. Select the countries with the largest latest values to plot them on the graph. Then hover your cursor over the timeline in the graph to learn when network response times slowed in those countries.
4. To further investigate root causes of network response time issues in specific countries, add filters for those countries and continue investigating across other attributes (like radio types and devices).

<br />

*** ** * ** ***

<br />

## View more details about user sessions

Performance Monitoringalso provides reports of user sessions, which are periods of time when your app is in the foreground. These reports are associated with a specific trace, and they present the trace in a timeline context of other traces thatPerformance Monitoringcollected during that same session.

For example, you can see your custom code traces lined up in the order they started (along with their individual durations), and you can also see any network request traces that were happening at that same time.

The console displays a random sampling of these user sessions. They're available for Apple and Android apps and for all types of traces*except*screen rendering traces.

Here's some of the other data that you can view about a user session:
![an image of the <span class=](https://firebase.google.com/static/docs/perf-mon/images/perf-mon-sessions-thumb.png)Firebase Performance Monitoringsessions page" /\>

- **Information about the trace:**Detailed information about the trace for that session, including start time, end time, attributes (like device and country), and any applicable metrics for that type of trace (for example, duration for a custom code trace or response time for a network request trace).
- **CPU:**How much user time and system time your app consumed during the session
- **Memory:** How muchyour app used during the session

#### How to view sessions data

1. Go to the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance)in theFirebaseconsole, scroll down to the traces table, then click the appropriate subtab for the trace of interest.
2. Click the trace name in the table to view all its available metrics.
3. To view sessions data for the specified trace, click**View all sessions**.
4. To view sessions associated with an attribute value of the selected metric, hover your cursor over the desired row and click the**Sessions**text that appears in the rightmost column of that row.

![an image of the <span class=](https://firebase.google.com/static/docs/perf-mon/images/perf-mon-view-sessions-data.png)Firebase Performance Monitoringtrace with a link to sessions" /\>

#### Filter sessions by percentile

Sessions are distributed into percentiles for each metric. Sessions in lower percentile ranges have a lower value for the metric than sessions in higher percentile ranges.

To filter the available sessions by percentile, use the percentiles dropdown above the sessions details, or drag the chart handles.
![an image of the <span class=](https://firebase.google.com/static/docs/perf-mon/images/perf-mon-filter-sessions-by-percentile.png)Firebase Performance Monitoringsessions page" /\>