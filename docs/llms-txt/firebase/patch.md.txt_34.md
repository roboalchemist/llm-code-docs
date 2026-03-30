# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/patch.md.txt

# Method: sites.versions.patch

Updates the specified metadata for the specified version.

This method will fail with `FAILED_PRECONDITION` in the event of an invalid state transition. The supported [state](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions#versionstatus) transitions for a version are from `CREATED` to `FINALIZED`.

Use [`versions.delete`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/delete) to set the status of a version to `DELETED`.

### HTTP request

`PATCH https://firebasehosting.googleapis.com/v1beta1/{version.name=sites/*/versions/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `version.name` | `string` The fully-qualified resource name for the version, in the format: `sites/SITE_ID/versions/VERSION_ID` This name is provided in the response body when you call [`versions.create`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/sites.versions/create). |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask` format)`` A set of field names from your [version](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions) that you want to update. A field will be overwritten if, and only if, it's in the mask. If a mask is not provided then a default mask of only [`status`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions#Version.FIELDS.status) will be used. This is a comma-separated list of fully qualified names of fields. Example: `"config,status"`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions#Version`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions#Version`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.hosting`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).