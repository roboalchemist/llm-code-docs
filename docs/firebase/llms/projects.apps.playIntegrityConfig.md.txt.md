# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig.md.txt

# REST Resource: projects.apps.playIntegrityConfig

## Resource: PlayIntegrityConfig

An app's Play Integrity configuration object. This configuration controls certain properties of the `https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken` returned by `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangePlayIntegrityToken#google.firebase.appcheck.v1.TokenExchangeService.ExchangePlayIntegrityToken`, such as its `https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken#FIELDS.ttl`.

Note that your registered SHA-256 certificate fingerprints are used to validate tokens issued by the Play Integrity API; please register them via the Firebase Console or programmatically via the [Firebase Management Service](https://firebase.google.com/docs/projects/api/reference/rest/v1beta1/projects.androidApps.sha/create).

| JSON representation |
|---|
| ``` { "name": string, "tokenTtl": string } ``` |

| Fields ||
|---|---|
| `name` | `string` Required. The relative resource name of the Play Integrity configuration object, in the format: projects/{project_number}/apps/{app_id}/playIntegrityConfig |
| `tokenTtl` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#duration` format)`` Specifies the duration for which App Check tokens exchanged from Play Integrity tokens will be valid. If unset, a default value of 1 hour is assumed. Must be between 30 minutes and 7 days, inclusive. A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. |

| ## Methods ||
|---|---|
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig/batchGet` | Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig#PlayIntegrityConfig`s for the specified list of apps. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig/get` | Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig#PlayIntegrityConfig` for the specified app. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig/patch` | Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig#PlayIntegrityConfig` for the specified app. |