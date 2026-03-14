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

## Class ASCIIUtility

- java.lang.Object

- 

  - com.sun.mail.util.ASCIIUtility

- 

---

```
public class ASCIIUtility
extends Object
```

- 

  - 

### Method Summary

All Methods Static Methods Concrete Methods 

Modifier and Type
Method and Description

`static byte[]`
`getBytes(InputStream is)` 

`static byte[]`
`getBytes(String s)` 

`static int`
`parseInt(byte[] b,
        int start,
        int end)`
Convert the bytes within the specified range of the given byte 
 array into a signed integer .

`static int`
`parseInt(byte[] b,
        int start,
        int end,
        int radix)`
Convert the bytes within the specified range of the given byte 
 array into a signed integer in the given radix .

`static long`
`parseLong(byte[] b,
         int start,
         int end)`
Convert the bytes within the specified range of the given byte 
 array into a signed long .

`static long`
`parseLong(byte[] b,
         int start,
         int end,
         int radix)`
Convert the bytes within the specified range of the given byte 
 array into a signed long in the given radix .

`static String`
`toString(byte[] b)`
Convert the bytes into a String.

`static String`
`toString(byte[] b,
        int start,
        int end)`
Convert the bytes within the specified range of the given byte 
 array into a String.

`static String`
`toString(ByteArrayInputStream is)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Method Detail

    - 

#### parseInt

```
public static int parseInt(byte[] b,
                           int start,
                           int end,
                           int radix)
                    throws NumberFormatException
```

Convert the bytes within the specified range of the given byte 
 array into a signed integer in the given radix . The range extends 
 from `start` till, but not including `end`. 

 Based on java.lang.Integer.parseInt()

Parameters:
`b` - the bytes
`start` - the first byte offset
`end` - the last byte offset
`radix` - the radix
Returns:
the integer value
Throws:
`NumberFormatException` - for conversion errors

    - 

#### parseInt

```
public static int parseInt(byte[] b,
                           int start,
                           int end)
                    throws NumberFormatException
```

Convert the bytes within the specified range of the given byte 
 array into a signed integer . The range extends from 
 `start` till, but not including `end`.

Parameters:
`b` - the bytes
`start` - the first byte offset
`end` - the last byte offset
Returns:
the integer value
Throws:
`NumberFormatException` - for conversion errors

    - 

#### parseLong

```
public static long parseLong(byte[] b,
                             int start,
                             int end,
                             int radix)
                      throws NumberFormatException
```

Convert the bytes within the specified range of the given byte 
 array into a signed long in the given radix . The range extends 
 from `start` till, but not including `end`. 

 Based on java.lang.Long.parseLong()

Parameters:
`b` - the bytes
`start` - the first byte offset
`end` - the last byte offset
`radix` - the radix
Returns:
the long value
Throws:
`NumberFormatException` - for conversion errors

    - 

#### parseLong

```
public static long parseLong(byte[] b,
                             int start,
                             int end)
                      throws NumberFormatException
```

Convert the bytes within the specified range of the given byte 
 array into a signed long . The range extends from 
 `start` till, but not including `end`. 

Parameters:
`b` - the bytes
`start` - the first byte offset
`end` - the last byte offset
Returns:
the long value
Throws:
`NumberFormatException` - for conversion errors

    - 

#### toString

```
public static String toString(byte[] b,
                              int start,
                              int end)
```

Convert the bytes within the specified range of the given byte 
 array into a String. The range extends from `start`
 till, but not including `end`.

Parameters:
`b` - the bytes
`start` - the first byte offset
`end` - the last byte offset
Returns:
the String

    - 

#### toString

```
public static String toString(byte[] b)
```

Convert the bytes into a String.

Parameters:
`b` - the bytes
Returns:
the String
Since:
JavaMail 1.4.4

    - 

#### toString

```
public static String toString(ByteArrayInputStream is)
```

    - 

#### getBytes

```
public static byte[] getBytes(String s)
```

    - 

#### getBytes

```
public static byte[] getBytes(InputStream is)
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