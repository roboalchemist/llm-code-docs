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

com.sun.mail.iap

## Class ByteArray

- java.lang.Object

- 

  - com.sun.mail.iap.ByteArray

- 

---

```
public class ByteArray
extends Object
```

A simple wrapper around a byte array, with a start position and
 count of bytes.

Author:
John Mani

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`ByteArray(byte[] b,
         int start,
         int count)`
Constructor

`ByteArray(int size)`
Constructor that creates a byte array of the specified size.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`byte[]`
`getBytes()`
Returns the internal byte array.

`int`
`getCount()`
Returns the count of bytes

`byte[]`
`getNewBytes()`
Returns a new byte array that is a copy of the data.

`int`
`getStart()`
Returns the start position

`void`
`grow(int incr)`
Grow the byte array by incr bytes.

`void`
`setCount(int count)`
Set the count of bytes.

`ByteArrayInputStream`
`toByteArrayInputStream()`
Returns a ByteArrayInputStream.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### ByteArray

```
public ByteArray(byte[] b,
                 int start,
                 int count)
```

Constructor

Parameters:
`b` - the byte array to wrap
`start` - start position in byte array
`count` - number of bytes in byte array

    - 

#### ByteArray

```
public ByteArray(int size)
```

Constructor that creates a byte array of the specified size.

Parameters:
`size` - the size of the ByteArray
Since:
JavaMail 1.4.1

  - 

### Method Detail

    - 

#### getBytes

```
public byte[] getBytes()
```

Returns the internal byte array. Note that this is a live
 reference to the actual data, not a copy.

Returns:
the wrapped byte array

    - 

#### getNewBytes

```
public byte[] getNewBytes()
```

Returns a new byte array that is a copy of the data.

Returns:
a new byte array with the bytes from start for count

    - 

#### getStart

```
public int getStart()
```

Returns the start position

Returns:
the start position

    - 

#### getCount

```
public int getCount()
```

Returns the count of bytes

Returns:
the number of bytes

    - 

#### setCount

```
public void setCount(int count)
```

Set the count of bytes.

Parameters:
`count` - the number of bytes
Since:
JavaMail 1.4.1

    - 

#### toByteArrayInputStream

```
public ByteArrayInputStream toByteArrayInputStream()
```

Returns a ByteArrayInputStream.

Returns:
the ByteArrayInputStream

    - 

#### grow

```
public void grow(int incr)
```

Grow the byte array by incr bytes.

Parameters:
`incr` - how much to grow
Since:
JavaMail 1.4.1

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