# Source: https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/delete.md.txt

# Method: projects.rulesets.delete

- [HTTP request](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/delete#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/delete#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/delete#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/delete#body.response_body)
- [Authorization Scopes](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/delete#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/delete#try-it)

Delete a `Ruleset` by resource name.

If the `Ruleset` is referenced by a `Release` the operation will fail.

### HTTP request

`DELETE https://firebaserules.googleapis.com/v1/{name=projects/*/rulesets/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. Resource name for the ruleset to delete. Format: `projects/{project_id}/rulesets/{ruleset_id}` |

### Request body

The request body must be empty.

### Response body

If successful, the response body is empty.

### Authorization Scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).