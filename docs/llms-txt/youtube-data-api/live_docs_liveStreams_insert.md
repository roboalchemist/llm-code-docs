# Source: https://developers.google.com/youtube/v3/live/docs/liveStreams/insert.md.txt

# LiveStreams: insert

Creates a video stream. The stream enables you to send your video to YouTube, which can then broadcast the video to your audience.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/live/docs/liveStreams/insert#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
POST https://www.googleapis.com/youtube/v3/liveStreams
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/live/authentication)).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ||
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |||
| `part`                          | `string` The **part** parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include. The `part` properties that you can include in the parameter value are `id`, `snippet`, `cdn`, `contentDetails`, and `status`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |||
| `onBehalfOfContentOwner`        | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/live/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwner** parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `onBehalfOfContentOwnerChannel` | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/live/authentication). This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwnerChannel** parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the `onBehalfOfContentOwner` parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the `onBehalfOfContentOwner` parameter specifies. Finally, the channel that the `onBehalfOfContentOwnerChannel` parameter value specifies must be linked to the content owner that the `onBehalfOfContentOwner` parameter specifies. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel. |

### Request body

Provide a [liveStream resource](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) in the request body.
For that resource:

- You must specify a value for these properties:

  <br />

  - `snippet.title`
  - `cdn.frameRate`
  - `cdn.ingestionType`
  - `cdn.resolution`

  <br />

- You can set values for these properties:

  <br />

  - `snippet.title`
  - `snippet.description`
  - `cdn.frameRate`
  - `cdn.ingestionType`
  - `cdn.resolution`
  - `contentDetails.isReusable`

  <br />

## Response

If successful, this method returns a [liveStream resource](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/live/docs/errors) documentation for more detail.

|        Error type         |         Error detail          |                                                                                                                 Description                                                                                                                  |
|---------------------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `insufficientPermissions` | `insufficientLivePermissions` | The request is not authorized to create the specified live stream.                                                                                                                                                                           |
| `insufficientPermissions` | `livePermissionBlocked`       | The user that authorized the request is unable to stream live video on YouTube at this time. Details explaining why the user cannot stream live video may be available in the user's channel settings at <https://www.youtube.com/features>. |
| `insufficientPermissions` | `liveStreamingNotEnabled`     | The user that authorized the request is not enabled to stream live video on YouTube. The user can find more information at <https://www.youtube.com/features>.                                                                               |
| `invalidValue (400)`      | `invalidDescription`          | The `snippet.description` property's value in the [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) resource can have up to 10000 characters.                                                            |
| `invalidValue (400)`      | `invalidFormat`               | The `cdn.format` property value in the [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) resource is invalid.                                                                                            |
| `invalidValue (400)`      | `invalidFrameRate`            | The `cdn.frameRate` property's value in the [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) resource is invalid.                                                                                       |
| `invalidValue (400)`      | `invalidIngestionType`        | The `cdn.ingestionType` property's value in the [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) resource is invalid.                                                                                   |
| `invalidValue (400)`      | `invalidResolution`           | The `cdn.resolution` property's value in the [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) resource is invalid.                                                                                      |
| `invalidValue (400)`      | `invalidTitle`                | The `snippet.title` property's value in the [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) resource must be between 1 and 128 characters long.                                                        |
| `rateLimitExceeded`       | `userRequestsExceedRateLimit` | The user has sent too many requests in a given timeframe.                                                                                                                                                                                    |
| `required (400)`          | `cdnRequired`                 | The [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) resource must contain the `cdn` object.                                                                                                            |
| `required (400)`          | `frameRateRequired`           | The API returns this error if you specify a value for the `cdn.resolution` property but not for the `cdn.frameRate` property.                                                                                                                |
| `required (400)`          | `ingestionTypeRequired`       | The [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) resource must specify a value for the `cdn.ingestionType` property\>.                                                                              |
| `required (400)`          | `resolutionRequired`          | The API returns this error if you specify a value for the `cdn.frameRate` property but not for the `cdn.resolution` property.                                                                                                                |
| `required (400)`          | `titleRequired`               | The [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) resource must specify a value for the `snippet.title` property.                                                                                    |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.