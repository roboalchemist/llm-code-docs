# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery.md.txt

Runs an aggregation query.

Rather than producing `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents#Document` results like `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runQuery#google.firestore.v1.Firestore.RunQuery`, this API allows running an aggregation to produce a series of `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery#AggregationResult` server-side.

High-Level Example:

    -- Return the number of documents in table given a filter.
    SELECT COUNT(*) FROM ( SELECT * FROM k where a = true );

### HTTP request

Choose a location:
<button value="global" default="">global</button> <button value="africa-south1">africa-south1</button> <button value="asia-east1">asia-east1</button> <button value="asia-east2">asia-east2</button> <button value="asia-northeast1">asia-northeast1</button> <button value="asia-northeast2">asia-northeast2</button> <button value="asia-northeast3">asia-northeast3</button> <button value="asia-south1">asia-south1</button> <button value="asia-south2">asia-south2</button> <button value="asia-southeast1">asia-southeast1</button> <button value="asia-southeast2">asia-southeast2</button> <button value="asia-southeast3">asia-southeast3</button> <button value="australia-southeast1">australia-southeast1</button> <button value="australia-southeast2">australia-southeast2</button> <button value="europe-central2">europe-central2</button> <button value="europe-north1">europe-north1</button> <button value="europe-north2">europe-north2</button> <button value="europe-southwest1">europe-southwest1</button> <button value="europe-west1">europe-west1</button> <button value="europe-west10">europe-west10</button> <button value="europe-west12">europe-west12</button> <button value="europe-west15">europe-west15</button> <button value="europe-west2">europe-west2</button> <button value="europe-west3">europe-west3</button> <button value="europe-west4">europe-west4</button> <button value="europe-west6">europe-west6</button> <button value="europe-west8">europe-west8</button> <button value="europe-west9">europe-west9</button> <button value="me-central1">me-central1</button> <button value="me-central2">me-central2</button> <button value="me-west1">me-west1</button> <button value="northamerica-northeast1">northamerica-northeast1</button> <button value="northamerica-northeast2">northamerica-northeast2</button> <button value="northamerica-south1">northamerica-south1</button> <button value="southamerica-east1">southamerica-east1</button> <button value="southamerica-west1">southamerica-west1</button> <button value="us-central1">us-central1</button> <button value="us-east1">us-east1</button> <button value="us-east4">us-east4</button> <button value="us-east5">us-east5</button> <button value="us-south1">us-south1</button> <button value="us-west1">us-west1</button> <button value="us-west2">us-west2</button> <button value="us-west3">us-west3</button> <button value="us-west4">us-west4</button> <button value="eu">eu</button> <button value="us">us</button>   
`POST https://firestore.googleapis.com/v1/{parent=projects/*/databases/*/documents}:runAggregationQuery`

<br />

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The parent resource name. In the format: `projects/{projectId}/databases/{databaseId}/documents` or `projects/{projectId}/databases/{databaseId}/documents/{document_path}`. For example: `projects/my-project/databases/my-database/documents` or `projects/my-project/databases/my-database/documents/chatrooms/my-chatroom` |

### Request body

The request body contains data with the following structure:

| JSON representation |
|---|
| ``` { "explainOptions": { object (`https://firebase.google.com/docs/firestore/reference/rest/v1/ExplainOptions`) }, // Union field `query_type` can be only one of the following: "structuredAggregationQuery": { object (`https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery#StructuredAggregationQuery`) } // End of list of possible types for union field `query_type`. // Union field `consistency_selector` can be only one of the following: "transaction": string, "newTransaction": { object (`https://firebase.google.com/docs/firestore/reference/rest/v1/TransactionOptions`) }, "readTime": string // End of list of possible types for union field `consistency_selector`. } ``` |

| Fields ||
|---|---|
| `explainOptions` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/v1/ExplainOptions`)`` Optional. Explain options for the query. If set, additional query statistics will be returned. If not, only query results will be returned. |
| Union field `query_type`. The query to run. `query_type` can be only one of the following: ||
| `structuredAggregationQuery` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery#StructuredAggregationQuery`)`` An aggregation query. |
| Union field `consistency_selector`. The consistency mode for the query, defaults to strong consistency. `consistency_selector` can be only one of the following: ||
| `transaction` | `string (https://developers.google.com/discovery/v1/type-format format)` Run the aggregation within an already active transaction. The value here is the opaque transaction ID to execute the query in. A base64-encoded string. |
| `newTransaction` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/v1/TransactionOptions`)`` Starts a new transaction as part of the query, defaulting to read-only. The new transaction ID will be returned as the first response in the stream. |
| `readTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Executes the query at the given timestamp. This must be a microsecond precision timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |

### Response body

The response for `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery#google.firestore.v1.Firestore.RunAggregationQuery`.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "result": { object (`https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery#AggregationResult`) }, "transaction": string, "readTime": string, "explainMetrics": { object (`https://firebase.google.com/docs/firestore/reference/rest/v1/ExplainMetrics`) } } ``` |

| Fields ||
|---|---|
| `result` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery#AggregationResult`)`` A single aggregation result. Not present when reporting partial progress. |
| `transaction` | `string (https://developers.google.com/discovery/v1/type-format format)` The transaction that was started as part of this request. Only present on the first response when the request requested to start a new transaction. A base64-encoded string. |
| `readTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` The time at which the aggregate result was computed. This is always monotonically increasing; in this case, the previous AggregationResult in the result stream are guaranteed not to have changed between their `readTime` and this one. If the query returns no results, a response with `readTime` and no `result` will be sent, and this represents the time at which the query was run. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `explainMetrics` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/v1/ExplainMetrics`)`` Query explain metrics. This is only present when the `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery#body.request_body.FIELDS.explain_options` is provided, and it is sent only once with the last response in the stream. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/datastore`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).

## StructuredAggregationQuery

Firestore query for running an aggregation over a `https://firebase.google.com/docs/firestore/reference/rest/v1/StructuredQuery`.

| JSON representation |
|---|
| ``` { "aggregations": [ { object (`https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery#Aggregation`) } ], // Union field `query_type` can be only one of the following: "structuredQuery": { object (`https://firebase.google.com/docs/firestore/reference/rest/v1/StructuredQuery`) } // End of list of possible types for union field `query_type`. } ``` |

| Fields ||
|---|---|
| `aggregations[]` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery#Aggregation`)`` Optional. Series of aggregations to apply over the results of the `structuredQuery`. Requires: - A minimum of one and maximum of five aggregations per query. |
| Union field `query_type`. The base query to aggregate over. `query_type` can be only one of the following: ||
| `structuredQuery` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/v1/StructuredQuery`)`` Nested structured query. |

## Aggregation

Defines an aggregation that produces a single result.

| JSON representation |
|---|
| ``` { "alias": string, // Union field `operator` can be only one of the following: "count": { object (`https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery#Count`) }, "sum": { object (`https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery#Sum`) }, "avg": { object (`https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery#Avg`) } // End of list of possible types for union field `operator`. } ``` |

| Fields ||
|---|---|
| `alias` | `string` Optional. Optional name of the field to store the result of the aggregation into. If not provided, Firestore will pick a default name following the format `field_<incremental_id++>`. For example: AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2), COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) OVER ( ... ); becomes: AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2) AS field_1, COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) AS field_2 OVER ( ... ); Requires: - Must be unique across all aggregation aliases. - Conform to `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents#Document.FIELDS.fields` limitations. |
| Union field `operator`. The type of aggregation to perform, required. `operator` can be only one of the following: ||
| `count` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery#Count`)`` Count aggregator. |
| `sum` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery#Sum`)`` Sum aggregator. |
| `avg` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery#Avg`)`` Average aggregator. |

## Count

Count of documents that match the query.

The `COUNT(*)` aggregation function operates on the entire document so it does not require a field reference.

| JSON representation |
|---|
| ``` { "upTo": string } ``` |

| Fields ||
|---|---|
| `upTo` | `string (https://developers.google.com/discovery/v1/type-format format)` Optional. Optional constraint on the maximum number of documents to count. This provides a way to set an upper bound on the number of documents to scan, limiting latency, and cost. Unspecified is interpreted as no bound. High-Level Example: AGGREGATE COUNT_UP_TO(1000) OVER ( SELECT * FROM k ); Requires: - Must be greater than zero when present. |

## Sum

Sum of the values of the requested field.

- Only numeric values will be aggregated. All non-numeric values including `NULL` are skipped.

- If the aggregated values contain `NaN`, returns `NaN`. Infinity math follows IEEE-754 standards.

- If the aggregated value set is empty, returns 0.

- Returns a 64-bit integer if all aggregated numbers are integers and the sum result does not overflow. Otherwise, the result is returned as a double. Note that even if all the aggregated values are integers, the result is returned as a double if it cannot fit within a 64-bit signed integer. When this occurs, the returned value will lose precision.

- When underflow occurs, floating-point aggregation is non-deterministic. This means that running the same query repeatedly without any changes to the underlying values could produce slightly different results each time. In those cases, values should be stored as integers over floating-point numbers.

| JSON representation |
|---|
| ``` { "field": { object (`https://firebase.google.com/docs/firestore/reference/rest/v1/FieldReference`) } } ``` |

| Fields ||
|---|---|
| `field` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/v1/FieldReference`)`` The field to aggregate on. |

## Avg

Average of the values of the requested field.

- Only numeric values will be aggregated. All non-numeric values including `NULL` are skipped.

- If the aggregated values contain `NaN`, returns `NaN`. Infinity math follows IEEE-754 standards.

- If the aggregated value set is empty, returns `NULL`.

- Always returns the result as a double.

| JSON representation |
|---|
| ``` { "field": { object (`https://firebase.google.com/docs/firestore/reference/rest/v1/FieldReference`) } } ``` |

| Fields ||
|---|---|
| `field` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/v1/FieldReference`)`` The field to aggregate on. |

## AggregationResult

The result of a single bucket from a Firestore aggregation query.

The keys of `aggregateFields` are the same for all results in an aggregation query, unlike document queries which can have different fields present for each result.

| JSON representation |
|---|
| ``` { "aggregateFields": { string: { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Value`) }, ... } } ``` |

| Fields ||
|---|---|
| `aggregateFields` | ``map (key: string, value: object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Value`))`` The result of the aggregation functions, ex: `COUNT(*) AS total_docs`. The key is the `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/runAggregationQuery#Aggregation.FIELDS.alias` assigned to the aggregation function on input and the size of this map equals the number of aggregation functions in the query. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |