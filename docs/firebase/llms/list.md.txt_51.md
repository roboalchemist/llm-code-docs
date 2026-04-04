# Source: https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/list.md.txt

# Method: projects.rulesets.list

- [HTTP request](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/list#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/list#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/list#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/list#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/list#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/list#body.ListRulesetsResponse.SCHEMA_REPRESENTATION)
- [Authorization Scopes](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/list#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/list#try-it)

List `Ruleset` metadata only and optionally filter the results by `Ruleset` name.

The full `Source` contents of a `Ruleset` may be retrieved with `https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/get#google.firebase.rules.v1.FirebaseRulesService.GetRuleset`.

### HTTP request

`GET https://firebaserules.googleapis.com/v1/{name=projects/*}/rulesets`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. Resource name for the project. Format: `projects/{project_id}` |

### Query parameters

| Parameters ||
|---|---|
| `filter` | `string` `Ruleset` filter. The list method supports filters with restrictions on `Ruleset.name`. Filters on `Ruleset.create_time` should use the `date` function which parses strings that conform to the RFC 3339 date/time specifications. Example: `createTime > date("2017-01-01T00:00:00Z") AND name=UUID-*` |
| `pageSize` | `integer` Page size to load. Maximum of 100. Defaults to 10. Note: `pageSize` is just a hint and the service may choose to load less than `pageSize` due to the size of the output. To traverse all of the releases, caller should iterate until the `pageToken` is empty. |
| `pageToken` | `string` Next page token for loading the next batch of `Ruleset` instances. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:
The response for `https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/list#google.firebase.rules.v1.FirebaseRulesService.ListRulesets`.

| JSON representation ||
|---|---|
| ``` { "rulesets": [ { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets#Ruleset`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `rulesets[]` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets#Ruleset`)`` List of `Ruleset` instances. |
| `nextPageToken` | `string` The pagination token to retrieve the next page of results. If the value is empty, no further results remain. |

### Authorization Scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`
- `https://www.googleapis.com/auth/firebase.readonly`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).