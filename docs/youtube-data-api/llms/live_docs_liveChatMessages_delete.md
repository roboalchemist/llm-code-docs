# Source: https://developers.google.com/youtube/v3/live/docs/liveChatMessages/delete.md.txt

# LiveChatMessages: delete

Deletes a chat message. The API request must be authorized by the channel owner or a moderator of the live chat associated with the ban.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/live/docs/liveChatMessages/delete#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
DELETE https://www.googleapis.com/youtube/v3/liveChat/messages
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/live/authentication)).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                    Parameters                                                    ||
|------|------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                             |||
| `id` | `string` The **id** parameter specifies the YouTube chat message ID of the resource that is being deleted. |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns an HTTP `204` response code (`No Content`).

## Errors

The following table identifies error messages that the API could return in response to a call to this method. See the [error message](https://developers.google.com/youtube/v3/live/docs/errors) documentation for more detail.

|    Error type     |       Error detail        |                                                                                   Description                                                                                    |
|-------------------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `forbidden (403)` | `forbidden`               | You don't have the permissions required to delete the specified message.                                                                                                         |
| `forbidden (403)` | `modificationNotAllowed`  | The specified `liveChatMessage` resource cannot be deleted. The `id` parameter might identify a message created by a moderator or another user whose messages cannot be deleted. |
| `notFound (404)`  | `liveChatMessageNotFound` | The message that you are trying to delete cannot be found. Check the value of the `id` parameter to ensure it is correct.                                                        |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.