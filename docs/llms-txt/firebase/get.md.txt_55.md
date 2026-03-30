# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains/get.md.txt

# Method: projects.sites.customDomains.get

Gets the specified `CustomDomain`.

### HTTP request

`GET https://firebasehosting.googleapis.com/v1beta1/{name=projects/*/sites/*/customDomains/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The name of the `CustomDomain` to get. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains#CustomDomain`.

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