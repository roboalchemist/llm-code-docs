# Source: https://docs.startree.ai/corecapabilities/ingestdata/adv-concepts/realtime/decoders/protobuf.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Protobuf Message Decoder

Protobuf message decoder is used in **real-time ingestion** to handle **Protobuf-encoded messages** from Kafka topics using the **Confluent Schema Registry** for schema management.

### Class

`org.apache.pinot.plugin.inputformat.protobuf.KafkaConfluentSchemaRegistryProtoBufMessageDecoder`

***

## When to Use

Use this decoder when:

* The Kafka messages are serialized using **Protocol Buffers (Protobuf)**.
* The schema must be registered in the Confluent Schema Registry.
* You need to ingest structured Protobuf data into a Pinot real-time table.

***

## Configuration Example

Specify this decoder in the `streamConfig` of your table config:

```json  theme={null}
"streamConfig": {
  "streamType": "kafka",
  "stream.kafka.topic.name": "metrics_topic",
  "stream.kafka.consumer.type": "lowlevel",
  "stream.kafka.decoder.class.name": "org.apache.pinot.plugin.inputformat.protobuf.KafkaConfluentSchemaRegistryProtoBufMessageDecoder",
  "stream.kafka.broker.list": "broker:9092",
  "stream.kafka.decoder.prop.schema.registry.url": "http://schema-registry:8081"
}
```

## Decoder Behavior

* Retrieves and caches Protobuf schemas from the Schema Registry.
* Uses the schema to parse Protobuf messages into column-value pairs.
* The decoder fetches the schema dynamically using the schema ID in the message payload.
* Ignores fields not defined in the Pinot schema.
* Supports nested fields if flattened before ingestion.
* Enable nullHandlingEnabled for optional fields.

Built with [Mintlify](https://mintlify.com).
