# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies/get.md.txt

# Method: projects.services.resourcePolicies.get

Gets the requested `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy` configuration.

### HTTP request

`GET https://firebaseappcheck.googleapis.com/v1beta/{name=projects/*/services/*/resourcePolicies/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The relative resource name of the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy` to retrieve, in the format: projects/{project_number}/services/{service_id}/resourcePolicies/{resource_policy_id} Note that the `service_id` element must be a supported service ID. Currently, the following service IDs are supported: - `oauth2.googleapis.com` (Google Identity for iOS) |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).