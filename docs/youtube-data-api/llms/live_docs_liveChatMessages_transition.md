# Source: https://developers.google.com/youtube/v3/live/docs/liveChatMessages/transition.md.txt

# LiveChatMessages: transition

Transitions the status of a YouTube live chat message and initiates any processes associated with the new status. For example, when you transition a live poll's status to `closed`, YouTube ends that message's poll. Before calling this method, you should confirm that the value of the [status](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.pollDetails.metadata.status) property for the live poll message is `active`.

## Request

### HTTP request

```
POST https://www.googleapis.com/youtube/v3/liveChat/messages/transition
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/live/authentication)).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                    Parameters                                                                                                                                                                                                    ||
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                             |||
| `id`     | `string` The **id** parameter specifies the unique ID of the message that is transitioning to another status.                                                                                                                                                                                                                                                                                          |
| `status` | `enum` The **status** parameter identifies the state to which the message is changing. To transition a message to the `closed` state, the [status](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.pollDetails.metadata.status) must be `active` for the poll that the message is bound to. <br /> You can only transition to **closed**, meaning that the poll is closed. |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                             |||
| `part`   | `string` The **part** parameter specifies the `liveChatMessage` resource parts that the API response will include. Supported values are `id`, `snippet`, and `authorDetails`. <br /> Set the parameter value to `snippet` to get the final poll result in the response body.                                                                                                                           |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a [liveChatMessages resource](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#resource) in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/live/docs/errors) documentation for more detail.

|    Error type     |        Error detail        |                                                                           Description                                                                           |
|-------------------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `forbidden (403)` | `forbidden`                | You don't have the permissions required to transition the status of the specified message.                                                                      |
| `required (400)`  | `idRequired`               | The required `id` parameter must identify the message whose status you want to transition.                                                                      |
| `required (400)`  | `statusRequired`           | The API request must specify a value for the `status` parameter.                                                                                                |
| `notFound (404)`  | `liveChatMessagesNotFound` | The message specified by the `id` parameter does not exist.                                                                                                     |
| `forbidden (403)` | `modificationNotAllowed`   | The status of the specified `liveChatMessage` resource cannot be transitioned. The `id` parameter might identify a message whose status cannot be transitioned. |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.