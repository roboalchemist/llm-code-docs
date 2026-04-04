# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAssertion.md.txt

# Method: projects.apps.exchangeAppAttestAssertion

Accepts an App Attest assertion and an artifact previously obtained from
`
https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAttestation
`
and verifies those with Apple. If valid, returns an
`
https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken
`
.

### HTTP request


`
POST https://firebaseappcheck.googleapis.com/v1beta/{app=projects/*/apps/*}:exchangeAppAttestAssertion
`


The URL uses
[gRPC Transcoding](https://google.aip.dev/127)
syntax.

### Path parameters

| Parameters ||
|---|---|
| ` app ` | ` string ` Required. The relative resource name of the iOS app, in the format: projects/{project_number}/apps/{app_id} If necessary, the ` project_number ` element can be replaced with the project ID of the Firebase project. Learn more about using project identifiers in Google's [AIP 2510](https://google.aip.dev/cloud/2510) standard. Alternatively, if this method is being called for an OAuth client protected by App Check, this field can also be in the format: oauthClients/{oauthClientId} You can view the OAuth client ID for your OAuth clients in the Google Cloud console. Note that only iOS OAuth clients are supported at this time, and they must be linked to corresponding iOS Firebase apps. Please see [the documentation](https://developers.google.com/identity/sign-in/ios/appcheck/get-started#project-setup) for more information. |

### Request body


The request body contains data with the following structure:

| JSON representation |
|---|
| ``` { "artifact": string, "assertion": string, "challenge": string, "limitedUse": boolean } ``` |

| Fields ||
|---|---|
| ` artifact ` | ` string ( https://developers.google.com/discovery/v1/type-format format) ` Required. The artifact returned by a previous call to ` https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAttestation ` . A base64-encoded string. |
| ` assertion ` | ` string ( https://developers.google.com/discovery/v1/type-format format) ` Required. The CBOR-encoded assertion returned by the client-side App Attest API. A base64-encoded string. |
| ` challenge ` | ` string ( https://developers.google.com/discovery/v1/type-format format) ` Required. A one-time challenge returned by an immediately prior call to ` https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/generateAppAttestChallenge#google.firebase.appcheck.v1beta.TokenExchangeService.GenerateAppAttestChallenge ` . A base64-encoded string. |
| ` limitedUse ` | ` boolean ` Specifies whether this attestation is for use in a *limited use* ( ` true ` ) or *session based* ( ` false ` ) context. To enable this attestation to be used with the *replay protection* feature, set this to ` true ` . The default value is ` false ` . |

### Response body


If successful, the response body contains an instance of
`
https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken
`
.