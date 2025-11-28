# Source: https://developers.google.com/youtube/v3/docs/thumbnails/set.md.txt

# Thumbnails: set

Uploads a custom video thumbnail to YouTube and sets it for a video.

This method supports media upload. Uploaded files must conform to these constraints:

- **Maximum file size:** 2MB
- **Accepted Media MIME types:** `image/jpeg`, `image/png`, `application/octet-stream`

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of approximately 50 units.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/thumbnails/set#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
POST https://www.googleapis.com/upload/youtube/v3/thumbnails/set
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/guides/authentication)).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtubepartner`    |
| `https://www.googleapis.com/auth/youtube.upload`    |
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                                                                                                                                                                                  Parameters                                                                                                                                                                                                                                                                                                                                                                  ||
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |||
| `videoId`                | `string` The **videoId** parameter specifies a YouTube video ID for which the custom video thumbnail is being provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |||
| `onBehalfOfContentOwner` | `string` **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwner** parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner. |

### Request body

The body of the request contains the thumbnail image that you are uploading. The request body does not contain a [thumbnail](https://developers.google.com/youtube/v3/docs/thumbnails#resource-representation) resource.

## Response

If successful, this method returns a response body with the following structure:  

```objective-c
{
  "kind": "youtube#thumbnailSetResponse",
  "etag": etag,
  "items": [
    thumbnail resource
  ]
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                Properties                                                 ||
|-----------|------------------------------------------------------------------------------------------------|
| `kind`    | `string` Identifies the API resource's type. The value will be `youtube#thumbnailSetResponse`. |
| `etag`    | `etag` The Etag of this resource.                                                              |
| `items[]` | `list` A list of thumbnails.                                                                   |

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|       Error type        |       Error detail        |                                                                            Description                                                                            |
|-------------------------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)`      | `invalidImage`            | The provided image content is invalid.                                                                                                                            |
| `badRequest (400)`      | `mediaBodyRequired`       | The request does not include the image content.                                                                                                                   |
| `forbidden (403)`       | `forbidden`               | The thumbnail can't be set for the specified video. The request might not be properly authorized.                                                                 |
| `forbidden (403)`       | `forbidden`               | The authenticated user doesn't have permissions to upload and set custom video thumbnails.                                                                        |
| `notFound (404)`        | `videoNotFound`           | The video that you are trying to insert a thumbnail image for cannot be found. Check the value of the request's `videoId` parameter to ensure that it is correct. |
| `tooManyRequests (429)` | `uploadRateLimitExceeded` | The channel has uploaded too many thumbnails recently. Please try the request again later.                                                                        |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.