# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.md.txt

# REST Resource: projects.services

## Resource: Service

The enforcement configuration for a Firebase service supported by App Check.

| JSON representation |
|---|
| ``` { "name": string, "enforcementMode": enum (`https://firebase.google.com/docs/reference/appcheck/rest/v1beta/EnforcementMode`), "updateTime": string, "etag": string } ``` |

| Fields ||
|---|---|
| `name` | `string` Required. The relative resource name of the service configuration object, in the format: projects/{project_number}/services/{service_id} Note that the `service_id` element must be a supported service ID. Currently, the following service IDs are supported: - `firebasestorage.googleapis.com` (Cloud Storage for Firebase) - `firebasedatabase.googleapis.com` (Firebase Realtime Database) - `firestore.googleapis.com` (Cloud Firestore) - `identitytoolkit.googleapis.com` (Firebase Authentication with Identity Platform) - `oauth2.googleapis.com` (Google Identity for iOS) |
| `enforcementMode` | ``enum (`https://firebase.google.com/docs/reference/appcheck/rest/v1beta/EnforcementMode`)`` Required. The App Check enforcement mode for this service. |
| `updateTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Output only. Timestamp when this service configuration object was most recently updated. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `etag` | `string` This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. This etag is strongly validated as defined by RFC 7232. |

| ## Methods ||
|---|---|
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/batchUpdate` | Atomically updates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` configurations. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/get` | Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` configuration for the specified service name. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/list` | Lists all `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` configurations for the specified project. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/patch` | Updates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` configuration. |