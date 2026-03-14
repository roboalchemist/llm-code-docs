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

## Class BEncoderStream

- java.lang.Object

- 

  - java.io.OutputStream

  - 

    - java.io.FilterOutputStream

    - 

      - com.sun.mail.util.BASE64EncoderStream

      - 

        - com.sun.mail.util.BEncoderStream

- 

All Implemented Interfaces:
Closeable, Flushable, AutoCloseable

---

```
public class BEncoderStream
extends BASE64EncoderStream
```

This class implements a 'B' Encoder as defined by RFC2047 for
 encoding MIME headers. It subclasses the BASE64EncoderStream
 class.

Author:
John Mani

- 

  - 

### Field Summary

    - 

### Fields inherited from class java.io.FilterOutputStream

`out`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`BEncoderStream(OutputStream out)`
Create a 'B' encoder that encodes the specified input stream.

  - 

### Method Summary

All Methods Static Methods Concrete Methods 

Modifier and Type
Method and Description

`static int`
`encodedLength(byte[] b)`
Returns the length of the encoded version of this byte array.

    - 

### Methods inherited from class com.sun.mail.util.BASE64EncoderStream

`close, encode, flush, write, write, write`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BEncoderStream

```
public BEncoderStream(OutputStream out)
```

Create a 'B' encoder that encodes the specified input stream.

Parameters:
`out` - the output stream

  - 

### Method Detail

    - 

#### encodedLength

```
public static int encodedLength(byte[] b)
```

Returns the length of the encoded version of this byte array.

Parameters:
`b` - the byte array
Returns:
the length

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