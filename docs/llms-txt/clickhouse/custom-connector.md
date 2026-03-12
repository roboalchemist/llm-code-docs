# Source: https://clickhouse.ferndocs.com/integrations/kafka/cloud/confluent/custom-connector.md

---
sidebar_label: Kafka Connector Sink on Confluent Platform
sidebar_position: 3
slug: /integrations/kafka/cloud/confluent/custom-connector
description: Using ClickHouse Connector Sink with Kafka Connect and ClickHouse
title: Integrating Confluent Cloud with ClickHouse
keywords:

- Confluent ClickHouse integration
- ClickHouse Kafka connector
- Kafka Connect ClickHouse sink
- Confluent Platform ClickHouse
- custom connector Confluent
doc_type: guide

---

<div class='vimeo-container'>
  <iframe src="//www.youtube.com/embed/SQAiPVbd3gg"
    width="640"
    height="360"
    frameborder="0"
    allow="autoplay;
    fullscreen;
    picture-in-picture"
    allowfullscreen>
  </iframe>
</div>

## Prerequisites [#prerequisites]

We assume you are familiar with:
- [ClickHouse Connector Sink](/integrations/kafka/clickhouse-kafka-connect-sink)
- Confluent Platform and [Custom Connectors](https://docs.confluent.io/cloud/current/connectors/bring-your-connector/overview.html).

## The official Kafka connector from ClickHouse with Confluent Platform [#the-official-kafka-connector-from-clickhouse-with-confluent-platform]

### Installing on Confluent platform [#installing-on-confluent-platform]

This is meant to be a quick guide to get you started with the ClickHouse Sink Connector on Confluent Platform.
For more details, please refer to the [official Confluent documentation](https://docs.confluent.io/cloud/current/connectors/bring-your-connector/custom-connector-qs.html#uploading-and-launching-the-connector).

#### Create a Topic [#create-a-topic]

Creating a topic on Confluent Platform is fairly simple, and there are detailed instructions [here](https://docs.confluent.io/cloud/current/client-apps/topics/manage.html).

#### Important notes [#important-notes]

- The Kafka topic name must be the same as the ClickHouse table name. The way to tweak this is by using a transformer (for example [`ExtractTopic`](https://docs.confluent.io/platform/current/connect/transforms/extracttopic.html)).
- More partitions does not always mean more performance - see our upcoming guide for more details and performance tips.

#### Install connector [#install-connector]

You can download the connector from our [repository](https://github.com/ClickHouse/clickhouse-kafka-connect/releases) - please feel free to submit comments and issues there as well!

Navigate to "Connector Plugins" -> "Add plugin" and using the following settings:

```text
'Connector Class' - 'com.clickhouse.kafka.connect.ClickHouseSinkConnector'
'Connector type' - Sink
'Sensitive properties' - 'password'. This will ensure entries of the ClickHouse password are masked during configuration.
```

Example:
<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7ff18d4f9af199cf64e4468691428759e9f64b7c6bc51ded42c988a1832308ef/images/integrations/data-ingestion/kafka/confluent/AddCustomConnectorPlugin.png" alt="Confluent Platform UI showing settings for adding a custom ClickHouse connector"/>

#### Gather your connection details [#gather-your-connection-details]

To connect to ClickHouse with HTTP(S) you need this information:

| Parameter(s)            | Description                                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------------------------|
|`HOST` and `PORT`        | Typically, the port is 8443 when using TLS or 8123 when not using TLS.                                        |
|`DATABASE NAME`          | Out of the box, there is a database named `default`, use the name of the database that you want to connect to.|
|`USERNAME` and `PASSWORD`| Out of the box, the username is `default`. Use the username appropriate for your use case.                    |

The details for your ClickHouse Cloud service are available in the ClickHouse Cloud console.
Select a service and click **Connect**:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9de2a784fe6ef2c5c51be720b96cb4bb7ebd0838901449759f587e0df6d9034a/images/_snippets/cloud-connect-button.png" alt="ClickHouse Cloud service connect button" />

Choose **HTTPS**. Connection details are displayed in an example `curl` command.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/710d528cac4deb00e877550b033fe8d67e19e1a8f825c75889eb0573ab25f7b0/images/_snippets/connection-details-https.png" alt="ClickHouse Cloud HTTPS connection details" />

If you are using self-managed ClickHouse, the connection details are set by your ClickHouse administrator.

#### Configure the connector [#configure-the-connector]

Navigate to `Connectors` -> `Add Connector` and use the following settings (note that the values are examples only):

```json
{
  "database": "<DATABASE_NAME>",
  "errors.retry.timeout": "30",
  "exactlyOnce": "false",
  "schemas.enable": "false",
  "hostname": "<CLICKHOUSE_HOSTNAME>",
  "password": "<SAMPLE_PASSWORD>",
  "port": "8443",
  "ssl": "true",
  "topics": "<TOPIC_NAME>",
  "username": "<SAMPLE_USERNAME>",
  "key.converter": "org.apache.kafka.connect.storage.StringConverter",
  "value.converter": "org.apache.kafka.connect.json.JsonConverter",
  "value.converter.schemas.enable": "false"
}
```

#### Specify the connection endpoints [#specify-the-connection-endpoints]

You need to specify the allow-list of endpoints that the connector can access.
You must use a fully-qualified domain name (FQDN) when adding the networking egress endpoint(s).
Example: `u57swl97we.eu-west-1.aws.clickhouse.com:8443`

<Note>
You must specify HTTP(S) port. The Connector doesn't support Native protocol yet.
</Note>

[Read the documentation.](https://docs.confluent.io/cloud/current/connectors/bring-your-connector/custom-connector-qs.html#cc-byoc-endpoints)

You should be all set!

#### Known limitations [#known-limitations]
- Custom Connectors must use public internet endpoints. Static IP addresses aren't supported.
- You can override some Custom Connector properties. See the fill [list in the official documentation.](https://docs.confluent.io/cloud/current/connectors/bring-your-connector/custom-connector-manage.html#override-configuration-properties)
- Custom Connectors are available only in [some AWS regions](https://docs.confluent.io/cloud/current/connectors/bring-your-connector/custom-connector-fands.html#supported-aws-regions)
- See the list of [Custom Connectors limitations in the official docs](https://docs.confluent.io/cloud/current/connectors/bring-your-connector/custom-connector-fands.html#limitations)
