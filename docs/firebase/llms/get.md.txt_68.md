# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/testEnvironmentCatalog/get.md.txt

# Method: testEnvironmentCatalog.get

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/testEnvironmentCatalog/get#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/testEnvironmentCatalog/get#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/testEnvironmentCatalog/get#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/testEnvironmentCatalog/get#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/testEnvironmentCatalog/get#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/testEnvironmentCatalog/get#body.aspect)
- [EnvironmentType](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/testEnvironmentCatalog/get#EnvironmentType)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/testEnvironmentCatalog/get#try-it)

Gets the catalog of supported test environments.

May return any of the following canonical error codes:

- INVALID_ARGUMENT - if the request is malformed
- NOT_FOUND - if the environment type does not exist
- INTERNAL - if an internal error occurred

### HTTP request

`GET https://testing.googleapis.com/v1/testEnvironmentCatalog/{environmentType}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `environmentType` | ``enum (`https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/testEnvironmentCatalog/get#EnvironmentType`)`` Required. The type of environment that should be listed. |

### Query parameters

| Parameters ||
|---|---|
| `projectId` | `string` For authorization, the cloud project requesting the TestEnvironmentCatalog. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/testEnvironmentCatalog#TestEnvironmentCatalog`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/cloud-platform.read-only`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## EnvironmentType

Types of environments the Test API supports.

| Enums ||
|---|---|
| `ENVIRONMENT_TYPE_UNSPECIFIED` | Do not use. For proto versioning only. |
| `ANDROID` | A device running a version of the Android OS. |
| `IOS` | A device running a version of iOS. |
| `NETWORK_CONFIGURATION` | A network configuration to use when running a test. |
| `PROVIDED_SOFTWARE` | The software environment provided by TestExecutionService. |
| `DEVICE_IP_BLOCKS` | The IP blocks used by devices in the test environment. |