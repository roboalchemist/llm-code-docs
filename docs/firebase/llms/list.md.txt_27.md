# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.operations/list.md.txt

# Method: projects.locations.operations.list

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

### HTTP request

`GET https://firebaseapphosting.googleapis.com/v1/{name=projects/*/locations/*}/operations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax. To know more about valid error responses that can be thrown by this HTTP request, please refer to the [service error catalog](https://firebase.google.com/docs/reference/apphosting/rest/v1/errors)

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` The name of the operation's parent resource. |

### Query parameters

| Parameters ||
|---|---|
| `filter` | `string` The standard list filter. |
| `pageSize` | `integer` The standard list page size. |
| `pageToken` | `string` The standard list page token. |

### Request body

The request body must be empty.

### Response body

The response message for `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.operations/list#google.longrunning.Operations.ListOperations`.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "operations": [ { object (`https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.operations#Operation`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `operations[]` | ``object (`https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.operations#Operation`)`` A list of operations that matches the specified filter in the request. |
| `nextPageToken` | `string` The standard List next-page token. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebaseapphosting.operations.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

See also Firebase App Hosting's [IAM Permissions](https://firebase.google.com/docs/projects/iam/permissions#app-hosting) and [Predefined IAM Roles](https://firebase.google.com/docs/projects/iam/roles-predefined-product).