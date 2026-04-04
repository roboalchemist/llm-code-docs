# Source: https://developers.google.com/youtube/v3/docs/channelBanners.md.txt

# ChannelBanners

A `channelBanner` resource contains the URL that you would use to set a newly uploaded image as the banner image for a channel.

## Methods

The API supports the following methods for `channelBanners` resources:

[insert](https://developers.google.com/youtube/v3/docs/channelBanners/insert)
:   Uploads a channel banner image to YouTube. This method represents the first two steps in a three-step process to update the banner image for a channel:

    1. Call the [channelBanners.insert](https://developers.google.com/youtube/v3/docs/channelBanners/insert) method to upload the binary image data to YouTube. The image must have a 16:9 aspect ratio and be at least 2048x1152 pixels. We recommend uploading a 2560px by 1440px image.
    2. Extract the `url` property's value from the response that the API returns for step 1.
    3. Call the [channels.update](https://developers.google.com/youtube/v3/docs/channels/update) method to update the channel's branding settings. Set the [brandingSettings.image.bannerExternalUrl](https://developers.google.com/youtube/v3/docs/channels#brandingSettings.image.bannerExternalUrl) property's value to the URL obtained in step 2.

## Resource representation

The following JSON structure shows the format of a `channelBanners` resource:  

```text
{
  "kind": "youtube#channelBannerResource",
  "etag": etag,
  "url": string
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                                                                                                                                                                                                                    Properties                                                                                                                                                                                                                                                                    ||
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kind` | `string` Identifies the API resource's type. The value will be `youtube#channelBannerResource`.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `etag` | `etag` The Etag of this resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `url`  | `string` The banner image's URL. After calling the [channelBanners.insert](https://developers.google.com/youtube/v3/docs/channelBanners/insert) method, extract this value from the API response. Then call the [channels.update](https://developers.google.com/youtube/v3/docs/channels/update) method, and set the URL as the value of the [brandingSettings.image.bannerExternalUrl](https://developers.google.com/youtube/v3/docs/channels#brandingSettings.image.bannerExternalUrl) property to set the banner image for a channel. |