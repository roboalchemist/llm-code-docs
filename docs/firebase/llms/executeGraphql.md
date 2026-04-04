# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services/executeGraphql.md.txt

# Method: projects.locations.services.executeGraphql

Execute any GraphQL query and mutation against the Firebase Data Connect's generated GraphQL schema. Grants full read and write access to the connected data sources.

Note: Use introspection query to explore the generated GraphQL schema.

### HTTP request

`POST https://firebasedataconnect.googleapis.com/v1beta/{name=projects/*/locations/*/services/*}:executeGraphql`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                            Parameters                                                                             ||
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name` | `string` Required. The relative resource name of Firebase Data Connect service, in the format: projects/{project}/locations/{location}/services/{service} |

### Request body

The request body contains data with the following structure:

|                                                                                          JSON representation                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "query": string, "operationName": string, "variables": { object }, "extensions": { object (https://firebase.google.com/docs/reference/data-connect/rest/v1beta/GraphqlRequestExtensions) } } ``` |

|                                                                                                  Fields                                                                                                  ||
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `query`         | `string` Required. The GraphQL query document source.                                                                                                                                   |
| `operationName` | `string` Optional. The name of the GraphQL operation name. Required only if `query` contains multiple operations. See <https://graphql.org/learn/queries/#operation-name>.              |
| `variables`     | `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Values for GraphQL variables provided in this request.                          |
| `extensions`    | `object (`[GraphqlRequestExtensions](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/GraphqlRequestExtensions)`)` Optional. Additional GraphQL request information. |

### Response body

If successful, the response body contains an instance of [GraphqlResponse](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/GraphqlResponse).

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebasedataconnect.services.executeGraphql`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).