# Source: https://developers.google.com/youtube/v3/docs/videos/rate.md.txt

# Videos: rate

Add a like or dislike rating to a video or remove a rating from a video.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

**NOTE:** This does not affect the official like/dislike count of the video.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/videos/rate#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
POST https://www.googleapis.com/youtube/v3/videos/rate
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

|                                                                                                                                                      Parameters                                                                                                                                                      ||
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                 |||
| `id`     | `string` The **id** parameter specifies the YouTube video ID of the video that is being rated or having its rating removed.                                                                                                                                                                                |
| `rating` | `string` Specifies the rating to record. Acceptable values are: - **dislike** -- Records that the authenticated user disliked the video. - **like** -- Records that the authenticated user liked the video. - **none** -- Removes any rating that the authenticated user had previously set for the video. |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns an HTTP `204` response code (`No Content`).

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|     Error type     |      Error detail       |                                                             Description                                                              |
|--------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)` | `emailNotVerified`      | The user must verify their e-mail address prior to rating.                                                                           |
| `badRequest (400)` | `invalidRating`         | The request contained an unexpected value for the `rating` parameter.                                                                |
| `badRequest (400)` | `videoPurchaseRequired` | Rental videos can only be rated by users who rented them.                                                                            |
| `forbidden (403)`  | `forbidden`             | The video that you are trying to rate cannot be rated. The request might not be properly authorized.                                 |
| `forbidden (403)`  | `videoRatingDisabled`   | The owner of the video that you are trying to rate has disabled ratings for that video.                                              |
| `notFound (404)`   | `videoNotFound`         | The video that you are trying to rate cannot be found. Check the value of the request's `id` parameter to ensure that it is correct. |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.