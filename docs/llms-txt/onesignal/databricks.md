# Source: https://documentation.onesignal.com/docs/en/databricks.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Databricks

> Export OneSignal message events to Databricks and import Databricks behavioral events into OneSignal to trigger Journeys and personalize messaging.

export const PLATFORM_0 = "Databricks"

export const DATA_TYPE_0 = "event table columns"

export const COLUMN_HEADER_0 = "Databricks Column"

export const PROPERTIES_DESCRIPTION_0 = "Additional columns as JSON"

## Overview

The OneSignal + Databricks integration supports **two flows**:

* **Export**: Send OneSignal message events to Databricks for analytics and reporting.
* **Import**: Send custom events from Databricks to OneSignal to trigger Journeys and personalize campaigns.

<Info> Export and import are configured separately. You can set up one without the other. </Info>

***

## Export OneSignal message events to Databricks

Sync all your message events from OneSignal into your Databricks lakehouse for near real-time analytics and visibility.

**Requirements**

* [Professional Plan or higher](https://onesignal.com/pricing)
* Custom Events enabled (for event imports)
* Databricks Platform: AWS, Azure, or GCP
* Databricks Plan: Premium or higher
* Databricks Unity Catalog (recommended for governance)
* Databricks SQL Warehouse for querying
* Delta Lake event tables (for custom event import)

**Setup Steps**

### 1. Collect SQL warehouse details

<Steps>
  <Step title="Log in to your Databricks workspace">
    Go to **SQL Warehouses** in your Databricks workspace.
  </Step>

  <Step title="Select your warehouse">
    Select your warehouse and open the **Connection details** tab.
  </Step>

  <Step title="Save the following details">
    * Server Hostname
    * Port
    * HTTP Path

    <Frame caption="Databricks SQL connection details for Fivetran setup">
      <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1ce7c549df4a383336633d9f258bec12107a895dc9467134d672c12c2c85923f-cluster-databricks.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=1f03dbaa1a6cc6c4bdf804e49755cbf7" alt="Databricks SQL connection details for Fivetran setup" width="1810" height="988" data-path="images/docs/1ce7c549df4a383336633d9f258bec12107a895dc9467134d672c12c2c85923f-cluster-databricks.png" />
    </Frame>
  </Step>
</Steps>

### 2. Choose authentication method

Databricks supports two authentication methods. Choose the method that best fits your deployment and security requirements.

<Tabs>
  <Tab title="OAuth M2M">
    **When to use:**

    * Direct connections (not using PrivateLink)
    * Organizations with OAuth infrastructure

    **Note:** Does not support PrivateLink connections.

    #### Create a service principal

    <Steps>
      <Step title="Go to the Service Principals page">
        Go to **Workspace Settings > Identity and Access > Service Principals**.
      </Step>

      <Step title="Add a new service principal">
        Click **Add Service Principal**, then **Add New**.
      </Step>

      <Step title="Name the service principal">
        Name it (e.g., `onesignal-sync`).

        <Frame caption="Modal for adding a service principal, with the 'Add new' option highlighted">
          <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b8eeb211ceb77247f711eb312d3d68d1cb0da10788fd81fd37ae27e929e35cde-Screenshot_2025-04-01_at_9.16.12_PM.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=3bda750f12db717d630220bed24cdb2e" alt="Modal for adding a service principal, with the 'Add new' option highlighted" width="932" height="392" data-path="images/docs/b8eeb211ceb77247f711eb312d3d68d1cb0da10788fd81fd37ae27e929e35cde-Screenshot_2025-04-01_at_9.16.12_PM.png" />
        </Frame>
      </Step>
    </Steps>

    #### Generate a secret

    <Steps>
      <Step title="Click into the created principal" />

      <Step title="Go to the Secrets tab" />

      <Step title="Generate a secret">
        Click **Generate Secret** and save it securely.

        <Warning>
          The secret is only visible once—store it safely.
        </Warning>

        <Frame caption="Databricks 'Generate secret' modal showing OAuth secret and client ID for API authentication">
          <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/ff24d4d5bf9b21e0cadf67055f1e1a5a4b517b82e9c006520a02b4fd404d259e-Screenshot_2025-03-28_at_4.14.17_PM.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=54eaae1d695bfad59b726ba005ff6f1f" alt="Databricks 'Generate secret' modal showing OAuth secret and client ID for API authentication" width="746" height="368" data-path="images/docs/ff24d4d5bf9b21e0cadf67055f1e1a5a4b517b82e9c006520a02b4fd404d259e-Screenshot_2025-03-28_at_4.14.17_PM.png" />
        </Frame>
      </Step>
    </Steps>
  </Tab>

  <Tab title="Personal Access Token">
    **When to use:**

    * Using PrivateLink (AWS or Azure)
    * Simpler setup
    * Maximum compatibility

    **Note:** Works with all Databricks deployment types.

    #### Create a Personal Access Token

    <Steps>
      <Step title="Access Settings">
        In your Databricks workspace, click your username in the top bar and select **Settings**.
      </Step>

      <Step title="Navigate to Developer section">
        Click **Developer**.
      </Step>

      <Step title="Manage tokens">
        Next to **Access tokens**, click **Manage**.
      </Step>

      <Step title="Generate new token">
        Click **Generate new token**.
      </Step>

      <Step title="Configure token">
        * Enter a comment like "OneSignal Integration" to help identify this token
        * Set the token's lifetime in days (check your workspace documentation for maximum allowed duration)
        * Click **Generate**
      </Step>

      <Step title="Save the token">
        Copy the displayed token to a secure location, then click **Done**.

        <Warning>
          Save the token securely and don't share it. If you lose it, you must create a new token. Tokens that remain unused for 90 days are automatically revoked by Databricks.
        </Warning>
      </Step>
    </Steps>
  </Tab>
</Tabs>

<Note>
  **Recommendation:** If you're using PrivateLink or want the simplest setup, choose Personal Access Token. For direct connections with existing OAuth infrastructure, OAuth M2M works well.
</Note>

### 3. Assign permissions

<Steps>
  <Step title="Navigate to your Catalog and open the Permissions tab" />

  <Step title="Click Grant" />

  <Step title="Assign the following permissions to the service principal or user">
    * USE CATALOG
    * USE SCHEMA
    * SELECT
    * MODIFY
    * CREATE SCHEMA
    * CREATE TABLE

    <Frame caption="Privilege assignment screen for a Databricks principal with custom catalog permissions selected.">
      <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/5755c8739fd66a0f35fec57b817d54d202c64ae95bf8219645ba76abdc8fbe0b-Screenshot_2025-04-01_at_9.19.14_PM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=0964053615467ebd7372edd7beaf33fe" alt="Privilege assignment screen for a Databricks principal with custom catalog permissions selected" width="1034" height="812" data-path="images/docs/5755c8739fd66a0f35fec57b817d54d202c64ae95bf8219645ba76abdc8fbe0b-Screenshot_2025-04-01_at_9.19.14_PM.png" />
    </Frame>
  </Step>
</Steps>

### 4. Connect OneSignal

<Steps>
  <Step title="Activate the integration">
    In OneSignal, navigate to **Data > Integrations > Databricks**.
  </Step>

  <Step title="Enter the details">
    * Server Hostname
    * Port
    * HTTP Path
    * Catalog Name
    * Schema Name
    * Credentials

    <Frame caption="OneSignal Databricks Configuration form with fields for catalog, hostname, HTTP path, and credentials.">
      <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/816a07ed459d3d19910630da0cb52b2075c06d6eaf85af98e969703edab88ad5-Screenshot_2025-03-28_at_4.12.07_PM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=cd7ba1d76deff9922dc44b25a7528eb2" alt="OneSignal Databricks Configuration form with fields for catalog, hostname, HTTP path, and OAuth credentials" width="718" height="796" data-path="images/docs/816a07ed459d3d19910630da0cb52b2075c06d6eaf85af98e969703edab88ad5-Screenshot_2025-03-28_at_4.12.07_PM.png" />
    </Frame>
  </Step>

  <Step title="Configure the integration">
    * **Sync Frequency:** as often as every 15 minutes
    * **Dataset/Table Names:** pre-set as `onesignal_events_<app-id>` and `message_events` (editable)
    * **Event Types:** choose which to sync—select all or just what you need
  </Step>

  <Step title="Select events">
    Select the events you care to receive in your Databricks catalog.

    <Frame caption="OneSignal event export settings screen showing sync status, dataset configuration, and selected message event types.">
      <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1a5ff2af7dc8fc42a91ce70583a03b361fd8a343bc57fd3123f26a5d21dabbf8-Screenshot_2025-04-09_at_11.56.58_AM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=ce7eee0983e2026b1847a4d2a45cbe96" alt="OneSignal event export settings screen showing sync status, dataset configuration, and selected message event types" width="2738" height="1254" data-path="images/docs/1a5ff2af7dc8fc42a91ce70583a03b361fd8a343bc57fd3123f26a5d21dabbf8-Screenshot_2025-04-09_at_11.56.58_AM.png" />
    </Frame>
  </Step>

  <Step title="Complete the setup">
    Click **Save** and wait for the success confirmation
  </Step>
</Steps>

<Note>
  Initial data sync can take 15–30 minutes to appear in BigQuery.

  While you wait, send messages via push, email, in-app, or SMS to trigger the events selected.
</Note>

### 5. View data in Databricks

1. Open your **Catalog** in Databricks.

2. Once syncing completes, your configured schema will appear.

3. Access and query the `message_events` table.

   <Frame caption="Databricks Catalog view showing OneSignal message events table under a production schema.">
     <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1b59f6eff2070490f194df8a7496fab6cf17f8fc9355cfb7b77c7c076799632e-Screenshot_2025-04-01_at_9.22.01_PM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=c5908557481f292b1a659b4f0ef210ed" alt="Databricks Catalog view showing OneSignal message events table under a production schema" width="854" height="618" data-path="images/docs/1b59f6eff2070490f194df8a7496fab6cf17f8fc9355cfb7b77c7c076799632e-Screenshot_2025-04-01_at_9.22.01_PM.png" />
   </Frame>

4. Click into tables for sample data preview.

   <Frame caption="Sample data from the message_events_1 table with synced OneSignal event fields.">
     <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/112f17e471b8e29173429bfbbd4b34fb68923c9f76faa55b06161114249fcaab-Screenshot_2025-04-01_at_9.22.08_PM.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=a853fe144d238a24d86b5f989261f2be" alt="Sample data from the message_events_1 table with synced OneSignal event fields" width="1196" height="374" data-path="images/docs/112f17e471b8e29173429bfbbd4b34fb68923c9f76faa55b06161114249fcaab-Screenshot_2025-04-01_at_9.22.08_PM.png" />
   </Frame>

<Info>
  If you run into issues like missing schemas, permission errors, or malformed events, contact `support@onesignal.com`.
</Info>

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

## Import events from Databricks

Send behavioral event data from Databricks to OneSignal to:

* Trigger Journeys based on user activity
* Personalize messaging based on behavioral data

**Requirements**

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

* **Databricks workspace** with SQL Warehouse or compute cluster
* **Personal Access Token** with appropriate permissions
* **Event data tables** containing behavioral data in Delta Lake format
* **Unity Catalog** (recommended for data governance)

**Setup Steps**

<Steps>
  <Step title="Create Databricks Personal Access Token">
    Generate a Personal Access Token for OneSignal to access your Databricks workspace:

    1. Navigate to **User Settings** in your Databricks workspace
    2. Click **Developer** tab and then **Access tokens**
    3. Click **Generate new token**
    4. Enter a comment like "OneSignal Integration" and set expiration (recommend 90 days)
    5. Save the generated token (you'll need this for OneSignal)
  </Step>

  <Step title="Configure SQL Warehouse access">
    Ensure OneSignal can query your event data via SQL Warehouse:

    1. Navigate to **SQL Warehouses** in your Databricks workspace
    2. Select or create a SQL Warehouse for OneSignal access
    3. Note the **Server Hostname** and **HTTP Path** from the connection details
    4. Ensure the warehouse has access to your event data tables
  </Step>

  <Step title="Grant table permissions">
    Grant OneSignal read access to tables containing event data:

    ```sql  theme={null}
    -- For Unity Catalog enabled workspaces
    GRANT SELECT ON TABLE catalog.schema.event_table TO `onesignal@yourdomain.com`;

    -- For Hive metastore tables
    GRANT SELECT ON TABLE database.event_table TO `onesignal@yourdomain.com`;
    ```
  </Step>

  <Step title="Add integration in OneSignal">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    Select **Databricks** and provide:

    * **Server Hostname**: Your Databricks SQL Warehouse hostname
    * **HTTP Path**: SQL Warehouse HTTP path
    * **Personal Access Token**: Token created in step 1
    * **Catalog** (optional): Unity Catalog name if using Unity Catalog
  </Step>

  <Step title="Configure event data source">
    Specify the Databricks table containing your event data:

    * **Database/Schema**: Database or schema name containing event tables
    * **Table**: Table name with event records (e.g., `user_events`)
    * **Event Query**: Optional SQL query to filter or transform event data

    Your event table should contain columns for:

    * Event name/type (String)
    * User identifier (String)
    * Event timestamp (Timestamp)
    * Additional event properties
  </Step>

  <Step title="Test the connection">
    Click **Test Connection** to verify OneSignal can access your Databricks workspace and read event data.
  </Step>
</Steps>

### Event data mapping

Map your {PLATFORM_0} {DATA_TYPE_0} to OneSignal's custom events format:

| OneSignal Field | {COLUMN_HEADER_0} | Description                | Required |
| --------------- | ----------------- | -------------------------- | -------- |
| `name`          | `event_name`      | Event identifier           | Yes      |
| `external_id`   | `user_id`         | User identifier            | Yes      |
| `timestamp`     | `event_timestamp` | When event occurred        | No       |
| `properties`    | `event_data`      | {PROPERTIES_DESCRIPTION_0} | No       |

### Advanced configuration

#### Unity Catalog Integration

Leverage Unity Catalog for governed data access:

```sql  theme={null}
SELECT
  event_name,
  user_id,
  event_timestamp,
  to_json(
    named_struct(
      'product_id', product_id,
      'purchase_amount', purchase_amount,
      'category', category
    )
  ) as payload
FROM catalog.schema.user_events
WHERE event_timestamp >= current_timestamp() - INTERVAL 7 DAYS
```

### Delta Lake Optimization

Optimize event tables for better query performance:

* **Partitioning**: Partition by date (`event_date`) for faster time-based queries
* **Z-Ordering**: Z-order by `user_id` and `event_name` for better filtering
* **Delta Lake Features**: Use liquid clustering for automatic optimization

#### Streaming Event Processing

For real-time event processing, consider:

* **Structured Streaming**: Process events as they arrive
* **Delta Live Tables**: Build robust event processing pipelines
* **Auto Loader**: Continuously ingest new event files

<Warning>
  Ensure your SQL Warehouse has sufficient compute resources to handle OneSignal's queries without affecting other workloads.
</Warning>

***

## FAQ

### Why do I see different message IDs with the same content?

This happens when the same message is sent more than once, likely via a transactional flow or message template reused across multiple sends.

### How often does OneSignal sync events from Databricks?

OneSignal syncs event data based on your configured schedule, with a minimum interval of 15 minutes.

### Can I use Databricks notebooks for event processing?

Yes, you can use notebooks to process and prepare event data, then expose it via tables that OneSignal can query.

### What about cost optimization for event queries?

Consider using serverless SQL Warehouses for cost-effective, on-demand compute that automatically scales based on query load.

***

Built with [Mintlify](https://mintlify.com).
