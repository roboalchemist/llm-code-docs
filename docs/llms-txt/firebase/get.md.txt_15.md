# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/get.md.txt

# Method: projects.services.get

Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` configuration for the specified service name.

### HTTP request

`GET https://firebaseappcheck.googleapis.com/v1beta/{name=projects/*/services/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The relative resource name of the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` to retrieve, in the format: projects/{project_number}/services/{service_id} Note that the `service_id` element must be a supported service ID. Currently, the following service IDs are supported: - `firebasestorage.googleapis.com` (Cloud Storage for Firebase) - `firebasedatabase.googleapis.com` (Firebase Realtime Database) - `firestore.googleapis.com` (Cloud Firestore) - `identitytoolkit.googleapis.com` (Firebase Authentication with Identity Platform) - `oauth2.googleapis.com` (Google Identity for iOS) |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).