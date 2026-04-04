# Source: https://developers.google.com/youtube/v3/live/docs/liveStreams/update.md.txt

# LiveStreams: update

Updates a video stream. If the properties that you want to change cannot be updated, then you need to create a new stream with the proper settings.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/live/docs/liveStreams/update#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
PUT https://www.googleapis.com/youtube/v3/liveStreams
```

### Authorization

This request requires authorization with at least one of the following scopes. To read more about authentication and authorization, see [Implementing OAuth 2.0 authorization](https://developers.google.com/youtube/v3/live/authentication).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ||
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |||
| `part`                          | `string` The **part** parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include. The `part` properties that you can include in the parameter value are `id`, `snippet`, `cdn`, and `status`. Note that this method will override the existing values for all of the mutable properties that are contained in any parts that the parameter value specifies. If the request body does not specify a value for a mutable property, the existing value for that property will be removed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |||
| `onBehalfOfContentOwner`        | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/live/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwner** parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.                                                                                                                                                                                                                                                                                                                                                          |
| `onBehalfOfContentOwnerChannel` | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/live/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwnerChannel** parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the `onBehalfOfContentOwner` parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the `onBehalfOfContentOwner` parameter specifies. Finally, the channel that the `onBehalfOfContentOwnerChannel` parameter value specifies must be linked to the content owner that the `onBehalfOfContentOwner` parameter specifies. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel. |

### Request body

Provide a [liveStream resource](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) in the request body.
For that resource:

- You must specify a value for these properties:

  <br />

  - `id`
  - `snippet.title`
  - `cdn.frameRate`
  - `cdn.ingestionType`
  - `cdn.resolution`

  <br />

- You can set values for these properties:

  <br />

  - `snippet.title`
  - `snippet.description`

  <br />

  If you are submitting an update request, and your request does not specify a value for a property that already has a value, the property's existing value will be deleted.

## Response

If successful, this method returns a [liveStream resource](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. For more details, see [YouTube Live Streaming API - Errors](https://developers.google.com/youtube/v3/live/docs/errors).

|        Error type         |            Error detail            |                                                                                                                                                                                                                                         Description                                                                                                                                                                                                                                         |
|---------------------------|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `forbidden (403)`         | `liveStreamModificationNotAllowed` | The specified live stream cannot be modified in its current state. For more information, see [Life of a Broadcast](https://developers.google.com/youtube/v3/live/life-of-a-broadcast).                                                                                                                                                                                                                                                                                                      |
| `forbidden (403)`         | `liveStreamModificationNotAllowed` | The API does not allow you to change the value of the [cdn.format](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.format), [cdn.frameRate](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.frameRate), [cdn.ingestionType](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.ingestionType), or [cdn.resolution](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.resolution) fields after the stream is created. |
| `forbidden (403)`         | `liveStreamModificationNotAllowed` | The API does not allow you to change a reusable stream to be non-reusable, or vice versa. For more information, see [Understanding Broadcasts and Streams](https://developers.google.com/youtube/v3/live/broadcasts-and-streams).                                                                                                                                                                                                                                                           |
| `insufficientPermissions` | `insufficientLivePermissions`      | The request is not authorized to update the specified live stream. For more information, see [Implementing OAuth2 authentication](https://developers.google.com/youtube/v3/live/authentication).                                                                                                                                                                                                                                                                                            |
| `insufficientPermissions` | `liveStreamingNotEnabled`          | The user that authorized the request is not enabled to stream live video on YouTube. The user can find more information at [Feature eligibility](https://www.youtube.com/features).                                                                                                                                                                                                                                                                                                         |
| `invalidValue (400)`      | `invalidDescription`               | The `snippet.description` property's value in the [liveStream resource](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) can have up to 10000 characters.                                                                                                                                                                                                                                                                                                           |
| `invalidValue (400)`      | `invalidTitle`                     | The `snippet.title` property's value in the [liveStream resource](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) must be between 1 and 128 characters long.                                                                                                                                                                                                                                                                                                       |
| `notFound (404)`          | `liveStreamNotFound`               | The specified live stream doesn't exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `required (400)`          | `idRequired`                       | The [liveStream resource](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) must specify a value for the `id` property.                                                                                                                                                                                                                                                                                                                                              |
| `required (400)`          | `ingestionTypeRequired`            | The [liveStream resource](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) must specify a value for the `cdn.ingestionType` property.                                                                                                                                                                                                                                                                                                                               |
| `required (400)`          | `titleRequired`                    | The [liveStream resource](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) must specify a value for the `snippet.title` property.                                                                                                                                                                                                                                                                                                                                   |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.