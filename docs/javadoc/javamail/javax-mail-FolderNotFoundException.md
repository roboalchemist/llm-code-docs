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

## Class FolderNotFoundException

- java.lang.Object

- 

  - java.lang.Throwable

  - 

    - java.lang.Exception

    - 

      - javax.mail.MessagingException

      - 

        - javax.mail.FolderNotFoundException

- 

All Implemented Interfaces:
Serializable

---

```
public class FolderNotFoundException
extends MessagingException
```

This exception is thrown by Folder methods, when those
 methods are invoked on a non existent folder.

Author:
John Mani
See Also:
Serialized Form

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`FolderNotFoundException()`
Constructs a FolderNotFoundException with no detail message.

`FolderNotFoundException(Folder folder)`
Constructs a FolderNotFoundException.

`FolderNotFoundException(Folder folder,
                       String s)`
Constructs a FolderNotFoundException with the specified
 detail message.

`FolderNotFoundException(Folder folder,
                       String s,
                       Exception e)`
Constructs a FolderNotFoundException with the specified
 detail message and embedded exception.

`FolderNotFoundException(String s,
                       Folder folder)`
Constructs a FolderNotFoundException with the specified detail message
 and the specified folder.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`Folder`
`getFolder()`
Returns the offending Folder object.

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

#### FolderNotFoundException

```
public FolderNotFoundException()
```

Constructs a FolderNotFoundException with no detail message.

    - 

#### FolderNotFoundException

```
public FolderNotFoundException(Folder folder)
```

Constructs a FolderNotFoundException.

Parameters:
`folder` - The Folder
Since:
JavaMail 1.2

    - 

#### FolderNotFoundException

```
public FolderNotFoundException(Folder folder,
                               String s)
```

Constructs a FolderNotFoundException with the specified
 detail message.

Parameters:
`folder` - The Folder
`s` - The detailed error message
Since:
JavaMail 1.2

    - 

#### FolderNotFoundException

```
public FolderNotFoundException(Folder folder,
                               String s,
                               Exception e)
```

Constructs a FolderNotFoundException with the specified
 detail message and embedded exception.  The exception is chained
 to this exception.

Parameters:
`folder` - The Folder
`s` - The detailed error message
`e` - The embedded exception
Since:
JavaMail 1.5

    - 

#### FolderNotFoundException

```
public FolderNotFoundException(String s,
                               Folder folder)
```

Constructs a FolderNotFoundException with the specified detail message
 and the specified folder.

Parameters:
`s` - The detail message
`folder` - The Folder

  - 

### Method Detail

    - 

#### getFolder

```
public Folder getFolder()
```

Returns the offending Folder object.

Returns:
the Folder object. Note that the returned value can be
                `null`.

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