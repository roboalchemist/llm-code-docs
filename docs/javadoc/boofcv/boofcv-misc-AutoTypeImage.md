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

boofcv.misc

## Enum AutoTypeImage

- java.lang.Object

- 

  - java.lang.Enum<AutoTypeImage>

  - 

    - boofcv.misc.AutoTypeImage

- 

All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<AutoTypeImage>

---

```
public enum AutoTypeImage
extends java.lang.Enum<AutoTypeImage>
```

Image information for auto generated code
Author:
  Peter Abeles

- 

  - 

### Enum Constant Summary

Enum Constants 

Enum Constant and Description

`**F32**` 

`**F64**` 

`**I**` 

`**I16**` 

`**I8**` 

`**S16**` 

`**S32**` 

`**S64**` 

`**S8**` 

`**U16**` 

`**U8**` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`java.lang.String`
`**getAbbreviatedType**()` 

`java.lang.String`
`**getBitWise**()` 

`java.lang.String`
`**getDataType**()` 

`static AutoTypeImage[]`
`**getFloatingTypes**()` 

`static AutoTypeImage[]`
`**getGenericTypes**()` 

`java.lang.String`
`**getImageName**()` 

`static AutoTypeImage[]`
`**getIntegerTypes**()` 

`java.lang.String`
`**getLargeSumType**()` 

`java.lang.Number`
`**getMax**()` 

`java.lang.Number`
`**getMin**()` 

`int`
`**getNumBits**()` 

`java.lang.Class<?>`
`**getPrimitiveType**()` 

`java.lang.String`
`**getRandType**()` 

`static AutoTypeImage[]`
`**getReallyGenericTypes**()` 

`static AutoTypeImage[]`
`**getSigned**()` 

`static AutoTypeImage[]`
`**getSpecificTypes**()` 

`java.lang.String`
`**getSumType**()` 

`java.lang.String`
`**getTypeCastFromSum**()` 

`static AutoTypeImage[]`
`**getUnsigned**()` 

`boolean`
`**isInteger**()` 

`boolean`
`**isSigned**()` 

`static AutoTypeImage`
`**valueOf**(java.lang.String name)`
Returns the enum constant of this type with the specified name.

`static AutoTypeImage[]`
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

#### I

```
public static final AutoTypeImage I
```

    - 

#### I8

```
public static final AutoTypeImage I8
```

    - 

#### U8

```
public static final AutoTypeImage U8
```

    - 

#### S8

```
public static final AutoTypeImage S8
```

    - 

#### I16

```
public static final AutoTypeImage I16
```

    - 

#### U16

```
public static final AutoTypeImage U16
```

    - 

#### S16

```
public static final AutoTypeImage S16
```

    - 

#### S32

```
public static final AutoTypeImage S32
```

    - 

#### S64

```
public static final AutoTypeImage S64
```

    - 

#### F32

```
public static final AutoTypeImage F32
```

    - 

#### F64

```
public static final AutoTypeImage F64
```

  - 

### Method Detail

    - 

#### values

```
public static AutoTypeImage[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared.  This method may be used to iterate
over the constants as follows:

```

for (AutoTypeImage c : AutoTypeImage.values())
    System.out.println(c);

```

Returns:an array containing the constants of this enum type, in
the order they are declared

    - 

#### valueOf

```
public static AutoTypeImage valueOf(java.lang.String name)
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

    - 

#### getIntegerTypes

```
public static AutoTypeImage[] getIntegerTypes()
```

    - 

#### getFloatingTypes

```
public static AutoTypeImage[] getFloatingTypes()
```

    - 

#### getGenericTypes

```
public static AutoTypeImage[] getGenericTypes()
```

    - 

#### getReallyGenericTypes

```
public static AutoTypeImage[] getReallyGenericTypes()
```

    - 

#### getSpecificTypes

```
public static AutoTypeImage[] getSpecificTypes()
```

    - 

#### getSigned

```
public static AutoTypeImage[] getSigned()
```

    - 

#### getUnsigned

```
public static AutoTypeImage[] getUnsigned()
```

    - 

#### getImageName

```
public java.lang.String getImageName()
```

    - 

#### getDataType

```
public java.lang.String getDataType()
```

    - 

#### getBitWise

```
public java.lang.String getBitWise()
```

    - 

#### getSumType

```
public java.lang.String getSumType()
```

    - 

#### getLargeSumType

```
public java.lang.String getLargeSumType()
```

    - 

#### isInteger

```
public boolean isInteger()
```

    - 

#### isSigned

```
public boolean isSigned()
```

    - 

#### getNumBits

```
public int getNumBits()
```

    - 

#### getPrimitiveType

```
public java.lang.Class<?> getPrimitiveType()
```

    - 

#### getTypeCastFromSum

```
public java.lang.String getTypeCastFromSum()
```

    - 

#### getAbbreviatedType

```
public java.lang.String getAbbreviatedType()
```

    - 

#### getRandType

```
public java.lang.String getRandType()
```

    - 

#### getMax

```
public java.lang.Number getMax()
```

    - 

#### getMin

```
public java.lang.Number getMin()
```

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