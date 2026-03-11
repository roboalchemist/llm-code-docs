# Source: https://docs.startree.ai/recipes/configuring-segment-threshold.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> In this guide we'll learn how to configure the segment threshold for flushing data in Apache Pinot real-time tables.

# Configuring the Segment Threshold

To learn how to configure the segment threshold for real-time tables, watch the following video, or complete the tutorial below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/qBMv3CcKVsI" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

| Pinot Version | 1.0.0                                                                                                                                                     |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Code          | [startreedata/pinot-recipes/configuring-segment-threshold](https://github.com/startreedata/pinot-recipes/tree/main/recipes/configuring-segment-threshold) |

<Info>
  To learn what the segment threshold is and why it's important, see [Segment Threshold](https://dev.startree.ai/docs/pinot/concepts/segment-threshold).
</Info>

## Configuration parameters

The segment threshold is configured using the following parameters:

| Property                                        | Description                                                     |
| ----------------------------------------------- | --------------------------------------------------------------- |
| `realtime.segment.flush.threshold.rows`         | Row count flush threshold.                                      |
| `realtime.segment.flush.threshold.time`         | Time threshold that will keep a segment open for it is flushed. |
| `realtime.segment.flush.threshold.segment.size` | The desired size of a completed segment.                        |

There are two main approaches for configuring these parameters:

### Desired row threshold

We can define a manual row threshold by specifying a value for `realtime.segment.flush.threshold.rows`.

Pinot will complete/flush segments as soon as the consuming segment contains the specified number of rows.
This will generally result in each segment having the same number of rows.

However, if the time threshold defined by `realtime.segment.flush.threshold.time` is reached, a segment will be completed even if the row count flush threshold has not yet been reached.

<Info>
  If *realtime.segment.flush.threshold.rows* is set to a value greater than 0, *realtime.segment.flush.threshold.segment.size* is ignored.
</Info>

### Desired segment size

Alternatively we can set `realtime.segment.flush.threshold.rows` to `0`, in which case Pinot will instead attempt to make sure that every segment has the desired size defined by
`realtime.segment.flush.threshold.segment.size`.

When configuring the segment threshold this way, the minimum number of rows in a segment is 10,000.

The first segment for a new partition will have 100,000 rows. For subsequent segments Pinot will slowly adjust the number of rows to get closer to the desired segment size. This means that the first few segments might differ in size, but over time the segment size will approach the desired size.

<Info>
  The algorithm used in this approach is described in more detail in the [Auto-tuning Pinot real-time consumption](https://engineering.linkedin.com/blog/2019/auto-tuning-pinot) blog post.
</Info>

## A worked example

Let's see how this works with a worked example.

### Prerequisites

To follow the code examples in this guide, you must [install Docker](https://docs.docker.com/get-docker/) locally and download recipes.

### Navigate to recipe

1. If you haven't already, download recipes.
2. In terminal, go to the recipe by running the following command:

```bash  theme={null}
cd pinot-recipes/recipes/configuring-segment-threshold
```

### Launch Pinot Cluster

You can spin up a Pinot Cluster by running the following command:

```bash  theme={null}
docker-compose up
```

This command will run a single instance of the Pinot Controller, Pinot Server, Pinot Broker, and Zookeeper. You can find the [docker-compose.yml](https://github.com/startreedata/pinot-recipes/blob/main/recipes/configuring-segment-threshold/docker-compose.yml) file on GitHub.

### Pinot Schema and Table

Let's create a Pinot Schema and Table.

The schema is defined below:

```json  theme={null}
{
  "schemaName":"events",
  "dimensionFieldSpecs":[
    {
      "name":"uuid",
      "dataType":"STRING"
    }
  ],
  "metricFieldSpecs":[
    {
      "name":"count",
      "dataType":"INT"
    }
  ],
  "dateTimeFieldSpecs":[
    {
      "name":"ts",
      "dataType":"TIMESTAMP",
      "format":"1:MILLISECONDS:EPOCH",
      "granularity":"1:MILLISECONDS"
    }
  ]
}
```

*config/schema.json*

And the table config below:

```json {20-22} theme={null}
{
  "tableName":"events",
  "tableType":"REALTIME",
  "segmentsConfig":{
    "timeColumnName":"ts",
    "schemaName":"events",
    "replication":"1",
    "replicasPerPartition":"1"
  },
  "tableIndexConfig":{
    "loadMode":"MMAP",
    "streamConfigs":{
      "streamType":"kafka",
      "stream.kafka.topic.name":"events",
      "stream.kafka.broker.list":"kafka-segment:9093",
      "stream.kafka.consumer.type":"lowlevel",
      "stream.kafka.consumer.prop.auto.offset.reset":"smallest",
      "stream.kafka.consumer.factory.class.name":"org.apache.pinot.plugin.stream.kafka20.KafkaConsumerFactory",
      "stream.kafka.decoder.class.name":"org.apache.pinot.plugin.stream.kafka.KafkaJSONMessageDecoder",
      "realtime.segment.flush.threshold.rows":"0",
      "realtime.segment.flush.threshold.time":"1h",
      "realtime.segment.flush.threshold.segment.size":"5M"
    }
  },
  "ingestionConfig":{
    "batchIngestionConfig":{
      "segmentIngestionType":"APPEND",
      "segmentIngestionFrequency":"DAILY"
    }
  },
  "tenants":{
    
  },
  "metadata":{
    
  }
}
```

*config/table.json*

Pinot will try to ensure that the size of our segments is 5MB. It will complete a segment after 1 hour if it hasn't already been flushed.

Create the table and schema by running the following command:

```bash  theme={null}
docker run \
   --network segment \
   -v $PWD/config:/config \
   apachepinot/pinot:1.0.0 AddTable \
     -schemaFile /config/schema.json \
     -tableConfigFile /config/table.json \
     -controllerHost "pinot-controller-segment" \
    -exec
```

### Ingesting Data

Next, we're going to ingest some data into Kafka:

```bash  theme={null}
python datagen.py | 
kcat -P -b localhost:9092 -t events
```

### Inspecting segment sizes

After the ingestion script has run for a while we can inspect the size of the segments that have been completed.

You can return the size of each completed segment by running the following command:

```bash  theme={null}
curl -X GET "http://localhost:9000/tables/events/size?detailed=true" \
  -H "accept: application/json" 2>/dev/null | 
  jq -r '.realtimeSegments .segments | .[] | .serverInfo | .[]' | 
  jq -sc 'sort_by(.segmentName) | .[]'
```

**Output**

```json  theme={null}
{"segmentName":"events__0__0__20220301T1457Z","diskSizeInBytes":5144515}
{"segmentName":"events__0__1__20220301T1504Z","diskSizeInBytes":5242744}
{"segmentName":"events__0__2__20220301T1511Z","diskSizeInBytes":5242744}
{"segmentName":"events__0__3__20220301T1518Z","diskSizeInBytes":5242744}
{"segmentName":"events__0__4__20220301T1525Z","diskSizeInBytes":5242744}
{"segmentName":"events__0__5__20220301T1532Z","diskSizeInBytes":5242744}
{"segmentName":"events__0__6__20220301T1539Z","diskSizeInBytes":5242797}
{"segmentName":"events__0__7__20220301T1546Z","diskSizeInBytes":5242797}
```

We can see that all the segments have a size of just over 5 million bytes, which is close to 5 MB. The first segment had a size of 4.9 MB, but after that the size increased to 4.9998 MB until the last two segments where it's increased to 4.9999 MB. Presumably adding an extra row would then take us further away from 5 MB.

Now let's see how many rows are contained in each segment. You can do that for one of the segments by running the following command:

```bash  theme={null}
curl -X GET "http://localhost:9000/segments/events/events__0__1__20220301T1504Z/metadata" \
  -H "accept: application/json" 2>/dev/null
```

**Output**

```json  theme={null}
{
  "segment.crc": "1090576205",
  "segment.creation.time": "1646147045318",
  "segment.end.time": "1646147463422",
  "segment.flush.threshold.size": "101912",
  "segment.index.version": "v3",
  "segment.name": "events__0__1__20220301T1504Z",
  "segment.realtime.download.url": "http://192.168.0.3:9000/segments/events/events__0__1__20220301T1504Z",
  "segment.realtime.endOffset": "201912",
  "segment.realtime.numReplicas": "1",
  "segment.realtime.startOffset": "100000",
  "segment.realtime.status": "DONE",
  "segment.start.time": "1646147042226",
  "segment.table.name": "events",
  "segment.time.unit": "MILLISECONDS",
  "segment.total.docs": "101912",
  "segment.type": "REALTIME"
}
```

The `segment.flush.threshold.size` property indicates that this segment contains 101,912 rows.

We can check how many rows are stored in all segments by running the following script:

```bash  theme={null}
segments=$(
  curl "http://localhost:9000/tables/events/size?detailed=true" 2>/dev/null | 
  jq -r '.realtimeSegments .segments | .[] | .serverInfo | .[]' | 
  jq -sc 'sort_by(.segmentName)'
)

for segment in $(echo $segments | jq -c '.[]'); do
  segmentName=$(echo $segment | jq -r '.segmentName')
  rows=$(
    curl "http://localhost:9000/segments/events/${segmentName}/metadata" 2>/dev/null |
    jq '."segment.flush.threshold.size" | tonumber'
  )
  echo $segment | jq -c --arg rows $rows '. + {"rows": $rows}'
done
```

**Output**

```json  theme={null}
{"segmentName":"events__0__0__20220301T1457Z","diskSizeInBytes":5144515,"rows":"100000"}
{"segmentName":"events__0__1__20220301T1504Z","diskSizeInBytes":5242744,"rows":"101912"}
{"segmentName":"events__0__2__20220301T1511Z","diskSizeInBytes":5242744,"rows":"101912"}
{"segmentName":"events__0__3__20220301T1518Z","diskSizeInBytes":5242744,"rows":"101912"}
{"segmentName":"events__0__4__20220301T1525Z","diskSizeInBytes":5242744,"rows":"101912"}
{"segmentName":"events__0__5__20220301T1532Z","diskSizeInBytes":5242744,"rows":"101912"}
{"segmentName":"events__0__6__20220301T1539Z","diskSizeInBytes":5242797,"rows":"101913"}
{"segmentName":"events__0__7__20220301T1546Z","diskSizeInBytes":5242797,"rows":"101913"}
```

It looks like Pinot has settled in on a size of 101,913 rows per segment. The number of rows would be reduced if we imported much bigger strings into the `uuid` column, but for now it looks fairly stable.

Built with [Mintlify](https://mintlify.com).
