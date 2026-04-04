# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list.md.txt

# Method: projects.histories.executions.steps.thumbnails.list

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#body.ListStepThumbnailsResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#body.aspect)
- [Image](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#Image)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#Image.SCHEMA_REPRESENTATION)
- [Thumbnail](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#Thumbnail)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#Thumbnail.SCHEMA_REPRESENTATION)
- [Status](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#Status)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#Status.SCHEMA_REPRESENTATION)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#try-it)

Lists thumbnails of images attached to a step.

May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to read from the project, or from any of the images - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the step does not exist, or if any of the images do not exist

### HTTP request

`GET https://toolresults.googleapis.com/toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/thumbnails`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `projectId` | `string` A Project id. Required. |
| `historyId` | `string` A History id. Required. |
| `executionId` | `string` An Execution id. Required. |
| `stepId` | `string` A Step id. Required. |

### Query parameters

| Parameters ||
|---|---|
| `pageToken` | `string` A continuation token to resume the query at the next item. Optional. |
| `pageSize` | `integer` The maximum number of thumbnails to fetch. Default value: 50. The server will use this default if the field is not set or has a value of 0. Optional. |

### Request body

The request body must be empty.

### Response body

A response containing the thumbnails in a step.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "thumbnails": [ { object (`https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#Image`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `thumbnails[]` | ``object (`https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#Image`)`` A list of image data. Images are returned in a deterministic order; they are ordered by these factors, in order of importance: \* First, by their associated test case. Images without a test case are considered greater than images with one. \* Second, by their creation time. Images without a creation time are greater than images with one. \* Third, by the order in which they were added to the step (by calls to steps.create or steps.patch). |
| `nextPageToken` | `string` A continuation token to resume the query at the next item. If set, indicates that there are more thumbnails to read, by calling list again with this value in the pageToken field. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## Image

An image, with a link to the main image and a thumbnail.

| JSON representation |
|---|
| ``` { "stepId": string, "sourceImage": { object (`https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/ToolOutputReference`) }, // Union field `thumbnail_or_error` can be only one of the following: "thumbnail": { object (`https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#Thumbnail`) }, "error": { object (`https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#Status`) } // End of list of possible types for union field `thumbnail_or_error`. } ``` |

| Fields ||
|---|---|
| `stepId` | `string` The step to which the image is attached. Always set. |
| `sourceImage` | ``object (`https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/ToolOutputReference`)`` A reference to the full-size, original image. This is the same as the toolOutputs entry for the image under its Step. Always set. |
| Union field `thumbnail_or_error`. Either a thumbnail of the image, or an error explaining why the thumbnail could not be rendered. `thumbnail_or_error` can be only one of the following: ||
| `thumbnail` | ``object (`https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#Thumbnail`)`` The thumbnail. |
| `error` | ``object (`https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#Status`)`` An error explaining why the thumbnail could not be rendered. |

## Thumbnail

A single thumbnail, with its size and format.

| JSON representation |
|---|
| ``` { "contentType": string, "heightPx": integer, "widthPx": integer, "data": string } ``` |

| Fields ||
|---|---|
| `contentType` | `string` The thumbnail's content type, i.e. "image/png". Always set. |
| `heightPx` | `integer` The height of the thumbnail, in pixels. Always set. |
| `widthPx` | `integer` The width of the thumbnail, in pixels. Always set. |
| `data` | `string (https://developers.google.com/discovery/v1/type-format format)` The thumbnail file itself. That is, the bytes here are precisely the bytes that make up the thumbnail file; they can be served as an image as-is (with the appropriate content type.) Always set. A base64-encoded string. |

## Status

The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details.

You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors).

| JSON representation |
|---|
| ``` { "code": integer, "message": string, "details": [ { "@type": string, field1: ..., ... } ] } ``` |

| Fields ||
|---|---|
| `code` | `integer` The status code, which should be an enum value of `google.rpc.Code`. |
| `message` | `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps.thumbnails/list#Status.FIELDS.details` field, or localized by the client. |
| `details[]` | `object` A list of messages that carry the error details. There is a common set of message types for APIs to use. An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`. |