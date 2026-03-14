# Source: https://documentation.onesignal.com/docs/en/bigquery.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google BigQuery

> Export messaging event data to BigQuery and import custom events from BigQuery to trigger personalized campaigns.

export const PLATFORM_0 = "BigQuery"

export const DATA_TYPE_0 = "event table columns"

export const COLUMN_HEADER_0 = "BigQuery Column"

export const PROPERTIES_DESCRIPTION_0 = "Additional columns as JSON"

## Overview

The OneSignal + BigQuery integration supports two powerful data pipelines:

* **Export**: Automatically send messaging event data (push, email, SMS, in-app) from OneSignal to BigQuery for analysis and reporting.
* **Import**: Sync custom user events from your BigQuery datasets to OneSignal to trigger automated Journeys and personalized messaging.

Together, these integrations give you complete control over user engagement data—powering advanced analytics and real-time behavior-driven messaging.

***

## Export OneSignal events to BigQuery

Send messaging performance and engagement events (e.g., sends, opens, clicks) to BigQuery to:

* Build custom dashboards and reports
* Track delivery and engagement trends across channels
* Combine OneSignal data with other business data for analysis

**Requirements**

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

* Google Cloud Platform project with **billing enabled**
* BigQuery enabled in your GCP project
* Service account with BigQuery write permissions

**Setup Steps**

### 1. Create a Service Account

<Steps>
  <Step title="Log in to your Google Cloud Platform account">
    After you login, ensure the proper project is selected.

    <Frame>
      <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/7fe257f51fcacd15a07c4f4f23bf8bf2f9f22c2f1c171ad8b8648624de4de304-BQ1-2.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=038779c4d976ba56a17a32f2e6646573" width="2388" height="558" data-path="images/docs/7fe257f51fcacd15a07c4f4f23bf8bf2f9f22c2f1c171ad8b8648624de4de304-BQ1-2.png" />
    </Frame>
  </Step>

  <Step title="Create a service account">
    Visit the [Create Service Account page](https://console.cloud.google.com/iam-admin/serviceaccounts/create) and click **Create Service Account.**

    <Frame>
      <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/7fe257f51fcacd15a07c4f4f23bf8bf2f9f22c2f1c171ad8b8648624de4de304-BQ1-2.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=038779c4d976ba56a17a32f2e6646573" width="2388" height="558" data-path="images/docs/7fe257f51fcacd15a07c4f4f23bf8bf2f9f22c2f1c171ad8b8648624de4de304-BQ1-2.png" />
    </Frame>
  </Step>

  <Step title="Fill out the fields.">
    Give it any name and service account ID you choose.

    <Frame>
      <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/6437e9849e23f18ec6f90e03c3821817566e7f150125f440a58fbe5fd2b42e0b-BQ1-3.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=37236688a79f1c16c0d6fdad15b03245" width="1344" height="870" data-path="images/docs/6437e9849e23f18ec6f90e03c3821817566e7f150125f440a58fbe5fd2b42e0b-BQ1-3.png" />
    </Frame>
  </Step>

  <Step title="Assign the 'BigQuery User' role">
    Give the service account the "BigQuery User" role.

    <Frame>
      <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b1bff32d7f010b488b60347e01ecb1fbde182602f19f16d3d89914d1de1c0635-BQ1-4.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=1df75028d3632a3ed413c10c1de9b94a" width="549" height="395" data-path="images/docs/b1bff32d7f010b488b60347e01ecb1fbde182602f19f16d3d89914d1de1c0635-BQ1-4.png" />
    </Frame>
  </Step>

  <Step title="Create a JSON key for this account">
    Go to your new service account > **Keys** > **Add Key** > **Create new key** > select JSON. Save the file.
  </Step>
</Steps>

<Info>
  You’ll paste the entire contents of this JSON key file into OneSignal to activate the integration.
</Info>

### 2. Activate the Integration in OneSignal

<Steps>
  <Step title="Go to OneSignal > Data > Integrations > BigQuery" />

  <Step title="Paste your service account JSON key" />

  <Step title="Configure settings">
    * **Sync Frequency**: As often as every 15 minutes
    * **Dataset/Table Names**: Must only contain lowercase letters, numbers and underscores, and cannot begin with a number.
    * **Event Types**: Select specific message events (e.g., sent, opened, clicked)
      * **Note:** You can select multiple event types or update selected events at a later time.
  </Step>

  <Step title="Click Save and wait for confirmation" />
</Steps>

<Note>
  Initial data sync can take 15–30 minutes to appear in BigQuery.

  While you wait, send messages via push, email, in-app, or SMS to trigger the events selected.
</Note>

### 3. View Data in BigQuery

Open your BigQuery console and locate the dataset (e.g., `onesignal_events_<app-id>`) to explore synced message events.

<Frame caption="BigQuery dataset containing exported message events">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c40ec987eadef5dd1c16cb47fb71c2c666b30ea8667624584ecbc481c12ef026-BQ5.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=08cf57a8bd91f9447909ad619077935f" width="1552" height="1052" data-path="images/docs/c40ec987eadef5dd1c16cb47fb71c2c666b30ea8667624584ecbc481c12ef026-BQ5.png" />
</Frame>

## Message events and properties

### Message event kinds

**Property:** `event_kind`
**Type:** `String`

The kind of message and event (e.g. `message.push.received`, `message.push.sent`).

| Message Event (OneSignal) |           `event_kind`           | Description                                                                |
| :-----------------------: | :------------------------------: | -------------------------------------------------------------------------- |
|         Push Sent         |        `message.push.sent`       | Push notification successfully sent.                                       |
|       Push Received       |      `message.push.received`     | Delivered push (see [Confirmed Delivery](/docs/en/confirmed-delivery)).    |
|        Push Clicked       |      `message.push.clicked`      | User clicked the push.                                                     |
|        Push Failed        |       `message.push.failed`      | Delivery failure. See message reports.                                     |
|     Push Unsubscribed     |    `message.push.unsubscribed`   | User unsubscribed from push.                                               |
|     In-App Impression     |     `message.iam.impression`     | In-App message shown.                                                      |
|       In-App Clicked      |       `message.iam.clicked`      | In-App message clicked.                                                    |
|     In-App Page Viewed    |   `message.iam.page_displayed`   | In-App page shown.                                                         |
|         Email Sent        |       `message.email.sent`       | Email delivered.                                                           |
|       Email Received      |     `message.email.received`     | Email accepted by recipient's mail server.                                 |
|        Email Opened       |      `message.email.opened`      | Email opened. See [Email Reports](/docs/en/email-message-reports).         |
|     Email Link Clicked    |      `message.email.clicked`     | Link in email clicked.                                                     |
|     Email Unsubscribed    |   `message.email.unsubscribed`   | Recipient unsubscribed.                                                    |
|   Email Reported As Spam  | `message.email.reported_as_spam` | Marked as spam. See [Email Deliverability](/docs/en/email-deliverability). |
|       Email Bounced       |      `message.email.bounced`     | Bounce due to permanent delivery failure.                                  |
|        Email Failed       |      `message.email.failed`      | Delivery failed.                                                           |
|      Email Suppressed     |    `message.email.suppressed`    | Suppressed due to suppression list.                                        |
|          SMS Sent         |        `message.sms.sent`        | SMS sent.                                                                  |
|       SMS Delivered       |      `message.sms.delivered`     | SMS successfully delivered.                                                |
|         SMS Failed        |       `message.sms.failed`       | SMS failed to deliver.                                                     |
|      SMS Undelivered      |     `message.sms.undelivered`    | SMS rejected or unreachable.                                               |

### Event data schema

For each message event generated by a user, the following metadata will be attached to the record.

|                   Column Name                   |      Type      | Description                                                  |
| :---------------------------------------------: | :------------: | ------------------------------------------------------------ |
|                    `event_id`                   |      UUID      | Unique identifier for the event                              |
|                `event_timestamp`                |    Timestamp   | Time of event occurrence                                     |
|                   `event_kind`                  |     String     | The [Event Kind](#message-event-kinds)                       |
|            `subscription_device_type`           |     String     | Device type (e.g., iOS, Android, Web, Email, SMS)            |
|                    `language`                   |     String     | Subscription language code                                   |
|                    `version`                    |     String     | Integration version                                          |
|                   `device_os`                   |     String     | Device operating system version                              |
|                  `device_type`                  |     Number     | Numeric device type                                          |
|                     `token`                     |     String     | Push token, phone number, or email                           |
|                `subscription_id`                |      UUID      | Subscription ID                                              |
|                   `subscribed`                  |     Boolean    | Subscription status                                          |
|                  `onesignal_id`                 |      UUID      | OneSignal user ID                                            |
|                  `last_active`                  |     String     | Last active timestamp                                        |
|                      `sdk`                      |     String     | OneSignal SDK version                                        |
|                  `external_id`                  |     String     | External user ID that should match the integration user ID   |
|                     `app_id`                    |      UUID      | App ID from OneSignal                                        |
|                  `template_id`                  |      UUID      | Template ID (if applicable)                                  |
|                   `message_id`                  |      UUID      | Message batch/request ID                                     |
|                  `message_name`                 |     String     | Name of the message                                          |
|                 `message_title`                 |     String     | Message title (English only)                                 |
|                `message_contents`               |     String     | Truncated message body (English only)                        |
|                 `failure_reason`                |     String     | Reason for failure (for push failed and email failed events) |
| `_created`, `_id`, `_index`, `_fivetran_synced` | *Internal use* | Fivetran sync metadata                                       |

### Notes

* Syncs after saving/activating may take an additional 15-30 minutes to complete.
* Deactivating may still result in one final sync after deactivation.
* To ensure efficient data synchronization, our system automatically creates and manages staging datasets. These datasets, named with a pattern like `fivetran_{two random words}_staging`, temporarily store data during processing before it's integrated into your main schema. These staging datasets are essential for maintaining a streamlined workflow and should not be deleted, as they will be automatically recreated.

***

## Import events from BigQuery

Send behavioral event data from BigQuery to OneSignal to:

* Trigger Journeys based on user activity
* Personalize messaging based on behavioral data

**Requirements**

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

* GCP project with BigQuery and event data tables
* Service account with read permissions
* Event data tables containing behavioral data in BigQuery datasets

**Setup Steps**

<Steps>
  <Step title="Create BigQuery service account">
    OneSignal will generate a service account automatically when you create the connection. Alternatively, you can provide your own service account key JSON file.

    If creating your own service account, ensure it has the required permissions listed below.
  </Step>

  <Step title="Grant required permissions">
    The OneSignal service account needs these BigQuery IAM roles:

    * **`bigquery.dataViewer`** - Read access to datasets and tables containing event data
    * **`bigquery.jobUser`** - Permission to create jobs for data queries
    * **`bigquery.metadataViewer`** - Project-level metadata access (recommended)

    Grant permissions using the Google Cloud Console or CLI:

    ```bash  theme={null}
    gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
      --member serviceAccount:ONESIGNAL_SERVICE_ACCOUNT_EMAIL \
      --role roles/bigquery.dataViewer

    gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
      --member serviceAccount:ONESIGNAL_SERVICE_ACCOUNT_EMAIL \
      --role roles/bigquery.jobUser
    ```
  </Step>

  <Step title="Add integration in OneSignal">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    <Frame caption="Add BigQuery integration">
      <img src="https://mintcdn.com/onesignal/IHzVtEbivOs2EktQ/images/integrations/bigquery-add-integration.png?fit=max&auto=format&n=IHzVtEbivOs2EktQ&q=85&s=6877dc14cfe8f9c1677404353927e4f8" width="1944" height="1764" data-path="images/integrations/bigquery-add-integration.png" />
    </Frame>

    * **Sync Engine**: Advanced sync is recommended for large datasets or complex event data queries. You can start with basic sync and switch to advanced sync later if needed.
    * **Google Cloud Project ID**: Your GCP project containing BigQuery datasets
    * **Dataset Region**: Location where your BigQuery datasets are stored
    * **Service Account Key** (optional): JSON key file if using your own service account
  </Step>

  <Step title="Configure event data source">
    Specify the BigQuery dataset and table containing your event data:

    * **Dataset**: BigQuery dataset name (e.g., `analytics_events`)
    * **Table/View**: Table or view containing event records
    * **Event Query**: Optional SQL query to filter or transform event data

    Your event table should contain columns for:

    * Event name/type
    * User identifier
    * Event timestamp
    * Additional event properties
  </Step>

  <Step title="Test the connection">
    Click **Test Connection** to verify OneSignal can access your BigQuery project and read event data.
  </Step>
</Steps>

***

### Event data mapping

Map your {PLATFORM_0} {DATA_TYPE_0} to OneSignal's custom events format:

| OneSignal Field | {COLUMN_HEADER_0} | Description                | Required |
| --------------- | ----------------- | -------------------------- | -------- |
| `name`          | `event_name`      | Event identifier           | Yes      |
| `external_id`   | `user_id`         | User identifier            | Yes      |
| `timestamp`     | `event_timestamp` | When event occurred        | No       |
| `properties`    | `event_data`      | {PROPERTIES_DESCRIPTION_0} | No       |

### Advanced configuration

#### Custom SQL Queries

Use custom SQL to filter or transform event data before syncing to OneSignal:

```sql  theme={null}
SELECT
  event_name,
  user_id,
  event_timestamp,
  STRUCT(
    product_id,
    purchase_amount,
    category
  ) as payload
FROM `project.dataset.events`
WHERE event_timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY)
```

#### Cross-Project Access

If your event data spans multiple BigQuery projects, grant the OneSignal service account access to each project containing referenced tables or views.

<Warning>
  Your BigQuery connection region must match the specific table region for optimal performance.
</Warning>

***

## FAQ

### Why is my sync failing?

There are a few common reasons why your sync may be failing:

* The service account does not have the required permissions
* The source dataset is too large for a basic sync and you need to use advanced sync

Review the above setup steps and ensure you have followed them correctly. If you still have issues, please contact `support@onesignal.com`.

### Why do I see multiple message IDs for the same content?

This typically occurs when a message template is reused across multiple sends or triggered flows.

### How often does OneSignal sync data?

Both export and import integrations can sync as frequently as every 15 minutes.

### Can I use BigQuery views?

Yes. Just make sure the service account has access to all referenced tables in the view.

***

## Related Resources

* [Creating service account keys in GCP](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating)
* [OneSignal Journeys documentation](./journeys-overview)
* [OneSignal Data Export documentation](./exporting-data)

***

Built with [Mintlify](https://mintlify.com).
