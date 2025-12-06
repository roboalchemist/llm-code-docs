# Vector Search

Source: https://docs.nomic.ai/reference/api/query/vector-search

# Vector Search

```
POST /v1/query/topk
```

## /v1/query/topk

Get sorted results of the top k most semantically similar data points to your query.

The below example demonstrates how to call the endpoint using curl. It includes a vector search query for "footwear", a filter for data with "comfortable" in the title, and will return the fields title, average_rating, and price along with _similarity (which is returned by default).

```
title
```

```
title
```

```
average_rating
```

```
price
```

```
_similarity
```

The results will be 3 data points that contain the text "comfortable" and are most semantically related to "footwear". If fields is not provided, all user-uploaded fields will be returned.

```
fields
```

See this guide for a more detailed walkthrough.

```
curl -X POST 'https://api-atlas.nomic.ai/v1/query/topk' \-H 'Content-Type: application/json' \-H 'Authorization: Bearer $NOMIC_API_KEY' \-d '{    "projection_id": "f1e499cd-b5c1-4d31-b38a-fff61e1f8b59",    "k": 3,    "fields": ["title", "average_rating", "price"],    "query": "footwear",    "selection": {        "method": "composition",        "conjunctor": "ALL",        "filters": [            {                "method": "search",                "query": "comfortable",                "field": "title"            }        ]    }}'
```

## Request​

- application/json
### Body

Body

required

Possible values: >= 1

```
>= 1
```

query

object

required

oneOf

- MOD1
- MOD2
string

- Array [
Array [

number

- ]
]

Possible values: [search_document, search_query, null]

```
search_document
```

```
search_query
```

```
null
```

Default value: search_query

```
search_query
```

selection

object

Possible values: [composition]

```
composition
```

Default value: true

```
true
```

Possible values: [ANY, ALL]

```
ANY
```

```
ALL
```

cherries

object

Default value: true

```
true
```

Possible values: [cherrypick]

```
cherrypick
```

Possible values: >= 2, <= 2

```
>= 2
```

```
<= 2
```

Default value: ``

Possible values: >= 2, <= 2

```
>= 2
```

```
<= 2
```

Default value: ``

filters

object[]

- Array [
Array [

oneOf

- SearchSelection
- NumericRangeSelection
- CategoricalFilterSelection
Default value: true

```
true
```

Possible values: [search]

```
search
```

Default value: true

```
true
```

Default value: true

```
true
```

Possible values: [range]

```
range
```

Possible values: >= 2, <= 2

```
>= 2
```

```
<= 2
```

Default value: true

```
true
```

Possible values: [category]

```
category
```

values

object

required

oneOf

- MOD1
- MOD2
- MOD3
- Array [
Array [

string

- ]
]

- Array [
Array [

number

- ]
]

- Array [
Array [

boolean

- ]
]

- ]
]

Default value: true

```
true
```

## Responses​

- 200
- 400
- 401
Returns the data included in your optional selection most semantically similar to your query. Each object contains the fields specified in the fields request parameter.

```
fields
```

- application/json
- Schema
- Example (from schema)
Schema

```
{  "data": [    {      "title": "Guide Gear Lace Up Walking Shoes for Men, Comfortable Shoes for Work, Casual Working",      "average_rating": 3.5999999046325684,      "price": 39.9900016784668,      "_similarity": 0.7691732048988342    },    {      "title": "Womens High Heel Wedges with Comfortable Plantar Orthopedic Sandals, Suitable for Outdoor",      "average_rating": 2.0999999046325684,      "price": null,      "_similarity": 0.7547734975814819    },    {      "title": "Men's Military Tactical Boots Lightweight Work Boots Combat Boots Comfortable Hiking Boots Breathable Jungle Boots",      "average_rating": 3.799999952316284,      "price": null,      "_similarity": 0.7544335722923279    }  ]}
```

Bad request

Unauthorized

