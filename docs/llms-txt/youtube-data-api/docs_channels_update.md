# Source: https://developers.google.com/youtube/v3/docs/channels/update.md.txt

# Channels: update

The API now supports the ability to mark your [channel](https://developers.google.com/youtube/v3/docs/channels) or [videos](https://developers.google.com/youtube/v3/docs/videos) as "made for kids." In addition, `channel` and `video` resources also now contain a property that identifies the "made for kids" status of that channel or video. The YouTube API Services Terms of Service and Developer Policies were also updated on 10 January 2020. For more information, see the revision histories for the [YouTube Data API Service](https://developers.google.com/youtube/v3/revision_history) and the [YouTube API Services Terms of Service](https://developers.google.com/youtube/terms/revision-history).
Updates a channel's metadata. Note that this method only supports updates to the `channel` resource's `brandingSettings`, `invideoPromotion`, and `localizations` objects and their child properties.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/channels/update#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
PUT https://www.googleapis.com/youtube/v3/channels
```

### Authorization

This request requires authorization with at least one of the following scopes. To read more about authentication and authorization, see [Implementing OAuth 2.0 authorization](https://developers.google.com/youtube/v3/guides/authentication).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtubepartner`    |
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                                                                                                                                                                                      Parameters                                                                                                                                                                                                                                                                                                                                                                      ||
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |||
| `part`                   | `string` The **part** parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include. The API only allows the parameter value to be set to either `brandingSettings`, `invideoPromotion`, or `localizations`. (You can only update any one of those parts with a single request.) Note that this method overrides the existing values for all of the mutable properties that are contained in the part that the parameter value specifies.                                                                                                                                                                   |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |||
| `onBehalfOfContentOwner` | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). The **onBehalfOfContentOwner** parameter indicates that the authenticated user is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with needs to be linked to the specified YouTube content owner. |

### Request body

Provide a [channel](https://developers.google.com/youtube/v3/docs/channels#resource) resource in the request body.
For that resource:

- You must specify a value for these properties:

  - `id`
- You can set values for these properties:

  - `brandingSettings.channel.country`
  - `brandingSettings.channel.description`
  - `brandingSettings.channel.defaultLanguage`
  - `brandingSettings.channel.keywords`
  - `brandingSettings.channel.trackingAnalyticsAccountId`
  - `brandingSettings.channel.unsubscribedTrailer`
  - `localizations.(key)`
  - `localizations.(key).title`
  - `localizations.(key).description`
  - `status.selfDeclaredMadeForKids`

  If you are submitting an update request, and your request does not specify a value for a property that already has a value, the property's existing value will be deleted.

## Response

If successful, this method returns a [channel](https://developers.google.com/youtube/v3/docs/channels#resource) resource in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Fore more details, see [YouTube Data API - Errors](https://developers.google.com/youtube/v3/docs/errors).

|     Error type     |         Error detail          |                                                                                                                                                                                       Description                                                                                                                                                                                       |
|--------------------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)` | `brandingValidationError`     | One of the values in the `brandingSettings` object failed validation. Use the [channels.list](https://developers.google.com/youtube/v3/docs/channels/list) method to retrieve the existing settings for the channel, and update the property values following the guidelines in the [channels](https://developers.google.com/youtube/v3/docs/channels#resource) resource documentation. |
| `badRequest (400)` | `channelTitleUpdateForbidden` | When updating a channel's `brandingSettings part`, you must set the `brandingSettings.channel.title` property's value to the channel's current title or omit the property. The API returns an error if you change the property's value.                                                                                                                                                 |
| `badRequest (400)` | `defaultLanguageNotSetError`  | The `defaultLanguage` must be set to update `localizations`.                                                                                                                                                                                                                                                                                                                            |
| `badRequest (400)` | `invalidBrandingOption`       | One of the branding settings that you specified does not exist. Use the [channels.list](https://developers.google.com/youtube/v3/docs/channels/list) method to retrieve valid values and make sure to update them following the guidelines in the [channels](https://developers.google.com/youtube/v3/docs/channels#resource) resource documentation.                                   |
| `badRequest (400)` | `invalidCustomMessage`        | The request metadata specifies an invalid custom message. Check the value of the [invideoPromotion.items[].customMessage](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].customMessage) property in the resource that the request sent.                                                                                                                |
| `badRequest (400)` | `invalidDuration`             | The request metadata specifies an invalid duration in the invideoPromotion part.                                                                                                                                                                                                                                                                                                        |
| `badRequest (400)` | `invalidDuration`             | The request metadata specifies an invalid position type for determining how the promoted item is positioned in the video player. Check the value of the [invideoPromotion.position.type](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.position.type) property in the resource that the request sent.                                                         |
| `badRequest (400)` | `invalidRecentlyUploadedBy`   | The request metadata specifies an invalid channel ID. Check the value of the [invideoPromotion.items[].id.recentlyUploadedBy](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].id.recentlyUploadedBy) property in the resource that the request sent.                                                                                                    |
| `badRequest (400)` | `invalidTimingOffset`         | The request metadata specifies an invalid timing offset in the invideoPromotion part.                                                                                                                                                                                                                                                                                                   |
| `badRequest (400)` | `invalidTimingOffset`         | The request metadata specifies an invalid timing offset for determining when the promoted item should be displayed in the video player. Check the value of the [invideoPromotion.timing.offsetMs](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.timing.offsetMs) property in the resource that the request sent.                                              |
| `badRequest (400)` | `invalidTimingType`           | The request metadata specifies an invalid timing method for determining when the promoted item should be displayed in the video player. Check the value of the [invideoPromotion.timing.type](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.timing.type) property in the resource that the request sent.                                                      |
| `badRequest (400)` | `localizationValidationError` | One of the values in the localizations object failed validation. Use the [channels.list](https://developers.google.com/youtube/v3/docs/channels/list) method to retrieve valid values and make sure to update them following the guidelines in [the channels resource documentation.](https://developers.google.com/youtube/v3/docs/channels#resource)                                  |
| `badRequest (400)` | `tooManyPromotedItems`        | Number of allowed promoted items exceeded in the invideoPromotion part.                                                                                                                                                                                                                                                                                                                 |
| `forbidden (403)`  | `channelForbidden`            | The channel specified in the `id` parameter does not support the request or the request is not properly authorized.                                                                                                                                                                                                                                                                     |
| `forbidden (403)`  | `promotedVideoNotAllowed`     | The channel that the API request is attempting to update cannot be found. Check the value of the `id` property in the `channel` resource that the request sent to ensure that the channel ID is correct.                                                                                                                                                                                |
| `forbidden (403)`  | `websiteLinkNotAllowed`       | The specified website URL is not allowed.                                                                                                                                                                                                                                                                                                                                               |
| `notFound (404)`   | `channelNotFound`             | The channel specified in the `id` parameter cannot be found.                                                                                                                                                                                                                                                                                                                            |
| `notFound (404)`   | `channelNotFound`             | The channel specified by the `id` parameter cannot be found or does not have branding options.                                                                                                                                                                                                                                                                                          |
| `notFound (404)`   | `unknownChannelId`            | The specified channel ID was not found.                                                                                                                                                                                                                                                                                                                                                 |
| `notFound (404)`   | `unknownChannelId`            | The specified recentlyUploadedBy channel ID was not found.                                                                                                                                                                                                                                                                                                                              |
| `notFound (404)`   | `unknownVideoId`              | The [video ID](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].videoId) specified as a promoted item cannot be found.                                                                                                                                                                                                                                   |
| `required (400)`   | `requiredItemIdType`          | The request metadata must specify an item type in the invideoPromotion part.                                                                                                                                                                                                                                                                                                            |
| `required (400)`   | `requiredItemId`              | The request metadata must specify an item id the invideoPromotion part.                                                                                                                                                                                                                                                                                                                 |
| `required (400)`   | `requiredTimingOffset`        | The request metadata must specify a default timing offset so that YouTube can determine when to display the promoted item. Set the value of the [invideoPromotion.defaultTiming.offsetMs](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.defaultTiming.offsetMs) property in the resource that the request sends.                                              |
| `required (400)`   | `requiredTimingOffset`        | The request metadata must specify a timing offset so that YouTube can determine when to display the promoted item. Set the value of the [invideoPromotion.timing.offsetMs](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.timing.offsetMs) property in the resource that the request sends.                                                                    |
| `required (400)`   | `requiredTimingType`          | The request metadata must specify a timing method so that YouTube can determine when to display the promoted item. Set the value of the [invideoPromotion.defaultTiming.type](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.defaultTiming.type) property in the resource that the request sends.                                                              |
| `required (400)`   | `requiredTimingType`          | The request metadata must specify a timing method so that YouTube can determine when to display the promoted item. Set the value of the [invideoPromotion.timing.type](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.timing.type) property in the resource that the request sends.                                                                            |
| `required (400)`   | `requiredTiming`              | The request metadata must specify a timing for each item in the `invideoPromotion` part.                                                                                                                                                                                                                                                                                                |
| `required (400)`   | `requiredVideoId`             | The request metadata must specify a [video ID](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].videoId) to identify the promoted item.                                                                                                                                                                                                                  |
| `required (400)`   | `requiredWebsiteUrl`          | The request metadata must specify a website URL in the invideoPromotion part. Set the value of the [invideoPromotion.items[].id.websiteUrl](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].id.websiteUrl) property in the resource that the request sends.                                                                                             |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.