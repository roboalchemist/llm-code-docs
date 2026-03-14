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

com.sun.mail.util

## Class CRLFOutputStream

- java.lang.Object

- 

  - java.io.OutputStream

  - 

    - java.io.FilterOutputStream

    - 

      - com.sun.mail.util.CRLFOutputStream

- 

All Implemented Interfaces:
Closeable, Flushable, AutoCloseable

Direct Known Subclasses:
SMTPOutputStream

---

```
public class CRLFOutputStream
extends FilterOutputStream
```

Convert lines into the canonical format, that is, terminate lines with the
 CRLF sequence.

Author:
John Mani

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`protected boolean`
`atBOL` 

`protected int`
`lastb` 

    - 

### Fields inherited from class java.io.FilterOutputStream

`out`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`CRLFOutputStream(OutputStream os)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`void`
`write(byte[] b)` 

`void`
`write(byte[] b,
     int off,
     int len)` 

`void`
`write(int b)` 

`void`
`writeln()` 

    - 

### Methods inherited from class java.io.FilterOutputStream

`close, flush`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### lastb

```
protected int lastb
```

    - 

#### atBOL

```
protected boolean atBOL
```

  - 

### Constructor Detail

    - 

#### CRLFOutputStream

```
public CRLFOutputStream(OutputStream os)
```

  - 

### Method Detail

    - 

#### write

```
public void write(int b)
           throws IOException
```

Overrides:
`write` in class `FilterOutputStream`
Throws:
`IOException`

    - 

#### write

```
public void write(byte[] b)
           throws IOException
```

Overrides:
`write` in class `FilterOutputStream`
Throws:
`IOException`

    - 

#### write

```
public void write(byte[] b,
                  int off,
                  int len)
           throws IOException
```

Overrides:
`write` in class `FilterOutputStream`
Throws:
`IOException`

    - 

#### writeln

```
public void writeln()
             throws IOException
```

Throws:
`IOException`

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