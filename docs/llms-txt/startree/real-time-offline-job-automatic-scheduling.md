# Source: https://docs.startree.ai/recipes/real-time-offline-job-automatic-scheduling.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Automatically schedule real-time to offline job

In this recipe we'll learn how to automatically schedule Apache Pinot's Real-Time to Offline job. This job is used to transition data from real-time to offline tables. For background reading on the use case for doing this, see [Managed Offline Flow](/recipes/managed-offline-flow).

| Pinot Version | 0.9.3                                                                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Code          | [startreedata/pinot-recipes/managed-offline-flow-automatic-scheduling](https://github.com/startreedata/pinot-recipes/tree/main/recipes/managed-offline-flow-automatic-scheduling) |

## Prerequisites

To follow the code examples in this guide, you must [install Docker](https://docs.docker.com/get-docker/) locally and download recipes.

## Navigate to recipe

1. If you haven't already, download recipes.
2. In terminal, go to the recipe by running the following command:

```bash  theme={null}
cd pinot-recipes/recipes/managed-offline-flow-automatic-scheduling
```

## Launch Pinot Cluster

You can spin up a Pinot Cluster by running the following command:

```bash  theme={null}
docker-compose up
```

This command will run a single instance of the Pinot Controller, Pinot Server, Pinot Broker, Pinot Minion, Kafka, and Zookeeper. You can find the [docker-compose.yml](https://github.com/startreedata/pinot-recipes/blob/main/recipes/managed-offline-flow-automatic-scheduling/docker-compose.yml) file on GitHub.

## Controller configuration

We need to provide configuration parameters to the Pinot Controller to have the Real-Time to Offline job (RT2OFF) run automatically. This is done in the following section of the Docker Compose file:

```yml  theme={null}
pinot-controller:
  image: apachepinot/pinot:0.9.3
  command: "StartController -zkAddress zookeeper-rt:2181 -config /config/controller-conf.conf"
```

The configuration is specified in `/config/controller-conf.conf`, the contents of which are shown below:

```conf {8-10} theme={null}
controller.access.protocols.http.port=9000
controller.zk.str=zookeeper-rt:2181
controller.helix.cluster.name=PinotCluster
controller.host=pinot-controller-rt
controller.port=9000
controller.data.dir=/data


controller.task.scheduler.enabled=true
controller.task.frequencyPeriod=5m
```

*/config/controller-conf.conf*

We're particularly interested in the last two lines:

* `controller.task.scheduler.enabled=true` enables the automatic running of the RT2OFF job
* `controller.task.frequencyPeriod=5m` configures it to run every 5 minutes

## Pinot Schema and Tables

Now let's create a Pinot Schema, as well as real-time and offline tables. Pinot is going to take care of populating data into the offline table, but it still expects us to configure the table.

### Schema

Our schema is going to capture some simple events, and looks like this:

```json  theme={null}
{
  "schemaName": "events",
  "dimensionFieldSpecs": [
    {
      "name": "uuid",
      "dataType": "STRING"
    }
  ],
  "metricFieldSpecs": [
    {
      "name": "count",
      "dataType": "INT"
    }
  ],
  "dateTimeFieldSpecs": [{
    "name": "ts",
    "dataType": "TIMESTAMP",
    "format" : "1:MILLISECONDS:EPOCH",
    "granularity": "1:MILLISECONDS"
  }]
}
```

*config/schema.json*

You can create the schema by running the following command:

```bash  theme={null}
docker exec -it pinot-controller-rt bin/pinot-admin.sh AddSchema   \
  -schemaFile /config/schema.json \
  -exec
```

### Offline Table

The offline table config is defined below:

```json  theme={null}
{
  "tableName": "events",
  "tableType": "OFFLINE",
  "segmentsConfig": {
    "timeColumnName": "ts",
    "schemaName": "events",
    "replication": "1",
    "replicasPerPartition": "1"
  },
  "ingestionConfig": {
    "batchIngestionConfig": {
      "segmentIngestionType": "APPEND",
      "segmentIngestionFrequency": "HOURLY"
    }
  },
  "tableIndexConfig": {
    "loadMode": "MMAP"
  },
  "tenants": {},
  "metadata": {}
}
```

*config/table-offline.json*

You can create the table by running the following command:

```bash  theme={null}
docker exec -it pinot-controller-rt bin/pinot-admin.sh AddTable   \
  -tableConfigFile /config/table-offline.json   \
  -exec
```

### Real-Time Table

And the real-time table is defined below:

```json  theme={null}
{
  "tableName": "events",
  "tableType": "REALTIME",
  "segmentsConfig": {
    "timeColumnName": "ts",
    "schemaName": "events",
    "replication": "1",
    "replicasPerPartition": "1",
    "retentionTimeUnit": "DAYS",
    "retentionTimeValue": "1"
  },
  "task": {
    "taskTypeConfigsMap": {
      "RealtimeToOfflineSegmentsTask": {
        "bufferTimePeriod": "1m",
        "bucketTimePeriod": "5m",        
        "roundBucketTimePeriod": "1m",
        "schedule": "0 * * * * ?",
        "mergeType": "rollup",
        "count.aggregationType": "max",
        "maxNumRecordsPerSegment": "100000"
      }
    }
  },
  "tableIndexConfig": {
    "loadMode": "MMAP",
    "streamConfigs": {
    "streamType": "kafka",
    "stream.kafka.topic.name": "events",
    "stream.kafka.broker.list": "kafka-rt:9093",
    "stream.kafka.consumer.type": "lowlevel",
    "stream.kafka.consumer.prop.auto.offset.reset": "smallest",
    "stream.kafka.consumer.factory.class.name": "org.apache.pinot.plugin.stream.kafka20.KafkaConsumerFactory",
    "stream.kafka.decoder.class.name": "org.apache.pinot.plugin.stream.kafka.KafkaJSONMessageDecoder",
    "realtime.segment.flush.threshold.rows": "10000",
    "realtime.segment.flush.threshold.time": "1h",
    "realtime.segment.flush.threshold.segment.size": "5M"
    }
  },
  "tenants": {},
  "metadata": {}
}
```

*config/table-realtime.json*

<Warning>
  The `realtime.segment.flush.threshold.rows` config is intentionally set to an extremely small value so that the segment will be committed after 10,000 records have been ingested.
  In a production system this value should be set much higher, as described in the [configuring segment threshold](/recipes/configuring-segment-threshold) guide.
</Warning>

The main thing that we're interested in is the `RealtimeToOfflineSegmentsTask`, which is extracted below:

```json  theme={null}
"task": {
  "taskTypeConfigsMap": {
    "RealtimeToOfflineSegmentsTask": {
      "bufferTimePeriod": "1m",
      "bucketTimePeriod": "5m",  
      "schedule": "0 * * * * ?"
    }
  }
}
```

This configuration enables the job and defines what should happen when it runs.

The `schedule` parameter indicates when this task will be run.
The value is a [Quartz Cron expression](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html) and in this case we have the job running once a minute.

<Warning>
  The values for `bufferTimePeriod` and `bucketTimePeriod`, and `schedule` are intentionally set to very low values so that it's easier to see how they work.

  In a production setup, `bufferTimePeriod` and `bucketTimePeriod` would usually be set to a time of 1 day or more, and `schedule` could be set to run once a day.
</Warning>

<Info>
  For a breakdown of all the parameters that can be defined for the `RealtimeToOfflineSegmentsTask`, see the [Manually scheduling real-time to offline job](/recipes/real-time-offline-job) guide.
</Info>

You can create the table by running the following command:

```bash  theme={null}
docker exec -it pinot-controller-rt bin/pinot-admin.sh AddTable   \
  -tableConfigFile /config/table-realtime.json   \
  -exec
```

## Ingesting Data

Let's ingest data into the `events` Kafka topic, by running the following:

```bash  theme={null}
while true; do
  ts=`date +%s%N | cut -b1-13`;
  uuid=`cat /proc/sys/kernel/random/uuid | sed 's/[-]//g'`
  count=$[ $RANDOM % 1000 + 0 ]
  echo "{\"ts\": \"${ts}\", \"uuid\": \"${uuid}\", \"count\": $count}"
done |
docker exec -i kafka-rt /opt/kafka/bin/kafka-console-producer.sh \
  --bootstrap-server localhost:9092 \
  --topic events
```

Data will make its way into the real-time table.
We can see how many records have been ingested by running the following query:

```sql  theme={null}
SELECT count(*)
FROM events
```

## Checking that the job is running

We can check that the job is running by querying the logs on the Pinot Controller, as shown below:

```bash  theme={null}
docker exec -it pinot-controller-rt grep -ri --color "\[RealtimeToOff" logs/pinot-all.log
```

We should see the following output:

<div class="text-output">
  ```text  theme={null}
  2022/03/08 13:21:00.009 INFO [RealtimeToOfflineSegmentsTaskGenerator] [DefaultQuartzScheduler_Worker-8] Start generating task configs for table: events_REALTIME for task: RealtimeToOfflineSegmentsTask
  2022/03/08 13:21:00.099 INFO [RealtimeToOfflineSegmentsTaskGenerator] [DefaultQuartzScheduler_Worker-8] Finished generating task configs for table: events_REALTIME for task: RealtimeToOfflineSegmentsTask
  ```
</div>

When the job can't create any new segments for the offline table it will instead output the following:

<div class="text-output">
  ```text  theme={null}
  2022/03/08 13:24:00.008 INFO [RealtimeToOfflineSegmentsTaskGenerator] [DefaultQuartzScheduler_Worker-1] Start generating task configs for table: events_REALTIME for task: RealtimeToOfflineSegmentsTask
  2022/03/08 13:24:00.076 INFO [RealtimeToOfflineSegmentsTaskGenerator] [DefaultQuartzScheduler_Worker-1] Window with start: 1646745600000 and end: 1646745900000 is not older than buffer time: 60000 configured as 1m ago. Skipping task generation: RealtimeToOfflineSegmentsTask
  ```
</div>

or

<div class="text-output">
  ```text  theme={null}
  2022/03/08 13:30:00.201 INFO [RealtimeToOfflineSegmentsTaskGenerator] [DefaultQuartzScheduler_Worker-1] Start generating task configs for table: events_REALTIME for task: RealtimeToOfflineSegmentsTask
  2022/03/08 13:30:00.212 INFO [RealtimeToOfflineSegmentsTaskGenerator] [DefaultQuartzScheduler_Worker-1] No realtime-completed segments found for table: events_REALTIME, skipping task generation: RealtimeToOfflineSegmentsTask
  ```
</div>

If you see these messages often, it might make sense to reduce the frequency of the RT2OFF job.

Built with [Mintlify](https://mintlify.com).
