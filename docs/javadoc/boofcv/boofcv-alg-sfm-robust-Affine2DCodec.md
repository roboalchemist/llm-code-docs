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

boofcv.alg.sfm.robust

## Class Affine2DCodec

- java.lang.Object

- 

  - boofcv.alg.sfm.robust.Affine2DCodec

- 

---

```
public class Affine2DCodec
extends java.lang.Object
```

Converts an `georegression.struct.affine.Affine2D_F64` to and from an array
 parameterized format.
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**Affine2DCodec**()` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`void`
`**decode**(double[] input,
      Affine2D_F64 model)` 

`static void`
`**decodeStatic**(double[] param,
            Affine2D_F64 model)` 

`void`
`**encode**(Affine2D_F64 model,
      double[] param)` 

`static void`
`**encodeStatic**(Affine2D_F64 model,
            double[] param)` 

`int`
`**getParamLength**()` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Affine2DCodec

```
public Affine2DCodec()
```

  - 

### Method Detail

    - 

#### getParamLength

```
public int getParamLength()
```

    - 

#### decode

```
public void decode(double[] input,
          Affine2D_F64 model)
```

    - 

#### decodeStatic

```
public static void decodeStatic(double[] param,
                Affine2D_F64 model)
```

    - 

#### encode

```
public void encode(Affine2D_F64 model,
          double[] param)
```

    - 

#### encodeStatic

```
public static void encodeStatic(Affine2D_F64 model,
                double[] param)
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

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

**Copyright © 2011-2012 Peter Abeles**