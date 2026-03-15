# Package com.nimbusds.jose.jwk

---

package com.nimbusds.jose.jwk

JSON Web Key (JWK) classes.

 

This package provides representation, serialisation and parsing of
 Elliptic Curve (EC), RSA and symmetric JWKs.

 

References:

 

     
- RFC 7517 (JWK)
 

- 

Related Packages

Package
Description
com.nimbusds.jose

Base Javascript Object Signing and Encryption (JOSE) interfaces and classes.

com.nimbusds.jose.jwk.gen

JSON Web Key (JWK) generation utilities.

com.nimbusds.jose.jwk.source

JSON Web Key (JWK) sourcing interface and utilities.

- 

Class
Description
AsymmetricJWK

Asymmetric (pair) JSON Web Key (JWK).

Curve

Cryptographic curve.

CurveBasedJWK

Curve based JSON Web Key (JWK).

ECKey

Public and private `Elliptic Curve` JSON Web Key (JWK).

ECKey.Builder

Builder for constructing Elliptic Curve JWKs.

ECParameterTable

Elliptic curve parameter table.

JWK

The base abstract class for JSON Web Keys (JWKs).

JWKException

JSON Web Key (JWK) related exception.

JWKMatcher

JSON Web Key (JWK) matcher.

JWKMatcher.Builder

Builder for constructing JWK matchers.

JWKParameterNames

JSON Web Key (JWK) parameter names.

JWKSelector

Selects (filters) one or more JSON Web Keys (JWKs) from a JWK set.

JWKSet

JSON Web Key (JWK) set.

KeyConverter

Key converter.

KeyOperation

Enumeration of key operations.

KeyRevocation

Key revocation.

KeyRevocation.Reason

Key revocation reason.

KeyType

Key type.

KeyUse

Enumeration of public key uses.

OctetKeyPair

`Octet key pair` JSON Web Key (JWK), used to represent
 Edwards-curve keys.

OctetKeyPair.Builder

Builder for constructing Octet Key Pair JWKs.

OctetSequenceKey

`Octet sequence` JSON Web Key (JWK), used to represent
 symmetric keys.

OctetSequenceKey.Builder

Builder for constructing octet sequence JWKs.

PasswordLookup

Password lookup interface.

RSAKey

Public and private `RSA` JSON Web Key (JWK).

RSAKey.Builder

Builder for constructing RSA JWKs.

RSAKey.OtherPrimesInfo

Other Primes Info, represents the private `oth` parameter of a
 RSA JWK.

SecretJWK

Secret (symmetric) JSON Web Key (JWK).

ThumbprintURI

JSON Web Key (JWK) thumbprint URI.

ThumbprintUtils

Thumbprint utilities.