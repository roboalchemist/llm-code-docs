# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken.md.txt

# AppCheckToken

Encapsulates an *App Check token*, which are used to access backend services protected by App Check.

| JSON representation |
|---|
| ``` { "attestationToken": string, "token": string, "ttl": string } ``` |

| Fields ||
|---|---|
| `attestationToken (deprecated)` | `string` > [!WARNING] > This field is deprecated; it has been renamed to `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken#FIELDS.token`. The App Check token. App Check tokens are signed [JWTs](https://tools.ietf.org/html/rfc7519) containing claims that identify the attested app and GCP project. This token is used to access Google services protected by App Check. These tokens can also be [verified by your own custom backends](https://firebase.google.com/docs/app-check/custom-resource-backend) using the Firebase Admin SDK or third-party libraries. |
| `token` | `string` The App Check token. App Check tokens are signed [JWTs](https://tools.ietf.org/html/rfc7519) containing claims that identify the attested app and GCP project. This token is used to access Google services protected by App Check. These tokens can also be [verified by your own custom backends](https://firebase.google.com/docs/app-check/custom-resource-backend) using the Firebase Admin SDK or third-party libraries. |
| `ttl` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#duration` format)`` The duration from the time this token is minted until its expiration. This field is intended to ease client-side token management, since the client may have clock skew, but is still able to accurately measure a duration. A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. |