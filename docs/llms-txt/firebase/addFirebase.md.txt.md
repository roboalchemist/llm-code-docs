# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/addFirebase.md.txt

# Method: projects.addFirebase

Adds Firebase resources and enables Firebase services in the specified existing [Google Cloud `Project`](https://cloud.google.com/resource-manager/reference/rest/v1/projects).

Since a `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject` is actually also a Google Cloud `Project`, a `FirebaseProject` has the same underlying Google Cloud identifiers (`projectNumber` and `projectId`). This allows for easy interop with Google APIs.

The result of this call is an [`Operation`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations). Poll the `Operation` to track the provisioning process by calling `operations.get` until [`done`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Operation.FIELDS.done) is `true`. When `done` is `true`, the `Operation` has either succeeded or failed. If the `Operation` succeeded, its [`response`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Operation.FIELDS.response) is set to a `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`; if the `Operation` failed, its [`error`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Operation.FIELDS.error) is set to a `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Status`. The `Operation` is automatically deleted after completion, so there is no need to call `operations.delete`.

This method does not modify any billing account information on the underlying Google Cloud `Project`.

To call `projects.addFirebase`, a project member or service account must have the following permissions (the IAM roles of Editor and Owner contain these permissions): `firebase.projects.update`, `resourcemanager.projects.get`, `serviceusage.services.enable`, and `serviceusage.services.get`.

### HTTP request

`POST https://firebase.googleapis.com/v1beta1/{project=projects/*}:addFirebase`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `project` | `string` The resource name of the Google Cloud `Project` in which Firebase resources will be added and Firebase services enabled, in the format: `projects/PROJECT_IDENTIFIER` Refer to the `FirebaseProject` [`name`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> values. After calling `projects.addFirebase`, the unique Project identifiers ( [`projectNumber`](https://cloud.google.com/resource-manager/reference/rest/v1/projects#Project.FIELDS.project_number) and [`projectId`](https://cloud.google.com/resource-manager/reference/rest/v1/projects#Project.FIELDS.project_id)) of the underlying Google Cloud `Project` are also the identifiers of the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |

### Request body

The request body contains data with the following structure:

| JSON representation |
|---|
| ``` { "locationId": string } ``` |

| Fields ||
|---|---|
| `locationId` | `string` **DEPRECATED.** *Instead, use product-specific REST APIs to work with the location of each resource in a Project. This field may be ignored, especially for newly provisioned projects after October 30, 2024.* The ID of the Project's ["location for default Google Cloud resources"](https://firebase.google.com/docs/projects/locations#default-cloud-location), which are resources associated with Google App Engine. The location must be one of the available [Google App Engine locations](https://cloud.google.com/about/locations#region). |

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Operation`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).