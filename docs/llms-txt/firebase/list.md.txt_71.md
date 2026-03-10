# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/list.md.txt

# Method: projects.webApps.list

Lists each `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp` associated with the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`.

The elements are returned in no particular order, but will be a consistent view of the Apps when additional requests are made with a `pageToken`.

### HTTP request

`GET https://firebase.googleapis.com/v1beta1/{parent=projects/*}/webApps`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` The resource name of the parent `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject` for which to list each associated `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp`, in the format: `projects/PROJECT_IDENTIFIER/webApps` Refer to the `FirebaseProject` [`name`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> values. |

### Query parameters

| Parameters ||
|---|---|
| `pageToken` | `string` Token returned from a previous call to `webApps.list` indicating where in the set of Apps to resume listing. |
| `pageSize` | `integer` The maximum number of Apps to return in the response. The server may return fewer than this value at its discretion. If no value is specified (or too large a value is specified), then the server will impose its own limit. |
| `showDeleted` | `boolean` Controls whether Apps in the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/State#ENUM_VALUES.DELETED` state should be returned in the response. If not specified, only `ACTIVE` Apps will be returned. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "apps": [ { object (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `apps[]` | ``object (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp`)`` List of each `WebApp` associated with the specified `FirebaseProject`. |
| `nextPageToken` | `string` If the result list is too large to fit in a single response, then a token is returned. If the string is empty, then this response is the last page of results. This token can be used in a subsequent call to `webApps.list` to find the next group of Apps. Page tokens are short-lived and should not be persisted. |

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