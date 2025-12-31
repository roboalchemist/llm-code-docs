# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services/batchUpdate.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/batchUpdate.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies/batchUpdate.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/batchUpdate.md.txt

Atomically updates the specified [ResourcePolicy](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy) configurations.

### HTTP request

`POST https://firebaseappcheck.googleapis.com/v1/{parent=projects/*/services/*}/resourcePolicies:batchUpdate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                  Parameters                                                                                                                   ||
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `parent` | `string` Required. The parent service name, in the format projects/{project_number}/services/{service_id} The parent collection in the `name` field of any resource being updated must match this field, or the entire batch fails. |

### Request body

The request body contains data with the following structure:

|                                                                                          JSON representation                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "updateMask": string, "requests": [ { object (https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/batchUpdate#UpdateResourcePolicyRequest) } ] } ``` |

|                                                                                                                                                                                                                                                                                                                                           Fields                                                                                                                                                                                                                                                                                                                                           ||
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `updateMask` | `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. A comma-separated list of names of fields in the [ResourcePolicy](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy) objects to update. Example: `enforcementMode`. If this field is present, the `updateMask` field in the [UpdateResourcePolicyRequest](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/batchUpdate#UpdateResourcePolicyRequest) messages must all match this field, or the entire batch fails and no updates will be committed. |
| `requests[]` | `object (`[UpdateResourcePolicyRequest](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/batchUpdate#UpdateResourcePolicyRequest)`)` Required. The request messages specifying the [ResourcePolicy](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy) objects to update. A maximum of 100 objects can be updated in a batch.                                                                                                                                                                                                                                      |

### Response body

Response message for the [resourcePolicies.batchUpdate](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/batchUpdate#google.firebase.appcheck.v1.ConfigService.BatchUpdateResourcePolicies) method.

If successful, the response body contains data with the following structure:

|                                                                      JSON representation                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "resourcePolicies": [ { object (https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy) } ] } ``` |

|                                                                                                                                                                     Fields                                                                                                                                                                      ||
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `resourcePolicies[]` | `object (`[ResourcePolicy](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy)`)` [ResourcePolicy](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy) objects after the updates have been applied. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).

## UpdateResourcePolicyRequest

Request message for the [resourcePolicies.patch](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/patch#google.firebase.appcheck.v1.ConfigService.UpdateResourcePolicy) method as well as an individual update message for the [resourcePolicies.batchUpdate](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/batchUpdate#google.firebase.appcheck.v1.ConfigService.BatchUpdateResourcePolicies) method.

|                                                                              JSON representation                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "resourcePolicy": { object (https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy) }, "updateMask": string } ``` |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                              Fields                                                                                                                                                                                                                                                                                                                                                                                                                                                               ||
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `resourcePolicy` | `object (`[ResourcePolicy](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy)`)` Required. The [ResourcePolicy](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy) to update. The [ResourcePolicy](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy)'s `name` field is used to identify the [ResourcePolicy](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy) to be updated, in the format: projects/{project_number}/services/{service_id}/resourcePolicies/{resource_policy_id} Note that the `service_id` element must be a supported service ID. Currently, the following service IDs are supported: - `oauth2.googleapis.com` (Google Identity for iOS) |
| `updateMask`     | `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. A comma-separated list of names of fields in the [ResourcePolicy](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy) to update. Example: `enforcementMode`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |