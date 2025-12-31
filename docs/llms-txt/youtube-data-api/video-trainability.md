# Source: https://developers.google.com/youtube/v3/video-trainability.md.txt

# YouTube Video Third-Party Trainability Home

YouTube Video Third-Party Trainability allows creators and rights holders to specify whether their
content can be used for training AI models.

## How it works

You can use the YouTube Video Third-Party Trainability API to identify if a given video is
trainable.

Creators and rights holders can choose whether to allow companies to use their
content for ML training. This is done by
[enabling the **Allow third-party companies to train AI models using my content** option](https://support.google.com/youtube/answer/15509944)
in YouTube Studio settings. By default, the third-party training setting is
turned off.

To learn more, see [Your content \& third-party training](https://support.google.com/youtube/answer/15509945)
in the YouTube Help Center.
| **Note:** Using the YouTube Video Third-Party Trainability API doesn't require authentication or quota requests.

## Service: youtube.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

- <https://youtube.googleapis.com/$discovery/rest?version=v3>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs are relative to this service endpoint:

- `https://youtube.googleapis.com/youtube/v3/videoTrainability`

## REST Resource: [v3.videoTrainability](https://developers.google.com/youtube/v3/video-trainability/reference/rest)

|                                                                           Methods                                                                           ||
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------|---|
| URIs relative to `https://www.googleapis.com/youtube/v3`                                                                                                       |||
| [get](https://developers.google.com/youtube/v3/video-trainability/reference/rest/get) | `GET /videoTrainability` Returns the trainability status of a video. |