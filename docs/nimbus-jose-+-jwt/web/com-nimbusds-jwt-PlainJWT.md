Package com.nimbusds.jwt

# Class PlainJWT

java.lang.Object
com.nimbusds.jose.JOSEObject
com.nimbusds.jose.PlainObject
com.nimbusds.jwt.PlainJWT

All Implemented Interfaces:
`JWT`, `Serializable`

---

@ThreadSafe
public class PlainJWT
extends PlainObject
implements JWT
Unsecured (plain) JSON Web Token (JWT).

Version:
2024-06-06
Author:
Vladimir Dzhuvinov
See Also:

- Serialized Form

- 

## Field Summary

### Fields inherited from class com.nimbusds.jose.JOSEObject

`MIME_TYPE_COMPACT, MIME_TYPE_JS`

- 

## Constructor Summary

Constructors

Constructor
Description
`PlainJWT(PlainHeader header,
 JWTClaimsSet claimsSet)`

Creates a new unsecured (plain) JSON Web Token (JWT) with the
 specified header and claims set.

`PlainJWT(Base64URL firstPart,
 Base64URL secondPart)`

Creates a new unsecured (plain) JSON Web Token (JWT) with the
 specified Base64URL-encoded parts.

`PlainJWT(JWTClaimsSet claimsSet)`

Creates a new unsecured (plain) JSON Web Token (JWT) with a default
 `PlainHeader` and the specified claims 
 set.

- 

## Method Summary

Modifier and Type
Method
Description
`JWTClaimsSet`
`getJWTClaimsSet()`

Gets the claims set of the JSON Web Token (JWT).

`static PlainJWT`
`parse(String s)`

Parses an unsecured (plain) JSON Web Token (JWT) from the specified
 string in compact format.

`protected void`
`setPayload(Payload payload)`

Sets the payload of this JOSE object.

### Methods inherited from class com.nimbusds.jose.PlainObject

`getHeader, serialize`

### Methods inherited from class com.nimbusds.jose.JOSEObject

`getParsedParts, getParsedString, getPayload, setParsedParts, split`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface com.nimbusds.jwt.JWT

`getHeader, getParsedParts, getParsedString, serialize`

- 

## Constructor Details

  - 

### PlainJWT

public PlainJWT(JWTClaimsSet claimsSet)
Creates a new unsecured (plain) JSON Web Token (JWT) with a default
 `PlainHeader` and the specified claims 
 set.

Parameters:
`claimsSet` - The JWT claims set. Must not be `null`.

  - 

### PlainJWT

public PlainJWT(PlainHeader header,
 JWTClaimsSet claimsSet)
Creates a new unsecured (plain) JSON Web Token (JWT) with the
 specified header and claims set.

Parameters:
`header` - The unsecured header. Must not be `null`.
`claimsSet` - The JWT claims set. Must not be `null`.

  - 

### PlainJWT

public PlainJWT(Base64URL firstPart,
 Base64URL secondPart)
         throws ParseException
Creates a new unsecured (plain) JSON Web Token (JWT) with the
 specified Base64URL-encoded parts.

Parameters:
`firstPart` - The first part, corresponding to the unsecured
                   header. Must not be `null`.
`secondPart` - The second part, corresponding to the claims set 
                   (payload). Must not be `null`.
Throws:
`ParseException` - If parsing of the serialised parts failed.

- 

## Method Details

  - 

### getJWTClaimsSet

public JWTClaimsSet getJWTClaimsSet()
                             throws ParseException
Description copied from interface: `JWT`
Gets the claims set of the JSON Web Token (JWT).

Specified by:
`getJWTClaimsSet` in interface `JWT`
Returns:
The claims set, `null` if not available (for an 
         encrypted JWT that isn't decrypted).
Throws:
`ParseException` - If the payload of the JWT doesn't represent a
                        valid JSON object and a JWT claims set.

  - 

### setPayload

protected void setPayload(Payload payload)
Description copied from class: `JOSEObject`
Sets the payload of this JOSE object.

Overrides:
`setPayload` in class `JOSEObject`
Parameters:
`payload` - The payload, `null` if not available (e.g. for 
                an encrypted JWE object).

  - 

### parse

public static PlainJWT parse(String s)
                      throws ParseException
Parses an unsecured (plain) JSON Web Token (JWT) from the specified
 string in compact format.

Parameters:
`s` - The string to parse. Must not be `null`.
Returns:
The unsecured JWT.
Throws:
`ParseException` - If the string couldn't be parsed to a valid 
                        unsecured JWT.