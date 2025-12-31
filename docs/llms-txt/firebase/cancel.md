# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.operations/cancel.md.txt

# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/cancel.md.txt

# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.operations/cancel.md.txt

# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.operations/cancel.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.operations/cancel.md.txt

# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/cancel.md.txt

# Method: projects.testMatrices.cancel

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/cancel#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/cancel#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/cancel#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/cancel#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/cancel#body.CancelTestMatrixResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/cancel#body.aspect)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/cancel#try-it)

Cancels unfinished test executions in a test matrix. This call returns immediately and cancellation proceeds asynchronously. If the matrix is already final, this operation will have no effect.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project
- INVALID_ARGUMENT - if the request is malformed
- NOT_FOUND - if the Test Matrix does not exist

### HTTP request

`POST https://testing.googleapis.com/v1/projects/{projectId}/testMatrices/{testMatrixId}:cancel`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                         Parameters                          ||
|----------------|---------------------------------------------|
| `projectId`    | `string` Cloud project that owns the test.  |
| `testMatrixId` | `string` Test matrix that will be canceled. |

### Request body

The request body must be empty.

### Response body

Response containing the current state of the specified test matrix.

If successful, the response body contains data with the following structure:

|                                                         JSON representation                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "testState": enum (https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices#TestState) } ``` |

|                                                                                                                                   Fields                                                                                                                                   ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `testState` | `enum (`[TestState](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices#TestState)`)` The current rolled-up state of the test matrix. If this state is already final, then the cancelation request will have no effect. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).