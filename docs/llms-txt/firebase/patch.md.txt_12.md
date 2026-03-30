# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig/patch.md.txt

# Method: projects.apps.deviceCheckConfig.patch

Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig#DeviceCheckConfig` for the specified app.

While this configuration is incomplete or invalid, the app will be unable to exchange DeviceCheck tokens for App Check tokens.

For security reasons, the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig#DeviceCheckConfig.FIELDS.private_key` field is never populated in the response.

### HTTP request

`PATCH https://firebaseappcheck.googleapis.com/v1beta/{deviceCheckConfig.name=projects/*/apps/*/deviceCheckConfig}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `deviceCheckConfig.name` | `string` Required. The relative resource name of the DeviceCheck configuration object, in the format: projects/{project_number}/apps/{app_id}/deviceCheckConfig |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` Required. A comma-separated list of names of fields in the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig#DeviceCheckConfig` to update. Example: `keyId,privateKey`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig#DeviceCheckConfig`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig#DeviceCheckConfig`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).