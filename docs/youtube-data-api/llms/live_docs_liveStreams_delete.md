# Source: https://developers.google.com/youtube/v3/live/docs/liveStreams/delete.md.txt

# LiveStreams: delete

Deletes a video stream.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/live/docs/liveStreams/delete#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
DELETE https://www.googleapis.com/youtube/v3/liveStreams
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

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ||
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |||
| `id`                            | `string` The **id** parameter specifies the YouTube live stream ID for the resource that is being deleted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |||
| `onBehalfOfContentOwner`        | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/live/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwner** parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.                                                                                                                                                                                                                                                                                                                                                          |
| `onBehalfOfContentOwnerChannel` | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/live/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwnerChannel** parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the `onBehalfOfContentOwner` parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the `onBehalfOfContentOwner` parameter specifies. Finally, the channel that the `onBehalfOfContentOwnerChannel` parameter value specifies must be linked to the content owner that the `onBehalfOfContentOwner` parameter specifies. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel. |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a [liveStream resource](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to
this method. For more details, see [error message](https://developers.google.com/youtube/v3/live/docs/errors).

|        Error type         |          Error detail          |                                                                                           Description                                                                                            |
|---------------------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `forbidden (403)`         | `liveStreamDeletionNotAllowed` | The specified live stream cannot be deleted because it is bound to a broadcast that has still not completed.                                                                                     |
| `insufficientPermissions` | `insufficientLivePermissions`  | The request is not authorized to delete the specified live stream. For more information, see [Implementing OAuth2 authentication](https://developers.google.com/youtube/v3/live/authentication). |
| `insufficientPermissions` | `liveStreamingNotEnabled`      | The user that authorized the request is not enabled to stream live video on YouTube. For more information, see [Feature eligibility](https://www.youtube.com/features).                          |
| `notFound (404)`          | `liveStreamNotFound`           | The specified live stream doesn't exist.                                                                                                                                                         |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.