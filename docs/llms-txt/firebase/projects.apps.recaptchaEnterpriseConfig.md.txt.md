# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaEnterpriseConfig.md.txt

# REST Resource: projects.apps.recaptchaEnterpriseConfig

## Resource: RecaptchaEnterpriseConfig

An app's reCAPTCHA Enterprise configuration object. This configuration is used by `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeRecaptchaEnterpriseToken#google.firebase.appcheck.v1.TokenExchangeService.ExchangeRecaptchaEnterpriseToken` to validate reCAPTCHA tokens issued to apps by reCAPTCHA Enterprise. It also controls certain properties of the returned `https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken`, such as its `https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken#FIELDS.ttl`.

| JSON representation |
|---|
| ``` { "name": string, "tokenTtl": string, "siteKey": string } ``` |

| Fields ||
|---|---|
| `name` | `string` Required. The relative resource name of the reCAPTCHA Enterprise configuration object, in the format: projects/{project_number}/apps/{app_id}/recaptchaEnterpriseConfig |
| `tokenTtl` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#duration` format)`` Specifies the duration for which App Check tokens exchanged from reCAPTCHA Enterprise tokens will be valid. If unset, a default value of 1 hour is assumed. Must be between 30 minutes and 7 days, inclusive. A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. |
| `siteKey` | `string` The score-based site key [created in reCAPTCHA Enterprise](https://cloud.google.com/recaptcha-enterprise/docs/create-key#creating_a_site_key) used to [invoke reCAPTCHA and generate the reCAPTCHA tokens](https://cloud.google.com/recaptcha-enterprise/docs/instrument-web-pages) for your application. Important: This is *not* the `siteSecret` (as it is in reCAPTCHA v3), but rather your score-based reCAPTCHA Enterprise site key. |

| ## Methods ||
|---|---|
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaEnterpriseConfig/batchGet` | Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaEnterpriseConfig#RecaptchaEnterpriseConfig`s for the specified list of apps. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaEnterpriseConfig/get` | Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaEnterpriseConfig#RecaptchaEnterpriseConfig` for the specified app. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaEnterpriseConfig/patch` | Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaEnterpriseConfig#RecaptchaEnterpriseConfig` for the specified app. |