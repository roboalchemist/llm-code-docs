# Source: https://docs.startree.ai/corecapabilities/ingestdata/dataportal/streaming/aws_msk.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to MSK - Managed Apache Kafka by AWS

## Step 1: In the Data Portal, click Tables and then click Create Table

## Step 2: Select **Custom** as the Data Source

Native support for AWS MSK is coming soon.

## Step 3: Create a New Connection

Select "Streaming" as the Data Source Category.

### Connect to AWS MSK Using IAM-Based SASL Authentication

Use the following JSON configuration when MSK is set up with IAM-based SASL authentication (AWS\_MSK\_IAM) and TLS (SASL\_SSL).

```json  theme={null}
{
  "authentication.type": "SASL",
  "security.protocol": "SASL_SSL",
  "sasl.mechanism": "AWS_MSK_IAM",
  "sasl.jaas.config": "org.apache.pinot.shaded.software.amazon.msk.auth.iam.IAMLoginModule required awsRoleArn=\"<arn:aws:iam::account-id:role/aws-arn-name>\";",
  "sasl.client.callback.handler.class": "org.apache.pinot.shaded.software.amazon.msk.auth.iam.IAMClientCallbackHandler",
  "stream.kafka.broker.list": "b-1.example.amazonaws.com:9098,b-2.example.amazonaws.com:9098",
  "stream.kafka.topic.name": "sample_topic",
  "stream.kafka.consumer.type": "lowlevel",
  "stream.kafka.consumer.factory.class.name": "org.apache.pinot.plugin.stream.kafka20.KafkaConsumerFactory",
  "stream.kafka.decoder.class.name": "org.apache.pinot.plugin.inputformat.json.JSONMessageDecoder",
  "stream.kafka.decoder.prop.format": "JSON",
  "stream.kafka.consumer.prop.auto.offset.reset": "smallest",
  "realtime.segment.flush.threshold.rows": "0",
  "realtime.segment.flush.threshold.segment.size": "200M",
  "realtime.segment.flush.threshold.time": "24h"
}
```

### Property Descriptions

| Property                                        | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `authentication.type`                           | Yes      | Authentication mode for Kafka/MSK. Set to `SASL` to enable SASL-based authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `security.protocol`                             | Yes      | Kafka security protocol. Use `SASL_SSL` to enable TLS + SASL for MSK IAM authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `sasl.mechanism`                                | Yes      | SASL mechanism. For AWS MSK IAM-based auth, set to `AWS_MSK_IAM`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `sasl.jaas.config`                              | Yes      | JAAS configuration string for the IAM login module. Must use `org.apache.pinot.shaded.software.amazon.msk.auth.iam.IAMLoginModule` and specify `awsRoleArn` (or equivalent credentials strategy).                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `sasl.client.callback.handler.class`            | Yes      | Callback handler implementation for MSK IAM authentication. Use `org.apache.pinot.shaded.software.amazon.msk.auth.iam.IAMClientCallbackHandler`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `stream.kafka.broker.list`                      | Yes      | Comma-separated list of MSK bootstrap brokers with ports. Example: `b-1.example.amazonaws.com:9098,b-2.example.amazonaws.com:9098`. Should match the Broker URL / bootstrap servers configured in the UI.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `stream.kafka.topic.name`                       | Yes      | Name of the MSK topic to consume from. Example: `sample_topic`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `stream.kafka.consumer.type`                    | No       | Kafka consumer mode. `lowlevel` uses Pinot’s low level consumer for fine-grained partition/offset control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `stream.kafka.consumer.factory.class.name`      | Yes      | Kafka consumer factory implementation. For Kafka 2.0+ clusters (including MSK), use `org.apache.pinot.plugin.stream.kafka20.KafkaConsumerFactory`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `stream.kafka.decoder.class.name`               | Yes      | The class name of the decoder used for Kafka message parsing. It is set based on the message format and schema.    <br />**Examples:** <br />\* For JSON Messages use `org.apache.pinot.plugin.inputformat.json.JSONMessageDecoder`     <br />\* For AVRO Messages use `org.apache.pinot.plugin.inputformat.avro.confluent.KafkaConfluentSchemaRegistryAvroMessageDecoder` <br />\* For PROTO Messages use `org.apache.pinot.plugin.inputformat.protobuf.KafkaConfluentSchemaRegistryProtoBufMessageDecoder`<br /><br />See [Message Decoders](/corecapabilities/ingestdata/adv-concepts/realtime/decoders/overview) for more information. |
| `stream.kafka.decoder.prop.format`              | Yes      | Format of the messages in Kafka. Supported values include `json`, `avro`, `proto` etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `stream.kafka.consumer.prop.auto.offset.reset`  | No       | Defines starting offset if there is no committed one. `smallest` (Kafka 0.8-style) = earliest offset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `realtime.segment.flush.threshold.rows`         | Yes\*    | Row-based flush threshold. `0` disables row-based flushing and makes size/time the only triggers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `realtime.segment.flush.threshold.segment.size` | Yes      | Target segment size before flush (e.g., `200M`). Controls memory usage and segment count.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `realtime.segment.flush.threshold.time`         | Yes      | Maximum time before a segment flush, even if row/size thresholds aren’t met. Example: `24h`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ⸻                                               |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## Step 6: Preview the Sample Data

Click **Show Sample Data** to see a preview of the source data.

<Card title="Next Step" icon="forward-step" iconType="solid" href="/corecapabilities/ingestdata/dataportal/data-modeling/overview">
  Proceed with [Data Modeling](/corecapabilities/ingestdata/dataportal/data-modeling/overview).
</Card>

Built with [Mintlify](https://mintlify.com).
