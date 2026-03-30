Package com.nimbusds.jose

# Class JOSEObjectJSON

java.lang.Object
com.nimbusds.jose.JOSEObjectJSON

All Implemented Interfaces:
`Serializable`

Direct Known Subclasses:
`JWEObjectJSON`, `JWSObjectJSON`

---

public abstract class JOSEObjectJSON
extends Object
implements Serializable
The base abstract class for JSON Web Signature (JWS) secured and JSON Web
 Encryption (JWE) secured objects serialisable to JSON.

Version:
2021-10-05
Author:
Vladimir Dzhuvinov
See Also:

- Serialized Form

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`MIME_TYPE_JOSE_JSON`

The MIME type of JOSE objects serialised to JSON:
 `application/jose+json; charset=UTF-8`

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
`protected `
`JOSEObjectJSON(Payload payload)`

Creates a new JOSE object with the specified payload.

- 

## Method Summary

Modifier and Type
Method
Description
`Payload`
`getPayload()`

Returns the payload of this JOSE object.

`static JOSEObjectJSON`
`parse(String json)`

Parses a JOSE secured object from the specified JSON string.

`static JOSEObjectJSON`
`parse(Map<String,Object> jsonObject)`

Parses a JOSE secured object from the specified JSON object
 representation.

`abstract String`
`serializeFlattened()`

Serialises this JOSE object to a flattened JSON object string.

`abstract String`
`serializeGeneral()`

Serialises this JOSE object to a general JOSE object string.

`protected void`
`setPayload(Payload payload)`

Sets the payload of this JOSE object.

`abstract Map<String,Object>`
`toFlattenedJSONObject()`

Returns a flattened JSON object representation of this JOSE secured
 object.

`abstract Map<String,Object>`
`toGeneralJSONObject()`

Returns a general JSON object representation of this JOSE secured
 object.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### MIME_TYPE_JOSE_JSON

public static final String MIME_TYPE_JOSE_JSON
The MIME type of JOSE objects serialised to JSON:
 `application/jose+json; charset=UTF-8`

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### JOSEObjectJSON

protected JOSEObjectJSON(Payload payload)
Creates a new JOSE object with the specified payload.

Parameters:
`payload` - The payload, `null` if not available (e.g. for
                an encrypted JWE object).

- 

## Method Details

  - 

### setPayload

protected void setPayload(Payload payload)
Sets the payload of this JOSE object.

Parameters:
`payload` - The payload, `null` if not available (e.g. for 
                an encrypted JWE object).

  - 

### getPayload

public Payload getPayload()
Returns the payload of this JOSE object.

Returns:
The payload, `null` if not available (for an encrypted
         JWE object that hasn't been decrypted).

  - 

### toGeneralJSONObject

public abstract Map<String,Object> toGeneralJSONObject()
Returns a general JSON object representation of this JOSE secured
 object.

 

See
 JWS
 general serialisation or
 JWE
 general serialisation.

Returns:
The JSON object.
Throws:
`IllegalStateException` - If the JOSE object is not in a state
                               that permits serialisation.

  - 

### toFlattenedJSONObject

public abstract Map<String,Object> toFlattenedJSONObject()
Returns a flattened JSON object representation of this JOSE secured
 object. There must be exactly one JWS signature or JWE recipient for
 a flattened JSON serialisation.

 

See
 JWS
 flattened serialisation or
 JWE
 flattened serialisation.

Returns:
The JSON object.
Throws:
`IllegalStateException` - If the JOSE object is not in a state
                               that permits serialisation or there
                               is more than one JWS signature or JWE
                               recipient.

  - 

### serializeGeneral

public abstract String serializeGeneral()
Serialises this JOSE object to a general JOSE object string.

 

See
 JWS
 general serialisation or
 JWE
 general serialisation.

Returns:
The JSON object string.
Throws:
`IllegalStateException` - If the JOSE object is not in a state
                               that permits serialisation.

  - 

### serializeFlattened

public abstract String serializeFlattened()
Serialises this JOSE object to a flattened JSON object string. There
 must be exactly one JWS signature or JWE recipient for a flattened
 JSON serialisation.

 

See
 JWS
 flattened serialisation or
 JWE
 flattened serialisation.

Returns:
The JSON object string.
Throws:
`IllegalStateException` - If the JOSE object is not in a state
                               that permits serialisation or there
                               is more than one JWS signature or JWE
                               recipient.

  - 

### parse

public static JOSEObjectJSON parse(Map<String,Object> jsonObject)
                            throws ParseException
Parses a JOSE secured object from the specified JSON object
 representation.

Parameters:
`jsonObject` - The JSON object to parse. Must not be
                   `null`.
Returns:
The corresponding `JWSObjectJSON`.
Throws:
`ParseException` - If the JSON object couldn't be parsed to a
                        valid JWS or JWE secured object.

  - 

### parse

public static JOSEObjectJSON parse(String json)
                            throws ParseException
Parses a JOSE secured object from the specified JSON string.

Parameters:
`json` - The JSON string to parse. Must not be `null`.
Returns:
The corresponding `JWSObjectJSON`.
Throws:
`ParseException` - If the string couldn't be parsed to a valid 
                        JWS or JWE secured object.