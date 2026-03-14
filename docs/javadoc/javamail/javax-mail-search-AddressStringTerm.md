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

## Class AddressStringTerm

- java.lang.Object

- 

  - javax.mail.search.SearchTerm

  - 

    - javax.mail.search.StringTerm

    - 

      - javax.mail.search.AddressStringTerm

- 

All Implemented Interfaces:
Serializable

Direct Known Subclasses:
FromStringTerm, RecipientStringTerm

---

```
public abstract class AddressStringTerm
extends StringTerm
```

This abstract class implements string comparisons for Message 
 addresses. 

 Note that this class differs from the `AddressTerm` class
 in that this class does comparisons on address strings rather than
 Address objects.

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

Modifier
Constructor and Description

`protected `
`AddressStringTerm(String pattern)`
Constructor.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`boolean`
`equals(Object obj)`
Equality comparison.

`protected boolean`
`match(Address a)`
Check whether the address pattern specified in the constructor is
 a substring of the string representation of the given Address
 object.

    - 

### Methods inherited from class javax.mail.search.StringTerm

`getIgnoreCase, getPattern, hashCode, match`

    - 

### Methods inherited from class javax.mail.search.SearchTerm

`match`

    - 

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AddressStringTerm

```
protected AddressStringTerm(String pattern)
```

Constructor.

Parameters:
`pattern` - the address pattern to be compared.

  - 

### Method Detail

    - 

#### match

```
protected boolean match(Address a)
```

Check whether the address pattern specified in the constructor is
 a substring of the string representation of the given Address
 object. 

 Note that if the string representation of the given Address object
 contains charset or transfer encodings, the encodings must be 
 accounted for, during the match process. 

Parameters:
`a` - The comparison is applied to this Address object.
Returns:
true if the match succeeds, otherwise false.

    - 

#### equals

```
public boolean equals(Object obj)
```

Equality comparison.

Overrides:
`equals` in class `StringTerm`

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