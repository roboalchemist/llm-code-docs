# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors/executeMutation.md.txt

# Method: projects.locations.services.connectors.executeMutation

Execute a predefined mutation in a Connector.

### HTTP request

`POST https://firebasedataconnect.googleapis.com/v1beta/{name=projects/*/locations/*/services/*/connectors/*}:executeMutation`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                           Parameters                                                                                            ||
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name` | `string` Required. The resource name of the connector to find the predefined mutation, in the format: projects/{project}/locations/{location}/services/{service}/connectors/{connector} |

### Request body

The request body contains data with the following structure:

|                     JSON representation                      |
|--------------------------------------------------------------|
| ``` { "operationName": string, "variables": { object } } ``` |

|                                                                                            Fields                                                                                             ||
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `operationName` | `string` Required. The name of the GraphQL operation name. Required because all Connector operations must be named. See <https://graphql.org/learn/queries/#operation-name>. |
| `variables`     | `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Values for GraphQL variables provided in this request.               |

### Response body

The connectors.executeMutation response from Firebase Data Connect.

If successful, the response body contains data with the following structure:

|                                                             JSON representation                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "data": { object }, "errors": [ { object (https://firebase.google.com/docs/reference/data-connect/rest/v1beta/GraphqlError) } ] } ``` |

|                                                                           Fields                                                                           ||
|------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `data`     | `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The result of executing the requested operation. |
| `errors[]` | `object (`[GraphqlError](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/GraphqlError)`)` Errors of this response.         |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).