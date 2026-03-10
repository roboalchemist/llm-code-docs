# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/get.md.txt

# Method: projects.testMatrices.get

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/get#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/get#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/get#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/get#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/get#body.aspect)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/get#try-it)

Checks the status of a test matrix and the executions once they are created.

The test matrix will contain the list of test executions to run if and only if the resultStorage.toolResultsExecution fields have been populated.

Note: Flaky test executions may be added to the matrix at a later stage.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project
- INVALID_ARGUMENT - if the request is malformed
- NOT_FOUND - if the Test Matrix does not exist

### HTTP request

`GET https://testing.googleapis.com/v1/projects/{projectId}/testMatrices/{testMatrixId}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `projectId` | `string` Cloud project that owns the test matrix. |
| `testMatrixId` | `string` Unique test matrix id which was assigned by the service. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices#TestMatrix`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/cloud-platform.read-only`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).