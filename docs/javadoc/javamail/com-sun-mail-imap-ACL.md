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

com.sun.mail.imap

## Class ACL

- java.lang.Object

- 

  - com.sun.mail.imap.ACL

- 

All Implemented Interfaces:
Cloneable

---

```
public class ACL
extends Object
implements Cloneable
```

An access control list entry for a particular authentication identifier
 (user or group).  Associates a set of Rights with the identifier.
 See RFC 2086.
 

Author:
Bill Shannon

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`ACL(String name)`
Construct an ACL entry for the given identifier and with no rights.

`ACL(String name,
   Rights rights)`
Construct an ACL entry for the given identifier with the given rights.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`Object`
`clone()`
Clone this ACL entry.

`String`
`getName()`
Get the identifier name for this ACL entry.

`Rights`
`getRights()`
Get the rights associated with this ACL entry.

`void`
`setRights(Rights rights)`
Set the rights associated with this ACL entry.

    - 

### Methods inherited from class java.lang.Object

`equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### ACL

```
public ACL(String name)
```

Construct an ACL entry for the given identifier and with no rights.

Parameters:
`name` - the identifier name

    - 

#### ACL

```
public ACL(String name,
           Rights rights)
```

Construct an ACL entry for the given identifier with the given rights.

Parameters:
`name` - the identifier name
`rights` - the rights

  - 

### Method Detail

    - 

#### getName

```
public String getName()
```

Get the identifier name for this ACL entry.

Returns:
the identifier name

    - 

#### setRights

```
public void setRights(Rights rights)
```

Set the rights associated with this ACL entry.

Parameters:
`rights` - the rights

    - 

#### getRights

```
public Rights getRights()
```

Get the rights associated with this ACL entry.
 Returns the actual Rights object referenced by this ACL;
 modifications to the Rights object will effect this ACL.

Returns:
the rights

    - 

#### clone

```
public Object clone()
             throws CloneNotSupportedException
```

Clone this ACL entry.

Overrides:
`clone` in class `Object`
Throws:
`CloneNotSupportedException`

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