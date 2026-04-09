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

javax.mail.internet

## Class ContentDisposition

- java.lang.Object

- 

  - javax.mail.internet.ContentDisposition

- 

---

```
public class ContentDisposition
extends Object
```

This class represents a MIME ContentDisposition value. It provides
 methods to parse a ContentDisposition string into individual components
 and to generate a MIME style ContentDisposition string.

Author:
John Mani

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`ContentDisposition()`
No-arg Constructor.

`ContentDisposition(String s)`
Constructor that takes a ContentDisposition string.

`ContentDisposition(String disposition,
                  ParameterList list)`
Constructor.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`String`
`getDisposition()`
Return the disposition value.

`String`
`getParameter(String name)`
Return the specified parameter value.

`ParameterList`
`getParameterList()`
Return a ParameterList object that holds all the available 
 parameters.

`void`
`setDisposition(String disposition)`
Set the disposition.

`void`
`setParameter(String name,
            String value)`
Set the specified parameter.

`void`
`setParameterList(ParameterList list)`
Set a new ParameterList.

`String`
`toString()`
Retrieve a RFC2045 style string representation of
 this ContentDisposition.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### ContentDisposition

```
public ContentDisposition()
```

No-arg Constructor.

    - 

#### ContentDisposition

```
public ContentDisposition(String disposition,
                          ParameterList list)
```

Constructor.

Parameters:
`disposition` - disposition
`list` - ParameterList
Since:
JavaMail 1.2

    - 

#### ContentDisposition

```
public ContentDisposition(String s)
                   throws ParseException
```

Constructor that takes a ContentDisposition string. The String
 is parsed into its constituents: dispostion and parameters. 
 A ParseException is thrown if the parse fails.

Parameters:
`s` - the ContentDisposition string.
Throws:
`ParseException` - if the parse fails.
Since:
JavaMail 1.2

  - 

### Method Detail

    - 

#### getDisposition

```
public String getDisposition()
```

Return the disposition value.

Returns:
the disposition
Since:
JavaMail 1.2

    - 

#### getParameter

```
public String getParameter(String name)
```

Return the specified parameter value. Returns `null`
 if this parameter is absent.

Parameters:
`name` - the parameter name
Returns:
parameter value
Since:
JavaMail 1.2

    - 

#### getParameterList

```
public ParameterList getParameterList()
```

Return a ParameterList object that holds all the available 
 parameters. Returns null if no parameters are available.

Returns:
ParameterList
Since:
JavaMail 1.2

    - 

#### setDisposition

```
public void setDisposition(String disposition)
```

Set the disposition.  Replaces the existing disposition.

Parameters:
`disposition` - the disposition
Since:
JavaMail 1.2

    - 

#### setParameter

```
public void setParameter(String name,
                         String value)
```

Set the specified parameter. If this parameter already exists,
 it is replaced by this new value.

Parameters:
`name` - parameter name
`value` - parameter value
Since:
JavaMail 1.2

    - 

#### setParameterList

```
public void setParameterList(ParameterList list)
```

Set a new ParameterList.

Parameters:
`list` - ParameterList
Since:
JavaMail 1.2

    - 

#### toString

```
public String toString()
```

Retrieve a RFC2045 style string representation of
 this ContentDisposition. Returns an empty string if
 the conversion failed.

Overrides:
`toString` in class `Object`
Returns:
RFC2045 style string
Since:
JavaMail 1.2

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