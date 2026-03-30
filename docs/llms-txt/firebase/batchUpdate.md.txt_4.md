# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/batchUpdate.md.txt

# Method: projects.services.batchUpdate

Atomically updates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` configurations.

### HTTP request

`POST https://firebaseappcheck.googleapis.com/v1beta/{parent=projects/*}/services:batchUpdate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The parent project name shared by all `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` configurations being updated, in the format projects/{project_number} The parent collection in the `name` field of any resource being updated must match this field, or the entire batch fails. |

### Request body

The request body contains data with the following structure:

| JSON representation |
|---|
| ``` { "updateMask": string, "requests": [ { object (`https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/batchUpdate#UpdateServiceRequest`) } ] } ``` |

| Fields ||
|---|---|
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` Optional. A comma-separated list of names of fields in the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service`s to update. Example: `displayName`. If the `updateMask` field is set in both this request and any of the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/batchUpdate#UpdateServiceRequest` messages, they must match or the entire batch fails and no updates will be committed. |
| `requests[]` | ``object (`https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/batchUpdate#UpdateServiceRequest`)`` Required. The request messages specifying the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service`s to update. A maximum of 100 objects can be updated in a batch. |

### Response body

Response message for the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/batchUpdate#google.firebase.appcheck.v1beta.ConfigService.BatchUpdateServices` method.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "services": [ { object (`https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service`) } ] } ``` |

| Fields ||
|---|---|
| `services[]` | ``object (`https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service`)`` `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` objects after the updates have been applied. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).

## UpdateServiceRequest

Request message for the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/patch#google.firebase.appcheck.v1beta.ConfigService.UpdateService` method as well as an individual update message for the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/batchUpdate#google.firebase.appcheck.v1beta.ConfigService.BatchUpdateServices` method.

| JSON representation |
|---|
| ``` { "service": { object (`https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service`) }, "updateMask": string } ``` |

| Fields ||
|---|---|
| `service` | ``object (`https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service`)`` Required. The `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` to update. The `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service`'s `name` field is used to identify the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` to be updated, in the format: projects/{project_number}/services/{service_id} Note that the `service_id` element must be a supported service ID. Currently, the following service IDs are supported: - `firebasestorage.googleapis.com` (Cloud Storage for Firebase) - `firebasedatabase.googleapis.com` (Firebase Realtime Database) - `firestore.googleapis.com` (Cloud Firestore) - `identitytoolkit.googleapis.com` (Firebase Authentication with Identity Platform) - `oauth2.googleapis.com` (Google Identity for iOS) For Firebase Authentication to work with App Check, you must first upgrade to [Firebase Authentication with Identity Platform](https://firebase.google.com/docs/auth#identity-platform). |
| `updateMask` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#field-mask` format)`` Required. A comma-separated list of names of fields in the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` to update. Example: `enforcementMode`. |