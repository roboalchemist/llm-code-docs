# Source: https://developers.google.com/youtube/v3/live/docs/liveChatBans.md.txt

# LiveChatBans

A **liveChatBan** resource identifies a YouTube user and a YouTube live chat that the user is banned from participating in.

## Methods

The API supports the following methods for `liveChatBans` resources:

[insert](https://developers.google.com/youtube/v3/live/docs/liveChatBans/insert)
:   Bans a specific user from participating in the live chat. The API request must be authorized by the channel owner or a moderator of the live chat associated with the ban.
    [Try it now](https://developers.google.com/youtube/v3/live/docs/liveChatBans/insert#try-it).

[delete](https://developers.google.com/youtube/v3/live/docs/liveChatBans/delete)
:   Removes a ban that prevents a specific user from contributing to a live chat, thereby enabling the user to rejoin the chat. The API request must be authorized by the channel owner or a moderator of the live chat associated with the ban.
    [Try it now](https://developers.google.com/youtube/v3/live/docs/liveChatBans/delete#try-it).

## Resource representation

The following JSON structure shows the format of a `liveChatBans` resource:  

```carbon
{
  "https://developers.google.com/youtube/v3/live/docs/liveChatBans#kind": "youtube#liveChatBan",
  "https://developers.google.com/youtube/v3/live/docs/liveChatBans#etag": etag,
  "https://developers.google.com/youtube/v3/live/docs/liveChatBans#id": string,
  "https://developers.google.com/youtube/v3/live/docs/liveChatBans#snippet": {
    "https://developers.google.com/youtube/v3/live/docs/liveChatBans#snippet.liveChatId": string,
    "https://developers.google.com/youtube/v3/live/docs/liveChatBans#snippet.type": string,
    "https://developers.google.com/youtube/v3/live/docs/liveChatBans#snippet.banDurationSeconds": unsigned long,
    "https://developers.google.com/youtube/v3/live/docs/liveChatBans#snippet.bannedUserDetails": {
      "https://developers.google.com/youtube/v3/live/docs/liveChatBans#snippet.bannedUserDetails.channelId": string
    }
  }
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                                                    Properties                                                                                                     ||
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kind`                                | `string` Identifies the API resource's type. The value will be `youtube#liveChatBan`.                                                                                      |
| `etag`                                | `etag` The Etag of this resource.                                                                                                                                          |
| `id`                                  | `string` The ID that YouTube assigns to uniquely identify the ban.                                                                                                         |
| `snippet`                             | `object` The `snippet` object identifies the banned user and contains details about the ban.                                                                               |
| snippet.`liveChatId`                  | `string` The live chat to which the ban applies. The live chat ID associated with a broadcast is returned in the `liveBroadcast` resource's `snippet.liveChatId` property. |
| snippet.`type`                        | `string` The type of ban. Valid values for this property are: - `permanent` - `temporary`                                                                                  |
| snippet.`banDurationSeconds`          | `unsigned long` The duration of the ban. Only set a value for this property if the ban's type is `temporary`. The default value is `300` (5 minutes).                      |
| snippet.`bannedUserDetails`           | `object` This object contains information that identifies the banned user.                                                                                                 |
| snippet.bannedUserDetails.`channelId` | `string` The banned user's YouTube channel ID.                                                                                                                             |