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

## Class ContentType

- java.lang.Object

- 

  - javax.mail.internet.ContentType

- 

---

```
public class ContentType
extends Object
```

This class represents a MIME Content-Type value. It provides
 methods to parse a Content-Type string into individual components
 and to generate a MIME style Content-Type string.

Author:
John Mani

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`ContentType()`
No-arg Constructor.

`ContentType(String s)`
Constructor that takes a Content-Type string.

`ContentType(String primaryType,
           String subType,
           ParameterList list)`
Constructor.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`String`
`getBaseType()`
Return the MIME type string, without the parameters.

`String`
`getParameter(String name)`
Return the specified parameter value.

`ParameterList`
`getParameterList()`
Return a ParameterList object that holds all the available 
 parameters.

`String`
`getPrimaryType()`
Return the primary type.

`String`
`getSubType()`
Return the subType.

`boolean`
`match(ContentType cType)`
Match with the specified ContentType object.

`boolean`
`match(String s)`
Match with the specified content-type string.

`void`
`setParameter(String name,
            String value)`
Set the specified parameter.

`void`
`setParameterList(ParameterList list)`
Set a new ParameterList.

`void`
`setPrimaryType(String primaryType)`
Set the primary type.

`void`
`setSubType(String subType)`
Set the subType.

`String`
`toString()`
Retrieve a RFC2045 style string representation of
 this Content-Type.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### ContentType

```
public ContentType()
```

No-arg Constructor.

    - 

#### ContentType

```
public ContentType(String primaryType,
                   String subType,
                   ParameterList list)
```

Constructor.

Parameters:
`primaryType` - primary type
`subType` - subType
`list` - ParameterList

    - 

#### ContentType

```
public ContentType(String s)
            throws ParseException
```

Constructor that takes a Content-Type string. The String
 is parsed into its constituents: primaryType, subType
 and parameters. A ParseException is thrown if the parse fails.

Parameters:
`s` - the Content-Type string.
Throws:
`ParseException` - if the parse fails.

  - 

### Method Detail

    - 

#### getPrimaryType

```
public String getPrimaryType()
```

Return the primary type.

Returns:
the primary type

    - 

#### getSubType

```
public String getSubType()
```

Return the subType.

Returns:
the subType

    - 

#### getBaseType

```
public String getBaseType()
```

Return the MIME type string, without the parameters.
 The returned value is basically the concatenation of
 the primaryType, the '/' character and the secondaryType.

Returns:
the type

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

    - 

#### getParameterList

```
public ParameterList getParameterList()
```

Return a ParameterList object that holds all the available 
 parameters. Returns null if no parameters are available.

Returns:
ParameterList

    - 

#### setPrimaryType

```
public void setPrimaryType(String primaryType)
```

Set the primary type. Overrides existing primary type.

Parameters:
`primaryType` - primary type

    - 

#### setSubType

```
public void setSubType(String subType)
```

Set the subType.  Replaces the existing subType.

Parameters:
`subType` - the subType

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

    - 

#### setParameterList

```
public void setParameterList(ParameterList list)
```

Set a new ParameterList.

Parameters:
`list` - ParameterList

    - 

#### toString

```
public String toString()
```

Retrieve a RFC2045 style string representation of
 this Content-Type. Returns an empty string if
 the conversion failed.

Overrides:
`toString` in class `Object`
Returns:
RFC2045 style string

    - 

#### match

```
public boolean match(ContentType cType)
```

Match with the specified ContentType object. This method
 compares **only the `primaryType` and 
 `subType` **. The parameters of both operands
 are ignored. 

 For example, this method will return `true` when
 comparing the ContentTypes for **"text/plain"**
 and **"text/plain; charset=foobar"**.

 If the `subType` of either operand is the special
 character '*', then the subtype is ignored during the match. 
 For example, this method will return `true` when 
 comparing the ContentTypes for **"text/plain"** 
 and **"text/*" **

Parameters:
`cType` - ContentType to compare this against
Returns:
true if it matches

    - 

#### match

```
public boolean match(String s)
```

Match with the specified content-type string. This method
 compares **only the `primaryType` and 
 `subType` **.
 The parameters of both operands are ignored. 

 For example, this method will return `true` when
 comparing the ContentType for **"text/plain"**
 with **"text/plain; charset=foobar"**.

 If the `subType` of either operand is the special 
 character '*', then the subtype is ignored during the match. 
 For example, this method will return `true` when 
 comparing the ContentType for **"text/plain"** 
 with **"text/*" **

Parameters:
`s` - the content-type string to match
Returns:
true if it matches

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