# Source: https://docs.startree.ai/corecapabilities/ingestdata/dataportal/streaming/kinesis.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to Amazon Kinesis

> Create a connection to ingest real-time data from Amazon Kinesis.

## Step 1: In the Data Portal, click Tables and then click Create Table

## Step 2: Select Kinesis as the Data Source

## Step 3: Create a New Connection

Click **New Connection**. If you want to use an existing connection, select the connection from the list and proceed to **Step 5**.

Enter a **Source Name** for the new connection and specify the **Broker URL**.

## Step 4: Configure Connection Parameters

### Connect Kinesis Using Basic Authentication

Use the following JSON configuration when Kinesis is set up with **basic authentication** using an **access key** and **secret key**.

```json  theme={null}
{
  "region": "us-west-1",
  "accessKey": "AKIAEXAMPLEACCESSKEY",
  "secretKey": "SECRETKEYEXAMPLE12345"
}
```

#### Property Descriptions

| Property    | Required | Description                                                              |
| ----------- | -------- | ------------------------------------------------------------------------ |
| `region`    | Yes      | The AWS region (e.g., `us-east-1`) where the Kinesis stream is located.  |
| `accessKey` | Yes      | The AWS access key used for authentication.                              |
| `secretKey` | Yes      | The AWS secret key used for authentication (paired with the access key). |

### Connecting to Kinesis Using IAM-Based Authentication

Please follow [these steps](/corecapabilities/ingestdata/recipes/iam-role-kinesis) to create IAM role for Kinesis setup.

Use the following JSON configuration when Kinesis is set up with IAM-based authentication by assuming an IAM Role for secure access.

```json  theme={null}
{
  "region": "us-west-1",
  "iamRoleBasedAccessEnabled" : "true",
  "roleArn": "arn:aws:iam::123456789012:role/PinotKinesisIngestionRole",
  "roleSessionName": "pinot_session"
}
```

#### Property Descriptions

| Property                    | Required | Description                                                                                                                                                                      |
| --------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `region`                    | Yes      | The AWS region (e.g., `us-east-1`) where the Kinesis stream is located.                                                                                                          |
| `iamRoleBasedAccessEnabled` | Yes      | Mark it as true, when IAM role based authentication is used.                                                                                                                     |
| `roleArn`                   | Yes      | ARN of the IAM role Pinot will assume to access Kinesis                                                                                                                          |
| `roleSessionName`           | Yes      | An identifier used when assuming an IAM role via AWS Security Token Service to access the Kinesis stream securely. It can help track usage in AWS CloudTrail logs, metrics, etc. |

## Step 5: Test the Connection and Configure Data Ingestion

After configuring the connection properties, test the connection to ensure it functions properly. Once the connection is successful, configure the additional data settings using the following JSON format:

```json  theme={null}
{
  "shardIteratorType": "TRIM_HORIZON",
  "stream.kinesis.topic.name": "topic-name",
  "stream.kinesis.decoder.prop.format": "Message-Format-Type",
  "stream.kinesis.decoder.class.name": "org.apache.pinot.plugin.inputformat.json.JSONMessageDecoder",
  "stream.kinesis.consumer.factory.class.name": "org.apache.pinot.plugin.stream.kinesis.KinesisConsumerFactory"
}
```

### Property Descriptions

| Property                                     | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `shardIteratorType`                          | No       | The shardIteratorType defines where consumption starts. Use LATEST to read only new records, or TRIM\_HORIZON to start from the earliest. Default is TRIM\_HORIZON.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `stream.kinesis.topic.name`                  | Yes      | The name of the Kinesis topic from which Pinot will consume data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `stream.kinesis.decoder.prop.format`         | Yes      | The format of the Kinesis messages. Supported values include **csv, json, avro, protobuf, parquet**, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `stream.kinesis.decoder.class.name`          | Yes      | The class name of the decoder used for Kinesis message parsing. It is set based on the message format and schema.     <br />**Examples:**<br />\* For JSON Messages: `org.apache.pinot.plugin.inputformat.json.JSONMessageDecoder`     <br />\* For AVRO Messages: `org.apache.pinot.plugin.inputformat.avro.confluent.KafkaConfluentSchemaRegistryAvroMessageDecoder` <br />\* For PROTO Messages: `org.apache.pinot.plugin.inputformat.protobuf.KafkaConfluentSchemaRegistryProtoBufMessageDecoder`<br /><br />See [Message Decoders](/corecapabilities/ingestdata/adv-concepts/realtime/decoders/overview) for more information. |
| `stream.kinesis.consumer.factory.class.name` | Yes      | The Kinesis consumer factory class to use. The default class is `org.apache.pinot.plugin.stream.kinesis.KinesisConsumerFactory` for AWS Kinesis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

### Configure Record Reader

<AccordionGroup>
  <Accordion title="AVRO">
    One configuration option `AvroRecordReaderConfig` is supported.

    * *enableLogicalTypes*: Enable logical type conversions for specific Avro logical types, such as DECIMAL, UUID, DATE, TIME\_MILLIS, TIME\_MICROS, TIMESTAMP\_MILLIS, and TIMESTAMP\_MICROS.

    ```bash  theme={null}
    {
      "enableLogicalTypes": "true"
    }
    ```

    For example, if the schema type is INT, logical type is DATE, the conversion applied is a TimeConversion, and the value is V; then a date is generated V days from epoch start.
  </Accordion>
</AccordionGroup>

## Step 6: Preview the Data

Click Show Sample Data to preview the source data before finalizing the configuration.

<Card title="Next Step" icon="forward-step" iconType="solid" href="/corecapabilities/ingestdata/dataportal/data-modeling/overview">
  Proceed with [Data Modeling](/corecapabilities/ingestdata/dataportal/data-modeling/overview).
</Card>

## FAQs

### Why should I use **Provisioned** mode instead of **On-Demand** for Kinesis when integrating with StarTree?

We recommend configuring Kinesis in **Provisioned** mode, rather than **On-Demand** mode, when using it as a source for StarTree ingestion pipelines. Here's why:

#### 🟠 On-Demand Mode

* **Automatic Scaling**: Manages shards dynamically to meet demand—no manual provisioning needed.
* **Pay-as-you-go**: Charges are based on actual throughput (reads and writes).
* **Best for**: Applications with unpredictable or spiky traffic patterns.
* **Auto-Scaling Limit**: Can scale up to **2×** the peak write throughput observed over the past 30 days.

> While On-Demand mode is flexible, it can make capacity planning opaque and may lead to surprises in performance or billing when dealing with sustained, high-throughput ingestion.

***

#### ✅ Provisioned Mode (Recommended)

* **Manual Shard Management**: You define the number of shards explicitly.
* **Fixed Capacity and Cost**: Billed based on shard count, regardless of actual usage.
* **Best for**: Workloads with predictable, steady traffic where throughput can be estimated.
* **Manual Scaling**: You are responsible for increasing/decreasing shard count as needed.

> Provisioned mode offers **greater predictability, control, and stability**, which is important when tuning for ingestion throughput, latency, and cost efficiency in a real-time analytics platform like StarTree.

Built with [Mintlify](https://mintlify.com).
