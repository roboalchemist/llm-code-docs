# Source: https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates.md.txt

# REST Resource: projects.locations.templates

## Resource: PromptTemplate

Represents a Prompt Template resource.

| JSON representation |
|---|
| ``` { "name": string, "templateId": string, "displayName": string, "templateString": string, "createTime": string, "updateTime": string, "stateChangeTime": string, "etag": string, "locked": boolean } ``` |

| Fields ||
|---|---|
| `name` | `string` Identifier. The resource name of the PromptTemplate. Format: projects/{project}/locations/{location}/templates/{promptTemplate} |
| `templateId` | `string` Output only. Immutable. The unique ID of the PromptTemplate, which is the final component of the PromptTemplate's resource name. |
| `displayName` | `string` Optional. The display name of the PromptTemplate. |
| `templateString` | `string` Required. The DotPrompt raw template string. |
| `createTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Output only. Timestamp when the PromptTemplate was created. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `updateTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Output only. Timestamp when the PromptTemplate was last updated. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `stateChangeTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Output only. Timestamp when the PromptTemplate state was last changed. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `etag` | `string` Optional. The etag of the PromptTemplate. If this is provided with an update request, it must match the server's etag for the operation to succeed. |
| `locked` | `boolean` Output only. Indicates if the PromptTemplate has been locked for mutations. It is strongly recommended that PromptTemplates used in productgion Apps be locked to avoid accidental distruption to live apps. To modify a PromptTemplate that has been locked, a call to templates.modifyLock with lock=false is required first. |

| ## Methods ||
|---|---|
| ### `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/create` | Creates a new PromptTemplate. |
| ### `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/delete` | Deletes a PromptTemplate. |
| ### `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/get` | Gets a PromptTemplate. |
| ### `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/list` | Lists PromptTemplates. |
| ### `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/modifyLock` | Updates the Lock state on a PromptTemplate |
| ### `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/patch` | Updates a PromptTemplate. |
| ### `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/templateGenerateContent` | Generate content with multimodal inputs using a server-side prompt template. |
| ### `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/templatePredict` | Perform an online prediction using a server-side prompt template. |
| ### `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/templateStreamGenerateContent` | Generate content with multimodal inputs and streaming outputs using a server-side prompt template. |