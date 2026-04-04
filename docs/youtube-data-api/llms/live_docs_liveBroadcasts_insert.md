# Source: https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/insert.md.txt

# LiveBroadcasts: insert

The API now supports the ability to mark your [live
broadcasts](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts) as "made for kids," and the `liveBroadcast` resource now contains a property that identifies the "made for kids" status of that live broadcast. The YouTube API Services Terms of Service and Developer Policies were also updated on 10 January 2020. For more information, please see the revision histories for the [YouTube Live Streaming API Service](https://developers.google.com/youtube/v3/live/revision_history) and the [YouTube API Services Terms of Service](https://developers.google.com/youtube/terms/revision-history).
Creates a broadcast.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/insert#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
POST https://www.googleapis.com/youtube/v3/liveBroadcasts
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
| `part`                          | `string` The **part** parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include. The `part` properties that you can include in the parameter value are `id`, `snippet`, `contentDetails`, and `status`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |||
| `onBehalfOfContentOwner`        | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/live/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwner** parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `onBehalfOfContentOwnerChannel` | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/live/authentication). This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwnerChannel** parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the `onBehalfOfContentOwner` parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the `onBehalfOfContentOwner` parameter specifies. Finally, the channel that the `onBehalfOfContentOwnerChannel` parameter value specifies must be linked to the content owner that the `onBehalfOfContentOwner` parameter specifies. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel. |

### Request body

Provide a [liveBroadcast resource](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource) in the request body.
For that resource:

- You must specify a value for these properties:

  <br />

  - `snippet.title`
  - `snippet.scheduledStartTime`
  - `status.privacyStatus`

  <br />

- You can set values for these properties:

  <br />

  - `snippet.title`
  - `snippet.description`
  - `snippet.scheduledStartTime`
  - `snippet.scheduledEndTime`
  - `status.privacyStatus`
  - `status.selfDeclaredMadeForKids`
  - `contentDetails.monitorStream.enableMonitorStream`
  - `contentDetails.monitorStream.broadcastStreamDelayMs`
  - `contentDetails.enableAutoStart`
  - `contentDetails.enableAutoStop`
  - `contentDetails.enableClosedCaptions`
  - `contentDetails.enableDvr`
  - `contentDetails.enableEmbed`
  - `contentDetails.recordFromStart`

  <br />

  **Note:** The [property table](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#properties) documents any default values that are set for the properties listed above. The default values will be assigned in either of the following cases:  
  - You do not specify values for those properties.
  - The [part](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/insert#part) parameter value in your request does not specify the part that contains those properties.

## Response

If successful, this method returns a [liveBroadcast resource](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource) in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/live/docs/errors) documentation for more detail.

|        Error type         |           Error detail            |                                                                                                                                                            Description                                                                                                                                                            |
|---------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `insufficientPermissions` | `insufficientLivePermissions`     | The request is not authorized to create the live broadcast.                                                                                                                                                                                                                                                                       |
| `insufficientPermissions` | `livePermissionBlocked`           | The user that authorized the request is unable to stream live video on YouTube at this time. Details explaining why the user cannot stream live video may be available in the user's channel settings at <https://www.youtube.com/features>.                                                                                      |
| `insufficientPermissions` | `liveStreamingNotEnabled`         | The user that authorized the request is not enabled to stream live video on YouTube. The user can find more information at <https://www.youtube.com/features>.                                                                                                                                                                    |
| `invalidValue (400)`      | `invalidAutoStart`                | The [liveBroadcast resource](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource) contained an invalid value for the `contentDetails.enableAutoStart` property. Not all broadcasts support this setting.                                                                                                   |
| `invalidValue (400)`      | `invalidAutoStop`                 | The [liveBroadcast resource](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource) contained an invalid value for the `contentDetails.enableAutoStop` property. You cannot modify the `enableAutoStop` setting for a persistent broadcast.                                                                  |
| `invalidValue (400)`      | `invalidDescription`              | The [liveBroadcast resource](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource) did not specify a valid value for the `snippet.description` property. The property's value can contain up to 5000 characters.                                                                                            |
| `invalidValue (400)`      | `invalidEmbedSetting`             | The [liveBroadcast resource](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource) contained an invalid value for the `contentDetails.enable_embed` property. You cannot embed this broadcast.                                                                                                              |
| `invalidValue (400)`      | `invalidLatencyPreferenceOptions` | The [liveBroadcast resource](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource) contained an invalid value for the `contentDetails.latencyPreference` property. Not all settings are supported with this latency preference.                                                                             |
| `invalidValue (400)`      | `invalidPrivacyStatus`            | The [liveBroadcast resource](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource) contained an invalid value for the [status.privacy_status](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#privacyStatus) property.                                                                    |
| `invalidValue (400)`      | `invalidProjection`               | The [liveBroadcast resource](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource) contained an invalid value for the `contentDetails.projection` property. A default broadcast's projection cannot be set to `360`.                                                                                        |
| `invalidValue (400)`      | `invalidScheduledEndTime`         | The [liveBroadcast resource](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource) contained an invalid value for the `snippet.scheduledEndTime` property. The scheduled end time must follow the scheduled start time.                                                                                     |
| `invalidValue (400)`      | `invalidScheduledStartTime`       | The [liveBroadcast resource](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource) contained an invalid value for the `snippet.scheduledStartTime` property. The scheduled start time must be in the future and close enough to the current date that a broadcast could be reliably scheduled at that time. |
| `invalidValue (400)`      | `invalidTitle`                    | The [liveBroadcast resource](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource) did not specify a valid value for the `snippet.title` property. The property's value must be between 1 and 100 characters long.                                                                                          |
| `limitExceeded`           | `userBroadcastsExceedLimit`       | The user has created too many live or scheduled broadcasts and must stop or delete some.                                                                                                                                                                                                                                          |
| `rateLimitExceeded`       | `userRequestsExceedRateLimit`     | The user has sent too many requests in a given timeframe.                                                                                                                                                                                                                                                                         |
| `required (400)`          | `privacyStatusRequired`           | The [liveBroadcast resource](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource) must specify a privacy status. See [valid `privacyStatus` values](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#privacyStatus).                                                                      |
| `required (400)`          | `scheduledEndTimeRequired`        | The [liveBroadcast resource](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource) must specify the `snippet.scheduledEndTime` property.                                                                                                                                                                    |
| `required (400)`          | `scheduledStartTimeRequired`      | The [liveBroadcast resource](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource) must specify the `snippet.scheduledStartTime` property.                                                                                                                                                                  |
| `required (400)`          | `titleRequired`                   | The [liveBroadcast resource](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource) must specify the `snippet.title` property.                                                                                                                                                                               |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.