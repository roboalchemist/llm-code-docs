# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.safetyNetConfig.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.safetyNetConfig.md.txt

# REST Resource: projects.apps.safetyNetConfig

## Resource: SafetyNetConfig

| The SafetyNet Attestation API is deprecated and has been replaced by the Play Integrity API. Support for SafetyNet will be removed from App Check by the migration deadline. We strongly recommend that App Check customers [migrate to the Play Integrity API](https://firebase.google.com/docs/app-check/android/play-integrity-provider). [Learn more](https://developer.android.com/training/safetynet/deprecation-timeline).
An app's SafetyNet configuration object. This configuration controls certain properties of the [`AppCheckToken`](https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken) returned by [ExchangeSafetyNetToken](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeSafetyNetToken#google.firebase.appcheck.v1.TokenExchangeService.ExchangeSafetyNetToken), such as its [ttl](https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken#FIELDS.ttl).

Note that your registered SHA-256 certificate fingerprints are used to validate tokens issued by SafetyNet; please register them via the Firebase Console or programmatically via the [Firebase Management Service](https://firebase.google.com/docs/projects/api/reference/rest/v11/projects.androidApps.sha/create).

|              JSON representation               |
|------------------------------------------------|
| ``` { "name": string, "tokenTtl": string } ``` |

|                                                                                                                                                                                                                        Fields                                                                                                                                                                                                                        ||
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`     | `string` Required. The relative resource name of the SafetyNet configuration object, in the format: projects/{project_number}/apps/{app_id}/safetyNetConfig                                                                                                                                                                                                                                                                              |
| `tokenTtl` | `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Specifies the duration for which App Check tokens exchanged from SafetyNet tokens will be valid. If unset, a default value of 1 hour is assumed. Must be between 30 minutes and 7 days, inclusive. A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. |

|                                                                                                                                                        ## Methods                                                                                                                                                         ||
|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ### [batchGet](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.safetyNetConfig/batchGet)` ` **(deprecated)** | Atomically gets the [SafetyNetConfig](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.safetyNetConfig#SafetyNetConfig)s for the specified list of apps. |
| ### [get](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.safetyNetConfig/get)` ` **(deprecated)**           | Gets the [SafetyNetConfig](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.safetyNetConfig#SafetyNetConfig) for the specified app.                      |
| ### [patch](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.safetyNetConfig/patch)` ` **(deprecated)**       | Updates the [SafetyNetConfig](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.safetyNetConfig#SafetyNetConfig) for the specified app.                   |