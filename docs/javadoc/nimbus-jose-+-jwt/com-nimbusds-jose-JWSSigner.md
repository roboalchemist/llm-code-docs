Package com.nimbusds.jose

# Interface JWSSigner

All Superinterfaces:
`JCAAware<JCAContext>`, `JOSEProvider`, `JWSProvider`

All Known Implementing Classes:
`ECDSASigner`, `Ed25519Signer`, `MACSigner`, `RSASSASigner`

---

public interface JWSSigner
extends JWSProvider
JSON Web Signature (JWS) signer.

Version:
2015-04-21
Author:
Vladimir Dzhuvinov

- 

## Method Summary

Modifier and Type
Method
Description
`Base64URL`
`sign(JWSHeader header,
 byte[] signingInput)`

Signs the specified `input` of a 
 `JWS object`.

### Methods inherited from interface com.nimbusds.jose.jca.JCAAware

`getJCAContext`

### Methods inherited from interface com.nimbusds.jose.JWSProvider

`supportedJWSAlgorithms`

- 

## Method Details

  - 

### sign

Base64URL sign(JWSHeader header,
 byte[] signingInput)
        throws JOSEException
Signs the specified `input` of a 
 `JWS object`.

Parameters:
`header` - The JSON Web Signature (JWS) header. Must 
                     specify a supported JWS algorithm and must not 
                     be `null`.
`signingInput` - The input to sign. Must not be `null`.
Returns:
The resulting signature part (third part) of the JWS object.
Throws:
`JOSEException` - If the JWS algorithm is not supported, if a
                       critical header parameter is not supported or
                       marked for deferral to the application, or if
                       signing failed for some other internal reason.