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

javax.mail

## Class AuthenticationFailedException

- java.lang.Object

- 

  - java.lang.Throwable

  - 

    - java.lang.Exception

    - 

      - javax.mail.MessagingException

      - 

        - javax.mail.AuthenticationFailedException

- 

All Implemented Interfaces:
Serializable

Direct Known Subclasses:
ReferralException

---

```
public class AuthenticationFailedException
extends MessagingException
```

This exception is thrown when the connect method on a Store or
 Transport object fails due to an authentication failure (e.g.,
 bad user name or password).

Author:
Bill Shannon
See Also:
Serialized Form

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AuthenticationFailedException()`
Constructs an AuthenticationFailedException.

`AuthenticationFailedException(String message)`
Constructs an AuthenticationFailedException with the specified
 detail message.

`AuthenticationFailedException(String message,
                             Exception e)`
Constructs an AuthenticationFailedException with the specified
 detail message and embedded exception.

  - 

### Method Summary

    - 

### Methods inherited from class javax.mail.MessagingException

`getCause, getNextException, setNextException, toString`

    - 

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AuthenticationFailedException

```
public AuthenticationFailedException()
```

Constructs an AuthenticationFailedException.

    - 

#### AuthenticationFailedException

```
public AuthenticationFailedException(String message)
```

Constructs an AuthenticationFailedException with the specified
 detail message.

Parameters:
`message` - The detailed error message

    - 

#### AuthenticationFailedException

```
public AuthenticationFailedException(String message,
                                     Exception e)
```

Constructs an AuthenticationFailedException with the specified
 detail message and embedded exception.  The exception is chained
 to this exception.

Parameters:
`message` - The detailed error message
`e` - The embedded exception
Since:
JavaMail 1.5

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