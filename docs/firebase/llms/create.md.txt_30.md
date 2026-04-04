# Source: https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/create.md.txt

# Method: projects.locations.instances.create

Requests that a new `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance` be created. The state of a successfully created DatabaseInstance is `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#State.ENUM_VALUES.ACTIVE`.

Only available for projects on the Blaze plan. Projects can be upgraded using the Cloud Billing API <https://cloud.google.com/billing/reference/rest/v1/projects/updateBillingInfo>.

Note that it might take a few minutes for billing enablement state to propagate to Firebase systems.

### HTTP request

`POST https://firebasedatabase.googleapis.com/v1beta/{parent=projects/*/locations/*}/instances`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` The parent project for which to create a database instance, in the form: `projects/{project-number}/locations/{location-id}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`: - `firebasedatabase.instances.create` |

### Query parameters

| Parameters ||
|---|---|
| `databaseId` | `string` The globally unique identifier of the database instance. |
| `validateOnly` | `boolean` When set to true, the request will be validated but not submitted. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance`.

### Authorization Scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).