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

boofcv.misc

## Class BoofcvClassLoader

- java.lang.Object

- 

  - boofcv.misc.BoofcvClassLoader

- 

All Implemented Interfaces:
XStreamClassLoader

---

```
public class BoofcvClassLoader
extends java.lang.Object
implements XStreamClassLoader
```

Custom ClassLoader for XStream which allows it to run inside of applets
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**BoofcvClassLoader**()` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`java.lang.ClassLoader`
`**getClassLoader**()`
Returns the underlying `ClassLoader`.

`java.lang.Class<?>`
`**loadClass**(java.lang.String name)`
Mimics functionality of `ClassLoader.loadClass(String)`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BoofcvClassLoader

```
public BoofcvClassLoader()
```

  - 

### Method Detail

    - 

#### loadClass

```
public java.lang.Class<?> loadClass(java.lang.String name)
                             throws java.lang.ClassNotFoundException
```

**Description copied from interface: `XStreamClassLoader`**
Mimics functionality of `ClassLoader.loadClass(String)`

**Specified by:**
`loadClass` in interface `XStreamClassLoader`
Throws:
`java.lang.ClassNotFoundException`

    - 

#### getClassLoader

```
public java.lang.ClassLoader getClassLoader()
```

**Description copied from interface: `XStreamClassLoader`**
Returns the underlying `ClassLoader`.

**Specified by:**
`getClassLoader` in interface `XStreamClassLoader`
Returns:instance of ClassLoader

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