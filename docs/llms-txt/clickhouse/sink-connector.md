# Source: https://clickhouse.ferndocs.com/integrations/kafka/cloud/confluent/sink-connector.md

---
sidebar_label: Kafka Connector Sink on Confluent Cloud
sidebar_position: 2
slug: /integrations/kafka/cloud/confluent/sink-connector
description: Guide to using the fully managed ClickHouse Connector Sinkon Confluent Cloud
title: Integrating Confluent Cloud with ClickHouse
keywords:
  - Kafka
  - Confluent Cloud
doc_type: guide
integration:
  - support_level: core
  - category: data_ingestion
  - website: 'https://clickhouse.com/cloud/clickpipes'
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
* [ClickHouse Connector Sink](/integrations/kafka/clickhouse-kafka-connect-sink)
* Confluent Cloud

## The official Kafka connector from ClickHouse with Confluent Cloud [#the-official-kafka-connector-from-clickhouse-with-confluent-cloud]

#### Create a Topic [#create-a-topic]
Creating a topic on Confluent Cloud is fairly simple, and there are detailed instructions [here](https://docs.confluent.io/cloud/current/client-apps/topics/manage.html).

#### Important notes [#important-notes]

* The Kafka topic name must be the same as the ClickHouse table name. The way to tweak this is by using a transformer (for example [`ExtractTopic`](https://docs.confluent.io/platform/current/connect/transforms/extracttopic.html)).
* More partitions does not always mean more performance - see our upcoming guide for more details and performance tips.

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


#### Install Connector [#install-connector]
Install the fully managed ClickHouse Sink Connector on Confluent Cloud following the [official documentation](https://docs.confluent.io/cloud/current/connectors/cc-clickhouse-sink-connector/cc-clickhouse-sink.html).

#### Configure the Connector [#configure-the-connector]
During the configuration of the ClickHouse Sink Connector, you will need to provide the following details:
- hostname of your ClickHouse server
- port of your ClickHouse server (default is 8443)
- username and password for your ClickHouse server
- database name in ClickHouse where the data will be written
- topic name in Kafka that will be used to write data to ClickHouse

The Confluent Cloud UI supports advanced configuration options to adjust poll intervals, batch sizes, and other parameters to optimize performance.

#### Known limitations [#known-limitations]
* See the list of [Connectors limitations in the official docs](https://docs.confluent.io/cloud/current/connectors/cc-clickhouse-sink-connector/cc-clickhouse-sink.html#limitations)
