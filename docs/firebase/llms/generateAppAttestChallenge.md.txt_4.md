# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/generateAppAttestChallenge.md.txt

# Method: projects.apps.generateAppAttestChallenge

Generates a challenge that protects the integrity of an immediately following call to `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAttestation` or `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAssertion#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAssertion`. A challenge should not be reused for multiple calls.

### HTTP request

`POST https://firebaseappcheck.googleapis.com/v1beta/{app=projects/*/apps/*}:generateAppAttestChallenge`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `app` | `string` Required. The relative resource name of the iOS app, in the format: projects/{project_number}/apps/{app_id} If necessary, the `project_number` element can be replaced with the project ID of the Firebase project. Learn more about using project identifiers in Google's [AIP 2510](https://google.aip.dev/cloud/2510) standard. Alternatively, if this method is being called for an OAuth client protected by App Check, this field can also be in the format: oauthClients/{oauthClientId} You can view the OAuth client ID for your OAuth clients in the Google Cloud console. Note that only iOS OAuth clients are supported at this time, and they must be linked to corresponding iOS Firebase apps. Please see [the documentation](https://developers.google.com/identity/sign-in/ios/appcheck/get-started#project-setup) for more information. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/GenerateAppAttestChallengeResponse`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).