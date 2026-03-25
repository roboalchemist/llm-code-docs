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

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

boofcv.struct

## Class BoofDefaults

- java.lang.Object

- 

  - boofcv.struct.BoofDefaults

- 

---

```
public class BoofDefaults
extends java.lang.Object
```

Author:
  Peter Abeles

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`static BorderType`
`**DERIV_BORDER_TYPE**` 

`static double`
`**SCALE_SPACE_CANONICAL_RADIUS**` 

`static java.lang.String`
`**version**`
String specifying BoofCV's version.

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**BoofDefaults**()` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`static ImageBorder_F32`
`**borderDerivative_F32**()`
Creates a new instance of the default border for derivatives of ImageFloat32

`static ImageBorder_I32`
`**borderDerivative_I32**()`
Creates a new instance of the default border for derivatives of integer images

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### version

```
public static java.lang.String version
```

String specifying BoofCV's version.

    - 

#### DERIV_BORDER_TYPE

```
public static BorderType DERIV_BORDER_TYPE
```

    - 

#### SCALE_SPACE_CANONICAL_RADIUS

```
public static final double SCALE_SPACE_CANONICAL_RADIUS
```

See Also:Constant Field Values

  - 

### Constructor Detail

    - 

#### BoofDefaults

```
public BoofDefaults()
```

  - 

### Method Detail

    - 

#### borderDerivative_I32

```
public static ImageBorder_I32 borderDerivative_I32()
```

Creates a new instance of the default border for derivatives of integer images

    - 

#### borderDerivative_F32

```
public static ImageBorder_F32 borderDerivative_F32()
```

Creates a new instance of the default border for derivatives of ImageFloat32

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

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

**Copyright © 2011-2012 Peter Abeles**