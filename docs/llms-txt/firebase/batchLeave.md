# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/batchLeave.md.txt

# Method: projects.groups.batchLeave

- [HTTP request](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/batchLeave#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/batchLeave#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/batchLeave#body.request_body)
  - [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/batchLeave#body.request_body.SCHEMA_REPRESENTATION)
- [Response body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/batchLeave#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/batchLeave#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/batchLeave#try-it)

Batch removed members from a group. The testers will lose access to all releases that the groups have access to.

### HTTP request

`POST https://firebaseappdistribution.googleapis.com/v1/{group=projects/*/groups/*}:batchLeave`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                                                Parameters                                                                                                                                                                 ||
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `group` | `string` Required. The name of the group resource from which testers are removed. Format: `projects/{projectNumber}/groups/{group_alias}` Authorization requires the following [IAM](https://firebase.google.com/docs/projects/iam/overview/) permission on the specified resource `group`: - `firebaseappdistro.testers.update` |

### Request body

The request body contains data with the following structure:

|       JSON representation        |
|----------------------------------|
| ``` { "emails": [ string ] } ``` |

|                                                                                 Fields                                                                                 ||
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `emails[]` | `string` Required. The email addresses of the testers to be removed from the group. A maximum of 999 and a minimum of 1 testers can be removed in a batch. |

### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).