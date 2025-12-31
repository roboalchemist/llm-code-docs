# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/GenerateAppAttestChallengeResponse.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/GenerateAppAttestChallengeResponse.md.txt

# GenerateAppAttestChallengeResponse

Response message for the [GenerateAppAttestChallenge](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/generateAppAttestChallenge#google.firebase.appcheck.v1.TokenExchangeService.GenerateAppAttestChallenge) method.

|              JSON representation               |
|------------------------------------------------|
| ``` { "challenge": string, "ttl": string } ``` |

|                                                                                                                                                                                                                     Fields                                                                                                                                                                                                                     ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `challenge` | `string (`[bytes](https://developers.google.com/discovery/v1/type-format)` format)` A one-time use challenge for the client to pass to the App Attest API. A base64-encoded string.                                                                                                                                                                                                                                               |
| `ttl`       | `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The duration from the time this challenge is minted until its expiration. This field is intended to ease client-side token management, since the client may have clock skew, but is still able to accurately measure a duration. A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. |