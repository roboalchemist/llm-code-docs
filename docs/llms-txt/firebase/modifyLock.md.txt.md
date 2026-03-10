# Source: https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/modifyLock.md.txt

# Method: projects.locations.templates.modifyLock

Updates the Lock state on a PromptTemplate

### HTTP request

`POST https://firebasevertexai.googleapis.com/v1beta/{name=projects/*/locations/*/templates/*}:modifyLock`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The name of the PromptTemplate resource to update the lock on. Format: projects/{project}/locations/{location}/templates/{promptTemplate} |

### Request body

The request body contains data with the following structure:

| JSON representation |
|---|
| ``` { "locked": boolean } ``` |

| Fields ||
|---|---|
| `locked` | `boolean` Required. Updates the lock on a PromptTemplate to match this value. If True, mutations to the PromptTemplate will be blocked. |

### Response body

If successful, the response body is empty.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

- `firebasevertexai.promptTemplates.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).