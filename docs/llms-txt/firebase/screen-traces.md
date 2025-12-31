# Source: https://firebase.google.com/docs/perf-mon/screen-traces.md.txt

<br />

iOS+Android  

<br />

Performance Monitoringuses*traces*to collect data about monitored processes in your app. A trace is a report that contains data captured between two points in time in your app.

For Apple and Android apps,Performance Monitoring*automatically* measures the rendering performance of different screens in your application.Performance Monitoringcreates a***screen rendering trace***for every screen in your application. These traces collect and measure the following metrics:

- [Slow rendering frames](https://firebase.google.com/docs/perf-mon/screen-traces#slow-rendering-frames)--- Measures the percentage of screen instances that take longer than 16ms to render.

- [Frozen frames](https://firebase.google.com/docs/perf-mon/screen-traces#frozen-frames)--- Measures the percentage of screen instances that take longer than 700ms to render.

Slow or frozen frames in your application might result in poor device performance, also known as jank or lag. Capturing frozen and slow rendering frame metrics can help you identify underperforming screens, giving you the ability to improve the rendering performance of your application.

You can view data for screen rendering traces in the*Screen rendering* tab of the traces table. The traces table is located at the bottom of the*Performance* page of the[Firebaseconsole](https://console.firebase.google.com/). For more information, see[Track, view, and filter performance data](https://firebase.google.com/docs/perf-mon/screen-traces#monitor-in-console).
| These out-of-the-box traces get you started with monitoring your app, but to learn about the performance of specific tasks or flows in your app, try out[instrumenting your own custom traces of code](https://firebase.google.com/docs/perf-mon/custom-code-traces)in your app.

## Metrics collected by screen rendering traces

These traces are out-of-the-box traces, so you cannot add custom metrics or custom attributes to them.

Slow rendering frames and frozen frames are calculated with an assumed device refresh rate of 60Hz. If a device refresh rate is lower than 60Hz, each frame will have a slower rendering time because fewer frames are rendered per second. Slower rendering times can cause more slow or frozen frames to be reported because more frames will be rendered slower or will freeze. However, if a device refresh rate is higher than 60Hz, each frame will have a faster rendering time. This can cause fewer slow or frozen frames to be reported. This is a current limitation in thePerformance MonitoringSDK.

### Slow rendering frames

This metric is the percentage of user sessions that experienced a noticeable amount of slow rendering for a specific screen. Specifically, this metric is the percentage of screen instances during which more than 50% of frames took longer than 16 ms to render.

### Frozen frames

This metric is the percentage of user sessions that experienced a noticeable amount of frozen frames for a specific screen. Specifically, this metric is the percentage of screen instances during which more than 0.1% of frames took longer than 700 ms to render.

## How are screen rendering traces generated?

- Starts for every UIViewController in the keyWindow when the app calls`viewDidAppear:`.

- Stops when the app calls`viewDidDisappear:`.

Note that screen rendering traces don't capture canonical container view controllers.

## Track, view, and filter performance data

To view real-time performance data, make sure that your app uses a Performance Monitoring SDK version that's compatible with real-time data processing.[Learn more about real-time performance data](https://firebase.google.com/docs/perf-mon/troubleshooting#faq-real-time-data).

### Track key metrics in your dashboard

To learn how your key metrics are trending, add them to your metrics board at the top of the*Performance*dashboard. You can quickly identify regressions by seeing week-over-week changes or verify that recent changes in your code are improving performance.
![an image of the metrics board in the <span class=](https://firebase.google.com/static/docs/perf-mon/images/perf-mon-metrics-board.png)Firebase Performance Monitoringdashboard" /\>

To add a metric to your metrics board, follow these steps:

1. Go to the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance)in theFirebaseconsole.
2. Click an empty metric card, then select an existing metric to add to your board.
3. Clickmore_verton a populated metric card for more options, for example to replace or remove a metric.

<br />

The metrics board shows collected metric data over time, both in graphical form and as a numerical percentage change.

Learn more about[using the dashboard](https://firebase.google.com/docs/perf-mon/console).

### View screen performance on console

To view your traces, go to the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance)in theFirebaseconsole, scroll down to the traces table, then click the appropriate subtab. The table displays some top metrics for each trace, and you can even sort the list by the percentage change for a specific metric.

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

Learn more about[viewing data for your traces](https://firebase.google.com/docs/perf-mon/console#view-traces-and-data).

## Next Steps

- Learn more about[using attributes](https://firebase.google.com/docs/perf-mon/attributes)to examine performance data.

- Learn more about how to[track performance issues](https://firebase.google.com/docs/perf-mon/issue-management)in theFirebaseconsole.