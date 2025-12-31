# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/ExplainOptions.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/ExplainOptions.md.txt

# ExplainOptions

Explain options for the query.

|      JSON representation       |
|--------------------------------|
| ``` { "analyze": boolean } ``` |

|                                                                                                                                                    Fields                                                                                                                                                     ||
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `analyze` | `boolean` Optional. Whether to execute this query. When false (the default), the query will be planned, returning only metrics from the planning stages. When true, the query will be planned and executed, returning the full query results along with both planning and execution stage metrics. |