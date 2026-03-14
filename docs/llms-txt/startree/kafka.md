# Source: https://docs.startree.ai/corecapabilities/ingestdata/dataportal/streaming/kafka.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to Apache Kafka

> Create a connection to stream real-time events using Apache Kafka.

## Step 1: In the Data Portal, click Tables and then click Create Table

## Step 2: Select Kafka as the Data Source

## Step 3: Create a New Connection

Click **New Connection**. If you want to use an existing connection, select the connection from the list and proceed to **Step 5**.

Enter a **Source Name** for the new connection and specify the **Broker URL**.

Select the **Security Protocol** to be used for authentication, from the drop-down list.

## Step 4: Configure Connection Parameters

Add the connection parameters according to your authentication method.

### Connecting to Kafka with No Authentication

Use the following connection JSON when connecting to Kafka without authentication.

```json  theme={null}
   {
      "stream.kafka.broker.list": "<broker_list>",
      "security.protocol": "PLAIN_TEXT"
   }
```

#### Property Descriptions

| Property Name            | Required | Description                                                                           |
| ------------------------ | -------- | ------------------------------------------------------------------------------------- |
| stream.kafka.broker.list | Yes      | List of Kafka brokers to connect to, typically in the format host1:port1,host2:port2. |
| security.protocol        | Yes      | Defines the security protocol used to connect to Kafka (e.g., PLAIN\_TEXT).           |

### Connecting to Kafka with SASL\_PLAINTEXT or SASL\_SSL Security Protocol

Use the following connection JSON when Kafka is configured with the SASL\_PLAINTEXT or SASL\_SSL security protocol enabled.

```json  theme={null}
   {
      "streamType": "kafka",
      "stream.kafka.broker.list": "",
      "security.protocol": "",
      "sasl.mechanism": "",
      "stream.kafka.password": "",
      "stream.kafka.username": "",
      "sasl.jaas.config": "org.apache.kafka.common.security.plain.PlainLoginModule required \n username=\"\" \n password=\"\";"
   }
```

#### Property Descriptions

| Property Name            | Required                                                               | Description                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------ | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| stream.kafka.broker.list | Yes                                                                    | List of Kafka brokers to connect to, typically in the format host1:port1,host2:port2.                                                                                                                                                                                                                                                                                                 |
| security.protocol        | Yes                                                                    | The security protocol used to connect to Kafka (for example, SASL\_SSL, PLAINTEXT). This parameter is mandatory when the Kafka cluster uses SASL.                                                                                                                                                                                                                                     |
| sasl.mechanism           | Yes                                                                    | The SASL mechanism for authentication (for example, PLAIN, SCRAM-SHA-256, SCRAM-SHA-512). This parameter is required when security.protocol is set to SASL\_SSL or SASL\_PLAINTEXT.                                                                                                                                                                                                   |
| stream.kafka.username    | Required when security.protocol is set to SASL\_SSL or SASL\_PLAINTEXT | The user name for authenticating with Kafka.                                                                                                                                                                                                                                                                                                                                          |
| stream.kafka.password    | Required when security.protocol is set to SASL\_SSL or SASL\_PLAINTEXT | The password for authenticating with Kafka.                                                                                                                                                                                                                                                                                                                                           |
| sasl.jaas.config         | Required when security.protocol is set to SASL\_SSL or SASL\_PLAINTEXT | The JAAS configuration string for SASL authentication. <br /><br />When the PLAIN SASL Mechanism is used: "org.apache.kafka.common.security.plain.PlainLoginModule required \n username="" \n password="";" <br /><br />When the SCRAM SASL Mechanism is used:<br />"org.apache.kafka.common.security.scram.ScramLoginModule required \n username="USERNAME" \n password="PASSWORD";" |

### Connecting to Kafka with SSL Security Protocol

See [prerequisites for SSL](/corecapabilities/ingestdata/dataportal/streaming/kafka-ssl-prerequisites) for steps to obtain the bootstrap server endpoint, the server certificate, the client certificate, and the client key, and to update an SSL certificate.

#### One-way SSL (Server Authentication)

In one-way SSL, only the server presents its SSL certificate to the client to prove its identity. The client verifies the server’s certificate using a trusted Certificate Authority (CA) before establishing an encrypted connection.
Use the following connection JSON when Kafka is configured with the SSL security protocol enabled:

```json  theme={null}
{
  "stream.kafka.broker.list": "",
  "security.protocol": "SSL",

  "ssl.truststore.location": "<path to truststore file>",
  "ssl.truststore.password": "<truststore password>",

  "stream.kafka.ssl.server.certificate": "<base64 encoded server certificate file>"
}
```

#### Two-way SSL (Mutual Authentication)

In two-way SSL, both the client and the server present certificates to authenticate each other. The server verifies the client’s certificate, and the client verifies the server’s certificate. This setup provides a higher level of security and trust, commonly used.
Use the following connection JSON when Kafka is configured with the SSL security protocol enabled:

```json  theme={null}
{
  "stream.kafka.broker.list": "",
  "security.protocol": "SSL",

  "ssl.truststore.location": "<path to truststore file>",
  "ssl.truststore.password": "<truststore password>",

  "ssl.keystore.location":"<path to keystore file>",
  "ssl.keystore.password":"<keystore password>",
  "ssl.key.password":"<key password>",

  "stream.kafka.ssl.server.certificate": "<base64 encoded server certificate file>",
  "stream.kafka.ssl.client.certificate": "<base64 encoded client certificate file>",
  "stream.kafka.ssl.client.key": "<base64 encoded client key file>",
}
```

<Note>
  The values for the ssl properties (server/client certificate, key) need to be base64 encoded.
</Note>

#### Property Descriptions

| Property                              | Required                | Description                                                                                                                                                                                             |
| ------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `stream.kafka.broker.list`            | Yes                     | List of Kafka brokers to connect to, typically in the format `host1:port1,host2:port2`.                                                                                                                 |
| `security.protocol`                   | Yes                     | Defines the security protocol used to connect to Kafka (e.g., `SASL_SSL`, `SSL`, `PLAINTEXT`). This parameter is mandatory when the Kafka cluster uses SSL or SASL.                                     |
| `ssl.truststore.location`             | Yes                     | Absolute path to the truststore file that contains trusted CA certificates (used to verify Kafka broker certificates).                                                                                  |
| `ssl.truststore.password`             | Yes                     | Password to open the truststore file.                                                                                                                                                                   |
| `stream.kafka.ssl.server.certificate` | Required in one-way SSL | Server Certificate for connecting to a Kafka cluster secured with SSL. Required when `security.protocol` is set to `SSL`. It needs to be Base64 encoded.                                                |
| `stream.kafka.ssl.client.certificate` | Required in two-way SSL | Client Certificate for connecting to a Kafka cluster secured with SSL. Required when `security.protocol` is set to `SSL`. It needs to be Base64 encoded.                                                |
| `stream.kafka.ssl.client.key`         | Required in two-way SSL | Certificate for connecting to a Kafka cluster secured with SSL. Required when `security.protocol` is set to `SSL` and `stream.kafka.ssl.client.certificate` is also set. It needs to be Base64 encoded. |
| `ssl.keystore.location`               | Required in two-way SSL | Path to the keystore file containing the client’s certificate and private key.                                                                                                                          |
| `ssl.keystore.password`               | Required in two-way SSL | Password to open the keystore file.                                                                                                                                                                     |
| `ssl.key.password`                    | Required in two-way SSL | Password protecting the private key inside the keystore.                                                                                                                                                |

## Step 5: Test the Connection and Configure Data Ingestion

After you have configured the connection properties, test the connection to ensure it is working.

When the connection is successful, use the following JSON to configure the source’s Kafka topic and data format:

```json  theme={null}
{
  "stream.kafka.decoder.prop.format": "",
  "stream.kafka.decoder.class.name": "",
  "stream.kafka.topic.name": "",
  "stream.kafka.consumer.type": "lowlevel",
  "stream.kafka.consumer.factory.class.name": "ai.startree.pinot.plugin.stream.kafka20.ConfluentKafkaConsumerFactory",
  "stream.kafka.consumer.prop.auto.offset.reset": "smallest"
}
```

### Property Descriptions

| Property                                       | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `stream.kafka.decoder.prop.format`             | Yes      | Format of the messages in Kafka. Supported values include `json`, `avro`, `proto` etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `stream.kafka.decoder.class.name`              | Yes      | The class name of the decoder used for Kafka message parsing. It is set based on the message format and schema.    <br />**Examples:** <br />\* For JSON Messages use `org.apache.pinot.plugin.inputformat.json.JSONMessageDecoder`     <br />\* For AVRO Messages use `org.apache.pinot.plugin.inputformat.avro.confluent.KafkaConfluentSchemaRegistryAvroMessageDecoder` <br />\* For PROTO Messages use `org.apache.pinot.plugin.inputformat.protobuf.KafkaConfluentSchemaRegistryProtoBufMessageDecoder`<br /><br />See [Message Decoders](/corecapabilities/ingestdata/adv-concepts/realtime/decoders/overview) for more information. |
| `stream.kafka.topic.name`                      | Yes      | The name of the Kafka topic from which Pinot will consume data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `stream.kafka.consumer.type`                   | No       | The type of Kafka consumer used in Apache Pinot. Use `lowlevel` for granular control of partitions and offsets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `stream.kafka.consumer.factory.class.name`     | Yes      | The Kafka consumer factory class to use. The specified class `ai.startree.pinot.plugin.stream.kafka20.ConfluentKafkaConsumerFactory` is the default Kafka consumer factory when using Kafka 2.0+ or Confluent Kafka clients.     <br /><br />Use `ai.startree.pinot.plugin.stream.kafka10.ConfluentKafkaConsumerFactory` for legacy Kafka (1.x) environments with Confluent client integration.                                                                                                                                                                                                                                            |
| `stream.kafka.consumer.prop.auto.offset.reset` | Yes      | The behavior when no committed offset exists or offsets are invalid (`smallest`, `latest`, `none`). Use `smallest` for backfilling or consuming all historical data. Use `latest` for real-time streaming.                                                                                                                                                                                                                                                                                                                                                                                                                                 |

#### Additional Configuration

The parameters mentioned above are the **minimum-required parameters** to establish the connection. Apache Pinot also provides additional configuration options to fine-tune and control the ingestion process. For a complete list of configuration parameters, refer to the [Apache Pinot documentation](https://docs.pinot.apache.org/basics/data-import/pinot-stream-ingestion/import-from-apache-kafka#consume-transactionally-committed-messages). In addition, [Kafka Consumer properties](https://kafka.apache.org/documentation/#consumerconfigs) can also be used.

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

  <Accordion title="PROTO">
    `ProtoBufRecordReaderConfig` exists in Pinot and the following configuration is possible.

    ```bash  theme={null}
    {
      "descriptorFile": "/path/to/descriptor/file"
    }
    ```
  </Accordion>
</AccordionGroup>

## Step 6: Preview the Sample Data

Click **Show Sample Data** to see a preview of the source data.

<Card title="Next Step" icon="forward-step" iconType="solid" href="/corecapabilities/ingestdata/dataportal/data-modeling/overview">
  Proceed with [Data Modeling](/corecapabilities/ingestdata/dataportal/data-modeling/overview).
</Card>

Built with [Mintlify](https://mintlify.com).
