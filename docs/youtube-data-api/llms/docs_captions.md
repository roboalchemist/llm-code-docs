# Source: https://developers.google.com/youtube/v3/docs/captions.md.txt

# Captions

**Note:** On March 13, 2024, YouTube announced that it is deprecating the `sync` parameter for the [captions.insert](https://developers.google.com/youtube/v3/docs/captions/insert) and [captions.update](https://developers.google.com/youtube/v3/docs/captions/insert) API endpoints. Captions auto-syncing is still available in YouTube Creator Studio. See the [API revision history](https://developers.google.com/youtube/v3/revision_history#release_notes_03_13_2024) for more details.
A **caption** resource represents a YouTube caption track. A caption track is associated with exactly one YouTube video.

## Methods

The API supports the following methods for `captions` resources:

[list](https://developers.google.com/youtube/v3/docs/captions/list)
:   Retrieve a list of caption tracks that are associated with a specified video. Note that the API response does not contain the actual captions and that the [captions.download](https://developers.google.com/youtube/v3/docs/captions/download) method provides the ability to retrieve a caption track.
    [Try it now](https://developers.google.com/youtube/v3/docs/captions/list#usage).

[insert](https://developers.google.com/youtube/v3/docs/captions/insert)
:   Upload a caption track.
    [Try it now](https://developers.google.com/youtube/v3/docs/captions/insert).

[update](https://developers.google.com/youtube/v3/docs/captions/update)
:   Update a caption track. When updating a caption track, you can change the track's [draft status](https://developers.google.com/youtube/v3/docs/captions#snippet.isDraft), upload a new caption file for the track, or both.
    [Try it now](https://developers.google.com/youtube/v3/docs/captions/update).

[download](https://developers.google.com/youtube/v3/docs/captions/download)
:   Download a caption track. The caption track is returned to its original format unless the request specifies a value for the `tfmt` parameter and to its original language unless the request specifies a value for the `tlang` parameter.
    [Try it now](https://developers.google.com/youtube/v3/docs/captions/download).

[delete](https://developers.google.com/youtube/v3/docs/captions/delete)
:   Delete a specified caption track.
    [Try it now](https://developers.google.com/youtube/v3/docs/captions/delete).

## Resource representation

The following JSON structure shows the format of a `captions` resource:  

```text
{
  "kind": "youtube#caption",
  "etag": etag,
  "id": string,
  "snippet": {
    "videoId": string,
    "lastUpdated": datetime,
    "trackKind": string,
    "language": string,
    "name": string,
    "audioTrackType": string,
    "isCC": boolean,
    "isLarge": boolean,
    "isEasyReader": boolean,
    "isDraft": boolean,
    "isAutoSynced": boolean,
    "status": string,
    "failureReason": string
  }
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                                                                                                                                                                                                                                          Properties                                                                                                                                                                                                                                                                                          ||
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kind`                   | `string` Identifies the API resource's type. The value will be `youtube#caption`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `etag`                   | `etag` The Etag of this resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `id`                     | `string` The ID that YouTube uses to uniquely identify the caption track.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `snippet`                | `object` The `snippet` object contains basic details about the caption.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| snippet.`videoId`        | `string` The ID that YouTube uses to uniquely identify the video associated with the caption track.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| snippet.`lastUpdated`    | `datetime` The date and time when the caption track was last updated. The value is specified in [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format.                                                                                                                                                                                                                                                                                                                                                                                                            |
| snippet.`trackKind`      | `string` The caption track's type. Valid values for this property are: - `ASR` -- A caption track generated using automatic speech recognition. - `forced` -- A caption track that plays when no other track is selected in the player. For example, a video that shows aliens speaking in an alien language might have a forced caption track to only show subtitles for the alien language. - `standard` -- A regular caption track. This is the default value.                                                                                                  |
| snippet.`language`       | `string` The language of the caption track. The property value is a [BCP-47](http://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| snippet.`name`           | `string` The name of the caption track. The name is intended to be visible to the user as an option during playback. The maximum name length supported is 150 characters.                                                                                                                                                                                                                                                                                                                                                                                          |
| snippet.`audioTrackType` | `string` The type of audio track associated with the caption track. Valid values for this property are: - `commentary` -- The caption track corresponds to an alternate audio track that includes commentary, such as directory commentary. - `descriptive` -- The caption track corresponds to an alternate audio track that includes additional descriptive audio. - `primary` -- The caption track corresponds to the primary audio track for the video, which is the audio track normally associated with the video. - `unknown` -- This is the default value. |
| snippet.`isCC`           | `boolean` Indicates whether the track contains closed captions for the deaf and hard of hearing. The default value is `false`.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| snippet.`isLarge`        | `boolean` Indicates whether the caption track uses large text for the vision-impaired. The default value is `false`.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| snippet.`isEasyReader`   | `boolean` Indicates whether caption track is formatted for "easy reader," meaning it is at a third-grade level for language learners. The default value is `false`.                                                                                                                                                                                                                                                                                                                                                                                                |
| snippet.`isDraft`        | `boolean` Indicates whether the caption track is a draft. If the value is `true`, then the track is not publicly visible. The default value is `false`.                                                                                                                                                                                                                                                                                                                                                                                                            |
| snippet.`isAutoSynced`   | `boolean` Indicates whether YouTube synchronized the caption track to the audio track in the video. The value will be `true` if a sync was explicitly requested when the caption track was uploaded. For example, when calling the `captions.insert` or `captions.update` methods, you can set the `sync` parameter to `true` to instruct YouTube to sync the uploaded track to the video. If the value is `false`, YouTube uses the time codes in the uploaded caption track to determine when to display captions.                                               |
| snippet.`status`         | `string` The caption track's status. Valid values for this property are: - `failed` - `serving` - `syncing`                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| snippet.`failureReason`  | `string` The reason that YouTube failed to process the caption track. This property is only present if the [state](https://developers.google.com/youtube/v3/docs/captions#state) property's value is `failed`. Valid values for this property are: - `processingFailed` -- YouTube failed to process the uploaded caption track. - `unknownFormat` -- The caption track's format was not recognized. - `unsupportedFormat` -- The caption track's format is not supported.                                                                                         |