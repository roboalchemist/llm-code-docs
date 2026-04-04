# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels/list.md.txt

# Method: sites.channels.list

Lists the channels for the specified site.

All sites have a default `live` channel.

### HTTP request

`GET https://firebasehosting.googleapis.com/v1beta1/{parent=sites/*}/channels`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The site for which to list channels, in the format: `sites/SITE_ID` |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` The maximum number of channels to return. The service may return a lower number if fewer channels exist than this maximum number. If unspecified, defaults to 10. The maximum value is 100; values above 100 will be coerced to 100. |
| `pageToken` | `string` A token from a previous call to `channels.list` that tells the server where to resume listing. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "channels": [ { object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels#Channel`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `channels[]` | ``object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels#Channel`)`` The list of channels. |
| `nextPageToken` | `string` The pagination token, if more results exist beyond the ones in this response. Include this token in your next call to `channels.list`. Page tokens are short-lived and should not be stored. |

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