# Source: https://developers.google.com/youtube/v3/docs/videos/reportAbuse.md.txt

# Videos: reportAbuse

Reports a video for containing abusive content.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Request

### HTTP request

```
POST https://www.googleapis.com/youtube/v3/videos/reportAbuse
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/guides/authentication)).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |
| `https://www.googleapis.com/auth/youtubepartner`    |

### Parameters

The table below lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                                                                                                                                                                                                                                                Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                 ||
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |||
| `onBehalfOfContentOwner` | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwner** parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner. |

### Request body

The request body has the following data structure:  

```text
{
  "videoId": string,
  "reasonId": string,
  "secondaryReasonId": string,
  "comments": string,
  "language": string
}
```

#### Required properties

You must set values for the following properties:

<br />

- [videoId](https://developers.google.com/youtube/v3/docs/videos/reportAbuse#videoId)
- [reasonId](https://developers.google.com/youtube/v3/docs/videos/reportAbuse#reasonId)

<br />

#### Optional properties

You can set values for the following properties:

<br />

- [secondaryReasonId](https://developers.google.com/youtube/v3/docs/videos/reportAbuse#secondaryReasonId)
- [comments](https://developers.google.com/youtube/v3/docs/videos/reportAbuse#comments)
- [language](https://developers.google.com/youtube/v3/docs/videos/reportAbuse#language)

<br />

### Properties

The following table defines the properties that appear in this resource:

|                                                                                                                                                                                                                            Properties                                                                                                                                                                                                                            ||
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `videoId`           | `string` Identifies the video that is being reported for containing abusive content. Set the value to that video's YouTube video ID.                                                                                                                                                                                                                                                                                                        |
| `reasonId`          | `object` Specifies the reason that the video that is being reported for containing abusive content. Set the value to the appropriate `videoAbuseReportReason` resource's [unique ID](https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons#id).                                                                                                                                                                             |
| `secondaryReasonId` | `object` Specifies the secondary reason that the video that is being reported for containing abusive content. A secondary reason provides a more specific description of the objectionable content than the primary reason, which the `reasonId` property identifies. Set the value to the appropriate secondary reason's [unique ID](https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons#snippet.secondaryReasons[].id). |
| `comments`          | `string` Provides any additional information that the reporter wants to add.                                                                                                                                                                                                                                                                                                                                                                |
| `language`          | `object` Identifies a language spoken by the reporter.                                                                                                                                                                                                                                                                                                                                                                                      |

## Response

If successful, this method returns an HTTP `204` response code (`No Content`).

## Errors

The table below identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|     Error type     |     Error detail     |                                                                      Description                                                                       |
|--------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)` | `invalidAbuseReason` | The request contained an unexpected value for the `reasonId` property, or an invalid combination of the `reasonId` and `secondaryReasonId` properties. |
| `badRequest (400)` | `rateLimitExceeded`  | The user has sent too many requests in a given timeframe.                                                                                              |
| `forbidden (403)`  | `forbidden`          |                                                                                                                                                        |
| `notFound (404)`   | `videoNotFound`      | The video that you are trying to report abuse for cannot be found.                                                                                     |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.