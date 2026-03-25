# Source: https://docs.startree.ai/recipes/ingest-json-files.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Ingesting JSON files

Learn how to ingest JSON documents from a newline-delimited JSON (jsonlines) file. Watch the following video, or complete the tutorial below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/zuuQwqkXNK8" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

| Pinot Version | 1.0.0                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Code          | [startreedata/pinot-recipes/ingest-json-files](https://github.com/startreedata/pinot-recipes/tree/main/recipes/ingest-json-files) |

## Prerequisites

To follow the code examples in this guide, you must [install Docker](https://docs.docker.com/get-docker/) locally and download recipes.

Clone this repository and navigate to this recipe:

```bash  theme={null}
git clone git@github.com:startreedata/pinot-recipes.git
cd pinot-recipes/recipes/ingest-json-files
```

## Run the recipe

Spin up a Pinot cluster using Docker Compose:

```bash  theme={null}
docker compose up
```

Open another tab to add the `movies` table:

```bash  theme={null}
docker run \
   --network json \
   -v $PWD/config:/config \
   apachepinot/pinot:1.0.0 AddTable \
     -tableConfigFile /config/table.json   \
     -schemaFile /config/schema.json \
     -controllerHost "pinot-controller-json" \
    -exec
```

Import [data/ingest.json](data/import.json) into Pinot:

```bash  theme={null}
docker run \
   --network json \
   -v $PWD/config:/config \
   -v $PWD/data:/data \
   apachepinot/pinot:1.0.0 LaunchDataIngestionJob \
     -jobSpecFile /config/job-spec.yml
```

Navigate to [http://localhost:9000/#/query](http://localhost:9000/#/query) and run the following query:

```sql  theme={null}
select * 
from movies 
limit 10
```

You will see the following output:

| genre   | id                 | title                               | year |
| ------- | ------------------ | ----------------------------------- | ---- |
| Drama   | 300441473147483650 | Dear John                           | 2010 |
| Comedy  | 332567813147483648 | The Ugly Truth                      | 2009 |
| Romance | 346905752147483649 | P.S. I Love You                     | 2007 |
| Comedy  | 361248901147483647 | Valentine's Day                     | 2010 |
| Fantasy | 394030854147483651 | The Curious Case of Benjamin Button | 2008 |

Built with [Mintlify](https://mintlify.com).
