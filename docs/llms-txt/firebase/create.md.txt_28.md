# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites/create.md.txt

# Method: projects.sites.create

Creates a new Hosting `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites#Site` in the specified parent Firebase project.

Note that Hosting sites can take several minutes to propagate through Firebase systems.

### HTTP request

`POST https://firebasehosting.googleapis.com/v1beta1/{parent=projects/*}/sites`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The Firebase project in which to create a Hosting site, in the format: `projects/PROJECT_IDENTIFIER` Refer to the `Site` [`name`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects#Site.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> values. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`: - `firebasehosting.sites.create` |

### Query parameters

| Parameters ||
|---|---|
| `siteId` | `string` Required. Immutable. A globally unique identifier for the Hosting site. This identifier is used to construct the Firebase-provisioned subdomains for the site, so it must also be a valid domain name label. |
| `validateOnly` | `boolean` Optional. If set, validates that the siteId is available and that the request would succeed, returning the expected resulting site or error. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites#Site`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites#Site`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.hosting`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).