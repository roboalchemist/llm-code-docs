Package com.nimbusds.jose

# Class JWSHeader

java.lang.Object
com.nimbusds.jose.Header
com.nimbusds.jose.JWSHeader

All Implemented Interfaces:
`Serializable`

---

@Immutable
public final class JWSHeader
extends Header
JSON Web Signature (JWS) header. This class is immutable.

 

Supports the following `registered
 header parameters`:

 

     
- alg
     
- jku
     
- jwk
     
- x5u
     
- x5t
     
- x5t#S256
     
- x5c
     
- kid
     
- typ
     
- cty
     
- crit
     
- b64
 

 

The header may also include `custom
 parameters`; these will be serialised and parsed along the registered ones.

 

Example header of a JSON Web Signature (JWS) object using the 
 `HMAC SHA-256 algorithm`:

 

```

 {
   "alg" : "HS256"
 }
 
```

Version:
2024-04-20
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
`JWSHeader.Builder`

Builder for constructing JSON Web Signature (JWS) headers.

- 

## Field Summary

### Fields inherited from class com.nimbusds.jose.Header

`MAX_HEADER_STRING_LENGTH`

- 

## Constructor Summary

Constructors

Constructor
Description
`JWSHeader(JWSAlgorithm alg)`

Creates a new minimal JSON Web Signature (JWS) header.

`JWSHeader(JWSAlgorithm alg,
 JOSEObjectType typ,
 String cty,
 Set<String> crit,
 URI jku,
 JWK jwk,
 URI x5u,
 Base64URL x5t,
 Base64URL x5t256,
 List<Base64> x5c,
 String kid,
 boolean b64,
 Map<String,Object> customParams,
 Base64URL parsedBase64URL)`

Creates a new JSON Web Signature (JWS) header.

`JWSHeader(JWSAlgorithm alg,
 JOSEObjectType typ,
 String cty,
 Set<String> crit,
 URI jku,
 JWK jwk,
 URI x5u,
 Base64URL x5t,
 Base64URL x5t256,
 List<Base64> x5c,
 String kid,
 Map<String,Object> customParams,
 Base64URL parsedBase64URL)`

Deprecated.

`JWSHeader(JWSHeader jwsHeader)`

Deep copy constructor.

- 

## Method Summary

Modifier and Type
Method
Description
`JWSAlgorithm`
`getAlgorithm()`

Gets the algorithm (`alg`) parameter.

`Set<String>`
`getIncludedParams()`

Gets the names of all included parameters (registered and custom) in
 the header instance.

`JWK`
`getJWK()`

Gets the public JSON Web Key (JWK) (`jwk`) parameter.

`URI`
`getJWKURL()`

Gets the public JSON Web Key (JWK) Set URL (`jku`) parameter.

`String`
`getKeyID()`

Gets the key ID (`kid`) parameter.

`static Set<String>`
`getRegisteredParameterNames()`

Gets the registered parameter names for JWS headers.

`List<Base64>`
`getX509CertChain()`

Gets the X.509 certificate chain (`x5c`) parameter
 corresponding to the key used to sign or encrypt the JWS / JWE
 object.

`Base64URL`
`getX509CertSHA256Thumbprint()`

Gets the X.509 certificate SHA-256 thumbprint (`x5t#S256`)
 parameter.

`Base64URL`
`getX509CertThumbprint()`

Deprecated.

`URI`
`getX509CertURL()`

Gets the X.509 certificate URL (`x5u`) parameter.

`boolean`
`isBase64URLEncodePayload()`

Returns the Base64URL-encode payload (`b64`) parameter.

`static JWSHeader`
`parse(Base64URL base64URL)`

Parses a JWS header from the specified Base64URL.

`static JWSHeader`
`parse(String jsonString)`

Parses a JWS header from the specified JSON object string.

`static JWSHeader`
`parse(String jsonString,
 Base64URL parsedBase64URL)`

Parses a JWS header from the specified JSON object string.

`static JWSHeader`
`parse(Map<String,Object> jsonObject)`

Parses a JWS header from the specified JSON object.

`static JWSHeader`
`parse(Map<String,Object> jsonObject,
 Base64URL parsedBase64URL)`

Parses a JWS header from the specified JSON object.

`Map<String,Object>`
`toJSONObject()`

Returns a JSON object representation of the header.

### Methods inherited from class com.nimbusds.jose.Header

`getContentType, getCriticalParams, getCustomParam, getCustomParams, getParsedBase64URL, getType, join, parseAlgorithm, toBase64URL, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### JWSHeader

public JWSHeader(JWSAlgorithm alg)
Creates a new minimal JSON Web Signature (JWS) header.

 

Note: Use `PlainHeader` to create a header with algorithm
 `none`.

Parameters:
`alg` - The JWS algorithm (`alg`) parameter. Must not be
            "none" or `null`.

  - 

### JWSHeader

@Deprecated
public JWSHeader(JWSAlgorithm alg,
 JOSEObjectType typ,
 String cty,
 Set<String> crit,
 URI jku,
 JWK jwk,
 URI x5u,
 Base64URL x5t,
 Base64URL x5t256,
 List<Base64> x5c,
 String kid,
 Map<String,Object> customParams,
 Base64URL parsedBase64URL)
Deprecated.
Creates a new JSON Web Signature (JWS) header.

 

Note: Use `PlainHeader` to create a header with algorithm
 `none`.

Parameters:
`alg` - The JWS algorithm (`alg`) parameter.
                        Must not be "none" or `null`.
`typ` - The type (`typ`) parameter,
                        `null` if not specified.
`cty` - The content type (`cty`) parameter,
                        `null` if not specified.
`crit` - The names of the critical header
                        (`crit`) parameters, empty set or
                        `null` if none.
`jku` - The JSON Web Key (JWK) Set URL (`jku`)
                        parameter, `null` if not specified.
`jwk` - The X.509 certificate URL (`jwk`)
                        parameter, `null` if not specified.
`x5u` - The X.509 certificate URL parameter
                        (`x5u`), `null` if not specified.
`x5t` - The X.509 certificate SHA-1 thumbprint
                        (`x5t`) parameter, `null` if not
                        specified.
`x5t256` - The X.509 certificate SHA-256 thumbprint
                        (`x5t#S256`) parameter, `null` if
                        not specified.
`x5c` - The X.509 certificate chain (`x5c`)
                        parameter, `null` if not specified.
`kid` - The key ID (`kid`) parameter,
                        `null` if not specified.
`customParams` - The custom parameters, empty map or
                        `null` if none.
`parsedBase64URL` - The parsed Base64URL, `null` if the
                        header is created from scratch.

  - 

### JWSHeader

public JWSHeader(JWSAlgorithm alg,
 JOSEObjectType typ,
 String cty,
 Set<String> crit,
 URI jku,
 JWK jwk,
 URI x5u,
 Base64URL x5t,
 Base64URL x5t256,
 List<Base64> x5c,
 String kid,
 boolean b64,
 Map<String,Object> customParams,
 Base64URL parsedBase64URL)
Creates a new JSON Web Signature (JWS) header.

 

Note: Use `PlainHeader` to create a header with algorithm
 `none`.

Parameters:
`alg` - The JWS algorithm (`alg`) parameter.
                        Must not be "none" or `null`.
`typ` - The type (`typ`) parameter,
                        `null` if not specified.
`cty` - The content type (`cty`) parameter,
                        `null` if not specified.
`crit` - The names of the critical header
                        (`crit`) parameters, empty set or
                        `null` if none.
`jku` - The JSON Web Key (JWK) Set URL (`jku`)
                        parameter, `null` if not specified.
`jwk` - The X.509 certificate URL (`jwk`)
                        parameter, `null` if not specified.
`x5u` - The X.509 certificate URL parameter
                        (`x5u`), `null` if not specified.
`x5t` - The X.509 certificate SHA-1 thumbprint
                        (`x5t`) parameter, `null` if not
                        specified.
`x5t256` - The X.509 certificate SHA-256 thumbprint
                        (`x5t#S256`) parameter, `null` if
                        not specified.
`x5c` - The X.509 certificate chain (`x5c`)
                        parameter, `null` if not specified.
`kid` - The key ID (`kid`) parameter,
                        `null` if not specified.
`b64` - `true` to Base64URL encode the payload
                        for standard JWS serialisation, `false`
                        for unencoded payload (RFC 7797).
`customParams` - The custom parameters, empty map or
                        `null` if none.
`parsedBase64URL` - The parsed Base64URL, `null` if the
                        header is created from scratch.

  - 

### JWSHeader

public JWSHeader(JWSHeader jwsHeader)
Deep copy constructor.

Parameters:
`jwsHeader` - The JWS header to copy. Must not be `null`.

- 

## Method Details

  - 

### getRegisteredParameterNames

public static Set<String> getRegisteredParameterNames()
Gets the registered parameter names for JWS headers.

Returns:
The registered parameter names, as an unmodifiable set.

  - 

### getAlgorithm

public JWSAlgorithm getAlgorithm()
Gets the algorithm (`alg`) parameter.

Overrides:
`getAlgorithm` in class `Header`
Returns:
The algorithm parameter.

  - 

### isBase64URLEncodePayload

public boolean isBase64URLEncodePayload()
Returns the Base64URL-encode payload (`b64`) parameter.

Returns:
`true` to Base64URL encode the payload for standard
         JWS serialisation, `false` for unencoded payload (RFC
         7797).

  - 

### getIncludedParams

public Set<String> getIncludedParams()
Description copied from class: `Header`
Gets the names of all included parameters (registered and custom) in
 the header instance.

Returns:
The included parameters.

  - 

### toJSONObject

public Map<String,Object> toJSONObject()
Description copied from class: `Header`
Returns a JSON object representation of the header. All custom
 parameters are included if they serialise to a JSON entity and
 their names don't conflict with the registered ones.

Returns:
The JSON object representation of the header.

  - 

### parse

public static JWSHeader parse(Map<String,Object> jsonObject)
                       throws ParseException
Parses a JWS header from the specified JSON object.

Parameters:
`jsonObject` - The JSON object to parse. Must not be
                   `null`.
Returns:
The JWS header.
Throws:
`ParseException` - If the specified JSON object doesn't
                        represent a valid JWS header.

  - 

### parse

public static JWSHeader parse(Map<String,Object> jsonObject,
 Base64URL parsedBase64URL)
                       throws ParseException
Parses a JWS header from the specified JSON object.

Parameters:
`jsonObject` - The JSON object to parse. Must not be
                        `null`.
`parsedBase64URL` - The original parsed Base64URL, `null`
                        if not applicable.
Returns:
The JWS header.
Throws:
`ParseException` - If the specified JSON object doesn't 
                        represent a valid JWS header.

  - 

### parse

public static JWSHeader parse(String jsonString)
                       throws ParseException
Parses a JWS header from the specified JSON object string.

Parameters:
`jsonString` - The JSON string to parse. Must not be
                   `null`.
Returns:
The JWS header.
Throws:
`ParseException` - If the specified JSON object string doesn't
                        represent a valid JWS header.

  - 

### parse

public static JWSHeader parse(String jsonString,
 Base64URL parsedBase64URL)
                       throws ParseException
Parses a JWS header from the specified JSON object string.

Parameters:
`jsonString` - The JSON string to parse. Must not be
                        `null`.
`parsedBase64URL` - The original parsed Base64URL, `null`
                        if not applicable.
Returns:
The JWS header.
Throws:
`ParseException` - If the specified JSON object string doesn't 
                        represent a valid JWS header.

  - 

### parse

public static JWSHeader parse(Base64URL base64URL)
                       throws ParseException
Parses a JWS header from the specified Base64URL.

Parameters:
`base64URL` - The Base64URL to parse. Must not be `null`.
Returns:
The JWS header.
Throws:
`ParseException` - If the specified Base64URL doesn't represent
                        a valid JWS header.

  - 

### getJWKURL

public URI getJWKURL()
Gets the public JSON Web Key (JWK) Set URL (`jku`) parameter.

Returns:
The public JSON Web Key (JWK) Set URL parameter,
         `null` if not specified.

  - 

### getJWK

public JWK getJWK()
Gets the public JSON Web Key (JWK) (`jwk`) parameter.

Returns:
The public JSON Web Key (JWK) parameter, `null` if not
         specified.

  - 

### getX509CertURL

public URI getX509CertURL()
Gets the X.509 certificate URL (`x5u`) parameter.

Returns:
The X.509 certificate URL parameter, `null` if not
         specified.

  - 

### getX509CertThumbprint

@Deprecated
public Base64URL getX509CertThumbprint()
Deprecated.
Gets the X.509 certificate SHA-1 thumbprint (`x5t`) parameter.

Returns:
The X.509 certificate SHA-1 thumbprint parameter,
         `null` if not specified.

  - 

### getX509CertSHA256Thumbprint

public Base64URL getX509CertSHA256Thumbprint()
Gets the X.509 certificate SHA-256 thumbprint (`x5t#S256`)
 parameter.

Returns:
The X.509 certificate SHA-256 thumbprint parameter,
         `null` if not specified.

  - 

### getX509CertChain

public List<Base64> getX509CertChain()
Gets the X.509 certificate chain (`x5c`) parameter
 corresponding to the key used to sign or encrypt the JWS / JWE
 object.

Returns:
The X.509 certificate chain parameter as a unmodifiable
         list, `null` if not specified.

  - 

### getKeyID

public String getKeyID()
Gets the key ID (`kid`) parameter.

Returns:
The key ID parameter, `null` if not specified.