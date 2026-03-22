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

boofcv.io.video

## Class BoofVideoManager

- java.lang.Object

- 

  - boofcv.io.video.BoofVideoManager

- 

---

```
public class BoofVideoManager
extends java.lang.Object
```

Allows a `VideoInterface` to be created abstractly without directly referencing
 the codec class.
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**BoofVideoManager**()` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`static VideoInterface`
`**loadManager**(java.lang.String pathToManager)`
Loads the specified default `VideoInterface`.

`static VideoInterface`
`**loadManagerDefault**()`
Loads the default `VideoInterface`.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BoofVideoManager

```
public BoofVideoManager()
```

  - 

### Method Detail

    - 

#### loadManagerDefault

```
public static VideoInterface loadManagerDefault()
```

Loads the default `VideoInterface`.
Returns:Video interface

    - 

#### loadManager

```
public static VideoInterface loadManager(java.lang.String pathToManager)
```

Loads the specified default `VideoInterface`.
Returns:Video interface

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