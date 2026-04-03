# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/ExchangeAppAttestAttestationResponse.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/ExchangeAppAttestAttestationResponse.md.txt

# ExchangeAppAttestAttestationResponse

Response message for the [ExchangeAppAttestAttestation](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1.TokenExchangeService.ExchangeAppAttestAttestation) method.

|                                                           JSON representation                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "artifact": string, "appCheckToken": { object (https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken) } } ``` |

|                                                                                                                                                                                            Fields                                                                                                                                                                                             ||
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `artifact`      | `string (`[bytes](https://developers.google.com/discovery/v1/type-format)` format)` An artifact that can be used in future calls to [ExchangeAppAttestAssertion](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAssertion#google.firebase.appcheck.v1.TokenExchangeService.ExchangeAppAttestAssertion). A base64-encoded string. |
| `appCheckToken` | `object (`[AppCheckToken](https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken)`)` Encapsulates an App Check token.                                                                                                                                                                                                                                     |