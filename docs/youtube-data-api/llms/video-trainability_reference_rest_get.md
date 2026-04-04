# Source: https://developers.google.com/youtube/v3/video-trainability/reference/rest/get.md.txt

# Method: videoTrainability.get

- [HTTP request](https://developers.google.com/youtube/v3/video-trainability/reference/rest/get#body.HTTP_TEMPLATE)
- [Query parameters](https://developers.google.com/youtube/v3/video-trainability/reference/rest/get#body.QUERY_PARAMETERS)
- [Request body](https://developers.google.com/youtube/v3/video-trainability/reference/rest/get#body.request_body)
- [Response body](https://developers.google.com/youtube/v3/video-trainability/reference/rest/get#body.response_body)
  - [JSON representation](https://developers.google.com/youtube/v3/video-trainability/reference/rest/get#body.VideoTrainability.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://developers.google.com/youtube/v3/video-trainability/reference/rest/get#body.aspect)
- [Try it!](https://developers.google.com/youtube/v3/video-trainability/reference/rest/get#try-it)

Returns the trainability status of a video.

### HTTP request

`GET https://youtube.googleapis.com/youtube/v3/videoTrainability`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

|                   Parameters                    ||
|------|-------------------------------------------|
| `id` | `string` The ID of the video to retrieve. |

### Request body

The request body must be empty.

### Response body

Specifies who is allowed to train on the video.

If successful, the response body contains data with the following structure:

|                                  JSON representation                                   |
|----------------------------------------------------------------------------------------|
| ``` { "videoId": string, "kind": string, "etag": string, "permitted": [ string ] } ``` |

|                                                                                    Fields                                                                                     ||
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `video``Id`   | `string` The ID of the video.                                                                                                                                  |
| `kind`        | `string` Identifies what kind of resource this is. Value: the fixed string `"youtube#videoTrainability"`                                                       |
| `etag`        | `string` Etag of this resource.                                                                                                                                |
| `permitted[]` | `string` Specifies who is allowed to train on the video. Valid values are: - A single string "all" - A single string "none" - A list of allowed parties <br /> |