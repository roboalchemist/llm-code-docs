# Source: https://developers.google.com/youtube/v3/live/docs/liveChatMessages/insert.md.txt

# LiveChatMessages: insert

Adds a message or a poll to a live chat.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/live/docs/liveChatMessages/insert#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
POST https://www.googleapis.com/youtube/v3/liveChat/messages
```

### Authorization

This request requires authorization with at least one of the following scopes. To read more about authentication and authorization, see [Implementing OAuth 2.0 authentication](https://developers.google.com/youtube/v3/live/authentication).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                           Parameters                                                                                                            ||
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                            |||
| `part` | `string` The **part** parameter serves two purposes. It identifies the properties that the write operation will set as well as the properties that the API response will include. Set the parameter value to `snippet`. |

### Request body

Provide a [liveChatMessage resource](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#resource) in the request body.
For that resource, you must specify values for these properties

- `snippet.liveChatId`
- `snippet.type` - choose one of the following options: `textMessageEvent` or `pollEvent`
- If type is `textMessageEvent`, include `snippet.textMessageDetails.messageText`
- If type is `pollEvent`, include `snippet.pollDetails` with the following values:
  - `snippet.pollDetails.metadata.options.questionText`
  - List of `snippet.pollDetails.metadata.options.optionText`. You must list at least two items and no more than four items. Items are displayed sequentially in the order they're listed.

## Response

If successful, this method returns a [liveChatMessage resource](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#resource) in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. For more details, see [YouTube Live Streaming API - Errors](https://developers.google.com/youtube/v3/live/docs/errors).

|      Error type      |       Error detail        |                                                                                                   Description                                                                                                    |
|----------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `forbidden (403)`    | `forbidden`               | You don't have the permissions required to create the specified message.                                                                                                                                         |
| `forbidden (403)`    | `liveChatDisabled`        | The specified live chat has been disabled by the owner, which means messages cannot be added to the chat.                                                                                                        |
| `forbidden (403)`    | `liveChatEnded`           | The specified live chat is no longer live.                                                                                                                                                                       |
| `invalidValue (400)` | `messageTextInvalid`      | The message text (`snippet.textMessageDetails.messageText`) is not valid.                                                                                                                                        |
| `notFound (404)`     | `liveChatNotFound`        | The live chat identified in the API request does not exist. This error occurs if the chat has been deleted by the owner.                                                                                         |
| `required (400)`     | `liveChatIdRequired`      | The [liveChatMessage resource](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#resource) must include and specify a value for the `snippet.liveChatId` property.                             |
| `required (400)`     | `messageTextRequired`     | The [liveChatMessage resource](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#resource) must include and specify a value for the `snippet.textMessageDetails.messageText` property.         |
| `required (400)`     | `typeRequired`            | The [liveChatMessage resource](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#resource) must include and specify a value for the `snippet.type` property. Set the parameter value to `text` |
| `required (400)`     | `preconditionCheckFailed` | A pinned active poll already exists.                                                                                                                                                                             |
| `rateLimitExceeded`  | `rateLimitExceeded`       | The user has posted too many chat messages in a given timeframe.                                                                                                                                                 |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.