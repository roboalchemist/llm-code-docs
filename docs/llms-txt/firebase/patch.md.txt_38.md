# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/patch.md.txt

# Method: projects.services.patch

Updates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` configuration.

### HTTP request

`PATCH https://firebaseappcheck.googleapis.com/v1beta/{service.name=projects/*/services/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `service.name` | `string` Required. The relative resource name of the service configuration object, in the format: projects/{project_number}/services/{service_id} Note that the `service_id` element must be a supported service ID. Currently, the following service IDs are supported: - `firebasestorage.googleapis.com` (Cloud Storage for Firebase) - `firebasedatabase.googleapis.com` (Firebase Realtime Database) - `firestore.googleapis.com` (Cloud Firestore) - `identitytoolkit.googleapis.com` (Firebase Authentication with Identity Platform) - `oauth2.googleapis.com` (Google Identity for iOS) |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` Required. A comma-separated list of names of fields in the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` to update. Example: `enforcementMode`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).