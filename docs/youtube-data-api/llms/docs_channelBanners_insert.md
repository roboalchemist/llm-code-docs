# Source: https://developers.google.com/youtube/v3/docs/channelBanners/insert.md.txt

# ChannelBanners: insert

Uploads a channel banner image to YouTube. This method represents the first two steps in a three-step process to update the banner image for a channel:

<br />

1. Call the `channelBanners.insert` method to upload the binary image data to YouTube. The image must have a 16:9 aspect ratio and be at least 2048x1152 pixels. We recommend uploading a 2560px by 1440px image.
2. Extract the `url` property's value from the response that the API returns for step 1.
3. Call the [channels.update](https://developers.google.com/youtube/v3/docs/channels/update) method to update the channel's branding settings. Set the [brandingSettings.image.bannerExternalUrl](https://developers.google.com/youtube/v3/docs/channels#brandingSettings.image.bannerExternalUrl) property's value to the URL obtained in step 2.

<br />

This method supports media upload. Uploaded files must conform to these constraints:

- **Maximum file size:** 6MB
- **Accepted Media MIME types:** `image/jpeg`, `image/png`, `application/octet-stream`

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Request

### HTTP request

```
POST https://www.googleapis.com/upload/youtube/v3/channelBanners/insert
```

### Authorization

This request requires authorization with at least one of the following scopes. To read more about authentication and authorization, see [Implementing OAuth 2.0 authorization](https://developers.google.com/youtube/v3/guides/authentication).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube.upload`    |
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                                                                                                                                                                                                                                                Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                 ||
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |||
| `onBehalfOfContentOwner` | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwner** parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner. |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a [channelBanner](https://developers.google.com/youtube/v3/docs/channelBanners#resource) resource in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. For more details, see [YouTube Data API - Errors](https://developers.google.com/youtube/v3/docs/errors).

|     Error type     |    Error detail     |                                                                                        Description                                                                                         |
|--------------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)` | `bannerAlbumFull`   | Your YouTube Channel Art album has too many images. To fix this, go to [Google Photos](http://photos.google.com), then navigate to the albums page and remove some images from that album. |
| `badRequest (400)` | `mediaBodyRequired` | The request does not include the image content.                                                                                                                                            |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.