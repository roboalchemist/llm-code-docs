# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/jwks/get.md.txt

# Method: jwks.get

Returns a public JWK set as specified by
[RFC 7517](https://tools.ietf.org/html/rfc7517)
that can be used to verify App Check tokens. Exactly one of the public keys in the returned set will successfully validate any App Check token that is currently valid.

### HTTP request


`
GET https://firebaseappcheck.googleapis.com/v1/{name=jwks}
`


The URL uses
[gRPC Transcoding](https://google.aip.dev/127)
syntax.

### Path parameters

| Parameters ||
|---|---|
| ` name ` | ` string ` Required. The relative resource name to the public JWK set. Must always be exactly the string ` jwks ` . |

### Request body


The request body must be empty.

### Response body


If successful, the response body contains an instance of
`
https://firebase.google.com/docs/reference/appcheck/rest/v1/jwks#PublicJwkSet
`
.