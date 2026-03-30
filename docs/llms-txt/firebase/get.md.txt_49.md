# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas/get.md.txt

# Method: projects.locations.services.schemas.get

Gets details of a single Schema.

### HTTP request

`GET https://firebasedataconnect.googleapis.com/v1beta/{name=projects/*/locations/*/services/*/schemas/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The name of the schema to retrieve, in the format: projects/{project}/locations/{location}/services/{service}/schemas/{schema} |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas#Schema`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebasedataconnect.schemas.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).