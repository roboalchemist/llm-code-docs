# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites/patch.md.txt

# Method: projects.sites.patch

Updates attributes of the specified Hosting `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites#Site`.

### HTTP request

`PATCH https://firebasehosting.googleapis.com/v1beta1/{site.name=projects/*/sites/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `site.name` | `string` Output only. The fully-qualified resource name of the Hosting site, in the format: `projects/PROJECT_IDENTIFIER/sites/SITE_ID` <var translate="no">PROJECT_IDENTIFIER</var>: the Firebase project's [`ProjectNumber`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its [`ProjectId`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.project_id). Learn more about using project identifiers in Google's [AIP 2510 standard](https://google.aip.dev/cloud/2510). |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask` format)`` A set of field names from your `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites#Site` that you want to update. This is a comma-separated list of fully qualified names of fields. Example: `"appId,labels"`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites#Site`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites#Site`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.hosting`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).