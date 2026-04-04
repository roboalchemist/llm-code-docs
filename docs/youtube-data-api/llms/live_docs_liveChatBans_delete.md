# Source: https://developers.google.com/youtube/v3/live/docs/liveChatBans/delete.md.txt

# LiveChatBans: delete

Removes a ban that prevents a specific user from contributing to a live chat, thereby enabling the user to rejoin the chat. The API request must be authorized by the channel owner or a moderator of the live chat associated with the ban.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/live/docs/liveChatBans/delete#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
DELETE https://www.googleapis.com/youtube/v3/liveChat/bans
```

### Authorization

This request requires authorization with at least one of the following scopes. To read more
about authentication and authorization, see [Implementing OAuth 2.0 authentication](https://developers.google.com/youtube/v3/live/authentication).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                           Parameters                                                            ||
|------|---------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                            |||
| `id` | `string` The **id** parameter identifies the chat ban to remove. The value uniquely identifies both the ban and the chat. |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns an HTTP `204 No Content` status code.

## Errors

The following table identifies error messages that the API could return in response to a call to
this method. For more details, see [error message](https://developers.google.com/youtube/v3/live/docs/errors).

|      Error type      |       Error detail        |                                                                           Description                                                                           |
|----------------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `forbidden (403)`    | `forbidden`               | The specified ban cannot be removed. This error can occur if the request is authorized by one moderator who is attempting to remove a ban on another moderator. |
| `forbidden (403)`    | `insufficientPermissions` | You do not have the necessary permissions to remove the specified ban.                                                                                          |
| `invalidValue (400)` | `invalidLiveChatBanId`    | The `id` parameter specifies an invalid value.                                                                                                                  |
| `notFound (404)`     | `liveChatBanNotFound`     | The specified ban cannot be found.                                                                                                                              |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.