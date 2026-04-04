# Source: https://developers.google.com/youtube/v3/live/revision_history.md.txt

# YouTube Live Streaming API - Revision History

This page lists YouTube Live Streaming API changes and documentation updates. [Subscribe to this changelog](https://developers.google.com/static/youtube/v3/live/feeds/livestreaming-api-revision-history.xml). [![Subscribe](https://developers.google.com/static/analytics/images/rss-o16.png)](https://developers.google.com/static/youtube/v3/live/feeds/livestreaming-api-revision-history.xml)

### July 14th, 2025

The description of the [liveChatMessages.streamList](https://developers.google.com/youtube/v3/live/docs/liveChatMessages/streamList) method has been updated to provide guidance on the streamList API usages.

### October 9, 2023

For reference only, you can find which Sticker IDs relate to which Super Stickers in this
[CSV file](https://youtube.googleapis.com/super_stickers/sticker_ids_to_urls.csv).
The definitions of the `liveChatMessage` resource's
[snippet.superStickerDetails.superStickerMetadata.stickerId](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.superStickerDetails.superStickerMetadata.stickerId)
property and the `superChatEvent` resource's
[snippet.superStickerMetadata.stickerId](https://developers.google.com/youtube/v3/live/docs/superChatEvents#snippet.superStickerMetadata.stickerId)
property have both been updated to reflect this information.

### September 15, 2023

The API now supports a new way of inserting ads into live broadcasts. In addition to
[liveCuepoints](https://developers.google.com/youtube/v3/live/docs/liveCuepoints), which let you
manually insert ad breaks into a broadcast, YouTube now supports a feature to automatically
insert midroll ad breaks into a broadcast at fixed intervals.

If the broadcast owner enables automated ads, they can view the following aspects of
ad behavior:

- the length of the interval between midroll ad breaks.
- the scheduling strategy for ad cuepoints. Cuepoints can be inserted concurrently for all viewers or the timing of the cuepoints can vary from viewer to viewer. The latter strategy enables YouTube to schedule cuepoints at an increased rate that allows viewers to receive cuepoints when they are eligible to do so.
- a period during which midroll ads are not shown; for this feature, the broadcast owner specifies that midroll ads insertion is paused until a particular time.

The documentation reflects the following API changes to support this feature:

- The `liveBroadcast` resource now contains a [monetizationDetails](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#monetizationDetails) object. The object's fields indicate whether automatic ad insertion is enabled for the broadcast and specify additional information for scheduling cuepoints.
- The `liveBroadcast.list` method's [part](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list#part) parameter supports the value `monetizationDetails`.
- The [update](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/update) method can be used to pause midroll ads insertion for a certain period for a live broadcast. The documentation also now identifies several errors that can occur when updating the monetization details for a live broadcast.

### August 1, 2023

This update contains the following changes:

- The [liveBroadcasts.update](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/update) method no longer requires values to be specified for these fields:

  - `snippet.title`
  - `status.privacyStatus`

  Omitting these fields from the request will leave them unchanged.

### November 1, 2022

- The new [liveBroadcasts.cuepoint](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/cuepoint)
  method enables any channel owner running a live broadcast on YouTube to insert cuepoints into
  that broadcast, which can trigger ad breaks. This method replaces the
  `liveCuepoints.insert` method, which only enabled YouTube content partners to
  insert cuepoints into live broadcasts.

  Several guides have been updated to reflect the availability of this new method.
- **Note:** This is a deprecation announcement.

  The `liveCuepoints.insert` method is now deprecated. Support for the
  `liveCuepoints.insert` method will be removed on or after May 1, 2023. API
  users should update their applications to call the `liveBroadcasts.cuepoint`
  method instead.
- Documentation for the `liveBroadcasts.control` method has been removed. A
  deprecation notice for that method was posted in September 2020.

### October 1, 2022

This update contains the following changes:

- The [liveBroadcasts.update](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/update) method no long requires values to be specified for these fields:

  - `contentDetails.enableContentEncryption`
  - `contentDetails.enableDvr`
  - `contentDetails.enableEmbed`
  - `contentDetails.recordFromStart`
  - `contentDetails.startWithSlate`

  Omitting these fields from the request will leave them unchanged.
- Removed documentation for obsolete `liveBroadcast` fields:

  - `contentDetails.enableContentEncryption`
  - `contentDetails.startWithSlate`

### April 1, 2022

This update contains the following changes:

- The [snippet.type](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.type) property now supports two new values:

  - `membershipGiftingEvent`
  - `giftMembershipReceivedEvent`
- The `liveChatMessage` resource's new [snippet.membershipGiftingDetails](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.membershipGiftingDetails) property and its children contain information about the Membership Gifting event. Similarly, the new [snippet.giftMembershipReceivedDetails](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.giftMembershipReceivedDetails) property and its children contain information about the Gift Membership Received event.

### September 15, 2021

This update contains the following changes:

- The [snippet.type](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.type) property now supports two new values:

  - `newSponsorEvent`
  - `memberMilestoneChatEvent`
- The `liveChatMessage` resource's new [snippet.memberMilestoneChatDetails](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.memberMilestoneChatDetails) property and its children contain information about the Member Milestone Chat event. Similarly, the new [snippet.newSponsorDetails](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.newSponsorDetails) property and its children contain information about the New Sponsor event.

### December 1, 2020

The API's [liveBroadcasts.transition](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/transition)
method supports a new `403` (`Forbidden`) error, which indicates that the user
has sent too many requests within a given timeframe. The error reason is `userRequestsExceedRateLimit`.

### September 21, 2020

- The definition of the `liveBroadcast` resource's
  [status.madeForKids](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#status.madeForKids)
  property has been updated to clarify that the property is read-only. This does not reflect a
  change in API functionality.

  To designate a live broadcast as being child-directed, set the
  [status.selfDeclaredMadeForKids](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#status.selfDeclaredMadeForKids)
  property to `true` when calling the
  [liveBroadcasts.insert](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/insert)
  method to create the broadcast.
- **Note:** This change includes a deprecation announcement and an update to
  a prior deprecation announcement.

  The [liveBroadcasts.control](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/control)
  method will be deprecated on or after 1 October 2020. After that date, all calls to this
  method will return a forbidden (403) error, and the method will later be completely removed.
  Clients can still implement their own slating by adding an overlay to the video sent to
  YouTube's ingestion servers.

  The deprecation date for the [deprecation announcement
  made on 16 April 2020](https://developers.google.com/youtube/v3/live/revision_history#release_notes_04_16_2020), which was originally scheduled for 1 September 2020, has been
  pushed back and will now happen on or after 1 October 2020. Thus, the features included in
  that deprecation announcement and the `liveBroadcasts.control` method will all be
  deprecated at the same time.

### July 17, 2020

**Note:** This is an update to a prior deprecation announcement.

The [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams) resource's
`cdn.format` field, which was deprecated in April 2016, will no longer be supported
as of August 17, 2020. Requests still using that field will fail as of that date.

If your code still uses the `cdn.format` field, it must be updated to specify the
frame rate and resolution separately, using the
[cdn.frameRate](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.frameRate) and
[cdn.resolution](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.resolution)
properties.

### July 6, 2020

The [Delivering Live YouTube Content via HLS](https://developers.google.com/youtube/v3/live/guides/hls-ingestion)
guide has been updated with a few changes:

- The recommended duration for a Media Segment has been updated to one to four seconds.
- A new section explains how to [obtain
  an HLS Ingestion URL from YouTube Creator Studio](https://developers.google.com/youtube/v3/live/guides/hls-ingestion#obtaining_an_hls_ingestion_url_from_youtube_creator_studio).
- Instructions for formatting the `file` parameter value have been moved to the new [Completing the HLS Ingestion URL](https://developers.google.com/youtube/v3/live/guides/hls-ingestion#completing_the_hls_ingestion_url) section. These instructions apply regardless of whether the HLS ingestion URL is obtained from the YouTube API or YouTube Creator Studio.

In addition, the new [ingestion
protocol comparison](https://developers.google.com/youtube/v3/live/guides/ingestion-protocol-comparison) lists the ingestion protocols that YouTube supports, the codecs supported
for each protocol, and additional information regarding appropriate use cases for each protocol.

### April 16, 2020

This update includes a new property and a deprecation announcement:

- The `liveBroadcast` resource now supports the
  [contentDetails.enableAutoStop](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableAutoStop)
  property. The property indicates whether a broadcast should stop automatically around one
  minute after the channel owner stops streaming video on the bound video stream.

  The [life of a broadcast](https://developers.google.com/youtube/v3/live/life-of-a-broadcast) document has been
  updated to explain how the step-by-step process of creating and managing a live YouTube event
  changes if you set the
  [contentDetails.enableAutoStart](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableAutoStart)
  or [contentDetails.enableAutoStop](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableAutoStop)
  properties to `true`.
- **Note:** This is a deprecation announcement. These changes will go into
  effect on or after September 1, 2020. The actual date that the changes take effect is referred
  to below as the deprecation date.

  This update explains a potentially breaking change. It affects API client applications that use
  channels' default `liveStream` and `liveBroadcast` resources to stream live
  content on YouTube. Specifically, the [broadcast ID](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#id)
  and [stream ID](https://developers.google.com/youtube/v3/live/docs/liveStreams#id) associated with the persistent
  broadcast and stream will no longer function to start new broadcasts.

  Your application will be affected if any of the following are true:
  - It checks the value of the `liveBroadcast` resource's [isDefaultBroadcast](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#snippet.isDefaultBroadcast) property. This property will not be returned after the deprecation date.
  - It checks the value of the `liveStream` resource's [isDefaultStream](https://developers.google.com/youtube/v3/live/docs/liveStreams#snippet.isDefaultStream) property. This property will not be returned after the deprecation date.
  - It calls the [liveBroadcasts.list](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list) method and sets the [broadcastType](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list#broadcastType) parameter value to `persistent` or `all`. This parameter will be deprecated as part of these changes. As of the deprecation date:
    - If the `broadcastType` parameter value is `persistent`, then the `liveBroadcasts.list` method will not return any results.
    - If the `broadcastType` parameter value is `all`, then the `liveBroadcasts.list` method will not return persistent broadcasts that existed before that time.

  As background, for the past few years, YouTube has automatically created a default stream and a
  default broadcast for a channel when that channel was enabled for live streaming. The default
  stream existed indefinitely, did not have a start or end time associated with it, and could not be
  deleted. Similarly, the default broadcast was considered *persistent*. It always existed and
  was not bound to a particular event.

  As of the deprecation date:
  - YouTube will no longer create default streams and broadcasts. Instead of relying on the default resources, API clients need to be able to create and manage `liveBroadcast` and `liveStream` resources and to bind those resources together.
  - If a channel's default broadcast and default stream are actively live, meaning the channel is using them for a live broadcast at the time the deprecation goes into effect, the ongoing broadcast will not be affected. However, after that broadcast ends, the channel will not be able to use the default broadcast and default stream again.
  - If a channel's default broadcast and default stream are not actively live, then after the deprecation goes into effect, YouTube will ignore attempts to use those resources to broadcast video.

  If your application is affected, please refer to the following documents, which will help you to
  update your application so that it still works as expected following this change:
  - A new [migration
    guide](https://developers.google.com/youtube/v3/live/guides/migration-guide-default-broadcasts) tries to explain the steps that developers might need to address in API clients that currently use default broadcasts and streams.
  - The [Life of a broadcast](https://developers.google.com/youtube/v3/live/life-of-a-broadcast) guide takes you through a step-by-step process that explains how to create and manage a live event on YouTube. Each step explains the API calls or other things that you need to do to complete a specific action, and your application will need to follow that process when YouTube stops supporting default streams and broadcasts.

### March 31, 2020

**Note:** This is a deprecation announcement.

The [sponsor](https://developers.google.com/youtube/v3/live/docs/sponsors) resource and
[sponsors.list](https://developers.google.com/youtube/v3/live/docs/sponsors/list) method have been
deprecated and replaced by the [member](https://developers.google.com/youtube/v3/live/docs/members)
resource and [members.list](https://developers.google.com/youtube/v3/docs/members/list) method.

The `sponsors.list` method will no longer be supported on or after September 30, 2020.
API clients should update calls to the `sponsors.list` method to use the
`members.list` method instead. Please see the
[YouTube Data API revision history](https://developers.google.com/youtube/v3/revision_history) for more information
about the new resource.

### March 11, 2020

The [Ingestion endpoint](https://developers.google.com/youtube/v3/live/guides/hls-ingestion#ingestion_endpoint)
section of the **Delivering Live YouTube Content via HLS** guide has been updated to
clarify the process that an encoder should use to complete the `file=` parameter value
when forming the primary and backup ingestion URLs.

### February 4, 2020

The [Delivering Live YouTube Content via HLS](https://developers.google.com/youtube/v3/live/guides/hls-ingestion)
guide has been updated to note that `DELETE` requests are optional and that YouTube's
HLS endpoint ignores them. For performance reasons, YouTube recommends clients do not send
`DELETE` requests.

### January 10, 2020

The API now supports the ability to identify child-directed content, which YouTube calls
"made for kids." [Learn more about
"made for kids" content](https://support.google.com/youtube/answer/9528076) in the YouTube Help Center.

- The [liveBroadcast](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts) resource supports two new properties to enable content creators and viewers to identify "made for kids" content:
  - The [selfDeclaredMadeForKids](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#status.selfDeclaredMadeForKids) property enables content creators to specify whether a live broadcast is child-directed content. This property can be set when [creating a broadcast](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/insert) via the `liveBroadcasts.insert` method. Note that this property is only included in API responses that contain `liveBroadcast` resources if the channel owner authorized the API request.
  - The [madeForKids](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#status.madeForKids) property enables any API user to retrieve the "made for kids" status of a broadcast. For example, the status might be determined based on the value of the `selfDeclaredMadeForKids` property. See the [YouTube Help Center](https://support.google.com/youtube/answer/9527654) for more information about setting the audience for your channel, videos, or broadcasts.
- In the YouTube Data API, the [channel](https://developers.google.com/youtube/v3/docs/channels) resource also supports new `selfDeclaredMadeForKids` and `madeForKids` properties.

We have also updated the YouTube API Services Terms of Service and Developer Policies. Please
see the [YouTube API Services Terms of Service - Revision
History](https://developers.google.com/youtube/terms/revision-history) for more information. The changes to the YouTube API Services Terms of Service and
Developer Policies will take effect on January 10, 2020 Pacific Time.

### August 20, 2019

The [Requirements](https://developers.google.com/youtube/v3/live/guides/hls-ingestion#requirements) section of the
**Delivering Live YouTube Content via HLS** guide has been updated with two changes:

- It explains that it is a best practice to include both acknowledged segments and outstanding segments in each Media Playlist. This practice makes it less likely for a segment to be skipped if a Media Playlist is lost on the server side. For example, you could include up to two acknowledged segments and up to five outstanding segments in each Media Playlist.
- It is now a requirement to send a Media Playlist for every Media Segment. This enables the server to recover quickly if a Media Playlist is lost. This practice was previously listed as a recommendation.

### June 28, 2019

YouTube now supports HLS ingestion. Accordingly, the `liveStream` resource's [ingestionType](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.ingestionType) property supports the new value `hls` to identify streams ingested to YouTube using HLS.

The new [Delivering Live YouTube Content via HLS](https://developers.google.com/youtube/v3/live/guides/hls-ingestion) guide provides guidelines for using HLS to stream live content to YouTube from an encoder. The guide aims to help encoder vendors add HLS delivery support to their products.

### April 4, 2019

This update contains the following changes:

- The API reference documentation has been updated to better explain common use cases for each method and to provide dynamic, high-quality code samples through the APIs Explorer widget. See the [liveBroadcasts.list](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list) method's documentation for an example. There are now two new elements on pages that describe API methods:

  - The APIs Explorer widget lets you select authorization scopes, enter sample parameter and property values, and then send actual API requests and see actual API responses. The widget also offers a fullscreen view that shows complete code samples, which dynamically update to use the scopes and values that you have entered.

  - The **Common use cases** section describes one or more common use cases for the method explained on the page. For example, you could call the `liveBroadcasts.list` method to retrieve data about a specific broadcast or to retrieve data about the current user's broadcasts.

    You can use links in that section to populate the APIs Explorer with sample values for your use case or to open the fullscreen APIs Explorer with those values already populated. These changes aim to make it easier for you to see code samples that are directly applicable to the use case that you're trying to implement in your own application.

  Code samples are currently supported for Java, JavaScript, PHP, Python, and curl.
- The [code samples](https://developers.google.com/youtube/v3/live/code_samples) page has also a new UI that offers all of the same features described above. Using that tool, you can explore use cases for different methods, load values into the APIs Explorer, and open the fullscreen APIs Explorer to get code samples in Java, JavaScript, PHP, and Python.

  In conjunction with this change, the pages that previously listed available code samples for Java, PHP, and Python have been removed.

### February 25, 2019

The documentation of the [liveChatMessage](https://developers.google.com/youtube/v3/live/docs/liveChatMessages) and [superChatEvent](https://developers.google.com/youtube/v3/live/docs/superChatEvents) resources has been updated to reflect the fact that both resources can now contain information about Super Stickers. Super Stickers are a type of Super Chat message that displays an image. Like other Super Chats, a Super Sticker message is purchased by a fan during a YouTube live stream.

- In a `liveChatMessage` resource, the [snippet.type](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.type) property is now set to `superStickerEvent` to indicate that the resource contains information about a Super Sticker. In that case, the resource also contains the [snippet.superStickerDetails](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.superStickerDetails) object, which contains additional information about the Super Sticker.
- In a `superChatEvent` resource, the boolean [snippet.isSuperStickerEvent](https://developers.google.com/youtube/v3/live/docs/superChatEvents#snippet.isSuperStickerEvent) indicates whether the Super Chat message is also a Super Sticker. If so, then the [snippet.superStickerMetadata](https://developers.google.com/youtube/v3/live/docs/superChatEvents#snippet.superStickerMetadata) object contains additional details about the Super Sticker.

### April 5, 2018

The description of the [superChatEvents.list](https://developers.google.com/youtube/v3/live/docs/superChatEvents/list) method has been updated to reflect the fact that the API response no longer contains `fanFundingEvents`, which were deprecated in early 2017.

### April 3, 2017

New [Java code samples](https://developers.google.com/youtube/v3/live/code_samples/java) have been added that show how to [list](https://developers.google.com/youtube/v3/live/code_samples/java#list_live_chat_messages), [insert](https://developers.google.com/youtube/v3/live/code_samples/java#insert_a_live_chat_message), and [delete](https://developers.google.com/youtube/v3/live/code_samples/java#delete_a_live_chat_message) live chat messages. The samples call the following methods:

- [liveBroadcasts.list](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list#examples)
- [liveChatMessages.list](https://developers.google.com/youtube/v3/live/docs/liveChatMessages/list#examples)
- [liveChatMessages.insert](https://developers.google.com/youtube/v3/live/docs/liveChatMessages/insert#examples)
- [liveChatMessages.delete](https://developers.google.com/youtube/v3/live/docs/liveChatMessages/delete#examples)

### February 13, 2017

This update contains the following changes:

- **Updates to existing resources and methods**

  - The [liveCuepoints.insert](https://developers.google.com/youtube/v3/live/docs/liveCuepoints/insert) method has been updated to reflect the fact that the [onBehalfOfContentOwner](https://developers.google.com/youtube/v3/live/docs/liveCuepoints/insert#onBehalfOfContentOwner) parameter is currently required. In addition, the method's description has been updated to note that calls to that method must be authorized by an account associated with a YouTube Content Owner.

### February 9, 2017

This update contains the following changes:

- **Updates to existing resources and methods**

  - The `superChatEvents.list` method's new [hl](https://developers.google.com/youtube/v3/live/docs/superChatEvents/list#hl) parameter lets you specify that the [snippet.displayString](https://developers.google.com/youtube/v3/live/docs/superChatEvents#snippet.displayString) property value should be formatted according to the conventions of a particular language. That property's definition has also been updated accordingly.

    The parameter value must be a language code included in the list returned by the [i18nLanguages.list](https://developers.google.com/youtube/v3/docs/i18nLanguages/list) method. The default value is `en`, which means that the default behavior is to format display strings as they would be used in English. For example, by default, a string is formatted as `$1.00` rather than `$1,00`.

### February 1, 2017

This update contains the following changes:

- **New resources and methods**

  - The new [superChatEvent](https://developers.google.com/youtube/v3/live/docs/superChatEvents) resource represents a Super Chat message purchased by a fan during a YouTube live stream. In the YouTube live chat stream, Super Chats stand out from other messages in two ways:

    <br />

    - Super Chats are highlighted with a color.
    - Super Chats stay pinned in the ticker for a set period of time.

    <br />

    The color of the Super Chat, the period of time it stays pinned in the ticker, and the maximum message length are all determined by the purchase amount. The [YouTube Help Center](https://support.google.com/youtube/answer/7277005) has more information about Super Chats.

    The API supports a method to [list](https://developers.google.com/youtube/v3/live/docs/superChatEvents/list) Super Chat events for a channel's live streams in the previous 30 days. That method also returns data about Fan Funding events ([fanFundingEvents](https://developers.google.com/youtube/v3/live/docs/fanFundingEvents)) from the channel's last live stream.
- **Updates to existing resources and methods**

  - The [snippet.type](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.type) property now supports the `superChatEvent` value, which indicates that the resource describes a Super Chat.

    In addition, the `liveChatMessage` resource's new [snippet.superChatDetails](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.superChatDetails) property and its children contain information about the Super Chat event.
  - The `liveStream` resource's [cdn.resolution](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.resolution) property now supports the value `2160p`.

- **New and updated errors**

  - The API supports the following new errors:

    |                                                                                                                                                                                                                                                                                                      Error details                                                                                                                                                                                                                                                                                                      ||
    |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [liveBroadcasts.insert](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/insert), [liveBroadcasts.update](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/update) | The `liveBroadcasts.insert` and `liveBroadcasts.update` methods return `400` (`Bad Request`) errors to indicate that the `liveBroadcast` resource being inserted or updated contains an invalid value for either the `contentDetails.enableEmbed` property or the `contentDetails.projection` property. The error reasons for the two new errors are `invalidEmbedSetting` and `invalidProjection`, respectively. |

### January 12, 2017

**Note:** This is a deprecation announcement.

In conjunction with the release of the new [Super Chat](https://youtube.googleblog.com/2017/01/can-we-chat-hello-super-chat.html) feature, YouTube has deprecated the Fan Funding feature, and the Fan Funding API will be turned off on February 28, 2017. As of that date:

- The [liveChatMessages.list](https://developers.google.com/youtube/v3/live/docs/liveChatMessages/list) method will no longer return messages with a [snippet.type](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.type) of `fanFundingEvent`. Similarly, `liveChatMessage` resources will no longer contain the [snippet.fanFundingEventDetails](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.fanFundingEventDetails) object.
- The [fanFundingEvents.list](https://developers.google.com/youtube/v3/live/docs/fanFundingEvents/list) method will no longer return data.

<br />

### August 11, 2016

This update contains the following changes:

- The newly published YouTube API Services Terms of Service ("the Updated Terms"), discussed in detail on the [YouTube Engineering and Developers Blog](http://youtube-eng.blogspot.com/), provides a rich set of updates to the current Terms of Service. In addition to the [Updated Terms](https://developers.google.com/youtube/terms/api-services-terms-of-service), which will go into effect as of February 10, 2017, this update includes several supporting documents to help explain the policies that developers must follow.

  The full set of new documents is described in the [revision history for the Updated Terms](https://developers.google.com/youtube/terms/revision-history). In addition, future changes to the Updated Terms or to those supporting documents will also be explained in that revision history. You can subscribe to an RSS feed listing changes in that revision history from a link in that document.

## May 20, 2016

YouTube now supports DASH ingestion. Accordingly, the `liveStream` resource's [ingestionType](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.ingestionType) property supports the new value `dash` to identify streams ingested to YouTube using DASH.

The new [Delivering Live YouTube Content via DASH](https://developers.google.com/youtube/v3/live/guides/encoding-with-dash) guide provides guidelines for using the DASH Delivery format to stream live data on YouTube from an encoder. It is intended to help encoder vendors add DASH delivery support to their products.

## April 18, 2016

This update contains the following changes:

- **Updates to existing resources and methods**

  - **`liveStream` resource updates**
    - YouTube now supports streams with 1440p resolution at either 30 or 60 frames per second.

      In addition, the `liveStream` resource contains new properties for specifying the frame rate and resolution of the inbound video data:

      |                                                                                                         Properties                                                                                                          ||
      |-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
      | [cdn.frameRate](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.frameRate)   | The frame rate of the inbound video data. Valid values are `30fps` and `60fps`.                                            |
      | [cdn.resolution](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.resolution) | The resolution of the inbound video data. Valid property values are: `1440p`, `1080p`, `720p`, `480p`, `360p`, and `240p`. |

    - In accordance with the introduction of the `liveStream` resource's `cdn.frameRate` and `cdn.resolution` properties, the resource's `cdn.format` is now deprecated. The `cdn.format` property specifies resolution and frame rate in a single value.

      We encourage you to transition to the newly supported fields. In the meantime, `cdn.format` continues to work. In addition, requests to insert live streams currently succeed as long as you specify values for either the `cdn.format` property *or* the `cdn.frameRate` and `cdn.resolution` properties. If you provide values for all three properties, the API might return an error if the values are not in agreement.

      Note that even though the `cdn.format` property is deprecated, it does now support two new values, `1440p` and `1440p_hfr`, to reflect the API's support for 1440p streams at either 30 or 60 frames per second.
  - **`liveBroadcast` resource updates**
    - The `liveBroadcast` resource contains the following new properties:

      |                                                                                                                                                                                         Properties                                                                                                                                                                                         ||
      |------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
      | [contentDetails.boundStreamLastUpdateTimeMs](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.boundStreamLastUpdateTimeMs) | The date and time that the live stream referenced by the broadcast's [contentDetails.boundStreamId](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.boundStreamId) property was last updated. |
      | [contentDetails.projection](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.projection)                                   | The broadcast's projection format. The property's default value is `rectangular`. Valid values for the property are `360` and `rectangular`.                                                                                   |

    - The definition of the `liveBroadcast` resource's [statistics.totalChatCount](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#statistics.totalChatCount) property has been updated to note that the property value only shows up if the broadcast has at least one chat message.

  - **`liveChatMessage` resource updates**
    - The [snippet.type](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.type) property supports two new values -- `messageDeletedEvent` and `userBannedEvent` -- that correspond to the new properties described in the following bullet point. The definition of the [snippet.authorChannelId](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.authorChannelId) property has also been updated to explain what the property value identifies for these new message types.

    - The `liveChatMessage` resource contains the following new properties:

      |                                                                                                                                                                                                                                                              Properties                                                                                                                                                                                                                                                              ||
      |------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
      | [snippet.messageDeletedDetails](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.messageDeletedDetails) | This object contains information about a message that was deleted by a chat moderator. The object is only present if the `snippet.type` property value is `messageDeletedEvent`.                                                                                                                                                                                                                 |
      | [snippet.userBannedDetails](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.userBannedDetails)         | This object contains information about a user who has been banned from participating in the chat. The object also contains information about the ban itself, namely whether the ban is permanent or temporary. If the ban is temporary, one of the object's properties specifies the duration of the ban. This object is only present if the `snippet.type` property value is `userBannedEvent`. |

- **New and updated errors**

  - The API supports the following new errors:

    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Error details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ||
    |-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [liveBroadcasts.bind](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/bind) | The `liveBroadcasts.bind` method returns a `403` (`Forbidden`) error to indicate that the user has sent too many requests within a given timeframe. The error reason is `userRequestsExceedRateLimit`. The `liveBroadcasts.insert` and `liveBroadcasts.update` methods already support the same error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
    | [liveStreams.insert](https://developers.google.com/youtube/v3/live/docs/liveStreams/insert)   | The `liveStreams.insert` method supports four new `400` (`Bad Request`) errors that identify an invalid property value in the `liveStream` resource that the request tried to insert. The following list identifies the error reasons and the properties with which they are associated: - `invalidFormat`: `cdn.format` - `invalidFrameRate`: [cdn.frameRate](https://developers.google.com/youtube/v3/live/docs/liveStreams/cdn.frameRate) - `invalidIngestionType`: [cdn.ingestionType](https://developers.google.com/youtube/v3/live/docs/liveStreams/cdn.ingestionType) - `invalidResolution`: [cdn.resolution](https://developers.google.com/youtube/v3/live/docs/liveStreams/cdn.resolution)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
    | [liveStreams.insert](https://developers.google.com/youtube/v3/live/docs/liveStreams/insert)   | The `liveStreams.insert` method supports two new `400` (`Bad Request`) errors, each of which indicates that a required value is not present in the `liveStream` resource that the request tried to insert. The following list identifies the error reasons and the properties with which they are associated: - `frameRateRequired`: [cdn.frameRate](https://developers.google.com/youtube/v3/live/docs/liveStreams/cdn.frameRate) - `resolutionRequired`: [cdn.resolution](https://developers.google.com/youtube/v3/live/docs/liveStreams/cdn.resolution) More specifically, when you insert a `liveStream` resource, you must specify a value for either the `cdn.format` property or for the [cdn.frameRate](https://developers.google.com/youtube/v3/live/docs/liveStreams/cdn.frameRate) *and* [cdn.resolution](https://developers.google.com/youtube/v3/live/docs/liveStreams/cdn.resolution) properties. - The API returns a `formatRequired` error if you do not specify a value for any of the three properties. - The API returns a `frameRateRequired` error if you specify a value for `cdn.resolution` but not `cdn.frameRate`. - The API returns a `resolutionRequired` error if you specify a value for `cdn.frameRate` but not `cdn.resolution`. |
    | [liveStreams.update](https://developers.google.com/youtube/v3/live/docs/liveStreams/update)   | The `liveStreams.update` method returns a `403` (`Forbidden`) error if the request tries to modify the value of any of the following non-mutable properties: - `cdn.format` - [cdn.frameRate](https://developers.google.com/youtube/v3/live/docs/liveStreams/cdn.frameRate) - [cdn.ingestionType](https://developers.google.com/youtube/v3/live/docs/liveStreams/cdn.ingestionType) - [cdn.resolution](https://developers.google.com/youtube/v3/live/docs/liveStreams/cdn.resolution) The `reason` in the error response is `liveStreamModificationNotAllowed`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## December 18, 2015

European Union (EU) laws require that certain disclosures must be given to and consents obtained from end users in the EU. Therefore, for end users in the European Union, you must comply with the [EU User Consent Policy](http://www.google.com/about/company/user-consent-policy.html). We have added a notice of this requirement in our [YouTube API Terms of Service](https://developers.google.com/youtube/terms#notices-to-users).

## December 17, 2015

This update contains the following changes:

- **New resources and methods**

  - The API supports several new resources to support chat functionality for live broadcasts. YouTube supports live chat functionality during active live broadcasts, and these resources and their methods support retrieval of chat messages as well as administrative functions for the chat.

    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Resources                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ||
    |---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [liveChatMessage](https://developers.google.com/youtube/v3/live/docs/liveChatMessages)      | This resource represents a message in a YouTube live chat. YouTube supports several types of messages, including text messages and Fan Funding events. Some message types identify a particular phase of the chat, such as the beginning of a sponsors-only period or the end of the chat. The API supports methods to list, insert, and delete live chat messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
    | [liveChatModerators](https://developers.google.com/youtube/v3/live/docs/liveChatModerators) | This resource identifies a chat moderator. Moderators can perform some administrative functions, such as banning users from the chat or removing messages. The API supports methods to list, insert, and delete live chat moderators.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
    | [liveChatBans](https://developers.google.com/youtube/v3/live/docs/liveChatBans)             | This resource identifies a user who is banned from posting messages to a particular live chat. Bans can be temporary or permanent. The API supports methods to insert and delete live chat bans.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
    | [fanFundingEvents](https://developers.google.com/youtube/v3/live/docs/fanFundingEvents)     | This resource represents a Fan Funding event on a YouTube channel. Fan Funding provides a way for viewers to voluntarily support YouTube Creators with one-time monetary support. The API's [fanFundingEvents.list](https://developers.google.com/youtube/v3/live/docs/fanFundingEvents/list) method lists a channel's Fan Funding events. Fan Funding events that are initiated through a live chat during a live broadcast owned by the channel also trigger a [`fanFundingEvent` message](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.type) to the broadcast's live chat. Learn more about Fan Funding in the [YouTube Help Center](https://support.google.com/youtube/answer/6052077).                                                                                                                                         |
    | [sponsors](https://developers.google.com/youtube/v3/live/docs/sponsors)                     | The [sponsor](https://developers.google.com/youtube/v3/live/docs/sponsors) resource identifies a sponsor of a YouTube channel. A sponsor pays a monthly fee to a channel. A badge shows up next to the sponsor's messages in the channel's live chats and sponsors can also participate in live chats exclusively for the channel's sponsors, if those occur. The API's [sponsors.list](https://developers.google.com/youtube/v3/live/docs/sponsors/list) method lists a channel's sponsors. When users sign up to sponsor a channel during a live broadcast owned by that channel, the API also adds a [`newSponsorEvent` message](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#snippet.type) to the broadcast's live chat. Learn more about sponsorships in the [YouTube Help Center](https://support.google.com/youtube/answer/6304294). |

- **Updates to existing resources and methods**

  - The `liveBroadcast` resource contains the following new properties:

    |                                                                                                                                                                                                                                                                                                                                                                                                      Properties                                                                                                                                                                                                                                                                                                                                                                                                       ||
    |----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [snippet.liveChatId](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#snippet.liveChatId)                                   | The ID for the broadcast's YouTube live chat. With this ID, you can use the [liveChatMessage](https://developers.google.com/youtube/v3/live/docs/liveChatMessages) resource's methods to retrieve, insert, or delete chat messages. You can also add or remove chat moderators, ban users from participating in live chats, or remove existing bans.                                                                                                                                                                                                                                                                                                                    |
    | [contentDetails.closedCaptionsType](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.closedCaptionsType)     | **Note: This property *replaces* the `contentDetails.enableClosedCaptions` property.** This property indicates whether closed captioning is enabled for your broadcast and, if so, what type of closed captions you are providing: - `closedCaptionsDisabled`: Closed captions are disabled for the live broadcast. - `closedCaptionsHttpPost`: You will send captions, via HTTP POST, to an [ingestion URL](https://developers.google.com/youtube/v3/live/docs/liveStreams#contentDetails.closedCaptionsIngestionUrl) associated with your live stream. - `closedCaptionsEmbedded`: Captions will be encoded in the video stream using EIA-608 and/or CEA-708 formats. |
    | [contentDetails.enableClosedCaptions](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableClosedCaptions) | This property has been deprecated as of December 17, 2015. Use the [contentDetails.closedCaptionsType](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.closedCaptionsType) property instead. For API clients that are already using this property: - Setting the property value to `true` is equivalent to setting the `contentDetails.closedCaptionsType` property to `closedCaptionsHttpPost`. - Setting the property value to `false` is equivalent to setting the `contentDetails.closedCaptionsType` property to `closedCaptionsDisabled`.                                                                                        |

  - The `liveBroadcasts.list` method's new [broadcastType](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list#broadcastType) parameter lets you filter an API response to include event broadcasts, persistent broadcasts, or all broadcasts.

    A persistent broadcast is one that always exists and is not tied to a particular event. Specifically, a channel's [default broadcast](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#snippet.isDefaultBroadcast) is a persistent broadcast, and it is accessible via the [Live Dashboard](https://www.youtube.com/live_dashboard) in the YouTube Creator Studio. The channel's other broadcasts are event broadcasts.
- The `liveStream` resource's [status.healthStatus.configurationIssues[].type](https://developers.google.com/youtube/v3/live/docs/liveStreams#status.healthStatus.configurationIssues[].type) field reports the following new health status errors:

  |                                                                                 Errors                                                                                 ||
  |------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
  | `audioTooManyChannels` | The audio has more than two channels, but only one (mono) or two (stereo) channels are supported. Please correct the number of audio channels. |
  | `frameRateHigh`        | The current framerate is too high. Please set the framerate to `%(framerate)s` fps or less.                                                    |

- The publication date of the previous documentation update was corrected.

- **New and updated errors**

  - In addition to errors defined for the new resources listed above, the API supports the following new errors:

    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Error details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ||
    |---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [liveBroadcasts.update](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/update) | |--------------------|------------------------------------------------------------------------------------------------------------------------------| | HTTP Response Code | `forbidden (403)`                                                                                                            | | Reason             | `closedCaptionsTypeModificationNotAllowed`                                                                                   | | Description        | The `contentDetails.closedCaptionsType` value can only be modified when the broadcast is in the `created` or `ready` status. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | [liveBroadcasts.update](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/update) | |--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | HTTP Response Code | `invalidValue (400)`                                                                                                                                                                                                                                                                                                                                         | | Reason             | `invalidEnableClosedCaptions`                                                                                                                                                                                                                                                                                                                                | | Description        | In the [liveBroadcast resource](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource), the value of the `contentDetails.enableClosedCaptions` property is incompatible with the value of the `contentDetails.closedCaptionType` setting. Modify the resource to only include one of the two properties, and then resubmit the request. | |

## August 19, 2015

This update contains the following changes:

- **New resources and methods**

  - **Note:** Documentation for the `liveChat` resource and its methods is confidential and only visible to select YouTube partners.

    The new [liveChat](https://developers.google.com/youtube/v3/live/docs/liveChats) resource contains a comment posted during a live broadcast on YouTube. The API supports two methods for this resource:

    |                                                              Methods                                                              ||
    |-----------------------------------------------------------------------------------------|------------------------------------------|
    | [liveChats.list](https://developers.google.com/youtube/v3/live/docs/liveChats/list)     | List live chat messages for a broadcast. |
    | [liveChats.insert](https://developers.google.com/youtube/v3/live/docs/liveChats/insert) | Create a new chat message.               |

    Live chat messages can only be retrieved and posted while a broadcast is live.
- **Updates to existing resources and methods**

  - The `liveStream` resource contains the following new properties:

    |                                                                                                                                                                                                                                                                                                                          Properties                                                                                                                                                                                                                                                                                                                          ||
    |-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [snippet.isDefaultStream](https://developers.google.com/youtube/v3/live/docs/liveStreams#snippet.isDefaultStream)     | Indicates whether this stream is the default stream for the channel. A channel's default stream exists indefinitely, does not have a start or end time associated with it, and cannot be deleted. See the property's definition for more information about how default streams work.                                                                                                                                                                                                                                                  |
    | [status.healthStatus](https://developers.google.com/youtube/v3/live/docs/liveStreams#status.healthStatus)             | This object contains information that could be used to identify, diagnose and resolve streaming problems. The object contains a number of child properties to help you evaluate the health of a live video stream. In particular, the `status.healthStatus.configurationIssues[]` object lists issues affecting a video stream. A new document, [Configuration Issues for LiveStream Resources](https://developers.google.com/youtube/v3/live/docs/liveStreams/health_status_messages), lists all of the issues that the API reports. |
    | [contentDetails.isReusable](https://developers.google.com/youtube/v3/live/docs/liveStreams#contentDetails.isReusable) | Indicates whether the stream is reusable, which means that it can be bound to multiple broadcasts. It is common for broadcasters to reuse the same stream for many different broadcasts if those broadcasts occur at different times.                                                                                                                                                                                                                                                                                                 |

  - The `liveBroadcast` resource contains the following new properties:

    |                                                                                                                                                                                                                                                                                Properties                                                                                                                                                                                                                                                                                 ||
    |--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [snippet.isDefaultBroadcast](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#snippet.isDefaultBroadcast)           | Indicates whether this broadcast is the default broadcast for the channel. When a YouTube channel is enabled for live streaming, YouTube creates a default stream and a default broadcast for the channel. The stream defines how the channel owner sends live video to YouTube, and the broadcast is how viewers can see the default stream. See the property's definition for more information about how default broadcasts work. |
    | [contentDetails.enableLowLatency](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableLowLatency) | Indicates whether this broadcast should be encoded for low-latency streaming. A low-latency stream can reduce the amount of time it takes for video to be visible to users watching a broadcast, though it can also impact the resolution for viewers of the stream.                                                                                                                                                                |
    | [statistics.totalChatCount](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#statistics.totalChatCount)             | The total number of live chat messages associated with the broadcast. The property and its value are present if the broadcast is visible to the user and has the live chat feature enabled. Note that this property will not specify a value after the broadcast ends. So, this property would not identify the number of chat messages for an archived video of a completed live broadcast.                                        |

- **New and updated errors**

  - In addition to errors defined for the new [liveChat](https://developers.google.com/youtube/v3/live/docs/liveChats) resource, the API supports the following new error:

    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Error details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ||
    |---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [liveStreams.update](https://developers.google.com/youtube/v3/live/docs/liveStreams/update) | |--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | HTTP Response Code | `forbidden (403)`                                                                                                                                                                                                                | | Reason             | `liveStreamModificationNotAllowed`                                                                                                                                                                                               | | Description        | The API does not allow you to change a reusable stream to be non-reusable, or vice versa. For more information, see [Understanding Broadcasts and Streams](https://developers.google.com/youtube/v3/live/broadcasts-and-streams) | |

## May 21, 2015

This update contains the following changes:

- YouTube now supports live video streaming at 60 frames per second (fps), which means smoother playback for gaming and other fast-action videos. When you start a live stream on YouTube at 60fps, YouTube also makes the stream available in 30fps on devices where high-frame-rate viewing is not yet available.

  The `liveStream` resource's `cdn.format` property supports two new values for this feature: `720p_hfr` and `1080p_hfr`.

  See the [YouTube Creators Blog](http://youtubecreator.blogspot.com/2015/05/60fps-live-streaming-on-youtube-in-html5.html) for more information about this feature.

## August 21, 2014

This update contains the following changes:

- The definition of the `liveBroadcasts.control` method's [walltime](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/control#walltime) parameter has been updated to note that the property value is specified in ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sssZ`).

- The API now supports the following errors:

  |        Error type         |         Error detail          |                                                                                                                                                                                                                              Description                                                                                                                                                                                                                              |
  |---------------------------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | `insufficientPermissions` | `liveStreamingNotEnabled`     | All methods for the [liveBroadcast](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts) and [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams) resources return this error if the user that authorized the API request has not been enabled to stream live video on YouTube. Details explaining why the user cannot stream live video may be available in the user's channel settings at <https://www.youtube.com/features>. |
  | `rateLimitExceeded`       | `userRequestsExceedRateLimit` | The [liveBroadcasts.insert](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/insert) and [liveStreams.insert](https://developers.google.com/youtube/v3/live/docs/liveStreams/insert) methods both return this error to indicate that the user has sent too many requests within a given timeframe.                                                                                                                                                   |

## May 2, 2014

This update contains the following changes:

- The descriptions of the [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams) resource and of the [liveBroadcasts.bind](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/bind) method have been updated to note that a broadcast can only be bound to one video stream, but a video stream can be bound to more than one broadcast. This change is solely a correction to the documentation; the underlying API functionality has not changed.

- The `liveBroadcast` resource's [contentDetails.monitorStream.enableMonitorStream](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.monitorStream.enableMonitorStream) property has been updated to explain that if the property's value is `true`, then you must transition your broadcast to the `testing` state before you can transition it to the `live` state. (If the property's value is `false`, your broadcast cannot have a `testing` stage, so you can transition the broadcast directly to the `live` state.

- The `liveCuepoint` resource's [settings.offsetTimeMs](https://developers.google.com/youtube/v3/live/docs/liveCuepoints#settings.offsetTimeMs) property has been updated to note that you should not specify a value for the property if your broadcast does not have a monitor stream.

- All of the methods for the `liveBroadcast` and `liveStream` resources now support the `onBehalfOfContentOwner` and `onBehalfOfContentOwnerChannel` parameters. These parameters allow you to use the same authorization credentials to complete API requests for different channels associated with the same content owner.

- The [liveCuepoints.insert](https://developers.google.com/youtube/v3/live/docs/liveCuepoints/insert) method's documentation has been updated to note that you can set a value for the [settings.walltime](https://developers.google.com/youtube/v3/live/docs/liveCuepoints#settings.walltime) property when calling that method.

- The [error documentation](https://developers.google.com/youtube/v3/live/docs/errors) now specifies the HTTP response code for each error type.

- The API now supports the following error:

  |        Error type         |      Error detail       |                                                                                                                                                                                                                                                                                  Description                                                                                                                                                                                                                                                                                   |
  |---------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | `insufficientPermissions` | `livePermissionBlocked` | The [liveBroadcasts.insert](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/insert), [liveBroadcasts.transition](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/transition), and [liveStreams.insert](https://developers.google.com/youtube/v3/live/docs/liveStreams/insert) methods return this error if the user that authorized the request is unable to stream live video on YouTube. Details explaining why the user cannot stream live video may be available in the user's channel settings at <https://www.youtube.com/features>. |

- The `liveBroadcasts.insert` method's `invalidScheduledStartTime` error has been updated to clarify that the scheduled start time must be close enough to the current date that a broadcast could be reliably scheduled at that time.

## December 13, 2013

This update contains the following changes:

- The `liveBroadcast` resource's new [status.recordingStatus](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#status.recordingStatus) property identifies the broadcast's current status.

- The `liveBroadcast` resource's new [contentDetails.enableClosedCaptions](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableClosedCaptions) property indicates whether closed captions can be ingested for the broadcast. The property value can be set when you insert or update a broadcast, but it cannot be updated once the broadcast is in the `testing` or `live` state. If you set this property to `true`, then the `liveStream` resource that is bound to the broadcast will specify the ingestion URL to use for the broadcast's closed captions.

- The `liveBroadcast` resource's [snippet.scheduledEndTime](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#snippet.scheduledEndTime) property now supports broadcasts that are scheduled to continue indefinitely. With this change, the property is no longer required in `liveBroadcasts.insert` and `liveBroadcasts.update` requests.  

  If you retrieve a `liveBroadcast` resource that does not specify a value for this property, then the broadcast is scheduled to continue indefinitely. Similarly, if you call the [liveBroadcasts.insert](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/insert#request_body) or [liveBroadcasts.update](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/update#request_body) method and do not specify a value for this property, the broadcast will be scheduled to continue indefinitely.

- The `liveBroadcast` resource's [contentDetails.recordFromStart](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.recordFromStart) property, which already had a default value of `true`, can now only be set to `false` if the broadcasting channel is allowed to disable recordings for live broadcasts.

  If your channel does not have permission to disable recordings, and you attempt to insert a broadcast with the `recordFromStart` property set to `false`, the API will return a `Forbidden` error. In addition, if your channel does not have that permission and you attempt to update a broadcast to set the `recordFromStart` property to `false`, the API will return a `modificationNotAllowed` error.
- The `liveBroadcast` resource no longer contains an `enableArchive` property, which had been mentioned in the descriptions of the [contentDetails.enableDvr](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableDvr) and [contentDetails.enableEmbed](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableEmbed) properties.

- The list of valid values for the `liveBroadcast` resource's `status.lifeCycleStatus` property has been updated to include a description of each status.

- The `liveCuepoint` resource's new [settings.walltime](https://developers.google.com/youtube/v3/live/docs/liveCuepoints#settings.walltime) property specifies the date and time at which the cuepoint should be inserted. The API returns an error if a request tries to insert a cuepoint that specifies a value for this property and for the `settings.offsetTimeMs` property.

- The new `contentDetails` object in a `liveStream` resource contains information about the stream. Currently, the object's only property is [contentDetails.closedCaptionsIngestionUrl](https://developers.google.com/youtube/v3/live/docs/liveStreams#contentDetails.closedCaptionsIngestionUrl), which specifies the ingestion URL for closed captions associated with the video stream.

- The list of valid values for the `liveStream` resource's `status.streamStatus` property has been updated to include a description of each status.

- The [liveBroadcasts.control](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/control) method's new `walltime` parameter lets you specify the date and time when a slate change will occur. The API returns an error if a request specifies a value for this parameter and for the `offsetTimeMs` parameter.

- In the API response to a `liveBroadcasts.list` request, the value of the [kind](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list#kind) property has changed from `youtube#liveBroadcastList` to `youtube#liveBroadcastListResponse`.

- In the API response to a `liveStreams.list` request, the value of the [kind](https://developers.google.com/youtube/v3/live/docs/liveStreams/list#kind) property has changed from `youtube#liveStreamList` to `youtube#liveStreamListResponse`.

- The `eventId` property has been deprecated from both the `liveBroadcastListResponse` and the `liveStreamListResponse`.

- The API supports the following new errors:

  |   Error type   |                 Error detail                 |                                                                                                                                                          Description                                                                                                                                                           |
  |----------------|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | `invalidValue` | `conflictingTimeFields`                      | The [liveBroadcasts.control](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/control) method returns this error if your request specifies values for the `offsetTimeMs` and `walltime` parameters. A request can either omit both parameters or specify a value for one of the two parameters.               |
  | `invalidValue` | `invalidWalltime`                            | The [liveBroadcasts.control](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/control) method returns this error if the `walltime` parameter's value is invalid.                                                                                                                                              |
  | `forbidden`    | `enableClosedCaptionsModificationNotAllowed` | The [liveBroadcasts.update](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/update) method returns this error if you attempt to update the `contentDetails.enableClosedCaptions` value and the broadcast's status is not `created` or `ready`.                                                               |
  | `invalidValue` | `conflictingTimeFields`                      | The [liveCuepoints.insert](https://developers.google.com/youtube/v3/live/docs/liveCuepoints/insert) method returns this error if your request specifies values for the `settings.offsetTimeMs` and `settings.walltime` properties. A request can either omit both properties or specify a value for one of the two properties. |

  In addition, the [liveStreams.update](https://developers.google.com/youtube/v3/live/docs/liveStreams/update) method no longer supports a `cdnRequired` error similar to the one that the [liveStreams.insert](https://developers.google.com/youtube/v3/live/docs/liveStreams/insert) method supports.

## May 10, 2013

This update contains the following changes:

- YouTube no longer identifies experimental API features and services. Instead, we now provide a list of [YouTube APIs that are subject to the deprecation policy](https://developers.google.com/youtube/youtube-api-list).

## May 2, 2013

This update contains the following changes:

- The new [liveBroadcasts.control](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/control) method enables you to toggle the display settings for a slate that displays in the broadcast stream for a broadcast that is already in progress. If your broadcast stream is delayed, you can also use this method to specify a time offset when the requested slate change will occur.

- The definitions of the following properties have been updated to explain that the property values must be set if you update a `liveBroadcast` resource's `contentDetails` part:

  <br />

  - [contentDetails.monitorStream.enableMonitorStream](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.monitorStream.enableMonitorStream)
  - [contentDetails.monitorStream.broadcastStreamDelayMs](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.monitorStream.broadcastStreamDelayMs)
  - [contentDetails.enableDvr](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableDvr)
  - [contentDetails.enableContentEncryption](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableContentEncryption)
  - [contentDetails.enableEmbed](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableEmbed)
  - [contentDetails.recordFromStart](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.recordFromStart)
  - [contentDetails.startWithSlate](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.startWithSlate)

  <br />

- The `liveStream` resource's [status.streamStatus](https://developers.google.com/youtube/v3/live/docs/liveStreams#status.streamStatus) no longer supports the value `deleted` as a possible stream status.

- The information that the API returns for many [error messages](https://developers.google.com/youtube/v3/live/docs/errors) has been revised to better explain why particular errors occurred. The API also supports several new errors.

## March 27, 2013

This update contains the following changes:

- The following properties have changed in the `liveBroadcast` resource:

  <br />

  - The `startWithSlateCuepoint` property has been renamed to [startWithSlate](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#startWithSlate).
  - The `enableArchive` property has been renamed to [recordFromStart](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#recordFromStart).
  - The `slateSettings` object has been deprecated and removed from the documentation. Error messages related to the `slateSettings` object or its properties have also been removed. Finally, the "Displaying Slates" section of the [Getting started](https://developers.google.com/youtube/v3/live/getting-started) guide has been removed.

  <br />

- The API no longer supports the ability to insert in-stream slates using the [liveCuepoints.insert](https://developers.google.com/youtube/v3/live/docs/liveCuepoints/insert) method. The following documents have been updated to reflect this change:

  - The [index page](https://developers.google.com/youtube/v3/live), [Getting started](https://developers.google.com/youtube/v3/live/getting-started) guide, and [Life of a broadcast](https://developers.google.com/youtube/v3/live/life-of-a-broadcast) tutorial no longer mention this functionality.

  - The `liveCuepoint` resource's [settings.cueType](https://developers.google.com/youtube/v3/live/docs/liveCuepoints#settings.cueType) property no longer supports `slate` as a property value. (The only supported value is `ad`.

  - The `liveCuepoint` resource's `settings.eventState` property has been deprecated and removed from the documentation.

## March 18, 2013

This update contains the following changes:

- All of the API's error messages have been updated to more clearly explain possible errors and, when possible, offer guidance about how to fix them.

- The API may now return several new errors. The list below identifies the error and the API method that might return that error:

  <br />

  - [liveBroadcasts.insert](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/insert#youtube.liveBroadcasts.insert-invalidValue-invalidLiveBroadcast-snippet.scheduled_end_time_ms) -- A broadcast's scheduled end time must be after its scheduled start time.
  - [liveBroadcasts.insert](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/insert#youtube.liveBroadcasts.insert-invalidValue-invalidLiveBroadcast-status.privacy_status) -- The broadcast specifies an invalid privacy status.
  - [liveBroadcasts.update](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/update#youtube.liveBroadcasts.update-invalidValue-invalidLiveBroadcast-content_details.wants_archive) -- The resource does not contain or does not set a value for the `contentDetails.enableArchive` property.
  - [liveBroadcasts.update](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/update#youtube.liveBroadcasts.update-invalidValue-invalidLiveBroadcast-content_details.enable_content_encryption) -- The resource does not contain or does not set a value for the `contentDetails.enableContentEncryption` property.
  - [liveBroadcasts.update](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/update#youtube.liveBroadcasts.update-invalidValue-invalidLiveBroadcast-content_details.wants_dvr) -- The resource does not contain or does not set a value for the `contentDetails.enableDvr` property.
  - [liveStreams.insert](https://developers.google.com/youtube/v3/live/docs/liveStreams/insert#youtube.liveStreams.insert-invalidValue-invalidLiveStream-snippet.title) -- The snippet title must be between 1 and 128 characters long.
  - [liveStreams.update](https://developers.google.com/youtube/v3/live/docs/liveStreams/update#youtube.liveStreams.update-invalidValue-invalidLiveStream-snippet.title) -- The resource does not contain or does not set a value for the `snippet.title` property.

  <br />

- The [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource) resource documentation has been updated to reflect that multicast and WebM are not supported ingestion methods as previously indicated. The list of formats for the `cdn.format` property has been updated accordingly, and the `cdn.multicastIngestionInfo` object and its child properties have been removed from the resource's documentation. In addition, `http` has been removed from the list of supported [cdn.ingestionType](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.ingestionType) values.