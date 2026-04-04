# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps/getAabInfo.md.txt

# Method: projects.apps.getAabInfo

- [HTTP request](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps/getAabInfo#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps/getAabInfo#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps/getAabInfo#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps/getAabInfo#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps/getAabInfo#body.AabInfo.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps/getAabInfo#body.aspect)
- [IntegrationState](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps/getAabInfo#IntegrationState)
- [TestCertificate](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps/getAabInfo#TestCertificate)
  - [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps/getAabInfo#TestCertificate.SCHEMA_REPRESENTATION)
- [Try it!](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps/getAabInfo#try-it)

Gets Android App Bundle (AAB) information for a Firebase app.

### HTTP request

`GET https://firebaseappdistribution.googleapis.com/v1/{name=projects/*/apps/*/aabInfo}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                                                       Parameters                                                                                                                                                                       ||
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name` | `string` Required. The name of the `AabInfo` resource to retrieve. Format: `projects/{projectNumber}/apps/{appId}/aabInfo` Authorization requires the following [IAM](https://firebase.google.com/docs/projects/iam/overview/) permission on the Firebase project that owns the specified resource `name`: - `firebaseappdistro.releases.list` |

### Request body

The request body must be empty.

### Response body

Android App Bundle (AAB) information for a Firebase app.

If successful, the response body contains data with the following structure:

|                                                                                                                                                JSON representation                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "name": string, "integrationState": enum (https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps/getAabInfo#IntegrationState), "testCertificate": { object (https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps/getAabInfo#TestCertificate) } } ``` |

|                                                                                                                                     Fields                                                                                                                                     ||
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`               | `string` The name of the `AabInfo` resource. Format: `projects/{projectNumber}/apps/{app}/aabInfo`                                                                                                                                                       |
| `integration``State` | `enum (`[IntegrationState](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps/getAabInfo#IntegrationState)`)` App bundle integration state. Only valid for android apps.                                                  |
| `test``Certificate`  | `object (`[TestCertificate](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps/getAabInfo#TestCertificate)`)` App bundle test certificate generated for the app. Set after the first app bundle is uploaded for this app. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).

## IntegrationState

The current state of AAB integration

|                                                          Enums                                                          ||
|-----------------------------------------------|--------------------------------------------------------------------------|
| `AAB_INTEGRATION_STATE_UNSPECIFIED`           | Aab integration state unspecified                                        |
| `INTEGRATED`                                  | App can receive app bundle uploads                                       |
| `PLAY_ACCOUNT_NOT_LINKED`                     | Firebase project is not linked to a Play developer account               |
| `NO_APP_WITH_GIVEN_BUNDLE_ID_IN_PLAY_ACCOUNT` | There is no app in linked Play developer account with the same bundle id |
| `APP_NOT_PUBLISHED`                           | The app in Play developer account is not in a published state            |
| `AAB_STATE_UNAVAILABLE`                       | Play App status is unavailable                                           |
| `PLAY_IAS_TERMS_NOT_ACCEPTED`                 | Play IAS terms not accepted                                              |

## TestCertificate

App bundle test certificate

|                           JSON representation                           |
|-------------------------------------------------------------------------|
| ``` { "hashSha1": string, "hashSha256": string, "hashMd5": string } ``` |

|                                              Fields                                               ||
|----------------|-----------------------------------------------------------------------------------|
| `hash``Sha1`   | `string` Hex string of SHA1 hash of the test certificate used to resign the AAB   |
| `hash``Sha256` | `string` Hex string of SHA256 hash of the test certificate used to resign the AAB |
| `hash``Md5`    | `string` Hex string of MD5 hash of the test certificate used to resign the AAB    |