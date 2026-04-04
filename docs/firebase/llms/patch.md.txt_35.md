# Source: https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/patch.md.txt

# Method: projects.releases.patch

- [HTTP request](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/patch#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/patch#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/patch#body.request_body)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/patch#body.request_body.SCHEMA_REPRESENTATION)
- [Response body](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/patch#body.response_body)
- [Authorization Scopes](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/patch#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/patch#try-it)

Update a `Release` via PATCH.

Only updates to `rulesetName` will be honored. `Release` rename is not supported. To create a `Release` use the `https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/create#google.firebase.rules.v1.FirebaseRulesService.CreateRelease` method.

### HTTP request

`PATCH https://firebaserules.googleapis.com/v1/{name=projects/*/releases/**}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. Resource name for the project which owns this `Release`. Format: `projects/{project_id}` |

### Request body

The request body contains data with the following structure:

| JSON representation ||
|---|---|
| ``` { "release": { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases#Release`) }, "updateMask": string } ``` |

| Fields ||
|---|---|
| `release` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases#Release`)`` `Release` to update. |
| `updateMask` | ``string (`https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask` format)`` Specifies which fields to update. This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`. |

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases#Release`.

### Authorization Scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).