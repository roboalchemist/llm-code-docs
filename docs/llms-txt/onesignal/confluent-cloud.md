# Source: https://documentation.onesignal.com/docs/en/confluent-cloud.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Confluent Cloud

> Sync custom events from Confluent Cloud to OneSignal to trigger automated Journeys and personalized messaging campaigns based on real-time user behavior.

export const PLATFORM_0 = "Confluent Cloud"

export const DATA_TYPE_0 = undefined

export const COLUMN_HEADER_0 = undefined

export const PROPERTIES_DESCRIPTION_0 = undefined

## Overview

The OneSignal + Confluent Cloud integration enables automatic syncing of custom events from your managed Kafka topics to OneSignal. This allows you to trigger automated Journeys and personalized messaging campaigns based on real-time user behavioral data flowing through your Confluent Cloud streaming platform.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### Confluent Cloud

* **Confluent Cloud cluster** with active topics
* **API credentials** with read access to event topics
* **Schema Registry** (optional, for structured event schemas)
* **Event topics** containing behavioral data with proper message format

***

## Setup

<Steps>
  <Step title="Create API credentials in Confluent Cloud">
    Generate API credentials for OneSignal in your Confluent Cloud console:

    1. Navigate to **Data Integration > API Keys** in Confluent Cloud
    2. Click **Create key** and select **Global access**
    3. Save the **API Key** and **API Secret** (you'll need these for OneSignal)
    4. Note your **Bootstrap servers** endpoint from your cluster settings
  </Step>

  <Step title="Configure topic ACLs (if using granular permissions)">
    Grant OneSignal read access to specific topics containing event data:

    ```bash  theme={null}
    confluent kafka acl create \
      --allow \
      --service-account <ONESIGNAL_SERVICE_ACCOUNT_ID> \
      --operation READ \
      --topic <EVENT_TOPIC_NAME>

    confluent kafka acl create \
      --allow \
      --service-account <ONESIGNAL_SERVICE_ACCOUNT_ID> \
      --operation DESCRIBE \
      --topic <EVENT_TOPIC_NAME>
    ```
  </Step>

  <Step title="Add integration in OneSignal">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    Select **Confluent Cloud** and provide:

    * **Bootstrap Servers**: Your Confluent Cloud cluster endpoint
    * **API Key**: Confluent Cloud API key
    * **API Secret**: Confluent Cloud API secret
    * **Consumer Group**: Unique group ID for OneSignal (e.g., `onesignal-events`)
    * **Schema Registry URL** (optional): If using Confluent Schema Registry
  </Step>

  <Step title="Configure event topics">
    Specify the Confluent Cloud topics containing your event data:

    * **Topic Names**: Comma-separated list of topics to consume (e.g., `user-events,purchase-events`)
    * **Event Format**: JSON, Avro, or Protobuf message format
    * **Schema Registry**: Enable if using structured schemas

    Your event messages should contain:

    * Event name/type (String)
    * User identifier (String)
    * Event timestamp (Long/ISO format)
    * Additional event properties (nested JSON)
  </Step>

  <Step title="Test the connection">
    Click **Test Connection** to verify OneSignal can connect to your Confluent Cloud cluster and consume event messages.
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

## Advanced Configuration

### Schema Registry Integration

Leverage Confluent Schema Registry for structured event data:

```json  theme={null}
{
  "schema": "user_event_schema_v1",
  "data": {
    "event_name": "purchase",
    "user_id": "user_12345",
    "event_timestamp": 1640995200000,
    "properties": {
      "product_id": "prod_abc123",
      "amount": 29.99,
      "currency": "USD"
    }
  }
}
```

### Consumer Group Management

OneSignal creates a dedicated consumer group to track message offsets:

* **Auto-commit**: Offsets committed automatically after successful processing
* **Error Handling**: Failed messages logged with retry mechanism
* **Scaling**: Partitions balanced across OneSignal consumer instances

### Real-time Processing

Confluent Cloud enables near real-time event activation:

* **Low Latency**: Events processed within seconds of being published
* **High Throughput**: Handles thousands of events per second
* **Fault Tolerance**: Built-in replication and automatic failover

<Warning>
  Ensure your Confluent Cloud cluster has sufficient throughput capacity to handle OneSignal's consumption rate alongside your other consumers.
</Warning>

***

## FAQ

### How often does OneSignal consume events from Confluent Cloud?

OneSignal consumes events in real-time as they arrive in your topics, with minimal latency (typically under 5 seconds).

### Can I consume from multiple topics simultaneously?

Yes, OneSignal can consume from multiple topics in parallel. Specify topic names as a comma-separated list in the configuration.

### What happens if OneSignal can't connect to Confluent Cloud?

OneSignal will retry connections with exponential backoff. Event consumption will resume automatically once connectivity is restored.

Built with [Mintlify](https://mintlify.com).
