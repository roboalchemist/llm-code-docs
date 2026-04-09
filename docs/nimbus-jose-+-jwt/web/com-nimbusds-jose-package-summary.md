# Package com.nimbusds.jose

---

package com.nimbusds.jose

Base Javascript Object Signing and Encryption (JOSE) interfaces and classes.

 

This package provides representation, compact serialisation and parsing 
 for the following JOSE objects:

 

     
- `Unsecured (alg=none) JOSE
         objects`.
     
- `JSON Web Signature (JWS) 
         objects`.
     
- `JSON Web Encryption (JWE) 
         objects`.
 

 

References:

 

     
- RFC 7515 (JWS)
     
- RFC 7516 (JWE)
 

- 

Related Packages

Package
Description
com.nimbusds.jose.crypto

Implementations of standard Javascript Object Signing and Encryption (JOSE)
 algorithms.

com.nimbusds.jose.jca

Java Cryptography Architecture (JCA) context interfaces and classes.

com.nimbusds.jose.jwk

JSON Web Key (JWK) classes.

com.nimbusds.jose.mint

JSON Web Signature (JWS) minting framework.

com.nimbusds.jose.proc

Framework for application-specific verification and decryption of JOSE
 objects (with arbitrary payloads).

com.nimbusds.jose.produce

Framework for producing JOSE objects (with arbitrary payloads).

com.nimbusds.jose.util

Utility interfaces and classes.

- 

Class
Description
ActionRequiredForJWSCompletionException

Action required for JWS completion.

Algorithm

The base class for algorithm names, with optional implementation 
 requirement.

CompletableJWSObjectSigning

Completable JSON Web Signature (JWS) object signing.

CompressionAlgorithm

Compression algorithm name, represents the `zip` header parameter in 
 JSON Web Encryption (JWE) objects.

CriticalHeaderParamsAware

JSON Web Signature (JWS) verifier or JSON Web Encryption (JWE) decrypter
 that supports processing and / or deferral of critical (`crit`) header
 parameters.

EncryptionMethod

Encryption method name, represents the `enc` header parameter in JSON
 Web Encryption (JWE) objects.

EncryptionMethod.Family

Encryption method family.

Header

The base abstract class for unsecured (`alg=none`), JSON Web Signature
 (JWS) and JSON Web Encryption (JWE) headers.

HeaderParameterNames

JSON Web Signature (JWS) and JSON Web Encryption (JWE) header parameter
 names.

JOSEException

Javascript Object Signing and Encryption (JOSE) exception.

JOSEObject

The base abstract class for JSON Web Signature (JWS) secured, JSON Web
 Encryption (JWE) secured and unsecured (plain / `alg=none`) objects
 serialisable to compact encoding.

JOSEObjectJSON

The base abstract class for JSON Web Signature (JWS) secured and JSON Web
 Encryption (JWE) secured objects serialisable to JSON.

JOSEObjectType

JOSE object type, represents the `typ` header parameter in unsecured,
 JSON Web Signature (JWS) and JSON Web Encryption (JWE) objects.

JOSEProvider

JavaScript Object Signing and Encryption (JOSE) provider.

JSONSerializable

Provides JSON serialization of the JOSE Object.

JWEAlgorithm

JSON Web Encryption (JWE) algorithm name, represents the `alg` header 
 parameter in JWE objects.

JWEAlgorithm.Family

JWE algorithm family.

JWECryptoParts

The cryptographic parts of a JSON Web Encryption (JWE) object.

JWEDecrypter

JSON Web Encryption (JWE) decrypter.

JWEDecrypterOption

Marker interface for a JSON Web Encryption (JWE) decrypter option.

JWEEncrypter

JSON Web Encryption (JWE) encrypter.

JWEEncrypterOption

Marker interface for a JSON Web Encryption (JWE) encrypter option.

JWEHeader

JSON Web Encryption (JWE) header.

JWEHeader.Builder

Builder for constructing JSON Web Encryption (JWE) headers.

JWEObject

JSON Web Encryption (JWE) secured object with
 compact
 serialisation.

JWEObject.State

Enumeration of the states of a JSON Web Encryption (JWE) secured
 object.

JWEObjectJSON

JSON Web Encryption (JWE) secured object with
 JSON
 serialisation.

JWEObjectJSON.Recipient

Individual recipient in a JWE object serialisable to JSON.

JWEProvider

JSON Web Encryption (JWE) provider.

JWSAlgorithm

JSON Web Signature (JWS) algorithm name, represents the `alg` header
 parameter in JWS objects.

JWSAlgorithm.Family

JWS algorithm family.

JWSHeader

JSON Web Signature (JWS) header.

JWSHeader.Builder

Builder for constructing JSON Web Signature (JWS) headers.

JWSObject

JSON Web Signature (JWS) secured object with
 compact
 serialisation.

JWSObject.State

Enumeration of the states of a JSON Web Signature (JWS) secured
 object.

JWSObjectJSON

JSON Web Signature (JWS) secured object with
 JSON
 serialisation.

JWSObjectJSON.Signature

Individual signature in a JWS secured object serialisable to JSON.

JWSObjectJSON.State

Enumeration of the states of a JSON Web Signature (JWS) secured
 object serialisable to JSON.

JWSProvider

JSON Web Signature (JWS) provider

JWSSigner

JSON Web Signature (JWS) signer.

JWSSignerOption

Marker interface for a JSON Web Signature (JWS) signer option.

JWSVerifier

JSON Web Signature (JWS) verifier.

KeyException

Key exception.

KeyLengthException

Key length exception.

KeySourceException

Key source exception.

KeyTypeException

Key type exception.

Option

Marker interface for an option.

Payload

Payload of an unsecured (plain), JSON Web Signature (JWS) or JSON Web
 Encryption (JWE) object.

Payload.Origin

Enumeration of the original data types used to create a 
 `Payload`.

PayloadTransformer<T>

Generic payload type transformer.

PlainHeader

Unsecured (`alg=none`) JOSE header.

PlainHeader.Builder

Builder for constructing unsecured (plain) headers.

PlainObject

Unsecured (plain / `alg=none`) JOSE object with
 compact
 serialisation.

RemoteKeySourceException

Remote key source exception.

Requirement

Enumeration of JOSE algorithm implementation requirements.

UnprotectedHeader

JSON Web Signature (JWS) or JSON Web Encryption (JWE) unprotected header
 (in a JSON serialisation).

UnprotectedHeader.Builder

Builder for constructing an unprotected JWS or JWE header.