# Source: https://developers.google.com/youtube/v3/docs/playlistImages/delete.md.txt

# PlaylistImages: delete

Deletes a playlist image.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Request

### HTTP request

```
DELETE https://www.googleapis.com/youtube/v3/playlistImages
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

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ||
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |||
| `id`                     | `string` The **id** parameter specifies the YouTube playlist image ID for the playlist image that is being deleted. In a `playlistImages` resource, the `id` property specifies the playlist image's ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |||
| `onBehalfOfContentOwner` | `string` **Note:** The **onBehalfOfContentOwner** parameter is intended exclusively for YouTube content partners and can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). This parameter is designed for YouTube content partners that own and manage many different YouTube channels. It enables users affiliated with the content owner to authenticate once and then be able to access and manage all of the content owner's video and channel data, without having to provide authentication credentials for each individual channel. When the parameter is present, its value identifies a content owner, and the request's authorization credentials identify a YouTube user who is authorized to act on behalf of that content owner. The account that the user authenticates with must be [linked to the specified content owner](https://support.google.com/youtube/answer/4524878) in the YouTube Creator Studio settings. |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns an HTTP `204` response code (`No Content`).