# Package com.nimbusds.jose.crypto

---

package com.nimbusds.jose.crypto

Implementations of standard Javascript Object Signing and Encryption (JOSE)
 algorithms.

 

Provides `signers` and 
 `verifiers` for the following JSON Web
 Signature (JWS) algorithms:

 

     
- For HMAC algorithms HS256, HS384 and HS512:
         

             
  - `MACSigner`
             
  - `MACVerifier`
         

     
- For RSA-SSA signatures RS256, RS384, RS512, PS256, PS384 and PS512:
         

             
  - `RSASSASigner`
             
  - `RSASSAVerifier`
         

      
- For ECDSA signatures ES256, ES384 and ES512:
         

             
  - `ECDSASigner`
             
  - `ECDSAVerifier`
         

      
- For EdDSA signatures Ed25519:
         

             
  - `Ed25519Signer`
             
  - `Ed25519Verifier`
         

 

 

Provides `encrypters` and 
 `decrypters` for the following JSON
 Web Encryption (JWE) algorithms:

 

     
- For RSA PKCS#1 v1.5 and RSA OAEP:
         

             
  - `RSAEncrypter`
             
  - `RSADecrypter`
         

     
- For AES key wrap and AES GCM key encryption:
         

             
  - `AESEncrypter`
             
  - `AESDecrypter`
         

     
- For direct encryption (using a shared symmetric key):
         

             
  - `DirectEncrypter`
             
  - `DirectDecrypter`
         

     
- For Elliptic Curve Diffie-Hellman (ECDH) encryption:
         

             
  - `ECDHEncrypter`
             
  - `ECDHDecrypter`
             
  - `X25519Encrypter` (for Curve25519 only)
             
  - `X25519Decrypter` (for Curve25519 only)
         

     
- For password-based (PBKDF2) encryption:
         

             
  - `PasswordBasedEncrypter`
             
  - `PasswordBasedDecrypter`
         

 

 

References:

 

     
- RFC 7518 (JWA)
     
- RFC 8037 (CFRG ECDH and
         Signatures JOSE)
 

- 

Related Packages

Package
Description
com.nimbusds.jose

Base Javascript Object Signing and Encryption (JOSE) interfaces and classes.

com.nimbusds.jose.crypto.bc
 
com.nimbusds.jose.crypto.factories

JWS signer, JWS verifier, JWE encrypter and JWE decrypter factory
 implementations.

com.nimbusds.jose.crypto.impl

Cryptographic primitives for JWS signers, JWS verifiers, JWE encrypters and
 JWE decrypters in the `com.nimbusds.jose.crypto` package.

com.nimbusds.jose.crypto.opts

Javascript Object Signing and Encryption (JOSE) options.

com.nimbusds.jose.crypto.utils

Cryptographic utilities.

- 

Classes

Class
Description
AESDecrypter

AES and AES GCM key wrap decrypter of `JWE
 objects`.

AESEncrypter

AES and AES GCM key wrap encrypter of `JWE
 objects`.

DirectDecrypter

Direct decrypter of `JWE objects` with a
 shared symmetric key.

DirectEncrypter

Direct encrypter of `JWE objects` with a
 shared symmetric key.

ECDH1PUDecrypter

Elliptic Curve Diffie-Hellman decrypter of
 `JWE objects` for curves using an EC JWK.

ECDH1PUEncrypter

Elliptic Curve Diffie-Hellman encrypter of
 `JWE objects` for curves using an EC JWK.

ECDH1PUX25519Decrypter

Elliptic Curve Diffie-Hellman decrypter of
 `JWE objects` for curves using an OKP JWK.

ECDH1PUX25519Encrypter

Elliptic Curve Diffie-Hellman encrypter of
 `JWE objects` for curves using an OKP JWK.

ECDHDecrypter

Elliptic Curve Diffie-Hellman decrypter of
 `JWE objects` for curves using EC JWK
 keys.

ECDHEncrypter

Elliptic Curve Diffie-Hellman encrypter of
 `JWE objects` for curves using EC JWK keys.

ECDSASigner

Elliptic Curve Digital Signature Algorithm (ECDSA) signer of
 `JWS objects`.

ECDSAVerifier

Elliptic Curve Digital Signature Algorithm (ECDSA) verifier of 
 `JWS objects`.

Ed25519Signer

Ed25519 signer of `JWS objects`.

Ed25519Verifier

Ed25519 verifier of `JWS objects`.

MACSigner

Message Authentication Code (MAC) signer of 
 `JWS objects`.

MACVerifier

Message Authentication Code (MAC) verifier of 
 `JWS objects`.

MultiDecrypter

Multi-recipient decrypter of `JWE objects`.

MultiEncrypter

Multi-recipient encrypter of `JWE
 objects`.

PasswordBasedDecrypter

Password-based decrypter of `JWE objects`.

PasswordBasedEncrypter

Password-based encrypter of `JWE objects`.

RSADecrypter

RSA decrypter of `JWE objects`.

RSAEncrypter

RSA encrypter of `JWE objects`.

RSASSASigner

RSA Signature-Scheme-with-Appendix (RSASSA) signer of 
 `JWS objects`.

RSASSAVerifier

RSA Signature-Scheme-with-Appendix (RSASSA) verifier of 
 `JWS objects`.

X25519Decrypter

Curve25519 Elliptic Curve Diffie-Hellman decrypter of
 `JWE objects`.

X25519Encrypter

Curve25519 Elliptic Curve Diffie-Hellman encrypter of
 `JWE objects`.