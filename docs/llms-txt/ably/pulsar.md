# Source: https://ably.com/docs/platform/integrations/streaming/pulsar.md

# Apache Pulsar integration

[Pulsar](https://pulsar.apache.org) integrations enable you to automatically forward events that occur in Ably to Pulsar topics.

<Aside data-type='note'>
This feature is only available to [enterprise](https://ably.com/docs/platform/pricing/enterprise.md) packages.
</Aside>

## Create a Pulsar integration

To create a rule in your [dashboard:](https://ably.com/dashboard/any)

1. Login and select the application you wish to integrate with Pulsar.
2. Click the **Integrations** tab.
3. Click the **New Integration Rule** button.
4. Choose Firehose.
5. Choose Pulsar.
6. Configure the Pulsar [settings](#settings).
7. Click **Create**.

You can also create a Pulsar integration using the [Control API](https://ably.com/docs/platform/account/control-api.md).

#### Settings

The following settings are available when creating a Pulsar integration:

| Setting | Description |
| ------- | ----------- |
| [Source](https://ably.com/docs/platform/integrations/streaming.md#sources) | Specifies the event types being sent to Pulsar. |
| [Channel filter](https://ably.com/docs/platform/integrations/streaming.md#filter) | Filters the source channels based on a regular expression. |
| Encoding | Specifies the encoding format of messages. Either JSON or MsgPack. |
| [Enveloped](https://ably.com/docs/platform/integrations/streaming.md#enveloped) | Checkbox to set whether messages should be enveloped or not. Enveloped is the default. |
| Routing key | Specifies the [routing key](https://ably.com/docs/messages.md#routing) used to route messages to Pulsar topics. |
| Topic | Defines the Pulsar topic to publish messages to. Must be in the format `tenant/namespace/topic_name`. |
| Service URL | Specifies the Pulsar cluster URL in the format `pulsar://host:port` or `pulsar+ssl://host:port`. |
| JWT Token | JWT to use for authentication. |
| TLS trust certificates | Specify a list of trusted CA certificates to verify TLS certificates presented by Pulsar. |

## Related Topics

- [Overview](https://ably.com/docs/platform/integrations/streaming.md): Outbound streaming integrations enable you to stream data from Ably to an external service for realtime processing.
- [Kafka](https://ably.com/docs/platform/integrations/streaming/kafka.md): Send data to Kafka based on message, channel lifecycle, channel occupancy, and presence events.
- [Kinesis](https://ably.com/docs/platform/integrations/streaming/kinesis.md): Send data to Kinesis based on message, channel lifecycle, channel occupancy, and presence events.
- [AMQP](https://ably.com/docs/platform/integrations/streaming/amqp.md): Send data to AMQP based on message, channel lifecycle, channel occupancy, and presence events.
- [SQS](https://ably.com/docs/platform/integrations/streaming/sqs.md): Send data to SQS based on message, channel lifecycle, channel occupancy, and presence events.
- [DataDog](https://ably.com/docs/platform/integrations/streaming/datadog.md): Connect Ably and Datadog to monitor messages, channels, and connections in realtime, integrating your Ably statistics with your existing Datadog setup.

## Documentation Index

To discover additional Ably documentation:

1. Fetch [llms.txt](https://ably.com/llms.txt) for the canonical list of available pages.
2. Identify relevant URLs from that index.
3. Fetch target pages as needed.

Avoid using assumed or outdated documentation paths.
