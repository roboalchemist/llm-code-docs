# Package com.nimbusds.jose.proc

---

package com.nimbusds.jose.proc

Framework for application-specific verification and decryption of JOSE
 objects (with arbitrary payloads). Provides a core
 `interface` for processing JWS,
 JWE and unsecured (plain) objects, with a
 `default implementation`
 which can be configured and extended as required.

 

To process JSON Web Tokens (JWT) refer to the
 `com.nimbusds.jwt.proc` package.

- 

Related Packages

Package
Description
com.nimbusds.jose

Base Javascript Object Signing and Encryption (JOSE) interfaces and classes.

- 

Class
Description
BadJOSEException

Bad JSON Object Signing and Encryption (JOSE) exception.

BadJWEException

Bad JSON Web Encryption (JWE) exception.

BadJWSException

Bad JSON Web Signature (JWS) exception.

ConfigurableJOSEProcessor<C extends SecurityContext>

Configurable processor of `unsecured`
 (plain), `JWS` and
 `JWE` objects.

DefaultJOSEObjectTypeVerifier<C extends SecurityContext>

Default JOSE header "typ" (type) parameter verifier.

DefaultJOSEProcessor<C extends SecurityContext>

Default processor of `unsecured`
 (plain), `JWS` and
 `JWE` objects.

JOSEMatcher

JOSE object / header matcher.

JOSEMatcher.Builder

Builder for constructing JOSE matchers.

JOSEObjectTypeVerifier<C extends SecurityContext>

JOSE object type (header "typ" parameter) verifier.

JOSEProcessor<C extends SecurityContext>

Interface for parsing and processing `unsecured` (plain), `JWS` and
 `JWE` objects.

JOSEProcessorConfiguration<C extends SecurityContext>

JOSE processor configuration.

JWEDecrypterFactory

JSON Web Encryption (JWE) decrypter factory.

JWEDecryptionKeySelector<C extends SecurityContext>

Key selector for decrypting JWE objects, where the key candidates are
 retrieved from a `JSON Web Key (JWK) source`.

JWEKeySelector<C extends SecurityContext>

Interface for selecting key candidates for decrypting a JSON Web Encryption
 (JWE) object.

JWKSecurityContext

A security context that contains JSON Web Keys (JWK).

JWSAlgorithmFamilyJWSKeySelector<C extends SecurityContext>

A `JWSKeySelector` that expects an algorithm from a specified
 algorithm family.

JWSKeySelector<C extends SecurityContext>

Interface for selecting key candidates for verifying a JSON Web Signature
 (JWS) object.

JWSVerificationKeySelector<C extends SecurityContext>

Key selector for verifying JWS objects, where the key candidates are
 retrieved from a `JSON Web Key (JWK) source`.

JWSVerifierFactory

JSON Web Signature (JWS) verifier factory.

SecurityContext

Security context.

SimpleSecurityContext

Simple map-based security context.

SingleKeyJWSKeySelector<C extends SecurityContext>

A `JWSKeySelector` that always returns the same `Key`.