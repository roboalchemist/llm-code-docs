# Source: https://firebase.google.com/docs/firestore/reference/query-explain-report-reference.md.txt

<br />

The following values are returned as results to operations performed with[Firestore Query Explain](https://firebase.google.com/docs/firestore/query-explain).
| **Note:** Query Explain is designed for useful ad hoc analysis; its report format will evolve to maximize ease of reading and understanding, not suitability for machine processing. Some metrics are expected to change asCloud Firestoreevolves (i.e., metrics may be added, removed, or updated) and are not covered by the same deprecation policy as otherCloud FirestoreAPIs. The following tables indicate which portions of the data are subject to change.

## Plan records

|     Key      |                                           Type                                            |                    Field subject to change?                     |                                                                                  Description                                                                                   |
|--------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| indexes_used | List of[Generic Structs](https://protobuf.dev/reference/protobuf/google.protobuf/#struct) | Yes, the contents in the Struct response are subject to change. | List of indexes selected for this query. See[below](https://firebase.google.com/docs/firestore/reference/query-explain-report-reference#query-analyze-reference-indexes-used). |

### Indexes used

The contents of indexes used are subject to change asCloud Firestoreevolves.

|     Key     |  Type  |                                              Description                                               |
|-------------|--------|--------------------------------------------------------------------------------------------------------|
| query_scope | String | The scope at which a query is run. For example:`Collection`,`Collection Group`and`Includes Ancestors`. |
| properties  | String | The index fields in a format. For example:`(age ASC, __name__ ASC)`.                                   |

## Execution statistics

Aggregated execution statistics for the query.

|        Key         |                                       Type                                        |                    Field subject to change?                     |                                                                                        Description                                                                                         |
|--------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| results_returned   | long                                                                              | No                                                              | Total number of results returned, including documents, projections, aggregation results, keys.                                                                                             |
| execution_duration | [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)     | No                                                              | Total time to execute the query in the backend.                                                                                                                                            |
| read_operations    | long                                                                              | No                                                              | Total billable read operations.                                                                                                                                                            |
| debug_stats        | [Generic Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct) | Yes, the contents in the Struct response are subject to change. | Debugging statistics from the execution of the query. See[below](https://firebase.google.com/docs/firestore/reference/query-explain-report-reference#query-analyze-reference-debug-stats). |

### Debug statistics

The following results are helpful for debugging use cases and analysis of raw, optional statistics.

The contents of debug statistics are subject to change asCloud Firestoreevolves.

|          Key          |                                       Type                                        |                                                                  Description                                                                   |
|-----------------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| index_entries_scanned | String                                                                            | Total number of index entries inspected during the query.                                                                                      |
| documents_scanned     | String                                                                            | Total number of documents scanned during the query.                                                                                            |
| billing_details       | [Generic Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct) | Billing details including metrics like: "documents_billable", "index_entries_billable", "knn_vector_index_entries_billable", "min_query_cost". |