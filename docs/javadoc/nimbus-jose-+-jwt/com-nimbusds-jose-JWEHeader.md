Package com.nimbusds.jose

# Class JWEHeader

java.lang.Object
com.nimbusds.jose.Header
com.nimbusds.jose.JWEHeader

All Implemented Interfaces:
`Serializable`

---

@Immutable
public final class JWEHeader
extends Header
JSON Web Encryption (JWE) header. This class is immutable.

 

Supports the following `registered
 header parameters`:

 

     
- alg
     
- enc
     
- epk
     
- zip
     
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
     
- apu
     
- apv
     
- p2s
     
- p2c
     
- iv
     
- tag
     
- skid
     
- iss
     
- sub
     
- aud
 

 

The header may also include `custom
 parameters`; these will be serialised and parsed along the registered ones.

 

Example header:

 

```

 { 
   "alg" : "RSA1_5",
   "enc" : "A128CBC-HS256"
 }
 
```

Version:
2024-10-01
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
`JWEHeader.Builder`

Builder for constructing JSON Web Encryption (JWE) headers.

- 

## Field Summary

### Fields inherited from class com.nimbusds.jose.Header

`MAX_HEADER_STRING_LENGTH`

- 

## Constructor Summary

Constructors

Constructor
Description
`JWEHeader(Algorithm alg,
 EncryptionMethod enc,
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
 JWK epk,
 CompressionAlgorithm zip,
 Base64URL apu,
 Base64URL apv,
 Base64URL p2s,
 int p2c,
 Base64URL iv,
 Base64URL tag,
 String skid,
 String iss,
 String sub,
 List<String> aud,
 Map<String,Object> customParams,
 Base64URL parsedBase64URL)`

Creates a new JSON Web Encryption (JWE) header.

`JWEHeader(Algorithm alg,
 EncryptionMethod enc,
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
 JWK epk,
 CompressionAlgorithm zip,
 Base64URL apu,
 Base64URL apv,
 Base64URL p2s,
 int p2c,
 Base64URL iv,
 Base64URL tag,
 String skid,
 Map<String,Object> customParams,
 Base64URL parsedBase64URL)`

Deprecated.

`JWEHeader(EncryptionMethod enc)`

Creates a new minimal JSON Web Encryption (JWE) header.

`JWEHeader(JWEAlgorithm alg,
 EncryptionMethod enc)`

Creates a new minimal JSON Web Encryption (JWE) header.

`JWEHeader(JWEHeader jweHeader)`

Deep copy constructor.

- 

## Method Summary

Modifier and Type
Method
Description
`Base64URL`
`getAgreementPartyUInfo()`

Gets the agreement PartyUInfo (`apu`) parameter.

`Base64URL`
`getAgreementPartyVInfo()`

Gets the agreement PartyVInfo (`apv`) parameter.

`JWEAlgorithm`
`getAlgorithm()`

Gets the algorithm (`alg`) parameter.

`List<String>`
`getAudience()`

Gets the audience (`aud`) claim as a parameter.

`Base64URL`
`getAuthTag()`

Gets the authentication tag (`tag`) parameter.

`CompressionAlgorithm`
`getCompressionAlgorithm()`

Gets the compression algorithm (`zip`) parameter.

`EncryptionMethod`
`getEncryptionMethod()`

Gets the encryption method (`enc`) parameter.

`JWK`
`getEphemeralPublicKey()`

Gets the Ephemeral Public Key (`epk`) parameter.

`Set<String>`
`getIncludedParams()`

Gets the names of all included parameters (registered and custom) in
 the header instance.

`String`
`getIssuer()`

Gets the issuer (`iss`) claim as a parameter.

`Base64URL`
`getIV()`

Gets the initialisation vector (`iv`) parameter.

`JWK`
`getJWK()`

Gets the public JSON Web Key (JWK) (`jwk`) parameter.

`URI`
`getJWKURL()`

Gets the public JSON Web Key (JWK) Set URL (`jku`) parameter.

`String`
`getKeyID()`

Gets the key ID (`kid`) parameter.

`int`
`getPBES2Count()`

Gets the PBES2 count (`p2c`) parameter.

`Base64URL`
`getPBES2Salt()`

Gets the PBES2 salt (`p2s`) parameter.

`static Set<String>`
`getRegisteredParameterNames()`

Gets the registered parameter names for JWE headers.

`String`
`getSenderKeyID()`

Gets the sender key ID (`skid`) parameter.

`String`
`getSubject()`

Gets the subject (`sub`) claim as a parameter.

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

`static JWEHeader`
`parse(Base64URL base64URL)`

Parses a JWE header from the specified Base64URL.

`static JWEHeader`
`parse(String jsonString)`

Parses a JWE header from the specified JSON object string.

`static JWEHeader`
`parse(String jsonString,
 Base64URL parsedBase64URL)`

Parses a JWE header from the specified JSON object string.

`static JWEHeader`
`parse(Map<String,Object> jsonObject)`

Parses a JWE header from the specified JSON object.

`static JWEHeader`
`parse(Map<String,Object> jsonObject,
 Base64URL parsedBase64URL)`

Parses a JWE header from the specified JSON object.

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

### JWEHeader

public JWEHeader(EncryptionMethod enc)
Creates a new minimal JSON Web Encryption (JWE) header.

Parameters:
`enc` - The encryption method parameter. Must not be
            `null`.

  - 

### JWEHeader

public JWEHeader(JWEAlgorithm alg,
 EncryptionMethod enc)
Creates a new minimal JSON Web Encryption (JWE) header.

 

Note: Use `PlainHeader` to create a header with algorithm
 `none`.

Parameters:
`alg` - The JWE algorithm parameter. Must not be "none" or
            `null`.
`enc` - The encryption method parameter. Must not be
            `null`.

  - 

### JWEHeader

@Deprecated
public JWEHeader(Algorithm alg,
 EncryptionMethod enc,
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
 JWK epk,
 CompressionAlgorithm zip,
 Base64URL apu,
 Base64URL apv,
 Base64URL p2s,
 int p2c,
 Base64URL iv,
 Base64URL tag,
 String skid,
 Map<String,Object> customParams,
 Base64URL parsedBase64URL)
Deprecated.
Creates a new JSON Web Encryption (JWE) header.

 

Note: Use `PlainHeader` to create a header with algorithm
 `none`.

Parameters:
`alg` - The JWE algorithm (`alg`) parameter.
                        `null` if not specified.
`enc` - The encryption method parameter. Must not be
                        `null`.
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
`epk` - The Ephemeral Public Key (`epk`)
                        parameter, `null` if not specified.
`zip` - The compression algorithm (`zip`)
                        parameter, `null` if not specified.
`apu` - The agreement PartyUInfo (`apu`)
                        parameter, `null` if not specified.
`apv` - The agreement PartyVInfo (`apv`)
                        parameter, `null` if not specified.
`p2s` - The PBES2 salt (`p2s`) parameter,
                        `null` if not specified.
`p2c` - The PBES2 count (`p2c`) parameter, zero
                        if not specified. Must not be negative.
`iv` - The initialisation vector (`iv`)
                        parameter, `null` if not specified.
`tag` - The authentication tag (`tag`)
                        parameter, `null` if not specified.
`skid` - The sender key ID (`skid`) parameter,
                        `null` if not specified.
`customParams` - The custom parameters, empty map or
                        `null` if none.
`parsedBase64URL` - The parsed Base64URL, `null` if the
                        header is created from scratch.

  - 

### JWEHeader

public JWEHeader(Algorithm alg,
 EncryptionMethod enc,
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
 JWK epk,
 CompressionAlgorithm zip,
 Base64URL apu,
 Base64URL apv,
 Base64URL p2s,
 int p2c,
 Base64URL iv,
 Base64URL tag,
 String skid,
 String iss,
 String sub,
 List<String> aud,
 Map<String,Object> customParams,
 Base64URL parsedBase64URL)
Creates a new JSON Web Encryption (JWE) header.

 

Note: Use `PlainHeader` to create a header with algorithm
 `none`.

Parameters:
`alg` - The JWE algorithm (`alg`) parameter.
                        `null` if not specified.
`enc` - The encryption method parameter. Must not be
                        `null`.
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
`epk` - The Ephemeral Public Key (`epk`)
                        parameter, `null` if not specified.
`zip` - The compression algorithm (`zip`)
                        parameter, `null` if not specified.
`apu` - The agreement PartyUInfo (`apu`)
                        parameter, `null` if not specified.
`apv` - The agreement PartyVInfo (`apv`)
                        parameter, `null` if not specified.
`p2s` - The PBES2 salt (`p2s`) parameter,
                        `null` if not specified.
`p2c` - The PBES2 count (`p2c`) parameter, zero
                        if not specified. Must not be negative.
`iv` - The initialisation vector (`iv`)
                        parameter, `null` if not specified.
`tag` - The authentication tag (`tag`)
                        parameter, `null` if not specified.
`skid` - The sender key ID (`skid`) parameter,
                        `null` if not specified.
`iss` - The issuer (`iss`) parameter as a
                        replicated claim, `null` if not
                        specified.
`sub` - The subject (`sub`) parameter as a
                        replicated claim, `null` if not
                        specified.
`aud` - The audience (`aud`) parameter as a
                        replicated claim, `null` if not
                        specified.
`customParams` - The custom parameters, empty map or
                        `null` if none.
`parsedBase64URL` - The parsed Base64URL, `null` if the
                        header is created from scratch.

  - 

### JWEHeader

public JWEHeader(JWEHeader jweHeader)
Deep copy constructor.

Parameters:
`jweHeader` - The JWE header to copy. Must not be `null`.

- 

## Method Details

  - 

### getRegisteredParameterNames

public static Set<String> getRegisteredParameterNames()
Gets the registered parameter names for JWE headers.

Returns:
The registered parameter names, as an unmodifiable set.

  - 

### getAlgorithm

public JWEAlgorithm getAlgorithm()
Gets the algorithm (`alg`) parameter.

Overrides:
`getAlgorithm` in class `Header`
Returns:
The algorithm parameter.

  - 

### getEncryptionMethod

public EncryptionMethod getEncryptionMethod()
Gets the encryption method (`enc`) parameter.

Returns:
The encryption method parameter.

  - 

### getEphemeralPublicKey

public JWK getEphemeralPublicKey()
Gets the Ephemeral Public Key (`epk`) parameter.

Returns:
The Ephemeral Public Key parameter, `null` if not
         specified.

  - 

### getCompressionAlgorithm

public CompressionAlgorithm getCompressionAlgorithm()
Gets the compression algorithm (`zip`) parameter.

Returns:
The compression algorithm parameter, `null` if not
         specified.

  - 

### getAgreementPartyUInfo

public Base64URL getAgreementPartyUInfo()
Gets the agreement PartyUInfo (`apu`) parameter.

Returns:
The agreement PartyUInfo parameter, `null` if not
         specified.

  - 

### getAgreementPartyVInfo

public Base64URL getAgreementPartyVInfo()
Gets the agreement PartyVInfo (`apv`) parameter.

Returns:
The agreement PartyVInfo parameter, `null` if not
         specified.

  - 

### getPBES2Salt

public Base64URL getPBES2Salt()
Gets the PBES2 salt (`p2s`) parameter.

Returns:
The PBES2 salt parameter, `null` if not specified.

  - 

### getPBES2Count

public int getPBES2Count()
Gets the PBES2 count (`p2c`) parameter.

Returns:
The PBES2 count parameter, zero if not specified.

  - 

### getIV

public Base64URL getIV()
Gets the initialisation vector (`iv`) parameter.

Returns:
The initialisation vector, `null` if not specified.

  - 

### getAuthTag

public Base64URL getAuthTag()
Gets the authentication tag (`tag`) parameter.

Returns:
The authentication tag, `null` if not specified.

  - 

### getSenderKeyID

public String getSenderKeyID()
Gets the sender key ID (`skid`) parameter.

Returns:
The sender key ID, `null` if not specified.

  - 

### getIssuer

public String getIssuer()
Gets the issuer (`iss`) claim as a parameter.

Returns:
The issuer claim, `null` if not specified.

  - 

### getSubject

public String getSubject()
Gets the subject (`sub`) claim as a parameter.

Returns:
The subject claim, `null` if not specified.

  - 

### getAudience

public List<String> getAudience()
Gets the audience (`aud`) claim as a parameter.

Returns:
The audience claim, empty list if not specified.

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

public static JWEHeader parse(Map<String,Object> jsonObject)
                       throws ParseException
Parses a JWE header from the specified JSON object.

Parameters:
`jsonObject` - The JSON object to parse. Must not be
                   `null`.
Returns:
The JWE header.
Throws:
`ParseException` - If the specified JSON object doesn't
                        represent a valid JWE header.

  - 

### parse

public static JWEHeader parse(Map<String,Object> jsonObject,
 Base64URL parsedBase64URL)
                       throws ParseException
Parses a JWE header from the specified JSON object.

Parameters:
`jsonObject` - The JSON object to parse. Must not be
                        `null`.
`parsedBase64URL` - The original parsed Base64URL, `null`
                        if not applicable.
Returns:
The JWE header.
Throws:
`ParseException` - If the specified JSON object doesn't 
                        represent a valid JWE header.

  - 

### parse

public static JWEHeader parse(String jsonString)
                       throws ParseException
Parses a JWE header from the specified JSON object string.

Parameters:
`jsonString` - The JSON object string to parse. Must not be `null`.
Returns:
The JWE header.
Throws:
`ParseException` - If the specified JSON object string doesn't 
                        represent a valid JWE header.

  - 

### parse

public static JWEHeader parse(String jsonString,
 Base64URL parsedBase64URL)
                       throws ParseException
Parses a JWE header from the specified JSON object string.

Parameters:
`jsonString` - The JSON string to parse. Must not be
                        `null`.
`parsedBase64URL` - The original parsed Base64URL, `null`
                        if not applicable.
Returns:
The JWE header.
Throws:
`ParseException` - If the specified JSON object string doesn't
                        represent a valid JWE header.

  - 

### parse

public static JWEHeader parse(Base64URL base64URL)
                       throws ParseException
Parses a JWE header from the specified Base64URL.

Parameters:
`base64URL` - The Base64URL to parse. Must not be `null`.
Returns:
The JWE header.
Throws:
`ParseException` - If the specified Base64URL doesn't represent
                        a valid JWE header.

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