# Package com.nimbusds.jose.crypto.impl

---

package com.nimbusds.jose.crypto.impl

Cryptographic primitives for JWS signers, JWS verifiers, JWE encrypters and
 JWE decrypters in the `com.nimbusds.jose.crypto` package.

- 

Related Packages

Package
Description
com.nimbusds.jose.crypto

Implementations of standard Javascript Object Signing and Encryption (JOSE)
 algorithms.

com.nimbusds.jose.crypto.bc
 
com.nimbusds.jose.crypto.factories

JWS signer, JWS verifier, JWE encrypter and JWE decrypter factory
 implementations.

com.nimbusds.jose.crypto.opts

Javascript Object Signing and Encryption (JOSE) options.

com.nimbusds.jose.crypto.utils

Cryptographic utilities.

- 

Class
Description
AAD

Additional authenticated data (AAD).

AESCBC

AES/CBC/PKCS5Padding and AES/CBC/PKCS5Padding/HMAC-SHA2 encryption and 
 decryption methods.

AESCryptoProvider

The base abstract class for AES and AES GCM key wrap encrypters and
 decrypters of `JWE objects`.

AESGCM

AES/GSM/NoPadding encryption and decryption methods.

AESGCMKW

AES GCM methods for Content Encryption Key (CEK) encryption and
 decryption.

AESKW

AES key Wrapping methods for Content Encryption Key (CEK) encryption and
 decryption.

AlgorithmParametersHelper

Utility for creating `AlgorithmParameters` objects with
 an optional JCA provider.

AlgorithmSupportMessage

Algorithm support messages, intended for JOSE exceptions.

AuthenticatedCipherText

Authenticated cipher text.

BaseJWEProvider

The base abstract class for JSON Web Encryption (JWE) encrypters and
 decrypters.

BaseJWSProvider

The base abstract class for JSON Web Signature (JWS) signers and verifiers.

CipherHelper

Helper utilities for instantiating ciphers.

CompositeKey

Composite key used in AES/CBC/PKCS5Padding/HMAC-SHA2 encryption.

ConcatKDF

Concatenation Key Derivation Function (KDF).

ContentCryptoProvider

JWE content encryption / decryption provider.

CriticalHeaderParamsDeferral

Critical (`crit`) header parameters deferral policy.

DeflateHelper

Deflate (RFC 1951) helper methods, intended for use by JWE encrypters and
 decrypters.

DirectCryptoProvider

The base abstract class for direct encrypters and decrypters of
 `JWE objects` with a shared symmetric key.

ECDH

Elliptic Curve Diffie-Hellman key agreement functions and utilities.

ECDH.AlgorithmMode

Enumeration of the Elliptic Curve Diffie-Hellman Ephemeral Static
 algorithm modes.

ECDH1PU

Elliptic Curve Diffie-Hellman One-Pass Unified Model (ECDH-1PU) key
 agreement functions and utilities.

ECDH1PUCryptoProvider

The base abstract class for Elliptic Curve Diffie-Hellman One-Pass Unified
 Model encrypters and decrypters of `JWE
 objects`.

ECDHCryptoProvider

The base abstract class for Elliptic Curve Diffie-Hellman encrypters and
 decrypters of `JWE objects`.

ECDSA

Elliptic Curve Digital Signature Algorithm (ECDSA) functions and utilities.

ECDSAProvider

The base abstract class for Elliptic Curve Digital Signature Algorithm 
 (ECDSA) signers and validators of `JWS 
 objects`.

EdDSAProvider

The base abstract class for Edwards-curve Digital Signature Algorithm 
 (EdDSA) signers and validators of `JWS 
 objects`.

HMAC

Static methods for Hash-based Message Authentication Codes (HMAC).

JWEHeaderValidation

JWE header validation.

LegacyConcatKDF

Legacy implementation of a Concatenation Key Derivation Function (KDF) for
 use by the deprecated `A128CBC+HS256` and `A256CBC+HS512`
 encryption methods.

MACProvider

The base abstract class for Message Authentication Code (MAC) signers and
 verifiers of `JWS objects`.

MultiCryptoProvider

The base abstract class for multi-recipient encrypters and decrypters of
 `JWE objects` with a shared symmetric
 key.

PasswordBasedCryptoProvider

The base abstract class for password-based encrypters and decrypters of
 `JWE objects`.

PBKDF2

Password-Based Key Derivation Function 2 (PBKDF2) utilities.

PRFParams

Pseudo-Random Function (PRF) parameters, intended for use in the Password-
 Based Key Derivation Function 2 (PBKDF2).

RSA_OAEP

RSAES OAEP methods for Content Encryption Key (CEK) encryption and 
 decryption.

RSA_OAEP_SHA2

RSAES OAEP with SHA-256, SHA-384 and SHA-512 methods for Content Encryption
 Key (CEK) encryption and decryption.

RSA1_5

RSAES-PKCS1-V1_5 methods for Content Encryption Key (CEK) encryption and
 decryption.

RSACryptoProvider

The base abstract class for RSA encrypters and decrypters of
 `JWE objects`.

RSAKeyUtils

RSA JWK conversion utility.

RSASSA

RSA-SSA functions and utilities.

RSASSAProvider

The base abstract class for RSA signers and verifiers of `JWS objects`.

XC20P

This class defines the XChaCha20 stream cipher as well as the use of the
 Poly1305 authenticator.