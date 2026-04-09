# Uses of Interface
com.nimbusds.jwt.JWT

Packages that use JWT

Package
Description
com.nimbusds.jwt

JSON Web Token (JWT) interfaces and classes.

com.nimbusds.jwt.proc

Framework for application-specific verification and decryption of JSON Web
 Tokens (JWTs).

- 

## Uses of JWT in com.nimbusds.jwt

Classes in com.nimbusds.jwt that implement JWT

Modifier and Type
Class
Description
`class `
`EncryptedJWT`

Encrypted JSON Web Token (JWT).

`class `
`PlainJWT`

Unsecured (plain) JSON Web Token (JWT).

`class `
`SignedJWT`

Signed JSON Web Token (JWT).

Methods in com.nimbusds.jwt that return JWT

Modifier and Type
Method
Description
`static JWT`
JWTParser.`parse(String s)`

Parses an unsecured (plain), signed or encrypted JSON Web Token
 (JWT) from the specified string in compact format.

- 

## Uses of JWT in com.nimbusds.jwt.proc

Methods in com.nimbusds.jwt.proc with parameters of type JWT

Modifier and Type
Method
Description
`protected JWTClaimsSet`
DefaultJWTProcessor.`extractJWTClaimsSet(JWT jwt)`

Extracts the claims set from the specified JWT.

`JWTClaimsSet`
DefaultJWTProcessor.`process(JWT jwt,
 C context)`
 
`JWTClaimsSet`
JWTProcessor.`process(JWT jwt,
 C context)`

Processes the specified JWT (unsecured, signed or encrypted).