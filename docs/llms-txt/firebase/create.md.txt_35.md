# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/create.md.txt

# Method: projects.testMatrices.create

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/create#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/create#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/create#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/create#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/create#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/create#body.aspect)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/create#try-it)

Creates and runs a matrix of tests according to the given specifications. Unsupported environments will be returned in the state UNSUPPORTED. A test matrix is limited to use at most 2000 devices in parallel.

The returned matrix will not yet contain the executions that will be created for this matrix. Execution creation happens later on and will require a call to testMatrices.get.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to write to project
- INVALID_ARGUMENT - if the request is malformed or if the matrix tries to use too many simultaneous devices.

### HTTP request

`POST https://testing.googleapis.com/v1/projects/{projectId}/testMatrices`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `projectId` | `string` The GCE project under which this job will run. |

### Query parameters

| Parameters ||
|---|---|
| `requestId` | `string` A string id used to detect duplicated requests. Ids are automatically scoped to a project, so users should ensure the ID is unique per-project. A UUID is recommended. Optional, but strongly recommended. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices#TestMatrix`.

### Response body

If successful, the response body contains a newly created instance of `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices#TestMatrix`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).