# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains/list.md.txt

# Method: projects.sites.customDomains.list

Lists each `CustomDomain` associated with the specified parent Hosting site.

Returns `CustomDomain`s in a consistent, but undefined, order to facilitate pagination.

### HTTP request

`GET https://firebasehosting.googleapis.com/v1beta1/{parent=projects/*/sites/*}/customDomains`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The Firebase Hosting `Site` with `CustomDomain` entities you'd like to list. |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` The max number of `CustomDomain` entities to return in a request. Defaults to 10. |
| `pageToken` | `string` A token from a previous call to `customDomains.list` that tells the server where to resume listing. |
| `showDeleted` | `boolean` If true, the request returns soft-deleted `CustomDomain`s that haven't been fully-deleted yet. To restore deleted `CustomDomain`s, make an `customDomains.undelete` request. |

### Request body

The request body must be empty.

### Response body

The response from `customDomains.list`.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "customDomains": [ { object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains#CustomDomain`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `customDomains[]` | ``object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains#CustomDomain`)`` A list of `CustomDomain` entities associated with the specified Firebase `Site`. |
| `nextPageToken` | `string` The pagination token, if more results exist beyond the ones in this response. Include this token in your next call to `customDomains.list`. Page tokens are short-lived and should not be stored. |

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