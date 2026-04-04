# Source: https://developers.google.com/youtube/v3/docs/commentThreads/insert.md.txt

# CommentThreads: insert

Creates a new top-level comment. To add a reply to an existing comment, use the [comments.insert](https://developers.google.com/youtube/v3/docs/comments/insert) method instead.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/commentThreads/insert#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
POST https://www.googleapis.com/youtube/v3/commentThreads
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/guides/authentication)).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                      Parameters                                                                                                                                                      ||
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                 |||
| `part` | `string` The **part** parameter identifies the properties that the API response will include. Set the parameter value to `snippet`. The `snippet` part has a quota cost of 2 units. The following list contains the `part` names that you can include in the parameter value: - `id` - `replies` - `snippet` |

### Request body

Provide a [commentThread resource](https://developers.google.com/youtube/v3/docs/commentThreads#resource) in the request body.

For that resource, you must specify a value for the following properties:

- `snippet.channelId`
- `snippet.videoId`
- `snippet.topLevelComment.snippet.textOriginal`

## Response

If successful, this method returns a [commentThread resource](https://developers.google.com/youtube/v3/docs/commentThreads#resource) in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. For more details, see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation.

|     Error type     |          Error detail          |                                                                                                                                                                                  Description                                                                                                                                                                                   |
|--------------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)` | `channelOrVideoIdMissing`      | Each comment thread must be linked to a video. Make sure the resource specifies values for the [snippet.channelId](https://developers.google.com/youtube/v3/docs/commentThreads#snippet.channelId) and the [snippet.videoId](https://developers.google.com/youtube/v3/docs/commentThreads#snippet.videoId) properties. A comment on a video appears on the video's watch page. |
| `badRequest (400)` | `commentTextRequired`          | The `comment` resource that is being inserted must specify a value for the `snippet.topLevelComment.snippet.textOriginal` property. Comments cannot be empty.                                                                                                                                                                                                                  |
| `badRequest (400)` | `commentTextTooLong`           | The `comment` resource that is being inserted contains too many characters in the `snippet.topLevelComment.snippet.textOriginal` property.                                                                                                                                                                                                                                     |
| `badRequest (400)` | `invalidCommentThreadMetadata` | The request metadata is invalid.                                                                                                                                                                                                                                                                                                                                               |
| `badRequest (400)` | `processingFailure`            | The API server failed to successfully process the request. While this can be a transient error, it usually indicates that the request's input is invalid. Check the structure of the `commentThread` resource in the request body to ensure that it is valid.                                                                                                                  |
| `forbidden (403)`  | `forbidden`                    | The comment thread couldn't be created due to insufficient permissions. The request might not be properly authorized.                                                                                                                                                                                                                                                          |
| `forbidden (403)`  | `ineligibleAccount`            | The YouTube account used to authorize the API request must be merged with the user's Google Account to insert a comment or comment thread.                                                                                                                                                                                                                                     |
| `notFound (404)`   | `channelNotFound`              | The specified channel couldn't be found. Check the value of the [snippet.channelId](https://developers.google.com/youtube/v3/docs/commentThreads#snippet.channelId) property to ensure it is correct.                                                                                                                                                                          |
| `notFound (404)`   | `videoNotFound`                | The specified video couldn't be found. Check the value of the [snippet.videoId](https://developers.google.com/youtube/v3/docs/commentThreads#snippet.videoId) property to ensure it is correct.                                                                                                                                                                                |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.