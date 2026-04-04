# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig.md.txt

# REST Resource: projects.apps.recaptchaConfig

## Resource: RecaptchaConfig

> [!WARNING]
> This REST resource is deprecated; it has been renamed to `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaV3Config#RecaptchaV3Config`.

An app's reCAPTCHA v3 configuration object. This configuration is used by `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeRecaptchaToken#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeRecaptchaToken` to validate reCAPTCHA tokens issued to apps by reCAPTCHA v3. It also controls certain properties of the returned `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken`, such as its `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken#FIELDS.ttl`.

| JSON representation |
|---|
| ``` { "tokenTtl": string, "name": string, "siteSecret": string, "siteSecretSet": boolean } ``` |

| Fields ||
|---|---|
| `tokenTtl` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#duration` format)`` Specifies the duration for which App Check tokens exchanged from reCAPTCHA tokens will be valid. If unset, a default value of 1 day is assumed. Must be between 30 minutes and 7 days, inclusive. A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. |
| `name` | `string` Required. The relative resource name of the reCAPTCHA v3 configuration object, in the format: projects/{project_number}/apps/{app_id}/recaptchaConfig |
| `siteSecret` | `string` Required. Input only. The site secret used to identify your service for reCAPTCHA v3 verification. For security reasons, this field will never be populated in any response. |
| `siteSecretSet` | `boolean` Output only. Whether the `siteSecret` field was previously set. Since we will never return the `siteSecret` field, this field is the only way to find out whether it was previously set. |

| ## Methods ||
|---|---|
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig/batchGet (deprecated)` | Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig#RecaptchaConfig`s for the specified list of apps. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig/get (deprecated)` | Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig#RecaptchaConfig` for the specified app. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig/patch (deprecated)` | Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig#RecaptchaConfig` for the specified app. |