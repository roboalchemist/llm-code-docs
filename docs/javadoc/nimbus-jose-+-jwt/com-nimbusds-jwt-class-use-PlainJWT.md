# Uses of Class
com.nimbusds.jwt.PlainJWT

Packages that use PlainJWT

Package
Description
com.nimbusds.jwt

JSON Web Token (JWT) interfaces and classes.

com.nimbusds.jwt.proc

Framework for application-specific verification and decryption of JSON Web
 Tokens (JWTs).

- 

## Uses of PlainJWT in com.nimbusds.jwt

Methods in com.nimbusds.jwt that return PlainJWT

Modifier and Type
Method
Description
`static PlainJWT`
PlainJWT.`parse(String s)`

Parses an unsecured (plain) JSON Web Token (JWT) from the specified
 string in compact format.

- 

## Uses of PlainJWT in com.nimbusds.jwt.proc

Methods in com.nimbusds.jwt.proc with parameters of type PlainJWT

Modifier and Type
Method
Description
`JWTClaimsSet`
DefaultJWTProcessor.`process(PlainJWT plainJWT,
 C context)`
 
`JWTClaimsSet`
JWTProcessor.`process(PlainJWT plainJWT,
 C context)`

Processes the specified unsecured (plain) JWT, typically by checking
 its context.