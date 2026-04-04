# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchRemove.md.txt

# Method: projects.testers.batchRemove

- [HTTP request](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchRemove#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchRemove#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchRemove#body.request_body)
  - [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchRemove#body.request_body.SCHEMA_REPRESENTATION)
- [Response body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchRemove#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchRemove#body.BatchRemoveTestersResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchRemove#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchRemove#try-it)

Batch removes testers. If found, this call deletes testers for the specified emails. Returns all deleted testers.

### HTTP request

`POST https://firebaseappdistribution.googleapis.com/v1/{project=projects/*}/testers:batchRemove`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                         Parameters                                                                                                                                          ||
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `project` | `string` Required. The name of the project resource. Format: `projects/{projectNumber}` Authorization requires the following [IAM](https://firebase.google.com/docs/projects/iam/overview/) permission on the specified resource `project`: - `firebaseappdistro.testers.update` |

### Request body

The request body contains data with the following structure:

|       JSON representation        |
|----------------------------------|
| ``` { "emails": [ string ] } ``` |

|                                                                            Fields                                                                             ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `emails[]` | `string` Required. The email addresses of the tester resources to removed. A maximum of 999 and a minimum of 1 testers can be deleted in a batch. |

### Response body

The response message for `testers.batchRemove`

If successful, the response body contains data with the following structure:

|       JSON representation        |
|----------------------------------|
| ``` { "emails": [ string ] } ``` |

|                       Fields                       ||
|------------|----------------------------------------|
| `emails[]` | `string` List of deleted tester emails |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).