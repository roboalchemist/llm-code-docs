# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites/list.md.txt

# Method: projects.sites.list

Lists each Hosting `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites#Site` associated with the specified parent Firebase project.

### HTTP request

`GET https://firebasehosting.googleapis.com/v1beta1/{parent=projects/*}/sites`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The Firebase project for which to list sites, in the format: `projects/PROJECT_IDENTIFIER` Refer to the `Site` [`name`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects#Site.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> values. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`: - `firebasehosting.sites.list` |

### Query parameters

| Parameters ||
|---|---|
| `pageToken` | `string` Optional. A token from a previous call to `sites.list` that tells the server where to resume listing. |
| `pageSize` | `integer` Optional. The maximum number of sites to return. The service may return a lower number if fewer sites exist than this maximum number. If unspecified, defaults to 40. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "sites": [ { object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites#Site`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `sites[]` | ``object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites#Site`)`` A list of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites#Site` objects associated with the specified Firebase project. |
| `nextPageToken` | `string` The pagination token, if more results exist beyond the ones in this response. Include this token in your next call to `sites.list`. Page tokens are short-lived and should not be stored. |

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