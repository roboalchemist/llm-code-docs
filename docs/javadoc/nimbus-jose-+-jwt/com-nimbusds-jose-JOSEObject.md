Package com.nimbusds.jose

# Class JOSEObject

java.lang.Object
com.nimbusds.jose.JOSEObject

All Implemented Interfaces:
`Serializable`

Direct Known Subclasses:
`JWEObject`, `JWSObject`, `PlainObject`

---

public abstract class JOSEObject
extends Object
implements Serializable
The base abstract class for JSON Web Signature (JWS) secured, JSON Web
 Encryption (JWE) secured and unsecured (plain / `alg=none`) objects
 serialisable to compact encoding.

Version:
2021-10-05
Author:
Vladimir Dzhuvinov
See Also:

- Serialized Form

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`MIME_TYPE_COMPACT`

The MIME type of JOSE objects serialised to compact encoding:
 `application/jose; charset=UTF-8`

`static final String`
`MIME_TYPE_JS`

Deprecated.
Use `JOSEObjectJSON.MIME_TYPE_JOSE_JSON` instead.

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
`protected `
`JOSEObject()`

Creates a new JOSE object.

`protected `
`JOSEObject(Payload payload)`

Creates a new JOSE object with the specified payload.

- 

## Method Summary

Modifier and Type
Method
Description
`abstract Header`
`getHeader()`

Returns the header of this JOSE object.

`Base64URL[]`
`getParsedParts()`

Returns the original parsed Base64URL parts used to create this JOSE
 object.

`String`
`getParsedString()`

Returns the original parsed string used to create this JOSE object.

`Payload`
`getPayload()`

Returns the payload of this JOSE object.

`static JOSEObject`
`parse(String s)`

Parses a JOSE object from the specified string in compact encoding.

`abstract String`
`serialize()`

Serialises this JOSE object to compact encoding consisting of
 Base64URL-encoded parts delimited by period ('.') characters.

`protected void`
`setParsedParts(Base64URL... parts)`

Sets the original parsed Base64URL parts used to create this JOSE 
 object.

`protected void`
`setPayload(Payload payload)`

Sets the payload of this JOSE object.

`static Base64URL[]`
`split(String s)`

Splits a compact serialised JOSE object into its Base64URL-encoded
 parts.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### MIME_TYPE_COMPACT

public static final String MIME_TYPE_COMPACT
The MIME type of JOSE objects serialised to compact encoding:
 `application/jose; charset=UTF-8`

See Also:

    - Constant Field Values

  - 

### MIME_TYPE_JS

@Deprecated
public static final String MIME_TYPE_JS
Deprecated.
Use `JOSEObjectJSON.MIME_TYPE_JOSE_JSON` instead.

The MIME type of JOSE objects serialised to JSON:
 `application/jose+json; charset=UTF-8`

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### JOSEObject

protected JOSEObject()
Creates a new JOSE object. The payload and the original parsed 
 Base64URL parts are not defined.

  - 

### JOSEObject

protected JOSEObject(Payload payload)
Creates a new JOSE object with the specified payload.

Parameters:
`payload` - The payload, `null` if not available (e.g. for
                an encrypted JWE object).

- 

## Method Details

  - 

### getHeader

public abstract Header getHeader()
Returns the header of this JOSE object.

Returns:
The header.

  - 

### setPayload

protected void setPayload(Payload payload)
Sets the payload of this JOSE object.

Parameters:
`payload` - The payload, `null` if not available (e.g. for 
                an encrypted JWE object).

  - 

### getPayload

public Payload getPayload()
Returns the payload of this JOSE object.

Returns:
The payload, `null` if not available (for an encrypted
         JWE object that hasn't been decrypted).

  - 

### setParsedParts

protected void setParsedParts(Base64URL... parts)
Sets the original parsed Base64URL parts used to create this JOSE 
 object.

Parameters:
`parts` - The original Base64URL parts used to create this JOSE
              object, `null` if the object was created from
              scratch. The individual parts may be empty or 
              `null` to indicate a missing part.

  - 

### getParsedParts

public Base64URL[] getParsedParts()
Returns the original parsed Base64URL parts used to create this JOSE
 object.

Returns:
The original Base64URL parts used to create this JOSE
         object, `null` if the object was created from scratch. 
         The individual parts may be empty or `null` to 
         indicate a missing part.

  - 

### getParsedString

public String getParsedString()
Returns the original parsed string used to create this JOSE object.

Returns:
The parsed string used to create this JOSE object, 
         `null` if the object was creates from scratch.
See Also:

    - `getParsedParts()`

  - 

### serialize

public abstract String serialize()
Serialises this JOSE object to compact encoding consisting of
 Base64URL-encoded parts delimited by period ('.') characters.

Returns:
The serialised JOSE object.
Throws:
`IllegalStateException` - If the JOSE object is not in a state 
                               that permits serialisation.

  - 

### split

public static Base64URL[] split(String s)
                         throws ParseException
Splits a compact serialised JOSE object into its Base64URL-encoded
 parts.

Parameters:
`s` - The compact serialised JOSE object to split. Must not be
          `null`.
Returns:
The JOSE Base64URL-encoded parts (three for unsecured and
         JWS objects, five for JWE objects).
Throws:
`ParseException` - If the specified string couldn't be split 
                        into three or five Base64URL-encoded parts.

  - 

### parse

public static JOSEObject parse(String s)
                        throws ParseException
Parses a JOSE object from the specified string in compact encoding.

Parameters:
`s` - The string to parse. Must not be `null`.
Returns:
The corresponding `JWSObject`, `JWEObject` or
         `PlainObject`.
Throws:
`ParseException` - If the string couldn't be parsed to a valid 
                        JWS, JWE or unsecured object.