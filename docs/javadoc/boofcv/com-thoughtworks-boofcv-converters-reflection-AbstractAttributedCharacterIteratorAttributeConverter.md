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

com.thoughtworks.boofcv.converters.reflection

## Class AbstractAttributedCharacterIteratorAttributeConverter

- java.lang.Object

- 

  - AbstractSingleValueConverter

  - 

    - com.thoughtworks.boofcv.converters.reflection.AbstractAttributedCharacterIteratorAttributeConverter

- 

---

```
public class AbstractAttributedCharacterIteratorAttributeConverter
extends AbstractSingleValueConverter
```

An abstract converter implementation for constants of
 `AttributedCharacterIterator.Attribute` and derived types.
Since:
  1.2.2
Author:
  Jörg Schaible

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**AbstractAttributedCharacterIteratorAttributeConverter**(java.lang.Class type)` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`boolean`
`**canConvert**(java.lang.Class type)` 

`java.lang.Object`
`**fromString**(java.lang.String str)` 

`java.lang.String`
`**toString**(java.lang.Object source)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AbstractAttributedCharacterIteratorAttributeConverter

```
public AbstractAttributedCharacterIteratorAttributeConverter(java.lang.Class type)
```

  - 

### Method Detail

    - 

#### canConvert

```
public boolean canConvert(java.lang.Class type)
```

    - 

#### toString

```
public java.lang.String toString(java.lang.Object source)
```

    - 

#### fromString

```
public java.lang.Object fromString(java.lang.String str)
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