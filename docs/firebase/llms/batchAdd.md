# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchAdd.md.txt

# Method: projects.testers.batchAdd

- [HTTP request](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchAdd#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchAdd#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchAdd#body.request_body)
  - [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchAdd#body.request_body.SCHEMA_REPRESENTATION)
- [Response body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchAdd#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchAdd#body.BatchAddTestersResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchAdd#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchAdd#try-it)

Batch adds testers. This call adds testers for the specified emails if they don't already exist. Returns all testers specified in the request, including newly created and previously existing testers. This action is idempotent.

### HTTP request

`POST https://firebaseappdistribution.googleapis.com/v1/{project=projects/*}/testers:batchAdd`

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

|                                                                           Fields                                                                            ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `emails[]` | `string` Required. The email addresses of the tester resources to create. A maximum of 999 and a minimum of 1 tester can be created in a batch. |

### Response body

The Response message for `testers.batchAdd`.

If successful, the response body contains data with the following structure:

|                                                         JSON representation                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "testers": [ { object (https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers#Tester) } ] } ``` |

|                                                                                       Fields                                                                                       ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `testers[]` | `object (`[Tester](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers#Tester)`)` The testers which are created and/or already exist |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).