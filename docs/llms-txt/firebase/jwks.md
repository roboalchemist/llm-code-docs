# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/jwks.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/jwks.md.txt

# REST Resource: jwks

## Resource: PublicJwkSet

The currently active set of public keys that can be used to verify App Check tokens.

This object is a JWK set as specified by [section 5 of RFC 7517](https://tools.ietf.org/html/rfc7517#section-5).

For security, the response **must not** be cached for longer than six hours.

|                                               JSON representation                                               |
|-----------------------------------------------------------------------------------------------------------------|
| ``` { "keys": [ { object (https://firebase.google.com/docs/reference/appcheck/rest/v1/jwks#PublicJwk) } ] } ``` |

|                                                                                                        Fields                                                                                                        ||
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `keys[]` | `object (`[PublicJwk](https://firebase.google.com/docs/reference/appcheck/rest/v1/jwks#PublicJwk)`)` The set of public keys. See [section 5.1 of RFC 7517](https://tools.ietf.org/html/rfc7517#section-5). |

## PublicJwk

A JWK as specified by [section 4 of RFC 7517](https://tools.ietf.org/html/rfc7517#section-4) and [section 6.3.1 of RFC 7518](https://tools.ietf.org/html/rfc7518#section-6.3.1).

|                                       JSON representation                                        |
|--------------------------------------------------------------------------------------------------|
| ``` { "kty": string, "use": string, "alg": string, "kid": string, "n": string, "e": string } ``` |

|                                                 Fields                                                  ||
|-------|--------------------------------------------------------------------------------------------------|
| `kty` | `string` See [section 4.1 of RFC 7517](https://tools.ietf.org/html/rfc7517#section-4.1).         |
| `use` | `string` See [section 4.2 of RFC 7517](https://tools.ietf.org/html/rfc7517#section-4.2).         |
| `alg` | `string` See [section 4.4 of RFC 7517](https://tools.ietf.org/html/rfc7517#section-4.4).         |
| `kid` | `string` See [section 4.5 of RFC 7517](https://tools.ietf.org/html/rfc7517#section-4.5).         |
| `n`   | `string` See [section 6.3.1.1 of RFC 7518](https://tools.ietf.org/html/rfc7518#section-6.3.1.1). |
| `e`   | `string` See [section 6.3.1.2 of RFC 7518](https://tools.ietf.org/html/rfc7518#section-6.3.1.2). |

|                                                                                                       ## Methods                                                                                                       ||
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| ### [get](https://firebase.google.com/docs/reference/appcheck/rest/v1/jwks/get) | Returns a public JWK set as specified by [RFC 7517](https://tools.ietf.org/html/rfc7517) that can be used to verify App Check tokens. |