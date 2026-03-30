# Source: https://docs.startree.ai/corecapabilities/ingestdata/dataportal/streaming/confluent.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to Confluent Cloud

> Create a connection to ingest from fully managed Kafka in Confluent Cloud.

## Step 1: In the Data Portal, click Tables and then click Create Table

## Step 2: Select Confluent Cloud as the Data Source

## Step 3: Create a New Connection

Click **New Connection**. If you want to use an existing connection, select the connection from the list and proceed to **Step 5**.

Enter a **Source Name** for the new connection and specify the **Broker URL**.

## Step 4: Configure Connection Parameters

Use the following JSON configuration:

```json  theme={null}
{
  "stream.kafka.broker.list": "abc-xyz05.region.aws.confluent.cloud:9092",
  "security.protocol": "SASL_SSL",
  "sasl.mechanism": "PLAIN",
  "stream.confluent.key": "AKIAEXAMPLEKEY",
  "stream.confluent.secret": "SECRETKEYEXAMPLE12345",
  "sasl.jaas.config": "org.apache.kafka.common.security.plain.PlainLoginModule required \n username=\"AKIAEXAMPLEKEY\" \n password=\"SECRETKEYEXAMPLE12345\";"
}
```

### Property Descriptions

| Property                   | Required | Description                                                                                                                                        |
| -------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `stream.kafka.broker.list` | Yes      | The list of Kafka brokers to connect to, typically in the format `host1:port1,host2:port2`. Required to establish a connection to Confluent Kafka. |
| `security.protocol`        | Yes      | The security protocol used to connect to Kafka (e.g., `SASL_SSL`). Mandatory when the Confluent Kafka cluster uses SASL.                           |
| `sasl.mechanism`           | Yes      | The SASL mechanism used for authentication. This value should be `PLAIN`.                                                                          |
| `stream.confluent.key`     | Yes      | The Confluent key for authentication.                                                                                                              |
| `stream.confluent.secret`  | Yes      | The Confluent secret for authentication.                                                                                                           |
| `sasl.jaas.config`         | Yes      | The JAAS configuration string for SASL authentication.                                                                                             |

## Step 5: Test the Connection and Configure Data Ingestion

After you have configured the connection properties, **test the connection** to ensure it functions properly.

Once the connection is successful, configure the additional data settings using the following JSON format:

```json  theme={null}
{
    "stream.kafka.topic.name": "",
    "stream.kafka.decoder.prop.format": "",
    "stream.kafka.decoder.class.name": "",
    "stream.kafka.consumer.type": "lowlevel",
    "stream.kafka.consumer.factory.class.name": "ai.startree.pinot.plugin.stream.kafka20.ConfluentKafkaConsumerFactory",
    "stream.kafka.consumer.prop.auto.offset.reset": "smallest",
    "stream.kafka.decoder.prop.schema": "",
    "stream.kafka.decoder.prop.schema.registry.rest.url": "",
    "stream.kafka.decoder.prop.schema.registry.schema.name": "",
    "stream.kafka.decoder.prop.schema.registry.key": "",
    "stream.confluent.schema.registry.secret": ""
}
```

### Property Descriptions

| Property                                                | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `stream.kafka.topic.name`                               | Yes      | The name of the Kafka topic from which Pinot will consume data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `stream.kafka.decoder.prop.format`                      | Yes      | The format of the input data. Supported values include **json, avro, proto**, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `stream.kafka.decoder.class.name`                       | Yes      | The class name of the decoder used for Kafka message parsing. Set based on the message format and schema. <br />**Examples:**<br />\* For JSON Messages: `org.apache.pinot.plugin.inputformat.json.JSONMessageDecoder`<br />\* For AVRO Messages: `org.apache.pinot.plugin.inputformat.avro.confluent.KafkaConfluentSchemaRegistryAvroMessageDecoder` <br />\* For PROTO Messages: `org.apache.pinot.plugin.inputformat.protobuf.KafkaConfluentSchemaRegistryProtoBufMessageDecoder`<br /><br />See [Message Decoders](/corecapabilities/ingestdata/adv-concepts/realtime/decoders/overview) for more information. |
| `stream.kafka.consumer.type`                            | No       | The type of Kafka consumer used in Apache Pinot. Use `lowlevel` for granular control of partitions and offsets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `stream.kafka.consumer.factory.class.name`              | Yes      | The Kafka consumer factory class to use. <br />The default class is `ai.startree.pinot.plugin.stream.kafka20.ConfluentKafkaConsumerFactory` for Kafka 2.0+ or Confluent Kafka clients.    <br /><br />Use `ai.startree.pinot.plugin.stream.kafka10.ConfluentKafkaConsumerFactory` for legacy Kafka (1.x) environments with Confluent client integration.                                                                                                                                                                                                                                                           |
| `stream.kafka.consumer.prop.auto.offset.reset`          | Yes      | Defines behavior when no committed offset exists or offsets are invalid.    **Options:** `smallest` (for backfilling or consuming all historical data), `latest` (for real-time streaming), or `none`.                                                                                                                                                                                                                                                                                                                                                                                                             |
| `stream.kafka.decoder.prop.schema`                      | No       | The schema definition that Pinot can use to deserialize and interpret Kafka messages during ingestion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `stream.kafka.decoder.prop.schema.registry.rest.url`    | No       | The URL endpoint of the Schema Registry service. This is required if the data type of message is either AVRO or PROTO                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `stream.kafka.decoder.prop.schema.registry.schema.name` | No       | The name of the schema to use for decoding Kafka messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `stream.kafka.decoder.prop.schema.registry.key`         | No       | The API key or identifier for authenticating with the Schema Registry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `stream.confluent.schema.registry.secret`               | No       | The secret (password) paired with the API key for Schema Registry authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## Step 6: Preview the sample Data

Click Show Sample Data to preview the source data before finalizing the configuration.

<Card title="Next Step" icon="forward-step" iconType="solid" href="/corecapabilities/ingestdata/dataportal/data-modeling/overview">
  Proceed with [Data Modeling](/corecapabilities/ingestdata/dataportal/data-modeling/overview).
</Card>

Built with [Mintlify](https://mintlify.com).
