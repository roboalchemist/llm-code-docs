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

javax.mail.internet

## Class AddressException

- java.lang.Object

- 

  - java.lang.Throwable

  - 

    - java.lang.Exception

    - 

      - javax.mail.MessagingException

      - 

        - javax.mail.internet.ParseException

        - 

          - javax.mail.internet.AddressException

- 

All Implemented Interfaces:
Serializable

---

```
public class AddressException
extends ParseException
```

The exception thrown when a wrongly formatted address is encountered.

Author:
Bill Shannon, Max Spivak
See Also:
Serialized Form

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`protected int`
`pos`
The index in the string where the error occurred, or -1 if not known.

`protected String`
`ref`
The string being parsed.

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AddressException()`
Constructs an AddressException with no detail message.

`AddressException(String s)`
Constructs an AddressException with the specified detail message.

`AddressException(String s,
                String ref)`
Constructs an AddressException with the specified detail message
 and reference info.

`AddressException(String s,
                String ref,
                int pos)`
Constructs an AddressException with the specified detail message
 and reference info.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`int`
`getPos()`
Get the position with the reference string where the error was
 detected (-1 if not relevant).

`String`
`getRef()`
Get the string that was being parsed when the error was detected
 (null if not relevant).

`String`
`toString()`
Override toString method to provide information on
 nested exceptions.

    - 

### Methods inherited from class javax.mail.MessagingException

`getCause, getNextException, setNextException`

    - 

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### ref

```
protected String ref
```

The string being parsed.

    - 

#### pos

```
protected int pos
```

The index in the string where the error occurred, or -1 if not known.

  - 

### Constructor Detail

    - 

#### AddressException

```
public AddressException()
```

Constructs an AddressException with no detail message.

    - 

#### AddressException

```
public AddressException(String s)
```

Constructs an AddressException with the specified detail message.

Parameters:
`s` - the detail message

    - 

#### AddressException

```
public AddressException(String s,
                        String ref)
```

Constructs an AddressException with the specified detail message
 and reference info.

Parameters:
`s` - the detail message
`ref` - the string being parsed

    - 

#### AddressException

```
public AddressException(String s,
                        String ref,
                        int pos)
```

Constructs an AddressException with the specified detail message
 and reference info.

Parameters:
`s` - the detail message
`ref` - the string being parsed
`pos` - the position of the error

  - 

### Method Detail

    - 

#### getRef

```
public String getRef()
```

Get the string that was being parsed when the error was detected
 (null if not relevant).

Returns:
the string that was being parsed

    - 

#### getPos

```
public int getPos()
```

Get the position with the reference string where the error was
 detected (-1 if not relevant).

Returns:
the position within the string of the error

    - 

#### toString

```
public String toString()
```

Description copied from class: `MessagingException`
Override toString method to provide information on
 nested exceptions.

Overrides:
`toString` in class `MessagingException`

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