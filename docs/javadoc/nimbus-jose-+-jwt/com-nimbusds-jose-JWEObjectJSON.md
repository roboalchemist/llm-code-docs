Package com.nimbusds.jose

# Class JWEObjectJSON

java.lang.Object
com.nimbusds.jose.JOSEObjectJSON
com.nimbusds.jose.JWEObjectJSON

All Implemented Interfaces:
`Serializable`

---

@ThreadSafe
public class JWEObjectJSON
extends JOSEObjectJSON
JSON Web Encryption (JWE) secured object with
 JSON
 serialisation.

 

This class is thread-safe.

Version:
2024-04-20
Author:
Egor Puzanov, Vladimir Dzhuvinov
See Also:

- Serialized Form

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static final class `
`JWEObjectJSON.Recipient`

Individual recipient in a JWE object serialisable to JSON.

- 

## Field Summary

### Fields inherited from class com.nimbusds.jose.JOSEObjectJSON

`MIME_TYPE_JOSE_JSON`

- 

## Constructor Summary

Constructors

Constructor
Description
`JWEObjectJSON(JWEHeader header,
 Payload payload)`

Creates a new to-be-encrypted JSON Web Encryption (JWE) object with
 the specified JWE protected header and payload.

`JWEObjectJSON(JWEHeader header,
 Payload payload,
 UnprotectedHeader unprotectedHeader,
 byte[] aad)`

Creates a new to-be-encrypted JSON Web Encryption (JWE) object with
 the specified JWE protected header, payload and Additional
 Authenticated Data (AAD).

`JWEObjectJSON(JWEHeader header,
 Base64URL cipherText,
 Base64URL iv,
 Base64URL authTag,
 List<JWEObjectJSON.Recipient> recipients,
 UnprotectedHeader unprotectedHeader,
 byte[] aad)`

Creates a new encrypted JSON Web Encryption (JWE) object.

`JWEObjectJSON(JWEObject jweObject)`

Creates a new JWE JSON object from the specified JWE object with
 compact serialisation.

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`decrypt(JWEDecrypter decrypter)`

Decrypts this JWE object with the specified decrypter.

`void`
`encrypt(JWEEncrypter encrypter)`

Encrypts this JWE object with the specified encrypter.

`byte[]`
`getAAD()`

Returns the Additional Authenticated Data (AAD) of this JWE object.

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

Returns the JWE protected header of this JWE object.

`Base64URL`
`getIV()`

Returns the initialisation vector (IV) of this JWE object.

`List<JWEObjectJSON.Recipient>`
`getRecipients()`

Returns the recipients list of the JWE object.

`JWEObject.State`
`getState()`

Returns the state of this JWE object.

`UnprotectedHeader`
`getUnprotectedHeader()`

Returns the shared unprotected header of this JWE object.

`static JWEObjectJSON`
`parse(String json)`

Parses a JWE object from the specified JSON object string.

`static JWEObjectJSON`
`parse(Map<String,Object> jsonObject)`

Parses a JWE object from the specified JSON object representation.

`String`
`serializeFlattened()`

Serialises this JOSE object to a flattened JSON object string.

`String`
`serializeGeneral()`

Serialises this JOSE object to a general JOSE object string.

`Map<String,Object>`
`toFlattenedJSONObject()`

Returns a flattened JSON object representation of this JOSE secured
 object.

`Map<String,Object>`
`toGeneralJSONObject()`

Returns a general JSON object representation of this JOSE secured
 object.

### Methods inherited from class com.nimbusds.jose.JOSEObjectJSON

`getPayload, setPayload`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### JWEObjectJSON

public JWEObjectJSON(JWEObject jweObject)
Creates a new JWE JSON object from the specified JWE object with
 compact serialisation. The initial state is copied from the JWE
 object.

Parameters:
`jweObject` - The JWE object. Must not be `null`.

  - 

### JWEObjectJSON

public JWEObjectJSON(JWEHeader header,
 Payload payload)
Creates a new to-be-encrypted JSON Web Encryption (JWE) object with
 the specified JWE protected header and payload. The initial state
 will be `unencrypted`.

Parameters:
`header` - The JWE protected header. Must not be `null`.
`payload` - The payload. Must not be `null`.

  - 

### JWEObjectJSON

public JWEObjectJSON(JWEHeader header,
 Payload payload,
 UnprotectedHeader unprotectedHeader,
 byte[] aad)
Creates a new to-be-encrypted JSON Web Encryption (JWE) object with
 the specified JWE protected header, payload and Additional
 Authenticated Data (AAD). The initial state will be
 `unencrypted`.

Parameters:
`header` - The JWE protected header. Must not be
                          `null`.
`payload` - The payload. Must not be `null`.
`unprotectedHeader` - The shared unprotected header, empty or
                          `null` if none.
`aad` - The additional authenticated data (AAD),
                          `null` if none.

  - 

### JWEObjectJSON

public JWEObjectJSON(JWEHeader header,
 Base64URL cipherText,
 Base64URL iv,
 Base64URL authTag,
 List<JWEObjectJSON.Recipient> recipients,
 UnprotectedHeader unprotectedHeader,
 byte[] aad)
Creates a new encrypted JSON Web Encryption (JWE) object. The state
 will be `encrypted`.

Parameters:
`header` - The JWE protected header. Must not be
                          `null`.
`cipherText` - The cipher text. Must not be `null`.
`iv` - The initialisation vector, empty or
                          `null` if none.
`authTag` - The authentication tag, empty or
                          `null` if none.
`recipients` - The recipients list. Must not be
                          `null`.
`unprotectedHeader` - The shared unprotected header, empty or
                          `null` if none.
`aad` - The additional authenticated data. Must not
                          be `null`.

- 

## Method Details

  - 

### getHeader

public JWEHeader getHeader()
Returns the JWE protected header of this JWE object.

Returns:
The JWE protected header.

  - 

### getUnprotectedHeader

public UnprotectedHeader getUnprotectedHeader()
Returns the shared unprotected header of this JWE object.

Returns:
The shared unprotected header, empty or `null` if
         none.

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

### getAAD

public byte[] getAAD()
Returns the Additional Authenticated Data (AAD) of this JWE object.

Returns:
The Additional Authenticated Data (AAD).

  - 

### getRecipients

public List<JWEObjectJSON.Recipient> getRecipients()
Returns the recipients list of the JWE object.

Returns:
The recipients list.

  - 

### getState

public JWEObject.State getState()
Returns the state of this JWE object.

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

### toGeneralJSONObject

public Map<String,Object> toGeneralJSONObject()
Description copied from class: `JOSEObjectJSON`
Returns a general JSON object representation of this JOSE secured
 object.

 

See
 JWS
 general serialisation or
 JWE
 general serialisation.

Specified by:
`toGeneralJSONObject` in class `JOSEObjectJSON`
Returns:
The JSON object.

  - 

### toFlattenedJSONObject

public Map<String,Object> toFlattenedJSONObject()
Description copied from class: `JOSEObjectJSON`
Returns a flattened JSON object representation of this JOSE secured
 object. There must be exactly one JWS signature or JWE recipient for
 a flattened JSON serialisation.

 

See
 JWS
 flattened serialisation or
 JWE
 flattened serialisation.

Specified by:
`toFlattenedJSONObject` in class `JOSEObjectJSON`
Returns:
The JSON object.

  - 

### serializeGeneral

public String serializeGeneral()
Description copied from class: `JOSEObjectJSON`
Serialises this JOSE object to a general JOSE object string.

 

See
 JWS
 general serialisation or
 JWE
 general serialisation.

Specified by:
`serializeGeneral` in class `JOSEObjectJSON`
Returns:
The JSON object string.

  - 

### serializeFlattened

public String serializeFlattened()
Description copied from class: `JOSEObjectJSON`
Serialises this JOSE object to a flattened JSON object string. There
 must be exactly one JWS signature or JWE recipient for a flattened
 JSON serialisation.

 

See
 JWS
 flattened serialisation or
 JWE
 flattened serialisation.

Specified by:
`serializeFlattened` in class `JOSEObjectJSON`
Returns:
The JSON object string.

  - 

### parse

public static JWEObjectJSON parse(Map<String,Object> jsonObject)
                           throws ParseException
Parses a JWE object from the specified JSON object representation.

Parameters:
`jsonObject` - The JSON object to parse. Must not be
                   `null`.
Returns:
The JWE secured object.
Throws:
`ParseException` - If the JSON object couldn't be parsed to a
                        JWE secured object.

  - 

### parse

public static JWEObjectJSON parse(String json)
                           throws ParseException
Parses a JWE object from the specified JSON object string.

Parameters:
`json` - The JSON object string to parse. Must not be
             `null`.
Returns:
The JWE object.
Throws:
`ParseException` - If the string couldn't be parsed to a JWE
                        object.