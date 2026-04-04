# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/generatePlayIntegrityChallenge.md.txt

# Method: projects.apps.generatePlayIntegrityChallenge

Generates a challenge that protects the integrity of an immediately following integrity verdict request to the Play Integrity API. The next call to `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangePlayIntegrityToken#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangePlayIntegrityToken` using the resulting integrity token will verify the presence and validity of the challenge. A challenge should not be reused for multiple calls.

### HTTP request

`POST https://firebaseappcheck.googleapis.com/v1beta/{app=projects/*/apps/*}:generatePlayIntegrityChallenge`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `app` | `string` Required. The relative resource name of the app, in the format: projects/{project_number}/apps/{app_id} If necessary, the `project_number` element can be replaced with the project ID of the Firebase project. Learn more about using project identifiers in Google's [AIP 2510](https://google.aip.dev/cloud/2510) standard. |

### Request body

The request body must be empty.

### Response body

Response message for the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/generatePlayIntegrityChallenge#google.firebase.appcheck.v1beta.TokenExchangeService.GeneratePlayIntegrityChallenge` method.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "challenge": string, "ttl": string } ``` |

| Fields ||
|---|---|
| `challenge` | `string` A one-time use [challenge](https://developer.android.com/google/play/integrity/verdict#protect-against-replay-attacks) for the client to pass to the Play Integrity API. |
| `ttl` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#duration` format)`` The duration from the time this challenge is minted until its expiration. This field is intended to ease client-side token management, since the client may have clock skew, but is still able to accurately measure a duration. A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).