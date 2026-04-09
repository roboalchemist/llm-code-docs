Package com.nimbusds.jwt

# Class EncryptedJWT

java.lang.Object
com.nimbusds.jose.JOSEObject
com.nimbusds.jose.JWEObject
com.nimbusds.jwt.EncryptedJWT

All Implemented Interfaces:
`JWT`, `Serializable`

---

@ThreadSafe
public class EncryptedJWT
extends JWEObject
implements JWT
Encrypted JSON Web Token (JWT). This class is thread-safe.

Version:
2024-06-06
Author:
Vladimir Dzhuvinov
See Also:

- Serialized Form

- 

## Nested Class Summary

## Nested classes/interfaces inherited from class com.nimbusds.jose.JWEObject

`JWEObject.State`

- 

## Field Summary

### Fields inherited from class com.nimbusds.jose.JWEObject

`MAX_COMPRESSED_CIPHER_TEXT_LENGTH`

### Fields inherited from class com.nimbusds.jose.JOSEObject

`MIME_TYPE_COMPACT, MIME_TYPE_JS`

- 

## Constructor Summary

Constructors

Constructor
Description
`EncryptedJWT(JWEHeader header,
 JWTClaimsSet claimsSet)`

Creates a new to-be-encrypted JSON Web Token (JWT) with the specified
 header and claims set.

`EncryptedJWT(Base64URL firstPart,
 Base64URL secondPart,
 Base64URL thirdPart,
 Base64URL fourthPart,
 Base64URL fifthPart)`

Creates a new encrypted JSON Web Token (JWT) with the specified 
 serialised parts.

- 

## Method Summary

Modifier and Type
Method
Description
`JWTClaimsSet`
`getJWTClaimsSet()`

Gets the claims set of the JSON Web Token (JWT).

`static EncryptedJWT`
`parse(String s)`

Parses an encrypted JSON Web Token (JWT) from the specified string in
 compact format.

`protected void`
`setPayload(Payload payload)`

Sets the payload of this JOSE object.

### Methods inherited from class com.nimbusds.jose.JWEObject

`decrypt, decrypt, encrypt, getAuthTag, getCipherText, getEncryptedKey, getHeader, getIV, getState, serialize`

### Methods inherited from class com.nimbusds.jose.JOSEObject

`getParsedParts, getParsedString, getPayload, setParsedParts, split`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface com.nimbusds.jwt.JWT

`getHeader, getParsedParts, getParsedString, serialize`

- 

## Constructor Details

  - 

### EncryptedJWT

public EncryptedJWT(JWEHeader header,
 JWTClaimsSet claimsSet)
Creates a new to-be-encrypted JSON Web Token (JWT) with the specified
 header and claims set. The initial state will be 
 `unencrypted`.

Parameters:
`header` - The JWE header. Must not be `null`.
`claimsSet` - The JWT claims set. Must not be `null`.

  - 

### EncryptedJWT

public EncryptedJWT(Base64URL firstPart,
 Base64URL secondPart,
 Base64URL thirdPart,
 Base64URL fourthPart,
 Base64URL fifthPart)
             throws ParseException
Creates a new encrypted JSON Web Token (JWT) with the specified 
 serialised parts. The state will be 
 `encrypted`.

Parameters:
`firstPart` - The first part, corresponding to the JWE header. 
                   Must not be `null`.
`secondPart` - The second part, corresponding to the encrypted 
                   key. Empty or `null` if none.
`thirdPart` - The third part, corresponding to the initialisation
                   vectory. Empty or `null` if none.
`fourthPart` - The fourth part, corresponding to the cipher text.
                   Must not be `null`.
`fifthPart` - The fifth part, corresponding to the integrity
                   value. Empty of `null` if none.
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

public static EncryptedJWT parse(String s)
                          throws ParseException
Parses an encrypted JSON Web Token (JWT) from the specified string in
 compact format.

Parameters:
`s` - The string to parse. Must not be `null`.
Returns:
The encrypted JWT.
Throws:
`ParseException` - If the string couldn't be parsed to a valid 
                        encrypted JWT.