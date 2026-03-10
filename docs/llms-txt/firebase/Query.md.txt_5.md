# Source: https://firebase.google.com/docs/reference/data-connect/gql/query.md.txt

This reference doc is generated based on this [example schema](https://firebase.google.com/docs/reference/data-connect#graphql_schema).

Query operations define the read-only entry points for fetching data in a GraphQL schema.

All queries are generated based on customer defined [`@table`](https://firebase.google.com/docs/reference/data-connect/gql/directive#table) types.
Customer defined queries are not supported.

## Data Connect Generated

### mainTable: [`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)

✨ Look up a single [`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable) based on `id`, `key` or `first` and return selected fields (or `null` if not found).

| Field | Type | Description |
|---|---|---|
| `id` | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID) | The unique ID of the object. |
| `key` | [`MainTable_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Key) | The key used to identify the object. |
| `first` | [`MainTable_FirstRow`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_FirstRow) | Fetch the first row based on the filters and ordering. |

### mainTables: [`[MainTable!]!`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)

✨ List [`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable) objects in the table and return selected fields, optionally filtered by `where` conditions

| Field | Type | Description |
|---|---|---|
| `where` | [`MainTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Filter) | Filter condition to narrow down the query results. |
| `orderBy` | [`[MainTable_Order!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Order) | Order the query results by specific fields. |
| `offset` | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Number of rows to skip before starting to return the results. |
| `limit` | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Maximum number of rows to return (defaults to 100 rows). |
| `distinct` | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean) | Set to true to return distinct results. |
| `having` | [`MainTable_Having`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Having) | Filter condition to apply to the groups of aggregate queries. |

### mainTables_search: [`[MainTable!]!`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)

✨ Search for [`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable) objects where fields with the @searchable directive contain a query string. Return selected fields, ordered by relevance of the query.)

| Field | Type | Description |
|---|---|---|
| `where` | [`MainTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Filter) | Filter condition to narrow down the query results. |
| `orderBy` | [`[MainTable_Order!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Order) | Order the query results by specific fields. |
| `offset` | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Number of rows to skip before starting to return the results. |
| `limit` | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Maximum number of rows to return (defaults to 100 rows). |
| `distinct` | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean) | Set to true to return distinct results. |
| `having` | [`MainTable_Having`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Having) | Filter condition to apply to the groups of aggregate queries. |
| `query` | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | The search term to use. |
| `relevanceThreshold` | [`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float) | Relevance threshold to use for search results. If a result has a relevance score below this threshold, it will not be returned. |
| `queryFormat` | [`Search_QueryFormat`](https://firebase.google.com/docs/reference/data-connect/gql/enum#Search_QueryFormat) | The query format for the search term. |

### mainTables_vectorField_similarity: [`[MainTable!]!`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)

✨ List [`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable) objects and return selected fields, ordered by vector similarity between the `vectorField` field and `compare_embed`.
(Alternatively, `compare` can be used if the input is a raw Vector.)

| Field | Type | Description |
|---|---|---|
| `compare` | [`Vector`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector) | Vector to compare with the stored vectors. |
| `compare_embed` | [`Vector_Embed`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Vector_Embed) | ✨ `_embed` server value variant of `compare` (Vector to compare with the stored vectors.) |
| `method` | [`VectorSimilarityMethod`](https://firebase.google.com/docs/reference/data-connect/gql/enum#VectorSimilarityMethod) | Similarity method to use for vector comparison (defaults to `INNER_PRODUCT`). |
| `within` | [`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float) | Threshold for distance comparison. |
| `where` | [`MainTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Filter) | Filter condition to apply when searching for similar vectors. |
| `limit` | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Limit the number of similar vectors returned (defaults to 100 rows). |

### manyToManyJoinTable: [`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable)

✨ Look up a single [`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable) based on `id`, `key` or `first` and return selected fields (or `null` if not found).

| Field | Type | Description |
|---|---|---|
| `key` | [`ManyToManyJoinTable_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Key) | The key used to identify the object. |
| `first` | [`ManyToManyJoinTable_FirstRow`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_FirstRow) | Fetch the first row based on the filters and ordering. |

### manyToManyJoinTables: [`[ManyToManyJoinTable!]!`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable)

✨ List [`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable) objects in the table and return selected fields, optionally filtered by `where` conditions

| Field | Type | Description |
|---|---|---|
| `where` | [`ManyToManyJoinTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Filter) | Filter condition to narrow down the query results. |
| `orderBy` | [`[ManyToManyJoinTable_Order!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Order) | Order the query results by specific fields. |
| `offset` | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Number of rows to skip before starting to return the results. |
| `limit` | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Maximum number of rows to return (defaults to 100 rows). |
| `distinct` | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean) | Set to true to return distinct results. |
| `having` | [`ManyToManyJoinTable_Having`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Having) | Filter condition to apply to the groups of aggregate queries. |

### manyToOneExample: [`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample)

✨ Look up a single [`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample) based on `id`, `key` or `first` and return selected fields (or `null` if not found).

| Field | Type | Description |
|---|---|---|
| `id` | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID) | The unique ID of the object. |
| `key` | [`ManyToOneExample_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Key) | The key used to identify the object. |
| `first` | [`ManyToOneExample_FirstRow`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_FirstRow) | Fetch the first row based on the filters and ordering. |

### manyToOneExamples: [`[ManyToOneExample!]!`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample)

✨ List [`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample) objects in the table and return selected fields, optionally filtered by `where` conditions

| Field | Type | Description |
|---|---|---|
| `where` | [`ManyToOneExample_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Filter) | Filter condition to narrow down the query results. |
| `orderBy` | [`[ManyToOneExample_Order!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Order) | Order the query results by specific fields. |
| `offset` | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Number of rows to skip before starting to return the results. |
| `limit` | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Maximum number of rows to return (defaults to 100 rows). |
| `distinct` | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean) | Set to true to return distinct results. |
| `having` | [`ManyToOneExample_Having`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Having) | Filter condition to apply to the groups of aggregate queries. |

### oneToOneExample: [`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample)

✨ Look up a single [`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample) based on `id`, `key` or `first` and return selected fields (or `null` if not found).

| Field | Type | Description |
|---|---|---|
| `id` | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID) | The unique ID of the object. |
| `key` | [`OneToOneExample_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Key) | The key used to identify the object. |
| `first` | [`OneToOneExample_FirstRow`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_FirstRow) | Fetch the first row based on the filters and ordering. |

### oneToOneExamples: [`[OneToOneExample!]!`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample)

✨ List [`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample) objects in the table and return selected fields, optionally filtered by `where` conditions

| Field | Type | Description |
|---|---|---|
| `where` | [`OneToOneExample_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Filter) | Filter condition to narrow down the query results. |
| `orderBy` | [`[OneToOneExample_Order!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Order) | Order the query results by specific fields. |
| `offset` | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Number of rows to skip before starting to return the results. |
| `limit` | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Maximum number of rows to return (defaults to 100 rows). |
| `distinct` | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean) | Set to true to return distinct results. |
| `having` | [`OneToOneExample_Having`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Having) | Filter condition to apply to the groups of aggregate queries. |

### stringTable: [`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable)

✨ Look up a single [`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable) based on `id`, `key` or `first` and return selected fields (or `null` if not found).

| Field | Type | Description |
|---|---|---|
| `id` | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID) | The unique ID of the object. |
| `key` | [`StringTable_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Key) | The key used to identify the object. |
| `first` | [`StringTable_FirstRow`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_FirstRow) | Fetch the first row based on the filters and ordering. |

### stringTables: [`[StringTable!]!`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable)

✨ List [`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable) objects in the table and return selected fields, optionally filtered by `where` conditions

| Field | Type | Description |
|---|---|---|
| `where` | [`StringTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Filter) | Filter condition to narrow down the query results. |
| `orderBy` | [`[StringTable_Order!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Order) | Order the query results by specific fields. |
| `offset` | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Number of rows to skip before starting to return the results. |
| `limit` | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Maximum number of rows to return (defaults to 100 rows). |
| `distinct` | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean) | Set to true to return distinct results. |
| `having` | [`StringTable_Having`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Having) | Filter condition to apply to the groups of aggregate queries. |

## Built In

### __schema: [`__Schema!`](https://firebase.google.com/docs/reference/data-connect/gql/object#__Schema)

### __type: [`__Type`](https://firebase.google.com/docs/reference/data-connect/gql/object#__Type)

| Field | Type | Description |
|---|---|---|
| `name` | [`String!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) |   |