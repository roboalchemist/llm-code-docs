# Source: https://developers.google.com/youtube/v3/revision_history.md.txt

# Revision History

This page lists YouTube Data API (v3) changes and documentation updates. [Subscribe to this changelog](https://developers.google.com/static/youtube/v3/feeds/data-api-revision-history.xml). [![Subscribe](https://developers.google.com/static/analytics/images/rss-o16.png)](https://developers.google.com/static/youtube/v3/feeds/data-api-revision-history.xml)

### July 10, 2025

As of July 21, 2025, YouTube will adjust the content that is returned by the [`video.list`](https://developers.google.com/youtube/v3/guides/implementation/videos) method's `mostPopular` chart. In the past, the `mostPopular` chart reflected the videos featured on the Trending Now list. Now, the `mostPopular` chart will feature videos from the Trending Music, Movies, and Gaming charts. This API change is in tandem with the deprecation of YouTube's [Trending page](https://support.google.com/youtube/thread/356702168).

### March 26, 2025

Starting March 31, 2025, YouTube will change how views for Shorts are counted. In the past, for Shorts, a view was counted after a Short was played for a certain number of seconds. Now, views will count the number of times your Short starts to play or replay, with no minimum watch time requirement.
[Learn more](https://yt.be/help/sviews)

Starting March 31, 2025, the following fields in the Data API will return the view count for Shorts as per this change:

- `channels.statistics.viewCount`
- `videos.statistics.viewCount`

### October 30, 2024

The API now supports the ability to identify videos that contain realistic **Altered or
Synthetic** (**A/S** ) content. Learn more about
[YouTube
policies related to A/S content](https://blog.youtube/inside-youtube/our-approach-to-responsible-ai-innovation/).

Examples of A/S content include videos that:

- Make a real person appear to say or do something they didn't actually say or do
- Alter footage of a real event or place
- Generate a realistic-looking scene that did not actually occur

To indicate whether a video contains A/S content, set the
[status.containsSyntheticMedia](https://developers.google.com/youtube/v3/docs/videos#status.containsSyntheticMedia)
property. This property can be set when calling the
[videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) or
[videos.update](https://developers.google.com/youtube/v3/docs/videos/update) methods. If set, the
property is returned in the
[video](https://developers.google.com/youtube/v3/docs/videos#status) resource.

### April 30, 2024

**Note:** This is a deprecation announcement.

This update contains the following changes:

The API no longer supports the ability to insert or retrieve channel discussions. This change is consistent with the functionality supported on the YouTube website, which does not support posting comments to channels.

### March 13, 2024

**Note:** This is a deprecation announcement.

This update contains the following changes:

The `sync` parameter for the
[captions.insert](https://developers.google.com/youtube/v3/docs/captions/insert#sync) and
[captions.update](https://developers.google.com/youtube/v3/docs/captions/update#sync) methods
has been deprecated. YouTube will stop supporting the
parameter as of April 12, 2024.

As a result of this change, developers must include timing information when inserting or
updating caption tracks or the upload will fail.

### March 12, 2024

This update contains the following changes:

Documentation for the `captions` resource has been updated to note that the maximum allowed length for the [snippet.name](https://developers.google.com/youtube/v3/docs/captions#snippet.name)
field is 150 characters. The API returns a [nameTooLong](https://developers.google.com/youtube/v3/docs/captions/insert#youtube.captions.insert-invalidValue-nameTooLong)
error if the track name is longer than that.

### March 7, 2024

**Note:** This is a deprecation announcement.

The [channel](https://developers.google.com/youtube/v3/docs/channels) resource property
`brandingSettings.channel.moderateComments` has been deprecated. YouTube will stop
supporting the parameter as of March 7, 2024.

### January 31, 2024

This update contains the following changes:

The `channels.list` method's new [forHandle](https://developers.google.com/youtube/v3/docs/channels/list#forHandle)
parameter enables you to retrieve information about a channel by specifying its YouTube handle.

### November 09, 2023

All references to the `videoId` resource under [Comments](https://developers.google.com/youtube/v3/docs/comments#resource-representation)
have been removed as the `videoId` resource is not being returned using an API call.

### September 12, 2023

**Note:** This is a deprecation announcement.

The [comments.markAsSpam](https://developers.google.com/youtube/v3/docs/comments/markAsSpam) method
has been deprecated for several years. This method is already unsupported on YouTube and is no
longer supported through the API.

A deprecation notice has been added to all of the documents referencing the
`comments.markAsSpam` method.

### August 22, 2023

The [search.list](https://developers.google.com/youtube/v3/docs/search/list) method now supports the
[videoPaidProductPlacement](https://developers.google.com/youtube/v3/docs/search/list#videoPaidProductPlacement)
parameter. This parameter enables you to filter search results to include only videos that the
creator has denoted as having a paid promotion.

### August 18, 2023

The definition of the `video` resource's
[liveStreamingDetails.concurrentViewers](https://developers.google.com/youtube/v3/docs/videos#liveStreamingDetails.concurrentViewers)
has been updated to note that the concurrent viewer counts that the YouTube Data API returns might
differ from the processed, despammed concurrent viewer counts available through YouTube
Analytics. The
[YouTube Help Center](https://support.google.com/youtube/answer/2853833)
provides more information about live streaming metrics.

### August 7, 2023

As [announced on June 12, 2023](https://developers.google.com/youtube/v3/revision_history#release_notes_06_12_2023), the
[search.list](https://developers.google.com/youtube/v3/docs/search/list) method's
`relatedToVideoId` parameter has been deprecated. That parameter is no longer
supported, and references to the parameter have been removed from the API documentation.

### June 28, 2023

The [thumbnails.set](https://developers.google.com/youtube/v3/docs/thumbnails/set#errors) method now supports the
`uploadRateLimitExceeded` error, which indicates that the channel has uploaded too many
thumbnails during the past 24 hours and should try again later.

### June 12, 2023

**Note:** This is a deprecation announcement.

The [search.list](https://developers.google.com/youtube/v3/docs/search/list#params) method's
`relatedToVideoId` parameter has been deprecated. YouTube will stop supporting the
parameter as of August 7, 2023.

At this time, a deprecation notice has been added to the `search.list` method's
documentation. This parameter will be fully removed from the `search.list` documentation
on or after August 7, 2023.

In addition, an example demonstrating how to retrieve related videos has been
removed from the [API implementation guide](https://developers.google.com/youtube/v3/guides/implementation/videos).

### August 22, 2022

Corrected type annotations for [video.statistics](https://developers.google.com/youtube/v3/docs/videos#statistics)
fields to string from unsigned long.

### August 5, 2022

YouTube has changed the way that caption IDs are generated and, as part of that change, is
assigning new caption IDs to all caption tracks. This change might be a backward-incompatible
change for applications that store
[caption_id](https://developers.google.com/youtube/v3/docs/captions#id) values, though it will not
affect applications that do not store
[caption_id](https://developers.google.com/youtube/v3/docs/captions#id) values.

Between now and December 1, 2022, the
[captions.list](https://developers.google.com/youtube/v3/docs/captions/list),
[captions.update](https://developers.google.com/youtube/v3/docs/captions/update),
[captions.download](https://developers.google.com/youtube/v3/docs/captions/download), and
and [captions.delete](https://developers.google.com/youtube/v3/docs/captions/delete) methods will
support both the old and new caption track IDs. However, on or after December 1, 2022, YouTube
will stop supporting the old caption track IDs. At that time, calling any of those API methods
with an old caption track ID will result in a
[captionNotFound](https://developers.google.com/youtube/v3/docs/captions/list#errors) error.

To prepare for this change, you should plan to fully replace all stored caption track data
between now and December 1, 2022. This means that for any video for which you store caption track
data, you should delete the currently stored data, then call the
[captions.list](https://developers.google.com/youtube/v3/docs/captions/list) method to retrieve the
current set of caption tracks for the video and store the data in the API response as you would
normally.

### July 12, 2022

The YouTube API Services Terms of Service has been updated. Please
see the [YouTube API Services Terms of Service - Revision
History](https://developers.google.com/youtube/terms/revision-history) for more information.

### April 27, 2022

The [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) method description has been updated to note that the maximum file size for uploaded videos has increased from 128GB to 256GB.

### April 8, 2022

The `subscriptions.list` method's
[myRecentSubscribers](https://developers.google.com/youtube/v3/docs/subscriptions/list#myRecentSubscribers)
and [mySubscribers](https://developers.google.com/youtube/v3/docs/subscriptions/list#mySubscribers) parameter definitions
have both been updated to note that the maximum number of subscribers returned by the API might be limited.
This change represents a documentation correction and not a change in API behavior.

### December 15, 2021

As announced on [November 18, 2021](https://developers.google.com/youtube/v3/revision_history#release_notes_11_18_2021), in conjunction with
[changes to make video dislike
counts private across the entire YouTube platform](https://blog.youtube/news-and-events/update-to-youtube/), the `video` resource's
[statistics.dislikeCount](https://developers.google.com/youtube/v3/docs/videos#statistics.dislikeCount)
property is now private.

You can learn more about this change on [YouTube's official blog](https://blog.youtube/news-and-events/update-to-youtube/).

### November 18, 2021

In conjunction with [changes to
make video dislike counts private across the entire YouTube platform](https://blog.youtube/news-and-events/update-to-youtube/), the `video` resource's
[statistics.dislikeCount](https://developers.google.com/youtube/v3/docs/videos#statistics.dislikeCount)
property will be made private as of December 13, 2021. This means that the property will only
be included in an API response from the `videos.list` endpoint if the API request was
authenticated by the video owner.

The [videos.rate](https://developers.google.com/youtube/v3/docs/videos/rate) endpoint is not affected
by this change.

Developers who do not display dislike counts publicly and still need the dislike count for their
API client can apply to be put on an allow list for an exemption. To apply for an exemption, you
must complete this
[application form](https://notifications.google.com/g/p/AD-FnEwIDS4bp_9WIGI6OCm7hPkOGOc3EDhVzSdo6a5ljmBmeIxVk1jJrP7Hn6cl_hmtGNwuNJqwNJ-zvpTM59UJovol1xJUpPy6xtfNKXczNtlYxda1JQPLK0uUUrwbxDi06PtUZTcIitRJKPWSUKXeYzdNFLeyP49q6N8yzgRdDZDAmEEQ8cenCu1GsjMo5Dv7NqSv2_IJ-9VF).

You can learn more about this change on [YouTube's official blog](https://blog.youtube/news-and-events/update-to-youtube/).


### July 2, 2021

**Note:** This is a deprecation announcement.

The `commentThreads.update` endpoint has been deprecated and is no longer supported.
This endpoint duplicated functionality available through other API endpoints. Instead, you can
call the [comments.update](https://developers.google.com/youtube/v3/docs/comments/update)
method and, if your code requires a `commentThreads` resource, make a secondary call to the [commentThreads.list](https://developers.google.com/youtube/v3/docs/commentThreads/list) method.

<br />

### July 1, 2021

All developers using YouTube's API Services must complete an API Compliance Audit in order to be granted more than the default quota allocation of 10,000 units. To date, both the compliance audit process and requests for additional quota unit allocations have been conducted by developers filling out and submitting the [YouTube API Services - Audit and Quota Extension Form](https://support.google.com/youtube/contact/yt_api_form).

To clarify these processes and better meet the needs of developers using our API Services, we are adding three new forms and a guide to completing those forms:

- [Audited Developer Requests Form](https://support.google.com/youtube/contact/yt_api_audited_developer_requests_form): Developers who have already passed an API Compliance Audit can fill out and submit this shorter form to request an allocated quota extension.
- [Appeals Form](https://support.google.com/youtube/contact/yt_api_appeals): Developers whose API projects have failed a compliance audit (or been denied a quota unit increase) can fill out and submit this form.
- [Change of Control Form](https://support.google.com/youtube/contact/yt_api_change_of_control_form): Developers, or any party operating an API client on a developer's behalf, who experience a change of control (for example, through a stock purchase or sale, merger or other form of corporate transaction) associated with an API project must fill out and submit this form. This enables YouTube's API team to update our records, audit the new API project's use case compliance, and validate the developer's current quota allocation.

Each new form will inform us of your intended usage of YouTube's API and enable us to better assist you.

More details are available in our new API Compliance Audits [guide](https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits).

### May 12, 2021

**Note:** This is a deprecation announcement.

This update covers the following API changes:

- The `channel` resource's
  [contentDetails.relatedPlaylists.favorites](https://developers.google.com/youtube/v3/docs/channels#contentDetails.relatedPlaylists.favorites)
  property has been deprecated. Favorite videos functionality has already been deprecated for
  several years as noted in the [April 28, 2016](https://developers.google.com/youtube/v3/revision_history#release_notes_04_28_2016), revision
  history entry.

  Prior to this update, the API would still create a new playlist if an API client attempted to
  add a video to a nonexistent favorites playlist. Going forward, the playlist will not be
  created in this case and the API will return an error. Attempts to modify favorites playlists
  by adding, modifying, or deleting items are also all deprecated per prior announcements and
  might start returning errors at any time.
- The following [channel](https://developers.google.com/youtube/v3/docs/channels) resource
  properties have been deprecated. These properties are already unsupported in the YouTube Studio UI
  and on YouTube. As a result, they are also no longer supported via the API.

  - `brandingSettings.channel.defaultTab`
  - `brandingSettings.channel.featuredChannelsTitle`
  - `brandingSettings.channel.featuredChannelsUrls[]`
  - `brandingSettings.channel.profileColor`
  - `brandingSettings.channel.showBrowseView`
  - `brandingSettings.channel.showRelatedChannels`

  All of the properties have been removed from the
  [`channel`
  resource representation](https://developers.google.com/youtube/v3/docs/channels#resource-representation), and their definitions have been removed from the resource's
  [property list](https://developers.google.com/youtube/v3/docs/channels#properties). In addition, errors
  associated with these properties have been removed from the method-specific documentation.
- The following [channelSection](https://developers.google.com/youtube/v3/docs/channelSections) resource
  properties have been deprecated. These properties are already unsupported in the YouTube Studio UI
  and on YouTube. As a result, they are also no longer supported via the API.

  - `snippet.style`
  - `snippet.defaultLanguage`
  - `snippet.localized.title`
  - `localizations`
  - `localizations.(key)`
  - `localizations.(key).title`
  - `targeting`
  - `targeting.languages[]`
  - `targeting.regions[]`
  - `targeting.countries[]`

  In conjunction with this change, the `channelSection.list` method's
  [hl](https://developers.google.com/youtube/v3/docs/channelSections/list#hl) parameter has also
  been deprecated since the features it supports are not supported.

  All of the properties have been removed from the
  [`channelSection`
  resource representation](https://developers.google.com/youtube/v3/docs/channelSections#resource-representation), and their definitions have been removed from the resource's
  [property list](https://developers.google.com/youtube/v3/docs/channelSections#properties). In addition, errors
  associated with these properties have been removed from the method-specific documentation.
- For the `channelSection` resource's
  [snippet.type](https://developers.google.com/youtube/v3/docs/channelSections#snippet.type) property,
  the following values have been deprecated. These values are already unsupported on YouTube
  channel pages and, as a result, they are also no longer supported via the API.

  - `likedPlaylists`
  - `likes`
  - `postedPlaylists`
  - `postedVideos`
  - `recentActivity`
  - `recentPosts`
- The [playlist](https://developers.google.com/youtube/v3/docs/playlists) resource's
  `snippet.tags[]` property has been deprecated. This property is already unsupported
  on YouTube and, as a result, it is no longer supported via the API.

### February 9, 2021

The [playlistItem](https://developers.google.com/youtube/v3/docs/playlistItems) resource supports two new properties:

- The [snippet.videoOwnerChannelId](https://developers.google.com/youtube/v3/docs/playlistItems#snippet.videoOwnerChannelId) property identifies the ID of the channel that uploaded the playlist video.
- The [snippet.videoOwnerChannelTitle](https://developers.google.com/youtube/v3/docs/playlistItems#snippet.videoOwnerChannelTitle) property identifies the name of the channel that uploaded the playlist video.

### January 28, 2021

This update contains the following changes:

- The [playlistItems.delete](https://developers.google.com/youtube/v3/docs/playlistItems/delete),
  [playlistItems.insert](https://developers.google.com/youtube/v3/docs/playlistItems/insert),
  [playlistItems.list](https://developers.google.com/youtube/v3/docs/playlistItems/list),
  [playlistItems.update](https://developers.google.com/youtube/v3/docs/playlistItems/update),
  [playlists.delete](https://developers.google.com/youtube/v3/docs/playlists/delete),
  [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list), and
  [playlists.update](https://developers.google.com/youtube/v3/docs/playlists/update) methods all support
  a new `playlistOperationUnsupported` error. The error occurs when a request attempts to
  perform an operation that is not allowed for a particular playlist. For example, a user cannot
  delete a video from their uploaded videos playlist or delete the playlist itself.

  In all cases, this error returns a `400` HTTP response code (Bad Request).
- The [playlistItems.list](https://developers.google.com/youtube/v3/docs/playlistItems/list) method's
  `watchHistoryNotAccessible` and `watchLaterNotAccessible` errors have
  been removed from the documentation. While users' watch history and watch later lists are, indeed,
  not accessible via the API, these particular errors are not returned by the API.

### October 15, 2020

Two new sections have been added to the [Developer
Policies](https://developers.google.com/youtube/terms/developer-policies):

- The new [Section III.E.4.i](https://developers.google.com/youtube/terms/developer-policies#III-E-4-i) provides additional information about the data collected and sent via the YouTube embedded player. You are responsible for any user data you send to us via any YouTube embedded player before the user has interacted with the player to indicate playback intent. You can limit the data shared with YouTube before a user interacts with the player by setting Autoplay to false.
- The new [Section III.E.4.j](https://developers.google.com/youtube/terms/developer-policies#III-E-4-j) relates to checking the Made for Kids (MFK) status of content before embedding it on your sites and apps. You are responsible for knowing when videos that you embed on your API Client are made for kids and treating data collected from the embedded player accordingly. As such, you must check the status of content using YouTube Data API Service before embedding it on your API Client via any YouTube embedded players.

The new [Finding the MadeForKids status of a video](https://developers.google.com/youtube/v3/guides/made_for_kids_status)
guide explains how to look up the MFK status of a video using the
[YouTube Data API Service](https://developers.google.com/youtube/v3/getting-started).

In conjunction with these changes, a reminder has been added to the
[Embedded Player Parameter documentation](https://developers.google.com/youtube/player_parameters) to explain that
if you enable Autoplay, playback will occur without any user interaction with the player; playback
data collection and sharing will therefore occur upon page load.

### October 8, 2020

This update covers three small changes related to the
[channel](https://developers.google.com/youtube/v3/docs/channels) resource:

- The [snippet.thumbnails](https://developers.google.com/youtube/v3/docs/channels#snippet.thumbnails) object, which identifies a channel's thumbnail images, might be empty for newly created channels and might take up to one day to populate.
- The [statistics.videoCount](https://developers.google.com/youtube/v3/docs/channels#statistics.videoCount) property reflects the count of the channel's public videos only, even to owners. This behavior is consistent with counts shown on the YouTube website.
- Channel keywords, which are identified in the [brandingSettings.channel.keywords](https://developers.google.com/youtube/v3/docs/channels#brandingSettings.channel.keywords) property, might be truncated if they exceed the maximum allowed length of 500 characters or if they contained unescaped quotation marks (`"`). Note that the 500 character limit is not a per-keyword limit but rather a limit on the total length of all keywords. This behavior is consistent with that on the YouTube website.

### September 9, 2020

**Note:** This is a deprecation announcement.

This update covers the following API changes. All changes will go into effect on or after
9 September 2020, the date of this announcement. With that in mind, developers should no longer
rely on any of the API features listed below.

- The following API resources, methods, parameters, and resource properties are deprecated immediately and will stop working on or after the date of this announcement:
  - The following [channel](https://developers.google.com/youtube/v3/docs/channels) resource properties:
    - The `statistics.commentCount` property
    - The `brandingSettings.image` object and all of its child properties
    - The `brandingSettings.hints`list and all of its child properties
  - The [channels.list](https://developers.google.com/youtube/v3/docs/channels/list) method's `categoryId` filter parameter
  - The [guideCategories](https://developers.google.com/youtube/v3/docs/guideCategories) resource and the [guideCategories.list](https://developers.google.com/youtube/v3/docs/guideCategories/list) method
- API responses for the [channels.list](https://developers.google.com/youtube/v3/docs/channels/list) method no longer contain the [prevPageToken](https://developers.google.com/youtube/v3/docs/channels/list#prevPageToken) property if the API request sets the [managedByMe](https://developers.google.com/youtube/v3/docs/channels/list#managedByMe) parameter to `true`. This change does not affect the `prevPageToken` property for other `channels.list` requests, and it does not affect the [nextPageToken](https://developers.google.com/youtube/v3/docs/channels/list#nextPageToken) property for any requests.
- The `channel` resource's `contentDetails.relatedPlaylists.watchLater` and `contentDetails.relatedPlaylists.watchHistory` properties were both announced as deprecated on [11 August 2016](https://developers.google.com/youtube/v3/revision_history#august-11,-2016). The `playlistItems.insert` method's and `playlistItems.delete` method's support for these playlists are also now fully deprecated, and the two properties have been removed from the documentation.
- The `channels.list` method's `mySubscribers` parameter, which was announced as deprecated on [30 July 2013](https://developers.google.com/youtube/v3/revision_history#release_notes_07_30_2013), has been removed from the documentation. Use the [subscriptions.list](https://developers.google.com/youtube/v3/docs/subscriptions/list) method and its `mySubscribers` parameter to retrieve a list of subscribers to the authenticated user's channel.
- The `channel` resource's `invideoPromotion` object and all of its child properties, which were announced as deprecated on [27 November 2017](https://developers.google.com/youtube/v3/revision_history#november-27,-2017), have been removed from the documentation.

### July 29, 2020

We have simplified our process for charging quota for API requests by removing the additional
cost associated with the `part` parameter. Effective immediately, we will only charge
the base cost for the method that is called. You can find more information about the simplified
quota [here](https://developers.google.com/youtube/v3/determine_quota_cost).

The effect of this change is that most API calls will have a marginally lower quota cost, while
some API calls will still have the same cost. This change does not increase the cost of any API
calls. Overall, the likely impact is that your allocated quota, which can be seen in the
[Google Cloud Console](http://console.cloud.google.com), will go a little further.

We strongly recommend that all developers complete a
[compliance audit](https://support.google.com/youtube/contact/yt_api_form) for their
projects to ensure continued access to the YouTube API Services.

This revision history entry was originally published on July 20, 2020.

### July 28, 2020

All videos uploaded via the [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert)
endpoint from unverified API projects created after **28 July 2020** will be restricted to
private viewing mode. To lift this restriction, each project must
[undergo an audit](https://support.google.com/youtube/contact/yt_api_form) to verify
compliance with the
[Terms of Service](https://developers.google.com/youtube/terms/api-services-terms-of-service).

Creators who use an unverified API client to upload video will receive an email explaining that
their video is locked as private, and that they can avoid the restriction by using an official
or audited client.

API projects created prior to 28 July 2020 are
not currently affected by this change. However, we strongly recommend that all developers
[complete a compliance audit](https://support.google.com/youtube/contact/yt_api_form)
for their projects to ensure continued access to the YouTube API Services.

### July 21, 2020

\[Updated July 28, 2020.\] The documentation update referenced in this revision
history entry was republished on July 28, 2020.

Yesterday, we published a documentation update related to our process for charging quota.
However, due to unforeseen circumstances, the quota change is not yet in effect. As a result, the
documentation has been reverted in the interest of accuracy. To avoid confusion, the revision
history entry explaining the change has been removed and will be republished in the near future.

### July 7, 2020

**Note:** This is a deprecation announcement.

The [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) method's
`autoLevels` and `stabilize` parameters are now deprecated, and both
parameters have been removed from the documentation. Their values are ignored and do not affect the
way newly uploaded videos are processed.

### June 15, 2020

The new [Complying with the YouTube Developer
Policies](https://developers.google.com/youtube/terms/developer-policies-guide) guide provides guidance and examples to help you ensure that your API clients adhere
to specific portions of the YouTube API Services
[Terms](https://developers.google.com/youtube/terms/api-services-terms-of-service) and
[Policies](https://developers.google.com/youtube/terms/developer-policies) (API TOS).

This guidance offers insight into how YouTube enforces certain aspects of the API TOS but does
not replace any existing documents. The guide addresses some of the most common questions that
developers ask during API compliance audits. We hope that it simplifies your feature development
process by helping you understand how we interpret and enforce our policies.

### June 4, 2020

**Note:** This is an update to a prior deprecation announcement.

The channel bulletin feature has now been fully deprecated. This change was initially announced
on 17 April 2020 and has now taken effect. As a result, the
[activities.insert](https://developers.google.com/youtube/v3/docs/activities/insert) method is no
longer supported, and the
[activities.list](https://developers.google.com/youtube/v3/docs/activities/list)
method no longer returns channel bulletins. For more details, please see the
[YouTube Help Center](https://support.google.com/youtube?p=channel-bulletins).

### April 17, 2020

**Note:** This is a deprecation announcement.

YouTube is deprecating the channel bulletin feature. As a result, the
[activities.insert](https://developers.google.com/youtube/v3/docs/activities/insert) method will be
deprecated, and the [activities.list](https://developers.google.com/youtube/v3/docs/activities/list)
method will stop returning channel bulletins. These changes will be effective in the API on or
after May 18, 2020. For more details, please see the
[YouTube Help Center](https://support.google.com/youtube?p=channel-bulletins).

### March 31, 2020

This update contains the following changes:

- **New resources and methods**

  - The new [member](https://developers.google.com/youtube/v3/docs/members) resource represents a
    channel member for a YouTube channel. A member provides recurring monetary support to a
    creator and receives special benefits. For example, members are able to chat when the
    creator turns on members-only mode for a chat.

    This resource replaces the [sponsor](https://developers.google.com/youtube/v3/live/docs/sponsors)
    resource, which is documented as part of the YouTube Live Streaming API. The
    `sponsor` resource is now deprecated and API clients should update calls to
    the `sponsors.list` method to use the
    [members.list](https://developers.google.com/youtube/v3/docs/members/list) method instead.
  - The new [membershipsLevel](https://developers.google.com/youtube/v3/docs/membershipsLevels)
    resource identifies a pricing level managed by the creator that authorized the API request.
    The [membershipsLevels.list](https://developers.google.com/youtube/v3/docs/membershipsLevels/list)
    method retrieves a list of all of the creator's membership levels.

### January 10, 2020

The API now supports the ability to identify child-directed content, which YouTube calls
"made for kids." [Learn more about
"made for kids" content](https://support.google.com/youtube/answer/9528076) in the YouTube Help Center.

The [channel](https://developers.google.com/youtube/v3/docs/channels) and
[video](https://developers.google.com/youtube/v3/docs/videos) resources support two new properties to
enable content creators and viewers to identify content that is made for kids:

- The `selfDeclaredMadeForKids` property enables content creators to specify whether a [channel](https://developers.google.com/youtube/v3/docs/channels#status.selfDeclaredMadeForKids) or [video](https://developers.google.com/youtube/v3/docs/videos#status.selfDeclaredMadeForKids) is made for kids.   

  For channels, this property can be set when calling the [channels.update](https://developers.google.com/youtube/v3/docs/channels/update) method. For videos, this property can be set when calling either the [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) or [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) methods.   

  Note that this property is only included in API responses that contain `channel` or `video` resources if the channel owner authorized the API request.
- The `madeForKids` property enables any user to retrieve the "made for kids" status of a [channel](https://developers.google.com/youtube/v3/docs/channels#status.madeForKids) or [video](https://developers.google.com/youtube/v3/docs/videos#status.madeForKids). For example, the status might be determined based on the value of the `selfDeclaredMadeForKids` property. See the [YouTube Help Center](https://support.google.com/youtube/answer/9527654) for more information about setting the audience for your channel, videos, or broadcasts.

We have also updated the YouTube API Services Terms of Service and Developer Policies. Please
see the [YouTube API Services Terms of Service - Revision
History](https://developers.google.com/youtube/terms/revision-history) for more information. The changes to the YouTube API Services Terms of Service and
Developer Policies will take effect on January 10, 2020 Pacific Time.

### September 10, 2019

The API reference documentation has been updated to reflect a change to the way that subscriber
counts are reported on YouTube and, consequently, in API responses. As a result of the change,
subscriber counts returned by the YouTube Data API Service are rounded down to three significant
figures for subscriber counts greater than 1000 subscribers. This change affects the
`channel` resource's
[statistics.subscriberCount](https://developers.google.com/youtube/v3/docs/channels#statistics.subscriberCount)
property.

**Note:** This change affects this property value even in cases where a user
sends an authorized request for data about their own channel. Channel owners can still see exact
subscriber counts in YouTube Studio.

For example, if a channel has 123,456 subscribers, the
`statistics.subscriberCount` property will contain the value `123000`.
The table below shows examples of how subscriber counts are rounded in API responses and
abbreviated in other publicly visible YouTube user interfaces:

| Example subscriber count | YouTube Data API | Publicly visible YouTube UIs |
|--------------------------|------------------|------------------------------|
| 1,234                    | 1230             | 1.23K                        |
| 12,345                   | 12300            | 12.3K                        |
| 123,456                  | 123000           | 123K                         |
| 1,234,567                | 1230000          | 1.23M                        |
| 12,345,678               | 12300000         | 12.3M                        |
| 123,456,789              | 123000000        | 123M                         |

### April 4, 2019

This update contains the following changes:

- The API reference documentation has been updated to better explain common use cases for each method and to provide dynamic, high-quality code samples through the APIs Explorer widget. See the [channels.list](https://developers.google.com/youtube/v3/docs/channels/list) method's documentation for an example. There are now two new elements on pages that describe API methods:

  - The APIs Explorer widget lets you select authorization scopes, enter sample parameter and property values, and then send actual API requests and see actual API responses. The widget also offers a fullscreen view that shows complete code samples, which dynamically update to use the scopes and values that you have entered.

  - The **Common use cases** section describes one or more common use cases for the method explained on the page. For example, you could call the `channels.list` method to retrieve data about a specific channel or to retrieve data about the current user's channel.

    You can use links in that section to populate the APIs Explorer with sample values for your use case or to open the fullscreen APIs Explorer with those values already populated. These changes aim to make it easier for you to see code samples that are directly applicable to the use case that you're trying to implement in your own application.

  Code samples are currently supported for Java, JavaScript, PHP, Python, and curl.
- The [code samples](https://developers.google.com/youtube/v3/code_samples/code_snippets) tool has also been updated with a new UI that offers all of the same features described above. Using that tool, you can explore use cases for different methods, load values into the APIs Explorer, and open the fullscreen APIs Explorer to get code samples in Java, JavaScript, PHP, and Python.

  In conjunction with this change, the pages that previously listed available code samples for Java, JavaScript, PHP, and Python have been removed.
- The quickstart guides for [Java](https://developers.google.com/youtube/v3/quickstarts/java), [JavaScript](https://developers.google.com/youtube/v3/quickstarts/js), [PHP](https://developers.google.com/youtube/v3/quickstarts/php), and [Python](https://developers.google.com/youtube/v3/quickstarts/python) have been updated. The revised guides explain how to run one sample with an API key and another sample with an OAuth 2.0 client ID using code samples from the APIs Explorer.

Note that the changes described above replace an interactive tool that had been added to the API documentation in 2017.

### July 9, 2018

This update contains the following changes:

- The definition of the `channel` resource's [snippet.thumbnails](https://developers.google.com/youtube/v3/docs/channels#snippet.thumbnails) property has been updated to note that when displaying thumbnails in your application, your code should use the image URLs exactly as they are returned in API responses. For example, your application should not use the `http` domain instead of the `https` domain in a URL returned in an API response.

  Beginning in July 2018, channel thumbnail URLs will only be available in the `https` domain, which is how the URLs appear in API responses. After that time, you might see broken images in your application if it tries to load YouTube images from the `http` domain.
- **Note:** This is a deprecation announcement.

  The `video` resource's [recordingDetails.location.altitude](https://developers.google.com/youtube/v3/docs/videos#recordingDetails.location.altitude) property has been deprecated. There is no guarantee that videos will return values for this property. Similarly, even if API requests attempt to set a value for that property, it is possible that the incoming data will not be stored.

### June 22, 2018

The [Implementation guide](https://developers.google.com/youtube/v3/guides/implementation), formerly known as the
Implementation and Migration guide, has been updated to remove instructions for migrating from the
v2 API to the v3 API. In addition, instructions have also been removed for features that have
since been deprecated in the v3 API, such as favorite videos.

### November 27, 2017

This update contains the following changes:

- **Note:** This is a deprecation announcement.

  YouTube is removing support for the **Featured Video** and **Featured Website** features, which are supported in the API via the `channel` resource's [invideoPromotion](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion) object. As a result, that object, including all of its child properties are being deprecated.

  You can still retrieve and set `invideoPromotion` data until December 14, 2017. After that date:
  - Attempts to retrieve the `invideoPromotion` part when calling `channels.list` will return an empty `invideoPromotion` or will not return any `invideoPromotion` data at all.
  - Attempts to update `invideoPromotion` data when calling `channels.update` will return a successful response until at least May 27, 2018, but they will be treated as no-ops, meaning that they will not actually perform an update.

  After May 27, 2018, it is possible that these requests could return error messages to indicate, for example, that `invalidPromotion` is an invalid part.

### November 16, 2017

This update contains the following changes:

- The [interactive code snippet tool](https://developers.google.com/youtube/v3/code_samples/code_snippets) now supports Node.js code samples. The samples are also visible in the documentation for almost all API methods, such as the [channels.list](https://developers.google.com/youtube/v3/docs/channels/list#usage) method.

  The customizable samples are designed to give you a use-case-specific starting point for a Node.js application. The functionality is similar to the code in the [Node.js quickstart guide](https://developers.google.com/youtube/v3/quickstart/nodejs). However, the samples do contain some utility functions that don't appear in the quickstart:
  - The `removeEmptyParameters` function takes a list of key-value pairs corresponding to API request parameters and removes the parameters that don't have values.
  - The `createResource` function takes a list of key-value pairs corresponding to properties in an API resource. It then converts the properties into a JSON object that can be used in `insert` and `update` operations. The example below shows a set of property names and values and the JSON object that the code would create for them:  

    ```
    # Key-value pairs:
    {'id': 'ABC123',
     'snippet.title': 'Resource title',
     'snippet.description': 'Resource description',
     'status.privacyStatus': 'private'}

    # JSON object:
    {
     'id': 'ABC123',
     'snippet': {
       'title': 'Resource title',
       'description': 'Resource description',
     },
     'status': {
       'privacyStatus': 'private'
     }
    }
    ```

  All of these samples are designed to be downloaded and run locally. For more information, see the prerequisites for [running full code samples locally](https://developers.google.com/youtube/v3/code_samples/code_snippet_instructions#toggle-code-snippets-and-full-samples) in the code snippet tool instructions.

### October 25, 2017

This update contains the following changes:

- The Python code samples in the [interactive code snippet tool](https://developers.google.com/youtube/v3/code_samples/code_snippets) have been updated to use the `google-auth` and `google-auth-oauthlib` libraries instead of the `oauth2client` library, which is now deprecated.

  In addition to that change, the tool now provides full code samples for installed Python applications and Python web server applications, which use slightly different authorization flows. To see the full samples (and this change):
  1. Go to the [interactive code snippet tool](https://developers.google.com/youtube/v3/code_samples/code_snippets) or to the documentation for any API method, such as the [channels.list](https://developers.google.com/youtube/v3/docs/channels/list#usage) method.
  2. Click the `Python` tab above the code samples.
  3. Click the toggle above the tabs to switch from seeing a snippet to a full sample.  
     ![](https://developers.google.com/static/youtube/images/interactive-snippet-slider.png)
  4. The tab should now show a complete code sample that uses the `InstalledAppFlow` authorization flow. The description above the sample explains this and also links to a sample for a web server application.
  5. Click the link to switch to the web server example. That sample uses the Flask web application framework and a different authorization flow.

  All of these samples are designed to be downloaded and run locally. If you'd like to run the samples, see the instructions for [running full code samples locally](https://developers.google.com/youtube/v3/code_samples/code_snippet_instructions#toggle-code-snippets-and-full-samples) in the code snippet tool instructions.

### August 29, 2017

This update contains the following changes:

- The definition of the `search.list` method's [forContentOwner](https://developers.google.com/youtube/v3/docs/search/list#forContentOwner) parameter has been updated to note that if that parameter is set to `true`, the `type` parameter must be set to `video`.
- The definition of the `search.list` method's [regionCode](https://developers.google.com/youtube/v3/docs/search/list#regionCode) parameter has been updated to clarify that the parameter restricts search results to videos that can be viewed in the specified region.
- YouTube has updated its branding logos and icons. New "developed with YouTube" logos can be downloaded from the [branding guidelines](https://developers.google.com/youtube/terms/branding-guidelines) page. Other new YouTube logos and icons are also shown on that page and can be downloaded from the [YouTube brand site](https://www.youtube.com/yt/about/brand-resources/#logos-icons-colors).

### July 24, 2017

This update contains the following changes:

- A new YouTube Data API quickstart guide is available for [iOS](https://developers.google.com/youtube/v3/quickstart/ios). The guide explains how to use the YouTube Data API in a simple iOS application written in either Objective-C or Swift.
- The [interactive code snippet tool](https://developers.google.com/youtube/v3/code_samples/code_snippets) for the YouTube Data API now includes documentation explaining some of the tool's features:
  - Executing API requests
  - Toggling between code snippets and full code samples
  - Using boilerplate functions
  - Loading existing resources (for update methods)

  **Note:** The tool is also embedded in API reference documentation for API methods ([example](https://developers.google.com/youtube/v3/docs/search/list#usage)).

### June 1, 2017

This update contains the following changes:

- **Note:** This is a deprecation announcement.

  The following [video](https://developers.google.com/youtube/v3/docs/videos) resource properties are being deprecated. While the properties will be supported until December 1, 2017, there is no guarantee that videos will continue to return values for those properties until that time. Similarly, [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) and [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) requests that set those property values will not generate errors before that date, but it is possible that the incoming data will not be stored.
  - [recordingDetails.locationDescription](https://developers.google.com/youtube/v3/docs/videos#recordingDetails.locationDescription)
  - [recordingDetails.location.latitude](https://developers.google.com/youtube/v3/docs/videos#recordingDetails.location.latitude)
  - [recordingDetails.location.longitude](https://developers.google.com/youtube/v3/docs/videos#recordingDetails.location.longitude)

### May 17, 2017

This update contains the following changes:

- The API reference documentation has been updated to make code snippets more ubiquitous and interactive. Pages that explain API methods, like [channels.list](https://developers.google.com/youtube/v3/docs/channels/list#usage) or [videos.rate](https://developers.google.com/youtube/v3/docs/videos/rate#usage), now feature an interactive tool that lets you view and customize code snippets in Java, JavaScript, PHP, Python, Ruby, Apps Script, and Go.

  For any given method, the tool shows code snippets for one or more use cases, and each use case describes a common way of calling that method. For example, you can call the `channels.list` method to retrieve data about a specific channel or about the current user's channel.

  You can also interact with code samples:
  - Modify parameter and property values, and the code snippets dynamically update to reflect the values you provide.

  - Toggle between code snippets and full samples. A code snippet shows the portion of the code that calls the API method. A full sample contains that snippet as well as boilerplate code for authorizing and sending requests. Full samples can be copied and run from the command line or a local web server.

  - Execute requests by clicking a button. (To execute requests, you need to authorize the tool to call the API on your behalf.)

  Note that this tool has replaced the APIs Explorer on the pages where it is available. (Each page displays a link so that you also have the option of loading the request you are working on in the APIs Explorer.)
- The [Data API Code Snippets](https://developers.google.com/youtube/v3/code_samples/code_snippets) tool has also been updated with a new UI that offers all of the same features described above. The major new features available on this page are:

  <br />

  - Support for API requests that write data.
  - Support for Java samples.
  - More flexible and comprehensive boilerplate code for authorizing users and building API requests.

  <br />

### April 27, 2017

This update contains the following changes:

- New quickstart guides explain how to set up a simple application that makes YouTube Data API requests. Guides are currently available for [Android](https://developers.google.com/youtube/v3/quickstart/android), [Apps Script](https://developers.google.com/youtube/v3/quickstart/apps-script), [Go](https://developers.google.com/youtube/v3/quickstart/go), [Java](https://developers.google.com/youtube/v3/quickstart/java), [JavaScript](https://developers.google.com/youtube/v3/quickstart/js), [Node.js](https://developers.google.com/youtube/v3/quickstart/nodejs), [PHP](https://developers.google.com/youtube/v3/quickstart/php), [Python](https://developers.google.com/youtube/v3/quickstart/python), and [Ruby](https://developers.google.com/youtube/v3/quickstart/ruby).

### March 30, 2017

This update contains the following changes:

- The `channel` resource's new [topicDetails.topicCategories[]](https://developers.google.com/youtube/v3/docs/channels#topicDetails.topicCategories[]) property contains a list of Wikipedia URLs that describe the channel's content. The URLs correspond to the topic IDs returned in the resource's `topicDetails.topicIds[]` property.
- The `playlistItem` resource's new [contentDetails.videoPublishedAt](https://developers.google.com/youtube/v3/docs/playlistItems#contentDetails.videoPublishedAt) property identifies the time that the video was published to YouTube. The resource already contains the [snippet.publishedAt](https://developers.google.com/youtube/v3/docs/playlistItems#snippet.publishedAt) property, which identifies the time that the item was added to the playlist.
- Like the `channel` resource, the `video` resource now returns the [topicDetails.topicCategories[]](https://developers.google.com/youtube/v3/docs/videos#topicDetails.topicCategories[]) property, which contains a list of Wikipedia URLs that describe the video's content. For `video` resources, the URLs correspond to the topic IDs returned in the resource's `topicDetails.relevantTopicIds[]` property.
- The `video` resource's new [contentDetails.contentRating.mpaatRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.mpaatRating) property identifies the rating that the Motion Picture Association of America gave to a movie trailer or preview.

### February 27, 2017

As originally [announced on August 11, 2016](https://developers.google.com/youtube/v3/revision_history#topic-id-changes), YouTube has switched the supported list of topic IDs to a curated list. The complete list of supported topic IDs is included in the `topicDetails` properties for [channel](https://developers.google.com/youtube/v3/docs/channels#topicDetails) and [video](https://developers.google.com/youtube/v3/docs/videos#topicDetails) resources as well as in the `search.list` method's [topicId](https://developers.google.com/youtube/v3/docs/search/list#topicId) parameter.

Note that there are several changes to the curated list:

- The following topics have been added as subtopics of `Society`:

  |   Name   |  topic ID   |
  |----------|-------------|
  | Business | `/m/09s1f`  |
  | Health   | `/m/0kt51`  |
  | Military | `/m/01h6rj` |
  | Politics | `/m/05qt0`  |
  | Religion | `/m/06bvp`  |

- The `Animated cartoon` topic, previously a child of `Entertainment`, has been removed.
- The `Children's music` topic, previously a child of `Music`, has been removed.

As a result of this change, topics related to a video are now always returned in the `video` resource's [topicDetails.relevantTopicIds[]](https://developers.google.com/youtube/v3/docs/videos#topicDetails.relevantTopicIds[]) property value.

### November 29, 2016

This update contains the following changes:

- There are three small changes to the list of topic IDs that will be supported as of February 10, 2017:

  - The `Professional wrestling` category, which was previously a child of the `Sports` category, is now a child of `Entertainment`.
  - The `TV shows` category, which is a child of `Entertainment`, is new.
  - The `Health` category, previously a child of `Lifestyle`, has been removed.

  Also note that there are a few parent categories (`Entertainment`, `Gaming`, `Lifestyle`, `Music`, and `Sports`). Any video that is associated with a child category, like `Tennis`, will also be associated with the parent category (`Sports`).

### November 10, 2016

This update contains the following changes:

- As [first announced on August 11, 2016](https://developers.google.com/youtube/v3/revision_history#topic-id-changes), the deprecation of Freebase and the Freebase API requires several changes related to topic IDs. Topic IDs identify topics associated with [channel](https://developers.google.com/youtube/v3/docs/channels#topicDetails) and [video](https://developers.google.com/youtube/v3/docs/videos#topicDetails) resources, and you can also use the [topicId](https://developers.google.com/youtube/v3/docs/search/list#topicId) search parameter to find channels or videos related to a particular topic.

  On February 10, 2017, YouTube will start returning a small set of topic IDs instead of the much more granular set of IDs returned thus far. In addition, note that channels and videos are not guaranteed to be associated with any topics, which is consistent with current API behavior.

  So that you can prepare your API Clients for those changes, the definitions of the following API parameters and properties have been updated to list the topic IDs that will be supported after that time. Note that the list of categories is the same for all of the properties.
  - The `channel` resource's [topicDetails.topicIds[]](https://developers.google.com/youtube/v3/docs/channels#topicDetails.topicIds[]) property.
  - The `video` resource's [topicDetails.relevantTopicIds[]](https://developers.google.com/youtube/v3/docs/videos#topicDetails.relevantTopicIds[]) property.
  - The `search.list` method's [topicId](https://developers.google.com/youtube/v3/docs/search/list#topicId) parameter.
- **Note:** This is a deprecation announcement.

  The following properties are being deprecated:
  - The `channel` resource's [topicDetails.topicIds[]](https://developers.google.com/youtube/v3/docs/channels#topicDetails.topicIds[]) property. This property will be supported until November 10, 2017.
  - The `video` resource's [topicDetails.relevantTopicIds[]](https://developers.google.com/youtube/v3/docs/videos#topicDetails.relevantTopicIds[]) property. This property will be supported until November 10, 2017.
  - The `video` resource's [topicDetails.topicIds[]](https://developers.google.com/youtube/v3/docs/videos#topicDetails.topicIds[]) property. This property will not contain values after February 10, 2017. (After that date, the `topicDetails.relevantTopicIds[]` property value will identify all of the topics associated with a video.)
- Since Freebase has already been deprecated, the **Searching with Freebase Topics** guide has been removed from the documentation. That guide provided code samples to show how an application would work with the Freebase API.

  In addition, several code samples related to topic IDs have been removed from the `search.list` method's documentation.

### November 2, 2016

This update contains the following changes:

- **New properties and parameters**

  - The `video` resource contains several new properties:

    - The [player.embedHtml](https://developers.google.com/youtube/v3/docs/videos#player.embedHtml) property contains an `<iframe>` tag that you can use to embed a player that plays the video. The new [player.embedHeight](https://developers.google.com/youtube/v3/docs/videos#player.embedHeight) and [player.embedWidth](https://developers.google.com/youtube/v3/docs/videos#player.embedWidth) properties identify the dimensions of the embedded player. These properties are only returned if the API request specifies a value for at least one of the `maxHeight` or `maxWidth` parameters. Those two new parameters are explained later in this revision history entry.

    - The new [hasCustomThumbnail](https://developers.google.com/youtube/v3/docs/videos#contentDetails.hasCustomThumbnail) property indicates whether the video uploader has provided a custom thumbnail image for the video. Note that this property is only visible to the video uploader.

    - The new [fpbRatingReasons[]](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.fpbRatingReasons[]) identifies reasons that the video received its FPB (South Africa) rating.

    - The new [mcstRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.mcstRating) identifies the rating that the video received in Vietnam.

  - The `videos.list` method supports two new parameters, [maxHeight](https://developers.google.com/youtube/v3/docs/videos/list#maxHeight) and [maxWidth](https://developers.google.com/youtube/v3/docs/videos/list#maxWidth). You can use either parameter or both parameters when retrieving the `player` part in `video` resources.

    By default, the height of the `<iframe>` returned in the `player.embedHtml` property is 360px. The width adjusts to match the video's aspect ratio, thereby ensuring that the embedded player does not have black bars framing the video. So, for example, if a video's aspect ratio is 16:9, the player's width would be 640px.

    With the new parameters, you can specify that instead of the default dimensions, the embed code should use a height and/or width appropriate for your application layout. The API server scales the player dimensions as appropriate to ensure that the embedded player does not have black bars framing the video. Note that both parameters specify the maximum dimensions of the embedded player. Thus, if both parameters are specified, one dimension might still be smaller than the maximum amount allowed for that dimension.

    For example, suppose a video has a 16:9 aspect ratio. Thus, the `player.embedHtml` tag would contain a 640x360 player if the `maxHeight` or `maxWidth` parameter is not set.

    <br />

    - If the `maxHeight` parameter is set to `720`, and the `maxWidth` parameter is not set, the API would return a 1280x720 player.
    - If the `maxWidth` parameter is set to `960`, and the `maxHeight` parameter is not set, the API would return a 960x540 player.
    - If the `maxWidth` parameter is set to `960`, and the `maxHeight` parameter is set to `450`, the API would return an 800x450 player.

    <br />

    The new [player.embedHeight](https://developers.google.com/youtube/v3/docs/videos#player.embedHeight) and [player.embedWidth](https://developers.google.com/youtube/v3/docs/videos#player.embedWidth) properties, which are described above, identify the player's dimensions.
- **Updates to existing methods, properties and parameters**

  - The [channelSection](https://developers.google.com/youtube/v3/docs/channelSections) resource description has been updated to note that a channel can create a maximum of 10 shelves without setting [targeting data](https://developers.google.com/youtube/v3/docs/channelSections#targeting) and can create a maximum of 100 shelves with targeting data.

    In addition, the `channelSection` resource's [targeting](https://developers.google.com/youtube/v3/docs/channelSections#targeting) property has been updated to reflect the fact that targeting options can only be set using the API. Targeting options are deleted if the channel section is modified using the user interface on the YouTube website.
  - The definition of the `i18nLanguage` resource's [snippet.name](https://developers.google.com/youtube/v3/docs/i18nLanguages#snippet.name) property has been corrected to reflect that the value represents a language's name as it is written in the language specified by the `i18nLanguage.list` method's [hl](https://developers.google.com/youtube/v3/docs/i18nLanguages/list#hl) parameter.

  - The `playlistItem` resource's [contentDetails.note](https://developers.google.com/youtube/v3/docs/playlistItems#contentDetails.note) property has been updated to note that the property value's maximum length is 280 characters.

  - The `playlistItem` resource's `contentDetails.startAt` and `contentDetails.endAt` properties have been deprecated. These fields are ignored if they are set in `playlistItems.insert` or `playlistItems.update` requests.

  - The [playlistItems.delete](https://developers.google.com/youtube/v3/docs/playlistItems/delete#params) and [playlistItems.update](https://developers.google.com/youtube/v3/docs/playlistItems/update#params) methods now support the `onBehalfOfContentOwner` parameter, which is already supported for several other methods. Requests that use that method also need to be authorized with a token that provides access to the `https://www.googleapis.com/auth/youtubepartner` scope.

  - The `search.list` method's [publishedBefore](https://developers.google.com/youtube/v3/docs/search/list#publishedBefore) and [publishedAfter](https://developers.google.com/youtube/v3/docs/search/list#publishedAfter) parameters have both been updated to indicate that the parameter values are inclusive. So, for example, if the `publishedBefore` parameter is set, the API returns resources created before *or at* the specified time.

  - The `video` resource's [contentDetails.contentRating.grfilmRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.grfilmRating) property supports three additional values: `grfilmK12`, `grfilmK15`, and `grfilmK18`.

  - The [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) method description has been updated to note that the maximum file size for uploaded videos has increased from 64GB to 128GB.

- **New and updated errors**

  - The API supports the following new errors:

    |      Error type      |        Error detail         |                                                                                                                                                                                              Description                                                                                                                                                                                               |
    |----------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | `forbidden (403)`    | `homeParameterDeprecated`   | The [activities.list](https://developers.google.com/youtube/v3/docs/activities/list) method returns this error to indicate that the user's home page activity data is not available through this API. This error might occur if you set the `home` parameter to `true` in an unauthorized request.                                                                                                     |
    | `invalidValue (400)` | `invalidContentDetails`     | The [playlistItems.insert](https://developers.google.com/youtube/v3/docs/playlistItems/insert) method returns this error to indicate that the `contentDetails` object in the request is invalid. One reason that this error occurs is that the `contentDetails.note` field is longer than 280 characters.                                                                                              |
    | `forbidden (403)`    | `watchHistoryNotAccessible` | The [playlistItems.list](https://developers.google.com/youtube/v3/docs/playlistItems/list) method returns this error to indicate that the request tried to retrieve "watch history" playlist items, but those cannot be retrieved using the API.                                                                                                                                                       |
    | `forbidden (403)`    | `watchLaterNotAccessible`   | The [playlistItems.list](https://developers.google.com/youtube/v3/docs/playlistItems/list) method returns this error to indicate that the request tried to retrieve "watch later" playlist items, but those cannot be retrieved using the API.                                                                                                                                                         |
    | `badRequest (400)`   | `uploadLimitExceeded`       | The [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) method returns this error to indicate that the channel has exceeded the number of videos that it may upload.                                                                                                                                                                                                          |
    | `forbidden (403)`    | `forbiddenEmbedSetting`     | The [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) method returns this error to indicate that the API request attempts to set an invalid embed setting for the video. Note that some channels may not have permission to offer embedded players for live streams. See the [YouTube Help Center](https://support.google.com/youtube/answer/2474026) for more information. |

  - The `playlistItems.insert` method no longer returns an error if you insert a duplicate video into a playlist. That error previously occurred for some playlists, like favorite videos, that did not allow duplicates but are no longer supported. In general, playlists do allow duplicate videos.

- **Other updates**

  - The revision history entry for September 15, 2016, has been updated to clarify that, whenever the `channel` resource's `contentDetails.relatedPlaylists.watchHistory` and `contentDetails.relatedPlaylists.watchLater` properties are included in a response, they always contain the values `HL` and `WL`, respectively. Moreover, those properties are only included if an authorized user is retrieving data about the user's own channel.

### September 15, 2016

This update contains the following changes:

- The August 11, 2016, revision history update discussed several changes related to topic IDs, including the fact that the set of supported topic IDs will change as of February 10, 2017. The list of topics that will be supported will be published by November 10, 2016.

- The following changes are now in effect. Notice of these changes was given in the revision history update on August 11, 2016:

  - If the `activities.list` method is called with the [home](https://developers.google.com/youtube/v3/docs/activities/list#home) parameter set to `true`, the API response now contains items similar to what a logged-out YouTube user would see on the home page.

    This is a slight change that is intended to provide a better user experience than the behavior described in the revision history update on August 11, 2016. That update had stated that requests using the `home` parameter would return an empty list.
  - The `channel` resource's `contentDetails.relatedPlaylists.watchHistory` and `contentDetails.relatedPlaylists.watchLater` properties now contain values of `HL` and `WL`, respectively, for all channels.

    To be clear, these properties are only visible to an authorized user retrieving data about the user's own channel. The properties always contain the values `HL` and `WL`, even for an authorized user retrieving data about the user's own channel. Thus, the watch history and watch later playlist IDs cannot be retrieved via the API.

    In addition, requests to retrieve playlist details (`playlists.list`) or playlist items (`playlistItems.list`) for a channel's watch history or watch later playlist now return empty lists. This behavior is true for the new values, `HL` and `WL`, as well as for any watch history or watch later playlist IDs that your API Client may have already stored.
- The [video](https://developers.google.com/youtube/v3/docs/videos) resource's `fileDetails.recordingLocation` object and its child properties are no longer returned. Previously, this data (like the parent `fileDetails` object) could only be retrieved by a video's owner.

### August 11, 2016

This update contains the following changes:

- The newly published YouTube API Services Terms of Service ("the Updated Terms"), discussed in detail on the [YouTube Engineering and Developers Blog](http://youtube-eng.blogspot.com/), provides a rich set of updates to the current Terms of Service. In addition to the [Updated Terms](https://developers.google.com/youtube/terms/api-services-terms-of-service), which will go into effect as of February 10, 2017, this update includes several supporting documents to help explain the policies that developers must follow.

  The full set of new documents is described in the [revision history for the Updated Terms](https://developers.google.com/youtube/terms/revision-history). In addition, future changes to the Updated Terms or to those supporting documents will also be explained in that revision history. You can subscribe to an RSS feed listing changes in that revision history from a link in that document.
- The deprecation of Freebase and the Freebase API is causing several changes related to topic IDs. Topic IDs are used in the following API resources and methods:

  - The `channel` resource's [topicDetails](https://developers.google.com/youtube/v3/docs/channels#topicDetails) part identifies topics associated with the channel.
  - The `video` resource's [topicDetails](https://developers.google.com/youtube/v3/docs/videos#topicDetails) part identifies topics associated with the video.
  - The `search.list` method's [topicId](https://developers.google.com/youtube/v3/docs/search/list#topicId) parameter lets you search for videos or channels related to a particular topic.

  The changes to these features are:
  - As of February 10, 2017, YouTube will start returning a small set of topic IDs instead of the much more granular set of IDs returned thus far. That set of supported topics will identify high-level categorizations like **Sports** or **Basketball**, but, for example, they will not identify specific teams or players. We will be announcing the set of supported topics so that you have time to prepare your application for this change.

  - Any Freebase topic IDs that you have already retrieved can be used to search for content until February 10, 2017. However, after that time, you will be able to use only the smaller set of topics identified in the previous item to retrieve search results by topic.

  - After February 10, 2017, if you try to search for results using a topic ID that is not in the smaller set of supported topic IDs, the API will return an empty result set.

- Several API fields and parameters are being deprecated effective September 12, 2016:

  - The `activities.list` method's [home](https://developers.google.com/youtube/v3/docs/activities/list#home) parameter enabled an authorized user to retrieve the activity feed that would display on the YouTube home page for that user. Requests that use this parameter after September 12, 2016, will return an empty list.

  - The `channel` resource's `contentDetails.relatedPlaylists.watchHistory` and `contentDetails.relatedPlaylists.watchLater` properties are only visible to an authorized user retrieving data about the user's own channel. After September 12, 2016, the `contentDetails.relatedPlaylists.watchHistory` will return a value of `HL` and the `contentDetails.relatedPlaylists.watchLater` property will return a value of `WL` for all channels.

    Requests to retrieve playlist details (`playlists.list`) for a channel's watch history or watch later playlist will return an empty list after September 12, 2016. Requests to retrieve playlist items (`playlistItems.list`) in either of those playlists will also return an empty list after that time. This is true for the new values, `HL` and `WL`, as well as for any watch history or watch later playlist IDs that your API Client may have already stored.
  - The [video](https://developers.google.com/youtube/v3/docs/videos) resource's `fileDetails.recordingLocation` object or any of its child properties will no longer be returned after September 12, 2016. This data can only be retrieved by a video's owner since the parent `fileDetails` object can only be retrieved by a video owner.

### June 13, 2016

This update contains the following changes:

- The `channel` resource's `contentDetails.googlePlusUserId` property has been deprecated. Previously, the property was only present if the channel was associated with a Google+ profile. Following the deprecation, the property will no longer be included in any `channel` resources.

- The `comment` resource's `snippet.authorGoogleplusProfileUrl` property has been deprecated. Previously, the property was only present if the channel was associated with a Google+ profile. Following the deprecation, the property will no longer be included in any `comment` resources.

Since neither of these properties will be returned following the deprecation, both properties have been removed from the corresponding resource documentation.

### May 31, 2016

This update contains the following changes:

- The `subscriptions.list` method's new [myRecentSubscribers](https://developers.google.com/youtube/v3/docs/subscriptions/list#myRecentSubscribers) parameter retrieves a list of the subscribers of the authenticated user's channel in reverse chronological order of the time that they subscribed to the channel.

  Note that the new parameter only supports retrieval of the most recent 1000 subscribers to the authenticated user's channel. To retrieve a complete list of subscribers, use the [mySubscribers](https://developers.google.com/youtube/v3/docs/subscriptions/list#mySubscribers) parameter. That parameter, which does not return subscribers in a particular order, does not limit the number of subscribers that can be retrieved.
- The definition of the `snippet.thumbnails.(key)` property has been updated for the [activity](https://developers.google.com/youtube/v3/docs/activities#snippet.thumbnails.(key)), [playlistItem](https://developers.google.com/youtube/v3/docs/playlistItems#snippet.thumbnails.(key)), [playlist](https://developers.google.com/youtube/v3/docs/playlists#snippet.thumbnails.(key)), [search result](https://developers.google.com/youtube/v3/docs/search#snippet.thumbnails.(key)), [thumbnail](https://developers.google.com/youtube/v3/docs/thumbnails#snippet.thumbnails.(key)), and [video](https://developers.google.com/youtube/v3/docs/videos#snippet.thumbnails.(key)) resources to note that additional thumbnail image sizes are available for some videos.

  - The `standard` image is 640px wide and 480px tall.
  - The `maxres` image is 1280px wide and 720px tall.
- The definition of the `channelSection.list` method's [part](https://developers.google.com/youtube/v3/docs/channelSections/list#part) parameter has been updated to note that the `targeting` part can be retrieved at a cost of `2` quota units.

- The `videos.list` method now returns a [forbidden](https://developers.google.com/youtube/v3/docs/videos/list#youtube.videos.list-forbidden-forbidden-feedback) (`403`) error when an improperly authorized request tries to retrieve the `fileDetails`, `processingDetails`, or `suggestions` parts of a `video` resource. Those parts are only available to the video's owner.

### May 17, 2016

The new [Data API Code Snippets](https://developers.google.com/youtube/v3/code_samples/code_snippets) tool provides short code snippets for common YouTube Data API use cases. Code snippets are currently available for all read-only API methods in Apps Script, Go, JavaScript, PHP, Python, and Ruby.

For each method, the tool shows code samples for one or more use cases. For example, it provides five code snippets for the `search.list` method:

- List videos by keyword
- List videos by location
- List live events
- Search for the authenticated user's videos
- List related videos

For each use case, the tool displays the parameters used in the API request. You can modify the parameter values, in which case the tool updates the code snippets to reflect the parameter values that you provided.

Finally, the tool displays the API response to each request. If you have modified the request parameters, the API response is based on your provided parameter values. Note that you need to authorize the tool to submit requests on your behalf for API responses to display.

### April 28, 2016

This update contains the following changes:

- The `video` resource's new [contentDetails.projection](https://developers.google.com/youtube/v3/docs/videos#contentDetails.projection) property specifies the video's projection format. Valid property values are `360` and `rectangular`.

- The `video` resource's [recordingDetails.location](https://developers.google.com/youtube/v3/docs/videos#recordingDetails.location) and [fileDetails.recordingLocation](https://developers.google.com/youtube/v3/docs/videos#fileDetails.recordingLocation) properties have both been updated to explain the difference between the two properties:

  <br />

  - The `recordingDetails.location` property identifies the location that the video owner wants to associate with the video. This location is editable, searchable on public videos, and might be displayed to users for public videos.
  - The `fileDetails.recordingLocation` property value is immutable and represents the location associated with the original, uploaded video file. The value is only visible to the video owner.

  <br />

- The definition of the `channel` resource's [contentDetails.relatedPlaylists.favorites](https://developers.google.com/youtube/v3/docs/channels#contentDetails.relatedPlaylists.favorites) property has been updated to note that the property value might contain a playlist ID that refers to an empty playlist and that cannot be fetched. This is due to the fact that favorite videos functionality has already been deprecated. Note that this property is [not subject to the API deprecation policy](https://developers.google.com/youtube/youtube-api-list).

- The definition of the `ineligibleAccount` error, which can be returned by the `comments.insert`, `comments.update`, `commentThreads.insert`, or `commentThreads.update` method, has been updated to reflect that the error occurs when the YouTube account used to authorize the API request has not been merged with the user's Google account.

### April 20, 2016

This update contains the following changes:

- The definition of the `channels.update` method's [part](https://developers.google.com/youtube/v3/docs/channels/update#part) parameter has been updated to note that `localizations` is also a valid value for that parameter.

- The [Quota Usage](https://developers.google.com/youtube/v3/getting-started#quota) section of the Getting Started guide has been updated to link to the Google Developer's Console, where you can see your actual quota and quota usage.

### March 16, 2016

This update contains the following changes:

- **Updates to existing resources and methods**

  - The [channelBanner](https://developers.google.com/youtube/v3/docs/channelBanners) resource documentation has been updated to note that the recommended size for the uploaded channel banner image is 2560px by 1440px. The minimum size (2048px by 1152px) has not changed.

  - The `channel` resource's new [snippet.customUrl](https://developers.google.com/youtube/v3/docs/channels#snippet.customUrl) property identifies the custom URL associated with the channel. (Not all channels have custom URLs.) The [YouTube Help Center](https://support.google.com/youtube/answer/2657968) explains eligibility requirements for getting a custom URL as well as how to set up the URL.

  - The `channel` resource's `brandingSettings.watch` object and all of its child properties have been deprecated.

  - The API response to a `search.list` request now contains a [regionCode](https://developers.google.com/youtube/v3/docs/search/list#properties) property. The property identifies the region code that was used for the search query. The region code instructs the API to return search results for the specified country.

    The property value is a two-letter ISO country code that identifies the region. The [i18nRegions.list](https://developers.google.com/youtube/v3/docs/i18nRegions/list) method returns a list of supported regions. The default value is `US`. If a non-supported region is specified, YouTube might still select another region, rather than the default value, to handle the query.
  - The definitions of the `videoAbuseReportReason` resource's [snippet.label](https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons#snippet.label) and [snippet.secondaryReasons[].label](https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons#snippet.secondaryReasons[].label) properties have been updated to note that the properties contain localized label text for the abuse report reasons.

    In addition, the `videoAbuseReportReasons.list` method now supports the [hl](https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons/list#params) parameter, which specifies the language that should be used for label text in the API response. The default parameter value is `en_US`.
  - The `video` resource's new [contentDetails.contentRating.ecbmctRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.ecbmctRating) property identifies a video's rating from Turkey's Evaluation and Classification Board of the Ministry of Culture and Tourism.

    In addition, API properties for other rating systems support the following new property values:
    - `contentDetails.contentRating.fpbRating` (South Africa)  
      Rating: 10; property value: `fpb10`
    - `contentDetails.contentRating.moctwRating` (Taiwan)  
      Rating: R-12; property value: `moctwR12`
    - `contentDetails.contentRating.moctwRating` (Taiwan)  
      Rating: R-15; property value: `moctwR15`
  - The `video` resource's [liveStreamingDetails.activeLiveChatId](https://developers.google.com/youtube/v3/docs/videos#liveStreamingDetails.activeLiveChatId) property contains the ID of the active live chat associated with the video. The property value is only present if the video is a current live broadcast that has live chat enabled. After the broadcast ends and the live chat concludes, the property is no longer returned for the video.

  - The `video` resource's [status.rejectionReason](https://developers.google.com/youtube/v3/docs/videos#status.rejectionReason) property supports the new property value `legal`.

- The API supports the following new errors:

  |      Error type      |             Error detail              |                                                                                                                                                                                                       Description                                                                                                                                                                                                       |
  |----------------------|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | `badRequest (400)`   | `notEditable`                         | The [channelSections.insert](https://developers.google.com/youtube/v3/docs/channelSections/insert), [channelSections.update](https://developers.google.com/youtube/v3/docs/channelSections/update), and [channelSections.delete](https://developers.google.com/youtube/v3/docs/channelSections/delete) methods return this error to indicate that the specified channel section cannot be created, updated, or deleted. |
  | `badRequest (400)`   | `styleRequired`                       | The [channelSections.insert](https://developers.google.com/youtube/v3/docs/channelSections/insert) and [channelSections.update](https://developers.google.com/youtube/v3/docs/channelSections/update) methods return this error to indicate that the `channelSection` resource submitted in the API request must specify a value for the `snippet.style` property.                                                      |
  | `badRequest (400)`   | `typeRequired`                        | The [channelSections.insert](https://developers.google.com/youtube/v3/docs/channelSections/insert) and [channelSections.update](https://developers.google.com/youtube/v3/docs/channelSections/update) methods return this error to indicate that the `channelSection` resource submitted in the API request must specify a value for the `snippet.type` property.                                                       |
  | `badRequest (400)`   | `processingFailure`                   | The [commentThreads.list](https://developers.google.com/youtube/v3/docs/commentThreads/list) method returns this error to indicate that the API server failed to successfully process the request. While this can be a transient error, it usually indicates that the request's input is invalid. Check the structure of the `commentThread` resource in the request body to ensure that it is valid.                   |
  | `forbidden (403)`    | `commentsDisabled`                    | The [commentThreads.list](https://developers.google.com/youtube/v3/docs/commentThreads/list) method returns this error to indicate that the video identified by the [videoId](https://developers.google.com/youtube/v3/docs/commentThreads/list#videoId) parameter has disabled comments.                                                                                                                               |
  | `badRequest (400)`   | `commentTextTooLong`                  | The [commentThreads.insert](https://developers.google.com/youtube/v3/docs/commentThreads/insert) method returns this error to indicate that the `comment` resource that is being inserted contains too many characters in the `snippet.topLevelComment.snippet.textOriginal` property.                                                                                                                                  |
  | `invalidValue (400)` | `videoAlreadyInAnotherSeriesPlaylist` | The [playlistItems.insert](https://developers.google.com/youtube/v3/docs/playlistItems/insert) method returns this error to indicate that the video that you are trying to add to the playlist is already in another series playlist. See the [YouTube Help Center](https://support.google.com/youtube/answer/6084043) for more information about series playlists.                                                     |
  | `badRequest (400)`   | `subscriptionForbidden`               | The [subscriptions.insert](https://developers.google.com/youtube/v3/docs/subscriptions/insert) method returns this error to indicate that you have reached your maximum number of subscriptions or that you have created too many recent subscriptions. In the latter case, you can retry the request after a few hours.                                                                                                |
  | `badRequest (400)`   | `invalidCategoryId`                   | The [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) method returns this error to indicate that the `snippet.categoryId` property in the uploaded `video` resource specified an invalid category ID. Use the [videoCategories.list](https://developers.google.com/youtube/v3/docs/videoCategories/list) method to retrieve supported categories.                                            |
  | `badRequest (400)`   | `invalidDescription`                  | The [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) method returns this error to indicate that the `snippet.description` property in the uploaded `video` resource specified an invalid value.                                                                                                                                                                                             |
  | `badRequest (400)`   | `invalidPublishAt`                    | The [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) method returns this error to indicate that the `status.publishAt` property in the uploaded `video` resource specified an invalid scheduled publishing time.                                                                                                                                                                            |
  | `badRequest (400)`   | `invalidRecordingDetails`             | The [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) method returns this error to indicate that the `recordingDetails` object in the uploaded `video` resource specified invalid recording details.                                                                                                                                                                                         |
  | `badRequest (400)`   | `invalidTags`                         | The [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) method returns this error to indicate that the `snippet.tags` property in the uploaded `video` resource specified an invalid value.                                                                                                                                                                                                    |
  | `badRequest (400)`   | `invalidTitle`                        | The [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) method returns this error to indicate that the `snippet.title` property in the uploaded `video` resource specified an invalid or empty video title.                                                                                                                                                                                    |
  | `badRequest (400)`   | `invalidVideoMetadata`                | The [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) method returns this error to indicate that the request metadata is invalid. This error occurs if the request updates the [snippet](https://developers.google.com/youtube/v3/docs/videos#snippet) part of a `video` resource but does not set a value for both the `snippet.title` and `snippet.categoryId` properties.                 |

### December 18, 2015

European Union (EU) laws require that certain disclosures must be given to and consents obtained from end users in the EU. Therefore, for end users in the European Union, you must comply with the [EU User Consent Policy](http://www.google.com/about/company/user-consent-policy.html). We have added a notice of this requirement in our [YouTube API Terms of Service](https://developers.google.com/youtube/terms#notices-to-users).

### November 19, 2015

The API now supports the ability to set and retrieve localized text for the `snippet.title` and `snippet.description` properties of the [playlist](https://developers.google.com/youtube/v3/docs/playlists#snippet.localized) and [video](https://developers.google.com/youtube/v3/docs/videos#snippet.localized) resources, the `snippet.title` property of the [channelSection](https://developers.google.com/youtube/v3/docs/channelSections#snippet.localized) resource, and the `snippet.description` property of the [channel](https://developers.google.com/youtube/v3/docs/channels#snippet.localized) resource.

- **Setting localized titles and descriptions**

  You can set localized values for a resource when calling the `insert` or `update` method for that resource. To set localized values for a resource, do both of the following:
  - Ensure that a value is set for the resource's `snippet.defaultLanguage` property. That property identifies the language of the resource's `snippet.title` and `snippet.description` properties. Its value can be any [supported application language](https://developers.google.com/youtube/v3/docs/i18nLanguages/list) or most other ISO 639-1:2002 language codes. For example, if you upload a video that has an English title and description, you would set the [snippet.defaultLanguage](https://developers.google.com/youtube/v3/docs/videos#snippet.defaultLanguage) property to `en`.

    **Note for updating `channel` resources:** To set the `snippet.defaultLanguage` property for a `channel` resource, you actually need to update the [brandingSettings.channel.defaultLanguage](https://developers.google.com/youtube/v3/docs/channels#brandingSettings.channel.defaultLanguage) property.
  - Add the `localizations` object to the resource you are updating. Each object key is a string that identifies an application language or ISO 639-1:2002 language code, and each key maps to an object that contains the localized title (and description) for the resource.

    The sample snippet below sets the resource's default language to English. It also adds localized German and Spanish titles and descriptions to a video:  

    ```
    {
      "kind": "youtube#video",
      ...
      "snippet": {
        "title": "Playing soccer",
        "description": "We play soccer in the park on Sundays.",
        "defaultLanguage": "en",
        ...
      },
      "localizations":
        "de": {
          "title": "FuÃball spielen",
          "description": "Wir spielen FuÃball im Park am Sonntag"
        },
        "es": {
          "title": "Jugar al fÃºtbol",
          "description": "Nosotros jugamos fÃºtbol en el parque los domingos",
        }
      }
    }
    ```
  - **Important:** Remember that when you update the localized data for a resource, your API request must include all of the existing localized versions of the data. For example, if you sent a subsequent request to add Portuguese data to the video in the example above, the request would need to include the localized data for German, Spanish, and Portuguese.
- **Retrieving localized values**

  The API supports two ways to retrieve localized values for a resource:
  - Add the `hl` parameter to your [channels.list](https://developers.google.com/youtube/v3/docs/channels/list#hl), [channelSections.list](https://developers.google.com/youtube/v3/docs/channelSections/list#hl), [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list#hl), or [videos.list](https://developers.google.com/youtube/v3/docs/videos/list#hl) request to retrieve localized data for a specific [application language that the YouTube website supports](https://developers.google.com/youtube/v3/docs/i18nLanguages). If localized resource details are available in that language, the resource's `snippet.localized` object will contain the localized values. However, if localized details are not available, the `snippet.localized` object will contain resource details in the resource's [default language](https://developers.google.com/youtube/v3/docs/videos#snippet.defaultLanguage).

    For example, suppose a `videos.list` request retrieved data for the video described above with localized German and Spanish data. If the `hl` parameter were set to `de`, the resource would contain the following data:  

    ```
    {
      "kind": "youtube#video",
      ...
      "snippet": {
        "title": "Playing soccer",
        "description": "We play soccer in the park on Sundays.",
        "defaultLanguage": "en",
        "localized": {
          "title": "FuÃball spielen",
          "description": "Wir spielen FuÃball im Park am Sonntag"
        }
        ...
      }
    }
    ```

    However, if the `hl` parameter were set to `fr`, the `snippet.localized` object would contain the English title and description because English is the default language for the resource, and localized French details are not available.  
    **Important:** The `hl` parameter only supports values that identify application languages that the YouTube website supports. To determine whether localized text is available for other languages, you need to retrieve the `localizations` part for the resource and filter to determine whether the localized text exists.  

    For example, you would need to retrieve the full list of localizations to determine whether localized text is available in Appalachian English.

  - When retrieving a resource, include `localizations` in the `part` parameter value to retrieve all of the localized details for that resource. If you are retrieving localized data for a language that is not a [current YouTube application language](https://developers.google.com/youtube/v3/docs/i18nLanguages/list), you need to use this approach to retrieve all localizations and then filter to determine whether the desired localized data exists.

- **Errors related to localized text values**

  The API also supports the following new errors for localized text values:

  |     Error type     |         Error detail          |                                                                                                                                                                                                                                                                                                                                                                                                                          Description                                                                                                                                                                                                                                                                                                                                                                                                                          |
  |--------------------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | `badRequest (400)` | `defaultLanguageNotSetError`  | This error indicates that a request that tries to insert or update the `localizations` object for a resource is failing because the `snippet.defaultLanguage` property is not set for that resource. The [channels.update](https://developers.google.com/youtube/v3/docs/channels/update), [channelSections.insert](https://developers.google.com/youtube/v3/docs/channelSections/insert), [channelSections.update](https://developers.google.com/youtube/v3/docs/channelSections/update), [playlists.insert](https://developers.google.com/youtube/v3/docs/playlists/insert), [playlists.update](https://developers.google.com/youtube/v3/docs/playlists/update), [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert), and [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) methods support this error. |
  | `badRequest (400)` | `localizationValidationError` | This error indicates that one of the values in a resource's `localizations` object failed to validate. For example, this error might occur if the object contains an invalid language code. The [channels.update](https://developers.google.com/youtube/v3/docs/channels/update), [channelSections.insert](https://developers.google.com/youtube/v3/docs/channelSections/insert), [channelSections.update](https://developers.google.com/youtube/v3/docs/channelSections/update), [playlists.insert](https://developers.google.com/youtube/v3/docs/playlists/insert), and [playlists.update](https://developers.google.com/youtube/v3/docs/playlists/update) methods support this error.                                                                                                                                                                      |

### November 4, 2015

This update contains the following changes:

- **Updates to existing resources and methods**

  - The `search.list` method's [order](https://developers.google.com/youtube/v3/docs/search/list#order) parameter has been updated to note that if you sort live broadcasts by `viewCount`, the API results are sorted by the broadcasts' number of concurrent viewers while the broadcasts are still ongoing.

  - The `search.list` method's [relatedToVideoId](https://developers.google.com/youtube/v3/docs/search/list#relatedToVideoId) parameter has been updated to note that if the parameter is set, the only other supported parameters are [part](https://developers.google.com/youtube/v3/docs/search/list#part), [maxResults](https://developers.google.com/youtube/v3/docs/search/list#maxResults), [pageToken](https://developers.google.com/youtube/v3/docs/search/list#pageToken), [regionCode](https://developers.google.com/youtube/v3/docs/search/list#regionCode), [relevanceLanguage](https://developers.google.com/youtube/v3/docs/search/list#relevanceLanguage), [safeSearch](https://developers.google.com/youtube/v3/docs/search/list#safeSearch), [type](https://developers.google.com/youtube/v3/docs/search/list#type) (which must be set to `video`), and [fields](https://developers.google.com/youtube/v3/docs/search/list#fields). This update does not reflect a change in API behavior.

  - The definition of the `video` resource's [snippet.publishedAt](https://developers.google.com/youtube/v3/docs/videos#snippet.publishedAt) property has been updated to note that the property value, which specifies the date and time that the video was published, might be different than the time that the video was uploaded. For example, if a video is uploaded as a private video and then made public at a later time, the property value specifies the time that the video was made public. The updated definition also explains how the value is populated for private and unlisted videos.

    This change does not reflect a change in API behavior.
  - The definition of the `video` resource's [status.publishAt](https://developers.google.com/youtube/v3/docs/videos#status.publishAt) property has been updated to note:

    - If you set this property's value when calling the [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) method, you must also set the [status.privacyStatus](https://developers.google.com/youtube/v3/docs/videos/update#status.privacyStatus) property value to `private` even if the video is already private.
    - If the request schedules a video to be published at some time in the past, it is published right away. As such, the effect of setting the `status.publishAt` property to a past date and time is the same as of changing the video's [privacyStatus](https://developers.google.com/youtube/v3/docs/videos/update#status.privacyStatus) from `private` to `public`.
  - The `video` resource's [contentDetails.contentRating.cncRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.cncRating) property specifies the video's rating from France's Commission de classification cinematographique. This property replaces the `contentDetails.contentRating.fmocRating` property, which is now deprecated.

  - The definition of the `channel` resource's [brandingSettings.channel.keywords](https://developers.google.com/youtube/v3/docs/channels#brandingSettings.channel.keywords) has been updated to correctly reflect that the property value contains a space-separated list of strings and not a comma-separated list, as previously documented. This update does not reflect a change in API behavior.

  - The documentation for the [thumbnails.set](https://developers.google.com/youtube/v3/docs/thumbnails/set#request-body) method has been updated to accurately reflect that the body of the request contains the thumbnail image that you are uploading and associating with a video. The request body does not contain a [thumbnail](https://developers.google.com/youtube/v3/docs/thumbnails#resource-representation) resource. Previously, the documentation said that you should not provide a request body when calling this method. This update does not reflect a change in API behavior.

  - The description of the [activity](https://developers.google.com/youtube/v3/docs/activities) resource has been updated to reflect the fact that the `activities.list` method does not currently include resources related to new video comments. The resource's [snippet.type](https://developers.google.com/youtube/v3/docs/activities#snippet.type) and [contentDetails.comment](https://developers.google.com/youtube/v3/docs/activities#contentDetails.comment) have been updated as well.

- **New and updated errors**

  - The API now supports the following errors:

    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Error details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ||
    |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [activities.insert](https://developers.google.com/youtube/v3/docs/activities/insert)                                                                                                                                                                     | |--------------------|-------------------------------------------------------------| | HTTP Response Code | `badRequest (400)`                                          | | Reason             | `invalidMetadata`                                           | | Description        | The `kind` property does not match the type of ID provided. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    | `commentThreads.update` [comments.insert](https://developers.google.com/youtube/v3/docs/comments/insert) [comments.update](https://developers.google.com/youtube/v3/docs/comments/update)                                                                | |--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------| | HTTP Response Code | `badRequest (400)`                                                                                                                                    | | Reason             | `commentTextTooLong`                                                                                                                                  | | Description        | The `comment` resource that is being inserted or updated contains too many characters in the `snippet.topLevelComment.snippet.textOriginal` property. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | [playlistItems.insert](https://developers.google.com/youtube/v3/docs/playlistItems/insert) [playlistItems.update](https://developers.google.com/youtube/v3/docs/playlistItems/update)                                                                    | |--------------------|--------------------------------------------------------------------------------------------------| | HTTP Response Code | `forbidden (403)`                                                                                | | Reason             | `playlistItemsNotAccessible`                                                                     | | Description        | The request is not properly authorized to insert, update, or delete the specified playlist item. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
    | [playlists.delete](https://developers.google.com/youtube/v3/docs/playlists/delete) [playlists.insert](https://developers.google.com/youtube/v3/docs/playlists/insert) [playlists.update](https://developers.google.com/youtube/v3/docs/playlists/update) | |--------------------|------------------------------------------------------------------------| | HTTP Response Code | `badRequest (400)`                                                     | | Reason             | `playlistForbidden`                                                    | | Description        | This operation is forbidden or the request is not properly authorized. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | [search.list](https://developers.google.com/youtube/v3/docs/search/list)                                                                                                                                                                                 | |--------------------|-----------------------------------------------------------------------------------| | HTTP Response Code | `badRequest (400)`                                                                | | Reason             | `invalidLocation`                                                                 | | Description        | The `location` and/or `locationRadius` parameter value was formatted incorrectly. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | [search.list](https://developers.google.com/youtube/v3/docs/search/list)                                                                                                                                                                                 | |--------------------|--------------------------------------------------------------------| | HTTP Response Code | `badRequest (400)`                                                 | | Reason             | `invalidRelevanceLanguage`                                         | | Description        | The `relevanceLanguage` parameter value was formatted incorrectly. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | [subscriptions.insert](https://developers.google.com/youtube/v3/docs/subscriptions/insert)                                                                                                                                                               | |--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | HTTP Response Code | `badRequest (400)`                                                                                                                                                                                                                                                                                                                                                            | | Reason             | `subscriptionForbidden`                                                                                                                                                                                                                                                                                                                                                       | | Description        | This error occurs when any of the following are true: - The subscription that you are trying to create already exists - You have already reached your maximum number of subscriptions - You are trying to subscribe to your own channel, which is not supported. - You have created too many subscriptions recently and need to wait a few hours before retrying the request. | |
    | [videos.update](https://developers.google.com/youtube/v3/docs/videos/update)                                                                                                                                                                             | |--------------------|-----------------------------------------------------------------------------------| | HTTP Response Code | `badRequest (400)`                                                                | | Reason             | `invalidDefaultBroadcastPrivacySetting`                                           | | Description        | The request attempts to set an invalid privacy setting for the default broadcast. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### August 28, 2015

This update contains the following changes:

- **Updates to existing resources and methods**

  - The `video` resource's [statistics.favoriteCount](https://developers.google.com/youtube/v3/docs/videos#statistics.favoriteCount) property has been deprecated.

    In accordance with our deprecation policy, this property will continue to be included in `video` resources for at least one year after this announcement. However, the property value is now always set to `0`.

### August 7, 2015

This update contains the following changes:

- **Updates to existing resources and methods**

  - The definition of the `video` resource's [snippet.tags[]](https://developers.google.com/youtube/v3/docs/videos#snippet.tags[]) property has been updated to provide more information about how the API server calculates the length of the property's value. Note that this update does not reflect a change in the API's behavior.

    Specifically, the definition now explains that if a tag contains a space, the API server handles the tag value as though it were wrapped in quotation marks, and the quotation marks count toward the character limit. So, for the purposes of character limits, the tag Foo-Baz contains seven characters, but the tag Foo Baz contains nine characters.
  - The [commentThreads.insert](https://developers.google.com/youtube/v3/docs/commentThreads/insert) method no longer supports the `shareOnGooglePlus` parameter, which previously indicated whether a comment and replies to that comment should also be posted to the author's Google+ profile. If a request submits the parameter, the API server ignores the parameter but otherwise handles the request.

### June 18, 2015

This update contains the following changes:

- **Updates to existing resources and methods**

  - The `commentThreads.list` method's new [order](https://developers.google.com/youtube/v3/docs/commentThreads/list#order) parameter specifies the order in which the API response should list comment threads. Threads can be ordered by time or relevance. The default behavior is to order them by time.

  - The `video` resource's new [snippet.defaultAudioLanguage](https://developers.google.com/youtube/v3/docs/videos#snippet.defaultAudioLanguage) property specifies the language spoken in the video's default audio track.

  - The definition of the `video` resource's [contentDetails.licensedContent](https://developers.google.com/youtube/v3/docs/videos#contentDetails.licensedContent) property has been updated to clarify that the content must have been originally uploaded to a channel linked to a YouTube content partner and then claimed by that partner. This does not represent a change in actual API behavior.

  - The [captions.delete](https://developers.google.com/youtube/v3/docs/captions/delete#params), [captions.download](https://developers.google.com/youtube/v3/docs/captions/download#params), [captions.insert](https://developers.google.com/youtube/v3/docs/captions/insert#params), [captions.list](https://developers.google.com/youtube/v3/docs/captions/list#params), and [captions.update](https://developers.google.com/youtube/v3/docs/captions/update#params) methods now support the `onBehalfOfContentOwner` parameter, which is already supported for several other methods. Requests that use that method also need to be authorized with a token that provides access to the `https://www.googleapis.com/auth/youtubepartner` scope.

- **New and updated errors**

  - The API now supports the following errors:

    |                                                                                                                                                                                                                     Error details                                                                                                                                                                                                                     ||
    |--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [videos.rate](https://developers.google.com/youtube/v3/docs/videos/rate) | |--------------------|-------------------------------------------------------------------| | HTTP Response Code | `badRequest (400)`                                                | | Reason             | `emailNotVerified`                                                | | Description        | The user must verify her email address prior to rating the video. | |
    | [videos.rate](https://developers.google.com/youtube/v3/docs/videos/rate) | |--------------------|-----------------------------------------------------------| | HTTP Response Code | `badRequest (400)`                                        | | Reason             | `videoPurchaseRequired`                                   | | Description        | Rental videos can only be rated by users who rented them. |                                 |

  - The [subscriptions.delete](https://developers.google.com/youtube/v3/docs/subscriptions/delete#errors) and [subscriptions.insert](https://developers.google.com/youtube/v3/docs/subscriptions/insert#errors) methods no longer support the `accountClosed` and `accountSuspended` errors.

### April 27, 2015

This update contains the following changes:

- **New resources and methods**

  - The new [videoAbuseReportReason](https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons) resource contains information about a reason that a video would be flagged for containing abusive content. The [videoAbuseReportReasons.list](https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons/list) method lets you retrieve a list of all of the reasons why videos might be flagged.

  - The new [videos.reportAbuse](https://developers.google.com/youtube/v3/docs/videos/reportAbuse) method provides a way to actually flag a video that contains abusive content. The body of the request contains a JSON object that specifies the video being flagged as well as the reason that the video is deemed to contain abusive content. Valid reasons can be obtained from the [videoAbuseReportReason.list](https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons/list) method described above.

    The [migration guide](https://developers.google.com/youtube/v3/migration-guide#videos) has also been updated with an example for reporting an abusive video. With this change, the v3 API now supports all of the v2 API features that it is scheduled to support. These features are also all explained in the migration guide.
- **Updates to existing resources and methods**

  - The `search.list` method's new [forDeveloper](https://developers.google.com/youtube/v3/docs/search/list#forDeveloper) filter parameter restricts a search to only retrieve videos uploaded via the developer's application or website. The `forDeveloper` parameter can be used in conjunction with optional search parameters like the `q` parameter.

    For this feature, each uploaded video is automatically tagged with the project number that is associated with the developer's application in the [Google Developers Console](https://console.developers.google.com).

    When a search request subsequently sets the `forDeveloper` parameter to `true`, the API server uses the request's authorization credentials to identify the developer. Therefore, a developer can restrict results to videos uploaded through the developer's own app or website but not to videos uploaded through other apps or sites.

    The new feature offers functionality that is similar, albeit not identical, to the [developer tags](https://developers.google.com/youtube/2.0/developers_guide_protocol_uploading_videos#Assigning_Developer_Tags) functionality that the v2 API supported.
  - The `channel` resource's new [snippet.country](https://developers.google.com/youtube/v3/docs/channels#snippet.country) property lets channel owners associate their channels with a particular country.

    **Note:** To set the `snippet.country` property for a `channel` resource, you actually need to update the [brandingSettings.channel.country](https://developers.google.com/youtube/v3/docs/channels#brandingSettings.channel.country) property.
  - The API now supports targeting for [channelSection](https://developers.google.com/youtube/v3/docs/channelSections) resources. Channel section targeting provides a way to restrict visibility of a content section to users that match particular criteria.

    The API exposes three targeting options. A user must meet all of the targeting settings for a channel section to be visible.
    - [targeting.languages[]](https://developers.google.com/youtube/v3/docs/channelSections#targeting.languages[]): A list of [YouTube application languages](https://developers.google.com/youtube/v3/docs/i18nLanguages). Users who have chosen one of those languages can see the corresponding channel section.

    - [targeting.regions[]](https://developers.google.com/youtube/v3/docs/channelSections#targeting.regions[]): A list of [YouTube preferred content regions](https://developers.google.com/youtube/v3/docs/i18nRegions). The channel section is visible to users that have selected one of those regions as well as users for whom one of those regions is automatically selected.

    - [targeting.countries[]](https://developers.google.com/youtube/v3/docs/channelSections#targeting.countries[]): A list of countries where the channel section is visible. Each value in the list is an [ISO 3166-1 alpha-2 country code](http://www.iso.org/iso/country_codes/iso_3166_code_lists/country_names_and_code_elements.htm).

  - The definition of the `video` resource's [contentDetails.duration](https://developers.google.com/youtube/v3/docs/videos#contentDetails.duration) property has been corrected to reflect that the value can reflect hours, days, and so forth.

  - The documentation for the `channelSections.delete`, `playlistItems.delete`, `playlists.delete`, `subscriptions.delete`, and `videos.delete` method has been corrected to reflect that, when successful, those methods all return an HTTP `204` response code (`No Content`).

- **New and updated errors**

  - The API now supports the following errors:

    |     Error type     |      Error detail       |                                                                                                                                                                                                                         Description                                                                                                                                                                                                                         |
    |--------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | `badRequest (400)` | `targetInvalidCountry`  | The [channelSections.insert](https://developers.google.com/youtube/v3/docs/channelSections/insert) and [channelSections.update](https://developers.google.com/youtube/v3/docs/channelSections/update) methods return this error if the inserted `channelSection` resource contained an invalid value for the `targeting.countries[]` property.                                                                                                              |
    | `badRequest (400)` | `targetInvalidLanguage` | The [channelSections.insert](https://developers.google.com/youtube/v3/docs/channelSections/insert) and [channelSections.update](https://developers.google.com/youtube/v3/docs/channelSections/update) methods return this error if the inserted `channelSection` resource contained an invalid value for the `targeting.languages[]` property.                                                                                                              |
    | `badRequest (400)` | `targetInvalidRegion`   | The [channelSections.insert](https://developers.google.com/youtube/v3/docs/channelSections/insert) and [channelSections.update](https://developers.google.com/youtube/v3/docs/channelSections/update) methods return this error if the inserted `channelSection` resource contained an invalid value for the `targeting.regions[]` property.                                                                                                                |
    | `badRequest (400)` | `operationNotSupported` | The [comments.insert](https://developers.google.com/youtube/v3/docs/comments/insert) method returns this error if the API user is not able to insert a comment in reply to the top-level comment identified by the `snippet.parentId` property. In a `commentThread` resource, the [snippet.canReply](https://developers.google.com/youtube/v3/docs/commentThreads#snippet.canReply) property indicates whether the current viewer can reply to the thread. |
    | `badRequest (400)` | `invalidChannelId`      | The [search.list](https://developers.google.com/youtube/v3/docs/search/list) method returns this error if the `channelId` parameter in the request specified an invalid channel ID.                                                                                                                                                                                                                                                                         |
    | `badRequest (400)` | `subscriptionForbidden` | The [subscriptions.insert](https://developers.google.com/youtube/v3/docs/subscriptions/insert) method returns this error if the API user tries to subscribe to the user's own channel.                                                                                                                                                                                                                                                                      |

  - The [captions.update](https://developers.google.com/youtube/v3/docs/captions/update#errors) method no longer supports the `invalidMetadata` and `videoNotFound` errors.

### April 16, 2015

This update contains the following changes:

- The [migration guide](https://developers.google.com/youtube/v3/migration-guide#comments) has been updated to explain how to migrate applications still using comments functionality from the v2 API.

  The guide also calls out several commenting features that the v2 API did not support but that are [supported in the v3 API](https://developers.google.com/youtube/v3/migration-guide#new-in-v3). These include:

  <br />

  - Retrieving comments about a channel
  - Retrieving all comment threads related to a channel, which means that the API response can contain comments about the channel or any of its videos.
  - Updating the text of a comment
  - Marking a comment as spam
  - Setting a comment's moderation status

  <br />

- The [Subscribing to push notifications](https://developers.google.com/youtube/v3/guides/push_notifications) guide has been updated to reflect the fact that notifications are only pushed to the Google PubSubHubBub hub and not also to the Superfeedr hub as previously indicated.

### April 9, 2015

This update contains the following changes:

- The API's new [commentThread](https://developers.google.com/youtube/v3/docs/commentThreads) and [comment](https://developers.google.com/youtube/v3/docs/comments) resources let you retrieve, insert, update, delete, and moderate comments.

  - A `commentThread` resource contains information about a YouTube comment thread, which comprises a top-level comment and replies, if any exist, to that comment. A `commentThread` resource can represent comments about either a video or a channel.

    The top-level comment and the replies are actually `comment` resources that are nested inside the `commentThread` resource. It is important to note that the `commentThread` resource does not necessarily contain all replies to a comment, and you need to use the [comments.list](https://developers.google.com/youtube/v3/docs/comments/list) method if you want to retrieve all replies for a particular comment. In addition, some comments do not have replies.

    The API supports the following methods for `commentThread` resources:

    <br />

    - [commentThreads.list](https://developers.google.com/youtube/v3/docs/commentThreads/list) -- Retrieve a list of comment threads. Use this method to retrieve comments associated with a particular video or channel.
    - [commentThreads.insert](https://developers.google.com/youtube/v3/docs/commentThreads/insert) -- Create a new top-level comment. (Use the [comments.insert](https://developers.google.com/youtube/v3/docs/comments/insert) method to reply to an existing comment.)
    - `commentThreads.update` -- Modify a top-level comment.

    <br />

  - A `comment` resource contains information about a single YouTube comment. A `comment` resource can represent a comment about either a video or a channel. In addition, the comment could be a top-level comment or a reply to a top-level comment.

    The API supports the following methods for `comment` resources:

    <br />

    - [comments.list](https://developers.google.com/youtube/v3/docs/comments/list) -- Retrieve a list of comment. Use this method to retrieve all of the replies to a particular comment.
    - [comments.insert](https://developers.google.com/youtube/v3/docs/comments/insert) -- Create a reply to an existing comment.
    - [comments.update](https://developers.google.com/youtube/v3/docs/comments/update) -- Modify a comment.
    - [comments.markAsSpam](https://developers.google.com/youtube/v3/docs/comments/markAsSpam) -- Flag one or more comments as spam.
    - [comments.setModerationStatus](https://developers.google.com/youtube/v3/docs/comments/setModerationStatus) -- Set the moderation status of one or more comments. For example, clear a comment for public display or reject a comment as unfit for display. The API request must be authorized by the owner of the channel or video associated with the comments..
    - [comments.delete](https://developers.google.com/youtube/v3/docs/comments/delete) -- Delete a comment.

    <br />

  Note that the API's new `https://www.googleapis.com/auth/youtube.force-ssl` scope, described in the [revision history for April 2, 2015](https://developers.google.com/youtube/v3/revision_history#release_notes_04_02_2015), is required for calls to the [comments.insert](https://developers.google.com/youtube/v3/docs/comments/insert), [comments.update](https://developers.google.com/youtube/v3/docs/comments/update), [comments.markAsSpam](https://developers.google.com/youtube/v3/docs/comments/markAsSpam), [comments.setModerationStatus](https://developers.google.com/youtube/v3/docs/comments/setModerationStatus), [comments.delete](https://developers.google.com/youtube/v3/docs/comments/delete), [commentThreads.insert](https://developers.google.com/youtube/v3/docs/commentThreads/insert), and `commentThreads.update` methods.
- The new [Subscribing to push notifications](https://developers.google.com/youtube/v3/guides/push_notifications) guide explains the API's new support for push notifications via [PubSubHubBub](https://github.com/pubsubhubbub/), a server-to-server publish/subscribe protocol for Web-accessible resources. Your PubSubHubBub callback server can receive Atom feed notifications when a channel does any of the following activities:

  <br />

  - uploads a video
  - updates a video's title
  - updates a video's description

  <br />

- The [migration guide](https://developers.google.com/youtube/v3/migration-guide#deprecated) has also been updated to note the new support for push notifications. However, since the v2 API supported numerous other types of push notifications that are not supported in the v3 API, the mention of PubSubHubBub support is still listed in the **Deprecated** section of that guide.

- The API's new `https://www.googleapis.com/auth/youtube.force-ssl` scope is now a valid scope for any API method that previously supported the `https://www.googleapis.com/auth/youtube` scope.

- The API now supports the following errors:

  |     Error type     |  Error detail   |                                                                                   Description                                                                                   |
  |--------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | `badRequest (400)` | `invalidRating` | The [videos.rate](https://developers.google.com/youtube/v3/docs/videos/rate) method returns this error if the request contained an unexpected value for the `rating` parameter. |

- The `subscriptions.insert` method no longer supports the `subscriptionLimitExceeded` error, which previously indicated that the subscriber identified with the request had exceeded the subscription rate limit.

### April 2, 2015

This update contains the following changes:

- The new [captions](https://developers.google.com/youtube/v3/docs/captions) resource represents a YouTube caption track. A caption track is associated with exactly one YouTube video.

  The API supports methods to [list](https://developers.google.com/youtube/v3/docs/captions/list), [insert](https://developers.google.com/youtube/v3/docs/captions/insert), [update](https://developers.google.com/youtube/v3/docs/captions/update), [download](https://developers.google.com/youtube/v3/docs/captions/download), and [delete](https://developers.google.com/youtube/v3/docs/captions/delete) caption tracks.
- The [migration guide](https://developers.google.com/youtube/v3/migration-guide) has also been updated to explain how to migrate applications still using captions functionality in the v2 API.

- The API's new `https://www.googleapis.com/auth/youtube.force-ssl` scope requires communication with the API server to happen over an SSL connection.

  This new scope grants the same access as the `https://www.googleapis.com/auth/youtube` scope. And, in fact, those two scopes are functionally identical because the YouTube API server is only available via an HTTPS endpoint. As a result, even though the `https://www.googleapis.com/auth/youtube` scope does not require an SSL connection, there is actually no other way to make an API request.

  The new scope is required for calls to the all of the `caption` resource's methods.

### March 11, 2015

This update contains the following changes:

- The [YouTube Data API (v3) migration guide](https://developers.google.com/youtube/v3/migration-guide#new-in-v3) contains a new tab, named **New in the v3 API** , that lists features that the v3 API does support and that the v2 API did not support. The same features were previously and are still listed in other tabs in the guide. For example, the new feature explaining how to update a channel's in-video promotional campaign data is also listed under the **Channels (profiles)** tab.

- The [YouTube Data API (v3) migration guide](https://developers.google.com/youtube/v3/migration-guide) has been updated to note that the v3 API will support the following v2 API feature:

  - [Flagging a video](https://developers.google.com/youtube/2.0/developers_guide_protocol_complaints)

- The [YouTube Data API (v3) migration guide](https://developers.google.com/youtube/v3/migration-guide) has been updated to note that the following v2 API features will not be supported in the v3 API:

  - [Retrieve video recommendations](https://developers.google.com/youtube/2.0/developers_guide_protocol_recommendations) -- The v3 API does not retrieve a list that only contains videos recommended for the current API user. However, you can use the v3 API to find recommended videos by calling the [activities.list](https://developers.google.com/youtube/v3/docs/activities/list) method and setting the [home](https://developers.google.com/youtube/v3/docs/activities/list#home) parameter value to `true`.

    In the API response, a resource corresponds to a recommended video if the [snippet.type](https://developers.google.com/youtube/v3/docs/activities/list#snippet.type) property's value is `recommendation`. In that case, the [contentDetails.recommendation.reason](https://developers.google.com/youtube/v3/docs/activities#contentDetails.recommendation.reason) and [contentDetails.recommendation.seedResourceId](https://developers.google.com/youtube/v3/docs/activities#contentDetails.recommendation.seedResourceId) properties will contain information about why the video was recommended. Note that there is no guarantee that the response will contain any particular number of recommended videos.
  - [Retrieve channel suggestions](https://developers.google.com/youtube/2.0/developers_guide_protocol_channel_suggestions)

  - [Retrieve new subscription videos](https://developers.google.com/youtube/2.0/developers_guide_protocol_subscriptions#Retrieving_new_subscription_videos) -- The v3 API does not retrieve a list that only contains videos that have recently been uploaded to channels that the API user subscribes to. However, you can use the v3 API to find new subscription videos by calling the [activities.list](https://developers.google.com/youtube/v3/docs/activities/list) method and setting the [home](https://developers.google.com/youtube/v3/docs/activities/list#home) parameter value to `true`.

    In the API response, a resource corresponds to a new subscription video if the [snippet.type](https://developers.google.com/youtube/v3/docs/activities/list#snippet.type) property's value is `upload`. Note that there is no guarantee that the response will contain any particular number of new subscription videos.
  - [RSS feed support](https://developers.google.com/youtube/2.0/developers_guide_protocol_api_query_parameters#altsp)

  - [Push notifications for feed updates](https://developers.google.com/youtube/2.0/developers_guide_protocol_sup) -- The v2 API supported push notifications, using either the Simple Update Protocol (SUP) or [PubSubHubbub](http://youtube-eng.blogspot.ch/2010/10/pubsubhubbub-for-youtube-activities_7.html), to monitor user activity feeds for YouTube users. Notifications were provided for new channel subscriptions and when videos were rated, shared, marked as favorites, commented on, or uploaded.

    The v3 API will support push notifications using the [PubSubHubbub protocol](https://github.com/pubsubhubbub/), but the notifications will only cover video uploads and updates to video titles or video descriptions.
  - [Channel location](https://developers.google.com/youtube/2.0/reference#youtube_data_api_tag_yt:location) -- The v2 API used the `<yt:location>` tag to identify the user's location as entered in the channel's YouTube public profile. While some developers used this field to associate a channel with a particular country, the field's data could not consistently be used for that purpose.

  - [Set or retrieve developer tags](https://developers.google.com/youtube/2.0/developers_guide_protocol_uploading_videos#Assigning_Developer_Tags) -- The v2 API supported the ability to associate keywords, or developer tags, with a video at the time that the video was uploaded. Developer tags would not be displayed to YouTube users, but video owners could retrieve videos that matched a specific developer tag.

    The v3 API will provide a similar, but not identical, feature. Specifically, a developer will be able to search for videos uploaded by the developer's own application. For this feature, each uploaded video is automatically tagged with the project number that is associated with the developer's application in the [Google Developers Console](https://console.developers.google.com). The developer then uses the same project number to search for videos.
  - [List videos by publication date, viewcount, or rating](https://developers.google.com/youtube/2.0/developers_guide_protocol_api_query_parameters#orderbysp) -- In the v2 API, the `orderby` parameter let you sort videos in a playlist by position, duration, publication date, title, and several other values. In the v3 API, playlist items are typically sorted by position in ascending order and other sorting options are not available.

    There are a few exceptions. A new upload, favorite video, liked video, or recently watched video is automatically added as the first item (`snippet.position`=`0`) for the following types of playlists. So, each of these lists is effectively sorted in order of newest to oldest item based on the times that items were added to the list.

    <br />

    - user uploads
    - favorite videos
    - liked videos
    - watch history

    <br />

    Note, however, that a new item added to the "Watch later" playlist is added as the last item in that list, so that list is effectively sorted from oldest to newest item.
  - [Batch processing](https://developers.google.com/youtube/2.0/developers_guide_protocol_batch_processing) -- The v3 API supports one of the batch processing use cases that the v2 API had supported. The v3 API's [channels.list](https://developers.google.com/youtube/v3/docs/channels/list#id), [channelSections.list](https://developers.google.com/youtube/v3/docs/channelSections/list#id), [guideCategories.list](https://developers.google.com/youtube/v3/docs/guideCategories/list#id), [playlistItems.list](https://developers.google.com/youtube/v3/docs/playlistItems/list#id), [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list#id), [subscriptions.list](https://developers.google.com/youtube/v3/docs/subscriptions/list#id), [videoCategories.list](https://developers.google.com/youtube/v3/docs/videoCategories/list#id), and [videos.list](https://developers.google.com/youtube/v3/docs/videos/list#id) methods all support an `id` parameter, which can be used to specify a comma-delimited list of IDs (video IDs, channel IDs, etc.). Using those methods, you can retrieve a list of multiple resources with a single request.

  With these changes, the guide now identifies all functionality that was supported in the old (v2) API that will be deprecated in the current API version (v3).

### March 4, 2015

This update contains the following changes:

- The [channelSections.delete](https://developers.google.com/youtube/v3/docs/channelSections/delete#params) and [channelSections.update](https://developers.google.com/youtube/v3/docs/channelSections/update#params) methods now support the `onBehalfOfContentOwner` parameter, which is already supported for several other methods.

- The following properties and their child properties have been deprecated:

  <br />

  - `brandingSettings.image.backgroundImageUrl`
  - `brandingSettings.image.largeBrandedBannerImageImapScript`
  - `brandingSettings.image.largeBrandedBannerImageUrl`
  - `brandingSettings.image.smallBrandedBannerImageImapScript`
  - `brandingSettings.image.smallBrandedBannerImageUrl`

  <br />

  **Note:** None of these properties had been subject to the API Deprecation Policy.
- The `video` resource's new [contentDetails.contentRating.contentDetails.contentRating.djctqRatingReasons](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.djctqRatingReasons) property identifies the reasons that explain why the video received its DJCQT (Brazil) rating.

- The API now supports the following errors:

  |     Error type     |           Error detail           |                                                                                                                                                                                                                                                                                                                                                                                   Description                                                                                                                                                                                                                                                                                                                                                                                    |
  |--------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | `notFound (404)`   | `channelNotFound`                | The [channels.update](https://developers.google.com/youtube/v3/docs/channels/update) method returns this error if the request's `id` parameter specifies a channel that cannot be found.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
  | `badRequest (400)` | `manualSortRequiredinvalidValue` | The [playlistItems.insert](https://developers.google.com/youtube/v3/docs/playlistItems/insert) and [playlistItems.update](https://developers.google.com/youtube/v3/docs/playlistItems/update) methods return this error if the request attempts to set the playlist item's position, but the playlist does not use manual sorting. For example, playlist items might be sorted by date or popularity. You can address this error by removing the `snippet.position` element from the resource sent in the request body. If you want the playlist item to have a specific position in the list, you need to first update the playlist's ordering setting to **Manual** . THis setting can be adjusted in the [YouTube Video Manager](https://www.youtube.com/view_all_playlists). |
  | `forbidden (403)`  | `channelClosed`                  | The [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list) method returns this error if the request's `channelId` parameter specifies a channel that has been closed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  | `forbidden (403)`  | `channelSuspended`               | The [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list) method returns this error if the request's `channelId` parameter specifies a channel that has been suspended.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  | `forbidden (403)`  | `playlistForbidden`              | The [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list) method returns this error if the request's `id` parameter does not support the request or the request is not properly authorized.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  | `notFound (404)`   | `channelNotFound`                | The [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list) method returns this error if the request's `channelId` parameter specifies a channel that cannot be found.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  | `notFound (404)`   | `playlistNotFound`               | The [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list) method returns this error if the request's `id` parameter specifies a playlist that cannot be found.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  | `notFound (404)`   | `videoNotFound`                  | The [videos.list](https://developers.google.com/youtube/v3/docs/videos/list) method returns this error if the request's `id` parameter specifies a video that cannot be found.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
  | `badRequest (400)` | `invalidRating`                  | The [videos.rate](https://developers.google.com/youtube/v3/docs/videos/rate) method returns this error if the request contains an unexpected value for the `rating` parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

### March 2, 2015

This update contains the following changes:

- The `search.list` method now supports the [relevanceLanguage](https://developers.google.com/youtube/v3/docs/search/list#relevanceLanguage) parameter, which lets you request results that are most relevant to a particular language.

  The [YouTube Data API (v3) migration guide](https://developers.google.com/youtube/v3/migration-guide#search-relevance-language) has also been updated to explain how to use this new parameter. The parameter addresses a feature gap that previously existed between the current API version (v3) and the previous version (v2), which has already been deprecated.
- The [YouTube Data API (v3) migration guide](https://developers.google.com/youtube/v3/migration-guide#deprecated) has also been updated to indicate the deprecation of the [special feeds and metadata fields](https://developers.google.com/youtube/2.0/developers_guide_protocol_movies_and_shows) that the v2 API provided for describing movies, trailers, television shows, television seasons, and television episodes.

### January 14, 2015

This update contains the following changes:

- The [YouTube Data API (v3) migration guide](https://developers.google.com/youtube/v3/migration-guide#videos) has been updated to explain how to use the v3 API to upload videos using JavaScript. (See the **Upload a video** section for details.) This functionality is comparable to the [browser-based uploading](https://developers.google.com/youtube/2.0/developers_guide_protocol_browser_based_uploading) functionality that the v2 API supports. Note that this change to the migration guide does not reflect an actual API change but rather the availability of new sample code for uploading videos with client-side JavaScript.

  Given the support for uploading videos with the JavaScript client library and CORS, the migration guide no longer lists browser-based uploading as a feature that may be deprecated in the v3 API.
- The documentation for the [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert#examples) method has been updated to include the new JavaScript code sample described above. The list of [JavaScript code samples](https://developers.google.com/youtube/v3/code_samples/javascript#upload_video) for the YouTube Data API (v3) has also been updated.

### November 11, 2014

This update contains the following changes:

- The quota cost for a call to the [search.list](https://developers.google.com/youtube/v3/docs/search/list) method has changed to 100 units.

  **Important:** In many cases, you can use other API methods to retrieve information at a lower quota cost. For example, consider these two ways of finding videos uploaded to the **GoogleDevelopers** channel.
  - **Quota cost: 100 units**

    Call the `search.list` method and search for `GoogleDevelopers`.
  - **Quota cost: 6 units**

    Call the `channels.list` method to find the right channel ID. Set the `forUsername` parameter to `GoogleDevelopers` and the `part` parameter to `contentDetails`. In the API response, the `contentDetails.relatedPlaylists.uploads` property specifies the playlist ID for the channel's uploaded videos.

    Then call the `playlistItems.list` method and set the `playlistId` parameter to the captured ID and the `part` parameter to `snippet`.

### October 8, 2014

This update contains the following changes:

- The [channel](https://developers.google.com/youtube/v3/docs/channels) resource contains two new properties:

  - The [status.longUploadsStatus](https://developers.google.com/youtube/v3/docs/channels#status.longUploadsStatus) property indicates whether the channel is eligible to upload videos that are more than 15 minutes long. This property is only returned if the channel owner authorized the API request. Valid property values are:

    <br />

    - `allowed` -- The channel can upload videos more than 15 minutes long.
    - `eligible` -- The channel is eligible to upload videos more than 15 minutes long but must first enable the feature.
    - `disallowed` -- The channel is not able or eligible to upload videos more than 15 minutes long.

    <br />

    See the property definition for more information about these values. The [YouTube Help Center](https://support.google.com/youtube/answer/71673) also provides more detailed information about this feature.
  - The [invideoPromotion.useSmartTiming](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.useSmartTiming) property indicates whether the channel's promotional campaign uses "smart timing." This feature attempts to show promotions at a point in the video when they are more likely to be clicked and less likely to disrupt the viewing experience. This feature also picks up a single promotion to show on each video.

- The definitions of the `video` resource's [snippet.title](https://developers.google.com/youtube/v3/docs/videos#snippet.title) and [snippet.categoryId](https://developers.google.com/youtube/v3/docs/videos#snippet.categoryId) properties have both been updated to clarify the way that API handles calls to the `videos.update` method. If you call that method to update the `snippet` part of a `video` resource, you must set a value for both of those properties.

  If you try to update the `snippet` part of a `video` resource and do not set a value for both of those properties, the API returns an [invalidRequest](https://developers.google.com/youtube/v3/docs/videos/update#errors) error. That error's description has also been updated.
- The `video` resource's [contentDetails.contentRating.oflcRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.oflcRating) property, which identifies a video's rating from New Zealand's Office of Film and Literature Classification, now supports two new ratings: `oflcRp13` and `oflcRp16`. These correspond to the `RP13` and `RP16` ratings, respectively.

- The [channelBanners.insert](https://developers.google.com/youtube/v3/docs/channelBanners/insert#errors) method now supports the following error:

  |  Error type  |   Error detail    |                                                                                               Description                                                                                               |
  |--------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | `badRequest` | `bannerAlbumFull` | The channel owner's YouTube Channel Art album has too many images. The channel owner should go to <http://photos.google.com>, navigate to the albums page, and remove some from images from that album. |

### September 12, 2014

This update contains the following changes:

- The quota cost for a call to the [search.list](https://developers.google.com/youtube/v3/docs/search/list) method has changed from 1 unit to 2 units in addition to the cost of the specified [resource parts](https://developers.google.com/youtube/v3/docs/search/list#part).

### August 13, 2014

This update contains the following changes:

- The [subscriptions.insert](https://developers.google.com/youtube/v3/docs/subscriptions/insert#errors) method now supports the following error:

  |  Error type  |        Error detail         |                                                               Description                                                                |
  |--------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
  | `badRequest` | `subscriptionLimitExceeded` | The subscriber identified with the request has exceeded the subscription rate limit. More subscriptions can be attempted in a few hours. |

### August 12, 2014

This update contains the following changes:

- A new guide, titled [Migrating Your Application to YouTube Data API (v3)](https://developers.google.com/youtube/v3/migration-guide), explains how to use the YouTube Data API (v3) to perform functionality available in the YouTube Data API (v2). The older API was officially deprecated as of March 4, 2014. The guide intends to help you migrate applications still using the v2 API to the most recent API version.

### July 8, 2014

This update contains the following changes:

- The [playlists.insert](https://developers.google.com/youtube/v3/docs/playlists/insert#errors) method now supports the following error:

  |  Error type  |     Error detail      |                                                        Description                                                         |
  |--------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------|
  | `badRequest` | `maxPlaylistExceeded` | This error occurs if a playlist cannot be created because the channel already has the maximum number of playlists allowed. |

### June 18, 2014

This update contains the following changes:

- The description of each API method has been updated to include the quota cost incurred by a call to that method. Similarly, the definitions of `part` parameters have been updated to specify the quota cost of each part that can be retrieved in an API call. For example, a call to the `subscriptions.insert` method has a quota cost of approximately 50 units. The `subscription` resource also contains three parts (`snippet`, `contentDetails`, and `subscriberSnippet`), and each of those has a cost of two units.

  Please remember that quota costs can change without warning.
- The `video` resource now supports 43 new content rating systems, which identify the ratings that videos received from various national rating agencies. The newly supported rating systems are from [Argentina](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.incaaRating), [Austria](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.bmukkRating), [Belgium](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.cicfRating), [Bulgaria](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.nfrcRating), Chile ([television](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.anatelRating)), Chile ([film](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.cccRating)), [Czech Republic](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.czfilmRating), [Colombia](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.mocRating), [Denmark](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.mccypRating), [Egypt](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.egfilmRating), [Estonia](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.eefilmRating), [Finland](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.mekuRating), [France](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.csaRating), [Greece](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.grfilmRating), [Hong Kong](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.fcoRating), [Iceland](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.smaisRating), [Indonesia](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.lsfRating), [Ireland](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.rteRating), [Israel](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.ilfilmRating), [Italy](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.agcomRating), [Kenya](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.kfcbRating), [Latvia](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.nkclvRating), [Luxembourg](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.cscfRating), [Malaysia](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.fcbmRating), [Maldives](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.nbcRating), [Malta](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.mccaaRating), [Netherlands](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.kijkwijzerRating), [Nigeria](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.nfvcbRating), [Norway](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.medietilsynetRating), [Peru](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.pefilmRating), [Philippines](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.mtrbcRating), [Portugal](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.cceRating), [Romania](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.cnaRating), [Singapore](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.mdaRating), [Slovakia](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.skfilmRating), [South Africa](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.fpgRating), [Sweden](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.smsaRating), [Switzerland](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.chfilmRating), [Taiwan](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.moctwRating), [Thailand](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.bfvcRating), and [Venezuela](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.resorteviolenciaRating).

### May 28, 2014

This update contains the following changes:

- The `search.list` method now supports the [location](https://developers.google.com/youtube/v3/docs/search/list#location) and [locationRadius](https://developers.google.com/youtube/v3/docs/search/list#location) parameters, which let you search for videos associated with a geographic location. A request must specify a value for both parameters to retrieve results based on location, and the API will return an error if a request includes only one of the two parameters.

  - The `location` parameter specifies the latitude/longitude coordinates at the center of the circular geographic area.

  - The `locationRadius` parameter specifies the maximum distance that the location associated with a video can be from the center of the area for the video to still be included in search results.

### May 13, 2014

This update contains the following changes:

- The `channel` resource's [invideoPromotion.items[]](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[]) property has been updated to note that you can typically only set one promoted item for your channel. If you try to insert too many promoted items, the API will return a `tooManyPromotedItems` error, which has an HTTP `400` status code.

- The [channelSection](https://developers.google.com/youtube/v3/docs/channelSections) resource now can contain information about a few new types of featured content. The `channelSection` resource's [snippet.type](https://developers.google.com/youtube/v3/docs/channelSections#snippet.type) property now supports the following values:

  <br />

  - `postedPlaylists` - playlists that the channel's owner posted to the channel's activity feed
  - `postedVideos` - videos that the channel's owner posted to the channel's activity feed
  - `subscriptions` - channels that the channel owner has subscribed to

  <br />

- The `video` resource's new [contentDetails.contentRating.ifcoRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.ifcoRating) property identifies the rating that a video received from the Irish Film Classification Office.

- The definition of the `watermark` resource's [position.cornerPosition](https://developers.google.com/youtube/v3/docs/watermarks#position.cornerPosition) property has been updated to note that the watermark always appear in the upper right corner of the player.

- The definition of the [q](https://developers.google.com/youtube/v3/docs/search/list#q) parameter for the `search.list` method has been updated to note that the query term can use the Boolean NOT (`-`) operator to exclude videos associated with a particular search term. The value can also use the Boolean OR (`|`) operator to find videos associated with one of several search terms.

- The definition of the [pageInfo.totalResults](https://developers.google.com/youtube/v3/docs/search/list#pageInfo.totalResults) property that is returned in an API response to a `search.list` call has been updated to note that the value is an approximation and may not represent an exact value. In addition, the maximum value is 1,000,000. You should not use this value to create pagination links. Instead, use the `nextPageToken` and `prevPageToken` property values to determine whether to show pagination links.

- The [watermarks.set](https://developers.google.com/youtube/v3/docs/watermarks/set#response) and [watermarks.unset](https://developers.google.com/youtube/v3/docs/watermarks/unset#response) methods have been updated to reflect that the API returns an HTTP `204` response code for successful requests to those methods.

### May 2, 2014

This update contains the following changes:

- The new [i18nLanguage](https://developers.google.com/youtube/v3/docs/i18nLanguages) resource identifies an application language that the YouTube website supports. The application language can also be referred to as a UI language. For the YouTube website, an application language could be automatically selected based on Google Account settings, browser language, or IP location, and a user could also manually select the desired UI language from the YouTube site footer.

  The API supports a method to [list](https://developers.google.com/youtube/v3/docs/i18nLanguages/list) supported application languages. Supported languages can be used as the value of the `hl` parameter when calling API methods like [videoCategories.list](https://developers.google.com/youtube/v3/docs/videoCategories/list) and [guideCategories.list](https://developers.google.com/youtube/v3/docs/guideCategories/list).
- The new [i18nRegion](https://developers.google.com/youtube/v3/docs/i18nRegions) resource identifies a geographic area that a YouTube user can select as the preferred content region. The content region can also be referred to as a content locale. For the YouTube website, a content region could be automatically selected based on heuristics like the YouTube domain or the user's IP location, and a user could also manually select the desired content region from the YouTube site footer.

  The API supports a method to [list](https://developers.google.com/youtube/v3/docs/i18nLanguages/list) supported content regions. Supported region codes can be used as the value of the `regionCode` parameter when calling API methods like [search.list](https://developers.google.com/youtube/v3/docs/search/list), [videos.list](https://developers.google.com/youtube/v3/docs/videos/list), [activities.list](https://developers.google.com/youtube/v3/docs/activities/list), and [videoCategories.list](https://developers.google.com/youtube/v3/docs/videoCategories/list).

### April 7, 2014

This update contains the following changes:

- The new [channelSection](https://developers.google.com/youtube/v3/docs/channelSections) resource contains information about a set of videos that a channel has chosen to feature. For example, a section could feature a channel's latest uploads, most popular uploads, or videos from one or more playlists.

  The API supports methods to [list](https://developers.google.com/youtube/v3/docs/channelSections/list), [insert](https://developers.google.com/youtube/v3/docs/channelSections/insert), [update](https://developers.google.com/youtube/v3/docs/channelSections/update), or [delete](https://developers.google.com/youtube/v3/docs/channelSections/delete) channel sections. You can retrieve a list of channel sections for the authenticated user's channel, by specifying a particular channel ID, or by specifying a list of unique channel section IDs.

  The [error documentation](https://developers.google.com/youtube/v3/docs/errors#channelSections) has also been updated to describe the error messages that the API supports specifically for these new methods.
- The definition of the `video` resource's [fileDetails](https://developers.google.com/youtube/v3/docs/videos#fileDetails) object has been updated to explain that that object will only be returned if the video's [processingDetails.fileDetailsAvailability](https://developers.google.com/youtube/v3/docs/videos#processingDetails.fileDetailsAvailability) property has a value of `available`.

  Similarly, the definition of the `video` resource's [suggestions](https://developers.google.com/youtube/v3/docs/videos#suggestions) object has been updated to explain that that object will only be returned if the video's [processingDetails.tagSuggestionsAvailability](https://developers.google.com/youtube/v3/docs/videos#processingDetails.tagSuggestionsAvailability) property or its [processingDetails.editorSuggestionsAvailability](https://developers.google.com/youtube/v3/docs/videos#processingDetails.editorSuggestionsAvailability) property has a value of `available`.
- The documentation for the [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) and [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) methods has been updated to reflect that the [status.publishAt](https://developers.google.com/youtube/v3/docs/videos#status.publishAt) property can be set when calling those methods.

- The definition of the `channel` resource's [invideoPromotion](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion) object has been updated to explain that the object can only be retrieved by the channel's owner.

- The parameter list for the [videos.rate](https://developers.google.com/youtube/v3/docs/videos/rate#params) method has been updated to reflect that that method does not actually support the `onBehalfOfContentOwner` parameter. This was a documentation error as `videos.rate` requests that set this parameter return a `500` error.

### March 31, 2014

This update contains the following changes:

- The `video` resource's new [status.publishAt](https://developers.google.com/youtube/v3/docs/videos#status.publishAt) property lets you specify the date and time when a private video is scheduled to be published. This property can only be set if the video's [privacy status](https://developers.google.com/youtube/v3/docs/videos#status.privacyStatus) is `private` and the video has never been published. This new property is [not subject to the deprecation policy](https://developers.google.com/youtube/youtube-api-list).

### March 13, 2014

This update contains the following changes:

- The API now supports the [contentOwnerDetails](https://developers.google.com/youtube/v3/docs/channels#contentOwnerDetails) part for `channel` resources. The new part contains channel data that is relevant for YouTube partners linked with the channel, including the ID of the content owner linked to the channel and the date and time when the content owner and channel were linked. Note that this new part is [not subject to the deprecation policy](https://developers.google.com/youtube/youtube-api-list).

- The documentation now lists the maximum supported character length for the following properties:

  | Resource  |                 Property                 |                                                      Maximum length                                                      |
  |-----------|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
  | `channel` | `invideoPromotion.items[].customMessage` | 40 characters                                                                                                            |
  | `video`   | `snippet.title`                          | 100 characters                                                                                                           |
  | `video`   | `snippet.description`                    | 5000 bytes                                                                                                               |
  | `video`   | `snippet.tags`                           | 500 characters. Note that the property value is a list and that commas between items in the list count toward the limit. |

- The [channel](https://developers.google.com/youtube/v3/docs/channels) resource's `brandingSettings.watch.featuredPlaylistId` property has been deprecated. The API will return an error if you attempt to set its value.

- The following `video` resource properties have been added to the list of values that can be set when [inserting](https://developers.google.com/youtube/v3/docs/videos/insert) or [updating](https://developers.google.com/youtube/v3/docs/videos/update) a video:

  <br />

  - [recordingDetails.locationDescription](https://developers.google.com/youtube/v3/docs/videos#recordingDetails.locationDescription)
  - [recordingDetails.location.latitude](https://developers.google.com/youtube/v3/docs/videos#recordingDetails.location.latitude)
  - [recordingDetails.location.longitude](https://developers.google.com/youtube/v3/docs/videos#recordingDetails.location.longitude)
  - [recordingDetails.recordingDate](https://developers.google.com/youtube/v3/docs/videos#recordingDetails.recordingDate)

  <br />

- The [error documentation](https://developers.google.com/youtube/v3/docs/errors) now specifies the HTTP response code for each error type.

- The API now supports the following errors:

  |     Error type     |         Error detail          |                                                                                                                                                                       Description                                                                                                                                                                       |
  |--------------------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | `badRequest (400)` | `invalidCriteria`             | The [channels.list](https://developers.google.com/youtube/v3/docs/channels/list) method returns this error if the request specifies filter parameters that cannot be used in conjunction with each other.                                                                                                                                               |
  | `badRequest (400)` | `channelTitleUpdateForbidden` | The [channels.update](https://developers.google.com/youtube/v3/docs/channels/update) method returns this error if you attempt to update a channel's `brandingSettings` part and change the value of the `brandingSettings.channel.title` property. (Note that the API does not return the error if you omit the property.)                              |
  | `badRequest (400)` | `invalidRecentlyUploadedBy`   | The [channels.update](https://developers.google.com/youtube/v3/docs/channels/update) method returns this error if the [invideoPromotion.items[].id.recentlyUploadedBy](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].id.recentlyUploadedBy) property specifies an invalid channel ID.                                 |
  | `badRequest (400)` | `invalidTimingOffset`         | The [channels.update](https://developers.google.com/youtube/v3/docs/channels/update) method returns this error if the [invideoPromotion](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion) part specifies an invalid timing offset.                                                                                              |
  | `badRequest (400)` | `tooManyPromotedItems`        | The [channels.update](https://developers.google.com/youtube/v3/docs/channels/update) method returns this error if the [invideoPromotion](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion) part specifies more than the allowed number of promoted items.                                                                        |
  | `forbidden (403)`  | `promotedVideoNotAllowed`     | The [channels.update](https://developers.google.com/youtube/v3/docs/channels/update) method returns this error if the [invideoPromotion.items[].id.videoId](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].id.videoId) property specifies a video ID that either cannot be found or cannot be used as a promoted item. |
  | `forbidden (403)`  | `websiteLinkNotAllowed`       | The [channels.update](https://developers.google.com/youtube/v3/docs/channels/update) method returns this error if the [invideoPromotion.items[].id.websiteUrl](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].id.websiteUrl) property specifies a URL that is not allowed.                                             |
  | `required (400)`   | `requiredTimingType`          | The [channels.update](https://developers.google.com/youtube/v3/docs/channels/update) method returns this error if a request does not specify default timing settings for when YouTube should display a promoted item.                                                                                                                                   |
  | `required (400)`   | `requiredTiming`              | The [channels.update](https://developers.google.com/youtube/v3/docs/channels/update) method must specify an [invideoPromotion.items[].timing](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].timing) object for each promoted item.                                                                                    |
  | `required (400)`   | `requiredWebsiteUrl`          | The [channels.update](https://developers.google.com/youtube/v3/docs/channels/update) method must specify an [invideoPromotion.items[].id.websiteUrl](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].id.websiteUrl) property for each promoted item.                                                                    |
  | `badRequest (400)` | `invalidPublishAt`            | The [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) method returns this error if the request metadata specifies an invalid scheduled publishing time.                                                                                                                                                                      |

### March 4, 2014

This update contains the following changes:

- The YouTube Data API, v3 is now subject to the Deprecation Policy described in the [YouTube APIs Terms of Service](https://developers.google.com/youtube/terms). Note that the page that lists the [APIs that are subject to the deprecation policy](https://developers.google.com/youtube/youtube-api-list) specifically excludes some v3 API functionality from being subject to the policy.

### December 5, 2013

This update contains the following changes:

- The [search.list](https://developers.google.com/youtube/v3/docs/search/list) method's documentation has been updated to properly reflect that you do not need to specify a value for exactly one filter parameter when submitting a search request. Rather, you can set a value for zero filter parameters or for one filter parameter.

- The definitions for the [search.list](https://developers.google.com/youtube/v3/docs/search/list#params) method's parameters have been updated to note that you must set the `type` parameter's value to `video` if you also specify a value for any of the following parameters:

  <br />

  - `eventType`
  - `videoCaption`
  - `videoCategoryId`
  - `videoDefinition`
  - `videoDimension`
  - `videoDuration`
  - `videoEmbeddable`
  - `videoLicense`
  - `videoSyndicated`
  - `videoType`

  <br />

- The minimum size of uploaded channel banner images has been reduced to 2048px by 1152px. (Previously, the minimum size was 2120px by 1192px.) In addition, note that the `channel` resource documentation specifies the maximum sizes of all of the banner images served from the API. For example, the maximum size of the `brandingSettings.image.bannerTvImageUrl` image for television applications is 2120px by 1192px, but the actual image may be 2048px by 1152px. The [YouTube Help Center](https://support.google.com/youtube/answer/2972003) provides additional guidance for optimizing channel art for display on different types of devices.

- Several `channel` resource property definitions have been updated to reflect the following information:

  <br />

  - The `brandingSettings.channel.description` property's value has a maximum length of 1000 characters.
  - The `brandingSettings.channel.featuredChannelsTitle` property has a maximum length of 30 characters.
  - The `brandingSettings.channel.featuredChannelsUrls[]` property can now list up to 100 channels.
  - The `brandingSettings.channel.unsubscribedTrailer` property value, if set, must specify the YouTube video ID of a public or unlisted video that is owned by the channel owner.

  <br />

- The [channels.update](https://developers.google.com/youtube/v3/docs/channels/update) method now supports updates to the `invideoPromotion.items[].promotedByContentOwner` property. That property indicates whether the content owner's name will be shown when displaying the promotion. It can only be set if the API request that sets the property value is being made on the content owner's behalf using the [onBehalfOfContentOwner](https://developers.google.com/youtube/v3/docs/channels/update#onBehalfOfContentOwner) parameter.

- The [playlistItems.list](https://developers.google.com/youtube/v3/docs/playlistItems/list#params) and [playlistItems.insert](https://developers.google.com/youtube/v3/docs/playlistItems/insert#params) methods now support the `onBehalfOfContentOwner` parameter, which is already supported for several other methods.

- The [contentDetails.contentRating.acbRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.acbRating) property can now specify a rating from either the Australian Classification Board (ACB) for movies or from the Australian Communications and Media Authority (ACMA) for children's television programming.

- The new [contentDetails.contentRating.catvRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.catvRating) and [contentDetails.contentRating.catvfrRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.catvfrRating) properties identify the ratings that a video received under the Canadian TV Classification System and the French-language RÃ©gie du cinÃ©ma rating system, which is used in QuÃ©bec, respectively.

- The `videoCategory` resource's new [snippet.assignable](https://developers.google.com/youtube/v3/docs/videoCategories#snippet.assignable) property indicates whether updated videos or newly uploaded videos can be associated with that video category.

- Code samples have been added for the following methods:

  <br />

  - [activities.insert](https://developers.google.com/youtube/v3/docs/activities/insert#examples) (Go)
  - [channelBanners.insert](https://developers.google.com/youtube/v3/docs/channelBanners/insert#examples) (Python)
  - [channels.update](https://developers.google.com/youtube/v3/docs/channels/update#examples) (Python)
  - [playlistItems.list](https://developers.google.com/youtube/v3/docs/playlistItems/list#examples) (Go)
  - [search.list](https://developers.google.com/youtube/v3/docs/search/list#examples) (Go)
  - [thumbnails.set](https://developers.google.com/youtube/v3/docs/thumbnails/set#examples) (Java)
  - [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert#examples) (Go)

  <br />

### October 24, 2013

This update contains the following changes:

- The API includes two additional features designed to help find and feature live broadcast content:

  The new [snippet.liveBroadcastContent](https://developers.google.com/youtube/v3/docs/search#snippet.liveBroadcastContent) property in search results indicates whether a video or channel resource has live broadcast content. Valid property values are `upcoming`, `active`, and `none`.
  - The `video` resource's new [snippet.liveBroadcastContent](https://developers.google.com/youtube/v3/docs/videos#snippet.liveBroadcastContent) property indicates whether the video is an upcoming or active live broadcast. The list below explains the property's possible values:

    - `upcoming` -- The video is a live broadcast that has not yet started.
    - `active` -- The video is an ongoing live broadcast.
    - `none` -- The video is not an upcoming or active live broadcast. This will be the property value for completed broadcasts that are still viewable on YouTube.
  - The `video` resource's new [liveStreamingDetails](https://developers.google.com/youtube/v3/docs/videos#liveStreamingDetails) property is an object that contains metadata about a live video broadcast. To retrieve this metadata, include `liveStreamingDetails` in the `part` parameter value's list of resource parts. The metadata includes the following new properties:

    <br />

    - [liveStreamingDetails.actualStartTime](https://developers.google.com/youtube/v3/docs/videos#liveStreamingDetails.actualStartTime) -- The time that the broadcast actually started. (This value will be present once the broadcast's state is `active`.)
    - [liveStreamingDetails.actualEndTime](https://developers.google.com/youtube/v3/docs/videos#liveStreamingDetails.actualEndTime) -- The time that the broadcast actually ended. (This value will be present once the broadcast is over.)
    - [liveStreamingDetails.scheduledStartTime](https://developers.google.com/youtube/v3/docs/videos#liveStreamingDetails.scheduledStartTime) -- The time that the broadcast is scheduled to begin.
    - [liveStreamingDetails.scheduledEndTime](https://developers.google.com/youtube/v3/docs/videos#liveStreamingDetails.scheduledEndTime) -- The time that the broadcast is scheduled to end. If the property value is empty or the property is not present, then the broadcast is scheduled to go on indefinitely.
    - [liveStreamingDetails.concurrentViewers](https://developers.google.com/youtube/v3/docs/videos#liveStreamingDetails.concurrentViewers) -- The number of people watching the live broadcast.

    <br />

    To retrieve this metadata, include `liveStreamingDetails` in the `part` parameter value when calling the [videos.list](https://developers.google.com/youtube/v3/docs/videos/list#part), [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert#part), or [videos.update](https://developers.google.com/youtube/v3/docs/videos/update#part) method.

  Note that two other features for identifying live broadcast content were released on October 1, 2013 -- the `search.list` method's `eventType` parameter and the search result's `snippet.liveBroadcastContent` property.
- The `videos.insert` method now supports the [notifySubscribers](https://developers.google.com/youtube/v3/docs/videos/insert#notifySubscribers) parameter, which indicates whether YouTube should send a notification about the new video to users who subscribe to the video's channel. The parameter's default value is `True`, which indicates that subscribers will be notified of newly uploaded videos. However, a channel owner who is uploading many videos might prefer to set the value to `False` to avoid sending a notification about each new video to the channel's subscribers.

- The list of properties that can be modified when calling the [channels.update](https://developers.google.com/youtube/v3/docs/channels/update#request_body) method has been updated to include the `invideoPromotion.items[].customMessage` and `invideoPromotion.items[].websiteUrl` properties. In addition, the list has been modified to identify the `brandingSettings` properties that are modifiable. These `brandingSettings` properties were already modifiable, so the documentation change does not reflect a change to the API's existing functionality.

- The [playlists.insert](https://developers.google.com/youtube/v3/docs/playlists/insert#params), [playlists.update](https://developers.google.com/youtube/v3/docs/playlists/update#params), and [playlists.delete](https://developers.google.com/youtube/v3/docs/playlists/delete#params) methods now support the `onBehalfOfContentOwner` parameter, which is already supported for several other methods.

- The [playlists.insert](https://developers.google.com/youtube/v3/docs/playlists/insert#params) method now supports the [onBehalfOfContentOwnerChannel](https://developers.google.com/youtube/v3/docs/playlists/insert#onBehalfOfContentOwnerChannel) parameter, which is already supported for several other methods.

- The `video` resource's [contentDetails.contentRating.tvpgRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.tvpgRating) property now supports a value of `pg14`, which corresponds to a `TV-14` rating.

- The definition of the [snippet.liveBroadcastContent](https://developers.google.com/youtube/v3/docs/search#snippet.liveBroadcastContent) property, which is part of search results, has been corrected to reflect that `live` is a valid property value, but `active` is not a valid property value.

- The `video` resource's [contentDetails.contentRating.mibacRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.mibacRating) property now supports two additional ratings:

  <br />

  - `mibacVap` (VAP) -- Children should be accompanied by an adult.
  - `mibacVm6` (V.M.6) -- Restricted to 6 and over.
  - `mibacVm12` (V.M.12) -- Restricted to 12 and over.

  <br />

- The `channel` resource's new [invideoPromotion.items[].promotedByContentOwner](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].promotedByContentOwner) property indicates whether the content owner's name will be shown when displaying the promotion. This field can only be set if the API request that sets the value is being made on the content owner's behalf. See the [onBehalfOfContentOwner](https://developers.google.com/youtube/v3/docs/channels/update#onBehalfOfContentOwner) parameter for more information.

### October 1, 2013

This update contains the following changes:

- The `channel` resource's new [auditDetails](https://developers.google.com/youtube/v3/docs/channels#auditDetails) object contains channel data that a multichannel network (MCN) would evaluate while determining whether to accept or reject a particular channel. Note that any API request that retrieves this resource part must provide an authorization token that contains the `https://www.googleapis.com/auth/youtubepartner-channel-audit` scope. In addition, any token that uses that scope must be revoked when the MCN decides to accept or reject the channel or within two weeks of the date that the token was issued.

- The `channel` resource's [invideoPromotion.items[].id.type](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].id.type) property now supports a value of `recentUpload`, which indicates that the promoted item is the most recently uploaded video from a specified channel.

  By default, the channel is the same as the one for which the in-video promotion data is set. However, you can promote the most recently uploaded video from another channel by setting the value of the new [invideoPromotion.items[].id.recentlyUploadedBy](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].id.recentlyUploadedBy) property to the channel ID for that channel.
- The `channel` resource contains three new properties -- [brandingSettings.image.bannerTvLowImageUrl](https://developers.google.com/youtube/v3/docs/channels#brandingSettings.image.bannerTvLowImageUrl), [brandingSettings.image.bannerTvMediumImageUrl](https://developers.google.com/youtube/v3/docs/channels#brandingSettings.image.bannerTvMediumImageUrl), [brandingSettings.image.bannerTvHighImageUrl](https://developers.google.com/youtube/v3/docs/channels#brandingSettings.image.bannerTvHighImageUrl) -- that specify the URLs for the banner images that display on channel pages in television applications.

- The new [snippet.liveBroadcastContent](https://developers.google.com/youtube/v3/docs/search#snippet.liveBroadcastContent) property in search results indicates whether a video or channel resource has live broadcast content. Valid property values are `upcoming`, `active`, and `none`.

  <br />

  - For a `video` resource, a value of `upcoming` indicates that the video is a live broadcast that has not yet started, while a value of `active` indicates that the video is an ongoing live broadcast.
  - For a `channel` resource, a value of `upcoming` indicates that the channel has a scheduled broadcast that has not yet started, while a value of `acive` indicates that the channel has an ongoing live broadcast.

  <br />

- In the `watermark` resource, the [targetChannelId](https://developers.google.com/youtube/v3/docs/watermarks#targetChannelId) property has changed from an object to a string. Instead of containing a child property that specifies the YouTube channel ID of the channel that the watermark image links to, the `targetChannelId` property now specifies that value itself. Accordingly, the resource's `targetChannelId.value` property has been removed.

- The `thumbnails.set` method now supports the [onBehalfOfContentOwner](https://developers.google.com/youtube/v3/docs/thumbnails/set#onBehalfOfContentOwner) parameter, which is already supported for several other methods.

- The `search.list` method now supports the [eventType](https://developers.google.com/youtube/v3/docs/search/list#eventType) parameter, which restricts a search to only return either active, upcoming, or completed broadcast events.

- The new [contentDetails.contentRating.mibacRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.mibacRating) property identifies the rating that a video received from Italy's Ministero dei Beni e delle Attivita Culturali e del Turismo.

- The API now supports the following errors:

  |  Error type  |     Error detail      |                                                                                        Description                                                                                        |
  |--------------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | `badRequest` | `invalidImage`        | The [thumbnails.set](https://developers.google.com/youtube/v3/docs/thumbnails/set) method returns this error if the provided image content is invalid.                                    |
  | `forbidden`  | `videoRatingDisabled` | The [videos.rate](https://developers.google.com/youtube/v3/docs/videos/rate) method returns this error if the owner of the video that is being rated has disabled ratings for that video. |

### August 27, 2013

This update contains the following changes:

- The new [watermark](https://developers.google.com/youtube/v3/docs/watermarks) resource identifies an image that displays during playbacks of a specified channel's videos. You can also specify a target channel to which the image will link as well as timing details that determine when the watermark appears during video playbacks and the length of time it is visible.

  The [watermarks.set](https://developers.google.com/youtube/v3/docs/watermarks/set) method uploads and sets a channel's watermark image. The [watermarks.unset](https://developers.google.com/youtube/v3/docs/watermarks/unset) method deletes a channel's watermark image.

  The error documentation describes the error messages that the API supports specifically for the [watermarks.set](https://developers.google.com/youtube/v3/docs/errors#watermarks_youtube.watermarks.set) and [watermarks.unset](https://developers.google.com/youtube/v3/docs/errors#watermarks_youtube.watermarks.unset) methods.
- The `channel` resource's new [statistics.hiddenSubscriberCount](https://developers.google.com/youtube/v3/docs/channels#statistics.hiddenSubscriberCount) property contains a boolean value that indicates whether the channel's number of subscribers is hidden. As such, the property's value is `false` if the channel's subscriber count is publicly visible.

- The `playlists.list` method now supports the [onBehalfOfContentOwner](https://developers.google.com/youtube/v3/docs/playlists/list#onBehalfOfContentOwner) and [onBehalfOfContentOwnerChannel](https://developers.google.com/youtube/v3/docs/playlists/list#onBehalfOfContentOwnerChannel) parameters. Both parameters are already supported for several other methods.

- The `videos.list` method now supports the [regionCode](https://developers.google.com/youtube/v3/docs/videos/list#regionCode) parameter, which identifies the content region for which a chart should be retrieved. This parameter can only be used in conjunction with the [chart](https://developers.google.com/youtube/v3/docs/videos/list#chart) parameter. The parameter value is an ISO 3166-1 alpha-2 country code.

- The [error documentation](https://developers.google.com/youtube/v3/docs/errors) describes the following new common request error, which could occur for multiple API methods:

  | Error type  |       Error detail        |                                                        Description                                                         |
  |-------------|---------------------------|----------------------------------------------------------------------------------------------------------------------------|
  | `forbidden` | `insufficientPermissions` | The scopes associated with the OAuth 2.0 token provided for the request are insufficient for accessing the requested data. |

### August 15, 2013

This update contains the following changes:

- The `channel` resource's `invideoPromotion` object has the following new and updated properties:

  - The API now supports the ability to specify a website as a promoted item. To do so, set the [invideoPromotion.items[].id.type](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].id.type) property value to `website` and use the new [invideoPromotion.items[].id.websiteUrl](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].id.websiteUrl) property to specify the URL. Also use the new [invideoPromotion.items[].customMessage](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].customMessage) property to define a custom message to display for the promotion.

    Links can be to associated websites, merchant sites, or social networking sites. See the YouTube Help Center instructions for [associated websites](https://support.google.com/youtube/answer/2887282) and [merchant sites](https://support.google.com/youtube/answer/2760471) for more information about enabling links for your content.

    By adding promotional links, you agree that those links will not be used to redirect traffic to unauthorized sites and that those links will comply with YouTube's [AdWords policies](https://support.google.com/adwordspolicy/bin/answer.py?answer=54818), [YouTube ad policies](https://support.google.com/youtube/answer/188570?topic=30084), [YouTube Community Guidelines](http://www.youtube.com/t/community_guidelines) and [YouTube Terms of Service](http://www.youtube.com/t/terms).
  - The properties related to the timing settings for displaying promoted items during video playback have been restructured:

    - The `invideoPromotion.timing` object has been moved to [invideoPromotion.items[].timing](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].timing). This object now enables you to customize the timing data for each promoted item in the `invideoPromotion.items[]` list.

    - The new [invideoPromotion.defaultTiming](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.defaultTiming) object specifies default timing settings for your promotion. Those settings define when a promoted item will display during playback of one of your channel's videos. You can override the default timing for any given promoted item using the [invideoPromotion.items[].timing](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].timing) object.

    - The new [invideoPromotion.items[].timing.durationMs](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.items[].timing.durationMs) property specifies the amount of time, in milliseconds, that the promotion should display. The `invideoPromotion.defaultTiming` object also contains a [durationMs](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion.defaultTiming.durationMs) field that specifies the default amount of time that the promoted item will display.

  - The `invideoPromotion.items[].type` and `invideoPromotion.items[].videoId` properties both have been moved into the `invideoPromotion.items[].id` object.

- The `subscriptions.list` method now supports the [onBehalfOfContentOwner](https://developers.google.com/youtube/v3/docs/subscriptions/list#onBehalfOfContentOwner) and [onBehalfOfContentOwnerChannel](https://developers.google.com/youtube/v3/docs/subscriptions/list#onBehalfOfContentOwnerChannel) parameters. Both parameters are already supported for several other methods.

- In the API response to a `thumbnails.set` request, the [kind](https://developers.google.com/youtube/v3/docs/thumbnails/set#kind) property value has changed from `youtube#thumbnailListResponse` to `youtube#thumbnailSetResponse`.

- Code samples have been added for the following methods:

  <br />

  - [channels.update](https://developers.google.com/youtube/v3/docs/channels/update#examples) (Java, Python)
  - [playlists.insert](https://developers.google.com/youtube/v3/docs/playlists/insert#examples) (.NET, PHP)
  - [subscriptions.insert](https://developers.google.com/youtube/v3/docs/subscriptions/insert#examples) (PHP, Python)
  - [thumbnails.set](https://developers.google.com/youtube/v3/docs/thumbnails/set#examples) (PHP, Python)
  - [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert#examples) (PHP)
  - [videos.list](https://developers.google.com/youtube/v3/docs/videos/list#examples) (PHP)
  - [videos.rate](https://developers.google.com/youtube/v3/docs/videos/rate#examples) (Python)
  - [videos.update](https://developers.google.com/youtube/v3/docs/videos/update#examples) (Java, PHP, Python)

  <br />

  Note that the Python example for the [playlistItems.insert](https://developers.google.com/youtube/v3/docs/playlistItems/insert) method was also removed since the functionality it demonstrated is now handled by the [videos.rate](https://developers.google.com/youtube/v3/docs/videos/rate#examples) method.
- The [error documentation](https://developers.google.com/youtube/v3/docs/errors) describes the following new request context error, which could occur for any API method that supports the `mine` request parameter:

  |  Error type  | Error detail  |                                                                                                                                                                                 Description                                                                                                                                                                                 |
  |--------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | `badRequest` | `invalidMine` | The `mine` parameter cannot be used in requests where the authenticated user is a YouTube partner. You should either remove the `mine` parameter, authenticate as a YouTube user by removing the `onBehalfOfContentOwner` parameter, or act as one of the partner's channels by providing the `onBehalfOfContentOwnerChannel` parameter if available for the called method. |

### August 8, 2013

This update contains the following changes:

- The [Getting Started with the YouTube Data API](https://developers.google.com/youtube/v3/getting-started) guide's [Quota Usage](https://developers.google.com/youtube/v3/getting-started#quota) section has been updated to reflect a change in the quota cost of a video upload from approximately 16000 units to approximately 1600 units.

### July 30, 2013

This update contains the following changes:

- In a `channelBanner` resource, the value of the `kind` property's value has changed from `youtube#channelBannerInsertResponse` to `youtube#channelBannerResource`. This resource is returned in response to a [channelBanners.insert](https://developers.google.com/youtube/v3/docs/channelBanners/insert) request.

- The `channel` resource's new [brandingSettings.channel.profileColor](https://developers.google.com/youtube/v3/docs/channels#brandingSettings.channel.profileColor) property specifies a prominent color that complements the channel's content. The property value is a pound sign (`#`) followed by a six-character hexadecimal string, such as `#2793e6`.

- The API now supports the ability to specify whether a subscription is for all of a channel's activities or just for new uploads. The `subscription` resource's new [contentDetails.activityType](https://developers.google.com/youtube/v3/docs/subscriptions#contentDetails.activityType) property identifies the types of activities that the subscriber will be notified about. Valid property values are `all` and `uploads`.

- The [videos.list](https://developers.google.com/youtube/v3/docs/videos/list) method supports new parameters for retrieving a chart of the most popular videos on YouTube:

  <br />

  - The [chart](https://developers.google.com/youtube/v3/docs/videos/list#chart) parameter identifies the chart that you want to retrieve. Currently, the only supported value is `mostPopular`. Note that the `chart` parameter is a filter parameter, which means it cannot be used in the same request as other filter parameters (`id` and `myRating`).
  - The [videoCategoryId](https://developers.google.com/youtube/v3/docs/videos/list#videoCategoryId) parameter identifies the [video category](https://developers.google.com/youtube/v3/docs/videoCategories) for which the chart should be retrieved. This parameter can only be used in conjunction with the `chart` parameter. By default, charts are not restricted to a particular category.

  <br />

- The `video` resource's new [topicDetails.relevantTopicIds[]](https://developers.google.com/youtube/v3/docs/videos#topicDetails.relevantTopicIds[]) property provides a list of Freebase topic IDs that are relevant to the video or its content. The subjects of these topics may be mentioned in or appear in the video.

- The `video` resource's `recordingDetails.location.elevation` property has been renamed to `recordingDetails.location.altitude`, and its `fileDetails.recordingLocation.location.elevation` property has been renamed to `fileDetails.recordingLocation.location.altitude`.

- The `video` resource's [contentDetails.contentRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating) object specifies the ratings that a video received under various rating schemes, including MPAA ratings, TVPG ratings, and so forth. For each rating system, the API now supports a rating value that indicates that the video has not been rated. Note that for [MPAA ratings](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.mpaaRating), an "unrated" rating is frequently used to identify uncut versions of films for which the cut version of the film did receive an official rating.

- The `video` resource's new [contentDetails.contentRating.ytRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.ytRating) property identifies age-restricted content. The property value will be `ytAgeRestricted` if YouTube has identified the video as containing content that is inappropriate for users less than 18 years old. If the property is absent or if the property value is empty, then the content has not been identified as age-restricted.

- The [channels.list](https://developers.google.com/youtube/v3/docs/channels/list) method's `mySubscribers` parameter has been deprecated. Use the [subscriptions.list](https://developers.google.com/youtube/v3/docs/subscriptions/list) method and its `mySubscribers` parameter to retrieve a list of subscribers to the authenticated user's channel.

- The [channelBanners.insert](https://developers.google.com/youtube/v3/docs/channelBanners/insert), [channels.update](https://developers.google.com/youtube/v3/docs/channels/update), [videos.getRating](https://developers.google.com/youtube/v3/docs/videos/getRating), and [videos.rate](https://developers.google.com/youtube/v3/docs/videos/rate) methods all now support the `onBehalfOfContentOwner` parameter. That parameter indicates that the authenticated user is acting on behalf of the content owner specified in the parameter value.

- The [channels.update](https://developers.google.com/youtube/v3/docs/channels/update) method's documentation has been updated to reflect the fact that that method can be used to update the `channel` resource's `brandingSettings` object and its child properties. The documentation also now lists the updated list of properties that you can set for the `channel` resource's `invideoPromotion` object.

- The [error documentation](https://developers.google.com/youtube/v3/docs/errors) describes the following new errors:

  |  Error type  |            Error detail             |                                                                                                                                              Description                                                                                                                                              |
  |--------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | `forbidden`  | `accountDelegationForbidden`        | This error is not specific to a particular API method. It indicates that the authenticated user is not authorized to act on behalf of the specified Google account.                                                                                                                                   |
  | `forbidden`  | `authenticatedUserAccountClosed`    | This error is not specific to a particular API method. It indicates that the authenticated user's YouTube account is closed. If the user is acting on behalf of another Google Account, then this error would indicate that that other account is closed.                                             |
  | `forbidden`  | `authenticatedUserAccountSuspended` | This error is not specific to a particular API method. It indicates that the authenticated user's YouTube account is suspended. If the user is acting on behalf of another Google Account, then this error would indicate that that other account is suspended.                                       |
  | `forbidden`  | `authenticatedUserNotChannel`       | This error is not specific to a particular API method. It indicates that the API server cannot identify the channel associated with the API request. If the request is authorized and uses the `onBehalfOfContentOwner` parameter, you should also set the `onBehalfOfContentOwnerChannel` parameter. |
  | `forbidden`  | `cmsUserAccountNotFound`            | This error is not specific to a particular API method. The CMS user is not allowed to act on behalf of the specified content owner.                                                                                                                                                                   |
  | `notFound`   | `contentOwnerAccountNotFound`       | This error is not specific to a particular API method. The specified content owner account was not found.                                                                                                                                                                                             |
  | `badRequest` | `invalidPart`                       | This error is not specific to a particular API method. The request's `part` parameter specifies parts that cannot be written at the same time.                                                                                                                                                        |
  | `badRequest` | `videoChartNotFound`                | The [videos.list](https://developers.google.com/youtube/v3/docs/videos/list) method returns this error when the request specifies an unsupported or unavailable video chart.                                                                                                                          |
  | `notFound`   | `videoNotFound`                     | The [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) method returns this error to indicate that the video you are trying to update cannot be found. Check the value of the `id` property in the request body to ensure it is correct.                                     |

### June 10, 2013

This update contains the following changes:

- The `channels.list` method's new [forUsername](https://developers.google.com/youtube/v3/docs/channels/list#forUsername) parameter enables you to retrieve information about a channel by specifying its YouTube username.

- The `activities.list` method now supports the [regionCode](https://developers.google.com/youtube/v3/docs/activities/list#regionCode) parameter, which instructs the API to return results relevant to the specified country. YouTube uses this value when the authorized user's previous activity on YouTube does not provide enough information to generate the activity feed.

- Playlist resources now contain the [snippet.tags](https://developers.google.com/youtube/v3/docs/playlists#snippet.tags[]) property. The property will be only be returned to authorized users who are retrieving data about their own playlists. Authorized users can also set playlist tags when calling either the [playlists.insert](https://developers.google.com/youtube/v3/docs/playlists/insert) or [playlists.update](https://developers.google.com/youtube/v3/docs/playlists/update) methods.

- The `onBehalfOfContentOwner` parameter, which was previously supported for the [channels.list](https://developers.google.com/youtube/v3/docs/channels/list) and [search.list](https://developers.google.com/youtube/v3/docs/search/list) methods, is now also supported for the [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert#onBehalfOfContentOwner), [videos.update](https://developers.google.com/youtube/v3/docs/videos/update#onBehalfOfContentOwner), and [videos.delete](https://developers.google.com/youtube/v3/docs/videos/delete#onBehalfOfContentOwner) methods. Note that when this parameter is used in a call to the [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) method, the request must also specify a value for the new [onBehalfOfContentOwnerChannel](https://developers.google.com/youtube/v3/docs/videos/insert#onBehalfOfContentOwnerChannel) parameter, which identifies the channel to which the video will be added. The channel must be linked to the content owner that the `onBehalfOfContentOwner` parameter specifies.

  The parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

  This parameter is intended for content partners that own and manage many different YouTube channels. The parameter enables those partners to authenticate once and get access to all of their video and channel data, without having to provide authentication credentials for each individual channel.

  Specifically in regard to this release, the parameter now enables a content partner to insert, update, or delete videos in any of the YouTube channels that the partner owns.
- The [error documentation](https://developers.google.com/youtube/v3/docs/errors) describes the following new errors:

  |   Error type   |        Error detail        |                                                                                                                                                 Description                                                                                                                                                 |
  |----------------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | `forbidden`    | `insufficientCapabilities` | This error is not specific to a particular API method. It indicates that the CMS user calling the API does not have sufficient permissions to perform the requested operation. This error is associated with the use of the `onBehalfOfContentOwner` parameter, which is supported for several API methods. |
  | `unauthorized` | `authorizationRequired`    | The [activities.list](https://developers.google.com/youtube/v3/docs/activities/list) method returns this error when the request uses the [home](https://developers.google.com/youtube/v3/docs/activities/list#home) parameter but is not properly authorized.                                               |

- In the [channels](https://developers.google.com/youtube/v3/docs/channels) resource, the `invideoPromotion.channelId` property has been removed because the channel ID is already specified using the resource's [id](https://developers.google.com/youtube/v3/docs/channels#id) property.

- The new [Working with Channel IDs](https://developers.google.com/youtube/v3/guides/working_with_channel_ids) guide explains how the API uses channel IDs. The guide may be especially useful for developers migrating from the previous version of the API and who have applications that either request content for the `default` user or that rely on the notion that every YouTube channel has a unique username, which is no longer the case.

### May 22, 2013

This update contains the following changes:

- The new [channelBanners.insert](https://developers.google.com/youtube/v3/docs/channelBanners/insert) method enables you to upload a banner image that can subsequently be set as the banner image for a channel using the `channel` resource's new [brandingSettings.image.bannerExternalUrl](https://developers.google.com/youtube/v3/docs/channels#brandingSettings.image.bannerExternalUrl) property.

- The documentation for the [channels.update](https://developers.google.com/youtube/v3/docs/channels/update#request_body) method has been updated to list the properties that can be modified when calling the method.

- The [video](https://developers.google.com/youtube/v3/docs/videos) resource documentation no longer lists `unspecified` as a valid property value for the [suggestions.processingErrors[]](https://developers.google.com/youtube/v3/docs/videos#suggestions.processingErrors[]), [suggestions.processingHints[]](https://developers.google.com/youtube/v3/docs/videos#suggestions.processingHints[]), [suggestions.processingWarnings[]](https://developers.google.com/youtube/v3/docs/videos#suggestions.processingWarnings[]), and [suggestions.editorSuggestions[]](https://developers.google.com/youtube/v3/docs/videos#suggestions.editorSuggestions[]) properties.

- The [videos.list](https://developers.google.com/youtube/v3/docs/videos/list) method's `maxResults` parameter now has a default value of `5`.

- The [error documentation](https://developers.google.com/youtube/v3/docs/errors) now lists errors for the `channelBanners.insert` and `subscriptions.list` methods. It also lists several new errors for the `channels.update` method.

### May 14, 2013

This update contains the following changes:

- Standalone pages now list code samples for [Java](https://developers.google.com/youtube/v3/code_samples/java), [.NET](https://developers.google.com/youtube/v3/code_samples/dotnet), [PHP](https://developers.google.com/youtube/v3/code_samples/php), and [Ruby](https://developers.google.com/youtube/v3/code_samples/ruby).

- The page that lists [Python](https://developers.google.com/youtube/v3/code_samples/python) code samples now includes examples for adding a subscription, creating a playlist, and updating a video.

### May 10, 2013

This update contains the following changes:

- YouTube no longer identifies experimental API features and services. Instead, we now provide a list of [YouTube APIs that are subject to the deprecation policy](https://developers.google.com/youtube/youtube-api-list).

### May 8, 2013

This update contains the following changes:

- Channel resources now support the [inVideoPromotion](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion) object, which encapsulates information about a promotional campaign associated with the channel. A channel can use an in-video promotional campaign to display thumbnail images for a promoted video within the video player during playbacks of the channel's videos.

  You can retrieve this data by including `invideoPromotion` in the [part](https://developers.google.com/youtube/v3/docs/channels/list#part) parameter value in a `channels.list` request.
- The new [channels.update](https://developers.google.com/youtube/v3/docs/channels/update) method can be used to update a channel's in-video promotional campaign data. Note that the method only supports updates to the [invideoPromotion](https://developers.google.com/youtube/v3/docs/channels#invideoPromotion) part of the `channel` resource and does not yet support updates to other parts of that resource.

### May 2, 2013

This update contains the following changes:

- Channel resources now support the [status.isLinked](https://developers.google.com/youtube/v3/docs/channels#status.isLinked) property, which indicates whether the channel data identifies a user that is already linked to either a YouTube username or a Google+ account. A user that has one of these links already has a public YouTube identity, which is a prerequisite for several actions, such as uploading videos.

- Subscription resources now support the [subscriberSnippet](https://developers.google.com/youtube/v3/docs/subscriptions#subscriberSnippet) part. That object encapsulates contains snippet data for the subscriber's channel.

- The API now supports the [videos.getRating](https://developers.google.com/youtube/v3/docs/videos/getRating) method, which retrieves the ratings that the authenticated user gave to a list of one or more videos.

- The `videos.list` method's new [myRating](https://developers.google.com/youtube/v3/docs/videos/list#myRating) parameter enables you to retrieve a list of videos that the authenticated user rated with a `like` or `dislike` rating.

  The `myRating` parameter and the [id](https://developers.google.com/youtube/v3/docs/videos/list#id) parameter are both now considered filter parameters, which means that an API request must specify exactly one of the parameters. (Previously, the `id` parameter was a required parameter for this method.)

  The method returns a [forbidden](https://developers.google.com/youtube/v3/docs/videos/list#errors") error for requests that attempt to retrieve video rating information but are not properly authorized to do so.
- With the introduction of the `myRating` parameter, the [videos.list](https://developers.google.com/youtube/v3/docs/videos/list) method has also been updated to support pagination. Note, however, that paging parameters are only supported for requests using the `myRating` parameter. (Paging parameters and information are not supported for requests that use the `id` parameter.)

  - The [maxResults](https://developers.google.com/youtube/v3/docs/videos/list#maxResults) parameter specifies the maximum number of videos that the API can return in the result set, and the [pageToken](https://developers.google.com/youtube/v3/docs/videos/list#pageToken) parameter identifies a specific page in the result set that you want to retrieve.

  - The `youtube#videoListResponse` resource, which is returned in response to a `videos.list` request, now contains the [pageInfo](https://developers.google.com/youtube/v3/docs/videos/list#pageInfo) object, which contains details like the total number of results and the number of results included in the current result set. The `youtube#videoListResponse` resource can also include `nextPageToken` and `prevPageToken` properties, each of which provides a token that could be used to retrieve a specific page in the result set.

- The [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert#params) method supports the following new parameters:

  <br />

  - [autoLevels](https://developers.google.com/youtube/v3/docs/videos/insert#autoLevels) -- Set this parameter value to `true` to instruct YouTube to automatically enhance the video's lighting and color.
  - [stabilize](https://developers.google.com/youtube/v3/docs/videos/insert#stabilize) -- Set this parameter value to `true` to instruct YouTube to adjust the video by removing shakiness resulting from camera motions.

  <br />

- The `channelTitle` property has been added to the `snippet` for the following resources:

  <br />

  - [playlistItem](https://developers.google.com/youtube/v3/docs/playlistItems#channelTitle) -- The property specifies the name of the channel that added the playlist item.
  - [playlist](https://developers.google.com/youtube/v3/docs/playlists#channelTitle) -- The property specifies the name of the channel that created the playlist.
  - [subscription](https://developers.google.com/youtube/v3/docs/subscriptions#channelTitle) -- The property specifies the name of the channel that is subscribed to.

  <br />

- Code samples have been added for the following methods:

  <br />

  - [activities.insert](https://developers.google.com/youtube/v3/docs/activities/insert#examples) (Ruby)
  - [playlistItems.list](https://developers.google.com/youtube/v3/docs/playlistItems/list#examples) (.NET)
  - [search.list](https://developers.google.com/youtube/v3/docs/search/list#examples) (.NET)
  - [subscriptions.insert](https://developers.google.com/youtube/v3/docs/subscriptions/insert#examples) (Java, Ruby)
  - [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert#examples) (.NET, Ruby)

  <br />

- The `subscriptions.list` method's new [mySubscribers](https://developers.google.com/youtube/v3/docs/subscriptions/list#mySubscribers) parameter enables you to retrieve a list of the currently authenticated user's subscribers. This parameter can only be used in a properly authorized request.

  **Note:** This functionality is intended to replace the [mySubscribers](https://developers.google.com/youtube/v3/docs/channels/list#mySubscribers) parameter currently supported for the `channels.list` method. That parameter will be deprecated.
- In a `video` resource, the property value `unspecified` is no longer a possible value for any of the following properties:

  <br />

  - [fileDetails.fileType](https://developers.google.com/youtube/v3/docs/videos#fileDetails.fileType)
  - [fileDetails.videoStreams[].rotation](https://developers.google.com/youtube/v3/docs/videos#fileDetails.videoStreams[].rotation)
  - [processingDetails.processingStatus](https://developers.google.com/youtube/v3/docs/videos#processingDetails.processingStatus)
  - [processingDetails.processingFailureReason](https://developers.google.com/youtube/v3/docs/videos#processingDetails.processingFailureReason)
  - [fileDetails.fileType](https://developers.google.com/youtube/v3/docs/videos#fileDetails.fileType)

  <br />

- API requests that contain an unexpected parameter now return a `badRequest` error, and the reported reason for the error is `unexpectedParameter`.

- The error that the [playlistItems.insert](https://developers.google.com/youtube/v3/docs/playlistItems/insert#errors) method returns when the playlist already contains the maximum number of allowed items has been updated. The error is now reported as a `forbidden` error, and the error reason is `playlistContainsMaximumNumberOfVideos`.

### April 19, 2013

This update contains the following changes:

- The new [videos.rate](https://developers.google.com/youtube/v3/docs/videos/rate) method lets a user set a `like` or `dislike` rating on a video or remove a rating from a video.

  The [error documentation](https://developers.google.com/youtube/v3/docs/errors#videos_youtube.videos.rate) has also been updated to list the errors that the API might return in response to a [videos.rate](https://developers.google.com/youtube/v3/docs/videos/rate) method call.
- Thumbnail images are now identified in the API documentation as a [separate resource](https://developers.google.com/youtube/v3/docs/thumbnails), and the new [thumbnails.set](https://developers.google.com/youtube/v3/docs/thumbnails/set) method enables you to upload a custom video thumbnail to YouTube and set it for a video.

  The [error documentation](https://developers.google.com/youtube/v3/docs/errors) has also been updated to list the errors that the API might return in response to a [thumbnails.set](https://developers.google.com/youtube/v3/docs/thumbnails/set) method call.

  Note that this change does not really affect existing resources that return thumbnail images. Thumbnail images are returned in those resources in the same way that they were previously, though the documentation does now list the names of the different thumbnail sizes that the API might return.
- The `channel` resource's new [brandingSettings](https://developers.google.com/youtube/v3/docs/channels#brandingSettings) part identifies settings, text, and images for the channel's channel page and video watch pages.

- The `playlistItem` resource contains the following new properties:

  - The new [status](https://developers.google.com/youtube/v3/docs/playlistItems#status) object encapsulates status information about the playlist item, and the [status.privacyStatus](https://developers.google.com/youtube/v3/docs/playlistItems#status.privacyStatus) property identifies the playlist item's privacy status.

- The `video` resource contains the following new properties:

  - The [status.publicStatsViewable](https://developers.google.com/youtube/v3/docs/videos#status.publicStatsViewable) property indicates whether extended video statistics on the watch page are publicly viewable. By default, those statistics are viewable, and statistics like a video's viewcount and ratings will still be publicly visible even if this property's value is set to `false`. You can set this property's value when calling the [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) or [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) method.

  - The [contentDetails.contentRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating) object encapsulates ratings that the video received under various rating schemes. The list below identifies the supported rating systems and provides a link to the property associated with each rating system. The property definitions identify the supported rating values for each system.

    |     Country     |                                Rating system                                |                                                                  Property                                                                   |
    |-----------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
    | `United States` | Motion Picture Association of America (MPAA)                                | [contentDetails.contentRating.mpaaRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.mpaaRating)     |
    | `United States` | TV Parental Guidelines                                                      | [contentDetails.contentRating.tvpgRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.tvpgRating)     |
    | `Australia`     | Australian Classification Board (ACB)                                       | [contentDetails.contentRating.acbRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.acbRating)       |
    | `Brazil`        | Departamento de JustiÃ§a, ClassificaÃ§Ã£o, QualificaÃ§Ã£o e TÃ­tulos              | [contentDetails.contentRating.djctqRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.djctqRating)   |
    | `Canada`        | Canadian Home Video Rating System (CHVRS)                                   | [contentDetails.contentRating.chvrsRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.chvrsRating)   |
    | `France`        | Centre national du cinÃ©ma et de l'image animÃ©e (French Ministry of Culture) | [contentDetails.contentRating.fmocRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.fmocRating)     |
    | `Germany`       | Freiwillige Selbstkontrolle der Filmwirtschaft (FSK)                        | [contentDetails.contentRating.fskRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.fskRating)       |
    | `Great Britain` | British Board of Film Classification (BBFC)                                 | [contentDetails.contentRating.bbfcRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.bbfcRating)     |
    | `India`         | Central Board of Film Certification (CBFC)                                  | [contentDetails.contentRating.cbfcRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.cbfcRating)     |
    | `Japan`         | æ å«ç®¡çå§å¡ä¼ (EIRIN)                                                             | [contentDetails.contentRating.eirinRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.eirinRating)   |
    | `Korea`         | ììë¬¼ë±ê¸ììí (KMRB)                                                             | [contentDetails.contentRating.kmrbRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.kmrbRating)     |
    | `Mexico`        | General Directorate of Radio, Television and Cinematography (RTC)           | [contentDetails.contentRating.rtcRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.rtcRating)       |
    | `New Zealand`   | Office of Film and Literature Classification                                | [contentDetails.contentRating.oflcRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.oflcRating)     |
    | `Russia`        | National Film Registry of the Russian Federation                            | [contentDetails.contentRating.russiaRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.russiaRating) |
    | `Spain`         | `Instituto de la CinematografÃ­a y de las Artes Audiovisuales (ICAA)`        | [contentDetails.contentRating.icaaRating](https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating.icaaRating)     |

- The [playlistItems.update](https://developers.google.com/youtube/v3/docs/playlistItems/update) method's documentation has been updated to reflect the fact that the `snippet.resourceId` property must be specified in the resource sent as the request body.

- The [search.list](https://developers.google.com/youtube/v3/docs/search/list) method now supports the following functionality:

  - The new [forMine](https://developers.google.com/youtube/v3/docs/search/list#forMine) parameter restricts a search to only retrieve the authenticated user's videos.

  - The [order](https://developers.google.com/youtube/v3/docs/search/list#order) parameter now supports the ability to sort results alphabetically by title (`order=title`) or by video count in descending order (`order=videoCount`).

  - The new [safeSearch](https://developers.google.com/youtube/v3/docs/search/list#safeSearch) parameter indicates whether search results should include restricted content.

- The [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) method supports several new errors, which are listed in the table below:

  |  Error type  |       Error detail        |                                                                                                   Description                                                                                                   |
  |--------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | `badRequest` | `invalidCategoryId`       | The `snippet.categoryId` property specifies an invalid category ID. Use the [videoCategories.list](https://developers.google.com/youtube/v3/docs/videoCategories/list) method to retrieve supported categories. |
  | `badRequest` | `invalidRecordingDetails` | The `metadata` specifies invalid recording details.                                                                                                                                                             |
  | `badRequest` | `invalidVideoGameRating`  | The request metadata specifies an invalid video game rating.                                                                                                                                                    |
  | `badRequest` | `invalidVideoMetadata`    | The request metadata is invalid.                                                                                                                                                                                |

- The `onBehalfOfContentOwner` parameter has been removed from the list of supported parameters for the `videos.update` and `videos.delete` methods.

### March 12, 2013

This update contains the following changes:

- The `channelTitle` property has been added to the `snippet` for the following resources:

  <br />

  - [activity](https://developers.google.com/youtube/v3/docs/activities#snippet.channelTitle) -- The property specifies the name of the channel responsible for the activity.
  - [search](https://developers.google.com/youtube/v3/docs/search#snippet.channelTitle) -- The property specifies the name of the channel associated with the resource that the search result identifies.
  - [video](https://developers.google.com/youtube/v3/docs/videos#snippet.channelTitle) -- The property specifies the name of the channel that uploaded the video.

  <br />

- The `search.list` method supports the following new parameters:

  - The [channelType](https://developers.google.com/youtube/v3/docs/search/list#channelType) parameter lets you restrict a search for channels to retrieve all channels or to retrieve only shows.

  - The [videoType](https://developers.google.com/youtube/v3/docs/search/list#videoType) parameter lets you restrict a search for videos to retrieve all videos or to retrieve only movies or only episodes of shows.

- The definition of the `video` resource's [recordingDetails](https://developers.google.com/youtube/v3/docs/videos#recordingDetails) part has been updated to note that the object will only be returned for a video if the video's geolocation data or recording time has been set.

- The `playlistItems.update` method now returns an [invalidSnippet](https://developers.google.com/youtube/v3/docs/errors#youtube.playlistItems.update-invalidValue-invalidSnippet) error, which is returned if the API request does not specify a valid snippet.

- Several API methods support new parameters that are intended exclusively for YouTube content partners. YouTube content partners include movie and television studios, record labels, and other content creators that make their content available on YouTube.

  - The [onBehalfOfContentOwner](https://developers.google.com/youtube/v3/docs/channels/list#onBehalfOfContentOwner) parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

    This parameter is intended for content partners that own and manage many different YouTube channels. The parameter enables those partners to authenticate once and get access to all of their video and channel data, without having to provide authentication credentials for each individual channel.

    The [channels.list](https://developers.google.com/youtube/v3/docs/channels/list), [search.list](https://developers.google.com/youtube/v3/docs/search/list), [videos.delete](https://developers.google.com/youtube/v3/docs/videos/delete), [videos.list](https://developers.google.com/youtube/v3/docs/videos/list), and [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) methods all support this parameter.
  - The [managedByMe](https://developers.google.com/youtube/v3/docs/channels/list#managedByMe) parameter, which is supported by the [channels.list](https://developers.google.com/youtube/v3/docs/channels/list) method, instructs the API to return all channels owned by the content owner that the [onBehalfOfContentOwner](https://developers.google.com/youtube/v3/docs/channels/list#onBehalfOfContentOwner) parameter specifies.

  - The [forContentOwner](https://developers.google.com/youtube/v3/docs/search/list#forContentOwner) parameter, which is supported by the [search.list](https://developers.google.com/youtube/v3/docs/search/list) method, instructs the API to restrict search results to only include resources that are owned by the content owner that the [onBehalfOfContentOwner](https://developers.google.com/youtube/v3/docs/channels/list#onBehalfOfContentOwner) parameter specifies.

### February 25, 2013

This update contains the following changes:

- The API supports several new parts and properties for [video](https://developers.google.com/youtube/v3/docs/videos) resources:

  - The new [fileDetails](https://developers.google.com/youtube/v3/docs/videos#fileDetails), [processingDetails](https://developers.google.com/youtube/v3/docs/videos#processingDetails), and [suggestions](https://developers.google.com/youtube/v3/docs/videos#suggestions) parts provide information to video owners about their uploaded videos. This data is very useful in applications that enable video uploads and includes the following:

    <br />

    - processing status and progress
    - errors or other issues encountered while processing a video
    - availability of thumbnail images
    - suggestions for improving video or metadata quality
    - details about the original file uploaded to YouTube

    <br />

    All of these parts can only be retrieved by the video owner. The list below briefly describes the new parts, and the [video](https://developers.google.com/youtube/v3/docs/videos) resource documentation defines all of the properties that each part contains.
    - The `fileDetails` object contains information about the video file that was uploaded to YouTube, including the file's resolution, duration, audio and video codecs, stream bitrates, and more.

    - The `processingProgress` object contains information about YouTube's progress in processing the uploaded video file. The object's properties identify the current processing status and estimate the time remaining until YouTube finishes processing the video. This part also indicates whether different types of data or content, such as file details or thumbnail images, are available for the video.

      This object is designed to be polled so that the video uploader can track the progress that YouTube has made in processing the uploaded video file.
    - The `suggestions` object contains suggestions that identify opportunities to improve the video quality or the metadata for the uploaded video.

  - The `contentDetails` part contains four new properties. These properties can be retrieved with unauthenticated requests.

    <br />

    - [dimension](https://developers.google.com/youtube/v3/docs/videos#contentDetails.dimension) -- Indicates whether the video is available in 2D or 3D.
    - [definition](https://developers.google.com/youtube/v3/docs/videos#contentDetails.definition) -- Indicates whether the video is available in standard or high definition.
    - [caption](https://developers.google.com/youtube/v3/docs/videos#contentDetails.caption) -- Indicates whether captions are available for the video.
    - [licensedContent](https://developers.google.com/youtube/v3/docs/videos#contentDetails.licensedContent) -- Indicates whether the video contains content that has been claimed by a YouTube content partner.

    <br />

  - The `status` part contains two new properties. Video owners can set values for both properties when inserting or updating a video. These properties can also be retrieved with unauthenticated requests.

    <br />

    - [embeddable](https://developers.google.com/youtube/v3/docs/videos#status.embeddable) -- Indicates whether the video can be embedded on another website.
    - [license](https://developers.google.com/youtube/v3/docs/videos#status.license) -- Specifies the video's license. Valid values are `creativeCommon` and `youtube`.

    <br />

- The definition of the `part` parameter has been updated for the [videos.list](https://developers.google.com/youtube/v3/docs/videos/list), [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert), and [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) methods to list the newly added parts described above as well as the `recordingDetails` part, which had been inadvertently omitted.

- The `channel` resource's new [contentDetails.googlePlusUserId](https://developers.google.com/youtube/v3/docs/channels#contentDetails.googlePlusUserId) property specifies the Google+ profile ID associated with the channel. This value can be used to generate a link to the Google+ profile.

- Each thumbnail image object now specifies the image's width and height. Thumbnail images are currently returned in [activity](https://developers.google.com/youtube/v3/docs/activities), [channel](https://developers.google.com/youtube/v3/docs/channels), [playlist](https://developers.google.com/youtube/v3/docs/playlists), [playlistItem](https://developers.google.com/youtube/v3/docs/playlistItems), [search result](https://developers.google.com/youtube/v3/docs/search), [subscription](https://developers.google.com/youtube/v3/docs/subscriptions), and [video](https://developers.google.com/youtube/v3/docs/videos) resources.

- The `playlistItems.list` now supports the [videoId](https://developers.google.com/youtube/v3/docs/playlistItems/list#videoId) parameter, which can be used in conjunction with the [playlistId](https://developers.google.com/youtube/v3/docs/playlistItems/list#playlistId) parameter to only retrieve the playlist item that represents the specified video.

  The API returns a [notFound](https://developers.google.com/youtube/v3/docs/playlistItems/list#youtube.playlistItems.list-notFound-videoNotFound) error if the video that the parameter identifies cannot be found in the playlist.
- The [error documentation](https://developers.google.com/youtube/v3/docs/errors) describes a new [forbidden](https://developers.google.com/youtube/v3/docs/errors#gdata.CoreErrorDomain-forbidden-forbidden) error, which indicates that a request is not properly authorized for the requested action.

- The [channel](https://developers.google.com/youtube/v3/docs/channels) resource's `snippet.channelId` property has been removed. The resource's `id` property provides the same value.

### January 30, 2013

This update contains the following changes:

- The new [error](https://developers.google.com/youtube/v3/docs/errors) page lists errors that the API can return. The page includes general errors, which might occur for multiple different API methods, as well as method-specific errors.

### January 16, 2013

This update contains the following changes:

- Code samples are now available for the methods and languages shown in the list below:

  <br />

  - [activities.insert](https://developers.google.com/youtube/v3/docs/activities/insert#examples) -- Java
  - [playlistItems.insert](https://developers.google.com/youtube/v3/docs/playlistItems/insert#examples) -- Python
  - [playlistItems.list](https://developers.google.com/youtube/v3/docs/playlistItems/list#examples) -- Java, JavaScript, PHP, Python, Ruby
  - [playlists.insert](https://developers.google.com/youtube/v3/docs/playlists/insert#examples) -- Java, JavaScript, Python
  - [search.list](https://developers.google.com/youtube/v3/docs/search/list#examples) -- Java, JavaScript, Python, Ruby
  - [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert#examples) -- Java

  <br />

- An [activity](https://developers.google.com/youtube/v3/docs/activities) resource can now report a `channelItem` action, which occurs when YouTube adds a video to an [automatically generated YouTube channel](http://support.google.com/youtube/bin/answer.py?answer=2579942). (YouTube algorithmically identifies topics that have a significant presence on the YouTube website and automatically generates channels for those topics.)

- The following [search.list](https://developers.google.com/youtube/v3/docs/search/list#params) parameters have been updated:

  <br />

  - The `q` parameter is no longer designated as a filter, which means ....
  - The `relatedToVideo` parameter has been renamed `relatedToVideoId`.
  - The `published` parameter has been replaced with two new parameters, `publishedAfter` and `publishedBefore`, which are described below.

  <br />

- The [search.list](https://developers.google.com/youtube/v3/docs/search/list) method supports the following new parameters:

  |                                        Parameter name                                        |   Value    |                                                                                   Description                                                                                    |
  |----------------------------------------------------------------------------------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | [channelId](https://developers.google.com/youtube/v3/docs/search/list#channelId)             | `string`   | Return resources created by the specified channel.                                                                                                                               |
  | [publishedAfter](https://developers.google.com/youtube/v3/docs/search/list#publishedAfter)   | `datetime` | Return resources created after the specified time.                                                                                                                               |
  | [publishedBefore](https://developers.google.com/youtube/v3/docs/search/list#publishedBefore) | `datetime` | Return resources created before the specified time.                                                                                                                              |
  | [regionCode](https://developers.google.com/youtube/v3/docs/search/list#regionCode)           | `string`   | Return resources for the specified country.                                                                                                                                      |
  | [videoCategoryId](https://developers.google.com/youtube/v3/docs/search/list#videoCategoryId) | `string`   | Filter video search results to only include videos associated with the specified [video category](https://developers.google.com/youtube/v3/docs/videoCategories).                |
  | [videoEmbeddable](https://developers.google.com/youtube/v3/docs/search/list#videoEmbeddable) | `string`   | Filter video search results to only include videos that can be played in an embedded player on a web page. Set the parameter value to `true` to only retrieve embeddable videos. |
  | [videoSyndicated](https://developers.google.com/youtube/v3/docs/search/list#videoSyndicated) | `string`   | Filter video search results to only include videos that can be played outside of YouTube.com. Set the parameter value to `true` to only retrieve syndicated videos.              |

- Several API resources support new properties. The table below identifies the resources and their new properties:

  |                                                    Resource                                                     |                Property name                 |       Value        |                                                                                                                                                                        Description                                                                                                                                                                        |
  |-----------------------------------------------------------------------------------------------------------------|----------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | [activity](https://developers.google.com/youtube/v3/docs/activities#contentDetails.playlistItem.playlistItemId) | `contentDetails.playlistItem.playlistItemId` | `string`           | The playlist item ID that YouTube assigned to uniquely identify the item in the playlist.                                                                                                                                                                                                                                                                 |
  | [activity](https://developers.google.com/youtube/v3/docs/activities#contentDetails.channelItem)                 | `contentDetails.channelItem`                 | `object`           | An object that contains information about a resource that was added to a channel. This property is only present if the `snippet.type` is `channelItem`.                                                                                                                                                                                                   |
  | [activity](https://developers.google.com/youtube/v3/docs/activities#contentDetails.channelItem.resourceId)      | `contentDetails.channelItem.resourceId`      | `object`           | An object that identifies the resource that was added to the channel. Like other `resourceId` properties, it contains a `kind` property that specifies the resource type, such as video or playlist. It also contains exactly one of several properties -- `videoId`, `playlistId`, etc. -- that specifies the ID that uniquely identifies that resource. |
  | [channel](https://developers.google.com/youtube/v3/docs/channels#status)                                        | `status`                                     | `object`           | This object encapsulates information about the channel's privacy status.                                                                                                                                                                                                                                                                                  |
  | [channel](https://developers.google.com/youtube/v3/docs/channels#status.privacyStatus)                          | `status.privacyStatus`                       | `string`           | The channel's privacy status. Valid values are `private` and `public`.                                                                                                                                                                                                                                                                                    |
  | [playlist](https://developers.google.com/youtube/v3/docs/playlists#contentDetails)                              | `contentDetails`                             | `object`           | This object contains metadata about the playlist's content.                                                                                                                                                                                                                                                                                               |
  | [playlist](https://developers.google.com/youtube/v3/docs/playlists#contentDetails.itemCount)                    | `contentDetails.itemCount`                   | `unsigned integer` | The number of videos in the playlist.                                                                                                                                                                                                                                                                                                                     |
  | [playlist](https://developers.google.com/youtube/v3/docs/playlists#player)                                      | `player`                                     | `object`           | This object contains information that you would use to play the playlist in an embedded player.                                                                                                                                                                                                                                                           |
  | [playlist](https://developers.google.com/youtube/v3/docs/playlists#player.embedHtml)                            | `player.embedHtml`                           | `string`           | An `<iframe>` tag that embeds a video player that plays the playlist.                                                                                                                                                                                                                                                                                     |
  | [video](https://developers.google.com/youtube/v3/docs/videos#recordingDetails)                                  | `recordingDetails`                           | `object`           | This object encapsulates information that identifies or describes the place and time that the video was recorded.                                                                                                                                                                                                                                         |
  | [video](https://developers.google.com/youtube/v3/docs/videos#recordingDetails.location)                         | `recordingDetails.location`                  | `object`           | This object contains geolocation information associated with the video.                                                                                                                                                                                                                                                                                   |
  | [video](https://developers.google.com/youtube/v3/docs/videos#recordingDetails.location.latitude)                | `recordingDetails.location.latitude`         | `double`           | Latitude in degrees.                                                                                                                                                                                                                                                                                                                                      |
  | [video](https://developers.google.com/youtube/v3/docs/videos#recordingDetails.location.longitude)               | `recordingDetails.location.longitude`        | `double`           | Longitude in degrees.                                                                                                                                                                                                                                                                                                                                     |
  | [video](https://developers.google.com/youtube/v3/docs/videos#recordingDetails.location.elevation)               | `recordingDetails.location.elevation`        | `double`           | Altitude above the Earth, in meters.                                                                                                                                                                                                                                                                                                                      |
  | [video](https://developers.google.com/youtube/v3/docs/videos#recordingDetails.locationDescription)              | `recordingDetails.locationDescription`       | `string`           | A text description of the location where the video was recorded.                                                                                                                                                                                                                                                                                          |
  | [video](https://developers.google.com/youtube/v3/docs/videos#recordingDetails.recordingDate)                    | `recordingDetails.recordingDate`             | `datetime`         | The date and time when the video was recorded. The value is specified in [ISO 8601](https://www.w3.org/TR/NOTE-datetime) (`YYYY-MM-DDThh:mm:ss.sZ`) format.                                                                                                                                                                                               |

- The documentation for several API methods now identifies properties that must be specified in the request body or that are updated based on values in the request body. The table below lists those methods as well as the required or modifiable properties.

  **Note:** Documentation for other methods may already list required and modifiable properties.

  |                                           Method                                           |                                                                 Properties                                                                 |
  |--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
  | [activities.insert](https://developers.google.com/youtube/v3/docs/activities/insert)       | **Required properties:** - `snippet.description` **Modifiable properties:** - `snippet.description` - `contentDetails.bulletin.resourceId` |
  | [playlists.update](https://developers.google.com/youtube/v3/docs/playlists/update)         | **Required properties:** - `id`                                                                                                            |
  | [playlistItems.update](https://developers.google.com/youtube/v3/docs/playlistItems/update) | **Required properties:** - `id`                                                                                                            |
  | [videos.update](https://developers.google.com/youtube/v3/docs/videos/update)               | **Required properties:** - `id`                                                                                                            |

- The API no longer reports a `playlistAlreadyExists` error if you try to [create](https://developers.google.com/youtube/v3/docs/playlists/insert) or [update](https://developers.google.com/youtube/v3/docs/playlists/update) a playlist that would have the same title as a playlist that already exists in the same channel.

- Several API methods support new error types. The table below identifies the method and the newly supported errors:

  |                                           Method                                           | Error type  |         Error detail         |                                                                                                    Description                                                                                                     |
  |--------------------------------------------------------------------------------------------|-------------|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | [guideCategories.list](https://developers.google.com/youtube/v3/docs/guideCategories/list) | `notFound`  | `notFound`                   | The guide category identified by the `id` parameter cannot be found. Use the [guideCategories.list](https://developers.google.com/youtube/v3/docs/guideCategories/list) method to retrieve a list of valid values. |
  | [playlistItems.delete](https://developers.google.com/youtube/v3/docs/playlistItems/delete) | `forbidden` | `playlistItemsNotAccessible` | The request is not properly authorized to delete the specified playlist item.                                                                                                                                      |
  | [videoCategories.list](https://developers.google.com/youtube/v3/docs/videoCategories/list) | `notFound`  | `videoCategoryNotFound`      | The video category identified by the `id` parameter cannot be found. Use the [videoCategories.list](https://developers.google.com/youtube/v3/docs/videoCategories/list) method to retrieve a list of valid values. |