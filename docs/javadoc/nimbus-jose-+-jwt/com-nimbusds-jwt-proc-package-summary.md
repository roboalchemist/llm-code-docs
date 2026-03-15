# Package com.nimbusds.jwt.proc

---

package com.nimbusds.jwt.proc

Framework for application-specific verification and decryption of JSON Web
 Tokens (JWTs). Provides a core `interface` for processing signed, encrypted and unsecured (plain) JWTs, with
 a `default implementation`
 which can be configured and extended as required.

 

To process generic JOSE objects refer to the
 `com.nimbusds.jose.proc` package.

 

References:

 

     
- RFC 7519 (JWT)
 

- 

Related Packages

Package
Description
com.nimbusds.jwt

JSON Web Token (JWT) interfaces and classes.

com.nimbusds.jwt.util

JSON Web Token (JWT) utility interfaces and classes.

- 

Class
Description
BadJWTException

Bad JSON Web Token (JWT) exception.

ClockSkewAware

Clock skew aware interface.

ConfigurableJWTProcessor<C extends SecurityContext>

Configurable processor of `unsecured` (plain), `signed` and
 `encrypted` JSON Web Tokens (JWT).

DefaultJWTClaimsVerifier<C extends SecurityContext>

A `JWT claims verifier` implementation.

DefaultJWTProcessor<C extends SecurityContext>

Default processor of `unsecured` (plain),
 `signed` and
 `encrypted` JSON Web Tokens (JWTs).

ExpiredJWTException

Expires JSON Web Token (JWT) exception.

JWTClaimsSetAwareJWSKeySelector<C extends SecurityContext>

Interface for selecting key candidates for processing a signed JWT which
 provides access to the JWT claims set in addition to the JWS header.

JWTClaimsSetVerifier<C extends SecurityContext>

JWT claims set verifier.

JWTProcessor<C extends SecurityContext>

Interface for parsing and processing `unsecured` (plain), `signed` and
 `encrypted` JSON Web Tokens (JWTs).

JWTProcessorConfiguration<C extends SecurityContext>

JWT processor configuration.