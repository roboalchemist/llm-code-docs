# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/create.md.txt

# Method: sites.versions.create

Creates a new version for the specified site.

### HTTP request

`POST https://firebasehosting.googleapis.com/v1beta1/{parent=sites/*}/versions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The site in which to create the version, in the format: `sites/SITE_ID` |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions#Version`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions#Version`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.hosting`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).