# Source: https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/list.md.txt

# Method: projects.locations.instances.list

Lists each `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance` associated with the specified parent project.

The list items are returned in no particular order, but will be a consistent view of the database instances when additional requests are made with a `pageToken`.

The resulting list contains instances in any `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#State`.

The list results may be stale by a few seconds.

Use `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/get#google.firebase.database.v1beta.RealtimeDatabaseService.GetDatabaseInstance` for consistent reads.

### HTTP request

`GET https://firebasedatabase.googleapis.com/v1beta/{parent=projects/*/locations/*}/instances`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` The parent project for which to list database instances, in the form: `projects/{project-number}/locations/{location-id}` To list across all locations, use a parent in the form: `projects/{project-number}/locations/-` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`: - `firebasedatabase.instances.list` |

### Query parameters

| Parameters ||
|---|---|
| `pageToken` | `string` Token returned from a previous call to `instances.list` indicating where in the set of database instances to resume listing. |
| `pageSize` | `integer` The maximum number of database instances to return in the response. The server may return fewer than this at its discretion. If no value is specified (or too large a value is specified), then the server will impose its own limit. |
| `showDeleted` | `boolean` Indicate that DatabaseInstances in the `DELETED` state should also be returned. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:
The response from the `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/list#google.firebase.database.v1beta.RealtimeDatabaseService.ListDatabaseInstances` method.

| JSON representation |
|---|
| ``` { "instances": [ { object (`https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `instances[]` | ``object (`https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance`)`` List of each `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance` that is in the parent Firebase project. |
| `nextPageToken` | `string` If the result list is too large to fit in a single response, then a token is returned. If the string is empty, then this response is the last page of results. This token can be used in a subsequent call to `instances.list` to find the next group of database instances. Page tokens are short-lived and should not be persisted. |

### Authorization Scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/cloud-platform.read-only`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/firebase.readonly`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).