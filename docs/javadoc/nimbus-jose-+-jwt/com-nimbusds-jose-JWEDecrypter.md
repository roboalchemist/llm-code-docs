Package com.nimbusds.jose

# Interface JWEDecrypter

All Superinterfaces:
`JCAAware<JWEJCAContext>`, `JOSEProvider`, `JWEProvider`

All Known Implementing Classes:
`AESDecrypter`, `DirectDecrypter`, `ECDH1PUDecrypter`, `ECDH1PUX25519Decrypter`, `ECDHDecrypter`, `MultiDecrypter`, `PasswordBasedDecrypter`, `RSADecrypter`, `X25519Decrypter`

---

public interface JWEDecrypter
extends JWEProvider
JSON Web Encryption (JWE) decrypter.

Version:
2023-03-26
Author:
Vladimir Dzhuvinov, Egor Puzanov

- 

## Method Summary

Modifier and Type
Method
Description
`byte[]`
`decrypt(JWEHeader header,
 Base64URL encryptedKey,
 Base64URL iv,
 Base64URL cipherText,
 Base64URL authTag,
 byte[] aad)`

Decrypts the specified cipher text of a `JWE Object`.

### Methods inherited from interface com.nimbusds.jose.jca.JCAAware

`getJCAContext`

### Methods inherited from interface com.nimbusds.jose.JWEProvider

`supportedEncryptionMethods, supportedJWEAlgorithms`

- 

## Method Details

  - 

### decrypt

byte[] decrypt(JWEHeader header,
 Base64URL encryptedKey,
 Base64URL iv,
 Base64URL cipherText,
 Base64URL authTag,
 byte[] aad)
        throws JOSEException
Decrypts the specified cipher text of a `JWE Object`.

Parameters:
`header` - The JSON Web Encryption (JWE) header. Must
                     specify a supported JWE algorithm and method.
                     Must not be `null`.
`encryptedKey` - The encrypted key, `null` if not required
                     by the JWE algorithm.
`iv` - The initialisation vector, `null` if not
                     required by the JWE algorithm.
`cipherText` - The cipher text to decrypt. Must not be
                     `null`.
`authTag` - The authentication tag, `null` if not
                     required.
`aad` - The additional authenticated data. Must not be
                     `null`.
Returns:
The clear text.
Throws:
`JOSEException` - If the JWE algorithm or method is not
                       supported, if a critical header parameter is
                       not supported or marked for deferral to the
                       application, or if decryption failed for some
                       other reason.