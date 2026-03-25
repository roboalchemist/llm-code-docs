# Source: https://docs.startree.ai/recipes/import-data-files-different-directories.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Import data files from different directories

In this recipe we'll learn how to import CSV files from different directories.

| Pinot Version | 0.9.3                                                                                                                                                       |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Code          | [startreedata/pinot-recipes/import-data-files-different-directories](https://github.com/startreedata/pinot-recipes/import-data-files-different-directories) |

## Prerequisites

To follow the code examples in this guide, you must [install Docker](https://docs.docker.com/get-docker/) locally and download recipes.

## Navigate to recipe

1. If you haven't already, download recipes.
2. In terminal, go to the recipe by running the following command:

```bash  theme={null}
cd pinot-recipes/recipes/import-data-files-different-directories
```

## Launch Pinot Cluster

You can spin up a Pinot Cluster by running the following command:

```bash  theme={null}
docker-compose up
```

This command will run a single instance of the Pinot Controller, Pinot Server, Pinot Broker, and Zookeeper. You can find the [docker-compose.yml](https://github.com/startreedata/pinot-recipes/blob/main/recipes/import-data-files-different-directories/docker-compose.yml) file on GitHub.

## Dataset

We're going to import the following CSV files:

### input/2000\_2009/2000\_2009.csv

```csv  theme={null}
title,genre,year,id
"The Da Vinci Code","Thriller",2006,331567813147483648
"Ice Age: The Meltdown","Children",2006,337567813147483648
"P.S. I Love You","Romance",2007,346905752147483649
"The Curious Case of Benjamin Button","Fantasy",2008,394030854147483651
"Harry Potter and the Half-Blood Prince","Fantasy",2009,323030454547483651
"The Ugly Truth","Comedy",2009,332567813147483648
```

### input/2010\_2019/2010\_2019.csv

```csv  theme={null}
title,genre,year,id
"Dear John","Drama",2010,300441473147483650
"Valentine's Day","Comedy",2010,361248901147483647
"Minions","Comedy",2015,333567813147483648
```

### input/2020\_present/2020\_present.csv

```csv  theme={null}
title,genre,year,id
"Uncharted","Action",2022,493030854147483651
```

## Pinot Schema and Table

Now let's create a Pinot Schema and Table.

A common pattern when creating a schema is to create columns that map directly to the names of the fields in our data source. We can't do that in this case since column names can't contain spaces, so instead we'll have the following:

### config/schema.json

```json  theme={null}
{
  "schemaName": "movies",
  "dimensionFieldSpecs": [{
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

We'll also have the following table config:

### config/table.json\*

```json  theme={null}
{
  "tableName": "movies",
  "tableType": "OFFLINE",
  "segmentsConfig": {
    "replication": 1
  },
  "tenants": {
    "broker": "DefaultTenant",
    "server": "DefaultTenant"
  },
  "tableIndexConfig": {
    "loadMode": "MMAP"
  },
  "ingestionConfig": {
    "batchIngestionConfig": {
      "segmentIngestionType": "APPEND",
      "segmentIngestionFrequency": "DAILY"
    },
    "transformConfigs": []
  },
  "metadata": {}
}
```

You can create the table and schema by running the following command:

```bash  theme={null}
docker run \
   --network csv \
   -v $PWD/config:/config \
   apachepinot/pinot:1.0.0 AddTable \
     -tableConfigFile /config/table.json   \
     -schemaFile /config/schema.json \
     -controllerHost "pinot-controller-csv" \
    -exec
```

You should see a message similar to the following if everything is working correctly:

```text  theme={null}
2021/11/25 12:02:04.606 INFO [AddTableCommand] [main] Executing command: AddTable -tableConfigFile /config/table.json -schemaFile /config/schema.json -controllerProtocol http -controllerHost 192.168.144.3 -controllerPort 9000 -user null -password [hidden] -exec
2021/11/25 12:02:05.084 INFO [AddTableCommand] [main] {"status":"Table movies_OFFLINE succesfully added"}
```

## Ingestion Job

Now we’re going to import the CSV file into Pinot.
We'll do this with the following ingestion spec:

### config/job-spec.yml

```yaml  theme={null}
executionFrameworkSpec:
  name: 'standalone'
  segmentGenerationJobRunnerClassName: 'org.apache.pinot.plugin.ingestion.batch.standalone.SegmentGenerationJobRunner'
  segmentTarPushJobRunnerClassName: 'org.apache.pinot.plugin.ingestion.batch.standalone.SegmentTarPushJobRunner'
segmentNameGeneratorSpec:
  configs:
    use.global.directory.sequence.id: true
jobType: SegmentCreationAndTarPush
inputDirURI: '/input'
includeFileNamePattern: 'glob:**/*.csv'
outputDirURI: '/data'
pinotFSSpecs:
  - scheme: file
    className: org.apache.pinot.spi.filesystem.LocalPinotFS
recordReaderSpec:
  dataFormat: 'csv'
  className: 'org.apache.pinot.plugin.inputformat.csv.CSVRecordReader'
  configClassName: 'org.apache.pinot.plugin.inputformat.csv.CSVRecordReaderConfig'
tableSpec:
  tableName: 'movies'
pinotClusterSpecs:
  - controllerURI: 'http://pinot-controller-csv:9000'
pushJobSpec:
  pushParallelism: 2
  pushAttempts: 2
```

The part of this file that we're most interested in is the following section:

```yaml  theme={null}
segmentNameGeneratorSpec:
  configs:
    use.global.directory.sequence.id: true
```

This config makes sure that the segment id (that's used in the segment name) is incremented globally across all directories, rather than being incremented on a directory by directory basis.

If we don't set this config, every segment that's created from a CSV file will be replaced by the segment created from the next CSV file. We would end up with only one segment that contained the rows from the last CSV that got processed.

<Info>We only need to use this config when importing data for tables that don't have a timestamp field. If a timestamp field is specified, timestamps are used in the segment name and the likelihood of segments being overridden is reduced.</Info>

You can run the following command to run the import:

```bash  theme={null}
docker run \
   --network csv \
   -v $PWD/config:/config \
   -v $PWD/data:/data \
   -v $PWD/input:/input \
   apachepinot/pinot:1.0.0 LaunchDataIngestionJob \
  -jobSpecFile /config/job-spec.yml
```

## Querying

Once that's completed, navigate to [localhost:9000/#/query](http://localhost:9000/#/query) and click on the `crimes` table or copy/paste the following query:

```sql  theme={null}
select * 
from movies 
limit 10
```

You will see the following output:

| genre    | id                 | title                                  | year |
| -------- | ------------------ | -------------------------------------- | ---- |
| Action   | 493030854147483651 | Uncharted                              | 2022 |
| Drama    | 300441473147483650 | Dear John                              | 2010 |
| Comedy   | 361248901147483647 | Valentine's Day                        | 2010 |
| Comedy   | 333567813147483648 | Minions                                | 2015 |
| Thriller | 331567813147483648 | The Da Vinci Code                      | 2006 |
| Children | 337567813147483648 | Ice Age: The Meltdown                  | 2006 |
| Romance  | 346905752147483649 | P.S. I Love You                        | 2007 |
| Fantasy  | 394030854147483651 | The Curious Case of Benjamin Button    | 2008 |
| Fantasy  | 323030454547483651 | Harry Potter and the Half-Blood Prince | 2009 |
| Comedy   | 332567813147483648 | The Ugly Truth                         | 2009 |

*Query Results*

Built with [Mintlify](https://mintlify.com).
