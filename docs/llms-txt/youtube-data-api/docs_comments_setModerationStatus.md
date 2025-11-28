# Source: https://developers.google.com/youtube/v3/docs/comments/setModerationStatus.md.txt

# Comments: setModerationStatus

Sets the moderation status of one or more comments. The API request must be authorized by the owner of the channel or video associated with the comments.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/comments/setModerationStatus#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
POST https://www.googleapis.com/youtube/v3/comments/setModerationStatus
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/guides/authentication)).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                             Parameters                                                                                                                                                                                                             ||
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                               |||
| `id`               | `string` The **id** parameter specifies a comma-separated list of IDs that identify the comments for which you are updating the moderation status.                                                                                                                                                                                                                                                             |
| `moderationStatus` | `string` Identifies the new moderation status of the specified comments. Acceptable values are: - **heldForReview** -- Marks a comment as awaiting review by a moderator. - **published** -- Clears a comment for public display. - **rejected** -- Rejects a comment as being unfit for display. This action also effectively hides all replies to the rejected comment.                                      |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                               |||
| `banAuthor`        | `boolean` The **banAuthor** parameter lets you indicate that you want to automatically reject any additional comments written by the comment's author. Set the parameter value to `true` to ban the author. **Note:** This parameter is only valid if the [moderationStatus](https://developers.google.com/youtube/v3/docs/comments/setModerationStatus#moderationStatus) parameter is also set to `rejected`. |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns an HTTP `204` response code (`No Content`).

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|     Error type     |      Error detail       |                                                                                                                    Description                                                                                                                     |
|--------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)` | `banWithoutReject`      | The `banAuthor` parameter can only be used if the `moderationStatus` parameter value is `rejected`.                                                                                                                                                |
| `badRequest (400)` | `operationNotSupported` | Comments not based on Google+ offer only limited moderation functionality.                                                                                                                                                                         |
| `badRequest (400)` | `processingFailure`     | The API server failed to successfully process the request. While this can be a transient error, it usually indicates that the request's input is invalid.                                                                                          |
| `forbidden (403)`  | `forbidden`             | The moderation status of one or more comments cannot be set due to insufficient permissions. The request might not be properly authorized.                                                                                                         |
| `notFound (404)`   | `commentNotFound`       | One or more of the comments that the request is trying to update cannot be found. Check the values of the request's [id](https://developers.google.com/youtube/v3/docs/comments/setModerationStatus#id) parameter to ensure that they are correct. |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.