# Source: https://developers.google.com/youtube/v3/docs/videos/update.md.txt

# Videos: update

The API now supports the ability to mark your [channel](https://developers.google.com/youtube/v3/docs/channels) or [videos](https://developers.google.com/youtube/v3/docs/videos) as "made for kids." In addition, `channel` and `video` resources also now contain a property that identifies the "made for kids" status of that channel or video. The YouTube API Services Terms of Service and Developer Policies were also updated on 10 January 2020. For more information, see the revision histories for the [YouTube Data API Service](https://developers.google.com/youtube/v3/revision_history) and the [YouTube API Services Terms of Service](https://developers.google.com/youtube/terms/revision-history).
Updates a video's metadata.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/videos/update#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
PUT https://www.googleapis.com/youtube/v3/videos
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/guides/authentication)).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtubepartner`    |
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ||
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |||
| `part`                   | `string` The **part** parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include. Note that this method will override the existing values for all of the mutable properties that are contained in any parts that the parameter value specifies. For example, a video's privacy setting is contained in the `status` part. As such, if your request is updating a private video, and the request's `part` parameter value includes the `status` part, the video's privacy setting will be updated to whatever value the request body specifies. If the request body does not specify a value, the existing privacy setting will be removed and the video will revert to the default privacy setting. In addition, not all parts contain properties that can be set when inserting or updating a video. For example, the `statistics` object encapsulates statistics that YouTube calculates for a video and does not contain values that you can set or modify. If the parameter value specifies a `part` that does not contain mutable values, that `part` will still be included in the API response. The following list contains the `part` names that you can include in the parameter value: - `contentDetails` - `fileDetails` - `id` - `liveStreamingDetails` - `localizations` - `paidProductPlacementDetails` - `player` - `processingDetails` - `recordingDetails` - `snippet` - `statistics` - `status` - `suggestions` - `topicDetails` |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |||
| `onBehalfOfContentOwner` | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwner** parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### Request body

Provide a [video resource](https://developers.google.com/youtube/v3/docs/videos#resource) in the request body. For that resource:

- You must specify a value for these properties:

  - `id`
  - `snippet.title` -- This property is only required if the request updates the `video` resource's `snippet`.
  - `snippet.categoryId` -- This property is only required if the request updates the `video` resource's `snippet`.
- You can set values for these properties:

  - `snippet.categoryId`
  - `snippet.defaultLanguage`
  - `snippet.description`
  - `snippet.tags[]`
  - `snippet.title`
  - `status.embeddable`
  - `status.license`
  - `status.privacyStatus`
  - `status.publicStatsViewable`
  - `status.publishAt` -- If you set a value for this property, you must also set the `status.privacyStatus` property to `private`.
  - `status.selfDeclaredMadeForKids`
  - `status.containsSyntheticMedia`
  - `recordingDetails.recordingDate`
  - `localizations.(key)`
  - `localizations.(key).title`
  - `localizations.(key).description`

  If you are submitting an update request, and your request does not specify a value for a property that already has a value, the property's existing value will be deleted.

## Response

If successful, this method returns a [video resource](https://developers.google.com/youtube/v3/docs/videos#resource) in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. See the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|     Error type     |              Error detail               |                                                                                                                              Description                                                                                                                               |
|--------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)` | `defaultLanguageNotSet`                 | The API request is trying to add localized video details without specifying the default language of the video details.                                                                                                                                                 |
| `badRequest (400)` | `invalidCategoryId`                     | The `snippet.categoryId` property specifies an invalid category ID. Use the [videoCategories.list](https://developers.google.com/youtube/v3/docs/videoCategories/list) method to retrieve supported categories.                                                        |
| `badRequest (400)` | `invalidDefaultBroadcastPrivacySetting` | The request attempts to set an invalid privacy setting for the default broadcast.                                                                                                                                                                                      |
| `badRequest (400)` | `invalidDescription`                    | The request metadata specifies an invalid video description.                                                                                                                                                                                                           |
| `badRequest (400)` | `invalidPublishAt`                      | The request metadata specifies an invalid scheduled publishing time.                                                                                                                                                                                                   |
| `badRequest (400)` | `invalidRecordingDetails`               | The `recordingDetails` object in the request metadata specifies invalid recording details.                                                                                                                                                                             |
| `badRequest (400)` | `invalidTags`                           | The request metadata specifies invalid video keywords.                                                                                                                                                                                                                 |
| `badRequest (400)` | `invalidTitle`                          | The request metadata specifies an invalid or empty video title.                                                                                                                                                                                                        |
| `badRequest (400)` | `invalidVideoMetadata`                  | The request metadata is invalid.                                                                                                                                                                                                                                       |
| `forbidden (403)`  | `forbidden`                             |                                                                                                                                                                                                                                                                        |
| `forbidden (403)`  | `forbiddenEmbedSetting`                 | The request attempts to set an invalid embed setting for the video. Note that some channels may not have permission to offer embedded players for live streams. See the [YouTube Help Center](https://support.google.com/youtube/answer/2474026) for more information. |
| `forbidden (403)`  | `forbiddenLicenseSetting`               | The request attempts to set an invalid license for the video.                                                                                                                                                                                                          |
| `forbidden (403)`  | `forbiddenPrivacySetting`               | The request attempts to set an invalid privacy setting for the video.                                                                                                                                                                                                  |
| `notFound (404)`   | `videoNotFound`                         | The video that you are trying to update cannot be found. Check the value of the `id` field in the request body to ensure that it is correct.                                                                                                                           |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.