Package com.nimbusds.jwt

# Interface JWT

All Superinterfaces:
`Serializable`

All Known Implementing Classes:
`EncryptedJWT`, `PlainJWT`, `SignedJWT`

---

public interface JWT
extends Serializable
JSON Web Token (JWT) interface.

Version:
2014-08-19
Author:
Vladimir Dzhuvinov

- 

## Method Summary

Modifier and Type
Method
Description
`Header`
`getHeader()`

Gets the JOSE header of the JSON Web Token (JWT).

`JWTClaimsSet`
`getJWTClaimsSet()`

Gets the claims set of the JSON Web Token (JWT).

`Base64URL[]`
`getParsedParts()`

Gets the original parsed Base64URL parts used to create the JSON Web
 Token (JWT).

`String`
`getParsedString()`

Gets the original parsed string used to create the JSON Web Token 
 (JWT).

`String`
`serialize()`

Serialises the JSON Web Token (JWT) to its compact format consisting 
 of Base64URL-encoded parts delimited by period ('.') characters.

- 

## Method Details

  - 

### getHeader

Header getHeader()
Gets the JOSE header of the JSON Web Token (JWT).

Returns:
The header.

  - 

### getJWTClaimsSet

JWTClaimsSet getJWTClaimsSet()
                      throws ParseException
Gets the claims set of the JSON Web Token (JWT).

Returns:
The claims set, `null` if not available (for an 
         encrypted JWT that isn't decrypted).
Throws:
`ParseException` - If the payload of the JWT doesn't represent a
                        valid JSON object and a JWT claims set.

  - 

### getParsedParts

Base64URL[] getParsedParts()
Gets the original parsed Base64URL parts used to create the JSON Web
 Token (JWT).

Returns:
The original Base64URL parts used to creates the JWT,
         `null` if the JWT was created from scratch. The 
         individual parts may be empty or `null` to indicate a 
         missing part.

  - 

### getParsedString

String getParsedString()
Gets the original parsed string used to create the JSON Web Token 
 (JWT).

Returns:
The parsed string used to create the JWT, `null` if 
         the JWT was created from scratch.
See Also:

    - `getParsedParts()`

  - 

### serialize

String serialize()
Serialises the JSON Web Token (JWT) to its compact format consisting 
 of Base64URL-encoded parts delimited by period ('.') characters.

Returns:
The serialised JWT.
Throws:
`IllegalStateException` - If the JWT is not in a state that 
                               permits serialisation.