# Source: https://docs.startree.ai/recipes/time-boundary-hybrid-table.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Get the Time Boundary for a Hybrid Table

Hybrid tables consist of real-time and offline tables with the same name. When querying these tables, the Pinot broker uses the time boundary to determine which records to read from the offline table and which to read from the real-time table.

To learn how to get the time boundary for a hybrid table, watch the following video, or complete the tutorial below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/lB3RaKJ0Hbs" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

| Pinot Version | 1.0.0                                                                                                                                               |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Code          | [startreedata/pinot-recipes/time-boundary-hybrid-table](https://github.com/startreedata/pinot-recipes/tree/main/recipes/time-boundary-hybrid-table) |

<Info>
  For more information on time boundaries, see [Concepts: Time Boundary](https://dev.startree.ai/docs/pinot/concepts/time-boundary)
</Info>

## Prerequisites

To follow the code examples in this guide, you must [install Docker](https://docs.docker.com/get-docker/) locally and download recipes.

## Navigate to recipe

1. If you haven't already, download recipes.
2. In terminal, go to the recipe by running the following command:

```bash  theme={null}
cd pinot-recipes/recipes/time-boundary-hybrid-table
```

## Makefile

The Makefile contains all of the commands need to start up Pinot and Kafka. Run the make command below.

`make recipe`

This command will also:

* Create a Kafka topic called `events`.
* Create a hybrid Pinot `events` table.
* Batch load data into the offline `events` table in Pinot.
* Generate stream data using the Pinot schema to Kafka and ultimately into the realtime `events` table in Pinot.

When you go to the [table list](http://localhost:9000/#/tables) in Pinot, you will see an `events_REALTIME` and an `events_OFFLINE` table. When you go to the [query console](http://localhost:9000/#/query) in Pinot, you will only see one table: `events`.

## Select Pinot Segments

The stream data generator will generate 1000 records into the `events_REALTIME` table. The batch loader will load 10 records into the `events_OFFLINE` table for a total of `1010` records.

If you count the number of records in this table, you will only get `1000`.

```sql  theme={null}
select count(*) from events
```

If you look at the `query response stats` you'll see `1000` documents scanned from `1010` totalDocs. When querying hybrid tables, the Pinot Broker must decide which records to read from the offline table and which to read from the real-time table.

If you run the SQL below, you'll see that there are no OFFLINE segments. They are only realtime segments.

```sql  theme={null}
select $segmentName, count(*) from events
group by $segmentName
```

Check the current time boundary:

```bash  theme={null}
curl "http://localhost:8099/debug/timeBoundary/events" -H "accept: application/json" 2>/dev/null | jq '.'
```

Execute the API call below to force Pinot to update the `event` table's time boundary.

```sql  theme={null}
curl -X POST \
  "http://localhost:9000/tables/events/timeBoundary" \
  -H "accept: application/json" | \
  jq
```

Run the query again below. This time, you should see both offline and realtime segments.

```sql  theme={null}
select $segmentName, count(*) from events
group by $segmentName
```

Built with [Mintlify](https://mintlify.com).
