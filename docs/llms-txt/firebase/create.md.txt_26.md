# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels/create.md.txt

# Method: sites.channels.create

Creates a new channel in the specified site.

### HTTP request

`POST https://firebasehosting.googleapis.com/v1beta1/{parent=sites/*}/channels`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The site in which to create this channel, in the format: `sites/SITE_ID` |

### Query parameters

| Parameters ||
|---|---|
| `channelId` | `string` Required. Immutable. A unique ID within the site that identifies the channel. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels#Channel`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels#Channel`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.hosting`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).