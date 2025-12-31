# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/oauthClients/exchangeDebugToken.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/oauthClients/exchangeDebugToken.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeDebugToken.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeDebugToken.md.txt

Validates a debug token secret that you have previously created using
`
`[CreateDebugToken](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens/create#google.firebase.appcheck.v1.ConfigService.CreateDebugToken)`
`
. If valid, returns an
`
`[AppCheckToken](https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken)`
`
.


Note that a restrictive quota is enforced on this method to prevent accidental exposure of the app to abuse.

### HTTP request


`
POST https://firebaseappcheck.googleapis.com/v1/{app=projects/*/apps/*}:exchangeDebugToken
`


The URL uses
[gRPC Transcoding](https://google.aip.dev/127)
syntax.

### Path parameters

|                                                                                                                                                                      Parameters                                                                                                                                                                      ||
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ` app ` | ` string ` Required. The relative resource name of the app, in the format: projects/{project_number}/apps/{app_id} If necessary, the ` project_number ` element can be replaced with the project ID of the Firebase project. Learn more about using project identifiers in Google's [AIP 2510](https://google.aip.dev/cloud/2510) standard. |

### Request body


The request body contains data with the following structure:

|                   JSON representation                   |
|---------------------------------------------------------|
| ``` { "debugToken": string, "limitedUse": boolean } ``` |

|                                                                                                                                                       Fields                                                                                                                                                        ||
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ` debugToken ` | ` string ` Required. A debug token secret. This string must match a debug token secret previously created using ` `[CreateDebugToken](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens/create#google.firebase.appcheck.v1.ConfigService.CreateDebugToken)` ` . |
| ` limitedUse ` | ` boolean ` Specifies whether this attestation is for use in a *limited use* ( ` true ` ) or *session based* ( ` false ` ) context. To enable this attestation to be used with the *replay protection* feature, set this to ` true ` . The default value is ` false ` .                             |

### Response body


If successful, the response body contains an instance of
`
`[AppCheckToken](https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken)`
`
.