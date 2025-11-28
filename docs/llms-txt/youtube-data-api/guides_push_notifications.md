# Source: https://developers.google.com/youtube/v3/guides/push_notifications.md.txt

# Subscribe to Push Notifications

The YouTube Data API (v3) supports push notifications via [PubSubHubbub](https://github.com/pubsubhubbub/), a server-to-server publish/subscribe protocol for Web-accessible resources. Notifications are pushed out to subscribers via HTTP webhooks, which is much more efficient than polling-based solutions. With PubSubHubbub, your server finds out about events in near real-time, without having to determine the optimal polling interval or repeatedly fetching data that hasn't changed.

Your PubSubHubbub callback server receives Atom feed notifications when a channel does any of the following activities:

<br />

- uploads a video
- updates a video's title
- updates a video's description

<br />

The following steps explain how to subscribe to notifications:

1. Set up a callback server that can handle incoming Atom feed notifications.

2. Use the [Google](https://pubsubhubbub.appspot.com/subscribe) hub to subscribe to receive push notifications:

   - Set the **mode** to `subscribe`. (Or set the mode to `unsubscribe` to cancel a subscription.)

   - Set the **callback URL** to the URL that you set up in step 1.

   - Set the **topic URL** to `https://www.youtube.com/feeds/videos.xml?channel_id=`**CHANNEL_ID**, where **CHANNEL_ID** is the [YouTube channel ID](https://developers.google.com/youtube/v3/docs/channels#id) for which you want to retrieve push notifications.

3. Process notifications sent to your callback server. The notification format is shown below. Note that you can use the `<yt:videoId>` element's value to identify the newly added or updated video. You can also use the `<yt:channelId>` element's value to identify the channel that owns that video.

   ```
   <feed xmlns:yt="http://www.youtube.com/xml/schemas/2015"
            xmlns="http://www.w3.org/2005/Atom">
     <link rel="hub" href="https://pubsubhubbub.appspot.com"/>
     <link rel="self" href="https://www.youtube.com/xml/feeds/videos.xml?channel_id=CHANNEL_ID"/>
     <title>YouTube video feed</title>
     <updated>2015-04-01T19:05:24.552394234+00:00</updated>
     <entry>
       <id>yt:video:VIDEO_ID</id>
       <yt:videoId>VIDEO_ID</yt:videoId>
       <yt:channelId>CHANNEL_ID</yt:channelId>
       <title>Video title</title>
       <link rel="alternate" href="http://www.youtube.com/watch?v=VIDEO_ID"/>
       <author>
        <name>Channel title</name>
        <uri>http://www.youtube.com/channel/CHANNEL_ID</uri>
       </author>
       <published>2015-03-06T21:40:57+00:00</published>
       <updated>2015-03-09T19:05:24.552394234+00:00</updated>
     </entry>
   </feed>
   ```