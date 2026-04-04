# Source: https://developers.google.com/youtube/v3/docs/videos/getRating.md.txt

# Videos: getRating

Retrieves the ratings that the authorized user gave to a list of specified videos.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 1 unit.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/videos/getRating#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
GET https://www.googleapis.com/youtube/v3/videos/getRating
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

|                                                                                                                                                                                                                                                                                                                                                                                                                                Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                 ||
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |||
| `id`                     | `string` The **id** parameter specifies a comma-separated list of the YouTube video ID(s) for the resource(s) for which you are retrieving rating data. In a `video` resource, the `id` property specifies the video's ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |||
| `onBehalfOfContentOwner` | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwner** parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner. |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a response body with the following structure:  

```text
{
  "kind": "youtube#videoGetRatingResponse",
  "etag": etag,
  "items": [
    {
      "videoId": string,
      "rating": string
    }
  ]
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                              Properties                                                                              ||
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `kind`            | `string` Identifies the API resource's type. The value will be `youtube#videoGetRatingResponse`.                                                  |
| `etag`            | `etag` The Etag of this resource.                                                                                                                 |
| `items[]`         | `list` A list of ratings that match the request criteria.                                                                                         |
| items[].`videoId` | `string` The ID that YouTube uses to uniquely identify the video.                                                                                 |
| items[].`rating`  | `string` The rating that the authorized user gave to the video. Valid values for this property are: - `dislike` - `like` - `none` - `unspecified` |

## Errors

The API does not define any error messages that are unique to this API method. However, this method could still return general API errors listed in the [error message](https://developers.google.com/youtube/v3/docs/errors#general) documentation.

## Try it!

Use the APIs Explorer to call this API and see the API request and response.