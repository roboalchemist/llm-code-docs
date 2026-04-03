# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/UploadReleaseResponse.md.txt

# UploadReleaseResponse

- [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/UploadReleaseResponse#SCHEMA_REPRESENTATION)

Response message for `releases.upload`.

|                                                                                                               JSON representation                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "result": enum (https://firebase.google.com/docs/reference/app-distribution/rest/v1/UploadReleaseResult), "release": { object (https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases#Release) } } ``` |

|                                                                                       Fields                                                                                       ||
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `result`  | `enum (`[UploadReleaseResult](https://firebase.google.com/docs/reference/app-distribution/rest/v1/UploadReleaseResult)`)` Result of upload release.                     |
| `release` | `object (`[Release](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases#Release)`)` Release associated with the uploaded binary. |