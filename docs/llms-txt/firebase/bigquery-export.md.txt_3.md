# Source: https://firebase.google.com/docs/crashlytics/bigquery-export.md.txt

You can export your Firebase Crashlytics data into
[BigQuery](https://cloud.google.com/bigquery).
Once the data is in BigQuery, you can
[analyze the data using SQL queries](https://firebase.google.com/docs/crashlytics/bigquery-run-queries),
[build data visualizations and custom dashboards](https://firebase.google.com/docs/crashlytics/bigquery-custom-dashboards),
and even
[export the data to other services](https://docs.cloud.google.com/bigquery/docs/export-intro).

This page describes how to set up export of Crashlytics and (optionally)
Firebase sessions data into BigQuery.

## Set up export to BigQuery

> [!NOTE]
> **Note:** Make sure that you have the [required level of access](https://firebase.google.com/docs/projects/bigquery-export#permissions-and-roles) to view or manage settings for data export to BigQuery.

1. In the Firebase console, go to the
   [**Integrations** page](https://console.firebase.google.com/project/_/settings/integrations).

2. In the **BigQuery** card, click **Link**.

3. Follow the on-screen instructions to set up export to BigQuery,
   including the following options:

   - To improve understanding of crash-free users and crash-free sessions,
     [enable Firebase sessions data export](https://firebase.google.com/docs/crashlytics/bigquery-export#enable-sessions-export).

   - To get near realtime access to your Crashlytics data and
     Firebase sessions data in BigQuery,
     [enable streaming export](https://firebase.google.com/docs/crashlytics/bigquery-export#enable-streaming).

<br />

#### *(Optional)* Enable Firebase sessions data export

<br />

> [!NOTE]
> **Note:** To export sessions data into BigQuery, your app must use *at minimum* the following versions of the Crashlytics SDK:  
> Apple platforms: v10.8.0+ \| Android: v18.6.0+ (BoM v32.6.0+) \| Flutter: v3.4.5+ \| Unity: 11.7.0+

This option can also be enabled during the initial setup of export to
BigQuery.

1. In the Firebase console, go to the
   [**Integrations** page](https://console.firebase.google.com/project/_/settings/integrations).

2. In the **BigQuery** card, click **Manage**.

3. Select the **Include sessions** checkbox.

This action enables export of session data for all of your linked apps. If you
have streaming export enabled, this will start exporting session data in
realtime as well.

<br />

<br />

<br />

#### *(Optional)* Enable streaming export

<br />

> [!NOTE]
> **Note:** Streaming export isn't available if your project is on the Spark pricing plan or using [BigQuery sandbox](https://cloud.google.com/bigquery/docs/sandbox) (no-cost access to BigQuery).

Learn about the
[Benefits of streaming export to BigQuery](https://firebase.google.com/docs/crashlytics/bigquery-export#streaming-export) later on
this page.

This option can also be enabled during the initial setup of export to
BigQuery.

1. In the Firebase console, go to the
   [**Integrations** page](https://console.firebase.google.com/project/_/settings/integrations).

2. In the **BigQuery** card, click **Manage**.

3. Select the **Include streaming** checkbox.

This action enables streaming for all of your linked apps. If you have
Firebase sessions export enabled, this will enable streaming export for session
data as well.

<br />

<br />

### Unlink from BigQuery

Unlinking from BigQuery stops the corresponding dataset(s) in
BigQuery from being populated.

Be aware of the following:

- Any data already exported into BigQuery will persist for the allowed
  retention time, and storage and query charges may still apply. You can
  manually delete your dataset(s) to prevent any further billing.

- If you have BigQuery data stored in other services, that data might
  be governed by different terms for data persistence.

You can unlink from BigQuery at the Firebase project level, at the
product-level, or at the app-level for a specific product.

> [!CAUTION]
> **Caution:** Unlinking your Firebase project from BigQuery stops ***all*** data export from any Firebase product (and if applicable, Google Analytics) for which you've set up export to BigQuery.

**Here's how to unlink from BigQuery:**

1. In the Firebase console, go to the
   [**Integrations** page](https://console.firebase.google.com/project/_/settings/integrations).

2. In the **BigQuery** card, click **Manage**.

3. Choose to unlink a specific product or to unlink specific apps for
   a specific product.

   To unlink your Firebase project entirely, find the button at the bottom of
   the page.
4. When prompted, confirm that you want to stop exports.

<br />

*** ** * ** ***

## What happens when you enable export?

- **Firebase exports data from the apps linked to BigQuery.**

  - During setup, by default, all apps in your project are linked to
    BigQuery, but you can select to *not* link specific apps during
    setup.

  - Any apps that you later add to your Firebase project are automatically
    linked to BigQuery.

  - At any time, you can
    [manage which apps export data](https://support.google.com/firebase/answer/6318765#manage).

- **Firebase exports data to the dataset location you selected during setup.**

  - This location applies to both the Crashlytics dataset and the
    Firebase sessions dataset (if sessions data is enabled for export).

  - This location is only applicable for the data exported into
    BigQuery, and it does not impact the location of data stored for
    use in the Crashlytics dashboard of the Firebase console or in
    Android Studio.

  - After a dataset is created, its location can't be changed, but you can
    copy the dataset to a different location or manually move (recreate) the
    dataset in a different location. To learn more, see
    [Change the location for existing exports](https://firebase.google.com/docs/projects/bigquery-export#change-dataset-location).

- **Firebase sets up daily syncs of your batch data to BigQuery.**

  - After linking to BigQuery, it may take up to 48 hours for the
    *initial* batch data export.

  - The daily sync happens once per day, regardless of any scheduled export
    that you might have set up in BigQuery. Note that the timing and
    duration of the sync job can change, so we don't recommend scheduling
    downstream operations or jobs based on a specific timing of the export.

- **Firebase
  [exports a copy of your existing data](https://firebase.google.com/docs/crashlytics/bigquery-dataset-schema)
  to BigQuery.**

  - For each linked app, this export includes a batch table containing the data
    from the daily sync.

  - You can
    [manually schedule data backfills](https://cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer)
    for the batch table up to the past 30 days *or* for the most recent date
    when you enabled export to BigQuery (whichever is most recent).

- **Firebase does the following if you
  [enable streaming export to BigQuery](https://firebase.google.com/docs/crashlytics/bigquery-export#streaming-export).**

  - Each linked app will also have its own realtime table containing constantly
    updating data (in addition to the app's batch table for daily batch export).

  - After enabling streaming, it may take up to 1 hour for data to begin
    streaming.

  <br />

  Are you not seeing data in your realtime table?

  <br />

  1. Make sure that you've sent at least two events from your app to
     Crashlytics and waited a couple minutes after sending them.

  2. Make sure your Firebase project is on the pay-as-you-go Blaze pricing plan.  

     You can check this by looking in the bottom-left corner of the
     [Firebase console](https://console.firebase.google.com/).

  3. If there's still no data in your realtime table after sending two events and
     waiting a couple minutes:

     1. Go to the
        [**BigQuery** card](https://console.firebase.google.com/project/_/settings/integrations)
        in the Firebase console.

     2. Disable and then re-enable streaming export.

     3. Make sure the service account
        `service-PROJECT_NUMBER@gcp-sa-crashlytics.iam.gserviceaccount.com`
        is in your Firebase project and has the
        *Firebase Crashlytics Service Agent* role.  

        You can check this in the *IAM* page of the
        [Google Cloud console](https://console.cloud.google.com/iam-admin/iam)
        (make sure to select the checkbox for
        **Include Google-provided role grants**).

     4. Send at least two events to Crashlytics and wait a couple minutes.

  4. If you still don't see data in your realtime table,
     [reach out to Firebase Support](https://firebase.google.com/support/troubleshooter/contact).

  <br />

  <br />

<br />

*** ** * ** ***

## Benefits of streaming export to BigQuery

By default, data is exported to BigQuery in a daily batch export.
Additionally, you can stream your Crashlytics data and Firebase sessions in
realtime with
[BigQuery streaming](https://cloud.google.com/bigquery/streaming-data-into-bigquery).
You can use streamed data for any purpose that requires live data, such as
presenting information in a live dashboard, watching a rollout live, or
monitoring application problems that trigger alerts and custom workflows.

> [!NOTE]
> **Note:** Streaming export isn't available if your project is on the Spark pricing plan or using [BigQuery sandbox](https://cloud.google.com/bigquery/docs/sandbox) (no-cost access to BigQuery).

When you enable streaming export to BigQuery, you'll also have
realtime tables (in addition to batch tables). Both types of tables will have
the same [dataset schema](https://firebase.google.com/docs/crashlytics/bigquery-dataset-schema),
but here some important differences between batch tables and realtime tables:

| **Batch table** | **Realtime table** |
|---|---|
| - Data is exported once daily. - Events are durably stored before batch writing to BigQuery. - Data can be [backfilled](https://cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer) up to 30 days prior\*. | - Data is exported in realtime. - No backfilling is available. |

The batch table is ideal for long-term analysis and identifying trends over time
because we durably store events before writing them, and they can be backfilled
to the table for up to 30 days\*. When we write data to your realtime table, we
immediately write it to BigQuery, and so it is ideal for live
dashboards and custom alerts. These two tables can be
[combined with a stitching query](https://firebase.google.com/docs/crashlytics/bigquery-work-with-data#example-top-5-issues-since-date)
to get the benefits of both.

By default, the realtime table has a partition expiration time of 30 days. To
learn how to modify this, see
[Set the partition expiration](https://cloud.google.com/bigquery/docs/managing-partitioned-tables#partition-expiration)
in the BigQuery documentation.

^**\*** *Backfills are supported for up to the past 30 days **or** for
the most recent date when you enabled export to BigQuery (whichever is
most recent).*^

<br />

*** ** * ** ***

## Pricing and the BigQuery sandbox

If your Firebase project is on the no-cost Spark pricing plan, you can use the
[BigQuery sandbox](https://cloud.google.com/bigquery/docs/sandbox),
which provides no-cost access to BigQuery. For information about the
BigQuery sandbox and its capabilities, see
[Using the BigQuery sandbox](https://cloud.google.com/bigquery/docs/sandbox#limits).

If your Firebase project is on the pay-as-you-go Blaze pricing plan, you can use all the
features of BigQuery. Your use of BigQuery is subject to
[BigQuery pricing](https://cloud.google.com/bigquery/pricing),
which includes limited no-cost use.

<br />

*** ** * ** ***


## What's next?

- Review
  [example SQL queries](https://firebase.google.com/docs/crashlytics/bigquery-run-queries).

- [Build custom dashboards](https://firebase.google.com/docs/crashlytics/bigquery-custom-dashboards) using
  exported data and various Google Cloud services, like Looker Studio.

- Learn about the
  [dataset schema for exported data](https://firebase.google.com/docs/crashlytics/bigquery-dataset-schema).