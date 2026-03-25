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

## Class BadCommandException

- java.lang.Object

- 

  - java.lang.Throwable

  - 

    - java.lang.Exception

    - 

      - com.sun.mail.iap.ProtocolException

      - 

        - com.sun.mail.iap.BadCommandException

- 

All Implemented Interfaces:
Serializable

---

```
public class BadCommandException
extends ProtocolException
```

Author:
John Mani
See Also:
Serialized Form

- 

  - 

### Field Summary

    - 

### Fields inherited from class com.sun.mail.iap.ProtocolException

`response`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`BadCommandException()`
Constructs an BadCommandException with no detail message.

`BadCommandException(Response r)`
Constructs an BadCommandException with the specified Response.

`BadCommandException(String s)`
Constructs an BadCommandException with the specified detail message.

  - 

### Method Summary

    - 

### Methods inherited from class com.sun.mail.iap.ProtocolException

`getResponse`

    - 

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BadCommandException

```
public BadCommandException()
```

Constructs an BadCommandException with no detail message.

    - 

#### BadCommandException

```
public BadCommandException(String s)
```

Constructs an BadCommandException with the specified detail message.

Parameters:
`s` - the detail message

    - 

#### BadCommandException

```
public BadCommandException(Response r)
```

Constructs an BadCommandException with the specified Response.

Parameters:
`r` - the Response

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