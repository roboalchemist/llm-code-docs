# Source: https://developers.google.com/youtube/v3/live/broadcasts-and-streams.md.txt

# YouTube Live Streaming API - Understanding Broadcasts and Streams

This guide provides a brief overview of **broadcasts** and **streams**. It also discusses use cases that show how broadcasters use the YouTube Live Streaming API to create and manage those resources.

- A **broadcast** represents an event that can be watched on YouTube as it happens. Each broadcast is a distinct YouTube video. A broadcast can be and needs to be bound to exactly one stream.

- A **stream** enables you to transmit audio-video content to YouTube, and it defines the settings for how you stream your content to YouTube. The same stream can be bound to up to three live broadcasts. It is also common for broadcasters to reuse the same stream for many different broadcasts if those broadcasts occur at different times.

The remaining sections present three use cases that explain how API users typically use broadcasts and streams.

## Configure a single encoder

In the most common API use case, your YouTube channel has a series of scheduled or recurring live events. As the channel owner, you have a single encoder and only want to configure the encoder one time. So, you perform the following steps:

1. Create one [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams) resource in the API.
2. Use the content delivery settings from that resource to configure the encoder for the channel.
3. Note that, if you have multiple channels, you must create a different stream for each channel.
4. Create [liveBroadcast](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts) resources in the API and [bind](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/bind) all of those resources to the [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams) resource. In this scenario, every live event that you schedule for your channel uses the same streaming settings. However, only one event is live at any given time, and the video content for each broadcast is unique.
5. Any time an event occurs, update the broadcast's status to either `testing` or `live` and proceed to broadcast that event on YouTube.

## Create one stream per broadcast

Another common approach is to create a separate stream for each broadcast. In this scenario, you would create a distinct [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams) resource for each [liveBroadcast](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts) resource and then configure your streaming encoder to use the appropriate settings for each broadcast.

This approach might make sense if your channel has multiple recurring broadcasts such that two broadcasts might occur simultaneously, making it infeasible for both broadcasts to use the same streaming settings. In fact, your channel might treat each recurring broadcast as a show and just create one [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams) resource per show. Then, each episode of the same show would represent a broadcast, and all broadcasts of the same show could be bound to the same stream.

## Use one stream to create simultaneous broadcasts

In this scenario, you want to split a live stream into multiple, simultaneous broadcasts. As such, you have one [liveStream](https://developers.google.com/youtube/v3/live/docs/liveStreams) resource that is bound to two (or more) [liveBroadcast](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts) resources that have a `live` status at the same time.

For example, suppose your channel broadcasts a 24/7 live feed, but you also want to create a separate video for an interview that occurs during that broadcast. In this case, the interview content is a subset of the 24/7 broadcast's content.

To handle this case, you create two `liveBroadcast` resources and bind both broadcasts to the same stream. The 24/7 broadcast is ongoing and its resource has a `live` status long before the interview begins. When the interview begins, you update the status of the resource associated with the interview to `live` without changing the 24/7 broadcast's resource. Thus, you are streaming the same content to two separate videos at the same time.

When the interview ends, you update the interview broadcast's resource again, this time setting its status to `complete`. However, you don't stop streaming video since the 24/7 broadcast continues.