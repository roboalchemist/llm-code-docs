Package com.nimbusds.jose.jwk

# Class JWKSet

java.lang.Object
com.nimbusds.jose.jwk.JWKSet

All Implemented Interfaces:
`Serializable`

---

@Immutable
public class JWKSet
extends Object
implements Serializable
JSON Web Key (JWK) set. Represented by a JSON object that contains an array
 of `JSON Web Keys` (JWKs) as the value of its "keys" member.
 Additional (custom) members of the JWK Set JSON object are also supported.

 

Example JWK set:

 

```

 {
   "keys" : [ { "kty" : "EC",
                "crv" : "P-256",
                "x"   : "MKBCTNIcKUSDii11ySs3526iDZ8AiTo7Tu6KPAqv7D4",
                "y"   : "4Etl6SRW2YiLUrN5vfvVHuhp7x8PxltmWWlbbM4IFyM",
                "use" : "enc",
                "kid" : "1" },

              { "kty" : "RSA",
                "n"   : "0vx7agoebGcQSuuPiLJXZptN9nndrQmbXEps2aiAFbWhM78LhWx
                         4cbbfAAtVT86zwu1RK7aPFFxuhDR1L6tSoc_BJECPebWKRXjBZCiFV4n3oknjhMs
                         tn64tZ_2W-5JsGY4Hc5n9yBXArwl93lqt7_RN5w6Cf0h4QyQ5v-65YGjQR0_FDW2
                         QvzqY368QQMicAtaSqzs8KJZgnYb9c7d0zgdAZHzu6qMQvRL5hajrn1n91CbOpbI
                         SD08qNLyrdkt-bFTWhAI4vMQFh6WeZu0fM4lFd2NcRwr3XPksINHaQ-G_xBniIqb
                         w0Ls1jF44-csFCur-kEgU8awapJzKnqDKgw",
                "e"   : "AQAB",
                "alg" : "RS256",
                "kid" : "2011-04-29" } ]
 }
 
```

Version:
2024-03-17
Author:
Vladimir Dzhuvinov, Vedran Pavic
See Also:

- Serialized Form

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`MIME_TYPE`

The MIME type of JWK set objects: 
 `application/jwk-set+json; charset=UTF-8`

- 

## Constructor Summary

Constructors

Constructor
Description
`JWKSet()`

Creates a new empty JWK set.

`JWKSet(JWK key)`

Creates a new JWK set with a single key.

`JWKSet(List<JWK> keys)`

Creates a new JWK set with the specified keys.

`JWKSet(List<JWK> keys,
 Map<String,Object> customMembers)`

Creates a new JWK set with the specified keys and additional custom
 members.

- 

## Method Summary

Modifier and Type
Method
Description
`boolean`
`containsJWK(JWK jwk)`

Returns `true` if this JWK set contains the specified JWK as
 public or private key, by comparing its thumbprint with those of the
 keys in the set.

`boolean`
`containsNonPublicKeys()`

Returns `true` if this JWK set contains non-public keys.

`boolean`
`equals(Object o)`
 
`JWKSet`
`filter(JWKMatcher jwkMatcher)`

Filters the keys in this JWK set.

`Map<String,Object>`
`getAdditionalMembers()`

Returns the additional custom members of this (JWK) set.

`JWK`
`getKeyByKeyId(String kid)`

Returns the key from this JWK set as identified by its Key ID (kid)
 member.

`List<JWK>`
`getKeys()`

Returns the keys (ordered) of this JWK set.

`int`
`hashCode()`
 
`boolean`
`isEmpty()`

Returns `true` if this JWK set is empty.

`static JWKSet`
`load(File file)`

Loads a JWK set from the specified file.

`static JWKSet`
`load(InputStream inputStream)`

Loads a JWK set from the specified input stream.

`static JWKSet`
`load(URL url)`

Loads a JWK set from the specified URL.

`static JWKSet`
`load(URL url,
 int connectTimeout,
 int readTimeout,
 int sizeLimit)`

Loads a JWK set from the specified URL.

`static JWKSet`
`load(URL url,
 int connectTimeout,
 int readTimeout,
 int sizeLimit,
 Proxy proxy)`

Loads a JWK set from the specified URL.

`static JWKSet`
`load(KeyStore keyStore,
 PasswordLookup pwLookup)`

Loads a JWK set from the specified JCA key store.

`static JWKSet`
`parse(String s)`

Parses the specified string representing a JWK set.

`static JWKSet`
`parse(Map<String,Object> json)`

Parses the specified JSON object representing a JWK set.

`int`
`size()`

Returns the number of keys in this JWK set.

`Map<String,Object>`
`toJSONObject()`

Returns the JSON object representation of this JWK set.

`Map<String,Object>`
`toJSONObject(boolean publicKeysOnly)`

Returns the JSON object representation of this JWK set.

`JWKSet`
`toPublicJWKSet()`

Returns a copy of this (JWK) set with all private keys and
 parameters removed.

`String`
`toString()`

Returns the JSON object string representation of this JWK set.

`String`
`toString(boolean publicKeysOnly)`

Returns the JSON object string representation of this JWK set.

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Field Details

  - 

### MIME_TYPE

public static final String MIME_TYPE
The MIME type of JWK set objects: 
 `application/jwk-set+json; charset=UTF-8`

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### JWKSet

public JWKSet()
Creates a new empty JWK set.

  - 

### JWKSet

public JWKSet(JWK key)
Creates a new JWK set with a single key.

Parameters:
`key` - The JWK. Must not be `null`.

  - 

### JWKSet

public JWKSet(List<JWK> keys)
Creates a new JWK set with the specified keys.

Parameters:
`keys` - The JWK list. Must not be `null`.

  - 

### JWKSet

public JWKSet(List<JWK> keys,
 Map<String,Object> customMembers)
Creates a new JWK set with the specified keys and additional custom
 members.

Parameters:
`keys` - The JWK list. Must not be `null`.
`customMembers` - The additional custom members. Must not be
                      `null`.

- 

## Method Details

  - 

### getKeys

public List<JWK> getKeys()
Returns the keys (ordered) of this JWK set.

Returns:
The keys as an unmodifiable list, empty list if none.

  - 

### isEmpty

public boolean isEmpty()
Returns `true` if this JWK set is empty.

Returns:
`true` if empty, else `false`.

  - 

### size

public int size()
Returns the number of keys in this JWK set.

Returns:
The number of keys, zero if none.

  - 

### getKeyByKeyId

public JWK getKeyByKeyId(String kid)
Returns the key from this JWK set as identified by its Key ID (kid)
 member.

 

If more than one key exists in the JWK Set with the same
 identifier, this function returns only the first one in the set.

Parameters:
`kid` - They key identifier.
Returns:
The key identified by `kid` or `null` if no key
         exists.

  - 

### containsJWK

public boolean containsJWK(JWK jwk)
                    throws JOSEException
Returns `true` if this JWK set contains the specified JWK as
 public or private key, by comparing its thumbprint with those of the
 keys in the set.

Parameters:
`jwk` - The JWK to check. Must not be `null`.
Returns:
`true` if contained, `false` if not.
Throws:
`JOSEException` - If thumbprint computation failed.

  - 

### getAdditionalMembers

public Map<String,Object> getAdditionalMembers()
Returns the additional custom members of this (JWK) set.

Returns:
The additional custom members as an unmodifiable map, empty
         map if none.

  - 

### toPublicJWKSet

public JWKSet toPublicJWKSet()
Returns a copy of this (JWK) set with all private keys and
 parameters removed.

Returns:
A copy of this JWK set with all private keys and parameters
         removed.

  - 

### filter

public JWKSet filter(JWKMatcher jwkMatcher)
Filters the keys in this JWK set.

Parameters:
`jwkMatcher` - The JWK matcher to filter the keys. Must not be
                   `null`.
Returns:
The new filtered JWK set.

  - 

### containsNonPublicKeys

public boolean containsNonPublicKeys()
Returns `true` if this JWK set contains non-public keys.

Returns:
`true` if non-public keys are found, `false` if
         there are only public keys in the JWK set.

  - 

### toJSONObject

public Map<String,Object> toJSONObject()
Returns the JSON object representation of this JWK set. Only public
 keys will be included. Use the alternative
 `toJSONObject(boolean)` method to include all key material.

Returns:
The JSON object representation.

  - 

### toJSONObject

public Map<String,Object> toJSONObject(boolean publicKeysOnly)
Returns the JSON object representation of this JWK set.

Parameters:
`publicKeysOnly` - Controls the inclusion of private keys and
                       parameters into the output JWK members. If
                       `true` only public keys will be
                       included. If `false` all available keys
                       with their parameters will be included.
Returns:
The JSON object representation.

  - 

### toString

public String toString(boolean publicKeysOnly)
Returns the JSON object string representation of this JWK set.

Parameters:
`publicKeysOnly` - Controls the inclusion of private keys and
                       parameters into the output JWK members. If
                       `true` only public keys will be
                       included. If `false` all available keys
                       with their parameters will be included.
Returns:
The JSON object string representation.

  - 

### toString

public String toString()
Returns the JSON object string representation of this JWK set. Only
 public keys will be included. Use the alternative
 `toString(boolean)` method to include all key material.

Overrides:
`toString` in class `Object`
Returns:
The JSON object string representation. Only public keys will
         be included.

  - 

### equals

public boolean equals(Object o)

Overrides:
`equals` in class `Object`

  - 

### hashCode

public int hashCode()

Overrides:
`hashCode` in class `Object`

  - 

### parse

public static JWKSet parse(String s)
                    throws ParseException
Parses the specified string representing a JWK set.

Parameters:
`s` - The string to parse. Must not be `null`.
Returns:
The JWK set.
Throws:
`ParseException` - If the string couldn't be parsed to a valid
                        JWK set.

  - 

### parse

public static JWKSet parse(Map<String,Object> json)
                    throws ParseException
Parses the specified JSON object representing a JWK set.

Parameters:
`json` - The JSON object to parse. Must not be `null`.
Returns:
The JWK set.
Throws:
`ParseException` - If the string couldn't be parsed to a valid
                        JWK set.

  - 

### load

public static JWKSet load(InputStream inputStream)
                   throws IOException,
ParseException
Loads a JWK set from the specified input stream.

Parameters:
`inputStream` - The JWK set input stream. Must not be `null`.
Returns:
The JWK set.
Throws:
`IOException` - If the input stream couldn't be read.
`ParseException` - If the input stream couldn't be parsed to a
                        valid JWK set.

  - 

### load

public static JWKSet load(File file)
                   throws IOException,
ParseException
Loads a JWK set from the specified file.

Parameters:
`file` - The JWK set file. Must not be `null`.
Returns:
The JWK set.
Throws:
`IOException` - If the file couldn't be read.
`ParseException` - If the file couldn't be parsed to a valid JWK
                        set.

  - 

### load

public static JWKSet load(URL url,
 int connectTimeout,
 int readTimeout,
 int sizeLimit)
                   throws IOException,
ParseException
Loads a JWK set from the specified URL.

Parameters:
`url` - The JWK set URL. Must not be `null`.
`connectTimeout` - The URL connection timeout, in milliseconds.
                       If zero no (infinite) timeout.
`readTimeout` - The URL read timeout, in milliseconds. If zero
                       no (infinite) timeout.
`sizeLimit` - The read size limit, in bytes. If zero no
                       limit.
Returns:
The JWK set.
Throws:
`IOException` - If the file couldn't be read.
`ParseException` - If the file couldn't be parsed to a valid JWK
                        set.

  - 

### load

public static JWKSet load(URL url,
 int connectTimeout,
 int readTimeout,
 int sizeLimit,
 Proxy proxy)
                   throws IOException,
ParseException
Loads a JWK set from the specified URL.

Parameters:
`url` - The JWK set URL. Must not be `null`.
`connectTimeout` - The URL connection timeout, in milliseconds.
                       If zero no (infinite) timeout.
`readTimeout` - The URL read timeout, in milliseconds. If zero
                       no (infinite) timeout.
`sizeLimit` - The read size limit, in bytes. If zero no
                       limit.
`proxy` - The optional proxy to use when opening the
                       connection to retrieve the resource. If
                       `null`, no proxy is used.
Returns:
The JWK set.
Throws:
`IOException` - If the file couldn't be read.
`ParseException` - If the file couldn't be parsed to a valid JWK
                        set.

  - 

### load

public static JWKSet load(URL url)
                   throws IOException,
ParseException
Loads a JWK set from the specified URL.

Parameters:
`url` - The JWK set URL. Must not be `null`.
Returns:
The JWK set.
Throws:
`IOException` - If the file couldn't be read.
`ParseException` - If the file couldn't be parsed to a valid JWK
                        set.

  - 

### load

public static JWKSet load(KeyStore keyStore,
 PasswordLookup pwLookup)
                   throws KeyStoreException
Loads a JWK set from the specified JCA key store. Key
 conversion exceptions are silently swallowed. PKCS#11 stores are
 also supported. Requires BouncyCastle.

 

**Important:** The X.509 certificates are not
 validated!

Parameters:
`keyStore` - The key store. Must not be `null`.
`pwLookup` - The password lookup for password-protected keys,
                 `null` if not specified.
Returns:
The JWK set, empty if no keys were loaded.
Throws:
`KeyStoreException` - On a key store exception.