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

## Class Authenticator

- java.lang.Object

- 

  - javax.mail.Authenticator

- 

---

```
public abstract class Authenticator
extends Object
```

The class Authenticator represents an object that knows how to obtain
 authentication for a network connection.  Usually, it will do this
 by prompting the user for information.
 

 Applications use this class by creating a subclass, and registering
 an instance of that subclass with the session when it is created.
 When authentication is required, the system will invoke a method
 on the subclass (like getPasswordAuthentication).  The subclass's
 method can query about the authentication being requested with a
 number of inherited methods (getRequestingXXX()), and form an
 appropriate message for the user.
 

 All methods that request authentication have a default implementation
 that fails.

Author:
Bill Foote, Bill Shannon
See Also:
`Authenticator`, 
`Session.getInstance(java.util.Properties,
					javax.mail.Authenticator)`, 
`Session.getDefaultInstance(java.util.Properties,
					javax.mail.Authenticator)`, 
`Session.requestPasswordAuthentication(java.net.InetAddress, int, java.lang.String, java.lang.String, java.lang.String)`, 
`PasswordAuthentication`

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`Authenticator()` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`protected String`
`getDefaultUserName()` 

`protected PasswordAuthentication`
`getPasswordAuthentication()`
Called when password authentication is needed.

`protected int`
`getRequestingPort()` 

`protected String`
`getRequestingPrompt()` 

`protected String`
`getRequestingProtocol()`
Give the protocol that's requesting the connection.

`protected InetAddress`
`getRequestingSite()` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Authenticator

```
public Authenticator()
```

  - 

### Method Detail

    - 

#### getRequestingSite

```
protected final InetAddress getRequestingSite()
```

Returns:
the InetAddress of the site requesting authorization, or null
                if it's not available.

    - 

#### getRequestingPort

```
protected final int getRequestingPort()
```

Returns:
the port for the requested connection

    - 

#### getRequestingProtocol

```
protected final String getRequestingProtocol()
```

Give the protocol that's requesting the connection.  Often this
 will be based on a URLName.

Returns:
the protcol
See Also:
`URLName.getProtocol()`

    - 

#### getRequestingPrompt

```
protected final String getRequestingPrompt()
```

Returns:
the prompt string given by the requestor

    - 

#### getDefaultUserName

```
protected final String getDefaultUserName()
```

Returns:
the default user name given by the requestor

    - 

#### getPasswordAuthentication

```
protected PasswordAuthentication getPasswordAuthentication()
```

Called when password authentication is needed.  Subclasses should
 override the default implementation, which returns null. 

 Note that if this method uses a dialog to prompt the user for this
 information, the dialog needs to block until the user supplies the
 information.  This method can not simply return after showing the
 dialog.

Returns:
The PasswordAuthentication collected from the
                user, or null if none is provided.

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