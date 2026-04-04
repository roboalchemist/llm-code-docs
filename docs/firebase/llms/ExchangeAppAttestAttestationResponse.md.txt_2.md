# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/ExchangeAppAttestAttestationResponse.md.txt

# ExchangeAppAttestAttestationResponse

Response message for the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAttestation` method.

| JSON representation |
|---|
| ``` { "artifact": string, "attestationToken": { object (`https://firebase.google.com/docs/reference/appcheck/rest/v1beta/ExchangeAppAttestAttestationResponse#AttestationTokenResponse`) }, "appCheckToken": { object (`https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken`) } } ``` |

| Fields ||
|---|---|
| `artifact` | `string (https://developers.google.com/discovery/v1/type-format format)` An artifact that can be used in future calls to `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAssertion#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAssertion`. A base64-encoded string. |
| `attestationToken (deprecated)` | ``object (`https://firebase.google.com/docs/reference/appcheck/rest/v1beta/ExchangeAppAttestAttestationResponse#AttestationTokenResponse`)`` > [!WARNING] > This field is deprecated; it has been renamed to `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/ExchangeAppAttestAttestationResponse#FIELDS.app_check_token`. Encapsulates an App Check token. |
| `appCheckToken` | ``object (`https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken`)`` Encapsulates an App Check token. |

## AttestationTokenResponse

> [!WARNING]
> This object is deprecated; it has been renamed to `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken`.

Encapsulates an *App Check token*, which are used to access Firebase services protected by App Check.

| JSON representation |
|---|
| ``` { "attestationToken": string, "ttl": string } ``` |

| Fields ||
|---|---|
| `attestationToken` | `string` An App Check token. App Check tokens are signed [JWTs](https://tools.ietf.org/html/rfc7519) containing claims that identify the attested app and Firebase project. This token is used to access Firebase services protected by App Check. |
| `ttl` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#duration` format)`` The duration from the time this token is minted until its expiration. This field is intended to ease client-side token management, since the client may have clock skew, but is still able to accurately measure a duration. A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. |