# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/oauthClients/exchangeAppAttestAssertion.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAssertion.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAssertion.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/oauthClients/exchangeAppAttestAssertion.md.txt

Accepts an App Attest assertion and an artifact previously obtained from
`
`[oauthClients.exchangeAppAttestAttestation](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1.TokenExchangeService.ExchangeAppAttestAttestation)`
`
and verifies those with Apple. If valid, returns an
`
`[AppCheckToken](https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken)`
`
.

### HTTP request


`
POST https://firebaseappcheck.googleapis.com/v1/{app=oauthClients/*}:exchangeAppAttestAssertion
`


The URL uses
[gRPC Transcoding](https://google.aip.dev/127)
syntax.

### Path parameters

|                                                                                                                                                                        Parameters                                                                                                                                                                        ||
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ` app ` | ` string ` Required. The relative resource name of the iOS app, in the format: projects/{project_number}/apps/{app_id} If necessary, the ` project_number ` element can be replaced with the project ID of the Firebase project. Learn more about using project identifiers in Google's [AIP 2510](https://google.aip.dev/cloud/2510) standard. |

### Request body


The request body contains data with the following structure:

|                                       JSON representation                                       |
|-------------------------------------------------------------------------------------------------|
| ``` { "artifact": string, "assertion": string, "challenge": string, "limitedUse": boolean } ``` |

|                                                                                                                                                                                                                   Fields                                                                                                                                                                                                                    ||
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ` artifact `   | ` string ( `[bytes](https://developers.google.com/discovery/v1/type-format)` format) ` Required. The artifact returned by a previous call to ` `[oauthClients.exchangeAppAttestAttestation](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1.TokenExchangeService.ExchangeAppAttestAttestation)` ` . A base64-encoded string.             |
| ` assertion `  | ` string ( `[bytes](https://developers.google.com/discovery/v1/type-format)` format) ` Required. The CBOR-encoded assertion returned by the client-side App Attest API. A base64-encoded string.                                                                                                                                                                                                                            |
| ` challenge `  | ` string ( `[bytes](https://developers.google.com/discovery/v1/type-format)` format) ` Required. A one-time challenge returned by an immediately prior call to ` `[oauthClients.generateAppAttestChallenge](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/generateAppAttestChallenge#google.firebase.appcheck.v1.TokenExchangeService.GenerateAppAttestChallenge)` ` . A base64-encoded string. |
| ` limitedUse ` | ` boolean ` Specifies whether this attestation is for use in a *limited use* ( ` true ` ) or *session based* ( ` false ` ) context. To enable this attestation to be used with the *replay protection* feature, set this to ` true ` . The default value is ` false ` .                                                                                                                                                     |

### Response body


If successful, the response body contains an instance of
`
`[AppCheckToken](https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken)`
`
.