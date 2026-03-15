# Package com.nimbusds.jose.crypto.opts

---

package com.nimbusds.jose.crypto.opts

Javascript Object Signing and Encryption (JOSE) options.

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

com.nimbusds.jose.crypto.impl

Cryptographic primitives for JWS signers, JWS verifiers, JWE encrypters and
 JWE decrypters in the `com.nimbusds.jose.crypto` package.

com.nimbusds.jose.crypto.utils

Cryptographic utilities.

- 

Classes

Class
Description
AllowWeakRSAKey

JSON Web Signature (JWS) and JSON Web Encryption (JWE) option to allow weak
 RSA keys shorter than
 `2048
 bits`.

CipherMode

JCA cipher mode.

MaxCompressedCipherTextLength

JSON Web Encryption (JWE) decrypter option to configure the maximum allowed
 length of compressed cipher text.

OptionUtils

Utilities for processing JOSE options.

UserAuthenticationRequired

JSON Web Signature (JWS) option to prompt the user to authenticate in order
 to complete the signing operation.