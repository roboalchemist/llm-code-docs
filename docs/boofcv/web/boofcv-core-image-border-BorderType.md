JavaScript is disabled on your browser.

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Enum Constants | 

- Field | 

- Method

- Detail: 

- Enum Constants | 

- Field | 

- Method

boofcv.core.image.border

## Enum BorderType

- java.lang.Object

- 

  - java.lang.Enum<BorderType>

  - 

    - boofcv.core.image.border.BorderType

- 

All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<BorderType>

---

```
public enum BorderType
extends java.lang.Enum<BorderType>
```

How the image border is handled by a convolution filter.  Care should be taken when selecting
 a border method since some types will not produce meaningful results for all kernel types.
Author:
  Peter Abeles

- 

  - 

### Enum Constant Summary

Enum Constants 

Enum Constant and Description

`**EXTENDED**`
The pixels along the image border are extended outwards

`**NORMALIZED**`
The kernel is renormalized to take in account that parts of it are not inside the image.

`**REFLECT**`
Access to outside the array are reflected back into the array around the closest border.

`**SKIP**`
Image borders are not processed and are simply skipped over.

`**VALUE**`
The image border is set to a fixed value

`**WRAP**`
Also known as periodic, an access outside of one border is wrapped around to the other border.

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`static BorderType`
`**valueOf**(java.lang.String name)`
Returns the enum constant of this type with the specified name.

`static BorderType[]`
`**values**()`
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

#### SKIP

```
public static final BorderType SKIP
```

Image borders are not processed and are simply skipped over.

    - 

#### EXTENDED

```
public static final BorderType EXTENDED
```

The pixels along the image border are extended outwards

    - 

#### NORMALIZED

```
public static final BorderType NORMALIZED
```

The kernel is renormalized to take in account that parts of it are not inside the image.
 Typically only used with kernels that blur the image.

    - 

#### REFLECT

```
public static final BorderType REFLECT
```

Access to outside the array are reflected back into the array around the closest border.  This
 is an even symmetric function, e.g. f(-1) = f(1) = 1, f(-2) = f(2) = 2.

    - 

#### WRAP

```
public static final BorderType WRAP
```

Also known as periodic, an access outside of one border is wrapped around to the other border.

    - 

#### VALUE

```
public static final BorderType VALUE
```

The image border is set to a fixed value

  - 

### Method Detail

    - 

#### values

```
public static BorderType[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared.  This method may be used to iterate
over the constants as follows:

```

for (BorderType c : BorderType.values())
    System.out.println(c);

```

Returns:an array containing the constants of this enum type, in
the order they are declared

    - 

#### valueOf

```
public static BorderType valueOf(java.lang.String name)
```

Returns the enum constant of this type with the specified name.
The string must match *exactly* an identifier used to declare an
enum constant in this type.  (Extraneous whitespace characters are 
not permitted.)
Parameters:`name` - the name of the enum constant to be returned.
Returns:the enum constant with the specified name
Throws:
`java.lang.IllegalArgumentException` - if this enum type has no constant
with the specified name
`java.lang.NullPointerException` - if the argument is null

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Enum Constants | 

- Field | 

- Method

- Detail: 

- Enum Constants | 

- Field | 

- Method

**Copyright © 2011-2012 Peter Abeles**