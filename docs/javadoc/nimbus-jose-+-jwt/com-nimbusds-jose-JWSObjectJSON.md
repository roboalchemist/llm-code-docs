Package com.nimbusds.jose

# Class JWSObjectJSON

java.lang.Object
com.nimbusds.jose.JOSEObjectJSON
com.nimbusds.jose.JWSObjectJSON

All Implemented Interfaces:
`Serializable`

---

@ThreadSafe
public class JWSObjectJSON
extends JOSEObjectJSON
JSON Web Signature (JWS) secured object with
 JSON
 serialisation.

 

This class is thread-safe.

Version:
2024-04-20
Author:
Alexander Martynov, Vladimir Dzhuvinov
See Also:

- Serialized Form

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static final class `
`JWSObjectJSON.Signature`

Individual signature in a JWS secured object serialisable to JSON.

`static enum `
`JWSObjectJSON.State`

Enumeration of the states of a JSON Web Signature (JWS) secured
 object serialisable to JSON.

- 

## Field Summary

### Fields inherited from class com.nimbusds.jose.JOSEObjectJSON

`MIME_TYPE_JOSE_JSON`

- 

## Constructor Summary

Constructors

Constructor
Description
`JWSObjectJSON(Payload payload)`

Creates a new to-be-signed JSON Web Signature (JWS) secured object
 with the specified payload.

- 

## Method Summary

Modifier and Type
Method
Description
`List<JWSObjectJSON.Signature>`
`getSignatures()`

Returns the individual signatures.

`JWSObjectJSON.State`
`getState()`

Returns the current signatures state.

`static JWSObjectJSON`
`parse(String json)`

Parses a JWS secured object from the specified JSON object string.

`static JWSObjectJSON`
`parse(Map<String,Object> jsonObject)`

Parses a JWS secured object from the specified JSON object
 representation.

`String`
`serializeFlattened()`

Serialises this JOSE object to a flattened JSON object string.

`String`
`serializeGeneral()`

Serialises this JOSE object to a general JOSE object string.

`void`
`sign(JWSHeader jwsHeader,
 JWSSigner signer)`

Signs this JWS secured object with the specified JWS signer and
 adds the resulting signature to it.

`void`
`sign(JWSHeader jwsHeader,
 UnprotectedHeader unprotectedHeader,
 JWSSigner signer)`

Signs this JWS secured object with the specified JWS signer and
 adds the resulting signature to it.

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

### JWSObjectJSON

public JWSObjectJSON(Payload payload)
Creates a new to-be-signed JSON Web Signature (JWS) secured object
 with the specified payload.

Parameters:
`payload` - The payload. Must not be `null`.

- 

## Method Details

  - 

### getSignatures

public List<JWSObjectJSON.Signature> getSignatures()
Returns the individual signatures.

Returns:
The individual signatures, as an unmodified list, empty list
         if none have been added.

  - 

### sign

public void sign(JWSHeader jwsHeader,
 JWSSigner signer)
          throws JOSEException
Signs this JWS secured object with the specified JWS signer and
 adds the resulting signature to it. To add multiple
 `signatures` call this method successively.

Parameters:
`jwsHeader` - The JWS protected header. The algorithm specified
                  by the header must be supported by the JWS signer.
                  Must not be `null`.
`signer` - The JWS signer. Must not be `null`.
Throws:
`JOSEException` - If the JWS object couldn't be signed.

  - 

### sign

public void sign(JWSHeader jwsHeader,
 UnprotectedHeader unprotectedHeader,
 JWSSigner signer)
          throws JOSEException
Signs this JWS secured object with the specified JWS signer and
 adds the resulting signature to it. To add multiple
 `signatures` call this method successively.

Parameters:
`jwsHeader` - The JWS protected header. The
                               algorithm specified by the header must
                               be supported by the JWS signer. Must
                               not be `null`.
`unprotectedHeader` - The unprotected header to include,
                               `null` if none.
`signer` - The JWS signer. Must not be
                               `null`.
Throws:
`JOSEException` - If the JWS object couldn't be signed.

  - 

### getState

public JWSObjectJSON.State getState()
Returns the current signatures state.

Returns:
The state.

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

public static JWSObjectJSON parse(Map<String,Object> jsonObject)
                           throws ParseException
Parses a JWS secured object from the specified JSON object
 representation.

Parameters:
`jsonObject` - The JSON object to parse. Must not be
                   `null`.
Returns:
The JWS secured object.
Throws:
`ParseException` - If the JSON object couldn't be parsed to a
                        JWS secured object.

  - 

### parse

public static JWSObjectJSON parse(String json)
                           throws ParseException
Parses a JWS secured object from the specified JSON object string.

Parameters:
`json` - The JSON object string to parse. Must not be
             `null`.
Returns:
The JWS secured object.
Throws:
`ParseException` - If the string couldn't be parsed to a JWS
                        secured object.