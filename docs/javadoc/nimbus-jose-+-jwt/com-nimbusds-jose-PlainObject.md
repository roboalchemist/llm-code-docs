Package com.nimbusds.jose

# Class PlainObject

java.lang.Object
com.nimbusds.jose.JOSEObject
com.nimbusds.jose.PlainObject

All Implemented Interfaces:
`Serializable`

Direct Known Subclasses:
`PlainJWT`

---

@ThreadSafe
public class PlainObject
extends JOSEObject
Unsecured (plain / `alg=none`) JOSE object with
 compact
 serialisation.

 

This class is thread-safe.

Version:
2024-04-20
Author:
Vladimir Dzhuvinov
See Also:

- Serialized Form

- 

## Field Summary

### Fields inherited from class com.nimbusds.jose.JOSEObject

`MIME_TYPE_COMPACT, MIME_TYPE_JS`

- 

## Constructor Summary

Constructors

Constructor
Description
`PlainObject(Payload payload)`

Creates a new unsecured JOSE object with a default `PlainHeader` and the specified payload.

`PlainObject(PlainHeader header,
 Payload payload)`

Creates a new unsecured JOSE object with the specified header and
 payload.

`PlainObject(Base64URL firstPart,
 Base64URL secondPart)`

Creates a new unsecured JOSE object with the specified
 Base64URL-encoded parts.

- 

## Method Summary

Modifier and Type
Method
Description
`PlainHeader`
`getHeader()`

Returns the header of this JOSE object.

`static PlainObject`
`parse(String s)`

Parses an unsecured JOSE object from the specified string in compact
 format.

`String`
`serialize()`

Serialises this unsecured JOSE object to its compact format
 consisting of Base64URL-encoded parts delimited by period ('.')

### Methods inherited from class com.nimbusds.jose.JOSEObject

`getParsedParts, getParsedString, getPayload, setParsedParts, setPayload, split`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### PlainObject

public PlainObject(Payload payload)
Creates a new unsecured JOSE object with a default `PlainHeader` and the specified payload.

Parameters:
`payload` - The payload. Must not be `null`.

  - 

### PlainObject

public PlainObject(PlainHeader header,
 Payload payload)
Creates a new unsecured JOSE object with the specified header and
 payload.

Parameters:
`header` - The unsecured header. Must not be `null`.
`payload` - The payload. Must not be `null`.

  - 

### PlainObject

public PlainObject(Base64URL firstPart,
 Base64URL secondPart)
            throws ParseException
Creates a new unsecured JOSE object with the specified
 Base64URL-encoded parts.

Parameters:
`firstPart` - The first part, corresponding to the unsecured
                   header. Must not be `null`.
`secondPart` - The second part, corresponding to the payload. 
                   Must not be `null`.
Throws:
`ParseException` - If parsing of the serialised parts failed.

- 

## Method Details

  - 

### getHeader

public PlainHeader getHeader()
Description copied from class: `JOSEObject`
Returns the header of this JOSE object.

Specified by:
`getHeader` in class `JOSEObject`
Returns:
The header.

  - 

### serialize

public String serialize()
Serialises this unsecured JOSE object to its compact format
 consisting of Base64URL-encoded parts delimited by period ('.') 
 characters.

 

```

 [header-base64url].[payload-base64url].[]
 
```

Specified by:
`serialize` in class `JOSEObject`
Returns:
The serialised unsecured JOSE object.

  - 

### parse

public static PlainObject parse(String s)
                         throws ParseException
Parses an unsecured JOSE object from the specified string in compact
 format.

Parameters:
`s` - The string to parse. Must not be `null`.
Returns:
The unsecured JOSE object.
Throws:
`ParseException` - If the string couldn't be parsed to a valid 
                        unsecured JOSE object.