# Source: https://firebase.google.com/docs/crashlytics/export-data-to-cloud.md.txt

<br />

Firebase Crashlytics and its dashboard in the Firebase console let you
explore and analyze stability data about your apps. The standard Crashlytics
features can help you with many of the tasks and goals involved with running
your app.

Sometimes, though, as your apps and business grow and become more complex,
**you might need answers to different types of questions, to analyze or join the
data in unique ways, or to build custom dashboards or custom alerts based
on your data.**

To help you do all this, Crashlytics offers **options for exporting your
data into powerful Google Cloud services: BigQuery and
Cloud Logging.** Check out
[What can you do with the exported data?](https://firebase.google.com/docs/crashlytics/export-data-to-cloud#what-can-you-do) for a more
comprehensive list of capabilities for these services.

- **BigQuery** : Analyze data using SQL queries, join data from other
  datasets, export data to another cloud provider, and build data visualizations
  and custom dashboards (for example, using Looker Studio).  

  [Set up export to BigQuery](https://firebase.google.com/docs/crashlytics/bigquery-export)

- **Cloud Logging** : Create log-based metrics for advanced analysis,
  set up advanced alerts for custom notification channels,
  build custom dashboards and charts with Cloud Monitoring, and more.  

  [Set up export to Cloud Logging](https://firebase.google.com/docs/crashlytics/cloud-logging-export)

This page describes in more detail how you can use your exported
Crashlytics data and (optionally) Firebase sessions data with these
Google Cloud services.

## What data is exported to each service?

Exports contain raw Crashlytics data (and optionally Firebase sessions data)
including device type, operating system, exceptions (Android apps) or errors
(Apple apps), and Crashlytics logs, as well as other associated metadata.

The data exported to each service is the same, but the structure is different.
For BigQuery, the data is in tables (see
[dataset schema](https://firebase.google.com/docs/crashlytics/bigquery-dataset-schema)), and for
Cloud Logging, the data is in log format (see
[log schema](https://firebase.google.com/docs/crashlytics/cloud-logging-schema)).

## What can you do with the exported data?

The following are highlights of what's possible when using these Google Cloud
services with Crashlytics data.
In the Google Cloud documentation, you can learn about all the capabilities of
[BigQuery](https://cloud.google.com/bigquery) and
[Cloud Logging](https://cloud.google.com/logging).

#### Data exported to BigQuery

- **Analyze data using SQL queries**   

  You can run queries on your Crashlytics data to generate custom reports
  and summaries. Since these types of custom reports aren't available in the
  Crashlytics dashboard of the Firebase console, they can supplement your
  analysis and understanding of crash data. We even provide you with a
  collection of [example queries](https://firebase.google.com/docs/crashlytics/bigquery-run-queries).

- **Join data from different datasets**   

  For example, if you choose to export Firebase sessions data when you set up
  Crashlytics data export, then you can improve understanding of crash-free
  users and crash-free sessions.
  Also, you can export data from various Firebase products (like Performance Monitoring) or
  from Google Analytics and then join and analyze that data in
  BigQuery with your Crashlytics data.

- **Create views**   

  Using the BigQuery UI, you can create a *view* , which is a virtual
  table defined by a SQL query. For detailed instructions about the different
  types of views and how to create them, see the
  [BigQuery documentation](https://cloud.google.com/bigquery/docs/views-intro).

- **Build data visualizations and custom dashboards**   

  For example, you can use a premade Crashlytics template to build a
  dashboard using Looker Studio.

#### Data exported to Cloud Logging

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

## When to choose BigQuery versus Cloud Logging?

At a high-level, here are some differences to consider when choosing where to
export your data.

|   | Data exported to BigQuery | Data exported to Cloud Logging |
|---|---|---|
| **Applicable business roles** | Ideal for data analyst roles, especially for joining data from multiple datasets. | Helpful for developers and SREs to set up custom alerts and dashboards, as well as to have easier connections to server-side monitoring data. |
| **Options for using the data with Google Cloud products** | - Looker Studio to [build custom dashboards](https://firebase.google.com/docs/crashlytics/bigquery-custom-dashboards#looker-studio-template). | - Cloud Logging to [build custom dashboards](https://firebase.google.com/docs/crashlytics/cloud-logging-custom-dashboards#other-options) - Cloud Monitoring to [build custom dashboards](https://firebase.google.com/docs/crashlytics/cloud-logging-custom-dashboards#dashboard-in-cloud-monitoring) and [set up custom alerts](https://firebase.google.com/docs/crashlytics/cloud-logging-custom-alerts) - Metrics Explorer to [create charts](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) |
| **Options for joining and further export of data** | - You can join BigQuery and Cloud Logging data using [linked datasets](https://docs.cloud.google.com/logging/docs/analyze/query-linked-dataset). - You *cannot* export data stored in BigQuery into Cloud Logging or Cloud Monitoring. - You can [export the data to another cloud provider](https://docs.cloud.google.com/bigquery/docs/export-intro). | - You can join BigQuery and Cloud Logging data using [linked datasets](https://docs.cloud.google.com/logging/docs/analyze/query-linked-dataset). - You can export data stored in Cloud Logging into BigQuery using a [log sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2). - You can [export the data to another cloud provider](https://docs.cloud.google.com/bigquery/docs/export-intro). |
| **Pricing** | You pay for both storage and querying. Learn more in [Export Crashlytics data to BigQuery](https://firebase.google.com/docs/crashlytics/bigquery-export#pricing). | You pay for storage, but not for querying. Learn more in [Export Crashlytics data to Cloud Logging](https://firebase.google.com/docs/crashlytics/cloud-logging-export#quotas-and-pricing). |

## What's next?

[Set up export to BigQuery](https://firebase.google.com/docs/crashlytics/bigquery-export)
[Set up export to Cloud Logging](https://firebase.google.com/docs/crashlytics/cloud-logging-export)

After you've set up export of Crashlytics and (optionally)
Firebase sessions data, start using the features of the Google Cloud services:

- For data exported to BigQuery, review
  [example queries](https://firebase.google.com/docs/crashlytics/bigquery-run-queries)
  and learn about the
  [dataset schema for exported data](https://firebase.google.com/docs/crashlytics/bigquery-dataset-schema).

- For data exported to Cloud Logging, learn
  [what you can do with your exported data](https://firebase.google.com/docs/crashlytics/cloud-logging-what-can-you-do),
  how to
  [filter and use log-based metrics](https://firebase.google.com/docs/crashlytics/cloud-logging-filtering-and-log-based-metrics),
  and how to
  [set up custom alerts for custom notification channels](https://firebase.google.com/docs/crashlytics/cloud-logging-custom-alerts).

- Build custom dashboards using various Google Cloud services.
  Learn about the options available via
  [BigQuery](https://firebase.google.com/docs/crashlytics/bigquery-custom-dashboards) or
  [Cloud Logging](https://firebase.google.com/docs/crashlytics/cloud-logging-custom-dashboards).