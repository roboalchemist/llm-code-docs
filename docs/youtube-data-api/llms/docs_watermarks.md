# Source: https://developers.google.com/youtube/v3/docs/watermarks.md.txt

# Watermarks

A **watermark** resource identifies an image that displays during playbacks of a specified channel's videos. You can also specify a target channel to which the image will link as well as timing details that determine when the watermark appears during video playbacks and the length of time it is visible.

## Methods

The API supports the following methods for `watermarks` resources:

[set](https://developers.google.com/youtube/v3/docs/watermarks/set)
:   Uploads a watermark image to YouTube and sets it for a channel.

[unset](https://developers.google.com/youtube/v3/docs/watermarks/unset)
:   Deletes a channel's watermark image.
    [Try it now](https://developers.google.com/youtube/v3/docs/watermarks/unset#try-it).

## Resource representation

The JSON structure below shows the format of a `watermarks` resource:  

```carbon
{
  "https://developers.google.com/youtube/v3/docs/watermarks#timing": {
    "https://developers.google.com/youtube/v3/docs/watermarks#timing.type": string,
    "https://developers.google.com/youtube/v3/docs/watermarks#timing.offsetMs": unsigned long,
    "https://developers.google.com/youtube/v3/docs/watermarks#timing.durationMs": unsigned long
  },
  "https://developers.google.com/youtube/v3/docs/watermarks#position": {
    "https://developers.google.com/youtube/v3/docs/watermarks#position.type": string,
    "https://developers.google.com/youtube/v3/docs/watermarks#position.cornerPosition": string
  },
  "https://developers.google.com/youtube/v3/docs/watermarks#imageUrl": string,
  "https://developers.google.com/youtube/v3/docs/watermarks#imageBytes": bytes,
  "https://developers.google.com/youtube/v3/docs/watermarks#targetChannelId": string
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                                                                                                                            Properties                                                                                                                                                                            ||
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `timing`                  | `object` The `timing` object encapsulates information about the time during a video playback when a channel's watermark image will display.                                                                                                                                                                                           |
| timing.`type`             | `string` The timing method that determines when the watermark image is displayed during the video playback. If the value is `offsetFromStart`, then the `offsetMs` field represents an offset from the start of the video. If the value is `offsetFromEnd`, then the `offsetMs` field represents an offset from the end of the video. |
| timing.`offsetMs`         | `unsigned long` The time offset, specified in milliseconds, that determines when the promoted item appears during video playbacks. The `type` property's value determines whether the offset is measured from the start or end of the video.                                                                                          |
| timing.`durationMs`       | `unsigned long` The length of time, in milliseconds, that the watermark image should display.                                                                                                                                                                                                                                         |
| `position`                | `object` The `position` object encapsulates information about the spatial position within the video where the watermark image will display.                                                                                                                                                                                           |
| position.`type`           | `string` The manner in which the promoted item is positioned in the video player. Valid values for this property are: - corner                                                                                                                                                                                                        |
| position.`cornerPosition` | `string` The corner of the player where the promoted item will appear. The item always appears in the upper right corner of the player. Valid values for this property are: - `topRight`                                                                                                                                              |
| `imageUrl`                | `string` The URL for the channel's watermark image. YouTube will generate this URL and return it in the API response to a `watermark.set` request.                                                                                                                                                                                    |
| `imageBytes`              | `bytes` The size of the watermark image, in bytes.                                                                                                                                                                                                                                                                                    |
| `targetChannelId`         | `string` The YouTube channel ID of the channel that the watermark image links to.                                                                                                                                                                                                                                                     |