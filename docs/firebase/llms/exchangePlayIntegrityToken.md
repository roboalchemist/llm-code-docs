# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangePlayIntegrityToken.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangePlayIntegrityToken.md.txt

Validates an
[integrity verdict response token from Play Integrity](https://developer.android.com/google/play/integrity/verdict#decrypt-verify)
. If valid, returns an
`
`[AppCheckToken](https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken)`
`
.

### HTTP request


`
POST https://firebaseappcheck.googleapis.com/v1/{app=projects/*/apps/*}:exchangePlayIntegrityToken
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

|                       JSON representation                       |
|-----------------------------------------------------------------|
| ``` { "playIntegrityToken": string, "limitedUse": boolean } ``` |

|                                                                                                                                             Fields                                                                                                                                              ||
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ` playIntegrityToken ` | ` string ` Required. The [integrity verdict response token from Play Integrity](https://developer.android.com/google/play/integrity/verdict#decrypt-verify) issued to your app.                                                                                         |
| ` limitedUse `         | ` boolean ` Specifies whether this attestation is for use in a *limited use* ( ` true ` ) or *session based* ( ` false ` ) context. To enable this attestation to be used with the *replay protection* feature, set this to ` true ` . The default value is ` false ` . |

### Response body


If successful, the response body contains an instance of
`
`[AppCheckToken](https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken)`
`
.