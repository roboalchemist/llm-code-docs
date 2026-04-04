# Source: https://firebase.google.com/docs/storage/monitor-storage.md.txt

# Monitor Cloud Storage activity

<br />

<br />

> [!CAUTION]
> **If you have an `*.appspot.com` default bucket,** your Firebase project must be upgraded to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) by **February 03, 2026** to maintain access to your default bucket. [Learn more.](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024)

As part of managing your Firebase projects, you'll want to review usage of
Cloud Storage (for example, how many Bytes are being stored, how many
download requests are coming from your apps).

To review your Cloud Storage billed usage, check the
[*Usage and Billing* dashboard](https://console.firebase.google.com/project/_/usage).

For resource usage, both the Cloud Storage **Usage** tab in the
Firebase console and the metrics available through Cloud Monitoring can
help you monitor Cloud Storage usage. This kind of monitoring can help
you spot potential problems in your app. Looking at your app's usage can also
give you insight into your bill. Additionally, if something seems off, getting a
clear picture of your Cloud Storage bucket's operations (for example, by
monitoring evaluation of Cloud Storage Security Rules) can be a helpful for
troubleshooting.

## Firebase console

The Firebase console includes a usage dashboard that shows Storage Bytes
stored, object count, bandwidth, and download requests over time. Storage
metrics (Bytes stored and object count) are updated within 24 hours. Usage
metrics (bandwidth and download requests) are updated every few hours.

[Go to the Usage page](https://console.firebase.google.com/project/_/storage/usage)

> [!NOTE]
> **Note:** As a result of how the dashboard computes usage, the numbers reported can differ slightly from billing reports. The billing reports are the final usage numbers.

![The Cloud Storage Usage dashboard in the Firebase console.](https://firebase.google.com/docs/storage/images/storage-usage-console-view_grey.png)

<br />

Additionally, the Firebase console provides a Firebase Security Rules evaluation dashboard,
a useful, at-a-glance view of rules invocations. You can also monitor Firebase Security Rules
usage through [Cloud Monitoring](https://firebase.google.com/docs/firestore/monitor-usage#cloud-monitoring).
This provides the same rule evaluation metrics,
along with the ability to build custom dashboards, analyze trends, and configure
alerts (for example, when denied requests spike).
See the [Cloud Monitoring metrics reference](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-firestore) for the complete
list of available metrics.

[Go to the Rules page](https://console.firebase.google.com/project/_/storage/rules)

![The Cloud Storage Rules dashboard in the Firebase console.](https://firebase.google.com/docs/storage/images/storage_rules_monitor.png)

## Google Cloud console

Since a Firebase project is just a Google Cloud project with Firebase services
and configurations added, you can view your project in the
Google Cloud console.

If you have a default Cloud Storage bucket with the name format
`*.appspot.com`, then its usage can be viewed in the
**App Engine Quotas** page in the Google Cloud console. This page tracks daily
storage usage information including Bytes stored, object counts, bandwidth used,
and download requests.

![Cloud Storage usage in the Google App Engine Quotas page.](https://firebase.google.com/docs/storage/images/storage-quotas-view.png)

## Cloud Monitoring

[Cloud Monitoring](https://cloud.google.com/monitoring/docs/) collects
metrics, events, and metadata from Google Cloud products that you can use to
create dashboards, charts, and alerts. Cloud Monitoring includes the
following Security Rules-related Cloud Storage metrics:

| Metric Name | Description |
|---|---|
| Rule evaluations | The number of Cloud Storage Security Rules evaluations performed in response to write or read requests. You can break this metric down by the result of the request (ALLOW, DENY, or ERROR) or the bucket name. |

Sampling rate
:   The Cloud Storage metrics are sampled every 60 seconds, but updates may take up to 4 minutes to show up in your dashboards.

Using these metrics, you can set up a Cloud Storage dashboard like the
following:

![Cloud Storage usage in a Cloud Monitoring dashboard.](https://firebase.google.com/docs/storage/images/storage-stackdriver-rule-metrics-view.png)

Complete the steps below to start monitoring Cloud Storage with
Cloud Monitoring.

### Create a Cloud Monitoring workspace

To monitor Firebase with Cloud Monitoring, you must set
up a workspace for your project. A workspace organizes
monitoring information from one or more projects. After setting up a workspace,
you can create custom dashboards and alerting policies.

1. [Open the Cloud Monitoring Page](https://console.cloud.google.com/monitoring/)

   If your project is already part of a workspace, the Cloud Monitoring Page
   opens. Otherwise, select a workspace for your project.
2. Select the **New Workspace** option or select an existing workspace.

3. Click **Add**. After your workspace builds, the Cloud Monitoring Page opens.

### Create a dashboard and add a chart

Display the Firebase metrics collected from
Cloud Monitoring in your own charts and dashboards.

Before you proceed, make sure your project is part of a
[Cloud Monitoring workspace](https://firebase.google.com/docs/storage/monitor-storage#stackdriver-setup).

1. In the Cloud Monitoring Page, open your workspace and go to the
   **Dashboards** page.

   [Go to the Dashboards page](https://console.cloud.google.com/monitoring/dashboards)
2. Click **Create Dashboard** and enter a dashboard name.

3. In the upper-right hand corner, click **Add Chart**.

4. In the **Add Chart** window, enter a chart title. Click the **Metric** tab.

5. In the **Find resource type and metric** field, enter **Cloud Storage for Firebase** . From the auto-populated dropdown, select one of the Cloud Storage metrics..

6. To add more metrics to the same chart, click **Add Metric** and repeat the previous step.

7. Optionally, tailor your chart as needed. For example, in the **Filter** field, click **+ Add a filter**. Scroll down, then select a value or range for the metric of interest you wish to filter the chart on.

8. Click **Save**.

For more on Cloud Monitoring charts,
see [Working with charts](https://cloud.google.com/monitoring/charts/).

### Create an alerting policy

You can create an alerting policy based on the Firebase metrics.
Follow the steps below can create an alerting policy that emails you whenever a
specific Firebase metric meets a certain threshold.

Before you proceed, make sure your project is part of a
[Cloud Monitoring workspace](https://firebase.google.com/docs/storage/monitor-storage#stackdriver-setup).

1. In the Cloud Monitoring Page, open your workspace, and go to
   the **Alerting** page.

   [Go to the Create New Alerting Policy page](https://console.cloud.google.com/monitoring/alerting)
2. Click **Create Policy**.

3. Enter a name for your alerting policy.

4. Add an alerting condition based on one of the Firebase metrics.
   Click **Add Condition**.

5. Select a **Target** . In the **Find resource type and metric** field, enter **Cloud Storage for Firebase** . From the auto-populated dropdown, select one of the Cloud Storage metrics.

6. Under **Policy triggers**, use the dropdown fields to define your alerting
   condition.

7. Add a notification channel to your alerting policy. Under **Notifications** ,
   Click **Add Notification Channel** . Select **Email** from the dropdown menu.

8. Enter your email in the **Email address** field. Click **Add**.

9. Optionally, fill out the documentation field to include additional information
   in your email notification.

10. Click **Save**.

If your Cloud Storage usage exceeds the configured threshold, you
will receive an email alert.

For more on alerting policies, see
[Introduction to alerting](https://cloud.google.com/monitoring/alerts/).

## What's next

- [Learn more about Cloud Monitoring.](https://cloud.google.com/monitoring/docs/)