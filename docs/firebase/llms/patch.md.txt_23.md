# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig/patch.md.txt

# Method: projects.apps.playIntegrityConfig.patch

Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig#PlayIntegrityConfig` for the specified app.

While this configuration is incomplete or invalid, the app will be unable to exchange Play Integrity tokens for App Check tokens.

### HTTP request

`PATCH https://firebaseappcheck.googleapis.com/v1beta/{playIntegrityConfig.name=projects/*/apps/*/playIntegrityConfig}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `playIntegrityConfig.name` | `string` Required. The relative resource name of the Play Integrity configuration object, in the format: projects/{project_number}/apps/{app_id}/playIntegrityConfig |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` Required. A comma-separated list of names of fields in the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig#PlayIntegrityConfig` to update. Example: `tokenTtl`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig#PlayIntegrityConfig`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig#PlayIntegrityConfig`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).