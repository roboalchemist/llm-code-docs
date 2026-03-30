# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations/get.md.txt

# Method: projects.locations.get

Gets information about a location.

### HTTP request

`GET https://firebasedataconnect.googleapis.com/v1beta/{name=projects/*/locations/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Resource name for the location. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations#Location`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebasedataconnect.locations.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).