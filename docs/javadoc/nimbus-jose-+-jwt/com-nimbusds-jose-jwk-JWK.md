Package com.nimbusds.jose.jwk

# Class JWK

java.lang.Object
com.nimbusds.jose.jwk.JWK

All Implemented Interfaces:
`Serializable`

Direct Known Subclasses:
`ECKey`, `OctetKeyPair`, `OctetSequenceKey`, `RSAKey`

---

public abstract class JWK
extends Object
implements Serializable
The base abstract class for JSON Web Keys (JWKs). It serialises to a JSON
 object.

 

The following JSON object members are common to all JWK types:

 

     
- `kty` (required)
     
- `use` (optional)
     
- `key_ops` (optional)
     
- `kid` (optional)
     
- `x5u` (optional)
     
- `x5t` (optional)
     
- `x5t#S256` (optional)
     
- `x5c` (optional)
     
- `exp` (optional)
     
- `nbf` (optional)
     
- `iat` (optional)
     
- `revoked` (optional)
     
- `getKeyStore()`
 

 

Example JWK (of the Elliptic Curve type):

 

```

 {
   "kty" : "EC",
   "crv" : "P-256",
   "x"   : "MKBCTNIcKUSDii11ySs3526iDZ8AiTo7Tu6KPAqv7D4",
   "y"   : "4Etl6SRW2YiLUrN5vfvVHuhp7x8PxltmWWlbbM4IFyM",
   "use" : "enc",
   "kid" : "1"
 }
 
```

Version:
2024-10-31
Author:
Vladimir Dzhuvinov, Justin Richer, Stefan Larsson
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

The MIME type of JWK objects: 
 `application/jwk+json; charset=UTF-8`

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
`protected `
`JWK(KeyType kty,
 KeyUse use,
 Set<KeyOperation> ops,
 Algorithm alg,
 String kid,
 URI x5u,
 Base64URL x5t,
 Base64URL x5t256,
 List<Base64> x5c,
 KeyStore ks)`

Deprecated.

`protected `
`JWK(KeyType kty,
 KeyUse use,
 Set<KeyOperation> ops,
 Algorithm alg,
 String kid,
 URI x5u,
 Base64URL x5t,
 Base64URL x5t256,
 List<Base64> x5c,
 Date exp,
 Date nbf,
 Date iat,
 KeyRevocation revocation,
 KeyStore ks)`

Creates a new JSON Web Key (JWK).

`protected `
`JWK(KeyType kty,
 KeyUse use,
 Set<KeyOperation> ops,
 Algorithm alg,
 String kid,
 URI x5u,
 Base64URL x5t,
 Base64URL x5t256,
 List<Base64> x5c,
 Date exp,
 Date nbf,
 Date iat,
 KeyStore ks)`

Deprecated.

- 

## Method Summary

Modifier and Type
Method
Description
`Base64URL`
`computeThumbprint()`

Computes the SHA-256 thumbprint of this JWK.

`Base64URL`
`computeThumbprint(String hashAlg)`

Computes the thumbprint of this JWK using the specified hash
 algorithm.

`ThumbprintURI`
`computeThumbprintURI()`

Computes the SHA-256 thumbprint URI of this JWK.

`boolean`
`equals(Object o)`
 
`Algorithm`
`getAlgorithm()`

Returns the intended JOSE algorithm (`alg`) for this JWK.

`Date`
`getExpirationTime()`

Returns the expiration time (`exp`) if this JWK.

`Date`
`getIssueTime()`

Returns the issued-at (`iat`) time of this JWK.

`String`
`getKeyID()`

Returns the ID (`kid`) of this JWK.

`Set<KeyOperation>`
`getKeyOperations()`

Returns the operations (`key_ops`) for this JWK.

`KeyRevocation`
`getKeyRevocation()`

Returns the key revocation (`revoked`) of this JWK.

`KeyStore`
`getKeyStore()`

Returns a reference to the underlying key store.

`KeyType`
`getKeyType()`

Returns the type (`kty`) of this JWK.

`KeyUse`
`getKeyUse()`

Returns the use (`use`) of this JWK.

`Date`
`getNotBeforeTime()`

Returns the not-before (`nbf`) of this JWK.

`List<X509Certificate>`
`getParsedX509CertChain()`

Returns the parsed X.509 certificate chain (`x5c`) of this
 JWK.

`abstract LinkedHashMap<String,?>`
`getRequiredParams()`

Returns the required JWK parameters.

`List<Base64>`
`getX509CertChain()`

Returns the X.509 certificate chain (`x5c`) of this JWK.

`Base64URL`
`getX509CertSHA256Thumbprint()`

Returns the X.509 certificate SHA-256 thumbprint (`x5t#S256`)
 of this JWK.

`Base64URL`
`getX509CertThumbprint()`

Deprecated.

`URI`
`getX509CertURL()`

Returns the X.509 certificate URL (`x5u`) of this JWK.

`int`
`hashCode()`
 
`abstract boolean`
`isPrivate()`

Returns `true` if this JWK contains private or sensitive
 (non-public) parameters.

`static JWK`
`load(KeyStore keyStore,
 String alias,
 char[] pin)`

Loads a JWK from the specified JCE key store.

`static JWK`
`parse(String s)`

Parses a JWK from the specified JSON object string representation.

`static JWK`
`parse(X509Certificate cert)`

Parses a public `RSA` or `EC JWK` from the
 specified X.509 certificate.

`static JWK`
`parse(Map<String,Object> jsonObject)`

Parses a JWK from the specified JSON object representation.

`static JWK`
`parseFromPEMEncodedObjects(String pemEncodedObjects)`

Parses an RSA or EC JWK from the specified string of one or more
 PEM-encoded object(s):

 
     X.509 certificate (PEM header: BEGIN CERTIFICATE)
     PKCS#1 RSAPublicKey (PEM header: BEGIN RSA PUBLIC KEY)
     X.509 SubjectPublicKeyInfo (PEM header: BEGIN PUBLIC KEY)
     PKCS#1 RSAPrivateKey (PEM header: BEGIN RSA PRIVATE KEY)
     PKCS#8 PrivateKeyInfo (PEM header: BEGIN PRIVATE KEY)
     matching pair of the above
 

`static JWK`
`parseFromPEMEncodedX509Cert(String pemEncodedCert)`

Parses a public `RSA` or `EC JWK` from the
 specified PEM-encoded X.509 certificate.

`abstract int`
`size()`

Returns the size of this JWK.

`ECKey`
`toECKey()`

Casts this JWK to an EC JWK.

`Map<String,Object>`
`toJSONObject()`

Returns a JSON object representation of this JWK.

`String`
`toJSONString()`

Returns the JSON object string representation of this JWK.

`OctetKeyPair`
`toOctetKeyPair()`

Casts this JWK to an octet key pair JWK.

`OctetSequenceKey`
`toOctetSequenceKey()`

Casts this JWK to an octet sequence JWK.

`abstract JWK`
`toPublicJWK()`

Creates a copy of this JWK with all private or sensitive parameters 
 removed.

`abstract JWK`
`toRevokedJWK(KeyRevocation keyRevocation)`

Creates a copy of this JWK with the specified key revocation.

`RSAKey`
`toRSAKey()`

Casts this JWK to an RSA JWK.

`String`
`toString()`
 

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Field Details

  - 

### MIME_TYPE

public static final String MIME_TYPE
The MIME type of JWK objects: 
 `application/jwk+json; charset=UTF-8`

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### JWK

@Deprecated
protected JWK(KeyType kty,
 KeyUse use,
 Set<KeyOperation> ops,
 Algorithm alg,
 String kid,
 URI x5u,
 Base64URL x5t,
 Base64URL x5t256,
 List<Base64> x5c,
 KeyStore ks)
Deprecated.
Creates a new JSON Web Key (JWK).

Parameters:
`kty` - The key type. Must not be `null`.
`use` - The key use, `null` if not specified or if the
               key is intended for signing as well as encryption.
`ops` - The key operations, `null` if not specified.
`alg` - The intended JOSE algorithm for the key, `null`
               if not specified.
`kid` - The key ID, `null` if not specified.
`x5u` - The X.509 certificate URL, `null` if not
               specified.
`x5t` - The X.509 certificate thumbprint, `null` if not
               specified.
`x5t256` - The X.509 certificate SHA-256 thumbprint, `null`
               if not specified.
`x5c` - The X.509 certificate chain, `null` if not
               specified.
`ks` - Reference to the underlying key store, `null` if
               none.

  - 

### JWK

@Deprecated
protected JWK(KeyType kty,
 KeyUse use,
 Set<KeyOperation> ops,
 Algorithm alg,
 String kid,
 URI x5u,
 Base64URL x5t,
 Base64URL x5t256,
 List<Base64> x5c,
 Date exp,
 Date nbf,
 Date iat,
 KeyStore ks)
Deprecated.
Creates a new JSON Web Key (JWK).

Parameters:
`kty` - The key type. Must not be `null`.
`use` - The key use, `null` if not specified or if the
               key is intended for signing as well as encryption.
`ops` - The key operations, `null` if not specified.
`alg` - The intended JOSE algorithm for the key, `null`
               if not specified.
`kid` - The key ID, `null` if not specified.
`x5u` - The X.509 certificate URL, `null` if not
               specified.
`x5t` - The X.509 certificate thumbprint, `null` if not
               specified.
`x5t256` - The X.509 certificate SHA-256 thumbprint, `null`
               if not specified.
`x5c` - The X.509 certificate chain, `null` if not
               specified.
`exp` - The key expiration time, `null` if not
               specified.
`nbf` - The key not-before time, `null` if not
               specified.
`iat` - The key issued-at time, `null` if not specified.
`ks` - Reference to the underlying key store, `null` if
               none.

  - 

### JWK

protected JWK(KeyType kty,
 KeyUse use,
 Set<KeyOperation> ops,
 Algorithm alg,
 String kid,
 URI x5u,
 Base64URL x5t,
 Base64URL x5t256,
 List<Base64> x5c,
 Date exp,
 Date nbf,
 Date iat,
 KeyRevocation revocation,
 KeyStore ks)
Creates a new JSON Web Key (JWK).

Parameters:
`kty` - The key type. Must not be `null`.
`use` - The key use, `null` if not specified or if
                   the key is intended for signing as well as
                   encryption.
`ops` - The key operations, `null` if not specified.
`alg` - The intended JOSE algorithm for the key,
                   `null` if not specified.
`kid` - The key ID, `null` if not specified.
`x5u` - The X.509 certificate URL, `null` if not
                   specified.
`x5t` - The X.509 certificate thumbprint, `null` if
                   not specified.
`x5t256` - The X.509 certificate SHA-256 thumbprint,
                   `null` if not specified.
`x5c` - The X.509 certificate chain, `null` if not
                   specified.
`exp` - The key expiration time, `null` if not
                   specified.
`nbf` - The key not-before time, `null` if not
                   specified.
`iat` - The key issued-at time, `null` if not
                   specified.
`revocation` - The key revocation, `null` if not specified.
`ks` - Reference to the underlying key store,
                   `null` if none.

- 

## Method Details

  - 

### getKeyType

public KeyType getKeyType()
Returns the type (`kty`) of this JWK.

Returns:
The key type.

  - 

### getKeyUse

public KeyUse getKeyUse()
Returns the use (`use`) of this JWK.

Returns:
The key use, `null` if not specified or if the key is
         intended for signing as well as encryption.

  - 

### getKeyOperations

public Set<KeyOperation> getKeyOperations()
Returns the operations (`key_ops`) for this JWK.

Returns:
The key operations, `null` if not specified.

  - 

### getAlgorithm

public Algorithm getAlgorithm()
Returns the intended JOSE algorithm (`alg`) for this JWK.

Returns:
The intended JOSE algorithm, `null` if not specified.

  - 

### getKeyID

public String getKeyID()
Returns the ID (`kid`) of this JWK. The key ID can be used to
 match a specific key. This can be used, for instance, to choose a 
 key within a `JWKSet` during key rollover. The key ID may also 
 correspond to a JWS/JWE `kid` header parameter value.

Returns:
The key ID, `null` if not specified.

  - 

### getX509CertURL

public URI getX509CertURL()
Returns the X.509 certificate URL (`x5u`) of this JWK.

Returns:
The X.509 certificate URL, `null` if not specified.

  - 

### getX509CertThumbprint

@Deprecated
public Base64URL getX509CertThumbprint()
Deprecated.
Returns the X.509 certificate SHA-1 thumbprint (`x5t`) of this
 JWK.

Returns:
The X.509 certificate SHA-1 thumbprint, `null` if not
         specified.

  - 

### getX509CertSHA256Thumbprint

public Base64URL getX509CertSHA256Thumbprint()
Returns the X.509 certificate SHA-256 thumbprint (`x5t#S256`)
 of this JWK.

Returns:
The X.509 certificate SHA-256 thumbprint, `null` if
         not specified.

  - 

### getX509CertChain

public List<Base64> getX509CertChain()
Returns the X.509 certificate chain (`x5c`) of this JWK.

Returns:
The X.509 certificate chain as a unmodifiable list,
         `null` if not specified.

  - 

### getParsedX509CertChain

public List<X509Certificate> getParsedX509CertChain()
Returns the parsed X.509 certificate chain (`x5c`) of this
 JWK.

Returns:
The X.509 certificate chain as a unmodifiable list,
         `null` if not specified.

  - 

### getExpirationTime

public Date getExpirationTime()
Returns the expiration time (`exp`) if this JWK.

Returns:
The expiration time, `null` if not specified.

  - 

### getNotBeforeTime

public Date getNotBeforeTime()
Returns the not-before (`nbf`) of this JWK.

Returns:
The not-before time, `null` if not specified.

  - 

### getIssueTime

public Date getIssueTime()
Returns the issued-at (`iat`) time of this JWK.

Returns:
The issued-at time, `null` if not specified.

  - 

### getKeyRevocation

public KeyRevocation getKeyRevocation()
Returns the key revocation (`revoked`) of this JWK.

Returns:
The key revocation, `null` if not specified.

  - 

### getKeyStore

public KeyStore getKeyStore()
Returns a reference to the underlying key store.

Returns:
The underlying key store, `null` if none.

  - 

### getRequiredParams

public abstract LinkedHashMap<String,?> getRequiredParams()
Returns the required JWK parameters. Intended as input for JWK
 thumbprint computation. See RFC 7638 for more information.

Returns:
The required JWK parameters, sorted alphanumerically by key
         name and ready for JSON serialisation.

  - 

### computeThumbprint

public Base64URL computeThumbprint()
                            throws JOSEException
Computes the SHA-256 thumbprint of this JWK. See RFC 7638 for more
 information.

Returns:
The SHA-256 thumbprint.
Throws:
`JOSEException` - If the SHA-256 hash algorithm is not
                       supported.

  - 

### computeThumbprint

public Base64URL computeThumbprint(String hashAlg)
                            throws JOSEException
Computes the thumbprint of this JWK using the specified hash
 algorithm. See RFC 7638 for more information.

Parameters:
`hashAlg` - The hash algorithm. Must not be `null`.
Returns:
The SHA-256 thumbprint.
Throws:
`JOSEException` - If the hash algorithm is not supported.

  - 

### computeThumbprintURI

public ThumbprintURI computeThumbprintURI()
                                   throws JOSEException
Computes the SHA-256 thumbprint URI of this JWK. See RFC 7638 and
 draft-ietf-oauth-jwk-thumbprint-uri for more information.

Returns:
The SHA-256 thumbprint URI.
Throws:
`JOSEException` - If the SHA-256 hash algorithm is not
                       supported.

  - 

### isPrivate

public abstract boolean isPrivate()
Returns `true` if this JWK contains private or sensitive
 (non-public) parameters.

Returns:
`true` if this JWK contains private parameters, else
         `false`.

  - 

### toPublicJWK

public abstract JWK toPublicJWK()
Creates a copy of this JWK with all private or sensitive parameters 
 removed.

Returns:
The newly created public JWK, or `null` if none can be
         created.

  - 

### toRevokedJWK

public abstract JWK toRevokedJWK(KeyRevocation keyRevocation)
Creates a copy of this JWK with the specified key revocation.

Parameters:
`keyRevocation` - The key revocation. Must not be `null`.
Returns:
The new JWK with the specified revocation.
Throws:
`IllegalStateException` - If the JWK is already revoked.

  - 

### size

public abstract int size()
Returns the size of this JWK.

Returns:
The JWK size, in bits.

  - 

### toRSAKey

public RSAKey toRSAKey()
Casts this JWK to an RSA JWK.

Returns:
The RSA JWK.

  - 

### toECKey

public ECKey toECKey()
Casts this JWK to an EC JWK.

Returns:
The EC JWK.

  - 

### toOctetSequenceKey

public OctetSequenceKey toOctetSequenceKey()
Casts this JWK to an octet sequence JWK.

Returns:
The octet sequence JWK.

  - 

### toOctetKeyPair

public OctetKeyPair toOctetKeyPair()
Casts this JWK to an octet key pair JWK.

Returns:
The octet key pair JWK.

  - 

### toJSONObject

public Map<String,Object> toJSONObject()
Returns a JSON object representation of this JWK. This method is 
 intended to be called from extending classes.

 

Example:

 

```

 {
   "kty" : "RSA",
   "use" : "sig",
   "kid" : "fd28e025-8d24-48bc-a51a-e2ffc8bc274b"
 }
 
```

Returns:
The JSON object representation.

  - 

### toJSONString

public String toJSONString()
Returns the JSON object string representation of this JWK.

Returns:
The JSON object string representation.

  - 

### toString

public String toString()

Overrides:
`toString` in class `Object`
See Also:

    - `toJSONString()`

  - 

### parse

public static JWK parse(String s)
                 throws ParseException
Parses a JWK from the specified JSON object string representation. 
 The JWK must be an `ECKey`, an `RSAKey`, or a 
 `OctetSequenceKey`.

Parameters:
`s` - The JSON object string to parse. Must not be `null`.
Returns:
The JWK.
Throws:
`ParseException` - If the string couldn't be parsed to a
                        supported JWK.

  - 

### parse

public static JWK parse(Map<String,Object> jsonObject)
                 throws ParseException
Parses a JWK from the specified JSON object representation. The JWK 
 must be an `ECKey`, an `RSAKey`, or a 
 `OctetSequenceKey`.

Parameters:
`jsonObject` - The JSON object to parse. Must not be 
                   `null`.
Returns:
The JWK.
Throws:
`ParseException` - If the JSON object couldn't be parsed to a 
                        supported JWK.

  - 

### parse

public static JWK parse(X509Certificate cert)
                 throws JOSEException
Parses a public `RSA` or `EC JWK` from the
 specified X.509 certificate. Requires BouncyCastle.

 

**Important:** The X.509 certificate is not
 validated!

 

Sets the following JWK parameters:

 

     
    - For an EC key the curve is obtained from the subject public
         key info algorithm parameters.
     
    - The JWK use inferred by `KeyUse.from(java.security.cert.X509Certificate)`.
     
    - The JWK ID from the X.509 serial number (in base 10).
     
    - The JWK X.509 certificate chain (this certificate only).
     
    - The JWK X.509 certificate SHA-256 thumbprint.
 

Parameters:
`cert` - The X.509 certificate. Must not be `null`.
Returns:
The public RSA or EC JWK.
Throws:
`JOSEException` - If parsing failed.

  - 

### parseFromPEMEncodedX509Cert

public static JWK parseFromPEMEncodedX509Cert(String pemEncodedCert)
                                       throws JOSEException
Parses a public `RSA` or `EC JWK` from the
 specified PEM-encoded X.509 certificate. Requires BouncyCastle.

 

**Important:** The X.509 certificate is not
 validated!

 

Sets the following JWK parameters:

 

     
    - For an EC key the curve is obtained from the subject public
         key info algorithm parameters.
     
    - The JWK use inferred by `KeyUse.from(java.security.cert.X509Certificate)`.
     
    - The JWK ID from the X.509 serial number (in base 10).
     
    - The JWK X.509 certificate chain (this certificate only).
     
    - The JWK X.509 certificate SHA-256 thumbprint.
 

Parameters:
`pemEncodedCert` - The PEM-encoded X.509 certificate. Must not be
                       `null`.
Returns:
The public RSA or EC JWK.
Throws:
`JOSEException` - If parsing failed.

  - 

### load

public static JWK load(KeyStore keyStore,
 String alias,
 char[] pin)
                throws KeyStoreException,
JOSEException
Loads a JWK from the specified JCE key store. The JWK can be a
 public / private `RSA key`, a public / private
 `EC key`, or a `secret key`.
 Requires BouncyCastle.

 

**Important:** The X.509 certificate is not
 validated!

Parameters:
`keyStore` - The key store. Must not be `null`.
`alias` - The alias. Must not be `null`.
`pin` - The pin to unlock the private key if any, empty or
                 `null` if not required.
Returns:
The public / private RSA or EC JWK, or secret JWK, or
         `null` if no key with the specified alias was found.
Throws:
`KeyStoreException` - On a key store exception.
`JOSEException` - If RSA or EC key loading failed.

  - 

### parseFromPEMEncodedObjects

public static JWK parseFromPEMEncodedObjects(String pemEncodedObjects)
                                      throws JOSEException
Parses an RSA or EC JWK from the specified string of one or more
 PEM-encoded object(s):

 

     
    - X.509 certificate (PEM header: BEGIN CERTIFICATE)
     
    - PKCS#1 RSAPublicKey (PEM header: BEGIN RSA PUBLIC KEY)
     
    - X.509 SubjectPublicKeyInfo (PEM header: BEGIN PUBLIC KEY)
     
    - PKCS#1 RSAPrivateKey (PEM header: BEGIN RSA PRIVATE KEY)
     
    - PKCS#8 PrivateKeyInfo (PEM header: BEGIN PRIVATE KEY)
     
    - matching pair of the above
 

 

Requires BouncyCastle.

Parameters:
`pemEncodedObjects` - The string of PEM-encoded object(s).
Returns:
The public / (private) RSA or EC JWK.
Throws:
`JOSEException` - If RSA or EC key parsing failed.

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