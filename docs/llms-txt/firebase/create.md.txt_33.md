# Source: https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/create.md.txt

# Method: projects.rulesets.create

- [HTTP request](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/create#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/create#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/create#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/create#body.response_body)
- [Authorization Scopes](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/create#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/create#try-it)

Create a `Ruleset` from `Source`.

The `Ruleset` is given a unique generated name which is returned to the caller. `Source` containing syntactic or semantics errors will result in an error response indicating the first error encountered.

### HTTP request

`POST https://firebaserules.googleapis.com/v1/{name=projects/*}/rulesets`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. Resource name for Project which owns this `Ruleset`. Format: `projects/{project_id}` |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets#Ruleset`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets#Ruleset`.

### Authorization Scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).