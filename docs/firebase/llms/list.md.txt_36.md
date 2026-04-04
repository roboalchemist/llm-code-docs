# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations/list.md.txt

# Method: projects.locations.list

Lists information about the supported locations for this service.

### HTTP request

`GET https://firebasedataconnect.googleapis.com/v1beta/{name=projects/*}/locations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` The resource that owns the locations collection, if applicable. |

### Query parameters

| Parameters ||
|---|---|
| `filter` | `string` A filter to narrow down results to a preferred subset. The filtering language accepts strings like `"displayName=tokyo"`, and is documented in more detail in [AIP-160](https://google.aip.dev/160). |
| `pageSize` | `integer` The maximum number of results to return. If not set, the service selects a default. |
| `pageToken` | `string` A page token received from the `nextPageToken` field in the response. Send that page token to receive the subsequent page. |

### Request body

The request body must be empty.

### Response body

The response message for `Locations.ListLocations`.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "locations": [ { object (`https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations#Location`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `locations[]` | ``object (`https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations#Location`)`` A list of locations that matches the specified filter in the request. |
| `nextPageToken` | `string` The standard List next-page token. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebasedataconnect.locations.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).