Package com.nimbusds.jose

# Class Header

java.lang.Object
com.nimbusds.jose.Header

All Implemented Interfaces:
`Serializable`

Direct Known Subclasses:
`JWEHeader`, `JWSHeader`, `PlainHeader`

---

public abstract class Header
extends Object
implements Serializable
The base abstract class for unsecured (`alg=none`), JSON Web Signature
 (JWS) and JSON Web Encryption (JWE) headers.

 

The header may also include `custom
 parameters`; these will be serialised and parsed along the registered ones.

Version:
2021-08-11
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
`static final int`
`MAX_HEADER_STRING_LENGTH`

The max allowed string length when parsing a JOSE header (after the
 BASE64URL decoding). 20K chars should be sufficient to accommodate
 JOSE headers with an X.509 certificate chain in the `x5c`
 header parameter.

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
`protected `
`Header(Algorithm alg,
 JOSEObjectType typ,
 String cty,
 Set<String> crit,
 Map<String,Object> customParams,
 Base64URL parsedBase64URL)`

Creates a new abstract header.

`protected `
`Header(Header header)`

Deep copy constructor.

- 

## Method Summary

Modifier and Type
Method
Description
`Algorithm`
`getAlgorithm()`

Gets the algorithm (`alg`) parameter.

`String`
`getContentType()`

Gets the content type (`cty`) parameter.

`Set<String>`
`getCriticalParams()`

Gets the critical header parameters (`crit`) parameter.

`Object`
`getCustomParam(String name)`

Gets a custom (non-registered) parameter.

`Map<String,Object>`
`getCustomParams()`

Gets the custom (non-registered) parameters.

`Set<String>`
`getIncludedParams()`

Gets the names of all included parameters (registered and custom) in
 the header instance.

`Base64URL`
`getParsedBase64URL()`

Gets the original Base64URL used to create this header.

`JOSEObjectType`
`getType()`

Gets the type (`typ`) parameter.

`Header`
`join(UnprotectedHeader unprotected)`

Join a `PlainHeader`, `JWSHeader` or `JWEHeader`
 with an Unprotected header.

`static Header`
`parse(Base64URL base64URL)`

Parses a `PlainHeader`, `JWSHeader` or `JWEHeader`
 from the specified Base64URL.

`static Header`
`parse(String jsonString)`

Parses a `PlainHeader`, `JWSHeader` or `JWEHeader`
 from the specified JSON object string.

`static Header`
`parse(String jsonString,
 Base64URL parsedBase64URL)`

Parses a `PlainHeader`, `JWSHeader` or `JWEHeader`
 from the specified JSON object string.

`static Header`
`parse(Map<String,Object> jsonObject)`

Parses a `PlainHeader`, `JWSHeader` or `JWEHeader`
 from the specified JSON object.

`static Header`
`parse(Map<String,Object> jsonObject,
 Base64URL parsedBase64URL)`

Parses a `PlainHeader`, `JWSHeader` or `JWEHeader` 
 from the specified JSON object.

`static Algorithm`
`parseAlgorithm(Map<String,Object> json)`

Parses an algorithm (`alg`) parameter from the specified 
 header JSON object.

`Base64URL`
`toBase64URL()`

Returns a Base64URL representation of the header.

`Map<String,Object>`
`toJSONObject()`

Returns a JSON object representation of the header.

`String`
`toString()`

Returns a JSON string representation of the header.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Field Details

  - 

### MAX_HEADER_STRING_LENGTH

public static final int MAX_HEADER_STRING_LENGTH
The max allowed string length when parsing a JOSE header (after the
 BASE64URL decoding). 20K chars should be sufficient to accommodate
 JOSE headers with an X.509 certificate chain in the `x5c`
 header parameter.

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### Header

protected Header(Algorithm alg,
 JOSEObjectType typ,
 String cty,
 Set<String> crit,
 Map<String,Object> customParams,
 Base64URL parsedBase64URL)
Creates a new abstract header.

Parameters:
`alg` - The algorithm (`alg`) parameter. Must
                        not be `null`.
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

### Header

protected Header(Header header)
Deep copy constructor.

Parameters:
`header` - The header to copy. Must not be `null`.

- 

## Method Details

  - 

### getAlgorithm

public Algorithm getAlgorithm()
Gets the algorithm (`alg`) parameter.

Returns:
The algorithm parameter.

  - 

### getType

public JOSEObjectType getType()
Gets the type (`typ`) parameter.

Returns:
The type parameter, `null` if not specified.

  - 

### getContentType

public String getContentType()
Gets the content type (`cty`) parameter.

Returns:
The content type parameter, `null` if not specified.

  - 

### getCriticalParams

public Set<String> getCriticalParams()
Gets the critical header parameters (`crit`) parameter.

Returns:
The names of the critical header parameters, as a
         unmodifiable set, `null` if not specified.

  - 

### getCustomParam

public Object getCustomParam(String name)
Gets a custom (non-registered) parameter.

Parameters:
`name` - The name of the custom parameter. Must not be
             `null`.
Returns:
The custom parameter, `null` if not specified.

  - 

### getCustomParams

public Map<String,Object> getCustomParams()
Gets the custom (non-registered) parameters.

Returns:
The custom parameters, as a unmodifiable map, empty map if
         none.

  - 

### getParsedBase64URL

public Base64URL getParsedBase64URL()
Gets the original Base64URL used to create this header.

Returns:
The parsed Base64URL, `null` if the header was created
         from scratch.

  - 

### getIncludedParams

public Set<String> getIncludedParams()
Gets the names of all included parameters (registered and custom) in
 the header instance.

Returns:
The included parameters.

  - 

### toJSONObject

public Map<String,Object> toJSONObject()
Returns a JSON object representation of the header. All custom
 parameters are included if they serialise to a JSON entity and
 their names don't conflict with the registered ones.

Returns:
The JSON object representation of the header.

  - 

### toString

public String toString()
Returns a JSON string representation of the header. All custom
 parameters will be included if they serialise to a JSON entity and
 their names don't conflict with the registered ones.

Overrides:
`toString` in class `Object`
Returns:
The JSON string representation of the header.

  - 

### toBase64URL

public Base64URL toBase64URL()
Returns a Base64URL representation of the header. If the header was
 parsed always returns the original Base64URL (required for JWS
 validation and authenticated JWE decryption).

Returns:
The original parsed Base64URL representation of the header,
         or a new Base64URL representation if the header was created
         from scratch.

  - 

### parseAlgorithm

public static Algorithm parseAlgorithm(Map<String,Object> json)
                                throws ParseException
Parses an algorithm (`alg`) parameter from the specified 
 header JSON object. Intended for initial parsing of unsecured
 (plain), JWS and JWE headers.

 

The algorithm type (none, JWS or JWE) is determined by inspecting
 the algorithm name for "none" and the presence of an "enc"
 parameter.

Parameters:
`json` - The JSON object to parse. Must not be `null`.
Returns:
The algorithm, an instance of `Algorithm.NONE`,
         `JWSAlgorithm` or `JWEAlgorithm`. `null`
         if not found.
Throws:
`ParseException` - If the `alg` parameter couldn't be 
                        parsed.

  - 

### join

public Header join(UnprotectedHeader unprotected)
            throws ParseException
Join a `PlainHeader`, `JWSHeader` or `JWEHeader`
 with an Unprotected header.

Parameters:
`unprotected` - The Unprotected header. `null`
                        if not applicable.
Returns:
The header.
Throws:
`ParseException` - If the specified Unprotected header can not be
                        merged to protected header.

  - 

### parse

public static Header parse(Map<String,Object> jsonObject)
                    throws ParseException
Parses a `PlainHeader`, `JWSHeader` or `JWEHeader`
 from the specified JSON object.

Parameters:
`jsonObject` - The JSON object to parse. Must not be
                   `null`.
Returns:
The header.
Throws:
`ParseException` - If the specified JSON object doesn't
                        represent a valid header.

  - 

### parse

public static Header parse(Map<String,Object> jsonObject,
 Base64URL parsedBase64URL)
                    throws ParseException
Parses a `PlainHeader`, `JWSHeader` or `JWEHeader` 
 from the specified JSON object.

Parameters:
`jsonObject` - The JSON object to parse. Must not be
                        `null`.
`parsedBase64URL` - The original parsed Base64URL, `null`
                        if not applicable.
Returns:
The header.
Throws:
`ParseException` - If the specified JSON object doesn't 
                        represent a valid header.

  - 

### parse

public static Header parse(String jsonString)
                    throws ParseException
Parses a `PlainHeader`, `JWSHeader` or `JWEHeader`
 from the specified JSON object string.

Parameters:
`jsonString` - The JSON object string to parse. Must not be
                        `null`.
Returns:
The header.
Throws:
`ParseException` - If the specified JSON object string doesn't
                        represent a valid header.

  - 

### parse

public static Header parse(String jsonString,
 Base64URL parsedBase64URL)
                    throws ParseException
Parses a `PlainHeader`, `JWSHeader` or `JWEHeader`
 from the specified JSON object string.

Parameters:
`jsonString` - The JSON object string to parse. Must not be
                        `null`.
`parsedBase64URL` - The original parsed Base64URL, `null`
                        if not applicable.
Returns:
The header.
Throws:
`ParseException` - If the specified JSON object string doesn't
                        represent a valid header.

  - 

### parse

public static Header parse(Base64URL base64URL)
                    throws ParseException
Parses a `PlainHeader`, `JWSHeader` or `JWEHeader`
 from the specified Base64URL.

Parameters:
`base64URL` - The Base64URL to parse. Must not be `null`.
Returns:
The header.
Throws:
`ParseException` - If the specified Base64URL doesn't represent
                        a valid header.