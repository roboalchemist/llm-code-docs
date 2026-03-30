# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/list.md.txt

# Method: sites.versions.list

Lists the versions that have been created for the specified site.

This list includes versions for both the default `live` channel and any active preview channels for the specified site.

### HTTP request

`GET https://firebasehosting.googleapis.com/v1beta1/{parent=sites/*}/versions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The site or channel for which to list versions, in either of the following formats: - <br /> `sites/SITE_ID` - `sites/SITE_ID/channels/CHANNEL_ID` <br /> <br /> |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` The maximum number of versions to return. The service may return a lower number if fewer versions exist than this maximum number. If unspecified, defaults to 25. The maximum value is 100; values above 100 will be coerced to 100. |
| `pageToken` | `string` A token from a previous call to `versions.list` that tells the server where to resume listing. |
| `filter` | `string` A filter string used to return a subset of versions in the response. The currently supported fields for filtering are: `name`, `status`, and `createTime`. Learn more about filtering in Google's [AIP 160 standard](https://google.aip.dev/160). |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "versions": [ { object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions#Version`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `versions[]` | ``object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions#Version`)`` The list of versions, if any exist. |
| `nextPageToken` | `string` The pagination token, if more results exist beyond the ones in this response. Include this token in your next call to `versions.list`. Page tokens are short-lived and should not be stored. |

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