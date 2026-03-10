# Source: https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/list.md.txt

# Method: projects.releases.list

- [HTTP request](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/list#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/list#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/list#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/list#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/list#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/list#body.ListReleasesResponse.SCHEMA_REPRESENTATION)
- [Authorization Scopes](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/list#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/list#try-it)

List the `Release` values for a project. This list may optionally be filtered by `Release` name, `Ruleset` name, `TestSuite` name, or any combination thereof.

### HTTP request

`GET https://firebaserules.googleapis.com/v1/{name=projects/*}/releases`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. Resource name for the project. Format: `projects/{project_id}` |

### Query parameters

| Parameters ||
|---|---|
| `filter` | `string` `Release` filter. The list method supports filters with restrictions on the `Release.name`, and `Release.ruleset_name`. Example 1: A filter of 'name=prod\*' might return `Release`s with names within 'projects/foo' prefixed with 'prod': Name -\> Ruleset Name: - projects/foo/releases/prod -\> projects/foo/rulesets/uuid1234 - projects/foo/releases/prod/v1 -\> projects/foo/rulesets/uuid1234 - projects/foo/releases/prod/v2 -\> projects/foo/rulesets/uuid8888 Example 2: A filter of `name=prod* rulesetName=uuid1234` would return only `Release` instances for 'projects/foo' with names prefixed with 'prod' referring to the same `Ruleset` name of 'uuid1234': Name -\> Ruleset Name: - projects/foo/releases/prod -\> projects/foo/rulesets/1234 - projects/foo/releases/prod/v1 -\> projects/foo/rulesets/1234 In the examples, the filter parameters refer to the search filters are relative to the project. Fully qualified prefixed may also be used. |
| `pageSize` | `integer` Page size to load. Maximum of 100. Defaults to 10. Note: `pageSize` is just a hint and the service may choose to load fewer than `pageSize` results due to the size of the output. To traverse all of the releases, the caller should iterate until the `pageToken` on the response is empty. |
| `pageToken` | `string` Next page token for the next batch of `Release` instances. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:
The response for `https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/list#google.firebase.rules.v1.FirebaseRulesService.ListReleases`.

| JSON representation ||
|---|---|
| ``` { "releases": [ { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases#Release`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `releases[]` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases#Release`)`` List of `Release` instances. |
| `nextPageToken` | `string` The pagination token to retrieve the next page of results. If the value is empty, no further results remain. |

### Authorization Scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`
- `https://www.googleapis.com/auth/firebase.readonly`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).