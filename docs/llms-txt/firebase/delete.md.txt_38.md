# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors/delete.md.txt

# Method: projects.locations.services.connectors.delete

Deletes a single Connector.

### HTTP request

`DELETE https://firebasedataconnect.googleapis.com/v1beta/{name=projects/*/locations/*/services/*/connectors/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The name of the connector to delete, in the format: projects/{project}/locations/{location}/services/{service}/connectors/{connector} |

### Query parameters

| Parameters ||
|---|---|
| `force` | `boolean` Optional. If set to true, any child resources (i.e. ConnectorRevisions) will also be deleted. Otherwise, the request will only work if the Connector has no child resources. |
| `etag` | `string` Optional. The etag of the Connector. If this is provided, it must match the server's etag. |
| `requestId` | `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). |
| `allowMissing` | `boolean` Optional. If true and the Connector is not found, the request will succeed but no action will be taken on the server. |
| `validateOnly` | `boolean` Optional. If set, validate the request and preview the Connector, but do not actually delete it. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.operations#Operation`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebasedataconnect.connectors.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).