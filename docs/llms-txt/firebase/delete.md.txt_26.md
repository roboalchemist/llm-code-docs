# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains/delete.md.txt

# Method: projects.sites.customDomains.delete

Deletes the specified `CustomDomain`.

### HTTP request

`DELETE https://firebasehosting.googleapis.com/v1beta1/{name=projects/*/sites/*/customDomains/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The name of the `CustomDomain` to delete. |

### Query parameters

| Parameters ||
|---|---|
| `allowMissing` | `boolean` If true, the request succeeds even if the `CustomDomain` doesn't exist. |
| `validateOnly` | `boolean` If true, Hosting validates that it's possible to complete your request but doesn't actually delete the `CustomDomain`. |
| `etag` | `string` A tag that represents the state of the `CustomDomain` as you know it. If present, the supplied tag must match the current value on your `CustomDomain`, or the request fails. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.operations#Operation`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.hosting`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).