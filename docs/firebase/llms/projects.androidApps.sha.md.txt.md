# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha.md.txt

# REST Resource: projects.androidApps.sha

## Resource: ShaCertificate

A SHA-1 or SHA-256 certificate associated with the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp`.

| JSON representation |
|---|
| ``` { "name": string, "shaHash": string, "certType": enum (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha#ShaCertificateType`) } ``` |

| Fields ||
|---|---|
| `name` | `string` The resource name of the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha#ShaCertificate` for the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp`, in the format: `projects/PROJECT_IDENTIFIER/androidApps/APP_ID/sha/SHA_HASH` - <var translate="no">PROJECT_IDENTIFIER</var>: the parent Project's [`ProjectNumber`](https://firebase.google.com/docs/reference/firebase-management/rest/projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its [`ProjectId`](https://firebase.google.com/docs/reference/firebase-management/rest/projects#FirebaseProject.FIELDS.project_id). Learn more about using project identifiers in Google's [AIP 2510 standard](https://google.aip.dev/cloud/2510). Note that the value for <var translate="no">PROJECT_IDENTIFIER</var> in any response body will be the `ProjectId`. - <var translate="no">APP_ID</var>: the globally unique, Firebase-assigned identifier for the App (see [`appId`](https://firebase.google.com/docs/reference/firebase-management/rest/projects.androidApps#AndroidApp.FIELDS.app_id)). - <var translate="no">SHA_HASH</var>: the certificate hash for the App (see [`shaHash`](https://firebase.google.com/docs/reference/firebase-management/rest/projects.androidApps.sha#ShaCertificate.FIELDS.sha_hash)). |
| `shaHash` | `string` The certificate hash for the `AndroidApp`. |
| `certType` | ``enum (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha#ShaCertificateType`)`` The type of SHA certificate encoded in the hash. |

## ShaCertificateType

The type of SHA certificate encoded in the hash.

| Enums ||
|---|---|
| `SHA_CERTIFICATE_TYPE_UNSPECIFIED` | Unknown state. This is only used for distinguishing unset values. |
| `SHA_1` | Certificate is a SHA-1 type certificate. |
| `SHA_256` | Certificate is a SHA-256 type certificate. |

| ## Methods ||
|---|---|
| ### `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha/create` | Adds a `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha#ShaCertificate` to the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp`. |
| ### `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha/delete` | Removes a `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha#ShaCertificate` from the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp`. |
| ### `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha/list` | Lists the SHA-1 and SHA-256 certificates for the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp`. |