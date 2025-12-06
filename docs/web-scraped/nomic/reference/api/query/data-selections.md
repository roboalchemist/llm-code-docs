# Data Selections

Source: https://docs.nomic.ai/reference/api/query/data-selections

# Data Selections

```
POST /v1/query
```

## /v1/query

Execute a query with the given projection ID and filters.

The below example demonstrates how to call the endpoint using curl. It includes the projection_id of our Atlas dataset, and a selection with filters for "comfortable" and "outdoor" in the title field.

```
curl
```

```
projection_id
```

```
title
```

The results will be all the data in the dataset with both the terms "comfortable" and "outdoor" in the title field.

```
title
```

See this guide for a more detailed walkthrough.

```
curl -X POST 'https://api-atlas.nomic.ai/v1/query' \-H 'Content-Type: application/json' \-H 'Authorization: Bearer $NOMIC_API_KEY' \-d '{    "projection_id": "f1e499cd-b5c1-4d31-b38a-fff61e1f8b59",    "selection": {        "method": "composition",        "conjunctor": "ALL",        "filters": [            {                "method": "search",                "query": "comfortable",                "field": "title"            },            {                "method": "search",                "query": "outdoor",                "field": "title"            }        ]    }}'
```

## Request​

- application/json
### Body

Body

required

selection

object

required

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

## Responses​

- 200
- 400
- 401
Returns the datum IDs for each point in your dataset included in your selection.

- application/json
- Schema
- Example (from schema)
Schema

```
{  "data": [    {      "id_": "ASNq"    },    {      "id_": "AS4V"    },    {      "id_": "AQpH"    },    {      "id_": "AWYf"    },    {      "id_": "PQA"    },    {      "id_": "224"    },    {      "id_": "Ab7v"    },    {      "id_": "ATLa"    },    {      "id_": "ASPB"    },    {      "id_": "yrQ"    },    {      "id_": "4eM"    },    {      "id_": "U0g"    },    {      "id_": "AZAd"    },    {      "id_": "AS59"    },    {      "id_": "R24"    },    {      "id_": "AcLc"    },    {      "id_": "5v4"    },    {      "id_": "AWs6"    },    {      "id_": "jYY"    },    {      "id_": "AXXw"    },    {      "id_": "AYEZ"    },    {      "id_": "Abna"    },    {      "id_": "AWfo"    },    {      "id_": "AXnL"    },    {      "id_": "qV8"    },    {      "id_": "Lr8"    },    {      "id_": "AUfu"    },    {      "id_": "NF0"    },    {      "id_": "fUo"    },    {      "id_": "QHY"    },    {      "id_": "Abjw"    },    {      "id_": "KKY"    },    {      "id_": "iFo"    },    {      "id_": "AVHO"    },    {      "id_": "o3U"    },    {      "id_": "5g8"    },    {      "id_": "zj4"    },    {      "id_": "g3Y"    },    {      "id_": "F58"    },    {      "id_": "0OY"    },    {      "id_": "AVOl"    },    {      "id_": "AR/v"    },    {      "id_": "ASKt"    },    {      "id_": "Aazc"    },    {      "id_": "zQM"    }  ]}
```

Bad request

Unauthorized

