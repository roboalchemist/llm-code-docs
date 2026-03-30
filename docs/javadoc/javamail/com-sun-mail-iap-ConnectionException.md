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

## Class ConnectionException

- java.lang.Object

- 

  - java.lang.Throwable

  - 

    - java.lang.Exception

    - 

      - com.sun.mail.iap.ProtocolException

      - 

        - com.sun.mail.iap.ConnectionException

- 

All Implemented Interfaces:
Serializable

---

```
public class ConnectionException
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

`ConnectionException()`
Constructs an ConnectionException with no detail message.

`ConnectionException(Protocol p,
                   Response r)`
Constructs an ConnectionException with the specified Response.

`ConnectionException(String s)`
Constructs an ConnectionException with the specified detail message.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`Protocol`
`getProtocol()` 

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

#### ConnectionException

```
public ConnectionException()
```

Constructs an ConnectionException with no detail message.

    - 

#### ConnectionException

```
public ConnectionException(String s)
```

Constructs an ConnectionException with the specified detail message.

Parameters:
`s` - the detail message

    - 

#### ConnectionException

```
public ConnectionException(Protocol p,
                           Response r)
```

Constructs an ConnectionException with the specified Response.

Parameters:
`p` - the Protocol object
`r` - the Response

  - 

### Method Detail

    - 

#### getProtocol

```
public Protocol getProtocol()
```

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