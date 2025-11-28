# Source: https://developers.google.com/youtube/v3/live/guides/migration-guide-default-broadcasts.md.txt

# Migration guide for deprecation of default broadcasts and streams

| **Note:** This guide relates to a [deprecation announcement](https://developers.google.com/youtube/v3/live/revision_history#release_notes_04_16_2020) made on April 16, 2020 that will go into effect on or after September 1, 2020. The actual date that the changes take effect is referred to below as the deprecation date. The announcement details a potentially breaking API change that will affect certain YouTube Live Streaming API clients.

## Overview

This guide is intended for developers of API client applications that use
YouTube channels' default `liveStream` and `liveBroadcast` resources to stream
live content. It aims to help you ensure that your application gracefully
handles the deprecation of default broadcasts and default streams, and it is
relevant for you if any of the following statements apply to your application:

- It checks the value of the `liveBroadcast` resource's [`isDefaultBroadcast`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#snippet.isDefaultBroadcast) property.
- It checks the value of the `liveStream` resource's [`isDefaultStream`](https://developers.google.com/youtube/v3/live/docs/liveStreams#snippet.isDefaultStream) property.
- It calls the [`liveBroadcasts.list`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list)
  method and sets the [`broadcastType`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list#broadcastType)
  parameter value to `persistent`. As of the deprecation date:

  - If the `broadcastType` parameter value is `persistent`, then the `liveBroadcasts.list` method will not return any results.
  - If the `broadcastType` parameter value is `all`, then the `liveBroadcasts.list` method will not return persistent broadcasts that existed before that time.

If your application is affected, please refer to the [Updating your
application](https://developers.google.com/youtube/v3/live/guides/migration-guide-default-broadcasts#updating_your_application) section, which explains the procedural
changes your application might need to make as a result of this deprecation.
That section identifies specific steps in the [Life of a broadcast](https://developers.google.com/youtube/v3/live/life-of-a-broadcast) guide that your API client might not
typically follow if it currently uses the default broadcast and stream.

## What is happening?

Since 2015, YouTube has automatically created a default stream and a default
broadcast for a channel when that channel was enabled for live streaming. The
default stream existed indefinitely and could not be deleted. Similarly, the
default broadcast was considered *persistent*. It always existed, did not have a
start or end time associated with it, and was not bound to a particular event.

As of the deprecation date mentioned above, YouTube will no longer create
default streams and broadcasts. This change affects client applications that
rely on those resources to broadcast live content. It will also affect
applications in which the user interface is customized to differentiate between
those default resources and other broadcasts and streams that channel owners
have created.

Instead of relying on the default resources, API clients need to create and
manage `liveBroadcast` and `liveStream` resources and to bind those resources
together.

## Updating your application

To quickly review terminology, a **broadcast** represents an event that can be
watched on YouTube as it happens, and a **stream** is the mechanism for sending
the actual video content to YouTube. A broadcast can be and needs to be bound to
exactly one stream.

### Migrating from default broadcasts

Prior to this deprecation, API clients could choose between using a channel's
default broadcast or creating an event-specific broadcast. The default broadcast
was a persistent resource that could be reused for multiple events, while an
event-specific broadcast resource is a single-use resource that corresponds to
exactly one YouTube video.

Your client application uses the default broadcast if it calls the
`liveBroadcasts.list` method and does either of the following:

- It sets the [`broadcastType`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list#broadcastType) parameter value to `persistent`. This request only retrieves the default broadcast.
- It sets the [`broadcastType`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list#broadcastType) parameter value to `all`, then identifies the `liveBroadcast` resource in the API response for which the [`isDefaultBroadcast`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#snippet.isDefaultBroadcast) property's value is `true`.

Following the deprecation, YouTube will only support event-specific broadcasts.
This means that instead of relying on the default broadcast, client applications
need to create [`liveBroadcast`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts) resources
for each individual broadcasting event.

To create a `liveBroadcast` resource, call the
[`liveBroadcasts.insert`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/insert) method.
This process is explained in [step 1.1 of the "Life of a broadcast" guide](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#stage_1_set_up_your_broadcast).

If it does not do so already, your user interface also needs to provide
mechanisms for users to distinguish and select between upcoming event-specific
broadcasts.

### Migrating from default streams

A stream enables you to transmit audio-video content to YouTube, and it defines
the settings for how you stream your content to YouTube. It is common for
broadcasters to reuse the same stream for many different broadcasts if those
broadcasts occur at different times.

Even though your application can't use the default stream, it can create a
reusable stream that can be reused for each broadcast. To create a `liveStream`
resource, call the [`liveStreams.insert`](https://developers.google.com/youtube/v3/live/docs/liveStreams/insert)
method, following the instructions in [step 1.2 of the "Life of a broadcast"
guide](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#step_12_create_your_stream). By
default, newly created streams are reusable. However, if you prefer, you can set the
[`contentDetails.isReusable`](https://developers.google.com/youtube/v3/live/docs/liveStreams#contentDetails.isReusable)
property to `false` to create single-use streams and have a one-to-one
relationship between broadcasts and streams.

The following list contains the four properties, besides the
[stream title](https://developers.google.com/youtube/v3/live/docs/liveStreams#snippet.title) and
[stream description](https://developers.google.com/youtube/v3/live/docs/liveStreams#snippet.description),
that you can set when creating a new stream. The list shows the values that
default streams use for each property, which are likely the settings you would
want to use in a client application if you're migrating away from using default
streams.

- [`cdn.frameRate`](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.frameRate) - `variable`
- [`cdn.ingestionType`](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.ingestionType) - `rtmp`
- [`cdn.resolution`](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.resolution) - `variable`
- [`contentDetails.isReusable`](https://developers.google.com/youtube/v3/live/docs/liveStreams#contentDetails.isReusable) - `true`

### Binding broadcasts to streams

Each `liveBroadcast` resource must be bound to exactly one stream before the
live broadcast on YouTube can actually start. (The broadcast is not bound to any
streams at the time that it's created.)

The binding process was handled automatically for the default broadcast, which
was inextricably bound to the default stream. However, after the deprecation
date, client applications need to manage that process for all broadcasts.

To bind a broadcast to a stream, call the
[`liveBroadcasts.bind`](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/bind) method as
explained in [step 1.3 of the "Life of a broadcast"
guide](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#step_13_bind_your_broadcast_to_its_stream).

- If you are using a reusable stream, you can create a stream once and then bind every broadcast to that stream.
- If you are not using a reusable stream, you need to create a broadcast and a stream, and then bind those two together.

### Testing your broadcast

When you don't use the default broadcast, you have the option to test your
broadcast. To conduct a test, you embed a player that lets you preview the
broadcast video as it would appear to YouTube viewers, but the broadcast is not
visible to other viewers.

If your API client previously used the default broadcast and stream, and you
want to add a testing phase to your streaming process, see [stage 3 of the
"Life of a broadcast" guide](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#stage_3_test).

If you do want to test your stream, then when you insert a broadcast, you need
to set the [contentDetails.monitorStream.enableMonitorStream](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.monitorStream.enableMonitorStream)
property to `true` and the [contentDetails.enableAutoStart](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableAutoStart) property to
`false`. These are the default values for both properties.

### Using the auto-start and auto-stop features

The default broadcast automatically started whenever you started streaming video
on the default stream. Similarly, the default broadcast ended after you stopped
streaming video. Each streaming session using those default resources
subsequently became a video in your channel.

While the auto-start and auto-stop features were the default behavior for
default broadcasts, those features are optional and need to be enabled for other
broadcasts. If you want to use these features, then when you insert a broadcast,
you need to set the [contentDetails.enableAutoStart](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableAutoStart) and
[contentDetails.enableAutoStop](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#contentDetails.enableAutoStop)
property values to `true`. These features are independent, so you can choose to
use one and not the other.

If you don't enable the auto-start and auto-stop features for new broadcasts,
your API client needs to call the [liveBroadcasts.transition](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/transition) method to update a broadcast's
status when you start and finish streaming video. In the "Life of a Broadcast"
guide, see [step 4.3](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#step_43_transition_your_broadcasts_status_to_live)
and [step 5.2](https://developers.google.com/youtube/v3/live/life-of-a-broadcast#step_52_transition_your_broadcasts_status_to_complete)
for instructions on managing these transitions at the beginning and end of a
broadcast.