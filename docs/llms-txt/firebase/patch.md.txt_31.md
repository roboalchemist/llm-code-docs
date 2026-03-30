# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains/patch.md.txt

# Method: projects.sites.customDomains.patch

Updates the specified `CustomDomain`.

### HTTP request

`PATCH https://firebasehosting.googleapis.com/v1beta1/{customDomain.name=projects/*/sites/*/customDomains/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `customDomain.name` | `string` Output only. The fully-qualified name of the `CustomDomain`. |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask` format)`` The set of field names from your `CustomDomain` that you want to update. A field will be overwritten if, and only if, it's in the mask. If you don't provide a mask, Hosting updates the entire `CustomDomain`. This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`. |
| `allowMissing` | `boolean` If true, Hosting creates the `CustomDomain` if it doesn't already exist. |
| `validateOnly` | `boolean` If true, Hosting validates that it's possible to complete your request but doesn't actually create or update the `CustomDomain`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains#CustomDomain`.

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