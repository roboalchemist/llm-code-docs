# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies/create.md.txt

# Method: projects.services.resourcePolicies.create

Creates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy` configuration.

### HTTP request

`POST https://firebaseappcheck.googleapis.com/v1beta/{parent=projects/*/services/*}/resourcePolicies`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The relative resource name of the parent `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` in which the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy` will be created, in the format: projects/{project_number}/services/{service_id} Note that the `service_id` element must be a supported service ID. Currently, the following service IDs are supported: - `oauth2.googleapis.com` (Google Identity for iOS) |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).