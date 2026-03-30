# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies/delete.md.txt

# Method: projects.services.resourcePolicies.delete

Deletes the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy` configuration.

### HTTP request

`DELETE https://firebaseappcheck.googleapis.com/v1beta/{name=projects/*/services/*/resourcePolicies/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The relative resource name of the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy` to delete, in the format: projects/{project_number}/services/{service_id}/resourcePolicies/{resource_policy_id} |

### Query parameters

| Parameters ||
|---|---|
| `etag` | `string` The checksum to be validated against the current `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy`, to ensure the client has an up-to-date value before proceeding. This checksum is computed by the server based on the values of fields in the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy` object, and can be obtained from the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy` object received from the last `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies/create#google.firebase.appcheck.v1beta.ConfigService.CreateResourcePolicy`, `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies/get#google.firebase.appcheck.v1beta.ConfigService.GetResourcePolicy`, `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies/list#google.firebase.appcheck.v1beta.ConfigService.ListResourcePolicies`, `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies/patch#google.firebase.appcheck.v1beta.ConfigService.UpdateResourcePolicy`, or `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies/batchUpdate#google.firebase.appcheck.v1beta.ConfigService.BatchUpdateResourcePolicies` call. This etag is strongly validated as defined by RFC 7232. |

### Request body

The request body must be empty.

### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).