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

## Class BODYSTRUCTURE

- java.lang.Object

- 

  - com.sun.mail.imap.protocol.BODYSTRUCTURE

- 

All Implemented Interfaces:
Item

---

```
public class BODYSTRUCTURE
extends Object
implements Item
```

A BODYSTRUCTURE response.

Author:
John Mani, Bill Shannon

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`String`
`attachment` 

`BODYSTRUCTURE[]`
`bodies` 

`ParameterList`
`cParams` 

`String`
`description` 

`String`
`disposition` 

`ParameterList`
`dParams` 

`String`
`encoding` 

`ENVELOPE`
`envelope` 

`String`
`id` 

`String[]`
`language` 

`int`
`lines` 

`String`
`md5` 

`int`
`msgno` 

`int`
`size` 

`String`
`subtype` 

`String`
`type` 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`BODYSTRUCTURE(FetchResponse r)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`boolean`
`isMulti()` 

`boolean`
`isNested()` 

`boolean`
`isSingle()` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### msgno

```
public int msgno
```

    - 

#### type

```
public String type
```

    - 

#### subtype

```
public String subtype
```

    - 

#### encoding

```
public String encoding
```

    - 

#### lines

```
public int lines
```

    - 

#### size

```
public int size
```

    - 

#### disposition

```
public String disposition
```

    - 

#### id

```
public String id
```

    - 

#### description

```
public String description
```

    - 

#### md5

```
public String md5
```

    - 

#### attachment

```
public String attachment
```

    - 

#### cParams

```
public ParameterList cParams
```

    - 

#### dParams

```
public ParameterList dParams
```

    - 

#### language

```
public String[] language
```

    - 

#### bodies

```
public BODYSTRUCTURE[] bodies
```

    - 

#### envelope

```
public ENVELOPE envelope
```

  - 

### Constructor Detail

    - 

#### BODYSTRUCTURE

```
public BODYSTRUCTURE(FetchResponse r)
              throws ParsingException
```

Throws:
`ParsingException`

  - 

### Method Detail

    - 

#### isMulti

```
public boolean isMulti()
```

    - 

#### isSingle

```
public boolean isSingle()
```

    - 

#### isNested

```
public boolean isNested()
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