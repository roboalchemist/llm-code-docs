Package com.nimbusds.jose

# Interface JWEEncrypter

All Superinterfaces:
`JCAAware<JWEJCAContext>`, `JOSEProvider`, `JWEProvider`

All Known Implementing Classes:
`AESEncrypter`, `DirectEncrypter`, `ECDH1PUEncrypter`, `ECDH1PUX25519Encrypter`, `ECDHEncrypter`, `MultiEncrypter`, `PasswordBasedEncrypter`, `RSAEncrypter`, `X25519Encrypter`

---

public interface JWEEncrypter
extends JWEProvider
JSON Web Encryption (JWE) encrypter.

Version:
2023-03-26
Author:
Vladimir Dzhuvinov, Egor Puzanov

- 

## Method Summary

Modifier and Type
Method
Description
`JWECryptoParts`
`encrypt(JWEHeader header,
 byte[] clearText,
 byte[] aad)`

Encrypts the specified clear text of a `JWE object`.

### Methods inherited from interface com.nimbusds.jose.jca.JCAAware

`getJCAContext`

### Methods inherited from interface com.nimbusds.jose.JWEProvider

`supportedEncryptionMethods, supportedJWEAlgorithms`

- 

## Method Details

  - 

### encrypt

JWECryptoParts encrypt(JWEHeader header,
 byte[] clearText,
 byte[] aad)
                throws JOSEException
Encrypts the specified clear text of a `JWE object`.

Parameters:
`header` - The JSON Web Encryption (JWE) header. Must specify
                  a supported JWE algorithm and method. Must not be
                  `null`.
`clearText` - The clear text to encrypt. Must not be `null`.
`aad` - The additional authenticated data. Must not be
                  `null`.
Returns:
The resulting JWE crypto parts.
Throws:
`JOSEException` - If the JWE algorithm or method is not
                       supported or if encryption failed for some
                       other internal reason.