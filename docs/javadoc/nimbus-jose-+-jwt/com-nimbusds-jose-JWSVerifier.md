Package com.nimbusds.jose

# Interface JWSVerifier

All Superinterfaces:
`JCAAware<JCAContext>`, `JOSEProvider`, `JWSProvider`

All Known Implementing Classes:
`ECDSAVerifier`, `Ed25519Verifier`, `MACVerifier`, `RSASSAVerifier`

---

public interface JWSVerifier
extends JWSProvider
JSON Web Signature (JWS) verifier.

Version:
2015-04-21
Author:
Vladimir Dzhuvinov

- 

## Method Summary

Modifier and Type
Method
Description
`boolean`
`verify(JWSHeader header,
 byte[] signingInput,
 Base64URL signature)`

Verifies the specified `signature` of a
 `JWS object`.

### Methods inherited from interface com.nimbusds.jose.jca.JCAAware

`getJCAContext`

### Methods inherited from interface com.nimbusds.jose.JWSProvider

`supportedJWSAlgorithms`

- 

## Method Details

  - 

### verify

boolean verify(JWSHeader header,
 byte[] signingInput,
 Base64URL signature)
        throws JOSEException
Verifies the specified `signature` of a
 `JWS object`.

Parameters:
`header` - The JSON Web Signature (JWS) header. Must
                     specify a supported JWS algorithm and must not
                     be `null`.
`signingInput` - The signing input. Must not be `null`.
`signature` - The signature part of the JWS object. Must not
                     be `null`.
Returns:
`true` if the signature was successfully verified, 
         `false` if the signature is invalid or if a critical
         header is neither supported nor marked for deferral to the
         application.
Throws:
`JOSEException` - If the JWS algorithm is not supported, or if
                       signature verification failed for some other
                       internal reason.