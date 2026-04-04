# Source: https://developers.google.com/youtube/v3/docs/i18nRegions.md.txt

# I18nRegions

An **i18nRegion** resource identifies a geographic area that a YouTube user can select as the preferred content region. The content region can also be referred to as a content locale. For the YouTube website, a content region could be automatically selected based on heuristics like the YouTube domain or the user's IP location. A user could also manually select the desired content region from the YouTube site footer.  

Each `i18nRegion` resource identifies a region code and a name. The region code can be used as the value of the `regionCode` parameter when calling API methods like `search.list`, `videos.list`, `activities.list`, and `videoCategories.list`.

## Methods

The API supports the following methods for `i18nRegions` resources:

[list](https://developers.google.com/youtube/v3/docs/i18nRegions/list)
:   Returns a list of content regions that the YouTube website supports.
    [Try it now](https://developers.google.com/youtube/v3/docs/i18nRegions/list#usage).

## Resource representation

The following JSON structure shows the format of a `i18nRegions` resource:  

```text
{
  "kind": "youtube#i18nRegion",
  "etag": etag,
  "id": string,
  "snippet": {
    "gl": string,
    "name": string
  }
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                          Properties                                                           ||
|----------------|---------------------------------------------------------------------------------------------------------------|
| `kind`         | `string` Identifies the API resource's type. The value will be `youtube#i18nRegion`.                          |
| `etag`         | `etag` The Etag of this resource.                                                                             |
| `id`           | `string` The ID that YouTube uses to uniquely identify the i18n region.                                       |
| `snippet`      | `object` The `snippet` object contains basic details about the i18n region, such as its region code and name. |
| snippet.`gl`   | `string` The two-letter ISO country code that identifies the region.                                          |
| snippet.`name` | `string` The name of the region.                                                                              |