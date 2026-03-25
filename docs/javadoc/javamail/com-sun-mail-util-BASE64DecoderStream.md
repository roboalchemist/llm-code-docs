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

## Class BASE64DecoderStream

- java.lang.Object

- 

  - java.io.InputStream

  - 

    - java.io.FilterInputStream

    - 

      - com.sun.mail.util.BASE64DecoderStream

- 

All Implemented Interfaces:
Closeable, AutoCloseable

---

```
public class BASE64DecoderStream
extends FilterInputStream
```

This class implements a BASE64 Decoder. It is implemented as
 a FilterInputStream, so one can just wrap this class around
 any input stream and read bytes from this filter. The decoding
 is done as the bytes are read out.

Author:
John Mani, Bill Shannon

- 

  - 

### Field Summary

    - 

### Fields inherited from class java.io.FilterInputStream

`in`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`BASE64DecoderStream(InputStream in)`
Create a BASE64 decoder that decodes the specified input stream.

`BASE64DecoderStream(InputStream in,
                   boolean ignoreErrors)`
Create a BASE64 decoder that decodes the specified input stream.

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`int`
`available()`
Returns the number of bytes that can be read from this input
 stream without blocking.

`static byte[]`
`decode(byte[] inbuf)`
Base64 decode a byte array.

`boolean`
`markSupported()`
Tests if this input stream supports marks.

`int`
`read()`
Read the next decoded byte from this input stream.

`int`
`read(byte[] buf,
    int off,
    int len)`
Reads up to `len` decoded bytes of data from this input stream
 into an array of bytes.

`long`
`skip(long n)`
Skips over and discards n bytes of data from this stream.

    - 

### Methods inherited from class java.io.FilterInputStream

`close, mark, read, reset`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BASE64DecoderStream

```
public BASE64DecoderStream(InputStream in)
```

Create a BASE64 decoder that decodes the specified input stream.
 The System property `mail.mime.base64.ignoreerrors`
 controls whether errors in the encoded data cause an exception
 or are ignored.  The default is false (errors cause exception).

Parameters:
`in` - the input stream

    - 

#### BASE64DecoderStream

```
public BASE64DecoderStream(InputStream in,
                           boolean ignoreErrors)
```

Create a BASE64 decoder that decodes the specified input stream.

Parameters:
`in` - the input stream
`ignoreErrors` - ignore errors in encoded data?

  - 

### Method Detail

    - 

#### read

```
public int read()
         throws IOException
```

Read the next decoded byte from this input stream. The byte
 is returned as an `int` in the range `0` 
 to `255`. If no byte is available because the end of 
 the stream has been reached, the value `-1` is returned.
 This method blocks until input data is available, the end of the 
 stream is detected, or an exception is thrown.

Overrides:
`read` in class `FilterInputStream`
Returns:
next byte of data, or `-1` if the end of the
             stream is reached.
Throws:
`IOException` - if an I/O error occurs.
See Also:
`FilterInputStream.in`

    - 

#### read

```
public int read(byte[] buf,
                int off,
                int len)
         throws IOException
```

Reads up to `len` decoded bytes of data from this input stream
 into an array of bytes. This method blocks until some input is
 available.
 

Overrides:
`read` in class `FilterInputStream`
Parameters:
`buf` - the buffer into which the data is read.
`off` - the start offset of the data.
`len` - the maximum number of bytes read.
Returns:
the total number of bytes read into the buffer, or
             `-1` if there is no more data because the end of
             the stream has been reached.
Throws:
`IOException` - if an I/O error occurs.

    - 

#### skip

```
public long skip(long n)
          throws IOException
```

Skips over and discards n bytes of data from this stream.

Overrides:
`skip` in class `FilterInputStream`
Throws:
`IOException`

    - 

#### markSupported

```
public boolean markSupported()
```

Tests if this input stream supports marks. Currently this class
 does not support marks

Overrides:
`markSupported` in class `FilterInputStream`

    - 

#### available

```
public int available()
              throws IOException
```

Returns the number of bytes that can be read from this input
 stream without blocking. However, this figure is only
 a close approximation in case the original encoded stream
 contains embedded CRLFs; since the CRLFs are discarded, not decoded

Overrides:
`available` in class `FilterInputStream`
Throws:
`IOException`

    - 

#### decode

```
public static byte[] decode(byte[] inbuf)
```

Base64 decode a byte array.  No line breaks are allowed.
 This method is suitable for short strings, such as those
 in the IMAP AUTHENTICATE protocol, but not to decode the
 entire content of a MIME part.

 NOTE: inbuf may only contain valid base64 characters.
       Whitespace is not ignored.

Parameters:
`inbuf` - the byte array
Returns:
the decoded byte array

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