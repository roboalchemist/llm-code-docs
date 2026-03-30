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

## Class ComparisonTerm

- java.lang.Object

- 

  - javax.mail.search.SearchTerm

  - 

    - javax.mail.search.ComparisonTerm

- 

All Implemented Interfaces:
Serializable

Direct Known Subclasses:
DateTerm, IntegerComparisonTerm

---

```
public abstract class ComparisonTerm
extends SearchTerm
```

This class models the comparison operator. This is an abstract
 class; subclasses implement comparisons for different datatypes.

Author:
Bill Shannon, John Mani
See Also:
Serialized Form

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`protected int`
`comparison`
The comparison.

`static int`
`EQ` 

`static int`
`GE` 

`static int`
`GT` 

`static int`
`LE` 

`static int`
`LT` 

`static int`
`NE` 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`ComparisonTerm()` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`boolean`
`equals(Object obj)`
Equality comparison.

`int`
`hashCode()`
Compute a hashCode for this object.

    - 

### Methods inherited from class javax.mail.search.SearchTerm

`match`

    - 

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### LE

```
public static final int LE
```

See Also:
Constant Field Values

    - 

#### LT

```
public static final int LT
```

See Also:
Constant Field Values

    - 

#### EQ

```
public static final int EQ
```

See Also:
Constant Field Values

    - 

#### NE

```
public static final int NE
```

See Also:
Constant Field Values

    - 

#### GT

```
public static final int GT
```

See Also:
Constant Field Values

    - 

#### GE

```
public static final int GE
```

See Also:
Constant Field Values

    - 

#### comparison

```
protected int comparison
```

The comparison.

  - 

### Constructor Detail

    - 

#### ComparisonTerm

```
public ComparisonTerm()
```

  - 

### Method Detail

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