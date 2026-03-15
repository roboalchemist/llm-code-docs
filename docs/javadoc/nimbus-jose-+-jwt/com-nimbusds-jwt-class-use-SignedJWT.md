# Uses of Class
com.nimbusds.jwt.SignedJWT

Packages that use SignedJWT

Package
Description
com.nimbusds.jose

Base Javascript Object Signing and Encryption (JOSE) interfaces and classes.

com.nimbusds.jwt

JSON Web Token (JWT) interfaces and classes.

com.nimbusds.jwt.proc

Framework for application-specific verification and decryption of JSON Web
 Tokens (JWTs).

- 

## Uses of SignedJWT in com.nimbusds.jose

Methods in com.nimbusds.jose that return SignedJWT

Modifier and Type
Method
Description
`SignedJWT`
Payload.`toSignedJWT()`

Returns a signed JSON Web Token (JWT) representation of this
 payload.

Constructors in com.nimbusds.jose with parameters of type SignedJWT

Modifier
Constructor
Description
` `
`Payload(SignedJWT signedJWT)`

Creates a new payload from the specified signed JSON Web Token
 (JWT).

- 

## Uses of SignedJWT in com.nimbusds.jwt

Methods in com.nimbusds.jwt that return SignedJWT

Modifier and Type
Method
Description
`static SignedJWT`
SignedJWT.`parse(String s)`

Parses a signed JSON Web Token (JWT) from the specified string in 
 compact format.

- 

## Uses of SignedJWT in com.nimbusds.jwt.proc

Methods in com.nimbusds.jwt.proc with parameters of type SignedJWT

Modifier and Type
Method
Description
`JWTClaimsSet`
DefaultJWTProcessor.`process(SignedJWT signedJWT,
 C context)`
 
`JWTClaimsSet`
JWTProcessor.`process(SignedJWT signedJWT,
 C context)`

Processes the specified signed JWT by verifying its signature.