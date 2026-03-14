# Source: https://docs.startree.ai/corecapabilities/ingestdata/adv-concepts/realtime/decoders/json.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# JSON Message Decoder

The JSON message decoder is used in **real-time ingestion** to **decode JSON-formatted messages** from Kafka topic and convert them into Pinot rows.

### Class

`org.apache.pinot.plugin.inputformat.json.JSONMessageDecoder`

## Configuration Example

Define it in your `streamConfig` within the table config:

```json  theme={null}
"streamConfig": {
  "streamType": "kafka",
  "stream.kafka.topic.name": "events_topic",
  "stream.kafka.consumer.type": "lowlevel",
  "stream.kafka.decoder.class.name": "org.apache.pinot.plugin.inputformat.json.JSONMessageDecoder",
  "stream.kafka.broker.list": "broker:9092"
}
```

## Decoder Behavior

* Parses JSON strings using a fast JSON library (e.g., Jackson/Gson).
* Converts each key-value pair into Pinot column values.
* Logs and skips invalid or malformed messages.

Built with [Mintlify](https://mintlify.com).
