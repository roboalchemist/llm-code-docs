# Source: https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/delete.md.txt

# Method: projects.locations.instances.delete

Marks a `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance` to be deleted. The DatabaseInstance will be set to the `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#State.ENUM_VALUES.DELETED` state for 20 days, and will be purged within 30 days. The default database cannot be deleted. IDs for deleted database instances may never be recovered or re-used. The Database may only be deleted if it is already in a `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#State.ENUM_VALUES.DISABLED` state.

### HTTP request

`DELETE https://firebasedatabase.googleapis.com/v1beta/{name=projects/*/locations/*/instances/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` The fully qualified resource name of the database instance, in the form: `projects/{project-number}/locations/{location-id}/instances/{database-id}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`: - `firebasedatabase.instances.delete` |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance`.

### Authorization Scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).