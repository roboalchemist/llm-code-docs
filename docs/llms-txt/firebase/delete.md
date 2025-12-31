# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites/delete.md.txt

# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains/delete.md.txt

# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas/delete.md.txt

# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors/delete.md.txt

# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.operations/delete.md.txt

# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.domains/delete.md.txt

# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.builds/delete.md.txt

# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends/delete.md.txt

# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.builds/delete.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/delete.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/delete.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens/delete.md.txt

# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/delete.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta2/projects.databases.collectionGroups.indexes/delete.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/delete.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.userCreds/delete.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents/delete.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.backupSchedules/delete.md.txt

# Source: https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/delete.md.txt

# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/delete.md.txt

# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels/delete.md.txt

# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha/delete.md.txt

# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services/delete.md.txt

# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.operations/delete.md.txt

# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends/delete.md.txt

# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.operations/delete.md.txt

# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.domains/delete.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies/delete.md.txt

# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/delete.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.indexes/delete.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.locations.backups/delete.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/delete.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.operations/delete.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.collectionGroups.indexes/delete.md.txt

# Source: https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/delete.md.txt

# Source: https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/delete.md.txt

# Source: https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/delete.md.txt

# Source: https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/delete.md.txt

# Method: projects.locations.instances.delete

Marks a [DatabaseInstance](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance) to be deleted. The DatabaseInstance will be set to the [DELETED](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#State.ENUM_VALUES.DELETED) state for 20 days, and will be purged within 30 days. The default database cannot be deleted. IDs for deleted database instances may never be recovered or re-used. The Database may only be deleted if it is already in a [DISABLED](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#State.ENUM_VALUES.DISABLED) state.

### HTTP request

`DELETE https://firebasedatabase.googleapis.com/v1beta/{name=projects/*/locations/*/instances/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                                               Parameters                                                                                                                                                                ||
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name` | `string` The fully qualified resource name of the database instance, in the form: `projects/{project-number}/locations/{location-id}/instances/{database-id}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`: - `firebasedatabase.instances.delete` |

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