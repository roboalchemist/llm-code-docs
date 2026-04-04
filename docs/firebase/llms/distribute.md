# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/distribute.md.txt

# Method: projects.apps.releases.distribute

- [HTTP request](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/distribute#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/distribute#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/distribute#body.request_body)
  - [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/distribute#body.request_body.SCHEMA_REPRESENTATION)
- [Response body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/distribute#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/distribute#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/distribute#try-it)

Distributes a release to testers. This call does the following:

1. Creates testers for the specified emails, if none exist.
2. Adds the testers and groups to the release.
3. Sends new testers an invitation email.
4. Sends existing testers a new release email.

The request will fail with a `INVALID_ARGUMENT` if it contains a group that doesn't exist.

### HTTP request

`POST https://firebaseappdistribution.googleapis.com/v1/{name=projects/*/apps/*/releases/*}:distribute`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                                                              Parameters                                                                                                                                                                               ||
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name` | `string` Required. The name of the release resource to distribute. Format: `projects/{projectNumber}/apps/{appId}/releases/{releaseId}` Authorization requires the following [IAM](https://firebase.google.com/docs/projects/iam/overview/) permission on the Firebase project that owns the specified resource `name`: - `firebaseappdistro.releases.update` |

### Request body

The request body contains data with the following structure:

|                        JSON representation                         |
|--------------------------------------------------------------------|
| ``` { "testerEmails": [ string ], "groupAliases": [ string ] } ``` |

|                                                                                               Fields                                                                                                ||
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `tester``Emails[]` | `string` A list of tester email addresses to be given access to this release. A combined maximum of 999 `testerEmails` and `groupAliases` can be specified in a single request. |
| `group``Aliases[]` | `string` A list of group aliases (IDs) to be given access to this release. A combined maximum of 999 `testerEmails` and `groupAliases` can be specified in a single request.    |

### Response body

If successful, the response body is empty.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).