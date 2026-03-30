# Source: https://firebase.google.com/docs/crashlytics/cloud-logging-export.md.txt

<br />

You can export your Firebase Crashlytics data into
[Cloud Logging](https://cloud.google.com/logging).
Once the data is exported, it's also available to the full Google Cloud Observability Suite,
where you can
[filter your logs](https://firebase.google.com/docs/crashlytics/cloud-logging-filtering-and-log-based-metrics#filter-logs-with-queries),
[build custom dashboards](https://firebase.google.com/docs/crashlytics/cloud-logging-custom-dashboards),
[set up custom alerts](https://firebase.google.com/docs/crashlytics/cloud-logging-custom-alerts),
and even
[export the data to other services](https://docs.cloud.google.com/bigquery/docs/export-intro).
Check out
[What can you do with your data?](https://firebase.google.com/docs/crashlytics/cloud-logging-what-can-you-do)
for a comprehensive list and examples for working with data stored in
Cloud Logging.

This page describes how to set up export of Crashlytics and (optionally)
Firebase sessions data into Cloud Logging.

## Set up export to Cloud Logging

<br />

1. In the Firebase console, go to the
   [**Integrations** page](https://console.firebase.google.com/project/_/settings/integrations).

2. In the **Cloud Logging** card, click **Link**.

3. Follow the on-screen instructions to set up export to Cloud Logging,
   including the following options:

   - *(Enabled by default)* To improve understanding of crash-free metrics,
     [enable Firebase sessions data export](https://firebase.google.com/docs/crashlytics/cloud-logging-export#enable-sessions-export).

   - Choose which apps will export logs.

     If you already have one or more active apps, the linking workflow displays
     an estimated data usage level for logs from each of your apps. This value
     is estimated based on the volume of Crashlytics data from the previous
     30 days.

<br />

#### *(Optional)* Enable Firebase sessions data export

<br />

> [!NOTE]
> **Note:** Only versions of your app using *at minimum* the following Crashlytics SDK versions will export sessions data to Cloud Logging:  
> Apple platforms: v10.8.0+ \| Android: v18.6.0+ (BoM v32.6.0+) \| Flutter: v3.4.5+ \| Unity: 11.7.0+

This option can also be enabled during the initial setup of export to
Cloud Logging.

1. In the Firebase console, go to the
   [**Integrations** page](https://console.firebase.google.com/project/_/settings/integrations).

2. In the **Cloud Logging** card, click **Manage**.

3. Select the **Include sessions** checkbox.

This action enables export of session data for all of your linked apps.

<br />

<br />

### Unlink from Cloud Logging

Unlinking from Cloud Logging stops any new logs from being exported.

<br />

Be aware of the following:

- Any data already exported into Cloud Logging will persist for the allowed
  retention time, and storage charges may still apply. You can manually delete
  your logs to prevent any further billing.

- If you have Cloud Logging data stored in other services (like
  BigQuery), that data might be governed by different terms for data
  persistence.

You can unlink from Cloud Logging at the Firebase
project level, at the Crashlytics product-level, or at the app-level.

> [!CAUTION]
> **Caution:** Unlinking your Firebase project from Cloud Logging stops ***all*** data export from any Firebase product for which you've set up export to Cloud Logging (except Cloud Functions for Firebase).

**Here's how to unlink from Cloud Logging:**

1. In the Firebase console, go to the
   [**Integrations** page](https://console.firebase.google.com/project/_/settings/integrations).

2. In the **Cloud Logging** card, click **Manage**.

3. Choose to unlink Crashlytics entirely or to
   unlink a specific app.

   To unlink your Firebase project entirely, find the button at the bottom of
   the page.
4. When prompted, confirm that you want to stop exports.

<br />

*** ** * ** ***

## What happens after you enable export?

- View logs for any new events within a few minutes of Crashlytics
  receiving the event.

- Monitor your data usage levels:

  - View the data usage level for logs from your linked apps in the
    [*Cloud Logging* integration card](https://console.firebase.google.com/project/_/settings/integrations/cloudlogging)
    in the Firebase console.

  - View your current and previous month's data usage in the
    [*Logs Storage* page](https://docs.cloud.google.com/logging/docs/store-log-entries)
    in the Google Cloud console.

<br />

*** ** * ** ***

## Quotas and pricing

Cloud Logging offers a no-cost level of usage per month (per project).
The usage can be from any Google or Firebase product using Cloud Logging. You
can upgrade your project to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) to unlock additional
paid usage and features. Learn more about
[pricing for Cloud Logging](https://cloud.google.com/stackdriver/pricing).

You can monitor and manage Cloud Logging and billing:

- Estimate your Cloud Logging bills using the
  [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator).

- Throttle logs by creating
  [exclusion filters for log sinks](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions).

- Set up
  [alerts](https://docs.cloud.google.com/stackdriver/docs/observability/pricing-optimize-and-monitor#monitor)
  to help control costs.

Logs are automatically deleted after 30 days, with the option to set
[custom retention](https://docs.cloud.google.com/logging/docs/buckets#custom-retention).

Note that the log entry for a particular request or event may be delayed or, in
rare cases, dropped. While logs can be used to understand requests or events,
they may not reflect the true usage that appears in your project usage and
billing.

<br />

*** ** * ** ***

## What's next?

- Learn how to
  [filter your logs](https://firebase.google.com/docs/crashlytics/cloud-logging-filtering-and-log-based-metrics#filter-logs-with-queries)
  to view specific information and costs for data storage and further analysis.

- View and build
  [log-based metrics](https://firebase.google.com/docs/crashlytics/cloud-logging-filtering-and-log-based-metrics#log-based-metrics),
  then use these metrics in Cloud Monitoring to do any of the following:

  - [Create charts](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

  - [Build custom dashboards.](https://firebase.google.com/docs/crashlytics/cloud-logging-custom-dashboards)

  - [Set up and send custom alerts to custom notification channels.](https://firebase.google.com/docs/crashlytics/cloud-logging-custom-alerts)

- Learn about the
  [log schema for exported data](https://firebase.google.com/docs/crashlytics/cloud-logging-schema).