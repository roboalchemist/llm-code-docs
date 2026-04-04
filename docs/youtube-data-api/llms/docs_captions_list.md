# Source: https://developers.google.com/youtube/v3/docs/captions/list.md.txt

# Captions: list

Returns a list of caption tracks that are associated with a specified video. Note that the API response does not contain the actual captions and that the [captions.download](https://developers.google.com/youtube/v3/docs/captions/download) method provides the ability to retrieve a caption track.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/captions/list#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
GET https://www.googleapis.com/youtube/v3/captions
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/guides/authentication)).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube.force-ssl` |
| `https://www.googleapis.com/auth/youtubepartner`    |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                                                                                                                                                                                                                                                    Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                    ||
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |||
| `part`                   | `string` The **part** parameter specifies the `caption` resource parts that the API response will include. The list below contains the `part` names that you can include in the parameter value: - `id` - `snippet`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `videoId`                | `string` The **videoId** parameter specifies the YouTube video ID of the video for which the API should return caption tracks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |||
| `id`                     | `string` The **id** parameter specifies a comma-separated list of IDs that identify the `caption` resources that should be retrieved. Each ID must identify a caption track associated with the specified video.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `onBehalfOfContentOwner` | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwner** parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner. |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a response body with the following structure:  

```objective-c
{
  "kind": "youtube#captionListResponse",
  "etag": etag,
  "items": [
    caption Resource
  ]
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                Properties                                                ||
|-----------|-----------------------------------------------------------------------------------------------|
| `kind`    | `string` Identifies the API resource's type. The value will be `youtube#captionListResponse`. |
| `etag`    | `etag` The Etag of this resource.                                                             |
| `items[]` | `list` A list of captions that match the request criteria.                                    |

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|    Error type     |   Error detail    |                                                                                                                                                                                Description                                                                                                                                                                                 |
|-------------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `forbidden (403)` | `forbidden`       | One or more caption tracks could not be retrieved because the permissions associated with the request are not sufficient to retrieve the requested resources. The request might not be properly authorized.                                                                                                                                                                |
| `notFound (404)`  | `captionNotFound` | One or more of the specified caption tracks could not be found. This error occurs if the `videoId` parameter identifies an actual video, but the `id` parameter either identifies caption track IDs that do not exist or track IDs that are associated with other videos. Check the values of the request's `id` and `videoId` parameters to ensure that they are correct. |
| `notFound (404)`  | `videoNotFound`   | The video identified by the `videoId` parameter could not be found.                                                                                                                                                                                                                                                                                                        |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.