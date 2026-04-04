# Source: https://developers.google.com/youtube/v3/docs/videoCategories.md.txt

# VideoCategories

A **videoCategory** resource identifies a category that has been or could be associated with uploaded videos.

## Methods

The API supports the following methods for `videoCategories` resources:

[list](https://developers.google.com/youtube/v3/docs/videoCategories/list)
:   Returns a list of categories that can be associated with YouTube videos.
    [Try it now](https://developers.google.com/youtube/v3/docs/videoCategories/list#usage).

## Resource representation

The following JSON structure shows the format of a `videoCategories` resource:  

```verilog
{
  "https://developers.google.com/youtube/v3/docs/videoCategories#kind": "youtube#videoCategory",
  "https://developers.google.com/youtube/v3/docs/videoCategories#etag": etag,
  "https://developers.google.com/youtube/v3/docs/videoCategories#id": string,
  "https://developers.google.com/youtube/v3/docs/videoCategories#snippet": {
    "https://developers.google.com/youtube/v3/docs/videoCategories#snippet.channelId": "UCBR8-60-B28hp2BmDPdntcQ",
    "https://developers.google.com/youtube/v3/docs/videoCategories#snippet.title": string,
    "https://developers.google.com/youtube/v3/docs/videoCategories#snippet.assignable": boolean
  }
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                        Properties                                                         ||
|----------------------|-----------------------------------------------------------------------------------------------------|
| `kind`               | `string` Identifies the API resource's type. The value will be `youtube#videoCategory`.             |
| `etag`               | `etag` The Etag of this resource.                                                                   |
| `id`                 | `string` The ID that YouTube uses to uniquely identify the video category.                          |
| `snippet`            | `object` The `snippet` object contains basic details about the video category, including its title. |
| snippet.`channelId`  | `string` The YouTube channel that created the video category.                                       |
| snippet.`title`      | `string` The video category's title.                                                                |
| snippet.`assignable` | `boolean` Indicates whether videos can be associated with the category.                             |