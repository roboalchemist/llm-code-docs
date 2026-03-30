# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors/patch.md.txt

# Method: projects.locations.services.connectors.patch

Updates the parameters of a single Connector, and creates a new ConnectorRevision with the updated Connector. The operations are validated against and must be compatible with the live schema. If the operations and schema are not compatible or if the schema is not present, this will result in an error.

### HTTP request

`PATCH https://firebasedataconnect.googleapis.com/v1beta/{connector.name=projects/*/locations/*/services/*/connectors/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `connector.name` | `string` Identifier. The relative resource name of the connector, in the format: projects/{project}/locations/{location}/services/{service}/connectors/{connector} |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` Optional. Field mask is used to specify the fields to be overwritten in the Connector resource by the update. The fields specified in the updateMask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`. |
| `requestId` | `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). |
| `allowMissing` | `boolean` Optional. If true and the Connector is not found, a new Connector will be created. In this case, `updateMask` is ignored. |
| `validateOnly` | `boolean` Optional. If set, validate the request and preview the Connector, but do not actually update it. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors#Connector`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.operations#Operation`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebasedataconnect.connectors.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).