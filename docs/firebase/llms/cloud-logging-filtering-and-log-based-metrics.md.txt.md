# Source: https://firebase.google.com/docs/crashlytics/cloud-logging-filtering-and-log-based-metrics.md.txt

<br />

Once your Crashlytics data and (optionally) Firebase sessions data is
exported to Cloud Logging, you can
[filter your logs](https://firebase.google.com/docs/crashlytics/cloud-logging-filtering-and-log-based-metrics#filter-logs-with-queries) and
[create log-based metrics](https://firebase.google.com/docs/crashlytics/cloud-logging-filtering-and-log-based-metrics#log-based-metrics). Both of these are
helpful for viewing, using, and analyzing specific data.

If you haven't already, make sure to check out
[What can you do with your data?](https://firebase.google.com/docs/crashlytics/cloud-logging-what-can-you-do)
for a comprehensive list and examples for working with data stored in
Cloud Logging.

## Filter your logs with queries

Filtering your logs is helpful for viewing specific data as well as to reduce
costs for data storage and further analysis. You filter logs using
[LQL (Logging Query Language)](https://docs.cloud.google.com/logging/docs/view/building-queries).

To learn about how to filter your logs with queries, visit
[Sample queries using Logs Explorer](https://docs.cloud.google.com/logging/docs/view/query-library)
and
[Building log queries](https://docs.cloud.google.com/logging/docs/view/building-queries).
The table below describes the fields available for those queries.

> [!TIP]
> **Tip:** You can **use Gemini directly within the Google Cloud console** to help you write these queries if you're not yet familiar with LQL.

### Example filters

For Crashlytics, here are some example initial filters for a query:

- Find all fatal crashes for a specific app version:

  ```
  logName="projects/PROJECT_ID/logs/firebasecrashlytics.googleapis.com%2Fevents"
  jsonPayload.issue.errorType="FATAL"
  jsonPayload.version.displayVersion="3.2.0"
  ```
- Identify crashes occurring on a specific device model (for example, Pixel 6a):

  ```
  logName="projects/PROJECT_ID/logs/firebasecrashlytics.googleapis.com%2Fevents"
  jsonPayload.device.model="Pixel 6a"
  ```
- Search for a specific `OutOfMemoryError` across all fatal events:

  ```
  logName="projects/PROJECT_ID/logs/firebasecrashlytics.googleapis.com%2Fevents"
  jsonPayload.issue.errorType="FATAL"
  jsonPayload.issue.subtitle="java.lang.OutOfMemoryError"
  ```
- Find events for a specific Crashlytics issue ID:

  ```
  logName="projects/PROJECT_ID/logs/firebasecrashlytics.googleapis.com%2Fevents"
  jsonPayload.issue.id="ISSUE_ID"
  ```

### Log schema

Each log entry has a predefined structure and queryable fields (see
[LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)).

Learn about the
[log schema for exported data](https://firebase.google.com/docs/crashlytics/cloud-logging-schema),
including
[Crashlytics data](https://firebase.google.com/docs/crashlytics/cloud-logging-schema#crashlytics),
[Firebase sessions data](https://firebase.google.com/docs/crashlytics/cloud-logging-schema#sessions),
and
[device logs](https://firebase.google.com/docs/crashlytics/cloud-logging-schema#device-log).

## Create log-based metrics

You can view and build
[log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics),
and then use these metrics in Cloud Monitoring to create
charts, custom dashboards, and custom alerts.

- Use
  [predefined system metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics#system-defined_metrics)
  that are automatically recorded, such as the number of logging events that
  occurred within a specific time period.

- Create
  [user-defined metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics#user-defined_metrics)
  for your project. You can count the number of log entries that match a given
  query or keep track of particular values with the matching log entries. You
  can filter using regular expressions. Make sure to review
  [pricing for user-defined metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics#user-lbm-pricing).

- Use
  [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs)
  to record the number of log entries containing particular messages or extract
  latency information reported in log entries. You can then use these metrics in
  charts and custom alerts.

### Example log-based metrics

Here are two example user-defined log-based metrics that you could create from
your exported Crashlytics and Firebase sessions data:

- Using Crashlytics data:  

  Create a metric named `firebase/crashlytics_events`
  with a label of `errorType`,
  and define it as:

  `logName="projects/PROJECT_ID/logs/firebasecrashlytics.googleapis.com%2Fevents"`
- Using Firebase sessions data:  

  Create a metric named `firebase/session_events`
  with a label of `eventType`,
  and define it as:

  `logName="projects/PROJECT_ID/logs/firebasecrashlytics.googleapis.com%2Fsession_events"`

## What's next?

- [Create temporary charts to quickly visualize data.](https://docs.cloud.google.com/monitoring/charts/metrics-explorer)

- [Build custom dashboards for longer-term and advanced monitoring.](https://firebase.google.com/docs/crashlytics/cloud-logging-custom-dashboards)

- [Set up and send custom alerts to custom notification channels.](https://firebase.google.com/docs/crashlytics/cloud-logging-custom-alerts)