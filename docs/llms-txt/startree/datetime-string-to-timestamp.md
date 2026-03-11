# Source: https://docs.startree.ai/recipes/datetime-string-to-timestamp.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Converting DateTime Strings to Timestamps

In this recipe we'll learn how to import DateTime strings into Pinot.

| Pinot Version | 1.0.0                                                                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Code          | [startreedata/pinot-recipes/datetime-string-to-timestamp](https://github.com/startreedata/pinot-recipes/tree/main/recipes/datetime-string-to-timestamp) |

## Prerequisites

To follow the code examples in this guide, you must [install Docker](https://docs.docker.com/get-docker/) locally and download recipes.

## Navigate to recipe

1. If you haven't already, download recipes.
2. In terminal, go to the recipe by running the following command:

```bash  theme={null}
cd pinot-recipes/recipes/datetime-string-to-timestamp
```

## Launch Pinot Cluster and Kafka

You can spin up a Pinot Cluster and Kafka Broker by running the following command:

```bash  theme={null}
docker-compose up
```

This command will run a single instance of the Pinot Controller, Pinot Server, Pinot Broker, Kafka, and Zookeeper. You can find the [docker-compose.yml](https://github.com/startreedata/pinot-recipes/blob/main/recipes/datetime-string-to-timestamp/docker-compose.yml) file on GitHub.

## DateTime Strings in Pinot

Pinot automatically creates Timestamps from DateTime strings that are in the following format:

* `yyyy-mm-dd hh:mm:ss[.fffffffff]`
* Millis since epoch

If we have a DateTime value in another format we'll need to convert that value using a transformation function.

We're going to import the following message into Kafka:

```json  theme={null}
{
  "timestamp1": "2019-10-09 22:25:25", 
  "timestamp2": "1570656325000", 
  "timestamp3": "10/09/2019T22:25:25"
}
```

## Add Schema and Table

Now let's create a Pinot Schema and Table.

```json  theme={null}
{
  "schemaName": "dates",
  "dimensionFieldSpecs": [
    {"name": "Date1", "dataType": "TIMESTAMP"},
    {"name": "Date2", "dataType": "TIMESTAMP"},
    {"name": "Date3", "dataType": "TIMESTAMP"}
  ],
  "dateTimeFieldSpecs": [
    {
      "name": "Date4",
      "dataType": "TIMESTAMP",
      "format" : "1:MILLISECONDS:EPOCH",
      "granularity": "1:MILLISECONDS"
    }
  ]
}
```

*config/schema.json*

```json {15-20} theme={null}
{
  "tableName":"dates",
  "tableType":"REALTIME",
  "segmentsConfig":{
    "timeColumnName":"Date4",
    "schemaName":"dates",
    "replication":"1",
    "replicasPerPartition":"1"
  },
  "ingestionConfig":{
    "batchIngestionConfig":{
      "segmentIngestionType":"APPEND",
      "segmentIngestionFrequency":"DAILY"
    },
    "transformConfigs":[
      {"columnName":"Date1", "transformFunction":"timestamp1"},
      {"columnName":"Date2", "transformFunction":"timestamp2"},
      {"columnName":"Date3", "transformFunction": "FromDateTime(timestamp3, 'MM/dd/yyyy''T''HH:mm:ss')"},
      {"columnName":"Date4", "transformFunction":"timestamp1"}
    ]
  },
  "tableIndexConfig":{
    "loadMode":"MMAP",
    "streamConfigs":{
      "streamType":"kafka",
      "stream.kafka.topic.name":"dates",
      "stream.kafka.broker.list":"kafka-datetime:9093",
      "stream.kafka.consumer.type":"lowlevel",
      "stream.kafka.consumer.prop.auto.offset.reset":"smallest",
      "stream.kafka.consumer.factory.class.name":"org.apache.pinot.plugin.stream.kafka20.KafkaConsumerFactory",
      "stream.kafka.decoder.class.name":"org.apache.pinot.plugin.stream.kafka.KafkaJSONMessageDecoder"
    }
  },
  "tenants":{},
  "metadata":{}
}
```

*config/table.json*

This table has multiple transform configs defined that:

* Map `timestamp1` from the data source into the `Date1` column
* Map `timestamp2` from the data source into the `Date2` column
* Map `timestamp3` from the data source into the `Date3` column, with help from the  function.
* Map `timestamp4` from the data source into the `Date1` column

You can create the schema and table by running the following command:

```bash  theme={null}
docker run \
   --network datetime \
   -v $PWD/config:/config \
   apachepinot/pinot:1.0.0 AddTable   \
  -tableConfigFile /config/table.json   \
  -schemaFile /config/schema.json \
  -controllerHost "pinot-controller-datetime" \
  -exec
```

## Ingesting Data into Kafka

We can ingest a message into Kafka by running the following command:

````bash  theme={null}
```bash
printf '{"timestamp1": "2019-10-09 22:25:25", "timestamp2": "1570656325000", "timestamp3": "10/09/2019T22:25:25"}\n' |
kcat -P -b localhost:9092 -t dates
````

## Querying

Once that's completed, navigate to [localhost:9000/#/query](http://localhost:9000/#/query) and click on the dates table or copy/paste the following query:

```sql  theme={null}
select * 
from dates 
limit 10
```

You will see the following output:

| Date1                 | Date2                 | Date3                 | Date4                 |
| --------------------- | --------------------- | --------------------- | --------------------- |
| 2019-10-09 22:25:25.0 | 2019-10-09 21:25:25.0 | 2019-10-09 22:25:25.0 | 2019-10-09 22:25:25.0 |

*Query Results*

Built with [Mintlify](https://mintlify.com).
