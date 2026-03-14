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

## Class BASE64EncoderStream

- java.lang.Object

- 

  - java.io.OutputStream

  - 

    - java.io.FilterOutputStream

    - 

      - com.sun.mail.util.BASE64EncoderStream

- 

All Implemented Interfaces:
Closeable, Flushable, AutoCloseable

Direct Known Subclasses:
BEncoderStream

---

```
public class BASE64EncoderStream
extends FilterOutputStream
```

This class implements a BASE64 encoder.  It is implemented as
 a FilterOutputStream, so one can just wrap this class around
 any output stream and write bytes into this filter.  The encoding
 is done as the bytes are written out.

Author:
John Mani, Bill Shannon

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

`BASE64EncoderStream(OutputStream out)`
Create a BASE64 encoder that encodes the specified input stream.

`BASE64EncoderStream(OutputStream out,
                   int bytesPerLine)`
Create a BASE64 encoder that encodes the specified output stream.

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`void`
`close()`
Forces any buffered output bytes to be encoded out to the stream
 and closes this output stream

`static byte[]`
`encode(byte[] inbuf)`
Base64 encode a byte array.

`void`
`flush()`
Flushes this output stream and forces any buffered output bytes
 to be encoded out to the stream.

`void`
`write(byte[] b)`
Encodes `b.length` bytes to this output stream.

`void`
`write(byte[] b,
     int off,
     int len)`
Encodes `len` bytes from the specified
 `byte` array starting at offset `off` to
 this output stream.

`void`
`write(int c)`
Encodes the specified `byte` to this output stream.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BASE64EncoderStream

```
public BASE64EncoderStream(OutputStream out,
                           int bytesPerLine)
```

Create a BASE64 encoder that encodes the specified output stream.

Parameters:
`out` - the output stream
`bytesPerLine` - number of bytes per line. The encoder inserts
                        a CRLF sequence after the specified number of bytes,
                        unless bytesPerLine is Integer.MAX_VALUE, in which
                        case no CRLF is inserted.  bytesPerLine is rounded
                        down to a multiple of 4.

    - 

#### BASE64EncoderStream

```
public BASE64EncoderStream(OutputStream out)
```

Create a BASE64 encoder that encodes the specified input stream.
 Inserts the CRLF sequence after outputting 76 bytes.

Parameters:
`out` - the output stream

  - 

### Method Detail

    - 

#### write

```
public void write(byte[] b,
                  int off,
                  int len)
           throws IOException
```

Encodes `len` bytes from the specified
 `byte` array starting at offset `off` to
 this output stream.

Overrides:
`write` in class `FilterOutputStream`
Parameters:
`b` - the data.
`off` - the start offset in the data.
`len` - the number of bytes to write.
Throws:
`IOException` - if an I/O error occurs.

    - 

#### write

```
public void write(byte[] b)
           throws IOException
```

Encodes `b.length` bytes to this output stream.

Overrides:
`write` in class `FilterOutputStream`
Parameters:
`b` - the data to be written.
Throws:
`IOException` - if an I/O error occurs.

    - 

#### write

```
public void write(int c)
           throws IOException
```

Encodes the specified `byte` to this output stream.

Overrides:
`write` in class `FilterOutputStream`
Parameters:
`c` - the `byte`.
Throws:
`IOException` - if an I/O error occurs.

    - 

#### flush

```
public void flush()
           throws IOException
```

Flushes this output stream and forces any buffered output bytes
 to be encoded out to the stream.

Specified by:
`flush` in interface `Flushable`
Overrides:
`flush` in class `FilterOutputStream`
Throws:
`IOException` - if an I/O error occurs.

    - 

#### close

```
public void close()
           throws IOException
```

Forces any buffered output bytes to be encoded out to the stream
 and closes this output stream

Specified by:
`close` in interface `Closeable`
Specified by:
`close` in interface `AutoCloseable`
Overrides:
`close` in class `FilterOutputStream`
Throws:
`IOException`

    - 

#### encode

```
public static byte[] encode(byte[] inbuf)
```

Base64 encode a byte array.  No line breaks are inserted.
 This method is suitable for short strings, such as those
 in the IMAP AUTHENTICATE protocol, but not to encode the
 entire content of a MIME part.

Parameters:
`inbuf` - the byte array
Returns:
the encoded byte array

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