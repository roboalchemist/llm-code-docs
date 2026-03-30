# Source: https://firebase.google.com/docs/crashlytics/cloud-logging-what-can-you-do.md.txt

<br />

After you export your Crashlytics and (optionally) Firebase sessions data
into Cloud Logging, you can start working with the data to
[better understand the stability of your app](https://firebase.google.com/docs/crashlytics/cloud-logging-what-can-you-do#better-understand-app)
and even
[use logs in other Google Cloud services](https://firebase.google.com/docs/crashlytics/cloud-logging-what-can-you-do#logs-in-other-cloud-services)
to build custom dashboards, set up custom alerts, and analyze your data.

You can also
[export the data to other services](https://docs.cloud.google.com/bigquery/docs/export-intro).

Here are some common use cases for working with your data:

- **Create log-based metrics for advanced analysis**   

  Turn your log entries into metrics that track specific app behaviors or
  stability trends over time.
  For example, you can create a metric to count how often a specific non-fatal
  exception occurs and visualize it alongside other system health metrics.

- **Set up advanced alerts for custom notification channels**   

  Go beyond default email alerts by setting up custom *alerting policies* in
  Cloud Monitoring.
  Trigger notifications based on specific log patterns or thresholds and send
  them to services like Slack, Jira, or PagerDuty.

- **Build custom dashboards and charts**   

  Use Cloud Monitoring to create personalized dashboards that highlight the
  metrics most important to your business.
  You can visualize crash-free rates, session volumes, and error counts in a
  single view combined with other Google Cloud product data.

- **Correlate app crashes with backend logs**   

  Integrate your client-side crash data with your server-side logs in one place.

- **Search and filter raw crash data at scale**   

  Use the Logs Explorer to run complex queries using
  LQL (Logging Query Language).
  You can search for specific log messages, custom keys, or breadcrumbs across
  all your users and versions to find rare or device-specific issues.

- **Route data for long-term retention or external processing**   

  Use log sinks to export your Crashlytics logs to Cloud Storage for
  compliance, BigQuery for massive-scale analytics, or
  Pub/Sub to stream data into your own external monitoring tools.

## Better understand the stability of your app

The
[Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface)
in the Google Cloud console offers tools to view your specific logs and data
using queries and built-in filters and data panels. Learn more about filtering
your logs with queries in the next section below.

While the Crashlytics dashboard provides a high-level overview of your app's
health, exporting to Cloud Logging lets you answer more granular questions
about your app's behavior:

- ***How does a specific crash correlate with backend activity?***   

  Use a common identifier (like a user ID or request ID) to see exactly what was
  happening on your servers at the moment a client-side crash occurred.

- ***What is the crash-free session rate for a specific geographic region?***   

  By joining Crashlytics events with Firebase sessions data, you can
  calculate advanced metrics that aren't available in the standard dashboard.

- ***Are certain device models experiencing a higher volume of non-fatal errors
  after a new rollout?***   

  Filter raw logs by `device.model` and `error_type` to identify
  hardware-specific regressions in real-time.

- ***What was the exact sequence of events leading up to a crash?***   

  Inspect the `breadcrumbs` and `logs` fields within a log entry to see the
  timestamped trail of user actions and system events that preceded a failure.

- ***How many users are impacted by a specific "out of memory" error in the
  latest version?***   

  Run a query across all logs to find the count of unique `installation_uuid`
  values associated with a specific exception type.

- ***Is a particular feature causing more crashes than others?***   

  If you use [custom keys](https://firebase.google.com/docs/crashlytics/customize-crash-reports#add-keys)
  to track feature flags or app states, then you can filter your logs to see if
  a specific key-value pair is disproportionately represented in crash events.

## Use logs in other Google Cloud services

You can also use your logs in other Google Cloud services, like
Cloud Monitoring or BigQuery.

### Cloud Monitoring

Using [Cloud Monitoring](https://cloud.google.com/monitoring),
you can use log-based metrics based on your exported data to do any of the
following:

- [Create charts](https://docs.cloud.google.com/monitoring/charts/metrics-explorer)
  and
  [build custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards).

- Set up and send
  [custom alerts to custom notification channels](https://firebase.google.com/docs/crashlytics/alerts-advanced).

#### How to access Cloud Logging data in Cloud Monitoring

Since Cloud Logging and Cloud Monitoring are both part of the
[Google Cloud Observability Suite](https://cloud.google.com/products/operations),
you can start using your data stored in Cloud Logging directly with
Cloud Monitoring without needing to export it.

### BigQuery

Using [BigQuery](https://cloud.google.com/bigquery),
you can do any of the following:

- Use Looker Studio to build custom dashboards of your
  exported data.
  Learn more about Looker Studio in their
  [welcome guide](https://cloud.google.com/looker/docs/studio).

- Run queries on your Crashlytics data and (optionally) Firebase sessions
  data to to generate custom reports and summaries.

- Combine your Crashlytics data with other Firebase data that you exported
  to BigQuery and query it in new ways.

#### How to access Cloud Logging data in BigQuery

To start using your exported data stored in Cloud Logging with
BigQuery, you need to make it accessible to BigQuery. Use one
of the following options:

- Join BigQuery and Cloud Logging data using
  [linked datasets](https://docs.cloud.google.com/logging/docs/analyze/query-linked-dataset).

- Export data stored in Cloud Logging into BigQuery using
  [log sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

> [!IMPORTANT]
> **Important:** The dataset schema when you export Crashlytics data or Firebase sessions data from Cloud Logging into BigQuery using log sinks is very different from the dataset schema when you [directly export data to BigQuery](https://firebase.google.com/docs/crashlytics/bigquery-export).   
> Note that this means that you can't directly use the example queries or the premade Looker Studio template for Crashlytics data exported directly to BigQuery, but you can use them for inspiration.