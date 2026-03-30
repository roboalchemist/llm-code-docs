# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/patch.md.txt

# Method: projects.patch

Updates the attributes of the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`.

All [query parameters](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/patch#query-parameters) are required.

### HTTP request

`PATCH https://firebase.googleapis.com/v1beta1/{project.name=projects/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `project.name` | `string` The resource name of the Project, in the format: `projects/PROJECT_IDENTIFIER` <var translate="no">PROJECT_IDENTIFIER</var>: the Project's [`ProjectNumber`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its [`ProjectId`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.project_id). Learn more about using project identifiers in Google's [AIP 2510 standard](https://google.aip.dev/cloud/2510). Note that the value for <var translate="no">PROJECT_IDENTIFIER</var> in any response body will be the `ProjectId`. |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` Specifies which fields of the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject` to update. Note that the following fields are immutable: `name`, `projectId`, and `projectNumber`. To update `state`, use any of the following Google Cloud endpoints: [`projects.delete`](https://cloud.google.com/resource-manager/reference/rest/v1/projects/delete) or [`projects.undelete`](https://cloud.google.com/resource-manager/reference/rest/v1/projects/undelete) This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).