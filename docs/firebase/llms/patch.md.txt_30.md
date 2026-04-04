# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/patch.md.txt

# Method: projects.webApps.patch

Updates the attributes of the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp`.

### HTTP request

`PATCH https://firebase.googleapis.com/v1beta1/{app.name=projects/*/webApps/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `app.name` | `string` The resource name of the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp`, in the format: `projects/PROJECT_IDENTIFIER/webApps/APP_ID` - <var translate="no">PROJECT_IDENTIFIER</var>: the parent Project's [`ProjectNumber`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its [`ProjectId`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.project_id). Learn more about using project identifiers in Google's [AIP 2510 standard](https://google.aip.dev/cloud/2510). Note that the value for <var translate="no">PROJECT_IDENTIFIER</var> in any response body will be the `ProjectId`. - <var translate="no">APP_ID</var>: the globally unique, Firebase-assigned identifier for the App (see [`appId`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp.FIELDS.app_id)). |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` Specifies which fields of the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp` to update. Note that the following fields are immutable: `name`, `appId`, and `projectId`. To update `state`, use any of the following endpoints: `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/remove#google.firebase.service.v1beta1.WebAppService.RemoveWebApp` or `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/undelete#google.firebase.service.v1beta1.WebAppService.UndeleteWebApp`. This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).