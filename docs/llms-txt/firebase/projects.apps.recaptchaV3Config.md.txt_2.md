# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config.md.txt

# REST Resource: projects.apps.recaptchaV3Config

## Resource: RecaptchaV3Config

An app's reCAPTCHA v3 configuration object. This configuration is used by `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeRecaptchaV3Token#google.firebase.appcheck.v1.TokenExchangeService.ExchangeRecaptchaV3Token` to validate reCAPTCHA tokens issued to apps by reCAPTCHA v3. It also controls certain properties of the returned `https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken`, such as its `https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken#FIELDS.ttl`.

| JSON representation |
|---|
| ``` { "tokenTtl": string, "name": string, "siteSecret": string, "siteSecretSet": boolean } ``` |

| Fields ||
|---|---|
| `tokenTtl` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#duration` format)`` Specifies the duration for which App Check tokens exchanged from reCAPTCHA tokens will be valid. If unset, a default value of 1 day is assumed. Must be between 30 minutes and 7 days, inclusive. A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. |
| `name` | `string` Required. The relative resource name of the reCAPTCHA v3 configuration object, in the format: projects/{project_number}/apps/{app_id}/recaptchaV3Config |
| `siteSecret` | `string` Required. Input only. The site secret used to identify your service for reCAPTCHA v3 verification. For security reasons, this field will never be populated in any response. |
| `siteSecretSet` | `boolean` Output only. Whether the `siteSecret` field was previously set. Since we will never return the `siteSecret` field, this field is the only way to find out whether it was previously set. |

| ## Methods ||
|---|---|
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config/batchGet` | Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config#RecaptchaV3Config`s for the specified list of apps. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config/get` | Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config#RecaptchaV3Config` for the specified app. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config/patch` | Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config#RecaptchaV3Config` for the specified app. |