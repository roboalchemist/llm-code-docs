# Package com.nimbusds.jwt

---

package com.nimbusds.jwt

JSON Web Token (JWT) interfaces and classes.

 

This package provides representation, compact serialisation and parsing 
 for the following JWT objects:

 

     
- `Unsecured (plain) JWTs`.
     
- `Signed JWTs`.
     
- `Encrypted JWTs`.
 

 

References:

 

     
- RFC 7519 (JWT)
 

- 

Related Packages

Package
Description
com.nimbusds.jwt.proc

Framework for application-specific verification and decryption of JSON Web
 Tokens (JWTs).

com.nimbusds.jwt.util

JSON Web Token (JWT) utility interfaces and classes.

- 

Class
Description
EncryptedJWT

Encrypted JSON Web Token (JWT).

JWT

JSON Web Token (JWT) interface.

JWTClaimNames

JSON Web Token (JWT) claim names.

JWTClaimsSet

JSON Web Token (JWT) claims set.

JWTClaimsSet.Builder

Builder for constructing JSON Web Token (JWT) claims sets.

JWTClaimsSetTransformer<T>

Generic JWT claims set type transformer.

JWTParser

Parser for unsecured (plain), signed and encrypted JSON Web Tokens (JWTs).

PlainJWT

Unsecured (plain) JSON Web Token (JWT).

SignedJWT

Signed JSON Web Token (JWT).