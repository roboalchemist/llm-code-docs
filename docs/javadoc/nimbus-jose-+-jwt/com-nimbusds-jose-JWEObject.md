Package com.nimbusds.jose

# Class JWEObject

java.lang.Object
com.nimbusds.jose.JOSEObject
com.nimbusds.jose.JWEObject

All Implemented Interfaces:
`Serializable`

Direct Known Subclasses:
`EncryptedJWT`

---

@ThreadSafe
public class JWEObject
extends JOSEObject
JSON Web Encryption (JWE) secured object with
 compact
 serialisation.

 

This class is thread-safe.

Version:
2026-01-04
Author:
Vladimir Dzhuvinov, Egor Puzanov
See Also:

- Serialized Form

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static enum `
`JWEObject.State`

Enumeration of the states of a JSON Web Encryption (JWE) secured
 object.

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final int`
`MAX_COMPRESSED_CIPHER_TEXT_LENGTH`

The maximum allowed character length of compressed cipher text.

### Fields inherited from class com.nimbusds.jose.JOSEObject

`MIME_TYPE_COMPACT, MIME_TYPE_JS`

- 

## Constructor Summary

Constructors

Constructor
Description
`JWEObject(JWEHeader header,
 Payload payload)`

Creates a new to-be-encrypted JSON Web Encryption (JWE) object with 
 the specified header and payload.

`JWEObject(Base64URL firstPart,
 Base64URL secondPart,
 Base64URL thirdPart,
 Base64URL fourthPart,
 Base64URL fifthPart)`

Creates a new encrypted JSON Web Encryption (JWE) object with the 
 specified serialised parts.

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`decrypt(JWEDecrypter decrypter)`

Decrypts this JWE object with the specified decrypter.

`void`
`decrypt(JWEDecrypter decrypter,
 Set<JWEDecrypterOption> opts)`

Decrypts this JWE object with the specified decrypter and options.

`void`
`encrypt(JWEEncrypter encrypter)`

Encrypts this JWE object with the specified encrypter.

`Base64URL`
`getAuthTag()`

Returns the authentication tag of this JWE object.

`Base64URL`
`getCipherText()`

Returns the cipher text of this JWE object.

`Base64URL`
`getEncryptedKey()`

Returns the encrypted key of this JWE object.

`JWEHeader`
`getHeader()`

Returns the header of this JOSE object.

`Base64URL`
`getIV()`

Returns the initialisation vector (IV) of this JWE object.

`JWEObject.State`
`getState()`

Returns the state of the JWE secured object.

`static JWEObject`
`parse(String s)`

Parses a JWE object from the specified string in compact form.

`String`
`serialize()`

Serialises this JWE object to its compact format consisting of 
 Base64URL-encoded parts delimited by period ('.') characters.

### Methods inherited from class com.nimbusds.jose.JOSEObject

`getParsedParts, getParsedString, getPayload, setParsedParts, setPayload, split`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### MAX_COMPRESSED_CIPHER_TEXT_LENGTH

public static final int MAX_COMPRESSED_CIPHER_TEXT_LENGTH
The maximum allowed character length of compressed cipher text.

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### JWEObject

public JWEObject(JWEHeader header,
 Payload payload)
Creates a new to-be-encrypted JSON Web Encryption (JWE) object with 
 the specified header and payload. The initial state will be 
 `unencrypted`.

Parameters:
`header` - The JWE header. Must not be `null`.
`payload` - The payload. Must not be `null`.

  - 

### JWEObject

public JWEObject(Base64URL firstPart,
 Base64URL secondPart,
 Base64URL thirdPart,
 Base64URL fourthPart,
 Base64URL fifthPart)
          throws ParseException
Creates a new encrypted JSON Web Encryption (JWE) object with the 
 specified serialised parts. The state will be `encrypted`.

Parameters:
`firstPart` - The first part, corresponding to the JWE header. 
                   Must not be `null`.
`secondPart` - The second part, corresponding to the encrypted 
                   key. Empty or `null` if none.
`thirdPart` - The third part, corresponding to the 
                   initialisation vector. Empty or `null` if 
                   none.
`fourthPart` - The fourth part, corresponding to the cipher text.
                   Must not be `null`.
`fifthPart` - The fifth part, corresponding to the 
                   authentication tag. Empty of `null` if none.
Throws:
`ParseException` - If parsing of the serialised parts failed.

- 

## Method Details

  - 

### getHeader

public JWEHeader getHeader()
Description copied from class: `JOSEObject`
Returns the header of this JOSE object.

Specified by:
`getHeader` in class `JOSEObject`
Returns:
The header.

  - 

### getEncryptedKey

public Base64URL getEncryptedKey()
Returns the encrypted key of this JWE object.

Returns:
The encrypted key, `null` not applicable or the JWE
         object has not been encrypted yet.

  - 

### getIV

public Base64URL getIV()
Returns the initialisation vector (IV) of this JWE object.

Returns:
The initialisation vector (IV), `null` if not 
         applicable or the JWE object has not been encrypted yet.

  - 

### getCipherText

public Base64URL getCipherText()
Returns the cipher text of this JWE object.

Returns:
The cipher text, `null` if the JWE object has not been
         encrypted yet.

  - 

### getAuthTag

public Base64URL getAuthTag()
Returns the authentication tag of this JWE object.

Returns:
The authentication tag, `null` if not applicable or
         the JWE object has not been encrypted yet.

  - 

### getState

public JWEObject.State getState()
Returns the state of the JWE secured object.

Returns:
The state.

  - 

### encrypt

public void encrypt(JWEEncrypter encrypter)
             throws JOSEException
Encrypts this JWE object with the specified encrypter. The JWE 
 object must be in an `unencrypted` state.

Parameters:
`encrypter` - The JWE encrypter. Must not be `null`.
Throws:
`IllegalStateException` - If the JWE object is not in an 
                               `unencrypted
                               state`.
`JOSEException` - If the JWE object couldn't be 
                               encrypted.

  - 

### decrypt

public void decrypt(JWEDecrypter decrypter)
             throws JOSEException
Decrypts this JWE object with the specified decrypter. The JWE 
 object must be in a `encrypted` state.

Parameters:
`decrypter` - The JWE decrypter. Must not be `null`.
Throws:
`IllegalStateException` - If the JWE object is not in an 
                               `encrypted
                               state`.
`JOSEException` - If the JWE object couldn't be 
                               decrypted.

  - 

### decrypt

public void decrypt(JWEDecrypter decrypter,
 Set<JWEDecrypterOption> opts)
             throws JOSEException
Decrypts this JWE object with the specified decrypter and options.
 The JWE object must be in a `encrypted` state.

Parameters:
`decrypter` - The JWE decrypter. Must not be `null`.
`opts` - The JWE decrypter options, `null` if none.
Throws:
`IllegalStateException` - If the JWE object is not in an 
                               `encrypted
                               state`.
`JOSEException` - If the JWE object couldn't be 
                               decrypted.

  - 

### serialize

public String serialize()
Serialises this JWE object to its compact format consisting of 
 Base64URL-encoded parts delimited by period ('.') characters. It 
 must be in a `encrypted` or 
 `decrypted` state.

 

```

 [header-base64url].[encryptedKey-base64url].[iv-base64url].[cipherText-base64url].[authTag-base64url]
 
```

Specified by:
`serialize` in class `JOSEObject`
Returns:
The serialised JWE object.
Throws:
`IllegalStateException` - If the JWE object is not in a 
                               `encrypted` or
                               `decrypted 
                               state`.

  - 

### parse

public static JWEObject parse(String s)
                       throws ParseException
Parses a JWE object from the specified string in compact form. The 
 parsed JWE object will be given an `JWEObject.State.ENCRYPTED` state.

Parameters:
`s` - The string to parse. Must not be `null`.
Returns:
The JWE object.
Throws:
`ParseException` - If the string couldn't be parsed to a valid 
                        JWE object.