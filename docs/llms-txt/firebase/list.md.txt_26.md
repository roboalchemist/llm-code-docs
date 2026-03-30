# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.rollouts/list.md.txt

# Method: projects.locations.backends.rollouts.list

Lists rollouts for a backend.

### HTTP request

`GET https://firebaseapphosting.googleapis.com/v1/{parent=projects/*/locations/*/backends/*}/rollouts`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax. To know more about valid error responses that can be thrown by this HTTP request, please refer to the [service error catalog](https://firebase.google.com/docs/reference/apphosting/rest/v1/errors)

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The parent backend in the format: `projects/{project}/locations/{locationId}/backends/{backendId}`. |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` Optional. The maximum number of results to return. If not set, the service selects a default. |
| `pageToken` | `string` Optional. A page token received from the nextPageToken field in the response. Send that page token to receive the subsequent page. |
| `filter` | `string` Optional. A filter to narrow down results to a preferred subset. Learn more about filtering in Google's [AIP 160 standard](https://google.aip.dev/160). |
| `orderBy` | `string` Optional. Hint for how to order the results. Supported fields are `name` and `createTime`. To specify descending order, append a `desc` suffix. |
| `showDeleted` | `boolean` Optional. If true, the request returns soft-deleted resources that haven't been fully-deleted yet. |

### Request body

The request body must be empty.

### Response body

Message for response to list rollouts.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "rollouts": [ { object (`https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.rollouts#Rollout`) } ], "nextPageToken": string, "unreachable": [ string ] } ``` |

| Fields ||
|---|---|
| `rollouts[]` | ``object (`https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.rollouts#Rollout`)`` The list of rollouts. |
| `nextPageToken` | `string` A token identifying the next page of results the server should return. |
| `unreachable[]` | `string` Locations that could not be reached. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

- `firebaseapphosting.rollouts.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

See also Firebase App Hosting's [IAM Permissions](https://firebase.google.com/docs/projects/iam/permissions#app-hosting) and [Predefined IAM Roles](https://firebase.google.com/docs/projects/iam/roles-predefined-product).