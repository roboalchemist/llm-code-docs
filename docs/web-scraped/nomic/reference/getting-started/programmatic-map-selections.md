# Nomic Documentation

Source: https://docs.nomic.ai/reference/getting-started/programmatic-map-selections

The Atlas interface provides various selections (filters) you may want to apply to your map, including semantic search and text search on
your uploaded data columns.

This capability can also be leveraged programmatically through our query endpoints.

See the API reference for the selection endpoint and vector search endpoint for more details.

## Querying with selections​

In this section, we cover several examples of different selections you can programmatically query.
All queries are built off the domain specific language (DSL) we use for Atlas operations such as tagging.
The endpoints will output a JSON list of data point ids that match your query.

The examples below use a projection_id (f1e499cd-b5c1-4d31-b38a-fff61e1f8b59) for a data map of product descriptions. You can find the projection_id on your dataset preview page's, located at atlas.nomic.ai/data/<YOUR_ORG_NAME>/<YOUR_DATASET_NAME>.

```
f1e499cd-b5c1-4d31-b38a-fff61e1f8b59
```

```
projection_id
```

```
atlas.nomic.ai/data/<YOUR_ORG_NAME>/<YOUR_DATASET_NAME>
```

### Search Query​

You can search for any keyword over any column in your dataset by performing the below query:

```
curl -L "https://api-atlas.nomic.ai/v1/query" \-H "Content-Type: application/json" \-H "Authorization: Bearer $NOMIC_API_KEY" \-d '{    "projection_id": "f1e499cd-b5c1-4d31-b38a-fff61e1f8b59",    "selection": {        "method": "composition",        "conjunctor": "ALL",        "filters": [            {                "method": "search",                "query": "comfortable",                "field": "title"            }        ]    }}'
```

### Inverting Filters​

You can invert your filter (e.g. returning all documents that do not contain a certain keyword) by setting
polarity to false.

```
polarity
```

```
curl -L "https://api-atlas.nomic.ai/v1/query" \-H "Content-Type: application/json" \-H "Authorization: Bearer $NOMIC_API_KEY" \-d '{    "projection_id": "f1e499cd-b5c1-4d31-b38a-fff61e1f8b59",    "selection": {        "method": "composition",        "conjunctor": "ALL",        "filters": [            {                "polarity": false,                "method": "search",                "query": "comfortable",                "field": "title"            }        ]    }}'
```

### Composing Filters​

You can combine different filters as shown below. Atlas supports two operations for composing filters: ANY will return
results that match at least one of the filters, ALL will return results that exactly match all the filters.

```
ANY
```

```
ALL
```

```
curl -L "https://api-atlas.nomic.ai/v1/query" \-H "Content-Type: application/json" \-H "Authorization: Bearer $NOMIC_API_KEY" \-d '{    "projection_id": "f1e499cd-b5c1-4d31-b38a-fff61e1f8b59",    "selection": {        "method": "composition",        "conjunctor": "ALL",        "filters": [            {                "method": "search",                "query": "comfortable",                "field": "title"            },            {                "method": "search",                "query": "outdoor",                "field": "title"            }        ]    }}'
```

### Nested Query Composition​

You can create arbitrarily complex queries by nesting composition filters. Each composition filter can contain other composition filters in its filters array, allowing you to express complex logical conditions.

```
filters
```

In this example, the query will return results that have "comfortable" in the title AND have either "dog" OR "cat" in the title.

```
curl -L "https://api-atlas.nomic.ai/v1/query/topk" \-H "Content-Type: application/json" \-H "Authorization: Bearer $NOMIC_API_KEY" \-d '{    "projection_id": "f1e499cd-b5c1-4d31-b38a-fff61e1f8b59",    "k": 3,    "fields": ["title", "average_rating", "price"],    "query": "footwear",    "selection": {        "method": "composition",        "conjunctor": "ALL",        "filters": [            {                "method": "search",                "query": "comfortable",                "field": "title"            },            {                "method": "composition",                "conjunctor": "ANY",                "filters": [                    {                        "method": "search",                        "query": "dog",                        "field": "title"                    },                    {                        "method": "search",                        "query": "cat",                        "field": "title"                    }                            ]            }        ]    }}'
```

### Range Filters​

You can filter data points based on numerical ranges or datetime ranges.

```
curl -L "https://api-atlas.nomic.ai/v1/query" \-H "Content-Type: application/json" \-H "Authorization: Bearer $NOMIC_API_KEY" \-d '{    "projection_id": "f1e499cd-b5c1-4d31-b38a-fff61e1f8b59",    "selection": {        "method": "composition",        "conjunctor": "ALL",        "filters": [            {                "method": "range",                "range": [1000000, 2000000],                "field": "complaint_id"            }        ]    }}'
```

For datetime fields, use milliseconds since Unix epoch. For example:

```
curl -L "https://api-atlas.nomic.ai/v1/query" \-H "Content-Type: application/json" \-H "Authorization: Bearer $NOMIC_API_KEY" \-d '{    "projection_id": "f1e499cd-b5c1-4d31-b38a-fff61e1f8b59",    "selection": {        "method": "composition",        "conjunctor": "ALL",        "filters": [            {                "method": "range",                "range": [1640995200000, 1672531200000],  // 2022-01-01 to 2023-01-01                "field": "published_date"            }        ]    }}'
```

### Categorical Filters​

You can filter data points based on categorical values:

```
curl -L "https://api-atlas.nomic.ai/v1/query" \-H "Content-Type: application/json" \-H "Authorization: Bearer $NOMIC_API_KEY" \-d '{    "projection_id": "f1e499cd-b5c1-4d31-b38a-fff61e1f8b59",    "selection": {        "method": "composition",        "conjunctor": "ALL",        "filters": [            {                "method": "category",                "field": "published_platform",                "values": ["Mobile"]            }        ]    }}'
```

## Vector Search​

Use the topk endpoint to perform a vector search over your dataset. This returns a sorted list of the top most semantically similar results to your query.
You can control which fields from the data get returned in the API response with the fields parameter.
The query parameter accepts either:

```
topk
```

```
fields
```

```
query
```

- A text string that will be embedded using Nomic's text embedding model
- An embedding vector (a list of floats matching the dimensionality of your dataset's embeddings). If you created your Atlas map with text/images, then Atlas created your embeddings using our text/image embedding models, so your query should be 768 dimensions to match our models.
- Text Query
- Vector Query
```
curl -L "https://api-atlas.nomic.ai/v1/query/topk" \-H "Content-Type: application/json" \-H "Authorization: Bearer $NOMIC_API_KEY" \-d '{    "projection_id": "f1e499cd-b5c1-4d31-b38a-fff61e1f8b59",    "k": 3,    "fields": ["title", "average_rating", "price"],    "query": "footwear"}'
```

```
curl -L "https://api-atlas.nomic.ai/v1/query/topk" \-H "Content-Type: application/json" \-H "Authorization: Bearer $NOMIC_API_KEY" \-d '{    "projection_id": "f1e499cd-b5c1-4d31-b38a-fff61e1f8b59",    "k": 3,    "fields": ["title", "average_rating", "price"],    "query": [0.1234, 0.5678, 0.9123, 0.4567, 0.7890, 0.3456, ..., 0.9821]}'
```

### Vector Search with Selection​

You can perform a vector search with a selection applied to your data. The selection is applied first to your data points,
and then top K nearest neighbors are then fetched from the filtered results.
Note, that this is not the same as composing filters with a semantic search filter.

```
curl -L "https://api-atlas.nomic.ai/v1/query/topk" \-H "Content-Type: application/json" \-H "Authorization: Bearer $NOMIC_API_KEY" \-d '{    "projection_id": "f1e499cd-b5c1-4d31-b38a-fff61e1f8b59",    "k": 3,    "fields": ["title", "average_rating", "price"],    "query": "footwear",    "selection": {        "method": "composition",        "conjunctor": "ALL",        "filters": [            {                "method": "search",                "query": "comfortable",                "field": "title"            }        ]    }}'
```

- Querying with selectionsSearch QueryInverting FiltersComposing FiltersNested Query CompositionRange FiltersCategorical Filters
- Search Query
- Inverting Filters
- Composing Filters
- Nested Query Composition
- Range Filters
- Categorical Filters
- Vector SearchVector Search with Selection
- Vector Search with Selection
