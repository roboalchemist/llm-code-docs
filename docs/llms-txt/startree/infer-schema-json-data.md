# Source: https://docs.startree.ai/recipes/infer-schema-json-data.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Infer Pinot Schema from JSON Data

In this recipe we'll learn how to infer a Pinot schema from a JSON input file.

| Pinot Version | 0.9.0                                                                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Code          | [startreedata/pinot-recipes/infer-schema-json-data](https://github.com/startreedata/pinot-recipes/tree/main/recipes/infer-schema-json-data) |

## Prerequisites

To follow the code examples in this guide, you must [install Docker](https://docs.docker.com/get-docker/) locally and download recipes.

## Navigate to recipe

1. If you haven't already, download recipes.
2. In terminal, go to the recipe by running the following command:

```bash  theme={null}
cd pinot-recipes/recipes/infer-schema-json-data
```

## JSON Data

We're going to infer a Pinot schema from the following input file:

```json  theme={null}
{
  "id":"7044874109",
  "type":"PushEvent",
  "actor":{
    "id":18542751,
    "login":"LimeVista",
    "display_login":"LimeVista",
    "gravatar_id":"",
    "url":"https://api.github.com/users/LimeVista",
    "avatar_url":"https://avatars.githubusercontent.com/u/18542751?"
  },
  "repo":{
    "id":115911530,
    "name":"LimeVista/Tapes",
    "url":"https://api.github.com/repos/LimeVista/Tapes"
  },
  "payload":{
    "push_id":2226018068,
    "size":1,
    "distinct_size":1,
    "ref":"refs/heads/master",
    "head":"c5fc8b32a9ead1eba315d97410cb4ac1e6ca1774",
    "before":"892d872c5d3f24cc6837900c9f4618dc2fe92930",
    "commits":[
      {
        "sha":"c5fc8b32a9ead1eba315d97410cb4ac1e6ca1774",
        "author":{
          "name":"Lime",
          "email":"4cc153d999e24274955157fc813e6f92f821525d@outlook.com"
        },
        "message":"Merge branch 'master' of https://github.com/LimeVista/Tapes\\n\\n# Conflicts:\\n#\\t.gitignore",
        "distinct":true,
        "url":"https://api.github.com/repos/LimeVista/Tapes/commits/c5fc8b32a9ead1eba315d97410cb4ac1e6ca1774"
      }
    ]
  },
  "public":true,
  "created_at":"2018-01-01T11:00:00Z"
}
```

*/data/github.json*

## Infer schema

Now we're going to infer a schema for this input file. We can do this using the `JsonToPinotSchema` command.

### Schema with only dimension fields

You can generate a schema file that creates a dimension column field per JSON field, by running the following command:

```bash  theme={null}
docker run \
  -v ${PWD}/data/github.json:/data/github.json \
  -v ${PWD}/config:/config \
  apachepinot/pinot:0.9.3 JsonToPinotSchema \
  -jsonFile /data/github.json \
  -pinotSchemaName="github" \
  -outputDir="/config" \
  -dimensions=""
```

A JSON file will be written to `./config/github.json`, the contents of which are shown below:

```json  theme={null}
{
  "schemaName" : "github",
  "dimensionFieldSpecs" : [ {
    "name" : "id",
    "dataType" : "STRING"
  }, {
    "name" : "type",
    "dataType" : "STRING"
  }, {
    "name" : "actor.id",
    "dataType" : "INT"
  }, {
    "name" : "actor.login",
    "dataType" : "STRING"
  }, {
    "name" : "actor.display_login",
    "dataType" : "STRING"
  }, {
    "name" : "actor.gravatar_id",
    "dataType" : "STRING"
  }, {
    "name" : "actor.url",
    "dataType" : "STRING"
  }, {
    "name" : "actor.avatar_url",
    "dataType" : "STRING"
  }, {
    "name" : "repo.id",
    "dataType" : "INT"
  }, {
    "name" : "repo.name",
    "dataType" : "STRING"
  }, {
    "name" : "repo.url",
    "dataType" : "STRING"
  }, {
    "name" : "payload.push_id",
    "dataType" : "LONG"
  }, {
    "name" : "payload.size",
    "dataType" : "INT"
  }, {
    "name" : "payload.distinct_size",
    "dataType" : "INT"
  }, {
    "name" : "payload.ref",
    "dataType" : "STRING"
  }, {
    "name" : "payload.head",
    "dataType" : "STRING"
  }, {
    "name" : "payload.before",
    "dataType" : "STRING"
  }, {
    "name" : "payload.commits",
    "dataType" : "STRING"
  }, {
    "name" : "public",
    "dataType" : "BOOLEAN"
  }, {
    "name" : "created_at",
    "dataType" : "STRING"
  } ]
}
```

*./config/github.json*

### Schema with time column

We should probably specify the `created_at` field as a date time field, which we can do using the following command:

```bash  theme={null}
docker run \
  -v ${PWD}/data/github.json:/data/github.json \
  -v ${PWD}/config:/config \
  apachepinot/pinot:0.9.3 JsonToPinotSchema \
  -jsonFile /data/github.json \
  -pinotSchemaName="github_with_ts" \
  -outputDir="/config" \
  -timeColumnName=created_at
```

A JSON file will be written to `./config/github.json`, the contents of which are shown below:

```json  theme={null}
{
  "schemaName" : "github_with_ts",
  "dimensionFieldSpecs" : [ {
    "name" : "id",
    "dataType" : "STRING"
  }, {
    "name" : "type",
    "dataType" : "STRING"
  }, {
    "name" : "actor.id",
    "dataType" : "INT"
  }, {
    "name" : "actor.login",
    "dataType" : "STRING"
  }, {
    "name" : "actor.display_login",
    "dataType" : "STRING"
  }, {
    "name" : "actor.gravatar_id",
    "dataType" : "STRING"
  }, {
    "name" : "actor.url",
    "dataType" : "STRING"
  }, {
    "name" : "actor.avatar_url",
    "dataType" : "STRING"
  }, {
    "name" : "repo.id",
    "dataType" : "INT"
  }, {
    "name" : "repo.name",
    "dataType" : "STRING"
  }, {
    "name" : "repo.url",
    "dataType" : "STRING"
  }, {
    "name" : "payload.push_id",
    "dataType" : "LONG"
  }, {
    "name" : "payload.size",
    "dataType" : "INT"
  }, {
    "name" : "payload.distinct_size",
    "dataType" : "INT"
  }, {
    "name" : "payload.ref",
    "dataType" : "STRING"
  }, {
    "name" : "payload.head",
    "dataType" : "STRING"
  }, {
    "name" : "payload.before",
    "dataType" : "STRING"
  }, {
    "name" : "payload.commits",
    "dataType" : "STRING"
  }, {
    "name" : "public",
    "dataType" : "BOOLEAN"
  } ],
  "dateTimeFieldSpecs" : [ {
    "name" : "created_at",
    "dataType" : "STRING",
    "format" : "1:DAYS:EPOCH",
    "granularity" : "1:DAYS"
  } ]
}
```

*./config/github\_with\_ts.json*

### Schema with unnested fields

At the moment the `payload.commits` JSON array is stored as a string. We can unnest each of the values in the documents in the array, by running the following command:

```bash  theme={null}
docker run \
  -v ${PWD}/data/github.json:/data/github.json \
  -v ${PWD}/config:/config \
  apachepinot/pinot:0.9.3 JsonToPinotSchema \
  -jsonFile /data/github.json \
  -pinotSchemaName="github_unnest" \
  -outputDir="/config" \
  -timeColumnName=created_at \
  -fieldsToUnnest=payload.commits
```

A JSON file will be written to `./config/github_unnest.json`, the contents of which are shown below:

```json  theme={null}
{
  "schemaName" : "github_unnest",
  "dimensionFieldSpecs" : [ {
    "name" : "id",
    "dataType" : "STRING"
  }, {
    "name" : "type",
    "dataType" : "STRING"
  }, {
    "name" : "actor.id",
    "dataType" : "INT"
  }, {
    "name" : "actor.login",
    "dataType" : "STRING"
  }, {
    "name" : "actor.display_login",
    "dataType" : "STRING"
  }, {
    "name" : "actor.gravatar_id",
    "dataType" : "STRING"
  }, {
    "name" : "actor.url",
    "dataType" : "STRING"
  }, {
    "name" : "actor.avatar_url",
    "dataType" : "STRING"
  }, {
    "name" : "repo.id",
    "dataType" : "INT"
  }, {
    "name" : "repo.name",
    "dataType" : "STRING"
  }, {
    "name" : "repo.url",
    "dataType" : "STRING"
  }, {
    "name" : "payload.push_id",
    "dataType" : "LONG"
  }, {
    "name" : "payload.size",
    "dataType" : "INT"
  }, {
    "name" : "payload.distinct_size",
    "dataType" : "INT"
  }, {
    "name" : "payload.ref",
    "dataType" : "STRING"
  }, {
    "name" : "payload.head",
    "dataType" : "STRING"
  }, {
    "name" : "payload.before",
    "dataType" : "STRING"
  }, {
    "name" : "payload.commits.sha",
    "dataType" : "STRING"
  }, {
    "name" : "payload.commits.author.name",
    "dataType" : "STRING"
  }, {
    "name" : "payload.commits.author.email",
    "dataType" : "STRING"
  }, {
    "name" : "payload.commits.message",
    "dataType" : "STRING"
  }, {
    "name" : "payload.commits.distinct",
    "dataType" : "BOOLEAN"
  }, {
    "name" : "payload.commits.url",
    "dataType" : "STRING"
  }, {
    "name" : "public",
    "dataType" : "BOOLEAN"
  } ],
  "dateTimeFieldSpecs" : [ {
    "name" : "created_at",
    "dataType" : "STRING",
    "format" : "1:DAYS:EPOCH",
    "granularity" : "1:DAYS"
  } ]
}
```

*./config/github\_unnest.json*

Built with [Mintlify](https://mintlify.com).
