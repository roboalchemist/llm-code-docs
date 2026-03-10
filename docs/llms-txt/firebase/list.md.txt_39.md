# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains.operations/list.md.txt

# Method: projects.sites.customDomains.operations.list

Lists operations that match the specified filter in the request.

### HTTP request

`GET https://firebasehosting.googleapis.com/v1beta1/{name=projects/*/sites/*/customDomains/*}/operations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

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

The response message for `Operations.ListOperations`.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "operations": [ { object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.operations#Operation`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `operations[]` | ``object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.operations#Operation`)`` A list of operations that matches the specified filter in the request. |
| `nextPageToken` | `string` The standard List next-page token. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.hosting.readonly`
- `
  https://www.googleapis.com/auth/firebase.hosting`
- `
  https://www.googleapis.com/auth/firebase.readonly`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/cloud-platform.read-only`
- `
  https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).