# Uses of Class
com.nimbusds.jwt.EncryptedJWT

Packages that use EncryptedJWT

Package
Description
com.nimbusds.jwt

JSON Web Token (JWT) interfaces and classes.

com.nimbusds.jwt.proc

Framework for application-specific verification and decryption of JSON Web
 Tokens (JWTs).

- 

## Uses of EncryptedJWT in com.nimbusds.jwt

Methods in com.nimbusds.jwt that return EncryptedJWT

Modifier and Type
Method
Description
`static EncryptedJWT`
EncryptedJWT.`parse(String s)`

Parses an encrypted JSON Web Token (JWT) from the specified string in
 compact format.

- 

## Uses of EncryptedJWT in com.nimbusds.jwt.proc

Methods in com.nimbusds.jwt.proc with parameters of type EncryptedJWT

Modifier and Type
Method
Description
`JWTClaimsSet`
DefaultJWTProcessor.`process(EncryptedJWT encryptedJWT,
 C context)`
 
`JWTClaimsSet`
JWTProcessor.`process(EncryptedJWT encryptedJWT,
 C context)`

Processes the specified encrypted JWT by decrypting it.