# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/list.md.txt

# Method: projects.list

Lists each `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject` accessible to the caller.

The elements are returned in no particular order, but they will be a consistent view of the Projects when additional requests are made with a `pageToken`.

This method is eventually consistent with Project mutations, which means newly provisioned Projects and recent modifications to existing Projects might not be reflected in the set of Projects. The list will include only ACTIVE Projects.

Use `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/get#google.firebase.service.v1beta1.FirebaseProjectService.GetFirebaseProject` for consistent reads as well as for additional Project details.

### HTTP request

`GET https://firebase.googleapis.com/v1beta1/projects`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

| Parameters ||
|---|---|
| `pageToken` | `string` Token returned from a previous call to `projects.list` indicating where in the set of Projects to resume listing. |
| `pageSize` | `integer` The maximum number of Projects to return in the response. The server may return fewer than this at its discretion. If no value is specified (or too large a value is specified), the server will impose its own limit. This value cannot be negative. |
| `showDeleted` | `boolean` Optional. Controls whether Projects in the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#State.ENUM_VALUES.DELETED` state should be returned in the response. If not specified, only `ACTIVE` Projects will be returned. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "results": [ { object (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `results[]` | ``object (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`)`` One page of the list of Projects that are accessible to the caller. |
| `nextPageToken` | `string` If the result list is too large to fit in a single response, then a token is returned. If the string is empty, then this response is the last page of results. This token can be used in a subsequent calls to `projects.list` to find the next group of Projects. Page tokens are short-lived and should not be persisted. |

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