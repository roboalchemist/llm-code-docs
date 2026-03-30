# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/availableProjects/list.md.txt

# Method: availableProjects.list

Lists each [Google Cloud `Project`](https://cloud.google.com/resource-manager/reference/rest/v1/projects) that can have Firebase resources added and Firebase services enabled.

A Project will only be listed if:

- The caller has sufficient [Google IAM](https://cloud.google.com/iam) permissions to call `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/addFirebase#google.firebase.service.v1beta1.FirebaseProjectService.AddFirebase`.
- The Project is not already a `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`.
- The Project is not in an Organization which has policies that prevent Firebase resources from being added.

<br />

### HTTP request

`GET https://firebase.googleapis.com/v1beta1/availableProjects`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

| Parameters ||
|---|---|
| `pageToken` | `string` Token returned from a previous call to `availableProjects.list` indicating where in the set of Projects to resume listing. |
| `pageSize` | `integer` The maximum number of Projects to return in the response. The server may return fewer than this value at its discretion. If no value is specified (or too large a value is specified), the server will impose its own limit. This value cannot be negative. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "projectInfo": [ { object (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/availableProjects/list#ProjectInfo`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `projectInfo[]` | ``object (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/availableProjects/list#ProjectInfo`)`` The list of Google Cloud `Projects` which can have Firebase resources added to them. |
| `nextPageToken` | `string` If the result list is too large to fit in a single response, then a token is returned. If the string is empty, then this response is the last page of results. This token can be used in a subsequent calls to `availableProjects.list` to find the next group of Projects. Page tokens are short-lived and should not be persisted. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/cloud-platform.read-only`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/firebase.readonly`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## ProjectInfo

A reference to a Google Cloud `Project`.

| JSON representation |
|---|
| ``` { "project": string, "displayName": string, "locationId": string } ``` |

| Fields ||
|---|---|
| `project` | `string` The resource name of the Google Cloud `Project` to which Firebase resources can be added, in the format: `projects/PROJECT_IDENTIFIER` Refer to the `FirebaseProject` [`name`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> values. |
| `displayName` | `string` The user-assigned display name of the Google Cloud `Project`, for example: `My App`. |
| `locationId` | `string` **DEPRECATED** *Instead, use product-specific REST APIs to work with the location of each resource in a Project. This field may not be populated, especially for newly provisioned projects after October 30, 2024.* The ID of the Project's ["location for default Google Cloud resources"](https://firebase.google.com/docs/projects/locations#default-cloud-location). The location is one of the available [Google App Engine locations](https://cloud.google.com/about/locations#region). Not all Projects will have this field populated. If it is not populated, it means that the Project does not yet have a location for default Google Cloud resources. |