Package com.nimbusds.jose

# Class PlainHeader

java.lang.Object
com.nimbusds.jose.Header
com.nimbusds.jose.PlainHeader

All Implemented Interfaces:
`Serializable`

---

@Immutable
public final class PlainHeader
extends Header
Unsecured (`alg=none`) JOSE header. This class is immutable.

 

Supports all `registered header
 parameters` of the unsecured JOSE object specification:

 

     
- alg (set to `"none"`).
     
- typ
     
- cty
     
- crit
 

 

The header may also carry `custom parameters`;
 these will be serialised and parsed along the registered ones.

 

Example:

 

```

 {
   "alg" : "none"
 }
 
```

Version:
2021-06-04
Author:
Vladimir Dzhuvinov
See Also:

- Serialized Form

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static class `
`PlainHeader.Builder`

Builder for constructing unsecured (plain) headers.

- 

## Field Summary

### Fields inherited from class com.nimbusds.jose.Header

`MAX_HEADER_STRING_LENGTH`

- 

## Constructor Summary

Constructors

Constructor
Description
`PlainHeader()`

Creates a new minimal unsecured (plain) header with algorithm
 `none`.

`PlainHeader(JOSEObjectType typ,
 String cty,
 Set<String> crit,
 Map<String,Object> customParams,
 Base64URL parsedBase64URL)`

Creates a new unsecured (plain) header with algorithm
 `none`.

`PlainHeader(PlainHeader plainHeader)`

Deep copy constructor.

- 

## Method Summary

Modifier and Type
Method
Description
`Algorithm`
`getAlgorithm()`

Gets the algorithm (`alg`) parameter.

`static Set<String>`
`getRegisteredParameterNames()`

Gets the registered parameter names for unsecured headers.

`static PlainHeader`
`parse(Base64URL base64URL)`

Parses an unsecured header from the specified Base64URL.

`static PlainHeader`
`parse(String jsonString)`

Parses an unsecured header from the specified JSON string.

`static PlainHeader`
`parse(String jsonString,
 Base64URL parsedBase64URL)`

Parses an unsecured header from the specified JSON string.

`static PlainHeader`
`parse(Map<String,Object> jsonObject)`

Parses an unsecured header from the specified JSON object.

`static PlainHeader`
`parse(Map<String,Object> jsonObject,
 Base64URL parsedBase64URL)`

Parses an unsecured header from the specified JSON object.

### Methods inherited from class com.nimbusds.jose.Header

`getContentType, getCriticalParams, getCustomParam, getCustomParams, getIncludedParams, getParsedBase64URL, getType, join, parseAlgorithm, toBase64URL, toJSONObject, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### PlainHeader

public PlainHeader()
Creates a new minimal unsecured (plain) header with algorithm
 `none`.

  - 

### PlainHeader

public PlainHeader(JOSEObjectType typ,
 String cty,
 Set<String> crit,
 Map<String,Object> customParams,
 Base64URL parsedBase64URL)
Creates a new unsecured (plain) header with algorithm
 `none`.

Parameters:
`typ` - The type (`typ`) parameter,
                        `null` if not specified.
`cty` - The content type (`cty`) parameter,
                        `null` if not specified.
`crit` - The names of the critical header
                        (`crit`) parameters, empty set or
                        `null` if none.
`customParams` - The custom parameters, empty map or
                        `null` if none.
`parsedBase64URL` - The parsed Base64URL, `null` if the
                        header is created from scratch.

  - 

### PlainHeader

public PlainHeader(PlainHeader plainHeader)
Deep copy constructor.

Parameters:
`plainHeader` - The unsecured header to copy. Must not be
                    `null`.

- 

## Method Details

  - 

### getRegisteredParameterNames

public static Set<String> getRegisteredParameterNames()
Gets the registered parameter names for unsecured headers.

Returns:
The registered parameter names, as an unmodifiable set.

  - 

### getAlgorithm

public Algorithm getAlgorithm()
Gets the algorithm (`alg`) parameter.

Overrides:
`getAlgorithm` in class `Header`
Returns:
`Algorithm.NONE`.

  - 

### parse

public static PlainHeader parse(Map<String,Object> jsonObject)
                         throws ParseException
Parses an unsecured header from the specified JSON object.

Parameters:
`jsonObject` - The JSON object to parse. Must not be `null`.
Returns:
The unsecured header.
Throws:
`ParseException` - If the specified JSON object doesn't
                        represent a valid unsecured header.

  - 

### parse

public static PlainHeader parse(Map<String,Object> jsonObject,
 Base64URL parsedBase64URL)
                         throws ParseException
Parses an unsecured header from the specified JSON object.

Parameters:
`jsonObject` - The JSON object to parse. Must not be
                        `null`.
`parsedBase64URL` - The original parsed Base64URL, `null`
                        if not applicable.
Returns:
The unsecured header.
Throws:
`ParseException` - If the specified JSON object doesn't
                        represent a valid unsecured header.

  - 

### parse

public static PlainHeader parse(String jsonString)
                         throws ParseException
Parses an unsecured header from the specified JSON string.

Parameters:
`jsonString` - The JSON string to parse. Must not be
                   `null`.
Returns:
The unsecured header.
Throws:
`ParseException` - If the specified JSON string doesn't
                        represent a valid unsecured header.

  - 

### parse

public static PlainHeader parse(String jsonString,
 Base64URL parsedBase64URL)
                         throws ParseException
Parses an unsecured header from the specified JSON string.

Parameters:
`jsonString` - The JSON string to parse. Must not be
                        `null`.
`parsedBase64URL` - The original parsed Base64URL, `null`
                        if not applicable.
Returns:
The unsecured header.
Throws:
`ParseException` - If the specified JSON string doesn't 
                        represent a valid unsecured header.

  - 

### parse

public static PlainHeader parse(Base64URL base64URL)
                         throws ParseException
Parses an unsecured header from the specified Base64URL.

Parameters:
`base64URL` - The Base64URL to parse. Must not be `null`.
Returns:
The unsecured header.
Throws:
`ParseException` - If the specified Base64URL doesn't represent
                        a valid unsecured header.