# Source: https://docs.startree.ai/recipes/managed-offline-flow.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Managed Offline Flow

Pinot is most commonly used to provide real-time analytics based on streaming data, which can be achieved using a real-time table. However, after running these systems for a while, we'll want to update the data ingested into this table. Perhaps the name of a value in a column has been updated, or we want to remove some duplicate records.

Segments in real-time tables can't be replaced, but we can replace those in offline tables. Managed offline flow is the way that Pinot handles the process of moving the data from real-time to offline tables.

In this recipe we'll learn how to use Pinot offline managed flow.

| Pinot Version | 0.9.3                                                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Code          | [startreedata/pinot-recipes/managed-offline-flow](https://github.com/startreedata/pinot-recipes/tree/main/recipes/managed-offline-flow) |

## Prerequisites

To follow the code examples in this guide, you must [install Docker](https://docs.docker.com/get-docker/) locally and download recipes.

Clone this repository and navigate to this recipe:

```bash  theme={null}
git clone git@github.com:startreedata/pinot-recipes.git
cd pinot-recipes/recipes/ingest-json-files
```

## Makefile

```bash  theme={null}
make recipe
```

Running this recipe will build the foundation and start producing data into Kafka.

Run the next Make task:

## Managed Offline Flow

```bash  theme={null}
make manage_offline_flow
```

The Make command above will perform these tasks:

* Sets the necessary properties in the Pinot Controller to enable the managed offline flow task: `RealtimeToOfflineSegmentsTask`.`timeoutMs` and `.numConcurrentTasksPerInstance`.
* Schedules the task to run.
* Prints logs related to the task.
* Updates the hybrid table's time boundary so that you can see records that have been move to offline.

## View realtime and offline segments

Navigate to [http://localhost:9000/#/query](http://localhost:9000/#/query) and run the following query:

```sql  theme={null}
select $segmentName, count(*) cnt
from events
group by $segmentName
order by cnt desc
```

Run the statement above to see records migrate from REALTIME to OFFLINE by running `make realtime` to generate more data and `make manage_offline_flow` to migrate older data to OFFLINE. See the [README on GitHub for this recipe](https://github.com/startreedata/pinot-recipes/blob/main/recipes/managed-offline-flow/README.md) for sample output.

## Clean up

```bash  theme={null}
make clean
```

## Troubleshooting

To clean up old Docker installations that may be interfering with your testing of this recipe, run the following command:

```bash  theme={null}
docker system prune
```

Built with [Mintlify](https://mintlify.com).
