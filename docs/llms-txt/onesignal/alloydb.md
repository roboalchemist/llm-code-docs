# Source: https://documentation.onesignal.com/docs/en/alloydb.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AlloyDB

> Sync custom events from Google AlloyDB to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "AlloyDB"

export const DATA_TYPE_0 = "table columns"

export const COLUMN_HEADER_0 = "AlloyDB Column"

export const PROPERTIES_DESCRIPTION_0 = "Event metadata as JSON object"

## Overview

The OneSignal + Google AlloyDB integration enables automatic syncing of custom events from your AlloyDB database directly to OneSignal's Custom Events API. This allows you to trigger automated Journeys and personalized messaging campaigns based on real user behavior stored in your database.

You can sync events like purchases, product views, subscription changes, or any custom user actions to automatically trigger onboarding sequences, re-engagement campaigns, transactional messages, and targeted promotions across push notifications, email, in-app messages, and SMS.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### Google AlloyDB

* **Google Cloud Platform** account with AlloyDB instance
* **Auth Proxy** configured as required by Google Cloud
* **Database permissions** to create users and grant access
* **Network access** to your AlloyDB instance

***

## Setup

### Configure AlloyDB permissions

OneSignal needs to read event data from your AlloyDB database. We recommend creating a dedicated `ONESIGNAL` user account with read-only access to your event tables.

<Steps>
  <Step title="Create OneSignal database user">
    Create a dedicated user account with a strong, unique password:

    ```sql  theme={null}
    -- Create the OneSignal user
    CREATE USER ONESIGNAL WITH PASSWORD '<strong, unique password>';
    ```
  </Step>

  <Step title="Grant schema access">
    Grant the OneSignal user access to read from your event data schema:

    ```sql  theme={null}
    -- Let the OneSignal user see your event schema
    GRANT USAGE ON SCHEMA "<your_event_schema>" TO ONESIGNAL;

    -- Let the OneSignal user read all existing tables in this schema
    GRANT SELECT ON ALL TABLES IN SCHEMA "<your_event_schema>" TO ONESIGNAL;

    -- Let the OneSignal user read any new tables added to this schema
    ALTER DEFAULT PRIVILEGES IN SCHEMA "<your_event_schema>" GRANT SELECT ON TABLES TO ONESIGNAL;
    ```

    <Info>
      Replace `<your_event_schema>` with the actual schema containing your event tables.
    </Info>
  </Step>

  <Step title="Grant function permissions (if needed)">
    If you use stored procedures or functions for event data:

    ```sql  theme={null}
    -- Let the OneSignal user execute functions in this schema
    GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA "<your_event_schema>" TO ONESIGNAL;

    -- Let the OneSignal user execute any new functions added to this schema
    ALTER DEFAULT PRIVILEGES IN SCHEMA "<your_event_schema>" GRANT EXECUTE ON FUNCTIONS TO ONESIGNAL;
    ```
  </Step>
</Steps>

### Set up Auth Proxy

<Steps>
  <Step title="Configure Auth Proxy">
    AlloyDB requires an Auth Proxy for third-party connections. Follow [Google's Auth Proxy documentation](https://cloud.google.com/alloydb/docs/auth-proxy/overview) to set this up.

    <Warning>
      The Auth Proxy is required - OneSignal cannot connect directly to AlloyDB without it.
    </Warning>
  </Step>

  <Step title="Note connection details">
    Save the following connection information:

    * **Host**: Auth Proxy endpoint
    * **Port**: Auth Proxy port (typically 5432)
    * **Database**: Your AlloyDB database name
    * **Username**: `ONESIGNAL` (created above)
    * **Password**: The password you set
  </Step>
</Steps>

### Configure OneSignal AlloyDB connection

<Steps>
  <Step title="Navigate to integrations">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.
  </Step>

  <Step title="Select Google AlloyDB">
    Choose **Google AlloyDB** from the list of available integrations.
  </Step>

  <Step title="Enter connection details">
    Provide the AlloyDB connection information:

    * **Host**: Your Auth Proxy endpoint
    * **Port**: Auth Proxy port
    * **Database**: AlloyDB database name
    * **Username**: `ONESIGNAL`
    * **Password**: User password
    * **SSL**: Enabled (recommended)
  </Step>

  <Step title="Test the connection">
    Click **Test Connection** to verify OneSignal can access your AlloyDB instance.
  </Step>
</Steps>

***

## Event Data Mapping

Once connected, you'll need to map your AlloyDB table columns to OneSignal custom event fields:

<Steps>
  <Step title="Select event tables">
    Choose the tables containing your event data that you want to sync to OneSignal.
  </Step>

  <Step title="Map required event fields">
    Map the required fields for custom events:

    * **Event Name**: Column containing the event type (e.g., "purchase", "signup")
    * **User Identifier**: External User ID, Email, or Phone Number column
    * **Event Timestamp**: When the event occurred (optional)
  </Step>

  <Step title="Map event payload data">
    Map additional columns to event payload properties:

    * Custom event properties (product\_id, price, category, etc.)
    * Contextual data (source, campaign, etc.)
    * Behavioral metrics (value, quantity, etc.)
  </Step>

  <Step title="Configure sync settings">
    Set your event processing frequency and delivery preferences.
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

***

## Advanced Network Configuration

### IP Address Allowlists

If your AlloyDB instance uses IP allowlists, add OneSignal's IP addresses. You can find the current IP ranges in your OneSignal dashboard under **Data > Integrations > Network Access**.

### SSH Tunneling

OneSignal supports connecting to AlloyDB through SSH tunnels for additional security:

<Steps>
  <Step title="Create SSH user">
    Create a dedicated user account for OneSignal on your SSH host server.
  </Step>

  <Step title="Configure SSH tunnel">
    In the OneSignal AlloyDB connection settings, enable **Use SSH Tunnel** and provide:

    * SSH Host
    * SSH Port
    * SSH Username
  </Step>

  <Step title="Add SSH key">
    OneSignal will generate an SSH keypair. Copy the public key to your SSH host's `authorized_keys` file for the OneSignal user.
  </Step>
</Steps>

***

## Limitations

* **Performance**: Avoid connecting to production databases during peak usage
* **Permissions**: OneSignal requires read-only access to event tables
* **Auth Proxy**: Required for all AlloyDB connections

***

## FAQ

### What happens if my event table structure changes?

OneSignal will detect schema changes and may require remapping of fields. Update your field mappings in the integration settings.

### How often does OneSignal sync events?

OneSignal checks for new events based on your configured sync frequency, with a minimum interval of 15 minutes.

***

## Need help?

Contact our support team at `support@onesignal.com` or use the in-app chat for assistance with your AlloyDB integration setup.

Built with [Mintlify](https://mintlify.com).
