# Source: https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces/list.md.txt

# Method: projects.namespaces.list

Lists all available namespaces for a given Firebase project.

The returned list currently includes "firebase" (for the client-side template) and "firebase-server" (for the server-side template).

### HTTP request

`GET https://firebaseremoteconfig.googleapis.com/v1/{parent=projects/*}/namespaces`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The parent project for which to list namespaces. Format: projects/{project} |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` Optional. The maximum number of items to return per page. If not specified, defaults to 100. |
| `pageToken` | `string` Optional. The token for the specific page to retrieve. |

### Request body

The request body must be empty.

### Response body

Response message for namespaces.list.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "namespaces": [ { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces#Namespace`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `namespaces[]` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces#Namespace`)`` The list of namespaces for the project. |
| `nextPageToken` | `string` Optional. The token for the specific page to retrieve. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.remoteconfig`
- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).