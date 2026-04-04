# Source: https://developers.google.com/youtube/v3/docs/playlists/insert.md.txt

# Playlists: insert

Creates a playlist.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/playlists/insert#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
POST https://www.googleapis.com/youtube/v3/playlists
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

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ||
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |||
| `part`                          | `string` The **part** parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include. The following list contains the `part` names that you can include in the parameter value: - `contentDetails` - `id` - `localizations` - `player` - `snippet` - `status`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |||
| `onBehalfOfContentOwner`        | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwner** parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.                                                                                                                                                                                                                                                                                                                                                          |
| `onBehalfOfContentOwnerChannel` | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwnerChannel** parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the `onBehalfOfContentOwner` parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the `onBehalfOfContentOwner` parameter specifies. Finally, the channel that the `onBehalfOfContentOwnerChannel` parameter value specifies must be linked to the content owner that the `onBehalfOfContentOwner` parameter specifies. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel. |

### Request body

Provide a [playlist](https://developers.google.com/youtube/v3/docs/playlists#resource) resource in the request body.
For that resource:

- You must specify a value for these properties:

  - `snippet.title`
- You can set values for these properties:

  - `snippet.title`
  - `snippet.description`
  - `status.privacyStatus`
  - `snippet.defaultLanguage`
  - `localizations.(key)`
  - `localizations.(key).title`
  - `localizations.(key).description`

## Response

If successful, this method returns a [playlist](https://developers.google.com/youtube/v3/docs/playlists#resource) resource in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. For more details, see [YouTube Data API - Errors](https://developers.google.com/youtube/v3/docs/errors).

|      Error type      |         Error detail          |                                                                                                                                                                        Description                                                                                                                                                                         |
|----------------------|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)`   | `defaultLanguageNotSetError`  | The `defaultLanguage` must be set to update `localizations`.                                                                                                                                                                                                                                                                                               |
| `badRequest (400)`   | `localizationValidationError` | One of the values in the localizations object failed validation. Use the [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list) method to retrieve valid values and make sure to update them following the guidelines in [the playlists resource documentation.](https://developers.google.com/youtube/v3/docs/playlists#resource) |
| `badRequest (400)`   | `maxPlaylistExceeded`         | The playlist cannot be created because the channel already has the maximum number of playlists allowed.                                                                                                                                                                                                                                                    |
| `forbidden (403)`    | `playlistForbidden`           | This operation is forbidden or the request is not properly authorized.                                                                                                                                                                                                                                                                                     |
| `invalidValue (400)` | `invalidPlaylistSnippet`      | The request provides an invalid playlist snippet.                                                                                                                                                                                                                                                                                                          |
| `required (400)`     | `playlistTitleRequired`       | The request must specify a playlist title.                                                                                                                                                                                                                                                                                                                 |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.