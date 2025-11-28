# Source: https://developers.google.com/youtube/v3/live/docs/liveChatModerators.md.txt

# LiveChatModerators

A **liveChatModerator** resource represents a moderator for a YouTube live chat. A chat moderator has the ability to ban or unban users from a chat, remove messages, and perform other administrative actions for the live chat.

## Methods

The API supports the following methods for `liveChatModerators` resources. All of the requests must be authorized by the owner of the live chat's channel.

[list](https://developers.google.com/youtube/v3/live/docs/liveChatModerators/list)
:   Lists moderators for a live chat.
    [Try it now](https://developers.google.com/youtube/v3/live/docs/liveChatModerators/list#try-it).

[insert](https://developers.google.com/youtube/v3/live/docs/liveChatModerators/insert)
:   Adds a new moderator for the chat.
    [Try it now](https://developers.google.com/youtube/v3/live/docs/liveChatModerators/insert#try-it).

[delete](https://developers.google.com/youtube/v3/live/docs/liveChatModerators/delete)
:   Removes a chat moderator.
    [Try it now](https://developers.google.com/youtube/v3/live/docs/liveChatModerators/delete#try-it).

## Resource representation

The following JSON structure shows the format of a `liveChatModerators` resource:  

```text
{
  "kind": "youtube#liveChatModerator",
  "etag": etag,
  "id": string,
  "snippet": {
    "moderatorDetails": {
      "channelId": string,
      "channelUrl": string,
      "displayName": string,
      "profileImageUrl": string
    },
    "liveChatId": string
  }
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                                                                       Properties                                                                                                                        ||
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kind`                                     | `string` Identifies the API resource's type. The value will be `youtube#liveChatModerator`.                                                                                                                 |
| `etag`                                     | `etag` The Etag of this resource.                                                                                                                                                                           |
| `id`                                       | `string` The ID that YouTube assigns to uniquely identify the moderator.                                                                                                                                    |
| `snippet`                                  | `object` The `snippet` object contains details about the moderator.                                                                                                                                         |
| snippet.`moderatorDetails`                 | `object` This object contains details about the moderator.                                                                                                                                                  |
| snippet.moderatorDetails.`channelId`       | `string` The moderator's YouTube channel ID.                                                                                                                                                                |
| snippet.moderatorDetails.`channelUrl`      | `string` The URL of the moderator's YouTube channel.                                                                                                                                                        |
| snippet.moderatorDetails.`displayName`     | `string` The display name of the moderator's YouTube channel.                                                                                                                                               |
| snippet.moderatorDetails.`profileImageUrl` | `string` The avatar URL of the moderator's YouTube channel.                                                                                                                                                 |
| snippet.`liveChatId`                       | `string` The ID of the live chat that the moderator has privileges to administer. The live chat ID associated with a broadcast is returned in the `liveBroadcast` resource's `snippet.liveChatId` property. |