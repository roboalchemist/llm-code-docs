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

## Class Argument

- java.lang.Object

- 

  - com.sun.mail.iap.Argument

- 

---

```
public class Argument
extends Object
```

Author:
John Mani, Bill Shannon

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`protected List<Object>`
`items` 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`Argument()`
Constructor

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`Argument`
`append(Argument arg)`
Append the given Argument to this Argument.

`void`
`write(Protocol protocol)` 

`Argument`
`writeArgument(Argument c)`
Write out as parenthesised list.

`Argument`
`writeAtom(String s)`
Write out given string as an Atom.

`Argument`
`writeBytes(byte[] b)`
Write out given byte[] as a Literal.

`Argument`
`writeBytes(ByteArrayOutputStream b)`
Write out given ByteArrayOutputStream as a Literal.

`Argument`
`writeBytes(Literal b)`
Write out given data as a literal.

`Argument`
`writeNString(String s)`
Write out given string as an NSTRING, depending on the type
 of the characters inside the string.

`Argument`
`writeNString(String s,
            Charset charset)`
Convert the given string into bytes in the specified
 charset, and write the bytes out as an NSTRING

`Argument`
`writeNString(String s,
            String charset)`
Convert the given string into bytes in the specified
 charset, and write the bytes out as an NSTRING

`Argument`
`writeNumber(int i)`
Write out number.

`Argument`
`writeNumber(long i)`
Write out number.

`Argument`
`writeString(String s)`
Write out given string as an ASTRING, depending on the type
 of the characters inside the string.

`Argument`
`writeString(String s,
           Charset charset)`
Convert the given string into bytes in the specified
 charset, and write the bytes out as an ASTRING

`Argument`
`writeString(String s,
           String charset)`
Convert the given string into bytes in the specified
 charset, and write the bytes out as an ASTRING

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### items

```
protected List<Object> items
```

  - 

### Constructor Detail

    - 

#### Argument

```
public Argument()
```

Constructor

  - 

### Method Detail

    - 

#### append

```
public Argument append(Argument arg)
```

Append the given Argument to this Argument. All items
 from the source argument are copied into this destination
 argument.

Parameters:
`arg` - the Argument to append
Returns:
this

    - 

#### writeString

```
public Argument writeString(String s)
```

Write out given string as an ASTRING, depending on the type
 of the characters inside the string. The string should
 contain only ASCII characters. 

 XXX: Hmm .. this should really be called writeASCII()

Parameters:
`s` - String to write out
Returns:
this

    - 

#### writeString

```
public Argument writeString(String s,
                            String charset)
                     throws UnsupportedEncodingException
```

Convert the given string into bytes in the specified
 charset, and write the bytes out as an ASTRING

Parameters:
`s` - String to write out
`charset` - the charset
Returns:
this
Throws:
`UnsupportedEncodingException` - for bad charset

    - 

#### writeString

```
public Argument writeString(String s,
                            Charset charset)
```

Convert the given string into bytes in the specified
 charset, and write the bytes out as an ASTRING

Parameters:
`s` - String to write out
`charset` - the charset
Returns:
this
Since:
JavaMail 1.6.0

    - 

#### writeNString

```
public Argument writeNString(String s)
```

Write out given string as an NSTRING, depending on the type
 of the characters inside the string. The string should
 contain only ASCII characters. 

Parameters:
`s` - String to write out
Returns:
this
Since:
JavaMail 1.5.1

    - 

#### writeNString

```
public Argument writeNString(String s,
                             String charset)
                      throws UnsupportedEncodingException
```

Convert the given string into bytes in the specified
 charset, and write the bytes out as an NSTRING

Parameters:
`s` - String to write out
`charset` - the charset
Returns:
this
Throws:
`UnsupportedEncodingException` - for bad charset
Since:
JavaMail 1.5.1

    - 

#### writeNString

```
public Argument writeNString(String s,
                             Charset charset)
```

Convert the given string into bytes in the specified
 charset, and write the bytes out as an NSTRING

Parameters:
`s` - String to write out
`charset` - the charset
Returns:
this
Since:
JavaMail 1.6.0

    - 

#### writeBytes

```
public Argument writeBytes(byte[] b)
```

Write out given byte[] as a Literal.

Parameters:
`b` - byte[] to write out
Returns:
this

    - 

#### writeBytes

```
public Argument writeBytes(ByteArrayOutputStream b)
```

Write out given ByteArrayOutputStream as a Literal.

Parameters:
`b` - ByteArrayOutputStream to be written out.
Returns:
this

    - 

#### writeBytes

```
public Argument writeBytes(Literal b)
```

Write out given data as a literal.

Parameters:
`b` - Literal representing data to be written out.
Returns:
this

    - 

#### writeAtom

```
public Argument writeAtom(String s)
```

Write out given string as an Atom. Note that an Atom can contain only
 certain US-ASCII characters.  No validation is done on the characters 
 in the string.

Parameters:
`s` - String
Returns:
this

    - 

#### writeNumber

```
public Argument writeNumber(int i)
```

Write out number.

Parameters:
`i` - number
Returns:
this

    - 

#### writeNumber

```
public Argument writeNumber(long i)
```

Write out number.

Parameters:
`i` - number
Returns:
this

    - 

#### writeArgument

```
public Argument writeArgument(Argument c)
```

Write out as parenthesised list.

Parameters:
`c` - the Argument
Returns:
this

    - 

#### write

```
public void write(Protocol protocol)
           throws IOException,
                  ProtocolException
```

Throws:
`IOException`
`ProtocolException`

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