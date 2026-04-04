# Source: https://developers.google.com/youtube/v3/docs/activities/insert.md.txt

# Activities: insert

**YouTube has deprecated the channel bulletin feature, and this method is no longer supported.**   

For more details, please see the [YouTube Help Center](https://support.google.com/youtube?p=channel-bulletins).
Posts a bulletin for a specific channel. (The user submitting the request must be authorized to act on the channel's behalf.)  

**Note:** Even though an `activity` resource can contain information about actions like a user rating a video or marking a video as a favorite, you need to use other API methods to generate those `activity` resources. For example, you would use the API's [videos.rate()](https://developers.google.com/youtube/v3/docs/videos/rate) method to rate a video and the [playlistItems.insert()](https://developers.google.com/youtube/v3/docs/playlistItems/insert) method to mark a video as a favorite.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Request

### HTTP request

```
POST https://www.googleapis.com/youtube/v3/activities
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/guides/authentication)).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                 Parameters                                                                                                                                                                  ||
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                        |||
| `part` | `string` The **part** parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include. The following list contains the `part` names that you can include in the parameter value: - `contentDetails` - `id` - `snippet` |

### Request body

Provide an [activity resource](https://developers.google.com/youtube/v3/docs/activities#resource) in the request body.
For that resource:

- You must specify a value for these properties:

  - `snippet.description`
- You can set values for these properties:

  - `snippet.description`
  - `contentDetails.bulletin.resourceId`

## Response

If successful, this method returns an [activity resource](https://developers.google.com/youtube/v3/docs/activities#resource) in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|          Error type           |      Error detail      |                                                                            Description                                                                             |
|-------------------------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)`            | `bulletinTextRequired` | The request must use the `snippet` object's `description` property to provide the text for the bulletin post.                                                      |
| `badRequest (400)`            | `invalidMetadata`      | The `kind` property does not match the type of ID provided.                                                                                                        |
| `forbidden (403)`             | `forbidden`            | The request is not properly authorized.                                                                                                                            |
| `notFound (404)`              | `playlistNotFound`     | YouTube cannot find the video that you are trying to associate with the bulletin post. Check the value of the `contentDetails.bulletinPosted.playlistId` property. |
| `notFound (404)`              | `videoNotFound`        | YouTube cannot find the video that you are trying to associate with the bulletin post. Check the value of the `contentDetails.bulletinPosted.videoId` property.    |
| `userRateLimitExceeded (403)` | `rateLimitExceeded`    | The request cannot be completed because you have exceeded your [quota](https://developers.google.com/youtube/v3/getting-started#quota).                            |