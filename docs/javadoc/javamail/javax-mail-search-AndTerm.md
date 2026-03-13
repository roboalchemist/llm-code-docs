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

## Class AndTerm

- java.lang.Object

- 

  - javax.mail.search.SearchTerm

  - 

    - javax.mail.search.AndTerm

- 

All Implemented Interfaces:
Serializable

---

```
public final class AndTerm
extends SearchTerm
```

This class implements the logical AND operator on individual
 SearchTerms.

Author:
Bill Shannon, John Mani
See Also:
Serialized Form

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AndTerm(SearchTerm[] t)`
Constructor that takes an array of SearchTerms.

`AndTerm(SearchTerm t1,
       SearchTerm t2)`
Constructor that takes two terms.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`boolean`
`equals(Object obj)`
Equality comparison.

`SearchTerm[]`
`getTerms()`
Return the search terms.

`int`
`hashCode()`
Compute a hashCode for this object.

`boolean`
`match(Message msg)`
The AND operation.

    - 

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AndTerm

```
public AndTerm(SearchTerm t1,
               SearchTerm t2)
```

Constructor that takes two terms.

Parameters:
`t1` - first term
`t2` - second term

    - 

#### AndTerm

```
public AndTerm(SearchTerm[] t)
```

Constructor that takes an array of SearchTerms.

Parameters:
`t` - array of terms

  - 

### Method Detail

    - 

#### getTerms

```
public SearchTerm[] getTerms()
```

Return the search terms.

Returns:
the search terms

    - 

#### match

```
public boolean match(Message msg)
```

The AND operation. 

 The terms specified in the constructor are applied to
 the given object and the AND operator is applied to their results.

Specified by:
`match` in class `SearchTerm`
Parameters:
`msg` - The specified SearchTerms are applied to this Message
                        and the AND operator is applied to their results.
Returns:
true if the AND succeds, otherwise false

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