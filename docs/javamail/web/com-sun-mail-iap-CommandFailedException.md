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

## Class CommandFailedException

- java.lang.Object

- 

  - java.lang.Throwable

  - 

    - java.lang.Exception

    - 

      - com.sun.mail.iap.ProtocolException

      - 

        - com.sun.mail.iap.CommandFailedException

- 

All Implemented Interfaces:
Serializable

---

```
public class CommandFailedException
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

`CommandFailedException()`
Constructs an CommandFailedException with no detail message.

`CommandFailedException(Response r)`
Constructs an CommandFailedException with the specified Response.

`CommandFailedException(String s)`
Constructs an CommandFailedException with the specified detail message.

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

#### CommandFailedException

```
public CommandFailedException()
```

Constructs an CommandFailedException with no detail message.

    - 

#### CommandFailedException

```
public CommandFailedException(String s)
```

Constructs an CommandFailedException with the specified detail message.

Parameters:
`s` - the detail message

    - 

#### CommandFailedException

```
public CommandFailedException(Response r)
```

Constructs an CommandFailedException with the specified Response.

Parameters:
`r` - the Response.

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