JavaScript is disabled on your browser.

Skip navigation links

- Overview

- Package

- Class

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

- Enum Constants | 

- Field | 

- Method

- Detail: 

- Enum Constants | 

- Field | 

- Method

graphql.cachecontrol

## Enum CacheControl.Scope

- java.lang.Object

- 

  - java.lang.Enum<CacheControl.Scope>

  - 

    - graphql.cachecontrol.CacheControl.Scope

- 

All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<CacheControl.Scope>

Enclosing class:
CacheControl

---

```
public static enum CacheControl.Scope
extends java.lang.Enum<CacheControl.Scope>
```

If the scope is set to PRIVATE, this indicates anything under this path should only be cached per-user,
 unless the value is overridden on a sub path. PUBLIC is the default and means anything under this path
 can be stored in a shared cache.

- 

  - 

### Enum Constant Summary

Enum Constants 

Enum Constant and Description

`PRIVATE` 

`PUBLIC` 

  - 

### Method Summary

All Methods Static Methods Concrete Methods 

Modifier and Type
Method and Description

`static CacheControl.Scope`
`valueOf(java.lang.String name)`
Returns the enum constant of this type with the specified name.

`static CacheControl.Scope[]`
`values()`
Returns an array containing the constants of this enum type, in
the order they are declared.

    - 

### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`

    - 

### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

- 

  - 

### Enum Constant Detail

    - 

#### PUBLIC

```
public static final CacheControl.Scope PUBLIC
```

    - 

#### PRIVATE

```
public static final CacheControl.Scope PRIVATE
```

  - 

### Method Detail

    - 

#### values

```
public static CacheControl.Scope[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared.  This method may be used to iterate
over the constants as follows:

```

for (CacheControl.Scope c : CacheControl.Scope.values())
    System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared

    - 

#### valueOf

```
public static CacheControl.Scope valueOf(java.lang.String name)
```

Returns the enum constant of this type with the specified name.
The string must match *exactly* an identifier used to declare an
enum constant in this type.  (Extraneous whitespace characters are 
not permitted.)

Parameters:
`name` - the name of the enum constant to be returned.
Returns:
the enum constant with the specified name
Throws:
`java.lang.IllegalArgumentException` - if this enum type has no constant with the specified name
`java.lang.NullPointerException` - if the argument is null

Skip navigation links

- Overview

- Package

- Class

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

- Enum Constants | 

- Field | 

- Method

- Detail: 

- Enum Constants | 

- Field | 

- Method