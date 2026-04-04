# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/oauthClients/exchangeDebugToken.md.txt

# Method: oauthClients.exchangeDebugToken

Validates a debug token secret that you have previously created using
`
https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/create#google.firebase.appcheck.v1beta.ConfigService.CreateDebugToken
`
. If valid, returns an
`
https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken
`
.


Note that a restrictive quota is enforced on this method to prevent accidental exposure of the app to abuse.

### HTTP request


`
POST https://firebaseappcheck.googleapis.com/v1beta/{app=oauthClients/*}:exchangeDebugToken
`


The URL uses
[gRPC Transcoding](https://google.aip.dev/127)
syntax.

### Path parameters

| Parameters ||
|---|---|
| ` app ` | ` string ` Required. The relative resource name of the app, in the format: projects/{project_number}/apps/{app_id} If necessary, the ` project_number ` element can be replaced with the project ID of the Firebase project. Learn more about using project identifiers in Google's [AIP 2510](https://google.aip.dev/cloud/2510) standard. Alternatively, if this method is being called for an OAuth client protected by App Check, this field can also be in the format: oauthClients/{oauthClientId} You can view the OAuth client ID for your OAuth clients in the Google Cloud console. Note that only iOS OAuth clients are supported at this time, and they must be linked to corresponding iOS Firebase apps. Please see [the documentation](https://developers.google.com/identity/sign-in/ios/appcheck/get-started#project-setup) for more information. |

### Request body


The request body contains data with the following structure:

| JSON representation |
|---|
| ``` { "debugToken": string, "limitedUse": boolean } ``` |

| Fields ||
|---|---|
| ` debugToken ` | ` string ` Required. A debug token secret. This string must match a debug token secret previously created using ` https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/create#google.firebase.appcheck.v1beta.ConfigService.CreateDebugToken ` . |
| ` limitedUse ` | ` boolean ` Specifies whether this attestation is for use in a *limited use* ( ` true ` ) or *session based* ( ` false ` ) context. To enable this attestation to be used with the *replay protection* feature, set this to ` true ` . The default value is ` false ` . |

### Response body


If successful, the response body contains an instance of
`
https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken
`
.