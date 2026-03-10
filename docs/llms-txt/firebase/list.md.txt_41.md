# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels.releases/list.md.txt

# Method: sites.channels.releases.list

Lists the releases that have been created for the specified site or channel.

When used to list releases for a site, this list includes releases for both the default `live` channel and any active preview channels for the specified site.

### HTTP request

`GET https://firebasehosting.googleapis.com/v1beta1/{parent=sites/*/channels/*}/releases`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The site or channel for which to list releases, in either of the following formats: - <br /> `sites/SITE_ID` - `sites/SITE_ID/channels/CHANNEL_ID` <br /> <br /> |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` The maximum number of releases to return. The service may return a lower number if fewer releases exist than this maximum number. If unspecified, defaults to 100. |
| `pageToken` | `string` A token from a previous call to `releases.list` or `channels.releases.list` that tells the server where to resume listing. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/ListReleasesResponse`.

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