# Source: https://grafbase.com/docs/gateway/configuration/message-signatures.md

# Source: https://grafbase.com/docs/gateway/security/message-signatures.md

# Source: https://grafbase.com/docs/gateway/configuration/message-signatures.md

# Source: https://grafbase.com/docs/gateway/security/message-signatures.md

# Source: https://grafbase.com/docs/gateway/configuration/message-signatures.md

# Source: https://grafbase.com/docs/gateway/security/message-signatures.md

# Source: https://grafbase.com/docs/gateway/configuration/message-signatures.md

# Source: https://grafbase.com/docs/gateway/security/message-signatures.md

# Source: https://grafbase.com/docs/gateway/configuration/message-signatures.md

# Source: https://grafbase.com/docs/gateway/security/message-signatures.md

# Message Signatures

The Grafbase Gateway can sign subgraph HTTP requests following [RFC 9421][rfc9421]. Read more on [configuring message signatures][config].

## Keys

A key file should be provided in the config. This key file should be one of:

1. A JSON file containing a JWK.
2. A PEM file containing a PKCS#8 private key.

### Algorithms

We'll choose which algorithm to use based on the key file provided, but a
specific algoithm can be provided in the configuration.

The available algorithms are:

- `hmac-sha256`
- `ed25519`
- `ecdsa-p256-sha256`
- `ecdsa-p384-sha384`

If the provided key & algorithm don't match the gateway will refuse to start.

The algorithm you use for singing can have an impact on the latency of your
subgraph requests. The list above is in performance order, from most
performant to least performant. We recommend testing your chosen algorithm &
settings if this is a concern - a message signing span will be output in
tracing that can be used to determine the impact of your settings.

## Controlling Signing

The Grafbase Gateway allows you to control which parts of a subgrah request are
used as input to message signing. There are several settings for this:

- The `headers` key can control which headers are included or excluded. It has
  two sub-keys:
  1. `include` should be a list of headers to include in the signature.
     If not present, all headers will be included.
  2. `exclude` should be a list of headers to exclude from the signature.
     This setting takes precedence over `include`
- The `derived_components` key allows you to control which "derived
  components" are included. This defaults to `["request_target"]`. The
  following options are available:
  - `method` the HTTP method.
  - `target_uri` the full URL of the request
  - `authority` the hostname of the requests target URL
  - `scheme` the scheme of the requests target URL
  - `request_target` the [request target][request-target] of the request.
  - `path` the absolute path of the request URL
- The `signature_parameters` key is a list of additional signature parameters
  to include. It currently only has one setting:
  - `nonce` can be provided to include a random nonce in every requests
    signature.
- `expiry` can be set to a duration string. (e.g. `"30s"` for 30 seconds). If
  provided, signatures will expire after this duration.

Here is an example of these settings:

[config]: /docs/gateway/configuration/message-signatures
[rfc9421]: https://datatracker.ietf.org/doc/html/rfc9421
[request-target]: https://datatracker.ietf.org/doc/html/rfc9421#name-request-target