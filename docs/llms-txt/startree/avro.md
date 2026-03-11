# Source: https://docs.startree.ai/corecapabilities/ingestdata/adv-concepts/realtime/decoders/avro.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Avro Message Decoder

Avro message decoder is used for **real-time ingestion** in Pinot when consuming **Avro-encoded messages** from Kafka topics that use **Confluent Schema Registry**.

### Class

`org.apache.pinot.plugin.inputformat.avro.confluent.KafkaConfluentSchemaRegistryAvroMessageDecoder`

## When to Use

Use this decoder when:

* Kafka messages are serialized using **Avro format**.
* Kafka messages must be Avro-encoded binary payloads and the schema must be registered in Confluent Schema Registry. Pinot uses the registry to deserialize the messages correctly.
* A **Confluent Schema Registry** is managing your Avro schemas.

### Configuration Example

Include it in your `streamConfig` section:

```json  theme={null}
"streamConfig": {
  "streamType": "kafka",
  "stream.kafka.topic.name": "orders_topic",
  "stream.kafka.consumer.type": "lowlevel",
  "stream.kafka.decoder.class.name": "org.apache.pinot.plugin.inputformat.avro.confluent.KafkaConfluentSchemaRegistryAvroMessageDecoder",
  "stream.kafka.broker.list": "broker:9092",
  "stream.kafka.decoder.prop.schema.registry.url": "http://schema-registry:8081"
}
```

## Decoder Behavior

* Automatically fetches and caches Avro schemas from the registry.
* Deserializes messages based on the schema ID embedded in the message.
* Converts Avro records into Pinot-compatible rows.
* Drops fields not present in the Pinot schema.
* Avoid nested records - flatten them before ingestion if needed.
* Use nullHandlingEnabled if fields might be missing or optional.

Built with [Mintlify](https://mintlify.com).
