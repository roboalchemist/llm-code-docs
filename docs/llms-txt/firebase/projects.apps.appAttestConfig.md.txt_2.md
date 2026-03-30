# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig.md.txt

# REST Resource: projects.apps.appAttestConfig

## Resource: AppAttestConfig

An app's App Attest configuration object. This configuration controls certain properties of the `https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken` returned by `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1.TokenExchangeService.ExchangeAppAttestAttestation` and `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAssertion#google.firebase.appcheck.v1.TokenExchangeService.ExchangeAppAttestAssertion`, such as its `https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken#FIELDS.ttl`.

Note that the Team ID registered with your app is used as part of the validation process. Please register it via the Firebase Console or programmatically via the [Firebase Management Service](https://firebase.google.com/docs/projects/api/reference/rest/v11/projects.iosApps/patch).

| JSON representation |
|---|
| ``` { "name": string, "tokenTtl": string } ``` |

| Fields ||
|---|---|
| `name` | `string` Required. The relative resource name of the App Attest configuration object, in the format: projects/{project_number}/apps/{app_id}/appAttestConfig |
| `tokenTtl` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#duration` format)`` Specifies the duration for which App Check tokens exchanged from App Attest artifacts will be valid. If unset, a default value of 1 hour is assumed. Must be between 30 minutes and 7 days, inclusive. A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. |

| ## Methods ||
|---|---|
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig/batchGet` | Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig#AppAttestConfig`s for the specified list of apps. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig/get` | Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig#AppAttestConfig` for the specified app. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig/patch` | Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig#AppAttestConfig` for the specified app. |