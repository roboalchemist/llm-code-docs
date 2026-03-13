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

com.sun.mail.imap.protocol

## Class BODY

- java.lang.Object

- 

  - com.sun.mail.imap.protocol.BODY

- 

All Implemented Interfaces:
Item

---

```
public class BODY
extends Object
implements Item
```

The BODY fetch response item.

Author:
John Mani, Bill Shannon

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`BODY(FetchResponse r)`
Constructor

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`ByteArray`
`getByteArray()` 

`ByteArrayInputStream`
`getByteArrayInputStream()` 

`String`
`getSection()` 

`boolean`
`isHeader()` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BODY

```
public BODY(FetchResponse r)
     throws ParsingException
```

Constructor

Parameters:
`r` - the FetchResponse
Throws:
`ParsingException` - for parsing failures

  - 

### Method Detail

    - 

#### getByteArray

```
public ByteArray getByteArray()
```

    - 

#### getByteArrayInputStream

```
public ByteArrayInputStream getByteArrayInputStream()
```

    - 

#### isHeader

```
public boolean isHeader()
```

    - 

#### getSection

```
public String getSection()
```

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