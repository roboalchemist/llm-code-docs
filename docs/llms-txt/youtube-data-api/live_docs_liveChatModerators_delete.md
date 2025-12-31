# Source: https://developers.google.com/youtube/v3/live/docs/liveChatModerators/delete.md.txt

# LiveChatModerators: delete

Removes a chat moderator. The request must be authorized by the owner of the live chat's channel.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/live/docs/liveChatModerators/delete#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
DELETE https://www.googleapis.com/youtube/v3/liveChat/moderators
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/live/authentication)).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                 Parameters                                                                  ||
|------|---------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                        |||
| `id` | `string` The **id** parameter identifies the chat moderator to remove. The value uniquely identifies both the moderator and the chat. |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns an HTTP `204` response code (`No Content`).

## Errors

The API does not define any error messages that are unique to this API method. However, this method could still return general API errors listed in the [error message](https://developers.google.com/youtube/v3/live/docs/errors#general) documentation.

## Try it!

Use the APIs Explorer to call this API and see the API request and response.