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

## Class FromStringTerm

- java.lang.Object

- 

  - javax.mail.search.SearchTerm

  - 

    - javax.mail.search.StringTerm

    - 

      - javax.mail.search.AddressStringTerm

      - 

        - javax.mail.search.FromStringTerm

- 

All Implemented Interfaces:
Serializable

---

```
public final class FromStringTerm
extends AddressStringTerm
```

This class implements string comparisons for the From Address
 header. 

 Note that this class differs from the `FromTerm` class
 in that this class does comparisons on address strings rather than Address
 objects. The string comparisons are case-insensitive.

Since:
JavaMail 1.1
See Also:
Serialized Form

- 

  - 

### Field Summary

    - 

### Fields inherited from class javax.mail.search.StringTerm

`ignoreCase, pattern`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`FromStringTerm(String pattern)`
Constructor.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`boolean`
`equals(Object obj)`
Equality comparison.

`boolean`
`match(Message msg)`
Check whether the address string specified in the constructor is
 a substring of the From address of this Message.

    - 

### Methods inherited from class javax.mail.search.AddressStringTerm

`match`

    - 

### Methods inherited from class javax.mail.search.StringTerm

`getIgnoreCase, getPattern, hashCode, match`

    - 

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### FromStringTerm

```
public FromStringTerm(String pattern)
```

Constructor.

Parameters:
`pattern` - the address pattern to be compared.

  - 

### Method Detail

    - 

#### match

```
public boolean match(Message msg)
```

Check whether the address string specified in the constructor is
 a substring of the From address of this Message.

Specified by:
`match` in class `SearchTerm`
Parameters:
`msg` - The comparison is applied to this Message's From
                        address.
Returns:
true if the match succeeds, otherwise false.

    - 

#### equals

```
public boolean equals(Object obj)
```

Equality comparison.

Overrides:
`equals` in class `AddressStringTerm`

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