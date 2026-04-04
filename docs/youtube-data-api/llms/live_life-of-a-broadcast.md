# Source: https://developers.google.com/youtube/v3/live/life-of-a-broadcast.md.txt

# Life of a Broadcast

## Introduction

This document walks you through the life of a live broadcast on YouTube that
is created and managed using the YouTube Live Streaming API and the
[YouTube Content ID API](https://developers.google.com/youtube/partner).

## Resources and resource types

As explained in the [getting started](https://developers.google.com/youtube/v3/live/getting-started#resources) guide, a resource is an individual
data entity with a unique identifier. To create and manage live events on
YouTube, you will use a number of different types of resources that are
defined as part of either the [YouTube Data API](https://developers.google.com/youtube/v3) or the
[YouTube Content ID API](https://developers.google.com/youtube/partner). The resources listed under the
**YouTube Live Streaming API** header are technically defined in those other
APIs but are listed separately because they are only used for live broadcasts.

**YouTube Live Streaming API resources**

- [`liveBroadcast`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts)
- [`liveStream`](https://developers.google.com/youtube/v3/live/docs/liveStreams)
- [`cuepoint`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/cuepoint)

**YouTube Data API resources**

- [`video`](https://developers.google.com/youtube/v3/docs/videos)

**YouTube Content ID API resources**

- [`asset`](https://developers.google.com/youtube/partner/docs/v1/assets)
- [`claim`](https://developers.google.com/youtube/partner/docs/v1/claims)
- [`policy`](https://developers.google.com/youtube/partner/docs/v1/policies)
- [`videoAdvertisingOption`](https://developers.google.com/youtube/partner/docs/v1/videoAdvertisingOptions)

## Create and manage a live broadcast

The following steps explain how to create and manage a live event on YouTube.
The steps are divided into the following stages:

1. [Set up your broadcast](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#stage_1_set_up_your_broadcast)
2. [Claim your content](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#stage_2_claim_your_content)
3. [Test](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#stage_3_test)
4. [Broadcast](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#stage_4_broadcast)
5. [Conclude your broadcast](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#stage_5_conclude_your_broadcast)
6. [Create a reference](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#stage_6_create_a_reference)

### Stage 1: Set up your broadcast

#### Step 1.1: Create your broadcast

Call the [`liveBroadcasts.insert`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/insert)
method to add your broadcast to YouTube's schedule of live events. The
`liveBroadcast` resource that you are inserting must define values for the
properties listed below.

- [`snippet.title`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#snippet.title)
- [`snippet.scheduledStartTime`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#snippet.scheduledStartTime)
- [`status.privacyStatus`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#status.privacyStatus)

Please consider the following guidelines when setting up your broadcast:

- If you want to have a testing phase for your broadcast, when you can view
  your video broadcast without other viewers also being able to see the
  broadcast, you must set the
  `contentDetails.monitorStream.enableMonitorStream` property to `true` and
  the `contentDetails.enableAutoStart` property to `false`. These are the
  default values for both properties.

- If you want to create a reference from your recorded broadcast, you must
  set the broadcast's [`contentDetails.recordFromStart`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.recordFromStart)
  property to `true`. If you want to make the recorded video available for
  playback immediately after the broadcast ends, you must also set the
  [`contentDetails.enableDvr`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableDvr) property to
  `true`. (Both of these properties have a default value of `true`.)

- You can update any of the `contentDetails` properties as long as your
  broadcast's status is still `created` or `ready`.

- You can update the broadcast's scheduled start time and scheduled end time
  as long as the broadcast's status is `created`, `ready`, or `testing`.

- The broadcast's title, description, and privacy status, and other metadata
  fields that are part of the broadcast's [`video`](https://developers.google.com/youtube/v3/docs/videos)
  resource, can be updated at any time.  


  **Note:** If you only want your video to be available to specific YouTube
  users, set the `status.privacyStatus` property value to either `unlisted`
  or `private` as appropriate to your needs.

**Processing the API response**

When you call the `liveBroadcasts.insert` method, the API response contains the
`liveBroadcast` resource that you created. Your code should extract and store
the [`id`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#id) from that resource. You
will need that value to identify the broadcast in future API requests. (You
can also identify the [`video`](https://developers.google.com/youtube/v3/docs/videos) resource that
corresponds to the `liveBroadcast` resource using the same ID.)

#### Step 1.2: Create your stream

A **`liveStream`** resource enables you to transmit your video to YouTube, and
it describes the content that you are transmitting. Each broadcast must be
associated with exactly one stream.

Call the `liveStreams.insert` method to create the video stream for your
event. When creating your stream, you must set values for the properties
listed below:

- [`snippet.title`](https://developers.google.com/youtube/v3/live/docs/liveStreams#snippet.title)
- [`cdn.frameRate`](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.frameRate)
- [`cdn.ingestionType`](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.ingestionType)
- [`cdn.resolution`](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.resolution)

With the exception of the stream's title, these values cannot be updated after
the stream is created. If you need to change them, then you actually need to
create a different stream by repeating this step. This process is discussed in
more detail in [step 3.5](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#step_35_completing_your_testing) later in this
document.

You also have the option of setting values for the following properties:

- [`snippet.description`](https://developers.google.com/youtube/v3/live/docs/liveStreams#snippet.description) - like the stream title, the stream description can be updated after the stream is created. Neither the title nor the description is visible to YouTube users.
- [`contentDetails.isReusable`](https://developers.google.com/youtube/v3/live/docs/liveStreams#contentDetails.isReusable) -
  Indicates whether the stream is reusable, which means that it can be bound
  to multiple broadcasts. This property's value effectively determines whether
  a channel has a many-to-one or one-to-one relationship between
  `liveBroadcast` and `liveStream` resources:

  - If you use the property's default value of `true`, then you can use the same `liveStream` resource for all of a channel's broadcasts. That means you do not need to repeat this step (1.2) for every broadcast. Instead, you can just reuse the stream ID for subsequent broadcasts.
  - If you set the property value to `false`, then you need to create a new stream for each broadcast.

After you issue the API request the stream, the API response contains the
`liveStream` resource that you created. Your code should extract and store the
[`id`](https://developers.google.com/youtube/v3/live/docs/liveStreams#id) from that resource. You will need
that value to identify the stream in future API requests.

#### Step 1.3: Bind your broadcast to its stream

Having created your `liveBroadcast` and `liveStream` resources, you now need
to associate the two using the [`liveBroadcasts.bind`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/bind) method. This action links the video
bits that you will transmit to YouTube with the event broadcast for that video.

In calling the `liveBroadcasts.bind` method, set the `id` parameter to the
broadcast ID obtained in step 1.1 and the `streamId` parameter to the stream
ID obtained in step 1.2.

### Stage 2: Claim your content

If you want like to show ads during your broadcast, you need to claim the
broadcast video before the event begins. The following steps explain this
process. Note that all of the API calls discussed in this stage are defined in
the [YouTube Content ID API](https://developers.google.com/youtube/partner).

#### Step 2.1: Create an asset

An [`asset`](https://developers.google.com/youtube/partner/docs/v1/assets) resource represents a piece of
intellectual property. In this case, the asset is your broadcast. Call the
[`assets.insert`](https://developers.google.com/youtube/partner/docs/v1/assets/insert) method to create
your asset.

The API response will contain the `asset` resource that you created. Your code
should extract and store the [`id`](https://developers.google.com/youtube/partner/docs/v1/assets#id) from
that resource as you will need that value to identify the asset in future API
requests.

#### Step 2.2: Define your ownership of the asset

An asset's ownership data identifies an asset's owners as well as the
territories where they own the asset. YouTube uses this data to determine
where an owner can set the policy for a claimed video.

For example, if you have the right to broadcast an event in the United States,
and another broadcaster owns the same rights for Canada, then you can each
define different policies for the broadcast video and for user-uploaded videos
that match the broadcast video. Your match policy will apply to matching
user-uploaded videos in the United States, while the other owner's policy
will apply to matching videos in Canada.

To define your ownership territories for the asset, call the
[`ownership.update`](https://developers.google.com/youtube/partner/docs/v1/ownership/update) method.
In that request, set the `assetId` parameter to the `id` that you stored in
step 2.1.

#### Step 2.3: Set the asset's match policy

An asset's match policy explains what YouTube should do when a user uploads
a video that matches a reference associated with the asset. In this case, the
match policy will indicate how YouTube should handle an uploaded video that
matches your live broadcast.

**Note:** You should set a match policy if you
plan to [create a reference](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#stage_6_create_a_reference) from your
broadcast video and use that reference to identify user-uploaded videos that
match your broadcast. Otherwise, you can skip this step.

To set the match policy, you first need to identify the policy that you want
to apply. You can retrieve a list of existing policies by calling the
[`policies.list`](https://developers.google.com/youtube/partner/docs/v1/policies/list) method, or you can
define a new policy by calling the
[`policies.insert`](https://developers.google.com/youtube/partner/docs/v1/policies/insert) method. In
either case, you need to capture the `id` of the policy you want to apply.

Once you have identified the policy, call the
[`assetMatchPolicy.update`](https://developers.google.com/youtube/partner/docs/v1/assetMatchPolicy/update)
method. In that request, set the `assetId` parameter to the `id` that you
stored in step 2.1.

#### Step 2.4: Claim your video

In this step, you create a claim, which links the video that you will
broadcast to the asset that you created in step 2.1. The claim sets a policy
that applies only to your broadcast video. (User-uploaded videos that match
your broadcast video are covered by the match policy set in the previous step.)

To create a claim, call the [`claims.insert`](https://developers.google.com/youtube/partner/docs/v1/claims/insert) method. In the `claim` resource that
you insert, you need to set values for the following properties:

- `assetId` -- You obtained this value in step 2.1.
- `videoId` -- This is the broadcast ID that you obtained in step 1.1.
- `policy` -- This is a [`policy`](https://developers.google.com/youtube/partner/docs/v1/policies) resource. You can apply an existing policy by setting that resource's `id` property to the existing policy's ID. The previous step explains how to retrieve the ID of an existing policy.
- `contentType` -- Set this value to `audiovisual`.

**Processing the API response**

When you insert the claim, the API response will contain the `claim` resource
that you created. Your code should extract and store the
[`id`](https://developers.google.com/youtube/partner/docs/v1/claims#id) from that resource. You will use
that value later to create a reference from your processed video.

#### Step 2.5: Update the ad settings for the broadcast

You need to set the advertising options for your video if you want to either
run a preroll ad when viewers start to watch your broadcast or run ads during
breaks in your broadcast.

- If you enable preroll ads for your broadcast, then all viewers will see an ad when they start to watch your broadcast even if they start watching in the middle of the broadcast.
- If you enable midroll ads for your broadcast, then you will be able to insert [ad cuepoints](https://developers.google.com/youtube/v3/live/getting-started#core-concepts) during the broadcast.

To enable ads, call the [`videoAdvertisingOptions.update`](https://developers.google.com/youtube/partner/docs/v1/videoAdvertisingOptions/update) method. In your
request, set the `videoId` parameter to the broadcast `id` that you obtained
in step 1.1. Use the `videoAdvertisingOption` resource's
[`adFormats[]`](https://developers.google.com/youtube/partner/docs/v1/videoAdvertisingOptions#adFormats%5B%5D)
property to identify the ad formats (`preroll`, `midroll`, or `postroll`) that
you want to enable.

### Stage 3: Test

| **Note:** This stage is optional. If you don't plan to have a testing stage, consider setting the `liveBroadcast` resource's [`contentDetails.enableAutoStart`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableAutoStart) and [`contentDetails.enableAutoStop`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableAutoStop) properties to `true` to simplify the streaming process. When those properties are set to `true`, YouTube automatically starts the broadcast when you start streaming video on the bound live stream and automatically ends the broadcast about a minute after you stop transmitting video.

During this stage, you embed a player that shows the monitor stream for your
broadcast so that you can test the viewing experience. The monitor stream is a
private stream that lets you preview the broadcast video as it would appear
to YouTube viewers.

Note that you can only test your video broadcast if its monitor stream is
enabled. By default, broadcasts' monitor streams are enabled. You can disable a
broadcast's monitor stream by setting the
[contentDetails.monitorStream.enableMonitorStream](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.monitorStream.enableMonitorStream)
property to `false` when creating or updating that broadcast.

#### Step 3.1: Embed a monitor stream player

Retrieve your broadcast using the [`liveBroadcasts.list`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list) method, and extract the value of
the `contentDetails.streamDetails.monitorStreamEmbedHtml` property. That value
contains the HTML that you need to embed a YouTube player that shows your
monitor stream.

#### Step 3.2: Start your video

Start transmitting video on your video stream.

#### Step 3.3: Confirm your video stream is active

Call the [`liveStreams.list`](https://developers.google.com/youtube/v3/live/docs/liveStreams/list) method
to retrieve the `liveStream` resource associated with your broadcast. Confirm
that the [`status.streamStatus`](https://developers.google.com/youtube/v3/live/docs/liveStreams#status.streamStatus) property's value is
`active`, which indicates that YouTube servers are receiving data from your
encoder correctly.

#### Step 3.4: Transition your broadcast's status to testing

Call the [`liveBroadcasts.transition`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/transition) method to update the
broadcast's status. Set the `id` parameter value to the broadcast ID obtained
in step 1.1, and set the `broadcastStatus` parameter value to `testing`.

After you call the [`liveBroadcasts.transition`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/transition) method, it may take several
seconds, or even up to a minute, for that transition to complete. During that
time, you should poll the API to check the broadcast's status. Until the
transition is complete, the broadcast's status will be `testStarting`. The
status will be `testing` once the transition is complete.

#### Step 3.5: Completing your testing

If your test went smoothly, you can move ahead to [stage 4](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#stage_4_broadcast).
However, in some cases, you might need to do further testing. For example,
if your testing reveals that the video stream is not configured correctly,
you need to remedy that before proceeding with your broadcast.

If the video stream is not configured correctly, then you need to unbind (and
delete) the existing stream and create a new stream. As an example, a stream
might not be configured correctly if it specifies the wrong video format.

1. To unbind the video stream, call the
   [liveBroadcasts.bind](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/bind)
   method from step 1.3. In the API request, set the `id`
   parameter to the `id` obtained in step 1.1. Do not include the
   `streamId` parameter in the request.

2. To delete the video stream, call the
   [liveStreams.delete](https://developers.google.com/youtube/v3/live/docs/liveStreams/delete)
   method. In the request, set the `id` parameter to the
   `id` obtained in step 1.2.

3. Repeat step 1.2 to create a new, properly configured
   `liveStream` resource. Then repeat step 1.3 to bind the new
   stream to your broadcast and steps 3.1 to 3.3 to test the new stream.

#### Step 3.6: Enable `autoStart` and `autoStop` properties

| **Note:** This step is optional.

After you have successfully completed your testing stage, you have the option of
setting the broadcast's
[`contentDetails.enableAutoStart`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableAutoStart)
and [`contentDetails.enableAutoStop`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableAutoStop)
properties to `true` before the actual broadcast begins. These properties can't
be set to `true` before the testing stage because the test would actually cause
the broadcast to start.

### Stage 4: Broadcast

During this stage, your broadcast video is viewable to your audience.

#### Step 4.1: Start your video

Start transmitting video on your video stream.

#### Step 4.2: Confirm your video stream is active

Call the [`liveStreams.list`](https://developers.google.com/youtube/v3/live/docs/liveStreams/list) method
to retrieve the `liveStream` resource associated with your broadcast. Confirm
that the [`status.streamStatus`](https://developers.google.com/youtube/v3/live/docs/liveStreams#status.streamStatus) property's value is
`active`, which indicates that YouTube servers are receiving data from your
encoder correctly.

#### Step 4.3: Transition your broadcast's status to live

**Important:** This step makes your video
visible to your audience.

Call the [`liveBroadcasts.transition`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/transition) method to update the
broadcast's status. Set the `id` parameter value to the broadcast ID obtained
in step 1.1, and set the `broadcastStatus` parameter value to `live`.

**If you set the `liveBroadcast` resource's
[`contentDetails.enableAutoStart`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableAutoStart)
property to `true`, then you do not need to call the `liveBroadcasts.transition`
method.**

After you make this API call -- or, if you have set the `contentDetails.enableAutoStart`
property to `true`, after you start streaming -- you typically need to wait 5 to
10 seconds for that transition to complete. The transition might take up to a
minute. During that time, you
should poll the API to check the broadcast's status. Until the transition is
complete, the broadcast's status will be `liveStarting`. The status will be
`live` once the transition is complete, and viewers are able to watch your
broadcast from that point in your monitor stream.

Note the following effects of this command:

- If you have enabled the monitor stream for your broadcast -- see step 3.1 -- you will be able to see the monitor stream in an embedded player.
- If you had set a value for the broadcast's `contentDetails.streamDetails.broadcastStreamDelayMs` property, the broadcast stream, which is visible to other viewers, will be delayed by that amount of time.

#### Step 4.4: Insert ad breaks into your broadcast

Call the [`liveBroadcasts.cuepoint`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/cuepoint)
method to insert a cuepoint. The cuepoint might trigger an ad break. In the [`cuepoint`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/cuepoint#request-body) resource provided in
the request body, set the `durationSecs` property to the desired length of the
break (in seconds) that you want to show. (The default value is `30`.)

At this time, YouTube attempts to play an ad in the video player for any viewers
who were watching the broadcast when the ad cuepoint was inserted. Whether an ad
plays depends on a variety of factors, such as ad availability and the viewer's
ad-viewing history. Viewers who do get an ad break return to your broadcast when
the ad break is over, while viewers who are not shown an ad continue to view the
broadcast stream during the break.

The [Getting started](https://developers.google.com/youtube/v3/live/getting-started#Controlling_Your_Broadcast_Stream_Content)
guide provides more information about the viewing experience during a live broadcast's
ad break.

### Stage 5: Conclude your broadcast

#### Step 5.1: Stop streaming

This concludes your test of the YouTube live broadcast system.

#### Step 5.2: Transition your broadcast's status to complete

| **Note:** If you set the `liveBroadcast` resource's [`contentDetails.enableAutoStop`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableAutoStop) property to `true`, then you do not need to complete this step. YouTube will automatically end the broadcast around a minute after you stop sending video on the bound live stream.

When you are ready to stop broadcasting, call the API's
[`liveBroadcasts.transition`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/transition)
method to update the broadcast's status. Set the `id` parameter value to the
broadcast ID obtained in step 1.1, and set the `broadcastStatus` parameter
value to `complete`.

If you had set the broadcast's [`contentDetails.recordFromStart`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.recordFromStart) and
[`contentDetails.enableDvr`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableDvr) properties to
`true`, then when the live event ends, your audience can immediately watch
the live event playback.

### Stage 6: Create a reference

Once the live recording is complete, you can create a reference from the
recorded video. This action instructs YouTube to look for user-uploaded
videos that match the broadcast and handle them according to the match policy
that you set in [step 2.3](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#step_23_set_the_assets_match_policy).

**Important:** To create the reference, you
must have set the broadcast's [contentDetails.recordFromStart](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.recordFromStart)
property to `true`.

#### Step 6.1: Poll the Data API for the video's status

YouTube must finish processing a broadcast or uploaded video before you can
create a reference from that video. To determine whether the video has
finished processing, poll the YouTube Data API's [`videos.list`](https://developers.google.com/youtube/v3/docs/videos/list) method, setting the `part` parameter to `status`
and the `id` parameter to the broadcast ID that you stored in
[step 1.1](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#step_11_create_your_broadcast).

The API response to your polling request will contain a `video` resource.
When the value of that resource's [status.uploadStatus](https://developers.google.com/youtube/v3/docs/videos#status.uploadStatus) property is `processed`, proceed
to step 6.2.

#### Step 6.2: Create a reference from the processed video

To create your reference, call the Content ID API's `references.insert` method
and set the [`claimId`](https://developers.google.com/youtube/partner/docs/v1/references/insert#claimId)
parameter to the claim ID that you stored in
[step 2.4](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#step_24_claim_your_video).

**Live Content ID Delivery**

Some YouTube partners are able to create a reference before their broadcast
transitions to the `testing` state, but that feature is not available to all
partners. In that flow, YouTube generates and continually updates the
reference from your live event's broadcast stream while the broadcast in in
progress. In addition, YouTube looks for matching user-uploaded videos while
the broadcast is still in progress. Note that creating a reference before a
broadcast begins automatically turns recording on for the broadcast, and
recording cannot be turned off after the reference is created.

To enable your broadcast for live Content ID delivery, attempt the actions
described in step 6.2 after [claiming your video](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#step_24_claim_your_video) in step 2.4.
If your partner account has not been approved to create a reference for a live
broadcast before that broadcast occurs, the API will return a
[`fingerprintingNotAllowed`](https://developers.google.com/youtube/partner/docs/v1/references/insert#youtubePartner.references.insert-forbidden-fingerprintingNotAllowed)
error. In that case, you need to wait until your broadcast is complete, as
described in steps 6.1 and 6.2 above, before creating the reference.