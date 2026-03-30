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

## Class FlagTerm

- java.lang.Object

- 

  - javax.mail.search.SearchTerm

  - 

    - javax.mail.search.FlagTerm

- 

All Implemented Interfaces:
Serializable

---

```
public final class FlagTerm
extends SearchTerm
```

This class implements comparisons for Message Flags.

Author:
Bill Shannon, John Mani
See Also:
Serialized Form

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`FlagTerm(Flags flags,
        boolean set)`
Constructor.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`boolean`
`equals(Object obj)`
Equality comparison.

`Flags`
`getFlags()`
Return the Flags to test.

`boolean`
`getTestSet()`
Return true if testing whether the flags are set.

`int`
`hashCode()`
Compute a hashCode for this object.

`boolean`
`match(Message msg)`
The comparison method.

    - 

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### FlagTerm

```
public FlagTerm(Flags flags,
                boolean set)
```

Constructor.

Parameters:
`flags` - Flags object containing the flags to check for
`set` - the flag setting to check for

  - 

### Method Detail

    - 

#### getFlags

```
public Flags getFlags()
```

Return the Flags to test.

Returns:
the flags

    - 

#### getTestSet

```
public boolean getTestSet()
```

Return true if testing whether the flags are set.

Returns:
true if testing whether the flags are set

    - 

#### match

```
public boolean match(Message msg)
```

The comparison method.

Specified by:
`match` in class `SearchTerm`
Parameters:
`msg` - The flag comparison is applied to this Message
Returns:
true if the comparson succeeds, otherwise false.

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