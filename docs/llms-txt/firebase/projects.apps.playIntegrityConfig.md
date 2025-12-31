# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig.md.txt

## Resource: PlayIntegrityConfig

An app's Play Integrity configuration object. This configuration controls certain properties of the [`AppCheckToken`](https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken) returned by [ExchangePlayIntegrityToken](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangePlayIntegrityToken#google.firebase.appcheck.v1.TokenExchangeService.ExchangePlayIntegrityToken), such as its [ttl](https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken#FIELDS.ttl).

Note that your registered SHA-256 certificate fingerprints are used to validate tokens issued by the Play Integrity API; please register them via the Firebase Console or programmatically via the [Firebase Management Service](https://firebase.google.com/docs/projects/api/reference/rest/v1beta1/projects.androidApps.sha/create).

|              JSON representation               |
|------------------------------------------------|
| ``` { "name": string, "tokenTtl": string } ``` |

|                                                                                                                                                                                                        Fields                                                                                                                                                                                                        ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`     | `string` Required. The relative resource name of the Play Integrity configuration object, in the format: projects/{project_number}/apps/{app_id}/playIntegrityConfig                                                                                                                                                                                                                                     |
| `tokenTtl` | `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Specifies the duration for which App Check tokens exchanged from Play Integrity tokens will be valid. If unset, a default value of 1 hour is assumed. Must be between 30 minutes and 7 days, inclusive. A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. |

|                                                                                                                                                      ## Methods                                                                                                                                                       ||
|------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ### [batchGet](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig/batchGet) | Atomically gets the [PlayIntegrityConfig](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig#PlayIntegrityConfig)s for the specified list of apps. |
| ### [get](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig/get)           | Gets the [PlayIntegrityConfig](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig#PlayIntegrityConfig) for the specified app.                      |
| ### [patch](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig/patch)       | Updates the [PlayIntegrityConfig](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig#PlayIntegrityConfig) for the specified app.                   |