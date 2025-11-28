# Source: https://developers.google.com/youtube/v3/live/docs/liveChatBans/insert.md.txt

# LiveChatBans: insert

Bans a specific user from participating in the live chat. The API request must be authorized by the channel owner or a moderator of the live chat associated with the ban.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/live/docs/liveChatBans/insert#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
POST https://www.googleapis.com/youtube/v3/liveChat/bans
```

### Authorization

This request requires authorization with at least one of the following scopes. To read more
about authentication and authorization, see
[Implementing OAuth 2.0 authentication](https://developers.google.com/youtube/v3/live/authentication).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                  Parameters                                                                                                                  ||
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                         |||
| `part` | `string` The **part** parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response returns. Set the parameter value to `snippet`. |

### Request body

Provide a [liveChatBan resource](https://developers.google.com/youtube/v3/live/docs/liveChatBans#resource) in the request body.
For that resource:

- You must specify a value for these properties:

  <br />

  - `snippet.liveChatId`
  - `snippet.type`
  - `snippet.bannedUserDetails.channelId`

  <br />

- You can set values for these properties:

  <br />

  - `snippet.banDurationSeconds`

  <br />

## Response

If successful, this method returns a [liveChatBan resource](https://developers.google.com/youtube/v3/live/docs/liveChatBans#resource) in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. For more details, see [YouTube Live Streaming API - Errors](https://developers.google.com/youtube/v3/live/docs/errors).

|      Error type      |           Error detail           |                                                                                  Description                                                                                  |
|----------------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `forbidden (403)`    | `insufficientPermissions`        | You do not have the necessary permissions to ban a user from the specified live chat.                                                                                         |
| `forbidden (403)`    | `liveChatBanInsertionNotAllowed` | The specified ban cannot be created. This error can occur if the request attempts to ban the chat owner or another moderator.                                                 |
| `invalidValue (400)` | `invalidChannelId`               | The specified channel ID cannot be found.                                                                                                                                     |
| `invalidValue (400)` | `invalidLiveChatId`              | The `snippet.liveChatId` value specified in the request is invalid. Check the associated `liveBroadcast` resource to ensure that you have the correct value.                  |
| `notFound (404)`     | `liveChatNotFound`               | The specified live chat cannot be found. Check the associated `liveBroadcast` resource to ensure that you are setting the `snippet.liveChatId` property to the correct value. |
| `notFound (404)`     | `liveChatUserNotFound`           | The live chat user you are trying to ban cannot be found.                                                                                                                     |
| `required (400)`     | `bannedUserChannelIdRequired`    | The `liveChatBan` resource submitted in the request body must specify a value for the `snippet.bannedUserDetails.channelId` property.                                         |
| `required (400)`     | `liveChatIdRequired`             | The `liveChatBan` resource submitted in the request body must specify a value for the `snippet.liveChatId` property.                                                          |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.