# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig.md.txt

# REST Resource: projects.apps.deviceCheckConfig

## Resource: DeviceCheckConfig

An app's DeviceCheck configuration object. This configuration is used by `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeDeviceCheckToken#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeDeviceCheckToken` to validate device tokens issued to apps by DeviceCheck. It also controls certain properties of the returned `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken`, such as its `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken#FIELDS.ttl`.

Note that the Team ID registered with your app is used as part of the validation process. Please register it via the Firebase Console or programmatically via the [Firebase Management Service](https://firebase.google.com/docs/projects/api/reference/rest/v1beta1/projects.iosApps/patch).

| JSON representation |
|---|
| ``` { "name": string, "tokenTtl": string, "keyId": string, "privateKey": string, "privateKeySet": boolean } ``` |

| Fields ||
|---|---|
| `name` | `string` Required. The relative resource name of the DeviceCheck configuration object, in the format: projects/{project_number}/apps/{app_id}/deviceCheckConfig |
| `tokenTtl` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#duration` format)`` Specifies the duration for which App Check tokens exchanged from DeviceCheck tokens will be valid. If unset, a default value of 1 hour is assumed. Must be between 30 minutes and 7 days, inclusive. A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. |
| `keyId` | `string` Required. The key identifier of a private key enabled with DeviceCheck, created in your Apple Developer account. |
| `privateKey` | `string` Required. Input only. The contents of the private key (`.p8`) file associated with the key specified by `keyId`. For security reasons, this field will never be populated in any response. |
| `privateKeySet` | `boolean` Output only. Whether the `privateKey` field was previously set. Since we will never return the `privateKey` field, this field is the only way to find out whether it was previously set. |

| ## Methods ||
|---|---|
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig/batchGet` | Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig#DeviceCheckConfig`s for the specified list of apps. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig/get` | Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig#DeviceCheckConfig` for the specified app. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig/patch` | Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig#DeviceCheckConfig` for the specified app. |