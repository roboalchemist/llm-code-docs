# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/patch.md.txt

# Method: projects.apps.releases.patch

- [HTTP request](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/patch#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/patch#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/patch#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/patch#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/patch#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/patch#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/patch#try-it)

Updates a release.

### HTTP request

`PATCH https://firebaseappdistribution.googleapis.com/v1/{release.name=projects/*/apps/*/releases/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `release.name` | `string` The name of the release resource. Format: `projects/{projectNumber}/apps/{appId}/releases/{releaseId}` Authorization requires the following [IAM](https://firebase.google.com/docs/projects/iam/overview/) permission on the Firebase project that owns the specified resource `name`: - `firebaseappdistro.releases.update` |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` The list of fields to update. This is a comma-separated list of fully qualified names of fields. Example: `"releaseNotes.text"`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases#Release`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases#Release`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).