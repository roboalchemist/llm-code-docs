# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/patch.md.txt

# Method: projects.testers.patch

- [HTTP request](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/patch#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/patch#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/patch#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/patch#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/patch#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/patch#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/patch#try-it)

Update a tester. If the testers joins a group they gain access to all releases that the group has access to.

### HTTP request

`PATCH https://firebaseappdistribution.googleapis.com/v1/{tester.name=projects/*/testers/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `tester.name` | `string` The name of the tester resource. Format: `projects/{projectNumber}/testers/{email_address}` |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` The list of fields to update. This is a comma-separated list of fully qualified names of fields. Example: `"displayName,groups"`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers#Tester`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers#Tester`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).