# Source: https://developers.google.com/youtube/v3/docs/captions/download.md.txt

# Captions: download

Downloads a caption track. The caption track is returned in its original format unless the request specifies a value for the `tfmt` parameter and in its original language unless the request specifies a value for the `tlang` parameter.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 200 units.

This method is requires the user to have permission to edit the video.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/captions/download#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
GET https://www.googleapis.com/youtube/v3/captions/id
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/guides/authentication)).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube.force-ssl` |
| `https://www.googleapis.com/auth/youtubepartner`    |

### Parameters

The table below lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                                                                                                                                                                                                                                                    Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                    ||
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |||
| `id`                     | `string` The **id** parameter identifies the caption track that is being retrieved. The value is a caption track ID as identified by the [id](https://developers.google.com/youtube/v3/docs/captions#id) property in a `caption` resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |||
| `onBehalfOfContentOwner` | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwner** parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner. |
| `tfmt`                   | `string` The **tfmt** parameter specifies that the caption track should be returned in a specific format. If the parameter is not included in the request, the track is returned in its original format. Supported values are: - **sbv** -- SubViewer subtitle - **scc** -- Scenarist Closed Caption format - **srt** -- SubRip subtitle - **ttml** -- Timed Text Markup Language caption - **vtt** -- Web Video Text Tracks caption                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `tlang`                  | `string` The **tlang** parameter specifies that the API response should return a translation of the specified caption track. The parameter value is an [ISO 639-1 two-letter language code](http://www.loc.gov/standards/iso639-2/php/code_list.php) that identifies the desired caption language. The translation is generated by using machine translation, such as Google Translate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a binary file. The `Content-Type` header for the response is `application/octet-stream`.

## Errors

The table below identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|      Error type      |   Error detail    |                                                                                                             Description                                                                                                             |
|----------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `forbidden (403)`    | `forbidden`       | The permissions associated with the request are not sufficient to download the caption track. The request might not be properly authorized.                                                                                         |
| `invalidValue (400)` | `couldNotConvert` | The caption track data could not be converted to the requested language and/or format. Ensure that the requested `tfmt` and `tlang` values are valid, and that the `snippet.status` of the requested caption track is not `failed`. |
| `notFound (404)`     | `captionNotFound` | The caption track could not be found. Check the value of the request's `id` parameter to ensure that it is correct.                                                                                                                 |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.