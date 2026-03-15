Package com.nimbusds.jose

# Class JWSObjectJSON.Signature

java.lang.Object
com.nimbusds.jose.JWSObjectJSON.Signature

Enclosing class:
JWSObjectJSON

---

@Immutable
public static final class JWSObjectJSON.Signature
extends Object
Individual signature in a JWS secured object serialisable to JSON.

- 

## Method Summary

Modifier and Type
Method
Description
`JWSHeader`
`getHeader()`

Returns the JWS protected header.

`Base64URL`
`getSignature()`

Returns the signature.

`UnprotectedHeader`
`getUnprotectedHeader()`

Returns the unprotected header.

`boolean`
`isVerified()`

Returns `true` if the signature was successfully
 verified with a previous call to `verify(com.nimbusds.jose.JWSVerifier)`.

`JWSObject`
`toJWSObject()`

Returns the compact JWS object representation of this
 individual signature.

`boolean`
`verify(JWSVerifier verifier)`

Checks the signature with the specified verifier.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### getHeader

public JWSHeader getHeader()
Returns the JWS protected header.

Returns:
The JWS protected header, `null` if none.

  - 

### getUnprotectedHeader

public UnprotectedHeader getUnprotectedHeader()
Returns the unprotected header.

Returns:
The unprotected header, `null` if none.

  - 

### getSignature

public Base64URL getSignature()
Returns the signature.

Returns:
The signature.

  - 

### toJWSObject

public JWSObject toJWSObject()
Returns the compact JWS object representation of this
 individual signature.

Returns:
The JWS object serialisable to compact encoding.

  - 

### isVerified

public boolean isVerified()
Returns `true` if the signature was successfully
 verified with a previous call to `verify(com.nimbusds.jose.JWSVerifier)`.

Returns:
`true` if the signature was successfully
         verified, `false` if the signature is invalid
         or `verify(com.nimbusds.jose.JWSVerifier)` was never called.

  - 

### verify

public boolean verify(JWSVerifier verifier)
               throws JOSEException
Checks the signature with the specified verifier.

Parameters:
`verifier` - The JWS verifier. Must not be `null`.
Returns:
`true` if the signature was successfully
         verified, else `false`.
Throws:
`JOSEException` - If the signature verification failed.