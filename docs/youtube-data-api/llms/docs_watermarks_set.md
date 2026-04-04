# Source: https://developers.google.com/youtube/v3/docs/watermarks/set.md.txt

# Watermarks: set

Uploads a watermark image to YouTube and sets it for a channel.

This method supports media upload. Uploaded files must conform to these constraints:

- **Maximum file size:** 10MB
- **Accepted Media MIME types:** `image/jpeg`, `image/png`, `application/octet-stream`

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Request

### HTTP request

```
POST https://www.googleapis.com/upload/youtube/v3/watermarks/set
```

### Authorization

This request requires authorization with at least one of the following scopes. To read more about authentication and authorization, see [Implementing OAuth 2.0 authorization](https://developers.google.com/youtube/v3/guides/authentication).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtubepartner`    |
| `https://www.googleapis.com/auth/youtube.upload`    |
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                                                                                                                                                                              Parameters                                                                                                                                                                                                                                                                                                                                                               ||
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |||
| `channelId`              | `string` The **channelId** parameter specifies the YouTube channel ID for which the watermark is being provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |||
| `onBehalfOfContentOwner` | `string` **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwner** parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner. |

### Request body

Provide a [watermark](https://developers.google.com/youtube/v3/docs/watermarks#resource) resource in the request body.

## Response

If successful, this method returns an HTTP `204 No Content` status code.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. For more details, see [YouTube Data API - Errors](https://developers.google.com/youtube/v3/docs/errors).

|     Error type     |       Error detail       |                                                                        Description                                                                         |
|--------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)` | `imageFormatUnsupported` | The image you provided is in an unsupported format.                                                                                                        |
| `badRequest (400)` | `imageTooTall`           | The image you provided is too tall.                                                                                                                        |
| `badRequest (400)` | `imageTooWide`           | The image you provided is too wide.                                                                                                                        |
| `badRequest (400)` | `mediaBodyRequired`      | The request does not include the image content.                                                                                                            |
| `forbidden (403)`  | `forbidden`              | The watermark can't be set for the specified channel. The request may not be properly authorized, or the `channelId` parameter is set to an invalid value. |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.