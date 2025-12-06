# Embed Text

Source: https://docs.nomic.ai/reference/api/embed-text-v-1-embedding-text-post

# Embed Text

```
POST /v1/embedding/text
```

## /v1/embedding/text

Generates text embeddings

nomic-embed-text was trained to support these tasks:

```
nomic-embed-text
```

- search_document (embedding document chunks for search & retrieval)
```
search_document
```

- search_query (embedding queries for search & retrieval)
```
search_query
```

- classification (embeddings for text classification)
```
classification
```

- clustering (embeddings for cluster visualization)
```
clustering
```

In the Nomic API or Python client, specify your task with the task_type parameter (default is search_document if no task_type is provided)

```
task_type
```

```
search_document
```

```
task_type
```

Using nomic-embed-text with other libraries requires you to use a prefix to specify your embedding task. See our HuggingFace model card for details.

```
nomic-embed-text
```

## Request​

- application/json
### Body

Body

required

A batch of text you want embedded.

Possible values: [nomic-embed-text-v1, nomic-embed-text-v1.5]

```
nomic-embed-text-v1
```

```
nomic-embed-text-v1.5
```

Default value: nomic-embed-text-v1

```
nomic-embed-text-v1
```

The model to use when embedding.

task_type

object

The downstream task to generate embeddings for. Options are search_document, search_query, classification, and clustering.

```
search_document
```

```
search_query
```

```
classification
```

```
clustering
```

anyOf

- MOD1
string

Possible values: [truncate, mean]

```
truncate
```

```
mean
```

Default value: mean

```
mean
```

How to handle text longer than the model can accept.

Default value: 8192

```
8192
```

Maximum amount of tokens per text. Defaults to 8192 if long_text_mode is "mean", or the maximum model input size if long_text_mode is "truncate".

```
long_text_mode
```

```
long_text_mode
```

dimensionality

object

Optionally reduce embedding dimensionality. Defaults to full-size embeddings if unspecified. Only applies to nomic-embed-text-v1.5.

```
nomic-embed-text-v1.5
```

anyOf

- MOD1
integer

## Responses​

- 200
- 422
Successful Response

- application/json
- Schema
- Example (from schema)
Schema

The embeddings

usage

object

required

The embedding usage

The number of non-generated tokens ingested.

The total tokens used.

Possible values: [nomic-embed-text-v1, nomic-embed-text-v1.5]

```
nomic-embed-text-v1
```

```
nomic-embed-text-v1.5
```

The model used to produce the embeddings.

```
{  "embeddings": [    [      0    ]  ],  "usage": {    "prompt_tokens": 0,    "total_tokens": 0  },  "model": "nomic-embed-text-v1"}
```

Validation Error

- application/json
- Schema
- Example (from schema)
Schema

detail

object[]

- Array [
Array [

loc

object[]

required

- Array [
Array [

anyOf

- MOD1
- MOD2
string

integer

- ]
]

- ]
]

```
{  "detail": [    {      "loc": [        "string",        0      ],      "msg": "string",      "type": "string"    }  ]}
```

