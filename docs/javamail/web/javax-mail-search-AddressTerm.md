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

javax.mail.search

## Class AddressTerm

- java.lang.Object

- 

  - javax.mail.search.SearchTerm

  - 

    - javax.mail.search.AddressTerm

- 

All Implemented Interfaces:
Serializable

Direct Known Subclasses:
FromTerm, RecipientTerm

---

```
public abstract class AddressTerm
extends SearchTerm
```

This class implements Message Address comparisons.

Author:
Bill Shannon, John Mani
See Also:
Serialized Form

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`protected Address`
`address`
The address.

  - 

### Constructor Summary

Constructors 

Modifier
Constructor and Description

`protected `
`AddressTerm(Address address)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`boolean`
`equals(Object obj)`
Equality comparison.

`Address`
`getAddress()`
Return the address to match with.

`int`
`hashCode()`
Compute a hashCode for this object.

`protected boolean`
`match(Address a)`
Match against the argument Address.

    - 

### Methods inherited from class javax.mail.search.SearchTerm

`match`

    - 

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### address

```
protected Address address
```

The address.

  - 

### Constructor Detail

    - 

#### AddressTerm

```
protected AddressTerm(Address address)
```

  - 

### Method Detail

    - 

#### getAddress

```
public Address getAddress()
```

Return the address to match with.

Returns:
the adddress

    - 

#### match

```
protected boolean match(Address a)
```

Match against the argument Address.

Parameters:
`a` - the address to match
Returns:
true if it matches

    - 

#### equals

```
public boolean equals(Object obj)
```

Equality comparison.

Overrides:
`equals` in class `Object`

    - 

#### hashCode

```
public int hashCode()
```

Compute a hashCode for this object.

Overrides:
`hashCode` in class `Object`

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