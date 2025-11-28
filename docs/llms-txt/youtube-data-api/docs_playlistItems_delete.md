# Source: https://developers.google.com/youtube/v3/docs/playlistItems/delete.md.txt

# PlaylistItems: delete

Deletes a playlist item.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/playlistItems/delete#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
DELETE https://www.googleapis.com/youtube/v3/playlistItems
```

### Authorization

This request requires authorization with at least one of the following scopes. To read more about authentication and authorization, see [Implementing OAuth 2.0 authorization](https://developers.google.com/youtube/v3/guides/authentication).

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
| `id`                     | `string` The **id** parameter specifies the YouTube playlist item ID for the playlist item that is being deleted. In a `playlistItem` resource, the `id` property specifies the playlist item's ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |||
| `onBehalfOfContentOwner` | `string` **Note:** The **onBehalfOfContentOwner** parameter is intended exclusively for YouTube content partners and can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). This parameter is designed for YouTube content partners that own and manage many different YouTube channels. It enables users affiliated with the content owner to authenticate once and then be able to access and manage all of the content owner's video and channel data, without having to provide authentication credentials for each individual channel. When the parameter is present, its value identifies a content owner, and the request's authorization credentials identify a YouTube user who is authorized to act on behalf of that content owner. The account that the user authenticates with must be [linked to the specified content owner](https://support.google.com/youtube/answer/4524878) in the YouTube Creator Studio settings. |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns an HTTP `204 No Content` status code.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. For more details, see [YouTube Data API - Errors](https://developers.google.com/youtube/v3/docs/errors).

|      Error type      |          Error detail          |                                                                         Description                                                                          |
|----------------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `forbidden (403)`    | `playlistItemsNotAccessible`   | The request is not properly authorized to delete the specified playlist item.                                                                                |
| `notFound (404)`     | `playlistItemNotFound`         | The playlist item identified with the request's `id` parameter cannot be found.                                                                              |
| `invalidValue (400)` | `playlistOperationUnsupported` | The API does not support the ability to delete videos from the specified playlist. For example, you can't delete a video from your uploaded videos playlist. |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.