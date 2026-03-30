# Source: https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/patch.md.txt

# Method: projects.locations.templates.patch

Updates a PromptTemplate.

### HTTP request

`PATCH https://firebasevertexai.googleapis.com/v1beta/{promptTemplate.name=projects/*/locations/*/templates/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `promptTemplate.name` | `string` Identifier. The resource name of the PromptTemplate. Format: projects/{project}/locations/{location}/templates/{promptTemplate} |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` Optional. The list of fields to update. This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`. |
| `validateOnly` | `boolean` Optional. If set to true, the request will be validated but not executed. |
| `allowMissing` | `boolean` Optional. If set to true and the PromptTemplate does not already exist, it will be created. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates#PromptTemplate`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates#PromptTemplate`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebasevertexai.promptTemplates.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).