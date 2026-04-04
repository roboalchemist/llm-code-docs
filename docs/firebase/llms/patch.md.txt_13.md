# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaEnterpriseConfig/patch.md.txt

# Method: projects.apps.recaptchaEnterpriseConfig.patch

Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaEnterpriseConfig#RecaptchaEnterpriseConfig` for the specified app.

While this configuration is incomplete or invalid, the app will be unable to exchange reCAPTCHA Enterprise tokens for App Check tokens.

### HTTP request

`PATCH https://firebaseappcheck.googleapis.com/v1beta/{recaptchaEnterpriseConfig.name=projects/*/apps/*/recaptchaEnterpriseConfig}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `recaptchaEnterpriseConfig.name` | `string` Required. The relative resource name of the reCAPTCHA Enterprise configuration object, in the format: projects/{project_number}/apps/{app_id}/recaptchaEnterpriseConfig |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` Required. A comma-separated list of names of fields in the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaEnterpriseConfig#RecaptchaEnterpriseConfig` to update. Example: `siteKey`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaEnterpriseConfig#RecaptchaEnterpriseConfig`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaEnterpriseConfig#RecaptchaEnterpriseConfig`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).