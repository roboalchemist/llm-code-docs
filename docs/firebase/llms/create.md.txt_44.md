# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors/create.md.txt

# Method: projects.locations.services.connectors.create

Creates a new Connector in a given project and location. The operations are validated against and must be compatible with the active schema. If the operations and schema are not compatible or if the schema is not present, this will result in an error.

### HTTP request

`POST https://firebasedataconnect.googleapis.com/v1beta/{parent=projects/*/locations/*/services/*}/connectors`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. Value for parent. |

### Query parameters

| Parameters ||
|---|---|
| `connectorId` | `string` Required. The ID to use for the connector, which will become the final component of the connector's resource name. |
| `requestId` | `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). |
| `validateOnly` | `boolean` Optional. If set, validate the request and preview the Connector, but do not actually create it. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors#Connector`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.operations#Operation`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

- `firebasedataconnect.connectors.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).