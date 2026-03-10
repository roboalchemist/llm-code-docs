# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services/create.md.txt

# Method: projects.locations.services.create

Creates a new Service in a given project and location.

### HTTP request

`POST https://firebasedataconnect.googleapis.com/v1beta/{parent=projects/*/locations/*}/services`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. Value of parent. |

### Query parameters

| Parameters ||
|---|---|
| `serviceId` | `string` Required. The ID to use for the service, which will become the final component of the service's resource name. |
| `requestId` | `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). |
| `validateOnly` | `boolean` Optional. If set, validate the request and preview the Service, but do not actually create it. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services#Service`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.operations#Operation`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

- `firebasedataconnect.services.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).