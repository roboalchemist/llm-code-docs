# Source: https://ably.com/docs/platform/integrations/streaming/amqp.md

# AMQP integration

[AMQP](https://www.amqp.org) integrations enable you to automatically forward events that occur in Ably to AMQP-compatible brokers.

## Create an AMQP integration

To create an AMQP integration in your [dashboard:](https://ably.com/dashboard/any)

1. Login and select the application you wish to integrate with AMQP.
2. Click the **Integrations** tab.
3. Click the **New Integration Rule** button.
4. Choose Firehose.
5. Choose AMQP.
6. Configure the AMQP [settings](#settings).
7. Click **Create**.

You can also create an AMQP integration using the [Control API](https://ably.com/docs/platform/account/control-api.md).

### Settings

The following settings are available when creating an AMQP integration:

| Setting | Description |
| ------- | ----------- |
| URL | Specifies the AMQP connection URL in the format `amqps://username:password@host.name/vhost`. |
| Headers | Allows the inclusion of additional information in key-value format. |
| [Source](https://ably.com/docs/platform/integrations/streaming.md#sources) | Specifies the event types being sent to AMQP. |
| [Channel filter](https://ably.com/docs/platform/integrations/streaming.md#filter) | Filters the source channels based on a regular expression. |
| Encoding | Specifies the encoding format of messages. Either JSON or MsgPack. |
| [Enveloped](https://ably.com/docs/platform/integrations/streaming.md#enveloped) | Checkbox to set whether messages should be enveloped or not. Enveloped is the default. |
| Routing key | Specifies the [routing key](https://ably.com/docs/messages.md#routing) used by the AMQP exchange to route messages to a physical queue. Supports interpolation. |
| Exchange | An optional RabbitMQ exchange. Supports interpolation. |
| Route mandatory | Messages are rejected if the route does not exist when set to `true`. Fails silently otherwise. |
| Route persistent | Messages are marked as persistent, instructing the broker to write them to disk if the queue is durable. |
| Optional TTL (minutes) | Override the default queue time to live (TTL), in minutes, for messages to be persisted. |

## Related Topics

- [Overview](https://ably.com/docs/platform/integrations/streaming.md): Outbound streaming integrations enable you to stream data from Ably to an external service for realtime processing.
- [Kafka](https://ably.com/docs/platform/integrations/streaming/kafka.md): Send data to Kafka based on message, channel lifecycle, channel occupancy, and presence events.
- [Kinesis](https://ably.com/docs/platform/integrations/streaming/kinesis.md): Send data to Kinesis based on message, channel lifecycle, channel occupancy, and presence events.
- [SQS](https://ably.com/docs/platform/integrations/streaming/sqs.md): Send data to SQS based on message, channel lifecycle, channel occupancy, and presence events.
- [Pulsar](https://ably.com/docs/platform/integrations/streaming/pulsar.md): Send data to Pulsar based on message, channel lifecycle, channel occupancy, and presence events.
- [DataDog](https://ably.com/docs/platform/integrations/streaming/datadog.md): Connect Ably and Datadog to monitor messages, channels, and connections in realtime, integrating your Ably statistics with your existing Datadog setup.

## Documentation Index

To discover additional Ably documentation:

1. Fetch [llms.txt](https://ably.com/llms.txt) for the canonical list of available pages.
2. Identify relevant URLs from that index.
3. Fetch target pages as needed.

Avoid using assumed or outdated documentation paths.
