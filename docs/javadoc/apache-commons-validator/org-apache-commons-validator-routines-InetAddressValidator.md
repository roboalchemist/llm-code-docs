Package org.apache.commons.validator.routines

# Class InetAddressValidator

java.lang.Object
org.apache.commons.validator.routines.InetAddressValidator

All Implemented Interfaces:
`Serializable`

---

public class InetAddressValidator
extends Object
implements Serializable

**InetAddress** validation and conversion routines (`java.net.InetAddress`).

 

This class provides methods to validate a candidate IP address.

 

 This class is a Singleton; you can retrieve the instance via the `getInstance()` method.
 

Since:
1.4
See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`InetAddressValidator()`

Constructs a new instance.

- 

## Method Summary

Modifier and Type
Method
Description
`static InetAddressValidator`
`getInstance()`

Returns the singleton instance of this validator.

`boolean`
`isValid(String inetAddress)`

Checks if the specified string is a valid IPv4 or IPv6 address.

`boolean`
`isValidInet4Address(String inet4Address)`

Validates an IPv4 address.

`boolean`
`isValidInet6Address(String inet6Address)`

Validates an IPv6 address.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### InetAddressValidator

public InetAddressValidator()
Constructs a new instance.

- 

## Method Details

  - 

### getInstance

public static InetAddressValidator getInstance()
Returns the singleton instance of this validator.

Returns:
the singleton instance of this validator

  - 

### isValid

public boolean isValid(String inetAddress)
Checks if the specified string is a valid IPv4 or IPv6 address.

Parameters:
`inetAddress` - the string to validate
Returns:
true if the string validates as an IP address

  - 

### isValidInet4Address

public boolean isValidInet4Address(String inet4Address)
Validates an IPv4 address. Returns true if valid.

Parameters:
`inet4Address` - the IPv4 address to validate
Returns:
true if the argument contains a valid IPv4 address

  - 

### isValidInet6Address

public boolean isValidInet6Address(String inet6Address)
Validates an IPv6 address. Returns true if valid.

Parameters:
`inet6Address` - the IPv6 address to validate
Returns:
true if the argument contains a valid IPv6 address
Since:
1.4.1