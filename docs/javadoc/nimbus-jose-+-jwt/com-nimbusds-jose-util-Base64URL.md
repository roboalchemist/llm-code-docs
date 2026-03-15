Package com.nimbusds.jose.util

# Class Base64URL

java.lang.Object
com.nimbusds.jose.util.Base64
com.nimbusds.jose.util.Base64URL

All Implemented Interfaces:
`Serializable`

---

@Immutable
public class Base64URL
extends Base64
Base64URL-encoded object.

 

Related specifications:

 

     
- RFC 4648.
 

Version:
2019-10-04
Author:
Vladimir Dzhuvinov
See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`Base64URL(String base64URL)`

Creates a new Base64URL-encoded object.

- 

## Method Summary

Modifier and Type
Method
Description
`static Base64URL`
`encode(byte[] bytes)`

Base64URL-encodes the specified byte array.

`static Base64URL`
`encode(String text)`

Base64URL-encodes the specified string.

`static Base64URL`
`encode(BigInteger bigInt)`

Base64URL-encodes the specified big integer, without the sign bit.

`boolean`
`equals(Object object)`

Overrides `Object.equals()`.

`static Base64URL`
`from(String base64URL)`

Creates a new Base64URL-encoded object from the specified string.

### Methods inherited from class com.nimbusds.jose.util.Base64

`decode, decodeToBigInteger, decodeToString, hashCode, toJSONString, toString`

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### Base64URL

public Base64URL(String base64URL)
Creates a new Base64URL-encoded object.

Parameters:
`base64URL` - The Base64URL-encoded object value. The value is 
                  not validated for having characters from the 
                  Base64URL alphabet. Must not be `null`.

- 

## Method Details

  - 

### equals

public boolean equals(Object object)
Overrides `Object.equals()`.

Overrides:
`equals` in class `Base64`
Parameters:
`object` - The object to compare to.
Returns:
`true` if the objects have the same value, otherwise
         `false`.

  - 

### from

public static Base64URL from(String base64URL)
Creates a new Base64URL-encoded object from the specified string.

Parameters:
`base64URL` - The Base64URL-encoded object value, `null` if
                  not specified. The value is not validated for
                  having characters from the Base64URL alphabet.
Returns:
The Base64URL-encoded object, `null` if not specified.

  - 

### encode

public static Base64URL encode(byte[] bytes)
Base64URL-encodes the specified byte array.

Parameters:
`bytes` - The byte array to encode. Must not be `null`.
Returns:
The resulting Base64URL object.

  - 

### encode

public static Base64URL encode(BigInteger bigInt)
Base64URL-encodes the specified big integer, without the sign bit.

Parameters:
`bigInt` - The big integer to encode. Must not be `null`.
Returns:
The resulting Base64URL object.

  - 

### encode

public static Base64URL encode(String text)
Base64URL-encodes the specified string.

Parameters:
`text` - The string to encode. Must be in the UTF-8 character set
             and not `null`.
Returns:
The resulting Base64URL object.