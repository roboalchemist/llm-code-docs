# Source: https://developers.google.com/youtube/v3/docs/channelSections.md.txt

# ChannelSections

A **channelSection** resource contains information about a set of
videos that a channel has chosen to feature. For example, a section could feature a channel's
latest uploads, most popular uploads, or videos from one or more playlists.  


A channel can create a maximum of 10 shelves.

## Methods

The API supports the following methods for `channelSections` resources:

[list](https://developers.google.com/youtube/v3/docs/channelSections/list)
:   Returns a list of `channelSection` resources that match the API request criteria.
    [Try it now](https://developers.google.com/youtube/v3/docs/channelSections/list#usage).

[insert](https://developers.google.com/youtube/v3/docs/channelSections/insert)
:   Adds a channel section to the authenticated user's channel. A channel can create a maximum of 10 shelves.
    [Try it now](https://developers.google.com/youtube/v3/docs/channelSections/insert#usage).

[update](https://developers.google.com/youtube/v3/docs/channelSections/update)
:   Updates a channel section.
    [Try it now](https://developers.google.com/youtube/v3/docs/channelSections/update#usage).

[delete](https://developers.google.com/youtube/v3/docs/channelSections/delete)
:   Deletes a channel section.
    [Try it now](https://developers.google.com/youtube/v3/docs/channelSections/delete#usage).

## Resource representation

The following JSON structure shows the format of a `channelSections` resource:  

```carbon
{
  "https://developers.google.com/youtube/v3/docs/channelSections#kind": "youtube#channelSection",
  "https://developers.google.com/youtube/v3/docs/channelSections#etag": etag,
  "https://developers.google.com/youtube/v3/docs/channelSections#id": string,
  "https://developers.google.com/youtube/v3/docs/channelSections#snippet": {
    "https://developers.google.com/youtube/v3/docs/channelSections#snippet.type": string,
    "https://developers.google.com/youtube/v3/docs/channelSections#snippet.channelId": string,
    "https://developers.google.com/youtube/v3/docs/channelSections#snippet.title": string,
    "https://developers.google.com/youtube/v3/docs/channelSections#snippet.position": unsigned integer
  },
  "https://developers.google.com/youtube/v3/docs/channelSections#contentDetails": {
    "https://developers.google.com/youtube/v3/docs/channelSections#contentDetails.playlists[]": [
      string
    ],
    "https://developers.google.com/youtube/v3/docs/channelSections#contentDetails.channels[]": [
      string
    ]
  }
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                                                                                                                                                                                                           Properties                                                                                                                                                                                                                                                           ||
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kind`                       | `string` Identifies the API resource's type. The value will be `youtube#channelSection`.                                                                                                                                                                                                                                                                                                                                                                                                         |
| `etag`                       | `etag` The Etag of this resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `id`                         | `string` The ID that YouTube uses to uniquely identify the channel section.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `snippet`                    | `object` The `snippet` object contains basic details about the channel section, such as its type and title.                                                                                                                                                                                                                                                                                                                                                                                      |
| snippet.`type`               | `string` The channel section's type. Valid values for this property are: - `allPlaylists` - `completedEvents` - `liveEvents` - `multipleChannels` - `multiplePlaylists` - `popularUploads` - `recentUploads` - `singlePlaylist` - `subscriptions` - `upcomingEvents`                                                                                                                                                                                                                             |
| snippet.`channelId`          | `string` The ID that YouTube uses to uniquely identify the channel that published the channel section.                                                                                                                                                                                                                                                                                                                                                                                           |
| snippet.`title`              | `string` The section's title. You can only set the title of a channel section that has a `snippet.type` value of either `multiplePlaylists` or `multipleChannels`, and, in fact, you must specify a title when inserting or updating either of those types of sections. If you specify a title for other types of channel sections, the value will be ignored. This property's value has a maximum length of 100 characters and may contain all valid UTF-8 characters except **\<** and **\>**. |
| snippet.`position`           | `unsigned integer` The section's position on the channel page. This property uses a 0-based index. A value of `0` identifies the first section that appears on the channel, a value of `1` identifies the second section, and so forth. If you do not specify a value for this property when inserting a channel section, the default behavior is to display the new section last.                                                                                                               |
| `contentDetails`             | `object` The `contentDetails` object contains details about the channel section's content, such as a list of playlists or channels featured in the section.                                                                                                                                                                                                                                                                                                                                      |
| contentDetails.`playlists[]` | `list` A list of one or more playlist IDs that are featured in a channel section. You must specify a list of playlist IDs if the `channelSection` resource's `snippet.type` property is either `singlePlaylist` or `multiplePlaylists`, and this property should not be specified for other types of sections. If the type is `singlePlaylist`, this list must specify exactly one playlist ID.                                                                                                  |
| contentDetails.`channels[]`  | `list` A list of one or more channel IDs that are featured in a channel section. You must specify a list of channel IDs if the `channelSection` resource's `snippet.type` property is `multipleChannels`, and this property should not be specified for other types of sections. You cannot include your own channel in the list.                                                                                                                                                                |