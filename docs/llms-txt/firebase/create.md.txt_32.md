# Source: https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/create.md.txt

# Method: projects.releases.create

- [HTTP request](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/create#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/create#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/create#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/create#body.response_body)
- [Authorization Scopes](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/create#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/create#try-it)

Create a `Release`.

Release names should reflect the developer's deployment practices. For example, the release name may include the environment name, application name, application version, or any other name meaningful to the developer. Once a `Release` refers to a `Ruleset`, the rules can be enforced by Firebase Rules-enabled services.

More than one `Release` may be 'live' concurrently. Consider the following three `Release` names for `projects/foo` and the `Ruleset` to which they refer.

Release Name -\> Ruleset Name:

- projects/foo/releases/prod -\> projects/foo/rulesets/uuid123
- projects/foo/releases/prod/beta -\> projects/foo/rulesets/uuid123
- projects/foo/releases/prod/v23 -\> projects/foo/rulesets/uuid456

The relationships reflect a `Ruleset` rollout in progress. The `prod` and `prod/beta` releases refer to the same `Ruleset`. However, `prod/v23` refers to a new `Ruleset`. The `Ruleset` reference for a `Release` may be updated using the `https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/patch#google.firebase.rules.v1.FirebaseRulesService.UpdateRelease` method.

### HTTP request

`POST https://firebaserules.googleapis.com/v1/{name=projects/*}/releases`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. Resource name for the project which owns this `Release`. Format: `projects/{project_id}` |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases#Release`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases#Release`.

### Authorization Scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).