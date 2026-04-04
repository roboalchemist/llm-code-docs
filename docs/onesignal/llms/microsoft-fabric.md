# Source: https://documentation.onesignal.com/docs/en/microsoft-fabric.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Fabric

> Sync custom events from Microsoft Fabric to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "Microsoft Fabric"

export const DATA_TYPE_0 = "table columns"

export const COLUMN_HEADER_0 = "Fabric Column"

export const PROPERTIES_DESCRIPTION_0 = "JSON object with event metadata"

## Overview

The OneSignal + Microsoft Fabric integration enables automatic syncing of custom events from your Fabric lakehouse or warehouse to OneSignal to trigger automated messaging campaigns and Journeys based on user behavior.

Microsoft Fabric is a unified analytics platform that brings together data engineering, data science, real-time analytics, and business intelligence in a single environment.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### Microsoft Fabric

* **Microsoft Fabric capacity** with workspace access
* **Service Principal** with appropriate permissions
* **SQL Endpoint** (Warehouse or Lakehouse) containing event data
* **External API access** enabled in tenant settings

***

## Setup

<Steps>
  <Step title="Create service principal in Azure">
    Create a new service principal for OneSignal to access your Fabric resources:

    1. Sign in to the Azure portal
    2. Navigate to **Microsoft Entra ID** > **App registrations**
    3. Click **+ New registration**
    4. Enter name: "OneSignal Fabric Integration"
    5. Select **Accounts in this organizational directory only**
    6. Click **Register**
    7. Note the **Application (client) ID** and **Directory (tenant) ID**
    8. Under **Certificates & secrets**, create a new client secret
    9. Note the **client secret value**
  </Step>

  <Step title="Configure Fabric tenant settings">
    Enable external access for service principals:

    1. In Microsoft Fabric, click **Settings** > **Admin portal**
    2. Go to **Tenant settings**
    3. Under **Developer settings**, enable **Service principals can use Fabric APIs**
    4. Under **OneLake settings**, enable **Users can access data stored in OneLake with apps external to Fabric**
  </Step>

  <Step title="Grant workspace access">
    Add the service principal to your Fabric workspace:

    1. Navigate to your workspace (create shared workspace if using "My Workspace")
    2. Click **Manage Access** > **+ Add people or groups**
    3. Select your service principal
    4. Set role to **Contributor**
  </Step>

  <Step title="Get SQL endpoint">
    Obtain the SQL connection string for your data source:

    1. In your workspace, hover over your warehouse/lakehouse
    2. Click **...** > **Settings**
    3. Copy the **SQL connection string** (this is your hostname)
  </Step>

  <Step title="Connect to OneSignal">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    Select **Microsoft Fabric** and provide:

    * **Hostname:** SQL endpoint from Step 4
    * **Database/Catalog:** Your lakehouse or warehouse name
    * **Tenant ID:** Directory ID from Step 1
    * **Client ID:** Application ID from Step 1
    * **Client Secret:** Secret value from Step 1
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

### Example Event Table Schema

```sql  theme={null}
-- Example Fabric table structure
CREATE TABLE user_events (
    event_name STRING,
    user_id STRING,
    event_time TIMESTAMP,
    properties JSON,
    session_id STRING,
    device_type STRING
);
```

***

## Processing Modes

### SQL Query Mode

Write custom SQL queries to transform your Fabric data before syncing:

```sql  theme={null}
SELECT
    event_name,
    user_id,
    event_time,
    TO_JSON(STRUCT(
        session_id,
        device_type,
        product_id
    )) as properties
FROM user_events
WHERE event_time >= CURRENT_DATE - INTERVAL 7 DAYS
```

### Table Mode

Sync entire tables or views directly from your Fabric workspace. OneSignal will automatically map columns to event fields.

***

## Limitations

* Requires Fabric capacity (not available on trial)
* SQL endpoints must be accessible to external services
* Large result sets may impact sync performance

***

## FAQ

### How do I optimize query performance?

Use partitioning and indexing in your Fabric tables. Consider creating materialized views for frequently accessed event data.

### Can I sync from both lakehouses and warehouses?

Yes, OneSignal supports any Fabric resource that exposes a SQL endpoint, including lakehouses, warehouses, and SQL analytics endpoints.

***

Built with [Mintlify](https://mintlify.com).
