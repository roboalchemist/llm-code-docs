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

## Class BodyTerm

- java.lang.Object

- 

  - javax.mail.search.SearchTerm

  - 

    - javax.mail.search.StringTerm

    - 

      - javax.mail.search.BodyTerm

- 

All Implemented Interfaces:
Serializable

---

```
public final class BodyTerm
extends StringTerm
```

This class implements searches on a message body.
 All parts of the message that are of MIME type "text/*" are searched.
 The pattern is a simple string that must appear as a substring in
 the message body.

Author:
Bill Shannon, John Mani
See Also:
Serialized Form

- 

  - 

### Field Summary

    - 

### Fields inherited from class javax.mail.search.StringTerm

`ignoreCase, pattern`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`BodyTerm(String pattern)`
Constructor

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`boolean`
`equals(Object obj)`
Equality comparison.

`boolean`
`match(Message msg)`
The match method.

    - 

### Methods inherited from class javax.mail.search.StringTerm

`getIgnoreCase, getPattern, hashCode, match`

    - 

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BodyTerm

```
public BodyTerm(String pattern)
```

Constructor

Parameters:
`pattern` - The String to search for

  - 

### Method Detail

    - 

#### match

```
public boolean match(Message msg)
```

The match method.

Specified by:
`match` in class `SearchTerm`
Parameters:
`msg` - The pattern search is applied on this Message's body
Returns:
true if the pattern is found; otherwise false

    - 

#### equals

```
public boolean equals(Object obj)
```

Equality comparison.

Overrides:
`equals` in class `StringTerm`

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