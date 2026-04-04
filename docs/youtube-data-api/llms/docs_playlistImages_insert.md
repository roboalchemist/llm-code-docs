# Source: https://developers.google.com/youtube/v3/docs/playlistImages/insert.md.txt

# PlaylistImages: insert

Adds an image to a playlist.

This method supports media upload. Uploaded files must conform to these constraints:

- **Maximum file size:** 2MB
- **Accepted aspect ratio:** 1:1 (square)
- **Accepted Media MIME types:** `image/jpeg`, `image/png`

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Request

### HTTP request

```
POST https://www.googleapis.com/youtube/v3/playlistImages
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/guides/authentication)).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtubepartner`    |
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ||
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |||
| `part`                          | `string` The **part** parameter specifies a comma-separated list of one or more `playlistImage` resource properties that the API response will include. If the parameter identifies a property that contains child properties, the child properties will be included in the response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |||
| `onBehalfOfContentOwner`        | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwner** parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.                                                                                                                                                                                                                                                                                                                                                                 |
| `onBehalfOfContentOwnerChannel` | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. <br /> The **onBehalfOfContentOwnerChannel** parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the `onBehalfOfContentOwner` parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the `onBehalfOfContentOwner` parameter specifies. Finally, the channel that the `onBehalfOfContentOwnerChannel` parameter value specifies must be linked to the content owner that the `onBehalfOfContentOwner` parameter specifies. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel. |

### Request body

Provide a [playlistImages resource](https://developers.google.com/youtube/v3/docs/playlistImages#resource) in the request body.

For that resource:

- You must specify a value for these properties:

  - `snippet.playlistId`
  - `snippet.type`
- You can set values for these properties:

  - `snippet.width`
  - `snippet.height`

## Response

If successful, this method returns a [playlistImages resource](https://developers.google.com/youtube/v3/docs/playlistImages#resource) in the response body.