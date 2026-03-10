# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains/create.md.txt

# Method: projects.sites.customDomains.create

Creates a `CustomDomain`.

### HTTP request

`POST https://firebasehosting.googleapis.com/v1beta1/{parent=projects/*/sites/*}/customDomains`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The custom domain's parent, specifically a Firebase Hosting `Site`. |

### Query parameters

| Parameters ||
|---|---|
| `customDomainId` | `string` Required. The ID of the `CustomDomain`, which is the domain name you'd like to use with Firebase Hosting. |
| `validateOnly` | `boolean` If true, Hosting validates that it's possible to complete your request but doesn't actually create a new `CustomDomain`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains#CustomDomain`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.operations#Operation`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.hosting`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).