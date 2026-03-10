# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/oauthClients/generateAppAttestChallenge.md.txt

# Method: oauthClients.generateAppAttestChallenge

Generates a challenge that protects the integrity of an immediately following call to `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1.TokenExchangeService.ExchangeAppAttestAttestation` or `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAssertion#google.firebase.appcheck.v1.TokenExchangeService.ExchangeAppAttestAssertion`. A challenge should not be reused for multiple calls.

### HTTP request

`POST https://firebaseappcheck.googleapis.com/v1/{app=oauthClients/*}:generateAppAttestChallenge`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `app` | `string` Required. The relative resource name of the iOS app, in the format: projects/{project_number}/apps/{app_id} If necessary, the `project_number` element can be replaced with the project ID of the Firebase project. Learn more about using project identifiers in Google's [AIP 2510](https://google.aip.dev/cloud/2510) standard. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1/GenerateAppAttestChallengeResponse`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).