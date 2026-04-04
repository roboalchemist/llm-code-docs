# Source: https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/reenable.md.txt

# Method: projects.locations.instances.reenable

Enables a [DatabaseInstance](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance). The database must have been disabled previously using [instances.disable](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/disable#google.firebase.database.v1beta.RealtimeDatabaseService.DisableDatabaseInstance). The state of a successfully reenabled DatabaseInstance is [ACTIVE](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#State.ENUM_VALUES.ACTIVE).

### HTTP request

`POST https://firebasedatabase.googleapis.com/v1beta/{name=projects/*/locations/*/instances/*}:reenable`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                                                Parameters                                                                                                                                                                 ||
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name` | `string` The fully qualified resource name of the database instance, in the form: `projects/{project-number}/locations/{location-id}/instances/{database-id}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`: - `firebasedatabase.instances.reenable` |

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