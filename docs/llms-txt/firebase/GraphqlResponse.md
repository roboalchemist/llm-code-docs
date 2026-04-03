# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/GraphqlResponse.md.txt

# GraphqlResponse

The GraphQL response from Firebase Data Connect.

It strives to match the GraphQL over HTTP spec. Note: Firebase Data Connect always responds with `Content-Type:
application/json`. <https://github.com/graphql/graphql-over-http/blob/main/spec/GraphQLOverHTTP.md#body>

|                                                             JSON representation                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "data": { object }, "errors": [ { object (https://firebase.google.com/docs/reference/data-connect/rest/v1beta/GraphqlError) } ] } ``` |

|                                                                                                                                                                                                                                                                               Fields                                                                                                                                                                                                                                                                               ||
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `data`     | `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The result of the execution of the requested operation. If an error was raised before execution begins, the data entry should not be present in the result. (a request error: <https://spec.graphql.org/draft/#sec-Errors.Request-Errors>) If an error was raised during the execution that prevented a valid response, the data entry in the response should be null. (a field error: <https://spec.graphql.org/draft/#sec-Errors.Error-Result-Format>) |
| `errors[]` | `object (`[GraphqlError](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/GraphqlError)`)` Errors of this response. If the data entry in the response is not present, the errors entry must be present. It conforms to <https://spec.graphql.org/draft/#sec-Errors>.                                                                                                                                                                                                                                                                |