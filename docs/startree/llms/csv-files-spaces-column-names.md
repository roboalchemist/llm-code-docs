# Source: https://docs.startree.ai/recipes/csv-files-spaces-column-names.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Importing CSV files with columns containing spaces

Pinot can transform data at ingestion. In this recipe, we'll learn how to use a transformation to change the name of a column. We will ingest a CSV file with a column containing spaces in its name. We will then use a transformation function to remove the space while the data is being ingested into Pinot.

| Pinot Version | 1.0.0                                                                                                                                                     |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Code          | [startreedata/pinot-recipes/csv-files-spaces-column-names](https://github.com/startreedata/pinot-recipes/tree/main/recipes/csv-files-spaces-column-names) |

## Prerequisites

To follow the code examples in this guide, you must [install Docker](https://docs.docker.com/get-docker/) locally and download recipes.

## Navigate to recipe

1. If you haven't already, download recipes.
2. In the terminal, navigate to this recipe's directory:

```bash  theme={null}
cd pinot-recipes/recipes/csv-files-spaces-column-names
```

## Launch Pinot Cluster

Launch a Pinot Cluster:

```bash  theme={null}
docker-compose up
```

This command will run a single instance of the Pinot Controller, Pinot Server, Pinot Broker, and Zookeeper.

You can find and examine the [docker-compose.yml](https://github.com/startreedata/pinot-recipes/blob/main/recipes/csv-files-spaces-column-names/docker-compose.yml) file on GitHub.

## Dataset

We're going to import the following CSV file, in which the `Case Number` column heading contains a space:

| ID       | Case Number |
| -------- | ----------- |
| 10224738 | HY411648    |
| 10224739 | HY411615    |
| 11646166 | JC213529    |
| 10224740 | HY411595    |

*data/import.csv*

## Pinot Schema and Table

Next we create a Pinot Schema and Table.

A common pattern when creating a schema is to create columns that map directly to the names of the fields in our data source. We can't do that in this case since column names can't contain spaces, so instead we'll use the following:

```json  theme={null}
{
    "schemaName": "crimes",
    "dimensionFieldSpecs": [
      {
        "name": "ID",
        "dataType": "INT"
      },
      {
        "name": "CaseNumber",
        "dataType": "STRING"
      }
    ]
}
```

*config/schema.json*

We'll also have the following table config:

```json  theme={null}
{
    "tableName": "crimes",
    "tableType": "OFFLINE",
    "segmentsConfig": {
      "replication": 1
    },
    "tenants": {
      "broker":"DefaultTenant",
      "server":"DefaultTenant"
    },
    "tableIndexConfig": {
      "loadMode": "MMAP"
    },
    "ingestionConfig": {
      "batchIngestionConfig": {
        "segmentIngestionType": "APPEND",
        "segmentIngestionFrequency": "DAILY"
      },
      "transformConfigs": [
        {"columnName": "CaseNumber", "transformFunction": "\"Case Number\"" }
      ]
    },
    "metadata": {}
}
```

*config/table.json*

<Info>
  The entry under `ingestionConfig.transformConfigs` makes sure that data in the `Case Number` field in the data source is ingested into the `CaseNumber` column of the table. To learn more about writing these functions, see the [ingestion transformation](https://docs.pinot.apache.org/developers/advanced/ingestion-level-transformations) documentation.
</Info>

Create the table and schema by running the following command:

```bash  theme={null}
docker run \
   --network csv \
   -v $PWD/config:/config \
   apachepinot/pinot:1.0.0 AddTable \
     -schemaFile /config/schema.json \
     -tableConfigFile /config/table.json \
     -controllerHost "pinot-controller-csv" \
    -exec
```

You should see a message similar to the following if everything is working correctly:

```text  theme={null}
2021/11/25 12:02:04.606 INFO [AddTableCommand] [main] Executing command: AddTable -tableConfigFile /config/table.json -schemaFile /config/schema.json -controllerProtocol http -controllerHost 192.168.144.3 -controllerPort 9000 -user null -password [hidden] -exec
2021/11/25 12:02:05.084 INFO [AddTableCommand] [main] {"status":"Table crimes_OFFLINE succesfully added"}
```

## Ingestion Job

Next, we import the CSV file into Pinot.
We'll do this with the following ingestion spec:

```yaml  theme={null}
executionFrameworkSpec:
  name: 'standalone'
  segmentGenerationJobRunnerClassName: 'org.apache.pinot.plugin.ingestion.batch.standalone.SegmentGenerationJobRunner'
  segmentTarPushJobRunnerClassName: 'org.apache.pinot.plugin.ingestion.batch.standalone.SegmentTarPushJobRunner'
  segmentUriPushJobRunnerClassName: 'org.apache.pinot.plugin.ingestion.batch.standalone.SegmentUriPushJobRunner'
jobType: SegmentCreationAndTarPush
inputDirURI: '/data'
includeFileNamePattern: 'glob:**/import.csv'
outputDirURI: '/opt/pinot/data/crimes/'
overwriteOutput: true
pinotFSSpecs:
  - scheme: file
    className: org.apache.pinot.spi.filesystem.LocalPinotFS
recordReaderSpec:
  dataFormat: 'csv'
  className: 'org.apache.pinot.plugin.inputformat.csv.CSVRecordReader'
  configClassName: 'org.apache.pinot.plugin.inputformat.csv.CSVRecordReaderConfig'
tableSpec:
  tableName: 'crimes'
pinotClusterSpecs:
  - controllerURI: 'http://pinot-controller-csv:9000'
pushJobSpec:
  pushAttempts: 2
  pushRetryIntervalMillis: 1000
```

*config/job-spec.yml*

Run the following command to run the import:

```bash  theme={null}
docker run \
   --network csv \
   -v $PWD/config:/config \
   -v $PWD/data:/data \
   apachepinot/pinot:1.0.0 LaunchDataIngestionJob \
  -jobSpecFile /config/job-spec.yml
```

## Querying

Once that's completed, navigate to [localhost:9000/#/query](http://localhost:9000/#/query) and click on the `crimes` table or copy/paste the following query:

```sql  theme={null}
select * 
from crimes 
limit 10
```

You will see the following output:

| CaseNumber | ID       |   |
| ---------- | -------- | - |
| HY411648   | 10224738 |   |
| HY411615   | 10224739 |   |
| JC213529   | 11646166 |   |
| HY411595   | 10224740 |   |

*Query Results*

Built with [Mintlify](https://mintlify.com).
