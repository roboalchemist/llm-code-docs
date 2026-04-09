Package com.nimbusds.jwt

# Class SignedJWT

java.lang.Object
com.nimbusds.jose.JOSEObject
com.nimbusds.jose.JWSObject
com.nimbusds.jwt.SignedJWT

All Implemented Interfaces:
`JWT`, `Serializable`

---

@ThreadSafe
public class SignedJWT
extends JWSObject
implements JWT
Signed JSON Web Token (JWT).

Version:
2024-06-06
Author:
Vladimir Dzhuvinov
See Also:

- Serialized Form

- 

## Nested Class Summary

## Nested classes/interfaces inherited from class com.nimbusds.jose.JWSObject

`JWSObject.State`

- 

## Field Summary

### Fields inherited from class com.nimbusds.jose.JOSEObject

`MIME_TYPE_COMPACT, MIME_TYPE_JS`

- 

## Constructor Summary

Constructors

Constructor
Description
`SignedJWT(JWSHeader header,
 JWTClaimsSet claimsSet)`

Creates a new to-be-signed JSON Web Token (JWT) with the specified
 header and claims set.

`SignedJWT(Base64URL firstPart,
 Base64URL secondPart,
 Base64URL thirdPart)`

Creates a new signed JSON Web Token (JWT) with the specified 
 serialised parts.

- 

## Method Summary

Modifier and Type
Method
Description
`JWTClaimsSet`
`getJWTClaimsSet()`

Gets the claims set of the JSON Web Token (JWT).

`static SignedJWT`
`parse(String s)`

Parses a signed JSON Web Token (JWT) from the specified string in 
 compact format.

`protected void`
`setPayload(Payload payload)`

Sets the payload of this JOSE object.

### Methods inherited from class com.nimbusds.jose.JWSObject

`getHeader, getSignature, getSigningInput, getState, parse, serialize, serialize, sign, verify`

### Methods inherited from class com.nimbusds.jose.JOSEObject

`getParsedParts, getParsedString, getPayload, setParsedParts, split`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface com.nimbusds.jwt.JWT

`getHeader, getParsedParts, getParsedString, serialize`

- 

## Constructor Details

  - 

### SignedJWT

public SignedJWT(JWSHeader header,
 JWTClaimsSet claimsSet)
Creates a new to-be-signed JSON Web Token (JWT) with the specified
 header and claims set. The initial state will be 
 `unsigned`.

Parameters:
`header` - The JWS header. Must not be `null`.
`claimsSet` - The JWT claims set. Must not be `null`.

  - 

### SignedJWT

public SignedJWT(Base64URL firstPart,
 Base64URL secondPart,
 Base64URL thirdPart)
          throws ParseException
Creates a new signed JSON Web Token (JWT) with the specified 
 serialised parts. The state will be 
 `signed`.

Parameters:
`firstPart` - The first part, corresponding to the JWS header. 
                   Must not be `null`.
`secondPart` - The second part, corresponding to the claims set
                   (payload). Must not be `null`.
`thirdPart` - The third part, corresponding to the signature.
                   Must not be `null`.
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

public static SignedJWT parse(String s)
                       throws ParseException
Parses a signed JSON Web Token (JWT) from the specified string in 
 compact format.

Parameters:
`s` - The string to parse. Must not be `null`.
Returns:
The signed JWT.
Throws:
`ParseException` - If the string couldn't be parsed to a valid 
                        signed JWT.