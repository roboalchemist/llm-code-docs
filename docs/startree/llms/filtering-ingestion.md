# Source: https://docs.startree.ai/recipes/filtering-ingestion.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Filtering records during ingestion

To learn how to filter records when ingesting data into Pinot, watch the following video, or complete the tutorial below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-tK71ka6xMw" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

| Pinot Version | 1.0.0                                                                                                             |
| ------------- | ----------------------------------------------------------------------------------------------------------------- |
| Code          | [startreedata/pinot-recipes/filtering](https://github.com/startreedata/pinot-recipes/tree/main/recipes/filtering) |

## Prerequisites

To follow the code examples in this guide, you must [install Docker](https://docs.docker.com/get-docker/) locally and download recipes.

## Navigate to recipe

1. If you haven't already, download recipes.
2. In terminal, go to the recipe by running the following command:

```bash  theme={null}
cd pinot-recipes/recipes/filtering
```

## Launch Pinot Cluster

You can spin up a Pinot Cluster by running the following command:

```bash  theme={null}
docker-compose up
```

This command will run a single instance of the Pinot Controller, Pinot Server, Pinot Broker, and Zookeeper. You can find the [docker-compose.yml](https://github.com/startreedata/pinot-recipes/blob/main/recipes/filtering/docker-compose.yml) file on GitHub.

## Dataset

We're going to import the following JSON file:

```json  theme={null}
{"title": "Valentine's Day", "genre": "Comedy", "year": 2010, "id": 361248901147483647}
{"title": "The Ugly Truth", "genre": "Comedy", "year": 2009, "id": 332567813147483648}
{"title": "P.S. I Love You", "genre": "Romance", "year": 2007, "id": 346905752147483649}
{"title": "Dear John", "genre": "Drama", "year": 2010, "id": 300441473147483650}
{"title": "The Curious Case of Benjamin Button", "genre": "Fantasy", "year": 2008, "id": 394030854147483651}
```

*data/import.json*

## Pinot Schema and Table

Now let's create a Pinot Schema and Table.

First, the schema:

```json  theme={null}
{
    "schemaName": "movies",
    "dimensionFieldSpecs": [
      {
        "name": "id",
        "dataType": "LONG"
      },
      {
        "name": "title",
        "dataType": "STRING"
      },
      {
        "name": "genre",
        "dataType": "STRING"
      },
      {
        "name": "year",
        "dataType": "INT"
      }
    ]
}
```

*config/schema.json*

We'll also have the following table config:

```json {16-18} theme={null}
{
    "tableName": "movies",
    "tableType": "OFFLINE",
    "segmentsConfig": {
      "replication": 1,
      "schemaName": "movies"
    },
    "tenants": {
      "broker":"DefaultTenant",
      "server":"DefaultTenant"
    },
    "tableIndexConfig": {
      "loadMode": "MMAP"
    },
    "ingestionConfig": {
      "filterConfig": {
        "filterFunction": "year >= 2010"
      },
      "batchIngestionConfig": {
        "segmentIngestionType": "APPEND",
        "segmentIngestionFrequency": "DAILY"
      }
    },
    "metadata": {}
}
```

*config/table.json*

Our filtering function ensures that any records with a `year` property with a value of 2010 or more are **not imported**.

You can create the table and schema by running the following command:\`

```bash  theme={null}
docker run \
   --network filtering\
   -v $PWD/config:/config \
   apachepinot/pinot:1.0.0 AddTable \
     -schemaFile /config/schema.json \
     -tableConfigFile /config/table.json \
     -controllerHost "pinot-controller-filtering" \
    -exec
```

You should see a message similar to the following if everything is working correctly:

```text  theme={null}
2022/02/25 09:39:00.839 INFO [AddTableCommand] [main] Executing command: AddTable -tableConfigFile /config/table.json -schemaFile /config/schema.json -controllerProtocol http -controllerHost 172.29.0.3 -controllerPort 9000 -user null -password [hidden] -exec
2022/02/25 09:39:01.308 INFO [AddTableCommand] [main] {"status":"Table movies_OFFLINE succesfully added"}
```

## Ingestion Job

Now we’re going to import the JSON file into Pinot. We'll do this with the following ingestion spec:

```yaml  theme={null}
executionFrameworkSpec:
  name: 'standalone'
  segmentGenerationJobRunnerClassName: 'org.apache.pinot.plugin.ingestion.batch.standalone.SegmentGenerationJobRunner'
  segmentTarPushJobRunnerClassName: 'org.apache.pinot.plugin.ingestion.batch.standalone.SegmentTarPushJobRunner'
jobType: SegmentCreationAndTarPush
inputDirURI: '/data'
includeFileNamePattern: 'glob:**/import.json'
outputDirURI: '/opt/pinot/data/movies/'
overwriteOutput: true
pinotFSSpecs:
  - scheme: file
    className: org.apache.pinot.spi.filesystem.LocalPinotFS
recordReaderSpec:
  dataFormat: 'json'
  className: 'org.apache.pinot.plugin.inputformat.json.JSONRecordReader'
tableSpec:
  tableName: 'movies'
pinotClusterSpecs:
  - controllerURI: 'http://pinot-controller-filtering:9000'
pushJobSpec:
  pushAttempts: 2
  pushRetryIntervalMillis: 1000
```

The import job will map fields in each JSON document to a corresponding column in the `movies` schema. If one of the fields doesn't exist in the schema it will be skipped.

<Info>
  You can also apply transformation functions to JSON documents during the ingestion process.
  For more details, see the [JSON Transformation Functions](/recipes/json-transformation-functions) guide.
</Info>

You can run the following command to run the import:

```bash  theme={null}
docker run \
   --network filtering \
   -v $PWD/config:/config \
   -v $PWD/data:/data \
   apachepinot/pinot:1.0.0 LaunchDataIngestionJob \
     -jobSpecFile /config/job-spec.yml
```

## Querying

Once that's completed, navigate to [localhost:9000/#/query](http://localhost:9000/#/query) and click on the `movies` table or copy/paste the following query:

```sql  theme={null}
select * 
from movies 
limit 10
```

You will see the following output:

| genre   | id                 | title                               | year |
| ------- | ------------------ | ----------------------------------- | ---- |
| Comedy  | 332567813147483648 | The Ugly Truth                      | 2009 |
| Romance | 346905752147483649 | P.S. I Love You                     | 2007 |
| Fantasy | 394030854147483651 | The Curious Case of Benjamin Button | 2008 |

*Query Results*

Built with [Mintlify](https://mintlify.com).
