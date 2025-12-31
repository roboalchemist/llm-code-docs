# Source: https://developers.google.com/youtube/v3/docs/membershipsLevels.md.txt

# MembershipsLevels

Note: This endpoint can only be used by individual creators to make requests for their own, channel-memberships-enabled YouTube channel. Reach out to your Google or YouTube representative to request access.

A **membershipsLevel** resource identifies a pricing level managed
by the creator that authorized the API request.

## Methods

The API supports the following methods for `membershipsLevel` resources:

[list](https://developers.google.com/youtube/v3/docs/membershipsLevels/list)
:   Lists membership levels for the channel that authorized the request.

## Resource representation

The following JSON structure shows the format of a `membershipsLevel` resource:  

```text
{
  "kind": "youtube#membershipsLevel",
  "etag": etag,
  "id": string,
  "snippet": {
    "creatorChannelId": string,
    "levelDetails": {
      "displayName": string,
    }
  }
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                                        Properties                                                                                        ||
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kind`                             | `string` Identifies the API resource's type. The value will be `youtube#membershipsLevel`.                                                           |
| `etag`                             | `etag` The Etag of this resource.                                                                                                                    |
| `id`                               | `string` The ID that YouTube assigns to uniquely identify the membership level. This value will not change even if the level's display name changes. |
| `snippet`                          | `object` The `snippet` object contains details about the membership level.                                                                           |
| snippet.`creatorChannelId`         | `string` The YouTube channel ID of the creator that owns the pricing level.                                                                          |
| snippet.`levelDetails`             | `object` This object contains data about the membership level.                                                                                       |
| snippet.levelDetails.`displayName` | `string` The level's display name.                                                                                                                   |