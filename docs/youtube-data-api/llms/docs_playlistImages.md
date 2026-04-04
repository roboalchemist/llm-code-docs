# Source: https://developers.google.com/youtube/v3/docs/playlistImages.md.txt

# PlaylistImages

A **playlistImage** resource identifies
the thumbnail image associated with a playlist.

## Methods

The API supports the following methods for `playlistImages` resources:

[list](https://developers.google.com/youtube/v3/docs/playlistImages/list)
:   Returns a collection of playlist images that match the API request parameters.
    [Try it now](https://developers.google.com/youtube/v3/docs/playlistImages/list#usage).

[insert](https://developers.google.com/youtube/v3/docs/playlistImages/insert)
:   Adds a thumbail image to a playlist.
    [Try it now](https://developers.google.com/youtube/v3/docs/playlistImages/insert#usage).

[update](https://developers.google.com/youtube/v3/docs/playlistImages/update)
:   Updates the thumbnail image for an existing playlist.
    [Try it now](https://developers.google.com/youtube/v3/docs/playlistImages/update#usage).

[delete](https://developers.google.com/youtube/v3/docs/playlistImages/delete)
:   Deletes a playlist thumbnail image.
    [Try it now](https://developers.google.com/youtube/v3/docs/playlistImages/delete#usage).

## Resource representation

The following JSON structure shows the format of a `playlistImages` resource:  

```carbon
{
  "https://developers.google.com/youtube/v3/docs/playlistImages#kind": "youtube#playlistImage",
  "https://developers.google.com/youtube/v3/docs/playlistImages#id": string,
  "https://developers.google.com/youtube/v3/docs/playlistImages#snippet": {
    "https://developers.google.com/youtube/v3/docs/playlistImages#snippet.playlistId": string,
    "https://developers.google.com/youtube/v3/docs/playlistImages#snippet.type": string,
    "https://developers.google.com/youtube/v3/docs/playlistImages#snippet.width": string,
    "https://developers.google.com/youtube/v3/docs/playlistImages#snippet.height": string,
    }
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                              Properties                                                               ||
|----------------------|-----------------------------------------------------------------------------------------------------------------|
| `kind`               | `string` Identifies the API resource's type. The value will be `youtube#playlistImage`.                         |
| `id`                 | `string` The ID that YouTube uses to uniquely identify the playlist image.                                      |
| `snippet`            | `object` The `snippet` object contains basic details about the playlist image, such as its type and dimensions. |
| snippet.`playlistId` | `string` The playlist ID of the playlist this image is associated with.                                         |
| snippet.`type`       | `string` The image type.                                                                                        |
| snippet.`width`      | `string` The image's width.                                                                                     |
| snippet.`height`     | `string` The images's height.                                                                                   |