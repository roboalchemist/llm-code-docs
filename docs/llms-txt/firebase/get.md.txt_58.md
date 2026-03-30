# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.releases/get.md.txt

# Method: sites.releases.get

Gets the specified release for a site or channel.

When used to get a release for a site, this can get releases for both the default `live` channel and any active preview channels for the specified site.

### HTTP request

`GET https://firebasehosting.googleapis.com/v1beta1/{name=sites/*/releases/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The fully-qualified resource name for the Hosting release, in either of the following formats: - <br /> `sites/SITE_ID/channels/CHANNEL_ID/releases/RELEASE_ID` - `sites/SITE_ID/releases/RELEASE_ID` <br /> <br /> |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels.releases#Release`.

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