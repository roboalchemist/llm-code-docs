# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/patch.md.txt

# Method: projects.services.resourcePolicies.patch

Updates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy` configuration.

### HTTP request

`PATCH https://firebaseappcheck.googleapis.com/v1/{resourcePolicy.name=projects/*/services/*/resourcePolicies/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `resourcePolicy.name` | `string` Required. Identifier. The relative name of the resource policy object, in the format: projects/{project_number}/services/{service_id}/resourcePolicies/{resource_policy_id} Note that the `service_id` element must be a supported service ID. Currently, the following service IDs are supported: - `oauth2.googleapis.com` (Google Identity for iOS) `resource_policy_id` is a system-generated UID. |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` Required. A comma-separated list of names of fields in the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy` to update. Example: `enforcementMode`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).