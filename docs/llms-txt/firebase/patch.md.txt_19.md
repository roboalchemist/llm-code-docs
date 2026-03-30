# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig/patch.md.txt

# Method: projects.apps.appAttestConfig.patch

Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig#AppAttestConfig` for the specified app.

While this configuration is incomplete or invalid, the app will be unable to exchange AppAttest tokens for App Check tokens.

### HTTP request

`PATCH https://firebaseappcheck.googleapis.com/v1/{appAttestConfig.name=projects/*/apps/*/appAttestConfig}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `appAttestConfig.name` | `string` Required. The relative resource name of the App Attest configuration object, in the format: projects/{project_number}/apps/{app_id}/appAttestConfig |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` Required. A comma-separated list of names of fields in the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig#AppAttestConfig` to update. Example: `tokenTtl`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig#AppAttestConfig`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig#AppAttestConfig`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).