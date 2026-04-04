# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels.releases/create.md.txt

# Method: sites.channels.releases.create

Creates a new release, which makes the content of the specified version actively display on the appropriate URL(s).

### HTTP request

`POST https://firebasehosting.googleapis.com/v1beta1/{parent=sites/*/channels/*}/releases`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The site or channel to which the release belongs, in either of the following formats: - <br /> `sites/SITE_ID` - `sites/SITE_ID/channels/CHANNEL_ID` |

### Query parameters

| Parameters ||
|---|---|
| `versionName` | `string` The unique identifier for a version, in the format: `sites/SITE_ID/versions/VERSION_ID` The <var translate="no">SITE_ID</var> in this version identifier must match the <var translate="no">SITE_ID</var> in the `parent` parameter. This query parameter must be empty if the `type` field in the request body is `SITE_DISABLE`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels.releases#Release`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels.releases#Release`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.hosting`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).