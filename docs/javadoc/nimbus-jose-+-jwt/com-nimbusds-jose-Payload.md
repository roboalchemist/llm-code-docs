Package com.nimbusds.jose

# Class Payload

java.lang.Object
com.nimbusds.jose.Payload

All Implemented Interfaces:
`Serializable`

---

@Immutable
public final class Payload
extends Object
implements Serializable
Payload of an unsecured (plain), JSON Web Signature (JWS) or JSON Web
 Encryption (JWE) object. Supports JSON object, string, byte array,
 Base64URL, JWS object and signed JWT payload representations. This class is
 immutable.

 

UTF-8 is the character set for all conversions between strings and byte
 arrays.

 

Conversion relations:

 

```

 JSON object <=> String <=> Base64URL
                        <=> byte[]
                        <=> JWSObject
                        <=> SignedJWT
 
```

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
`Payload.Origin`

Enumeration of the original data types used to create a 
 `Payload`.

- 

## Constructor Summary

Constructors

Constructor
Description
`Payload(byte[] bytes)`

Creates a new payload from the specified byte array.

`Payload(JWSObject jwsObject)`

Creates a new payload from the specified JWS object.

`Payload(Base64URL base64URL)`

Creates a new payload from the specified Base64URL-encoded object.

`Payload(SignedJWT signedJWT)`

Creates a new payload from the specified signed JSON Web Token
 (JWT).

`Payload(String string)`

Creates a new payload from the specified string.

`Payload(Map<String,Object> jsonObject)`

Creates a new payload from the specified JSON object.

- 

## Method Summary

Modifier and Type
Method
Description
`Payload.Origin`
`getOrigin()`

Gets the original data type used to create this payload.

`Base64URL`
`toBase64URL()`

Returns a Base64URL representation of this payload, as required for
 JOSE serialisation (see RFC 7515, section 7).

`byte[]`
`toBytes()`

Returns a byte array representation of this payload.

`Map<String,Object>`
`toJSONObject()`

Returns a JSON object representation of this payload.

`JWSObject`
`toJWSObject()`

Returns a JWS object representation of this payload.

`SignedJWT`
`toSignedJWT()`

Returns a signed JSON Web Token (JWT) representation of this
 payload.

`String`
`toString()`

Returns a string representation of this payload.

`<T> T`
`toType(PayloadTransformer<T> transformer)`

Returns a transformation of this payload.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### Payload

public Payload(Map<String,Object> jsonObject)
Creates a new payload from the specified JSON object.

Parameters:
`jsonObject` - The JSON object representing the payload. Must not
                   be `null`.

  - 

### Payload

public Payload(String string)
Creates a new payload from the specified string.

Parameters:
`string` - The string representing the payload. Must not be 
               `null`.

  - 

### Payload

public Payload(byte[] bytes)
Creates a new payload from the specified byte array.

Parameters:
`bytes` - The byte array representing the payload. Must not be 
              `null`.

  - 

### Payload

public Payload(Base64URL base64URL)
Creates a new payload from the specified Base64URL-encoded object.

Parameters:
`base64URL` - The Base64URL-encoded object representing the 
                  payload. Must not be `null`.

  - 

### Payload

public Payload(JWSObject jwsObject)
Creates a new payload from the specified JWS object. Intended for
 signed then encrypted JOSE objects.

Parameters:
`jwsObject` - The JWS object representing the payload. Must be in
                  a signed state and not `null`.

  - 

### Payload

public Payload(SignedJWT signedJWT)
Creates a new payload from the specified signed JSON Web Token
 (JWT). Intended for signed then encrypted JWTs.

Parameters:
`signedJWT` - The signed JWT representing the payload. Must be in
                  a signed state and not `null`.

- 

## Method Details

  - 

### getOrigin

public Payload.Origin getOrigin()
Gets the original data type used to create this payload.

Returns:
The payload origin.

  - 

### toJSONObject

public Map<String,Object> toJSONObject()
Returns a JSON object representation of this payload.

Returns:
The JSON object representation, `null` if the payload
         couldn't be converted to a JSON object.

  - 

### toString

public String toString()
Returns a string representation of this payload.

Overrides:
`toString` in class `Object`
Returns:
The string representation.

  - 

### toBytes

public byte[] toBytes()
Returns a byte array representation of this payload.

Returns:
The byte array representation.

  - 

### toBase64URL

public Base64URL toBase64URL()
Returns a Base64URL representation of this payload, as required for
 JOSE serialisation (see RFC 7515, section 7).

Returns:
The Base64URL representation.

  - 

### toJWSObject

public JWSObject toJWSObject()
Returns a JWS object representation of this payload. Intended for
 signed then encrypted JOSE objects.

Returns:
The JWS object representation, `null` if the payload
         couldn't be converted to a JWS object.

  - 

### toSignedJWT

public SignedJWT toSignedJWT()
Returns a signed JSON Web Token (JWT) representation of this
 payload. Intended for signed then encrypted JWTs.

Returns:
The signed JWT representation, `null` if the payload
         couldn't be converted to a signed JWT.

  - 

### toType

public <T> T toType(PayloadTransformer<T> transformer)
Returns a transformation of this payload.

Type Parameters:
`T` - Type of the result.
Parameters:
`transformer` - The payload transformer. Must not be
                    `null`.
Returns:
The transformed payload.