# Source: https://developers.google.com/youtube/v3/docs/guideCategories.md.txt

# GuideCategories

**Note:** This is a deprecation announcement.  

The `guideCategories` resource and the `guideCategories.list` method have both been deprecated as of September 9, 2020.
A **guideCategory** resource identifies a category that YouTube algorithmically assigns based on a channel's content or other indicators, such as the channel's popularity. The list is similar to [video categories](https://developers.google.com/youtube/v3/docs/videoCategories), with the difference being that a video's uploader can assign a video category but only YouTube can assign a channel category.

## Methods

The API supports the following methods for `guideCategories` resources:

[list](https://developers.google.com/youtube/v3/docs/guideCategories/list)
:   Returns a list of categories that can be associated with YouTube channels.
    [Try it now](https://developers.google.com/youtube/v3/docs/guideCategories/list#try-it).

## Resource representation

The JSON structure below shows the format of a `guideCategories` resource:  

```text
{
  "kind": "youtube#guideCategory",
  "etag": etag,
  "id": string,
  "snippet": {
    "channelId": "UCBR8-60-B28hp2BmDPdntcQ",
    "title": string
  }
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                       Properties                                                       ||
|---------------------|---------------------------------------------------------------------------------------------------|
| `kind`              | `string` Identifies the API resource's type. The value will be `youtube#guideCategory`.           |
| `etag`              | `etag` The Etag of this resource.                                                                 |
| `id`                | `string` The ID that YouTube uses to uniquely identify the guide category.                        |
| `snippet`           | `object` The `snippet` object contains basic details about the category, such as its title.       |
| snippet.`channelId` | `string` The ID that YouTube uses to uniquely identify the channel publishing the guide category. |
| snippet.`title`     | `string` The category's title.                                                                    |