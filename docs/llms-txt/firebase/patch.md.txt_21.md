# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config/patch.md.txt

# Method: projects.apps.recaptchaV3Config.patch

Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config#RecaptchaV3Config` for the specified app.

While this configuration is incomplete or invalid, the app will be unable to exchange reCAPTCHA v3 tokens for App Check tokens.

For security reasons, the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config#RecaptchaV3Config.FIELDS.site_secret` field is never populated in the response.

### HTTP request

`PATCH https://firebaseappcheck.googleapis.com/v1/{recaptchaV3Config.name=projects/*/apps/*/recaptchaV3Config}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `recaptchaV3Config.name` | `string` Required. The relative resource name of the reCAPTCHA v3 configuration object, in the format: projects/{project_number}/apps/{app_id}/recaptchaV3Config |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` Required. A comma-separated list of names of fields in the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config#RecaptchaV3Config` to update. Example: `siteSecret`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config#RecaptchaV3Config`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config#RecaptchaV3Config`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).