# Source: https://checklyhq.com/docs/concepts/results.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Results

> Learn about the results of Checkly

Check **Results** are the outcomes of every monitoring test that Checkly runs. You can select any check on the main Checkly dashboard to get an overview of the results they have produced so far. Select a check and you will see a breakdown of its recent runs, together with key availability and performance metrics.

Each time a Check executes—whether it's testing an API endpoint, clicking through a user flow, or verifying a service connection—it generates a **Result** that captures everything that happened during that test run.

**Results** are more than just pass or fail indicators. They're comprehensive records that include performance metrics, error details, screenshots, network traces, and any other telemetry that helps you understand not just whether something worked, but how well it worked and why it might have failed.

## Understanding Result Data

You can select any check on the main Checkly dashboard to get an overview of the results they have produced so far.

## Check results overview

Select a check and you will see a breakdown of its recent runs, together with key availability and performance metrics.

<img src="https://mintcdn.com/checkly-422f444a/pk96p0t2gChABUbF/images/docs/images/monitoring/check-overview.png?fit=max&auto=format&n=pk96p0t2gChABUbF&q=85&s=2214ef51c20dad73dd147e09097e7f04" alt="check results overview" width="1684" height="1053" data-path="images/docs/images/monitoring/check-overview.png" />

### Summary section

The summary at the top of the page allows for filtering based on the page's data points and the selected timeframe and locations. Retried check runs do not influence this section; only the final results are considered.

<img src="https://mintcdn.com/checkly-422f444a/pk96p0t2gChABUbF/images/docs/images/monitoring/check-overview-summary.png?fit=max&auto=format&n=pk96p0t2gChABUbF&q=85&s=6fbf1f5ee381fb32cf0cec8d5108326b" alt="check results overview summary" width="1500" height="272" data-path="images/docs/images/monitoring/check-overview-summary.png" />

Based on the user's selection, the metrics in the summary will also be updated to show the most important numbers at a glance.

### Monitoring results chart

The monitoring results chart shows a summary of the run results in the selected time period where each bar represents a part of that time period. You can change the time period in the summary section.

Hovering a bar in the chart will show the results of all check runs executed during that time. You can quickly filter the check run results in the right sidepanel by clicking a bar in the chart.

<img src="https://mintcdn.com/checkly-422f444a/pk96p0t2gChABUbF/images/docs/images/monitoring/check-overview-monitoring-result-chart.png?fit=max&auto=format&n=pk96p0t2gChABUbF&q=85&s=64114f14da689e80889f63bc729fa116" alt="check results overview time ribbon" width="936" height="260" data-path="images/docs/images/monitoring/check-overview-monitoring-result-chart.png" />

When retries are enabled, an additional icon highlights that the check result contains multiple check runs.

### Monitoring results sidebar

On the right side you can view the check result broken down per check run and location for the selected time frame. If you select a bar in the monitoring results chart it will filter out the corresponding results in the sidebar. Click any result to navigate to the check results screen for detailed information about the check run.

### Performance

Depending on the type of check, different performance metrics will be shown in the Performance section.

For Browser checks, several performance metrics are shown in separate charts:

1. The total duration of the check run
   <img src="https://mintcdn.com/checkly-422f444a/pk96p0t2gChABUbF/images/docs/images/monitoring/check-overview-performance-browser.png?fit=max&auto=format&n=pk96p0t2gChABUbF&q=85&s=c15a49172bfd082b01187ad84ad307d6" alt="check overview browser session duration graph" width="2700" height="1202" data-path="images/docs/images/monitoring/check-overview-performance-browser.png" />

2. Load timings for the first page navigation
   <img src="https://mintcdn.com/checkly-422f444a/pk96p0t2gChABUbF/images/docs/images/monitoring/check-overview-performance-loading.png?fit=max&auto=format&n=pk96p0t2gChABUbF&q=85&s=a06d5d48e833735130eb0328cbd7af27" alt="check overview load timings graph" width="2720" height="986" data-path="images/docs/images/monitoring/check-overview-performance-loading.png" />

3. A breakdown of different error types
   <img src="https://mintcdn.com/checkly-422f444a/pk96p0t2gChABUbF/images/docs/images/monitoring/check-overview-errors.png?fit=max&auto=format&n=pk96p0t2gChABUbF&q=85&s=c18dbc83c5cf812a50df8722b3688618" alt="check overview errors graph" width="2728" height="1048" data-path="images/docs/images/monitoring/check-overview-errors.png" />

4. An interactivity summary
   <img src="https://mintcdn.com/checkly-422f444a/pk96p0t2gChABUbF/images/docs/images/monitoring/check-overview-interactivity.png?fit=max&auto=format&n=pk96p0t2gChABUbF&q=85&s=8f2ab95fbdecfd41857c8dce91901f56" alt="check overview interactivity graph" width="2738" height="990" data-path="images/docs/images/monitoring/check-overview-interactivity.png" />

5. A visual stability breakdown
   <img src="https://mintcdn.com/checkly-422f444a/pk96p0t2gChABUbF/images/docs/images/monitoring/check-overview-visual-stability.png?fit=max&auto=format&n=pk96p0t2gChABUbF&q=85&s=032e3f1e4baa04d57256b5e1748094e2" alt="check overview visual stability graph" width="2742" height="960" data-path="images/docs/images/monitoring/check-overview-visual-stability.png" />

For API checks, a detailed response time breakdown is shown:
<img src="https://mintcdn.com/checkly-422f444a/pk96p0t2gChABUbF/images/docs/images/monitoring/check-overview-performance-api.png?fit=max&auto=format&n=pk96p0t2gChABUbF&q=85&s=0d57522314e2817aa2cd6daa0a75e3c3" alt="check overview api performance graph" width="2738" height="1178" data-path="images/docs/images/monitoring/check-overview-performance-api.png" />

For Multistep checks, a response time breakdown is shown per step:
<img src="https://mintcdn.com/checkly-422f444a/pk96p0t2gChABUbF/images/docs/images/monitoring/check-overview-performance-multistep.png?fit=max&auto=format&n=pk96p0t2gChABUbF&q=85&s=bac540945761ad06c2b021d364299758" alt="check overview multistep performance graph" width="1056" height="694" data-path="images/docs/images/monitoring/check-overview-performance-multistep.png" />

A performance comparison by location will also be included for both types of check:
<img src="https://mintcdn.com/checkly-422f444a/pk96p0t2gChABUbF/images/docs/images/monitoring/check-overview-locations.png?fit=max&auto=format&n=pk96p0t2gChABUbF&q=85&s=af408206b97257da25341146d38f3bf6" alt="check overview location performance graph" width="2732" height="500" data-path="images/docs/images/monitoring/check-overview-locations.png" />

## Navigating individual check results

The check result page will contain results from multiple locations when using [parallel scheduling](/monitoring/global-locations/#scheduling-strategies). Navigate between each location using the sidebar.
<img src="https://mintcdn.com/checkly-422f444a/pk96p0t2gChABUbF/images/docs/images/monitoring/location-select.gif?s=689a108e7d02ca758739457e669975da" alt="Viewing multiple attempts from the dropdown" width="1414" height="590" data-path="images/docs/images/monitoring/location-select.gif" />

To learn more about the results shown for each check type, refer to the documentation for the specific monitor:

* [API checks](/detect/synthetic-monitoring/api-checks/overview#api-check-results)
* [Browser checks](/detect/synthetic-monitoring/browser-checks/overview#browser-check-results)
* [Multistep checks](/detect/synthetic-monitoring/multistep-checks/overview#multistep-check-results)
* [Heartbeat monitors](/detect/uptime-monitoring/heartbeat-monitors/overview#heartbeat-monitor-results)
* [TCP monitors](/detect/uptime-monitoring/tcp-monitors/overview#tcp-monitor-results)
* [DNS monitors](/detect/uptime-monitoring/dns-monitors/overview#dns-monitor-results)
* [ICMP monitors](/detect/uptime-monitoring/icmp-monitors/overview#icmp-monitor-results)
* [URL monitors](/detect/uptime-monitoring/url-monitors/overview#url-monitor-results)

## Check results with retries

When checks are retried, a dropdown will indicate that the check result contains multiple check runs:

1. The initial failed attempt
2. The final result (which may have failed or succeeded)

When selecting a check run, all data and assets are available for inspection for each attempt.

<img src="https://mintcdn.com/checkly-422f444a/pk96p0t2gChABUbF/images/docs/images/monitoring/check-retries.gif?s=c1a11f52d3ebeeb962c20e95cbd9541e" alt="Viewing multiple attempts from the dropdown" width="1396" height="372" data-path="images/docs/images/monitoring/check-retries.gif" />


Built with [Mintlify](https://mintlify.com).