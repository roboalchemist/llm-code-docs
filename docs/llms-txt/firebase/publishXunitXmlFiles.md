# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/publishXunitXmlFiles.md.txt

# Method: projects.histories.executions.steps.publishXunitXmlFiles

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/publishXunitXmlFiles#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/publishXunitXmlFiles#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/publishXunitXmlFiles#body.request_body)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/publishXunitXmlFiles#body.request_body.SCHEMA_REPRESENTATION)
- [Response body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/publishXunitXmlFiles#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/publishXunitXmlFiles#body.aspect)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/publishXunitXmlFiles#try-it)

Publish xml files to an existing Step.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to write project
- INVALID_ARGUMENT - if the request is malformed
- FAILED_PRECONDITION - if the requested state transition is illegal, e.g. try to upload a duplicate xml file or a file too large.
- NOT_FOUND - if the containing Execution does not exist

### HTTP request

`POST https://toolresults.googleapis.com/toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}:publishXunitXmlFiles`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                           Parameters                                           ||
|---------------|---------------------------------------------------------------------------------|
| `projectId`   | `string` A Project id. Required.                                                |
| `historyId`   | `string` A History id. Required.                                                |
| `executionId` | `string` A Execution id. Required.                                              |
| `stepId`      | `string` A Step id. Note: This step must include a TestExecutionStep. Required. |

### Request body

The request body contains data with the following structure:

|                                                           JSON representation                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "xunitXmlFiles": [ { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/FileReference) } ] } ``` |

|                                                                                                                              Fields                                                                                                                              ||
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `xunitXmlFiles[]` | `object (`[FileReference](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/FileReference)`)` URI of the Xunit XML files to publish. The maximum size of the file this reference is pointing to is 50MB. Required. |

### Response body

If successful, the response body contains an instance of [Step](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps#Step).

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).