# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds/disable.md.txt

# Source: https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/disable.md.txt

# Method: projects.locations.instances.disable

Disables a [DatabaseInstance](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance). The database can be re-enabled later using [instances.reenable](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/reenable#google.firebase.database.v1beta.RealtimeDatabaseService.ReenableDatabaseInstance). When a database is disabled, all reads and writes are denied, including view access in the Firebase console.

### HTTP request

`POST https://firebasedatabase.googleapis.com/v1beta/{name=projects/*/locations/*/instances/*}:disable`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                                                Parameters                                                                                                                                                                ||
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name` | `string` The fully qualified resource name of the database instance, in the form: `projects/{project-number}/locations/{location-id}/instances/{database-id}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`: - `firebasedatabase.instances.disable` |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of [DatabaseInstance](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance).

### Authorization Scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).