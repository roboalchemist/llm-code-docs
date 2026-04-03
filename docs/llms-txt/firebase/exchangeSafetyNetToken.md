# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeSafetyNetToken.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeSafetyNetToken.md.txt

# Method: projects.apps.exchangeSafetyNetToken

| The SafetyNet Attestation API is deprecated and has been replaced by the Play Integrity API. Support for SafetyNet will be removed from App Check by the migration deadline. We strongly recommend that App Check customers
| [migrate to the Play Integrity API](https://firebase.google.com/docs/app-check/android/play-integrity-provider)
| .
| [Learn more](https://developer.android.com/training/safetynet/deprecation-timeline)
| .

Validates a
[SafetyNet token](https://developer.android.com/training/safetynet/attestation#request-attestation-step)
. If valid, returns an
`
`[AppCheckToken](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken)`
`
.

### HTTP request


`
POST https://firebaseappcheck.googleapis.com/v1beta/{app=projects/*/apps/*}:exchangeSafetyNetToken
`


The URL uses
[gRPC Transcoding](https://google.aip.dev/127)
syntax.

### Path parameters

|                                                                                                                                                                          Parameters                                                                                                                                                                          ||
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ` app ` | ` string ` Required. The relative resource name of the Android app, in the format: projects/{project_number}/apps/{app_id} If necessary, the ` project_number ` element can be replaced with the project ID of the Firebase project. Learn more about using project identifiers in Google's [AIP 2510](https://google.aip.dev/cloud/2510) standard. |

### Request body


The request body contains data with the following structure:

|         JSON representation          |
|--------------------------------------|
| ``` { "safetyNetToken": string } ``` |

|                                                                                          Fields                                                                                          ||
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ` safetyNetToken ` | ` string ` Required. The [SafetyNet attestation response](https://developer.android.com/training/safetynet/attestation#request-attestation-step) issued to your app. |

### Response body


If successful, the response body contains an instance of
`
`[AppCheckToken](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken)`
`
.