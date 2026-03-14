# Source: https://documentation.onesignal.com/docs/en/google-pubsub.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Pub/Sub

> Sync custom events from Google Pub/Sub to OneSignal to trigger automated Journeys and personalized messaging campaigns based on real-time user behavior.

export const PLATFORM_0 = "Pub/Sub"

export const DATA_TYPE_0 = "message fields"

export const COLUMN_HEADER_0 = "Pub/Sub Message Field"

export const PROPERTIES_DESCRIPTION_0 = "JSON object with event details"

## Overview

The OneSignal + Google Pub/Sub integration enables real-time syncing of custom events from your Pub/Sub topics to OneSignal to trigger automated messaging campaigns and Journeys based on user behavior.

Pub/Sub is Google's scalable messaging service that allows applications to send and receive messages between independent components. OneSignal acts as a subscriber to your Pub/Sub topics, allowing you to sync event messages from Pub/Sub to trigger personalized user experiences.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### Google Pub/Sub

* **Google Cloud Project** with Pub/Sub enabled
* **Pub/Sub topics** containing event messages
* **IAM permissions** to grant service account access
* **JSON-formatted messages** on your topics

***

## Setup

<Steps>
  <Step title="Create Pub/Sub connection">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    1. Select **Google Pub/Sub** from the list
    2. Enter the **GCP Project ID** where your Pub/Sub topics are located
    3. Choose authentication method:
       * **Auto-generated Service Account** (recommended): OneSignal creates and manages the service account
       * **Existing Service Account**: Provide your own service account key JSON file
    4. Click **Connect**
  </Step>

  <Step title="Grant permissions to service account">
    OneSignal will create a new service account and provide you with the service account email address.

    Grant the **`roles/pubsub.editor`** role to this service account on your GCP project:

    ```bash  theme={null}
    gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
      --member serviceAccount:SERVICE_ACCOUNT_EMAIL \
      --role roles/pubsub.editor
    ```

    OneSignal uses this role to:

    * Create subscriptions to your event topics
    * Consume event messages from topics
    * Create error topics (Dead Letter Queue) for failed processing
  </Step>

  <Step title="Test connection">
    Once you've granted the necessary permissions, click **Save** in OneSignal to verify the connection.

    OneSignal will validate that it can access your Pub/Sub topics and is ready to process event messages.
  </Step>
</Steps>

***

## Event Data Schema

Before you can use a Pub/Sub topic for custom events, you must define the schema of the event messages.

<Steps>
  <Step title="Navigate to event schema definition">
    In OneSignal, go to **Data > Integrations** and select your Pub/Sub connection.

    OneSignal automatically pulls the list of topics from your project. Click **Refresh topics** to manually refresh the list.
  </Step>

  <Step title="Define event message schema">
    1. Click on the name of the topic containing your event data
    2. Select **JSON** as the message format (only supported format)
    3. Click **Import sample message** and provide a sample event message
    4. Review the detected schema to ensure proper field mapping
    5. Click **Save Dataset**
  </Step>
</Steps>

### Event Message Format

Your Pub/Sub messages should follow this JSON structure for OneSignal custom events:

```json  theme={null}
{
  "event_name": "purchase_completed",
  "user_id": "user_12345",
  "timestamp": "2023-12-01T10:30:00Z",
  "properties": {
    "product_id": "prod_abc123",
    "price": 29.99,
    "category": "electronics",
    "payment_method": "credit_card"
  },
  "session_id": "session_789"
}
```

### Event data mapping

Map your {PLATFORM_0} {DATA_TYPE_0} to OneSignal's custom events format:

| OneSignal Field | {COLUMN_HEADER_0} | Description                | Required |
| --------------- | ----------------- | -------------------------- | -------- |
| `name`          | `event_name`      | Event identifier           | Yes      |
| `external_id`   | `user_id`         | User identifier            | Yes      |
| `timestamp`     | `event_timestamp` | When event occurred        | No       |
| `properties`    | `event_data`      | {PROPERTIES_DESCRIPTION_0} | No       |

<Warning>
  Do not include customer PII or sensitive data in sample messages. OneSignal stores message samples as part of the dataset definition.
</Warning>

***

## Real-time Event Processing

Unlike batch integrations, Pub/Sub enables near real-time event processing:

* **Low Latency**: Events are processed within seconds of being published to topics
* **Automatic Subscriptions**: OneSignal creates dedicated subscriptions for each topic
* **Error Handling**: Failed events are sent to Dead Letter Queue topics for investigation
* **Scalable Processing**: Handles high-volume event streams automatically

***

## Advanced Configuration

### Dead Letter Queue

OneSignal automatically creates error topics for events that fail processing:

* **Automatic Creation**: Error topics are created per subscription
* **Failed Event Storage**: Events that can't be processed are stored for debugging
* **Manual Review**: Access failed events through Google Cloud Console for troubleshooting

### Message Acknowledgment

OneSignal handles Pub/Sub message acknowledgment automatically:

* **Successful Processing**: Messages are acknowledged after successful event creation
* **Failed Processing**: Messages are negatively acknowledged and sent to Dead Letter Queue
* **Retry Logic**: Built-in retry handling for transient failures

***

## Limitations

* Only JSON message format is supported
* Message samples are stored as part of dataset definitions (avoid PII)
* Requires `roles/pubsub.editor` permissions at project level
* Maximum message size follows Google Pub/Sub limits (10MB)

***

## FAQ

### How quickly are events processed?

Events are typically processed within seconds of being published to your Pub/Sub topic, enabling near real-time Journey triggering.

### What happens if OneSignal can't process an event?

Failed events are automatically sent to a Dead Letter Queue topic that OneSignal creates. You can review these events in the Google Cloud Console for debugging.

### Can I use multiple topics for different event types?

Yes, you can define schemas for multiple topics within the same GCP project. Each topic can contain different event types with their own schema definitions.

Built with [Mintlify](https://mintlify.com).
