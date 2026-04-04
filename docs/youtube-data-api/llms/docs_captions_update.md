# Source: https://developers.google.com/youtube/v3/docs/captions/update.md.txt

# Captions: update

Updates a caption track. When updating a caption track, you can change the track's [draft status](https://developers.google.com/youtube/v3/docs/captions#snippet.isDraft), upload a new caption file for the track, or both.

This method supports media upload. Uploaded files must conform to these constraints:

- **Maximum file size:** 100MB
- **Accepted Media MIME types:** `text/xml`, `application/octet-stream`, `*/*`

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 450 units.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/captions/update#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
PUT https://www.googleapis.com/upload/youtube/v3/captions
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
| `part`                   | `string` The **part** parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include. Set the property value to `snippet` if you are updating the track's [draft status](https://developers.google.com/youtube/v3/docs/captions#snippet.isDraft). Otherwise, set the property value to `id`. The following list contains the `part` names that you can include in the parameter value: - `id` - `snippet`                                                                                                                                                                                                                                                                                                                                |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |||
| `onBehalfOfContentOwner` | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwner** parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner. |
| `sync`                   | `boolean` This parameter has been deprecated. **Note:** The API server only processes the parameter value if the request contains an updated caption file. The **sync** parameter indicates whether YouTube should automatically synchronize the caption file with the audio track of the video. If you set the value to `true`, YouTube will automatically synchronize the caption track with the audio track.                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### Request body

Provide a [caption resource](https://developers.google.com/youtube/v3/docs/captions#resource) in the request body.
For that resource:

- You must specify a value for these properties:

  <br />

  - `id`

  <br />

- You can set values for these properties:

  <br />

  - `snippet.isDraft`

  <br />

  If you are submitting an update request, and your request does not specify a value for a property that already has a value, the property's existing value will be deleted.

## Response

If successful, this method returns a [caption resource](https://developers.google.com/youtube/v3/docs/captions#resource) in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|     Error type     |   Error detail    |                                                                Description                                                                |
|--------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)` | `contentRequired` | The request did not upload an updated caption file. The actual track contents are required if the `sync` parameter is set to `true`.      |
| `forbidden (403)`  | `forbidden`       | The permissions associated with the request are not sufficient to update the caption track. The request might not be properly authorized. |
| `notFound (404)`   | `captionNotFound` | The specified caption track could not be found. Check the value of the request's `id` property to ensure that it is correct.              |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.