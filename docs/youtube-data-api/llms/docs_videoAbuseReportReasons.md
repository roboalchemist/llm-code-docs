# Source: https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons.md.txt

# VideoAbuseReportReasons

A **videoAbuseReportReason** resource contains information about a reason that a video would be flagged for containing abusive content. When your application calls the [videos.reportAbuse](https://developers.google.com/youtube/v3/docs/videos/reportAbuse) method to report an abusive video, the request uses the information from a `videoAbuseReportReason` resource to identify the reason that the video is being reported.

## Methods

The API supports the following methods for `videoAbuseReportReasons` resources:

[list](https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons/list)
:   Retrieve a list of reasons that can be used to report abusive videos.
    [Try it now](https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons/list#usage).

## Resource representation

The following JSON structure shows the format of a `videoAbuseReportReason` resource:  

```text
{
  "kind": "youtube#videoAbuseReportReason",
  "etag": etag,
  "id": string,
  "snippet": {
    "label": string,
    "secondaryReasons": [
      {
        "id": string,
        "label": string
      }
    ]
  }
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                                                                                                        Properties                                                                                                                                                         ||
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kind`                             | `string` Identifies the API resource's type. The value will be `youtube#videoAbuseReportReason`.                                                                                                                                                                                      |
| `etag`                             | `etag` The Etag of this resource.                                                                                                                                                                                                                                                     |
| `id`                               | `string` The ID that YouTube uses to identify the reason. When calling the `videos.reportAbuse` method, your application should use this value to set the [reasonId](https://developers.google.com/youtube/v3/docs/videos/reportAbuse#reasonId) property.                             |
| `snippet`                          | `object` The `snippet` object contains basic details about the reason.                                                                                                                                                                                                                |
| snippet.`label`                    | `string` The localized label text for the abuse report reason.                                                                                                                                                                                                                        |
| snippet.`secondaryReasons[]`       | `list` A list of secondary reasons associated with the reason, if any are available. (There might be 0 or more.)                                                                                                                                                                      |
| snippet.secondaryReasons[].`id`    | `string` The ID that YouTube uses to identify the secondary reason. When calling the `videos.reportAbuse` method, your application should use this value to set the [secondaryReasonId](https://developers.google.com/youtube/v3/docs/videos/reportAbuse#secondaryReasonId) property. |
| snippet.secondaryReasons[].`label` | `string` The localized label text for the secondary reason.                                                                                                                                                                                                                           |