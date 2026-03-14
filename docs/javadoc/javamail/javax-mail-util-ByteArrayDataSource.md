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

javax.mail.util

## Class ByteArrayDataSource

- java.lang.Object

- 

  - javax.mail.util.ByteArrayDataSource

- 

All Implemented Interfaces:
DataSource

---

```
public class ByteArrayDataSource
extends Object
implements DataSource
```

A DataSource backed by a byte array.  The byte array may be
 passed in directly, or may be initialized from an InputStream
 or a String.

Since:
JavaMail 1.4
Author:
John Mani, Bill Shannon, Max Spivak

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`ByteArrayDataSource(byte[] data,
                   String type)`
Create a ByteArrayDataSource with data from the
 specified byte array and with the specified MIME type.

`ByteArrayDataSource(InputStream is,
                   String type)`
Create a ByteArrayDataSource with data from the
 specified InputStream and with the specified MIME type.

`ByteArrayDataSource(String data,
                   String type)`
Create a ByteArrayDataSource with data from the
 specified String and with the specified MIME type.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`String`
`getContentType()`
Get the MIME content type of the data.

`InputStream`
`getInputStream()`
Return an InputStream for the data.

`String`
`getName()`
Get the name of the data.

`OutputStream`
`getOutputStream()`
Return an OutputStream for the data.

`void`
`setName(String name)`
Set the name of the data.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### ByteArrayDataSource

```
public ByteArrayDataSource(InputStream is,
                           String type)
                    throws IOException
```

Create a ByteArrayDataSource with data from the
 specified InputStream and with the specified MIME type.
 The InputStream is read completely and the data is
 stored in a byte array.

Parameters:
`is` - the InputStream
`type` - the MIME type
Throws:
`IOException` - errors reading the stream

    - 

#### ByteArrayDataSource

```
public ByteArrayDataSource(byte[] data,
                           String type)
```

Create a ByteArrayDataSource with data from the
 specified byte array and with the specified MIME type.

Parameters:
`data` - the data
`type` - the MIME type

    - 

#### ByteArrayDataSource

```
public ByteArrayDataSource(String data,
                           String type)
                    throws IOException
```

Create a ByteArrayDataSource with data from the
 specified String and with the specified MIME type.
 The MIME type should include a `charset`
 parameter specifying the charset to be used for the
 string.  If the parameter is not included, the
 default charset is used.

Parameters:
`data` - the String
`type` - the MIME type
Throws:
`IOException` - errors reading the String

  - 

### Method Detail

    - 

#### getInputStream

```
public InputStream getInputStream()
                           throws IOException
```

Return an InputStream for the data.
 Note that a new stream is returned each time
 this method is called.

Specified by:
`getInputStream` in interface `DataSource`
Returns:
the InputStream
Throws:
`IOException` - if no data has been set

    - 

#### getOutputStream

```
public OutputStream getOutputStream()
                             throws IOException
```

Return an OutputStream for the data.
 Writing the data is not supported; an `IOException`
 is always thrown.

Specified by:
`getOutputStream` in interface `DataSource`
Throws:
`IOException` - always

    - 

#### getContentType

```
public String getContentType()
```

Get the MIME content type of the data.

Specified by:
`getContentType` in interface `DataSource`
Returns:
the MIME type

    - 

#### getName

```
public String getName()
```

Get the name of the data.
 By default, an empty string ("") is returned.

Specified by:
`getName` in interface `DataSource`
Returns:
the name of this data

    - 

#### setName

```
public void setName(String name)
```

Set the name of the data.

Parameters:
`name` - the name of this data

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