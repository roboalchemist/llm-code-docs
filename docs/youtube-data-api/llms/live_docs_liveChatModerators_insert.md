# Source: https://developers.google.com/youtube/v3/live/docs/liveChatModerators/insert.md.txt

# LiveChatModerators: insert

Adds a new moderator for the chat. The request must be authorized by the owner of the live chat's channel.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/live/docs/liveChatModerators/insert#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
POST https://www.googleapis.com/youtube/v3/liveChat/moderators
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/live/authentication)).

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

Provide a [liveChatModerator resource](https://developers.google.com/youtube/v3/live/docs/liveChatModerators#resource) in the request body.
For that resource:

- You must specify a value for these properties:

  <br />

  - `snippet.moderatorDetails.channelId`
  - `snippet.liveChatId`

  <br />

## Response

If successful, this method returns a [liveChatModerator resource](https://developers.google.com/youtube/v3/live/docs/liveChatModerators#resource) in the response body.

## Errors

The API does not define any error messages that are unique to this API method. However, this method could still return general API errors listed in the [error message](https://developers.google.com/youtube/v3/live/docs/errors#general) documentation.

## Try it!

Use the APIs Explorer to call this API and see the API request and response.