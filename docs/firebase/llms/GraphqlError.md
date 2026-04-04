# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/GraphqlError.md.txt

# GraphqlError conforms to the GraphQL error spec. <https://spec.graphql.org/draft/#sec-Errors>

Firebase Data Connect API surfaces `GraphqlError` in various APIs: - Upon compile error, `UpdateSchema` and `UpdateConnector` return Code.Invalid_Argument with a list of `GraphqlError` in error details. - Upon query compile error, `ExecuteGraphql` and `ExecuteGraphqlRead` return Code.OK with a list of `GraphqlError` in response body. - Upon query execution error, `ExecuteGraphql`, `ExecuteGraphqlRead`, `ExecuteMutation` and `ExecuteQuery` all return Code.OK with a list of `GraphqlError` in response body.

|                                                                                                                                               JSON representation                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "message": string, "locations": [ { object (https://firebase.google.com/docs/reference/data-connect/rest/v1beta/GraphqlError#SourceLocation) } ], "path": array, "extensions": { object (https://firebase.google.com/docs/reference/data-connect/rest/v1beta/GraphqlError#GraphqlErrorExtensions) } } ``` |

|                                                                                                                                                                                                                                                                                Fields                                                                                                                                                                                                                                                                                ||
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `message`     | `string` The detailed error message. The message should help developer understand the underlying problem without leaking internal data.                                                                                                                                                                                                                                                                                                                                                                                                               |
| `locations[]` | `object (`[SourceLocation](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/GraphqlError#SourceLocation)`)` The source locations where the error occurred. Locations should help developers and toolings identify the source of error quickly. Included in admin endpoints (`ExecuteGraphql`, `ExecuteGraphqlRead`, `UpdateSchema` and `UpdateConnector`) to reference the provided GraphQL GQL document. Omitted in `ExecuteMutation` and `ExecuteQuery` since the caller shouldn't have access access the underlying GQL source. |
| `path`        | `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` The result field which could not be populated due to error. Clients can use path to identify whether a null result is intentional or caused by a runtime error. It should be a list of string or index from the root of GraphQL query document.                                                                                                                                                                                                   |
| `extensions`  | `object (`[GraphqlErrorExtensions](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/GraphqlError#GraphqlErrorExtensions)`)` Additional error information.                                                                                                                                                                                                                                                                                                                                                                          |

## SourceLocation

SourceLocation references a location in a GraphQL source.

|              JSON representation               |
|------------------------------------------------|
| ``` { "line": integer, "column": integer } ``` |

|                      Fields                      ||
|----------|----------------------------------------|
| `line`   | `integer` Line number starting at 1.   |
| `column` | `integer` Column number starting at 1. |

## GraphqlErrorExtensions

GraphqlErrorExtensions contains additional information of `GraphqlError`.

|    JSON representation     |
|----------------------------|
| ``` { "file": string } ``` |

|                                                                                     Fields                                                                                      ||
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `file` | `string` The source file name where the error occurred. Included only for `UpdateSchema` and `UpdateConnector`, it corresponds to `File.path` of the provided `Source`. |