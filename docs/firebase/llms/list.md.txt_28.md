# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations/list.md.txt

# Method: projects.locations.list

Lists information about the supported locations for this service.

### HTTP request

`GET https://firebaseapphosting.googleapis.com/v1/{name=projects/*}/locations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax. To know more about valid error responses that can be thrown by this HTTP request, please refer to the [service error catalog](https://firebase.google.com/docs/reference/apphosting/rest/v1/errors)

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
| `extraLocationTypes[]` | `string` Optional. A list of extra location types that should be used as conditions for controlling the visibility of the locations. |

### Request body

The request body must be empty.

### Response body

The response message for `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations/list#google.cloud.location.Locations.ListLocations`.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "locations": [ { object (`https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations#Location`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `locations[]` | ``object (`https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations#Location`)`` A list of locations that matches the specified filter in the request. |
| `nextPageToken` | `string` The standard List next-page token. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebaseapphosting.locations.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

See also Firebase App Hosting's [IAM Permissions](https://firebase.google.com/docs/projects/iam/permissions#app-hosting) and [Predefined IAM Roles](https://firebase.google.com/docs/projects/iam/roles-predefined-product).