# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/get.md.txt

# Method: sites.versions.get

Get the specified version that has been created for the specified site.

This can include versions that were created for the default `live` channel or for any active preview channels for the specified site.

### HTTP request

`GET https://firebasehosting.googleapis.com/v1beta1/{name=sites/*/versions/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The fully-qualified resource name for the version, in the format: `sites/SITE_ID/versions/VERSION_ID` |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions#Version`.

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