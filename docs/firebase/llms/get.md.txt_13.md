# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig/get.md.txt

# Method: projects.apps.recaptchaConfig.get

> [!WARNING]
> The `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig#RecaptchaConfig` REST resource is deprecated; it has been renamed to `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaV3Config#RecaptchaV3Config`. Please use `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaV3Config/get#google.firebase.appcheck.v1beta.ConfigService.GetRecaptchaV3Config` instead.

Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig#RecaptchaConfig` for the specified app.

For security reasons, the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig#RecaptchaConfig.FIELDS.site_secret` field is never populated in the response.

### HTTP request

`GET https://firebaseappcheck.googleapis.com/v1beta/{name=projects/*/apps/*/recaptchaConfig}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The relative resource name of the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig#RecaptchaConfig`, in the format: projects/{project_number}/apps/{app_id}/recaptchaConfig |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig#RecaptchaConfig`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).