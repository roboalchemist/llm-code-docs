# Source: https://developers.google.com/youtube/v3/docs/comments/update.md.txt

# Comments: update

Modifies a comment.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/comments/update#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
PUT https://www.googleapis.com/youtube/v3/comments
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/guides/authentication)).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                               Parameters                                                                                                                                                                               ||
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                   |||
| `part` | `string` The **part** parameter identifies the properties that the API response will include. You must at least include the `snippet` part in the parameter value since that part contains all of the properties that the API request can update. The following list contains the `part` names that you can include in the parameter value: - `id` - `snippet` |

### Request body

Provide a [comment resource](https://developers.google.com/youtube/v3/docs/comments#resource) in the request body.
For that resource:

- You can set values for these properties:

  <br />

  - `snippet.textOriginal`

  <br />

## Response

If successful, this method returns a [comment resource](https://developers.google.com/youtube/v3/docs/comments#resource) in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|     Error type     |       Error detail       |                                                                                                                       Description                                                                                                                       |
|--------------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)` | `commentTextTooLong`     | The `comment` resource that is being updated contains too many characters in the `snippet.textOriginal` property.                                                                                                                                       |
| `badRequest (400)` | `invalidCommentMetadata` | The request metadata is invalid.                                                                                                                                                                                                                        |
| `badRequest (400)` | `operationNotSupported`  | Only Google+ based comments can be updated.                                                                                                                                                                                                             |
| `badRequest (400)` | `processingFailure`      | The API server failed to successfully process the request. While this can be a transient error, it usually indicates that the request's input is invalid. Check the structure of the `comment` resource in the request body to ensure that it is valid. |
| `forbidden (403)`  | `forbidden`              | The comment could not be updated due to insufficient permissions. The request might not be properly authorized.                                                                                                                                         |
| `forbidden (403)`  | `ineligibleAccount`      | The YouTube account used to authorize the API request must be merged with the user's Google account to update a comment or comment thread.                                                                                                              |
| `notFound (404)`   | `commentNotFound`        | The specified comment could not be found. Check the value of the [id](https://developers.google.com/youtube/v3/docs/comments#id) property in the request body to ensure that it is correct.                                                             |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.