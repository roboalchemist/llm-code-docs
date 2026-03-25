Package com.nimbusds.jwt

# Class JWTClaimsSet

java.lang.Object
com.nimbusds.jwt.JWTClaimsSet

All Implemented Interfaces:
`Serializable`

---

@Immutable
public final class JWTClaimsSet
extends Object
implements Serializable
JSON Web Token (JWT) claims set. This class is immutable.

 

Supports all `registered claims` of the JWT
 specification:

 

     
- iss - Issuer
     
- sub - Subject
     
- aud - Audience
     
- exp - Expiration Time
     
- nbf - Not Before
     
- iat - Issued At
     
- jti - JWT ID
 

 

The set may also contain custom claims.

 

Claims with `null` values will not be serialised with
 `toPayload()` / `toJSONObject()` / `toString()` unless
 `JWTClaimsSet.Builder.serializeNullClaims` is enabled.

 

Example JWT claims set:

 

```

 {
   "sub"                         : "joe",
   "exp"                         : 1300819380,
   "https://example.com/is_root" : true
 }
 
```

 

Example usage:

 

```

 JWTClaimsSet claimsSet = new JWTClaimsSet.Builder()
     .subject("joe")
     .expirationTime(new Date(1300819380 * 1000l)
     .claim("http://example.com/is_root", true)
     .build();
 
```

Version:
2024-12-20
Author:
Vladimir Dzhuvinov, Justin Richer, Joey Zhao
See Also:

- Serialized Form

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static class `
`JWTClaimsSet.Builder`

Builder for constructing JSON Web Token (JWT) claims sets.

- 

## Method Summary

Modifier and Type
Method
Description
`boolean`
`equals(Object o)`
 
`List<String>`
`getAudience()`

Gets the audience (`aud`) claim.

`Boolean`
`getBooleanClaim(String name)`

Gets the specified claim (registered or custom) as
 `Boolean`.

`Object`
`getClaim(String name)`

Gets the specified claim (registered or custom).

`String`
`getClaimAsString(String name)`

Gets the specified claim (registered or custom) as
 `String`, primitive or Wrapper types will be converted to
 `String`.

`Map<String,Object>`
`getClaims()`

Gets the claims (registered and custom).

`Date`
`getDateClaim(String name)`

Gets the specified claim (registered or custom) as
 `Date`.

`Double`
`getDoubleClaim(String name)`

Gets the specified claim (registered or custom) as
 `Double`.

`Date`
`getExpirationTime()`

Gets the expiration time (`exp`) claim.

`Float`
`getFloatClaim(String name)`

Gets the specified claim (registered or custom) as
 `Float`.

`Integer`
`getIntegerClaim(String name)`

Gets the specified claim (registered or custom) as
 `Integer`.

`String`
`getIssuer()`

Gets the issuer (`iss`) claim.

`Date`
`getIssueTime()`

Gets the issued-at (`iat`) claim.

`Map<String,Object>`
`getJSONObjectClaim(String name)`

Gets the specified claim (registered or custom) as a JSON object.

`String`
`getJWTID()`

Gets the JWT ID (`jti`) claim.

`List<Object>`
`getListClaim(String name)`

Gets the specified claims (registered or custom) as a
 `List` list of objects.

`Long`
`getLongClaim(String name)`

Gets the specified claim (registered or custom) as
 `Long`.

`Date`
`getNotBeforeTime()`

Gets the not-before (`nbf`) claim.

`static Set<String>`
`getRegisteredNames()`

Gets the registered JWT claim names.

`String[]`
`getStringArrayClaim(String name)`

Gets the specified claims (registered or custom) as a
 `String` array.

`String`
`getStringClaim(String name)`

Gets the specified claim (registered or custom) as
 `String`.

`List<String>`
`getStringListClaim(String name)`

Gets the specified claims (registered or custom) as a
 `List` list of strings.

`String`
`getSubject()`

Gets the subject (`sub`) claim.

`URI`
`getURIClaim(String name)`

Gets the specified claim (registered or custom) as a
 `URI`.

`int`
`hashCode()`
 
`static JWTClaimsSet`
`parse(String s)`

Parses a JSON Web Token (JWT) claims set from the specified JSON
 object string representation.

`static JWTClaimsSet`
`parse(Map<String,Object> json)`

Parses a JSON Web Token (JWT) claims set from the specified JSON
 object representation.

`Map<String,Object>`
`toJSONObject()`

Returns the JSON object representation of this claims set.

`Map<String,Object>`
`toJSONObject(boolean serializeNullClaims)`

Returns the JSON object representation of this claims set.

`Payload`
`toPayload()`

Returns a JOSE object payload representation of this claims set.

`Payload`
`toPayload(boolean serializeNullClaims)`

Returns a JOSE object payload representation of this claims set.

`String`
`toString()`

Returns a JSON object string representation of this claims set.

`String`
`toString(boolean serializeNullClaims)`

Returns a JSON object string representation of this claims set.

`<T> T`
`toType(JWTClaimsSetTransformer<T> transformer)`

Returns a transformation of this JWT claims set.

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Method Details

  - 

### getRegisteredNames

public static Set<String> getRegisteredNames()
Gets the registered JWT claim names.

Returns:
The registered claim names, as an unmodifiable set.

  - 

### getIssuer

public String getIssuer()
Gets the issuer (`iss`) claim.

Returns:
The issuer claim, `null` if not specified.

  - 

### getSubject

public String getSubject()
Gets the subject (`sub`) claim.

Returns:
The subject claim, `null` if not specified.

  - 

### getAudience

public List<String> getAudience()
Gets the audience (`aud`) claim.

Returns:
The audience claim, empty list if not specified.

  - 

### getExpirationTime

public Date getExpirationTime()
Gets the expiration time (`exp`) claim.

Returns:
The expiration time, `null` if not specified.

  - 

### getNotBeforeTime

public Date getNotBeforeTime()
Gets the not-before (`nbf`) claim.

Returns:
The not-before claim, `null` if not specified.

  - 

### getIssueTime

public Date getIssueTime()
Gets the issued-at (`iat`) claim.

Returns:
The issued-at claim, `null` if not specified.

  - 

### getJWTID

public String getJWTID()
Gets the JWT ID (`jti`) claim.

Returns:
The JWT ID claim, `null` if not specified.

  - 

### getClaim

public Object getClaim(String name)
Gets the specified claim (registered or custom).

Parameters:
`name` - The name of the claim. Must not be `null`.
Returns:
The value of the claim, `null` if not specified.

  - 

### getStringClaim

public String getStringClaim(String name)
                      throws ParseException
Gets the specified claim (registered or custom) as
 `String`.

Parameters:
`name` - The name of the claim. Must not be `null`.
Returns:
The value of the claim, `null` if not specified.
Throws:
`ParseException` - If the claim value is not of the required
                        type.

  - 

### getClaimAsString

public String getClaimAsString(String name)
                        throws ParseException
Gets the specified claim (registered or custom) as
 `String`, primitive or Wrapper types will be converted to
 `String`.

Parameters:
`name` - The name of the claim. Must not be `null`.
Returns:
The value of the claim, `null` if not specified.
Throws:
`ParseException` - If the claim value is not and cannot be
                        automatically converted to `String`.

  - 

### getListClaim

public List<Object> getListClaim(String name)
                          throws ParseException
Gets the specified claims (registered or custom) as a
 `List` list of objects.

Parameters:
`name` - The name of the claim. Must not be `null`.
Returns:
The value of the claim, `null` if not specified.
Throws:
`ParseException` - If the claim value is not of the required
                        type.

  - 

### getStringArrayClaim

public String[] getStringArrayClaim(String name)
                             throws ParseException
Gets the specified claims (registered or custom) as a
 `String` array.

Parameters:
`name` - The name of the claim. Must not be `null`.
Returns:
The value of the claim, `null` if not specified.
Throws:
`ParseException` - If the claim value is not of the required
                        type.

  - 

### getStringListClaim

public List<String> getStringListClaim(String name)
                                throws ParseException
Gets the specified claims (registered or custom) as a
 `List` list of strings.

Parameters:
`name` - The name of the claim. Must not be `null`.
Returns:
The value of the claim, `null` if not specified.
Throws:
`ParseException` - If the claim value is not of the required
                        type.

  - 

### getURIClaim

public URI getURIClaim(String name)
                throws ParseException
Gets the specified claim (registered or custom) as a
 `URI`.

Parameters:
`name` - The name of the claim. Must not be `null`.
Returns:
The value of the claim, `null` if not specified.
Throws:
`ParseException` - If the claim couldn't be parsed to a URI.

  - 

### getBooleanClaim

public Boolean getBooleanClaim(String name)
                        throws ParseException
Gets the specified claim (registered or custom) as
 `Boolean`.

Parameters:
`name` - The name of the claim. Must not be `null`.
Returns:
The value of the claim, `null` if not specified.
Throws:
`ParseException` - If the claim value is not of the required
                        type.

  - 

### getIntegerClaim

public Integer getIntegerClaim(String name)
                        throws ParseException
Gets the specified claim (registered or custom) as
 `Integer`. May involve truncation if
 `Integer.MAX_VALUE` or `Integer.MIN_VALUE` is exceeded.

Parameters:
`name` - The name of the claim. Must not be `null`.
Returns:
The value of the claim, `null` if not specified.
Throws:
`ParseException` - If the claim value is not of the required
                        type.

  - 

### getLongClaim

public Long getLongClaim(String name)
                  throws ParseException
Gets the specified claim (registered or custom) as
 `Long`. May involve truncation if
 `Long.MAX_VALUE` or `Long.MIN_VALUE` is exceeded.

Parameters:
`name` - The name of the claim. Must not be `null`.
Returns:
The value of the claim, `null` if not specified.
Throws:
`ParseException` - If the claim value is not of the required
                        type.

  - 

### getDateClaim

public Date getDateClaim(String name)
                  throws ParseException
Gets the specified claim (registered or custom) as
 `Date`. The claim may be represented by a Date
 object or a number of a seconds since the Unix epoch.

Parameters:
`name` - The name of the claim. Must not be `null`.
Returns:
The value of the claim, `null` if not specified.
Throws:
`ParseException` - If the claim value is not of the required
                        type.

  - 

### getFloatClaim

public Float getFloatClaim(String name)
                    throws ParseException
Gets the specified claim (registered or custom) as
 `Float`. May involve truncation if `Float.MAX_VALUE` or `Float.MIN_VALUE` is exceeded, or
 rounding if floating-point precision is exceeded.

Parameters:
`name` - The name of the claim. Must not be `null`.
Returns:
The value of the claim, `null` if not specified.
Throws:
`ParseException` - If the claim value is not of the required
                        type.

  - 

### getDoubleClaim

public Double getDoubleClaim(String name)
                      throws ParseException
Gets the specified claim (registered or custom) as
 `Double`. May involve truncation if `Double.MAX_VALUE` or `Double.MIN_VALUE` is exceeded, or
 rounding if floating-point precision is exceeded.

Parameters:
`name` - The name of the claim. Must not be `null`.
Returns:
The value of the claim, `null` if not specified.
Throws:
`ParseException` - If the claim value is not of the required
                        type.

  - 

### getJSONObjectClaim

public Map<String,Object> getJSONObjectClaim(String name)
                                      throws ParseException
Gets the specified claim (registered or custom) as a JSON object.

Parameters:
`name` - The name of the claim. Must not be `null`.
Returns:
The value of the claim, `null` if not specified.
Throws:
`ParseException` - If the claim value is not of the required
                        type.

  - 

### getClaims

public Map<String,Object> getClaims()
Gets the claims (registered and custom).

 

Note that the registered claims Expiration-Time (`exp`),
 Not-Before-Time (`nbf`) and Issued-At (`iat`) will be
 returned as `java.util.Date` instances.

Returns:
The claims, as an unmodifiable map, empty map if none.

  - 

### toPayload

public Payload toPayload()
Returns a JOSE object payload representation of this claims set. The
 claims are serialised according to their insertion order. Claims
 with `null` values are output according to
 `JWTClaimsSet.Builder.serializeNullClaims(boolean)`.

Returns:
The payload representation.

  - 

### toPayload

public Payload toPayload(boolean serializeNullClaims)
Returns a JOSE object payload representation of this claims set. The
 claims are serialised according to their insertion order.

Parameters:
`serializeNullClaims` - `true` to serialise claims with
                            `null` values, `false` to
                            omit them.
Returns:
The payload representation.

  - 

### toJSONObject

public Map<String,Object> toJSONObject()
Returns the JSON object representation of this claims set. The
 claims are serialised according to their insertion order. Claims
 with `null` values are output according to
 `JWTClaimsSet.Builder.serializeNullClaims(boolean)`.

Returns:
The JSON object representation.

  - 

### toJSONObject

public Map<String,Object> toJSONObject(boolean serializeNullClaims)
Returns the JSON object representation of this claims set. The
 claims are serialised according to their insertion order.

Parameters:
`serializeNullClaims` - `true` to serialise claims with
                            `null` values, `false` to
                            omit them.
Returns:
The JSON object representation.

  - 

### toString

public String toString()
Returns a JSON object string representation of this claims set. The
 claims are serialised according to their insertion order. Claims
 with `null` values are output according to
 `JWTClaimsSet.Builder.serializeNullClaims(boolean)`.

Overrides:
`toString` in class `Object`
Returns:
The JSON object string representation.

  - 

### toString

public String toString(boolean serializeNullClaims)
Returns a JSON object string representation of this claims set. The
 claims are serialised according to their insertion order.

Parameters:
`serializeNullClaims` - `true` to serialise claims with
                            `null` values, `false` to
                            omit them.
Returns:
The JSON object string representation.

  - 

### toType

public <T> T toType(JWTClaimsSetTransformer<T> transformer)
Returns a transformation of this JWT claims set.

Type Parameters:
`T` - Type of the result.
Parameters:
`transformer` - The JWT claims set transformer. Must not be
                    `null`.
Returns:
The transformed JWT claims set.

  - 

### parse

public static JWTClaimsSet parse(Map<String,Object> json)
                          throws ParseException
Parses a JSON Web Token (JWT) claims set from the specified JSON
 object representation.

Parameters:
`json` - The JSON object to parse. Must not be `null`.
Returns:
The JWT claims set.
Throws:
`ParseException` - If the specified JSON object doesn't 
                        represent a valid JWT claims set.

  - 

### parse

public static JWTClaimsSet parse(String s)
                          throws ParseException
Parses a JSON Web Token (JWT) claims set from the specified JSON
 object string representation.

Parameters:
`s` - The JSON object string to parse. Must not be `null`.
Returns:
The JWT claims set.
Throws:
`ParseException` - If the specified JSON object string doesn't
                        represent a valid JWT claims set.

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