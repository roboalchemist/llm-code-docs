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

## Class DateTerm

- java.lang.Object

- 

  - javax.mail.search.SearchTerm

  - 

    - javax.mail.search.ComparisonTerm

    - 

      - javax.mail.search.DateTerm

- 

All Implemented Interfaces:
Serializable

Direct Known Subclasses:
ReceivedDateTerm, SentDateTerm

---

```
public abstract class DateTerm
extends ComparisonTerm
```

This class implements comparisons for Dates

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

`protected Date`
`date`
The date.

    - 

### Fields inherited from class javax.mail.search.ComparisonTerm

`comparison, EQ, GE, GT, LE, LT, NE`

  - 

### Constructor Summary

Constructors 

Modifier
Constructor and Description

`protected `
`DateTerm(int comparison,
        Date date)`
Constructor.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`boolean`
`equals(Object obj)`
Equality comparison.

`int`
`getComparison()`
Return the type of comparison.

`Date`
`getDate()`
Return the Date to compare with.

`int`
`hashCode()`
Compute a hashCode for this object.

`protected boolean`
`match(Date d)`
The date comparison method.

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

#### date

```
protected Date date
```

The date.

  - 

### Constructor Detail

    - 

#### DateTerm

```
protected DateTerm(int comparison,
                   Date date)
```

Constructor.

Parameters:
`comparison` - the comparison type
`date` - The Date to be compared against

  - 

### Method Detail

    - 

#### getDate

```
public Date getDate()
```

Return the Date to compare with.

Returns:
the date

    - 

#### getComparison

```
public int getComparison()
```

Return the type of comparison.

Returns:
the comparison type

    - 

#### match

```
protected boolean match(Date d)
```

The date comparison method.

Parameters:
`d` - the date in the constructor is compared with this date
Returns:
true if the dates match, otherwise false

    - 

#### equals

```
public boolean equals(Object obj)
```

Equality comparison.

Overrides:
`equals` in class `ComparisonTerm`

    - 

#### hashCode

```
public int hashCode()
```

Compute a hashCode for this object.

Overrides:
`hashCode` in class `ComparisonTerm`

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