# Source: https://developers.google.com/youtube/v3/live/docs.md.txt

This API reference explains how to schedule live broadcasts and video streams on YouTube using the YouTube Live Streaming API.

## Resource types

### LiveBroadcasts

A**liveBroadcast**resource represents an event that will be streamed, via live video, on YouTube.

For more information about this resource, see its[resource representation](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#resource)and list of[properties](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts#properties).

|                                           Method                                           |           HTTP request            |                                                                                                                                                                                                                                         Description                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| URIs relative to`https://www.googleapis.com/youtube/v3`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |||
| [bind](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/bind)             | `POST /liveBroadcasts/bind`       | Binds a YouTube broadcast to a stream or removes an existing binding between a broadcast and a stream. A broadcast can only be bound to one video stream, though a video stream may be bound to more than one broadcast.                                                                                                                                                                                                                                                                    |
| [delete](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/delete)         | `DELETE /liveBroadcasts`          | Deletes a broadcast.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [insert](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/insert)         | `POST /liveBroadcasts`            | Creates a broadcast.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [list](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list)             | `GET /liveBroadcasts`             | Returns a list of YouTube broadcasts that match the API request parameters.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [transition](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/transition) | `POST /liveBroadcasts/transition` | Changes the status of a YouTube live broadcast and initiates any processes associated with the new status. For example, when you transition a broadcast's status to`testing`, YouTube starts to transmit video to that broadcast's monitor stream. Before calling this method, you should confirm that the value of the[status.streamStatus](https://developers.google.com/youtube/v3/live/docs/liveStreams#status.streamStatus)property for the stream bound to your broadcast is`active`. |
| [update](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/update)         | `PUT /liveBroadcasts`             | Updates a broadcast. For example, you could modify the broadcast settings defined in the`liveBroadcast`resource's`contentDetails`object.                                                                                                                                                                                                                                                                                                                                                    |
| [cuepoint](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/cuepoint)     | `POST /liveBroadcasts/cuepoint`   | Inserts a cuepoint into a live broadcast. The cuepoint might trigger an ad break.                                                                                                                                                                                                                                                                                                                                                                                                           |

### LiveChatBans

A**liveChatBan**resource identifies a YouTube user and a YouTube live chat that the user is banned from participating in.

For more information about this resource, see its[resource representation](https://developers.google.com/youtube/v3/live/docs/liveChatBans#resource)and list of[properties](https://developers.google.com/youtube/v3/live/docs/liveChatBans#properties).

|                                      Method                                       |      HTTP request       |                                                                                                                 Description                                                                                                                  |
|-----------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| URIs relative to`https://www.googleapis.com/youtube/v3`                                                                                                                                                                                                                                                                                                  |||
| [delete](https://developers.google.com/youtube/v3/live/docs/liveChat/bans/delete) | `DELETE /liveChat/bans` | Removes a ban that prevents a specific user from contributing to a live chat, thereby enabling the user to rejoin the chat. The API request must be authorized by the channel owner or a moderator of the live chat associated with the ban. |
| [insert](https://developers.google.com/youtube/v3/live/docs/liveChat/bans/insert) | `POST /liveChat/bans`   | Bans a specific user from participating in the live chat. The API request must be authorized by the channel owner or a moderator of the live chat associated with the ban.                                                                   |

### LiveChatMessages

A**liveChatMessage**resource represents a chat message in a YouTube live chat. The resource can contain details about several types of messages, including a newly posted text message or fan funding event.  

The live chat feature is enabled by default for live broadcasts and is available while the live event is active. (After the event ends, live chat is no longer available for that event.)

For more information about this resource, see its[resource representation](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#resource)and list of[properties](https://developers.google.com/youtube/v3/live/docs/liveChatMessages#properties).

|                                            Method                                             |                                                HTTP request                                                |                                                               Description                                                                |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| URIs relative to`https://www.googleapis.com/youtube/v3`                                                                                                                                                                                                                                                                                             |||
| [delete](https://developers.google.com/youtube/v3/live/docs/liveChat/messages/delete)         | `DELETE /liveChat/messages`                                                                                | Deletes a chat message. The API request must be authorized by the channel owner or a moderator of the live chat associated with the ban. |
| [insert](https://developers.google.com/youtube/v3/live/docs/liveChat/messages/insert)         | `POST /liveChat/messages`                                                                                  | Adds a message to a live chat.                                                                                                           |
| [list](https://developers.google.com/youtube/v3/live/docs/liveChat/messages/list)             | `GET /liveChat/messages`                                                                                   | Lists live chat messages for a specific chat.                                                                                            |
| [streamList](https://developers.google.com/youtube/v3/live/docs/liveChat/messages/streamList) | Enables a server-streaming connection for receiving live chat messages for a specific chat in low latency. |

### LiveChatModerators

A**liveChatModerator**resource represents a moderator for a YouTube live chat. A chat moderator has the ability to ban or unban users from a chat, remove messages, and perform other administrative actions for the live chat.

For more information about this resource, see its[resource representation](https://developers.google.com/youtube/v3/live/docs/liveChatModerators#resource)and list of[properties](https://developers.google.com/youtube/v3/live/docs/liveChatModerators#properties).

|                                         Method                                          |         HTTP request          |                                                   Description                                                   |
|-----------------------------------------------------------------------------------------|-------------------------------|-----------------------------------------------------------------------------------------------------------------|
| URIs relative to`https://www.googleapis.com/youtube/v3`                                                                                                                                                                                 |||
| [delete](https://developers.google.com/youtube/v3/live/docs/liveChat/moderators/delete) | `DELETE /liveChat/moderators` | Removes a chat moderator. The request must be authorized by the owner of the live broadcast's channel.          |
| [insert](https://developers.google.com/youtube/v3/live/docs/liveChat/moderators/insert) | `POST /liveChat/moderators`   | Adds a new moderator for the chat. The request must be authorized by the owner of the live broadcast's channel. |
| [list](https://developers.google.com/youtube/v3/live/docs/liveChat/moderators/list)     | `GET /liveChat/moderators`    | Lists moderators for a live chat. The request must be authorized by the owner of the live broadcast's channel.  |

### LiveStreams

A**liveStream**resource contains information about the video stream that you are transmitting to YouTube. The stream provides the content that will be broadcast to YouTube users. Once created, a`liveStream`resource can be bound to one or more[liveBroadcast](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts)resources.

For more information about this resource, see its[resource representation](https://developers.google.com/youtube/v3/live/docs/liveStreams#resource)and list of[properties](https://developers.google.com/youtube/v3/live/docs/liveStreams#properties).

|                                     Method                                      |     HTTP request      |                                                                     Description                                                                     |
|---------------------------------------------------------------------------------|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| URIs relative to`https://www.googleapis.com/youtube/v3`                                                                                                                                                                                                     |||
| [delete](https://developers.google.com/youtube/v3/live/docs/liveStreams/delete) | `DELETE /liveStreams` | Deletes a video stream.                                                                                                                             |
| [insert](https://developers.google.com/youtube/v3/live/docs/liveStreams/insert) | `POST /liveStreams`   | Creates a video stream. The stream enables you to send your video to YouTube, which can then broadcast the video to your audience.                  |
| [list](https://developers.google.com/youtube/v3/live/docs/liveStreams/list)     | `GET /liveStreams`    | Returns a list of video streams that match the API request parameters.                                                                              |
| [update](https://developers.google.com/youtube/v3/live/docs/liveStreams/update) | `PUT /liveStreams`    | Updates a video stream. If the properties that you want to change cannot be updated, then you need to create a new stream with the proper settings. |

### SuperChatEvents

A**superChatEvent**resource represents a Super Chat message purchased by a fan during a YouTube live stream. In the YouTube live chat stream, Super Chats stand out from other messages in two ways:

<br />

- Super Chats are highlighted with a color.
- Super Chats stay pinned in the ticker for a set period of time.

<br />

The color of the Super Chat, the period of time it stays pinned in the ticker, and the maximum message length are all determined by the purchase amount. See the[YouTube Help Center](https://support.google.com/youtube/answer/7277005)to learn more about Super Chats.

For more information about this resource, see its[resource representation](https://developers.google.com/youtube/v3/live/docs/superChatEvents#resource)and list of[properties](https://developers.google.com/youtube/v3/live/docs/superChatEvents#properties).

|                                     Method                                      |      HTTP request      |                                  Description                                  |
|---------------------------------------------------------------------------------|------------------------|-------------------------------------------------------------------------------|
| URIs relative to`https://www.googleapis.com/youtube/v3`                                                                                                                                |||
| [list](https://developers.google.com/youtube/v3/live/docs/superChatEvents/list) | `GET /superChatEvents` | List Super Chat events from a channel's live streams in the previous 30 days. |