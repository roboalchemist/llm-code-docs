# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/batchDelete.md.txt

# Method: projects.apps.releases.batchDelete

- [HTTP request](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/batchDelete#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/batchDelete#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/batchDelete#body.request_body)
  - [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/batchDelete#body.request_body.SCHEMA_REPRESENTATION)
- [Response body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/batchDelete#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/batchDelete#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/batchDelete#try-it)

Deletes releases. A maximum of 100 releases can be deleted per request.

### HTTP request

`POST https://firebaseappdistribution.googleapis.com/v1/{parent=projects/*/apps/*}/releases:batchDelete`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                                                                    Parameters                                                                                                                                                                                    ||
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `parent` | `string` Required. The name of the app resource, which is the parent of the release resources. Format: `projects/{projectNumber}/apps/{appId}` Authorization requires the following [IAM](https://firebase.google.com/docs/projects/iam/overview/) permission on the Firebase project that owns the specified resource `parent`: - `firebaseappdistro.releases.update` |

### Request body

The request body contains data with the following structure:

|       JSON representation       |
|---------------------------------|
| ``` { "names": [ string ] } ``` |

|                                                                                                 Fields                                                                                                 ||
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `names[]` | `string` Required. The names of the release resources to delete. Format: `projects/{projectNumber}/apps/{appId}/releases/{releaseId}` A maximum of 100 releases can be deleted per request. |

### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).