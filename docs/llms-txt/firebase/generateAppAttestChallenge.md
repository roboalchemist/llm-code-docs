# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/oauthClients/generateAppAttestChallenge.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/generateAppAttestChallenge.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/generateAppAttestChallenge.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/oauthClients/generateAppAttestChallenge.md.txt

Generates a challenge that protects the integrity of an immediately following call to [oauthClients.exchangeAppAttestAttestation](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1.TokenExchangeService.ExchangeAppAttestAttestation) or [oauthClients.exchangeAppAttestAssertion](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAssertion#google.firebase.appcheck.v1.TokenExchangeService.ExchangeAppAttestAssertion). A challenge should not be reused for multiple calls.

### HTTP request

`POST https://firebaseappcheck.googleapis.com/v1/{app=oauthClients/*}:generateAppAttestChallenge`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                                                     Parameters                                                                                                                                                                     ||
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `app` | `string` Required. The relative resource name of the iOS app, in the format: projects/{project_number}/apps/{app_id} If necessary, the `project_number` element can be replaced with the project ID of the Firebase project. Learn more about using project identifiers in Google's [AIP 2510](https://google.aip.dev/cloud/2510) standard. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of [GenerateAppAttestChallengeResponse](https://firebase.google.com/docs/reference/appcheck/rest/v1/GenerateAppAttestChallengeResponse).

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).