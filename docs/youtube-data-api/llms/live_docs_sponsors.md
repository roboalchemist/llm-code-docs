# Source: https://developers.google.com/youtube/v3/live/docs/sponsors.md.txt

# Sponsors

Note: This resource is deprecated as of March 31, 2020. It has been replaced by the [member](https://developers.google.com/youtube/v3/docs/members) resource. You can find information about that resource in the YouTube Data API documentation.  

As part of this deprecation, the `sponsors.list` method will no longer be supported on or after September 30, 2020. API clients should update calls to the `sponsors.list` method to use the [members.list](https://developers.google.com/youtube/v3/docs/members/list) method instead.

A **sponsor** resource represents a channel member (formerly known as a "sponsor") for a YouTube channel.
A member provides recurring monetary support to a creator and receives
special benefits. For example, members are able to chat when the creator turns on members-only mode for a chat.

## Methods

The API supports the following methods for `sponsors` resources:

[list](https://developers.google.com/youtube/v3/live/docs/sponsors/list)
:   Lists sponsors for a channel. The API request must be authorized by the channel owner.
    [Try it now](https://developers.google.com/youtube/v3/live/docs/sponsors/list#try-it).

## Resource representation

The following JSON structure shows the format of a `sponsors` resource:  

```text
{
  "kind": "youtube#sponsor",
  "etag": etag,
  "id": string,
  "snippet": {
    "channelId": string,
    "sponsorDetails": {
      "channelId": string,
      "channelUrl": string,
      "displayName": string,
      "profileImageUrl": string
    },
    "sponsorSince": datetime
  }
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                                                     Properties                                                                                                      ||
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kind`                                   | `string` Identifies the API resource's type. The value will be `youtube#sponsor`.                                                                                         |
| `etag`                                   | `etag` The Etag of this resource.                                                                                                                                         |
| `id`                                     | `string` The ID that YouTube assigns to uniquely identify the sponsor.                                                                                                    |
| `snippet`                                | `object` The `snippet` object contains details about the sponsor.                                                                                                         |
| snippet.`channelId`                      | `string` This ID identifies the channel being sponsored.                                                                                                                  |
| snippet.`sponsorDetails`                 | `object` This object contains details about the sponsor.                                                                                                                  |
| snippet.sponsorDetails.`channelId`       | `string` The YouTube channel ID.                                                                                                                                          |
| snippet.sponsorDetails.`channelUrl`      | `string` The channel's URL.                                                                                                                                               |
| snippet.sponsorDetails.`displayName`     | `string` The channel's display name.                                                                                                                                      |
| snippet.sponsorDetails.`profileImageUrl` | `string` The channels's avatar URL.                                                                                                                                       |
| snippet.`sponsorSince`                   | `datetime` The date and time when the user became a sponsor. The value is specified in [ISO 8601](https://www.w3.org/TR/NOTE-datetime) (`YYYY-MM-DDThh:mm:ss.sZ`) format. |