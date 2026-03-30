Package com.nimbusds.jose

# Class JWSObject

java.lang.Object
com.nimbusds.jose.JOSEObject
com.nimbusds.jose.JWSObject

All Implemented Interfaces:
`Serializable`

Direct Known Subclasses:
`SignedJWT`

---

@ThreadSafe
public class JWSObject
extends JOSEObject
JSON Web Signature (JWS) secured object with
 compact
 serialisation.

 

This class is thread-safe.

Version:
2024-04-20
Author:
Vladimir Dzhuvinov
See Also:

- Serialized Form

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static enum `
`JWSObject.State`

Enumeration of the states of a JSON Web Signature (JWS) secured
 object.

- 

## Field Summary

### Fields inherited from class com.nimbusds.jose.JOSEObject

`MIME_TYPE_COMPACT, MIME_TYPE_JS`

- 

## Constructor Summary

Constructors

Constructor
Description
`JWSObject(JWSHeader header,
 Payload payload)`

Creates a new to-be-signed JSON Web Signature (JWS) object with the 
 specified header and payload.

`JWSObject(Base64URL firstPart,
 Payload payload,
 Base64URL thirdPart)`

Creates a new signed JSON Web Signature (JWS) object with the
 specified serialised parts and payload which can be optionally
 unencoded (RFC 7797).

`JWSObject(Base64URL firstPart,
 Base64URL secondPart,
 Base64URL thirdPart)`

Creates a new signed JSON Web Signature (JWS) object with the
 specified serialised parts.

- 

## Method Summary

Modifier and Type
Method
Description
`JWSHeader`
`getHeader()`

Returns the header of this JOSE object.

`Base64URL`
`getSignature()`

Returns the signature of this JWS object.

`byte[]`
`getSigningInput()`

Returns the signing input for this JWS object.

`JWSObject.State`
`getState()`

Returns the state of the JWS secured object.

`static JWSObject`
`parse(String s)`

Parses a JWS object from the specified string in compact format.

`static JWSObject`
`parse(String s,
 Payload detachedPayload)`

Parses a JWS object from the specified string in compact format and
 a detached payload which can be optionally unencoded (RFC 7797).

`String`
`serialize()`

Serialises this JWS object to its compact format consisting of 
 Base64URL-encoded parts delimited by period ('.') characters.

`String`
`serialize(boolean detachedPayload)`

Serialises this JWS object to its compact format consisting of
 Base64URL-encoded parts delimited by period ('.') characters.

`void`
`sign(JWSSigner signer)`

Signs this JWS object with the specified signer.

`boolean`
`verify(JWSVerifier verifier)`

Checks the signature of this JWS object with the specified verifier.

### Methods inherited from class com.nimbusds.jose.JOSEObject

`getParsedParts, getParsedString, getPayload, setParsedParts, setPayload, split`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### JWSObject

public JWSObject(JWSHeader header,
 Payload payload)
Creates a new to-be-signed JSON Web Signature (JWS) object with the 
 specified header and payload. The initial state will be 
 `unsigned`.

Parameters:
`header` - The JWS header. Must not be `null`.
`payload` - The payload. Must not be `null`.

  - 

### JWSObject

public JWSObject(Base64URL firstPart,
 Base64URL secondPart,
 Base64URL thirdPart)
          throws ParseException
Creates a new signed JSON Web Signature (JWS) object with the
 specified serialised parts. The state will be
 `signed`.

Parameters:
`firstPart` - The first part, corresponding to the JWS header.
                   Must not be `null`.
`secondPart` - The second part, corresponding to the payload.
                   Must not be `null`.
`thirdPart` - The third part, corresponding to the signature.
                   Must not be `null`.
Throws:
`ParseException` - If parsing of the serialised parts failed.

  - 

### JWSObject

public JWSObject(Base64URL firstPart,
 Payload payload,
 Base64URL thirdPart)
          throws ParseException
Creates a new signed JSON Web Signature (JWS) object with the
 specified serialised parts and payload which can be optionally
 unencoded (RFC 7797). The state will be `signed`.

Parameters:
`firstPart` - The first part, corresponding to the JWS header.
                  Must not be `null`.
`payload` - The payload. Must not be `null`.
`thirdPart` - The third part, corresponding to the signature.
                  Must not be `null`.
Throws:
`ParseException` - If parsing of the serialised parts failed.

- 

## Method Details

  - 

### getHeader

public JWSHeader getHeader()
Description copied from class: `JOSEObject`
Returns the header of this JOSE object.

Specified by:
`getHeader` in class `JOSEObject`
Returns:
The header.

  - 

### getSigningInput

public byte[] getSigningInput()
Returns the signing input for this JWS object.

Returns:
The signing input, to be passed to a JWS signer or verifier.

  - 

### getSignature

public Base64URL getSignature()
Returns the signature of this JWS object.

Returns:
The signature, `null` if the JWS object is not signed 
         yet.

  - 

### getState

public JWSObject.State getState()
Returns the state of the JWS secured object.

Returns:
The state.

  - 

### sign

public void sign(JWSSigner signer)
          throws JOSEException
Signs this JWS object with the specified signer. The JWS object must
 be in a `unsigned` state.

Parameters:
`signer` - The JWS signer. Must not be `null`.
Throws:
`IllegalStateException` - If the JWS object is not in an 
                               `unsigned state`.
`JOSEException` - If the JWS object couldn't be signed.

  - 

### verify

public boolean verify(JWSVerifier verifier)
               throws JOSEException
Checks the signature of this JWS object with the specified verifier.
 The JWS object must be in a `signed` state.

Parameters:
`verifier` - The JWS verifier. Must not be `null`.
Returns:
`true` if the signature was successfully verified,
         else `false`.
Throws:
`IllegalStateException` - If the JWS object is not in a
                               `signed` or
                               `verified state`.
`JOSEException` - If the JWS object couldn't be
                               verified.

  - 

### serialize

public String serialize()
Serialises this JWS object to its compact format consisting of 
 Base64URL-encoded parts delimited by period ('.') characters. It 
 must be in a `signed` or 
 `verified` state.

 

```

 [header-base64url].[payload-base64url].[signature-base64url]
 
```

Specified by:
`serialize` in class `JOSEObject`
Returns:
The serialised JWS object.
Throws:
`IllegalStateException` - If the JWS object is not in a 
                               `signed` or
                               `verified` state.

  - 

### serialize

public String serialize(boolean detachedPayload)
Serialises this JWS object to its compact format consisting of
 Base64URL-encoded parts delimited by period ('.') characters. It
 must be in a `signed` or
 `verified` state.

Parameters:
`detachedPayload` - `true` to return a serialised object
                        with a detached payload compliant with RFC
                        7797, `false` for regular JWS
                        serialisation.
Returns:
The serialised JOSE object.
Throws:
`IllegalStateException` - If the JOSE object is not in a state
                               that permits serialisation.

  - 

### parse

public static JWSObject parse(String s)
                       throws ParseException
Parses a JWS object from the specified string in compact format. The
 parsed JWS object will be given a `JWSObject.State.SIGNED` state.

Parameters:
`s` - The JWS string to parse. Must not be `null`.
Returns:
The JWS object.
Throws:
`ParseException` - If the string couldn't be parsed to a JWS
                        object.

  - 

### parse

public static JWSObject parse(String s,
 Payload detachedPayload)
                       throws ParseException
Parses a JWS object from the specified string in compact format and
 a detached payload which can be optionally unencoded (RFC 7797). The
 parsed JWS object will be given a `JWSObject.State.SIGNED` state.

Parameters:
`s` - The JWS string to parse for a detached
                        payload. Must not be `null`.
`detachedPayload` - The detached payload, optionally unencoded
                        (RFC 7797). Must not be `null`.
Returns:
The JWS object.
Throws:
`ParseException` - If the string couldn't be parsed to a JWS
                        object.