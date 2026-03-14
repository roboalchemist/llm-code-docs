JavaScript is disabled on your browser.

Skip navigation links

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

javax.mail

## Class Address

- java.lang.Object

- 

  - javax.mail.Address

- 

All Implemented Interfaces:
Serializable

Direct Known Subclasses:
InternetAddress, NewsAddress

---

```
public abstract class Address
extends Object
implements Serializable
```

This abstract class models the addresses in a message.
 Subclasses provide specific implementations.  Subclasses
 will typically be serializable so that (for example) the
 use of Address objects in search terms can be serialized
 along with the search terms.

Author:
John Mani, Bill Shannon
See Also:
Serialized Form

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`Address()` 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description

`abstract boolean`
`equals(Object address)`
The equality operator.

`abstract String`
`getType()`
Return a type string that identifies this address type.

`abstract String`
`toString()`
Return a String representation of this address object.

    - 

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Address

```
public Address()
```

  - 

### Method Detail

    - 

#### getType

```
public abstract String getType()
```

Return a type string that identifies this address type.

Returns:
address type
See Also:
`InternetAddress`

    - 

#### toString

```
public abstract String toString()
```

Return a String representation of this address object.

Overrides:
`toString` in class `Object`
Returns:
string representation of this address

    - 

#### equals

```
public abstract boolean equals(Object address)
```

The equality operator.  Subclasses should provide an
 implementation of this method that supports value equality
 (do the two Address objects represent the same destination?),
 not object reference equality.  A subclass must also provide
 a corresponding implementation of the `hashCode`
 method that preserves the general contract of
 `equals` and `hashCode` - objects that
 compare as equal must have the same hashCode.

Overrides:
`equals` in class `Object`
Parameters:
`address` - Address object

Skip navigation links

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

Copyright © 2018 Oracle. All rights reserved.