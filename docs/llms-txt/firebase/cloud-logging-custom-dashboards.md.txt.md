# Source: https://firebase.google.com/docs/crashlytics/cloud-logging-custom-dashboards.md.txt

<br />

You can use your exported Crashlytics and (optionally) Firebase sessions
data in Cloud Logging to create custom dashboards.

## Create custom dashboards in the Logs Dashboard

After you've
[created log-based metrics](https://firebase.google.com/docs/crashlytics/cloud-logging-filtering-and-log-based-metrics#log-based-metrics)
for your exported data, you can visualize them on
[*custom dashboards* within Cloud Logging](https://docs.cloud.google.com/logging/docs/view/dashboard#custom_dashboard).

Note that Crashlytics does *not yet* have a predefined dashboard within
Cloud Logging.

1. Make sure that you've created at least one
   [log-based metric](https://firebase.google.com/docs/crashlytics/cloud-logging-filtering-and-log-based-metrics#log-based-metrics)
   for your exported data.

2. In the Google Cloud console, select
   **Logging \> [Dashboards](https://console.cloud.google.com/monitoring/dashboards/resourceList/logs)**.

3. Click **Create custom dashboard**.

4. Add charts to your dashboard:

   1. Click **Add widget**.

   2. From the **Metric** drop-down, select the log-based metric you
      previously created.

   3. Configure the aggregation and display options as needed.

   4. Save the chart.

5. Arrange and resize charts to create your preferred dashboard layout.

6. Save the dashboard.

## Build charts and dashboards using Cloud Monitoring

After you've created
[log-based metrics](https://firebase.google.com/docs/crashlytics/cloud-logging-filtering-and-log-based-metrics#log-based-metrics)
for your exported data, you can use Cloud Monitoring to
[create charts](https://docs.cloud.google.com/monitoring/charts/metrics-explorer)
and
[build custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards).

Charts are temporary and let you quickly visualize your data in the
Metrics Explorer, while dashboards offer more permanent and powerful options for
longer-term and more advanced monitoring. You can even save a chart to a
custom dashboard.