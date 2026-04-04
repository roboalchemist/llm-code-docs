# Source: https://developers.google.com/youtube/v3/docs/playlistItems/update.md.txt

# PlaylistItems: update

Modifies a playlist item. For example, you could update the item's position in the playlist.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/playlistItems/update#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
PUT https://www.googleapis.com/youtube/v3/playlistItems
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

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ||
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |||
| `part`                   | `string` The **part** parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include. Note that this method will override the existing values for all of the mutable properties that are contained in any parts that the parameter value specifies. For example, a playlist item can specify a start time and end time, which identify the times portion of the video that should play when users watch the video in the playlist. If your request is updating a playlist item that sets these values, and the request's `part` parameter value includes the `contentDetails` part, the playlist item's start and end times will be updated to whatever value the request body specifies. If the request body does not specify values, the existing start and end times will be removed and replaced with the default settings. The following list contains the `part` names that you can include in the parameter value: - `contentDetails` - `id` - `snippet` - `status` |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |||
| `onBehalfOfContentOwner` | `string` **Note:** The **onBehalfOfContentOwner** parameter is intended exclusively for YouTube content partners and can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). This parameter is designed for YouTube content partners that own and manage many different YouTube channels. It enables users affiliated with the content owner to authenticate once and then be able to access and manage all of the content owner's video and channel data, without having to provide authentication credentials for each individual channel. When the parameter is present, its value identifies a content owner, and the request's authorization credentials identify a YouTube user who is authorized to act on behalf of that content owner. The account that the user authenticates with must be [linked to the specified content owner](https://support.google.com/youtube/answer/4524878) in the YouTube Creator Studio settings.                                                                                     |

### Request body

Provide a [playlistItem resource](https://developers.google.com/youtube/v3/docs/playlistItems#resource) in the request body.
For that resource:

- You must specify a value for these properties:

  <br />

  - `id`
  - `snippet.playlistId`
  - `snippet.resourceId`

  <br />

- You can set values for these properties:

  <br />

  - `snippet.position`
  - `contentDetails.note`
  - `contentDetails.startAt`
  - `contentDetails.endAt`

  <br />

  If you are submitting an update request, and your request does not specify a value for a property that already has a value, the property's existing value will be deleted.

## Response

If successful, this method returns a [playlistItem resource](https://developers.google.com/youtube/v3/docs/playlistItems#resource) in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|      Error type      |          Error detail          |                                                                                                                                                                                                                                                                                         Description                                                                                                                                                                                                                                                                                         |
|----------------------|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `forbidden (403)`    | `playlistItemsNotAccessible`   | The request is not properly authorized to update the specified playlist item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `invalidValue (400)` | `invalidPlaylistItemPosition`  | The request attempts to set the playlist item's position to an invalid or unsupported value. Check the value of the `position` property in the resource's `snippet`.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `invalidValue (400)` | `invalidResourceType`          | The `type` specified for the resource ID is not supported for this operation. The resource ID identifies the item being added to the playlist -- e.g. `youtube#video`.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `invalidValue (400)` | `invalidSnippet`               | The request does not specify a valid `snippet` property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `invalidValue (400)` | `manualSortRequired`           | The request attempts to set the playlist item's position, but the playlist does not use manual sorting. (For example, playlist items might be sorted by date or popularity.) You can address the error by removing the `snippet.position` element from the resource that the request is inserting. If you want the playlist item to have a particular position in the list, you need to first update the playlist's **Ordering** option to **Manual** in the playlist's settings. This settings can be adjusted in the [YouTube Video Manager](https://www.youtube.com/view_all_playlists). |
| `notFound (404)`     | `playlistItemNotFound`         | The playlist item identified with the request's `id` property cannot be found.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `notFound (404)`     | `playlistNotFound`             | The playlist identified with the request's `playlistId` parameter cannot be found.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `required (400)`     | `channelIdRequired`            | The request does not specify a value for the required `channelId` property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `required (400)`     | `playlistIdRequired`           | The request does not specify a value for the required `playlistId` property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `required (400)`     | `playlistItemIdRequired`       | The playlist item resource specified in the request must use the `id` property to identify the playlist item that is being updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `invalidValue (400)` | `playlistOperationUnsupported` | The API does not support the ability to update videos in the specified playlist. For example, you can't update a video in your uploaded videos playlist.                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.