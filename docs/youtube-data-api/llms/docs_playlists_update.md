# Source: https://developers.google.com/youtube/v3/docs/playlists/update.md.txt

# Playlists: update

Modifies a playlist. For example, you could change a playlist's title, description, or privacy status.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/playlists/update#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
PUT https://www.googleapis.com/youtube/v3/playlists
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

|                                                                                                                                                                                                                                                                                                                                                                                                                                Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                 ||
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |||
| `part`                   | `string` The **part** parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include. Note that this method will override the existing values for mutable properties that are contained in any parts that the request body specifies. For example, a playlist's description is contained in the `snippet` part, which must be included in the request body. If the request does not specify a value for the `snippet.description` property, the playlist's existing description will be deleted. The following list contains the `part` names that you can include in the parameter value: - `contentDetails` - `id` - `localizations` - `player` - `snippet` - `status`                                                          |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |||
| `onBehalfOfContentOwner` | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwner** parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner. |

### Request body

Provide a [playlist](https://developers.google.com/youtube/v3/docs/playlists#resource) resource in the request body.
For that resource:

- You must specify a value for these properties:

  - `id`
  - `snippet.title`
- You can set values for these properties:

  - `snippet.title`
  - `snippet.description`
  - `status.privacyStatus`
  - `status.podcastStatus`
  - `snippet.defaultLanguage`
  - `localizations.(key)`
  - `localizations.(key).title`
  - `localizations.(key).description`

  If you are submitting an update request, and your request does not specify a value for a property that already has a value, the property's existing value will be deleted.

## Response

If successful, this method returns a [playlist](https://developers.google.com/youtube/v3/docs/playlists#resource) resource in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. For more details, see [YouTube Data API - Errors](https://developers.google.com/youtube/v3/docs/errors).

|      Error type      |          Error detail          |                                                                                                                                                                        Description                                                                                                                                                                         |
|----------------------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)`   | `defaultLanguageNotSetError`   | The `defaultLanguage` must be set to update `localizations`.                                                                                                                                                                                                                                                                                               |
| `badRequest (400)`   | `localizationValidationError`  | One of the values in the localizations object failed validation. Use the [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list) method to retrieve valid values and make sure to update them following the guidelines in [the playlists resource documentation.](https://developers.google.com/youtube/v3/docs/playlists#resource) |
| `forbidden (403)`    | `playlistForbidden`            | This operation is forbidden or the request is not properly authorized.                                                                                                                                                                                                                                                                                     |
| `invalidValue (400)` | `invalidPlaylistSnippet`       | The request provides an invalid playlist snippet.                                                                                                                                                                                                                                                                                                          |
| `notFound (404)`     | `playlistNotFound`             | The playlist identified with the request's `id` parameter cannot be found.                                                                                                                                                                                                                                                                                 |
| `required (400)`     | `playlistTitleRequired`        | The request must specify a playlist title.                                                                                                                                                                                                                                                                                                                 |
| `invalidValue (400)` | `playlistOperationUnsupported` | The API does not support the ability to update the specified playlist. For example, you can't update the properties of your uploaded videos playlist.                                                                                                                                                                                                      |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.