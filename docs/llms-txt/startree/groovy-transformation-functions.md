# Source: https://docs.startree.ai/recipes/groovy-transformation-functions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Groovy Transformation Functions

In this recipe we'll learn how to use Groovy transformation functions to ingest a CSV file with column names contain spaces.

| Pinot Version | 1.0.0                                                                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Code          | [startreedata/pinot-recipes/groovy-transformation-functions](https://github.com/startreedata/pinot-recipes/tree/main/recipes/groovy-transformation-functions) |

## Prerequisites

To follow the code examples in this guide, you must [install Docker](https://docs.docker.com/get-docker/) locally and download recipes.

## Navigate to recipe

1. If you haven't already, download recipes.
2. Navigate to the recipe by running the following command:

```bash  theme={null}
cd pinot-recipes/recipes/groovy-transformation-functions
```

## Launch Pinot Cluster

You can spin up a Pinot Cluster and Kafka Broker by running the following command:

```bash  theme={null}
docker compose up
```

This command will run a single instance of the Pinot Controller, Pinot Server, Pinot Broker, Kafka Broker, and Zookeeper. You can find the [docker-compose.yml](https://github.com/startreedata/pinot-recipes/blob/main/recipes/groovy-transformation-functions/docker-compose.yml) file on GitHub.

## Controller configuration

We need to provide configuration parameters to the Pinot Controller to enable Groovy in transformation functions. This is done in the following section of the Docker Compose file:

```yml  theme={null}
pinot-controller:
  image: apachepinot/pinot:1.0.0
  command: "StartController -zkAddress zookeeper-grooy:2181 -config /config/controller-conf.conf"
```

The configuration is specified in `/config/controller-conf.conf`, the contents of which are shown below:

```conf  theme={null}
controller.access.protocols.http.port=9000
controller.zk.str=zookeeper-groovy:2181
controller.helix.cluster.name=PinotCluster
controller.host=pinot-controller-groovy
controller.port=9000
controller.data.dir=/tmp/data/PinotController

controller.disable.ingestion.groovy=false
```

*/config/controller-conf.conf*

## Dataset

We're going to import a couple of JSON documents into Kafka and then from there into Pinot.

<div class="text-output">
  ```json  theme={null}
  {"timestamp": "2019-10-09 21:25:25", "payload": {"firstName": "James", "lastName": "Smith", "before": {"id": 2}, "after": { "id": 3}}}
  {"timestamp": "2019-10-10 21:33:25", "payload": {"firstName": "John", "lastName": "Gates", "before": {"id": 2}}}
  ```
</div>

## Pinot Schema and Table

Now let's create a Pinot Schema and Table.

Only the *timestamp* field from our data source maps to a schema column name - we'll be using transformation functions to populate the *id* and *name* columns.

```json  theme={null}
{
    "schemaName": "events",
    "dimensionFieldSpecs": [
      {
        "name": "id",
        "dataType": "INT"
      },
      {
        "name": "name",
        "dataType": "STRING"
      }
    ],
    "dateTimeFieldSpecs": [{
      "name": "timestamp",
      "dataType": "TIMESTAMP",
      "format" : "1:MILLISECONDS:EPOCH",
      "granularity": "1:MILLISECONDS"
    }]
}
```

*config/schema.json*

The table config indicates that data will be ingested from the Kafka `events` topic:

```json  theme={null}
{
  "tableName": "events",
  "tableType": "REALTIME",
  "segmentsConfig": {
    "timeColumnName": "timestamp",
    "schemaName": "events",
    "replication": "1",
    "replicasPerPartition": "1"
  },
  "query" : {
    "disableGroovy": false
  },
  "tenants": {},
  "tableIndexConfig": {
    "loadMode": "MMAP",
    "streamConfigs": {
      "streamType": "kafka",
      "stream.kafka.topic.name": "events",
      "stream.kafka.broker.list": "kafka-groovy:9093",
      "stream.kafka.consumer.type": "lowlevel",
      "stream.kafka.consumer.prop.auto.offset.reset": "smallest",
      "stream.kafka.consumer.factory.class.name": "org.apache.pinot.plugin.stream.kafka20.KafkaConsumerFactory",
      "stream.kafka.decoder.class.name": "org.apache.pinot.plugin.stream.kafka.KafkaJSONMessageDecoder"
    }
  },
  "ingestionConfig": {
    "batchIngestionConfig": {
      "segmentIngestionType": "APPEND",
      "segmentIngestionFrequency": "DAILY"
    },
    "transformConfigs": [
      {
        "columnName": "id",
        "transformFunction": "Groovy({def jsonSlurper = new groovy.json.JsonSlurper(); def object = jsonSlurper.parseText(new groovy.json.JsonBuilder(payload).toPrettyString()); def result = object.after == null ? Long.valueOf(object.before.id) : Long.valueOf(object.after.id); return result}, payload)"
      },
      {
        "columnName": "name",
        "transformFunction": "Groovy({def jsonSlurper = new groovy.json.JsonSlurper(); def object = jsonSlurper.parseText(new groovy.json.JsonBuilder(payload).toPrettyString()); return object.firstName + ' ' + object.lastName}, payload)"
      }
    ]
  },
  "metadata": {}
}
```

*config/table.json*

Let's dive into the [transformation functions](https://docs.pinot.apache.org/developers/advanced/ingestion-level-transformations) defined under `ingestionConfig.transformConfigs`:

* The *id* one extracts `payload.after.id` if the `after` property exists, otherwise it uses `payload.before.id`
* The *name* one concatenates `payload.firstName` and `payload.lastName`

They both use Groovy's JSON parser to create an object from the payload, before using logic from the programming language to return the desired out.

<Info>
  If you only need to do simple data transformation, you can use the [built-in transformation functions](https://docs.pinot.apache.org/developers/advanced/ingestion-level-transformations#inbuilt-pinot-functions).
</Info>

We can add the table and schema by running the following command:

```bash  theme={null}
docker run \
   --network groovy \
   -v $PWD/config:/config \
   apachepinot/pinot:1.0.0 AddTable \
     -schemaFile /config/schema.json \
     -tableConfigFile /config/table.json \
     -controllerHost "pinot-controller-groovy" \
    -exec
```

## Ingest Data into Kafka

We can run the following command to import a couple of documents into Kafka:

```bash  theme={null}
printf '{"timestamp": "2019-10-09 21:25:25", "payload": {"firstName": "James", "lastName": "Smith", "before": {"id": 2}, "after": { "id": 3}}}
{"timestamp": "2019-10-10 21:33:25", "payload": {"firstName": "John", "lastName": "Gates", "before": {"id": 2}}}\n' |
kcat -P -b localhost:9092 -t events
```

Let's check those documents have been imported by running the following command:

```bash  theme={null}
kcat -C -b localhost:9092 -t events -c2
```

```json  theme={null}
{"timestamp": "2019-10-09 21:25:25", "payload": {"firstName": "James", "lastName": "Smith", "before": {"id": 2}, "after": { "id": 3}}}
{"timestamp": "2019-10-09 21:25:25", "payload": {"firstName": "James", "lastName": "Smith", "before": {"id": 2}}}
```

*Output*

Looks good so far.

## Querying

Once that's completed, navigate to [localhost:9000/#/query](http://localhost:9000/#/query) and click on the `events` table or copy/paste the following query:

```sql  theme={null}
select * 
from events 
limit 10
```

You will see the following output:

| id | name        | timestamp             |
| -- | ----------- | --------------------- |
| 3  | James Smith | 2019-10-09 21:25:25.0 |
| 2  | John Gates  | 2019-10-10 21:33:25.0 |

*Query Results*

Built with [Mintlify](https://mintlify.com).
