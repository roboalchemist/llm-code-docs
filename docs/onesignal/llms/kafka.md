# Source: https://documentation.onesignal.com/docs/en/kafka.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Apache Kafka

> Sync custom events from Apache Kafka topics to OneSignal to trigger automated Journeys and personalized messaging campaigns based on real-time user behavior.

export const PLATFORM_0 = "Kafka"

export const DATA_TYPE_0 = undefined

export const COLUMN_HEADER_0 = undefined

export const PROPERTIES_DESCRIPTION_0 = undefined

## Overview

The OneSignal + Apache Kafka integration enables automatic syncing of custom events from your Kafka topics directly to OneSignal's Custom Events API. This allows you to trigger automated Journeys and personalized messaging campaigns based on real-time user behavior streaming through your Kafka infrastructure.

You can sync events like purchases, product views, subscription changes, or any custom user actions to automatically trigger onboarding sequences, re-engagement campaigns, transactional messages, and targeted promotions across push notifications, email, in-app messages, and SMS.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### Apache Kafka

* **Kafka Cluster** (Apache Kafka, Confluent, or cloud-managed)
* **Topics** containing event data
* **Authentication credentials** (SASL/SCRAM, SSL, or API keys)
* **Network access** to Kafka brokers
* **Event data** in JSON format

***

## Setup

### Configure Kafka permissions

OneSignal needs to consume events from your Kafka topics. The exact setup depends on your Kafka configuration:

<Steps>
  <Step title="Gather connection details">
    Collect the following information about your Kafka cluster:

    * **Bootstrap Servers**: Kafka broker endpoints
    * **Security Protocol**: PLAINTEXT, SASL\_PLAINTEXT, SASL\_SSL, or SSL
    * **Authentication**: Username/password, certificates, or API keys
    * **Topic Names**: List of topics containing event data
  </Step>

  <Step title="Create consumer credentials">
    Create credentials for OneSignal to access your Kafka topics:

    **For SASL/SCRAM authentication:**

    ```bash  theme={null}
    # Create a user with read access to event topics
    kafka-configs --bootstrap-server localhost:9092 \
      --alter --add-config 'SCRAM-SHA-256=[password=onesignal-password]' \
      --entity-type users --entity-name onesignal-consumer
    ```

    **For ACL-based authorization:**

    ```bash  theme={null}
    # Grant read access to topics and consumer group
    kafka-acls --bootstrap-server localhost:9092 \
      --add --allow-principal User:onesignal-consumer \
      --operation Read --topic your-event-topic

    kafka-acls --bootstrap-server localhost:9092 \
      --add --allow-principal User:onesignal-consumer \
      --operation Read --group onesignal-consumer-group
    ```
  </Step>

  <Step title="Verify topic access">
    Test that OneSignal can access your event topics:

    ```bash  theme={null}
    kafka-console-consumer --bootstrap-server localhost:9092 \
      --topic your-event-topic \
      --from-beginning \
      --max-messages 5
    ```
  </Step>
</Steps>

### Configure OneSignal Kafka connection

<Steps>
  <Step title="Navigate to integrations">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.
  </Step>

  <Step title="Select Apache Kafka">
    Choose **Apache Kafka** from the list of available integrations.
  </Step>

  <Step title="Enter connection details">
    Provide your Kafka connection information:

    * **Bootstrap Servers**: Comma-separated broker endpoints
    * **Security Protocol**: Your cluster's security configuration
    * **Username/Password**: SASL credentials (if applicable)
    * **Topic Names**: Topics containing your event data
    * **Consumer Group**: Unique group ID for OneSignal
  </Step>

  <Step title="Test the connection">
    Click **Test Connection** to verify OneSignal can connect to your Kafka cluster and consume events.
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

## Event Data Schema

Your Kafka event messages should be in JSON format and include fields that map to OneSignal custom event structure:

| Kafka Event Field | OneSignal Event Field | Description |
| ----------------- | --------------------- | ----------- |
| `event_type`      |                       |             |

Built with [Mintlify](https://mintlify.com).
