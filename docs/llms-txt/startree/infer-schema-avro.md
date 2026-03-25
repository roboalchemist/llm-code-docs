# Source: https://docs.startree.ai/recipes/infer-schema-avro.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Infer Pinot Schema from Avro Schema

In this recipe, we'll learn how to infer a Pinot schema from an Avro schema.

| Pinot Version | 0.9.0                                                                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Code          | [startreedata/pinot-recipes/infer-schema-avro-data](https://github.com/startreedata/pinot-recipes/tree/main/recipes/infer-schema-avro-data) |

## Prerequisites

To follow the code examples in this guide, you must [install Docker](https://docs.docker.com/get-docker/) locally and download recipes.

## Navigate to recipe

1. If you haven't already, download recipes.
2. In the terminal, go to the recipe by running the following command:

```bash  theme={null}
cd pinot-recipes/recipes/infer-schema-avro-data
```

## JSON Data

We're going to infer a Pinot schema from the following Avro schema:

```json  theme={null}
{
  "type":"record",
  "namespace":"com.simonaubury",
  "name":"MastodonDetails",
  "fields":[
    {"name":"m_id","type":"long","default":0},
    {"name":"created_at","type": "int","logicalType":"date"},
    {"name":"created_at_str","type":"string","default":"unknown"},
    {"name":"app","type":"string","default":"unknown"},
    {"name":"url","type":"string","default":"null"},
    {"name":"base_url","type":"string","default":"null"},
    {"name":"language","type":"string","default":"null"},
    {"name":"favourites","type":"int","default":0},
    {"name":"username","type":"string","default":""},
    {"name":"bot","type":"boolean"},
    {"name":"tags","type":"int","default":0},
    {"name":"characters","type":"int","default":0},
    {"name":"words","type":"int","default":0},
    {"name":"mastodon_text","type":"string","default":"null"}
  ]
}
```

*/avro/mastodon-topic-value.avsc*

## Infer schema

Now we're going to infer a schema for this input file.
We can do this using the `AvroSchemaToPinotSchema` command.

You can generate a schema file that creates a dimension column field per Aro field, by running the following command:

```bash  theme={null}
docker run \
  -v ${PWD}/config:/config \
  -v ${PWD}/avro:/avro \
  apachepinot/pinot:1.0.0 AvroSchemaToPinotSchema \
  -avroSchemaFile /avro/mastodon-topic-value.avsc \
  -pinotSchemaName="mastodon" \
  -outputDir="/config" \
  -dimensions="" \
  -timeColumnName "created_at" \
  -metrics "favourites,words,characters,tags"
```

A JSON file will be written to `./config/mastodon.json`, the contents of which are shown below:

```json  theme={null}
{
  "schemaName": "mastodon",
  "dimensionFieldSpecs": [
    {"name": "m_id", "dataType": "LONG"},
    {"name": "created_at_str", "dataType": "STRING"},
    {"name": "app", "dataType": "STRING"},
    {"name": "url", "dataType": "STRING"},
    {"name": "base_url", "dataType": "STRING"},
    {"name": "language", "dataType": "STRING"},
    {"name": "username", "dataType": "STRING"},
    {"name": "bot", "dataType": "BOOLEAN"},
    {"name": "mastodon_text", "dataType": "STRING"}
  ],
  "metricFieldSpecs": [
    {"name": "favourites", "dataType": "INT"},
    {"name": "tags", "dataType": "INT"},
    {"name": "characters", "dataType": "INT"},
    {"name": "words", "dataType": "INT"}
  ],
  "dateTimeFieldSpecs": [
    {
      "name": "created_at",
      "dataType": "INT",
      "format": "1:DAYS:EPOCH",
      "granularity": "1:DAYS"
    }
  ]
}
```

*./config/mastodon.json*

Built with [Mintlify](https://mintlify.com).
