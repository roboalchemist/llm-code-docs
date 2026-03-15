# Nimbus JOSE + JWT v10.8

# Nimbus JOSE + JWT

                
                

Create, parse and process:
                
                

                        
- JOSE secured objects:
                                

                                        
  - With compact URL-safe serialisation:
                                                

                                                        
    - `JSON Web Signature (JWS) objects`
                                                        
    - `JSON Web Encryption (JWE) objects`
                                                        
    - `Unsecured (alg=none) JOSE objects`
                                                        
    - `Signed`,
                                                                `encrypted` and
                                                                `unsecured`
                                                                `JSON Web Tokens (JWTs)`
                                                

                                        
                                        
  - With JSON serialisation:
                                                

                                                        
    - `JWS JSON objects` with one or more signatures.
                                                        
    - `JWE JSON objects` with one or more recipients.
                                                

                                        
                                

                        
                        
- `JSON Web Key (JWK) objects` and `JWK sets`
                

                

A framework for secure application-specific
                `processing of JWTs` as well as generic
                        (i.e. arbitrary payload) `JOSE objects`
                        is provided.

                

The library `implements` the
            following JWS and JWE algorithms:

        

JWS algorithms:
                

                        
- HMAC integrity protection: HS256, HS384 and HS512
                        
- RSA signatures: RS256, RS384, RS512, PS256, PS384 and PS512.
                        
- EC signatures: ES256, ES256K, ES384 and ES512
                        
- EdDSA signatures: EdDSA
                

        

JWE key management algorithms:

        

                        
- Key encryption with RSAES-PKCS1-V1_5: RSA1_5 (deprecated)
                        
- Key encryption with RSAES OAEP: RSA-OAEP (deprecated) and RSA-OAEP-256
            
- Key encryption with AES key wrap: A128KW, A192KW and A256KW
            
- Key encryption with AES GCM key wrap: A128CGMKW, A192CGMKW and A256CGMKW
            
- Direct encryption with a symmetric key: dir
                        
- Key Agreement with Elliptic Curve Diffie-Hellman Ephemeral Static: ECDH-ES, ECDH-ES+A128KW, ECDH-ES+A192KW and ECDH-ES+A256KW
                        
- Public key authenticated encryption utilising the One-Pass Unified Model for Elliptic Curve Diffie-Hellman key agreement: ECDH-1PU, ECDH-1PU+A128KW, ECDH-1PU+A128KW, ECDH-1PU+A256KW
                        
- Password-based encryption: PBES2-HS256+A128KW, PBES2-HS384+A192KW and PBES2-HS512+A256KW
        

        

JWE content encryption algorithms:

        

            
- AES_CBC_HMAC_SHA2: A128CBC-HS256, A192CBC-HS384, A256CBC-HS512,
                the deprecated A128CBC+HS256 and A256CBC+HS512 are also supported
            
- AES GCM: A128GCM, A192GCM and A256GCM
                        
- Extended nonce ChaCha20-Poly1305: XC20P
        

        

New JWA algorithms can be easily added. The library provides a set
                        of interfaces to decouple the representation of JOSE / JWT objects
                        from JWA cryptography code for signing / verification or encryption
                        / decryption. Multiple JCA providers, including hardware-based
                        (PKCS#11) can be configured.
                
                

Supported specifications:
                
                

                        
- RFC 7515 - JWS
                        
- RFC 7516 - JWE
                        
- RFC 7517 - JWK
                        
- RFC 7518 - JWA
                        
- RFC 7519 - JWT
                        
- RFC 7165 - Use Cases and Requirements for JSON Object Signing and Encryption (JOSE)
                        
- RFC 7520 - Examples of Protecting Content Using JSON Object Signing and Encryption (JOSE)
                        
- RFC 7638 - JWK Thumbprint
                        
- RFC 7797 - JWS Unencoded Payload Option
                        
- RFC 8037 - CFRG ECDH and Signatures in JOSE
                        
- RFC 8812 - CBOR Object Signing and Encryption (COSE) and JSON Object Signing and Encryption (JOSE) Registrations for Web Authentication (WebAuthn) Algorithms
                        
- RFC 9278 - JWK Thumbprint URI
                        
- OpenID Federation 1.0
                        
- draft-madden-jose-ecdh-1pu-04 - Public Key Authenticated Encryption for JOSE: ECDH-1PU
                        
- draft-amringer-jose-chacha-02 - Chacha derived AEAD algorithms in JSON Object Signing and Encryption (JOSE) (support for XC20P only)
                        
- XChaCha: eXtended-nonce ChaCha and AEAD_XChaCha20_Poly1305
                        
- Fully-Specified Algorithms for JOSE and COSE
                

                
                

Dependencies (see the Maven pom.xml for details):
                
                

                        
- [shaded] JCIP for concurrency annotations
                        
- [shaded] GSon for parsing and serialisation of JSON
                        
- [optional] BouncyCastle as an alternative JCA provider and for selected key and certificate utilities
                        
- [optional] Tink for OKP generation, EdDSA with Ed25519, ECDH with X25519 and content encryption with XC20P
                

                

To post bug reports and suggestions:

                

https://bitbucket.org/connect2id/nimbus-jose-jwt/issues

Packages

Package
Description
com.nimbusds.jose

Base Javascript Object Signing and Encryption (JOSE) interfaces and classes.

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

com.nimbusds.jose.crypto.opts

Javascript Object Signing and Encryption (JOSE) options.

com.nimbusds.jose.crypto.utils

Cryptographic utilities.

com.nimbusds.jose.jca

Java Cryptography Architecture (JCA) context interfaces and classes.

com.nimbusds.jose.jwk

JSON Web Key (JWK) classes.

com.nimbusds.jose.jwk.gen

JSON Web Key (JWK) generation utilities.

com.nimbusds.jose.jwk.source

JSON Web Key (JWK) sourcing interface and utilities.

com.nimbusds.jose.mint

JSON Web Signature (JWS) minting framework.

com.nimbusds.jose.proc

Framework for application-specific verification and decryption of JOSE
 objects (with arbitrary payloads).

com.nimbusds.jose.produce

Framework for producing JOSE objects (with arbitrary payloads).

com.nimbusds.jose.util

Utility interfaces and classes.

com.nimbusds.jose.util.cache

Simple object caching.

com.nimbusds.jose.util.events

Event listener interfaces.

com.nimbusds.jose.util.health

Health status reporting.

com.nimbusds.jwt

JSON Web Token (JWT) interfaces and classes.

com.nimbusds.jwt.proc

Framework for application-specific verification and decryption of JSON Web
 Tokens (JWTs).

com.nimbusds.jwt.util

JSON Web Token (JWT) utility interfaces and classes.