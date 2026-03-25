# Source: https://docs.startree.ai/recipes/json-transformation-functions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# JSON Transformation Functions

In this recipe we'll learn how to use JSON transformation functions to extract values from nested JSON documents during the data ingestion process.

| Pinot Version | 0.9.3                                                                                                                                                     |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Code          | [startreedata/pinot-recipes/json-transformation-functions](https://github.com/startreedata/pinot-recipes/tree/main/recipes/json-transformation-functions) |

## Prerequisites

To follow the code examples in this guide, you must [install Docker](https://docs.docker.com/get-docker/) locally and download recipes.

## Navigate to recipe

1. If you haven't already, download recipes.
2. In terminal, go to the recipe by running the following command:

```bash  theme={null}
cd pinot-recipes/recipes/json-transformation-functions
```

## Launch Pinot Cluster

You can spin up a Pinot Cluster by running the following command:

```bash  theme={null}
docker-compose up
```

This command will run a single instance of the Pinot Controller, Pinot Server, Pinot Broker, and Zookeeper. You can find the [docker-compose.yml](https://github.com/startreedata/pinot-recipes/blob/main/recipes/json-transformation-functions/docker-compose.yml) file on GitHub.

## Dataset

We're going to import the following JSON file:

<div class="text-output">
  ```json  theme={null}
  {"name":"Pete", "meta": {"age":24}, "subjectsAndGrades":[{"name":"Maths", "grade":"A"}, {"name":"English", "grade":"B"}]}
  {"name":"John", "meta": {"age":28}, "subjectsAndGrades":[{"name":"Maths", "grade":"A"}, {"name":"Computer Science", "grade":"C"}]}
  ```

  *data/import.json*
</div>

## Pinot Schema and Table

Now let's create a Pinot Schema and Table.

First, the schema:

```json  theme={null}
{
  "schemaName":"people",
  "dimensionFieldSpecs":[
    {
      "name":"name",
      "dataType":"STRING"
    },
    {
      "name":"age",
      "dataType":"INT"
    },
    {
      "dataType":"STRING",
      "name":"subjects",
      "singleValueField":false
    },
    {
      "dataType":"STRING",
      "name":"grades",
      "singleValueField":false
    }
  ]
}
```

*config/schema.json*

The `subjects` and `grades` columns will both contains arrays of values, which we can configure by setting `"singleValueField":false`.

We'll also have the following table config:

```json {9-22} theme={null}
{
  "tableName":"people",
  "tableType":"OFFLINE",
  "segmentsConfig":{
    "replication":1,
    "schemaName":"people"
  },
  "ingestionConfig":{
    "transformConfigs":[
      {
        "columnName":"subjects",
        "transformFunction":"jsonPathArray(subjectsAndGrades, '$.[*].name')"
      },
      {
        "columnName":"grades",
        "transformFunction":"jsonPathArray(subjectsAndGrades, '$.[*].grade')"
      },
      {
        "columnName":"age",
        "transformFunction":"JSONPATHLONG(meta, '$.age')"
      }
    ],
    "batchIngestionConfig":{
      "segmentIngestionType":"APPEND",
      "segmentIngestionFrequency":"DAILY"
    }
  },
  "tenants":{
    "broker":"DefaultTenant",
    "server":"DefaultTenant"
  },
  "tableIndexConfig":{
    "loadMode":"MMAP"
  },
  "metadata":{}
}
```

*config/table.json*

In this config we define transform configs (`ingestionConfig.transformConfigs`) to extract the subject names and grades from the `subjectAndGrades` property, using the [jsonPathArray](https://docs.pinot.apache.org/configuration-reference/functions/jsonpatharray) function. We also define one to extract the `age` from the `meta` property using the [JSONPATHLONG](https://docs.pinot.apache.org/configuration-reference/functions/jsonpathlong) function.

You can create the table and schema by running the following command:

```bash  theme={null}
docker run \
   --network json \
   -v $PWD/config:/config \
   apachepinot/pinot:1.0.0 AddTable \
     -schemaFile /config/schema.json \
     -tableConfigFile /config/table.json \
     -controllerHost "pinot-controller-json" \
    -exec
```

You should see a message similar to the following if everything is working correctly:

```text  theme={null}
2022/02/25 13:21:11.963 INFO [AddTableCommand] [main] Executing command: AddTable -tableConfigFile /config/table.json -schemaFile /config/schema.json -controllerProtocol http -controllerHost 172.30.0.3 -controllerPort 9000 -user null -password [hidden] -exec
2022/02/25 13:21:13.337 INFO [AddTableCommand] [main] {"status":"Table people_OFFLINE succesfully added"}
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
  tableName: 'people'
pinotClusterSpecs:
  - controllerURI: 'http://localhost:9000'
pushJobSpec:
  pushAttempts: 2
  pushRetryIntervalMillis: 1000
```

*config/table.json*

The import job will map fields in each JSON document to a corresponding column in the `people` schema. If one of the fields doesn't exist in the schema it will be skipped.

In this case the `name` field will be automatically mapped to the `name` column. The `subjectAndGrades` field is processed by transformation functions and the values are imported into the `subjects` and `grades` columns. The `meta` field is processed by a transformation function to extract the `age` property, which is stored in the `age` column.

You can run the following command to run the import:

```bash  theme={null}
docker run \
   --network json \
   -v $PWD/config:/config \
   -v $PWD/data:/data \
   apachepinot/pinot:1.0.0 LaunchDataIngestionJob \
    -jobSpecFile /config/job-spec.yml
```

## Querying

Once that's completed, navigate to [localhost:9000/#/query](http://localhost:9000/#/query) and click on the `people` table or copy/paste the following query:

```sql  theme={null}
select * 
from people 
limit 10
```

You will see the following output:

| age | grades | name | subjects               |
| --- | ------ | ---- | ---------------------- |
| 24  | A,B    | Pete | Maths,English          |
| 28  | A,C    | John | Maths,Computer Science |

*Query Results*

Built with [Mintlify](https://mintlify.com).
