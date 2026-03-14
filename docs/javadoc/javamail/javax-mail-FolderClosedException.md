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

## Class FolderClosedException

- java.lang.Object

- 

  - java.lang.Throwable

  - 

    - java.lang.Exception

    - 

      - javax.mail.MessagingException

      - 

        - javax.mail.FolderClosedException

- 

All Implemented Interfaces:
Serializable

---

```
public class FolderClosedException
extends MessagingException
```

This exception is thrown when a method is invoked on a Messaging object
 and the Folder that owns that object has died due to some reason. 

 Following the exception, the Folder is reset to the "closed" state. 
 All messaging objects owned by the Folder should be considered invalid. 
 The Folder can be reopened using the "open" method to reestablish the 
 lost connection. 

 The getMessage() method returns more detailed information about the
 error that caused this exception. 

Author:
John Mani
See Also:
Serialized Form

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`FolderClosedException(Folder folder)`
Constructs a FolderClosedException.

`FolderClosedException(Folder folder,
                     String message)`
Constructs a FolderClosedException with the specified
 detail message.

`FolderClosedException(Folder folder,
                     String message,
                     Exception e)`
Constructs a FolderClosedException with the specified
 detail message and embedded exception.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`Folder`
`getFolder()`
Returns the dead Folder object

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

#### FolderClosedException

```
public FolderClosedException(Folder folder)
```

Constructs a FolderClosedException.

Parameters:
`folder` - The Folder

    - 

#### FolderClosedException

```
public FolderClosedException(Folder folder,
                             String message)
```

Constructs a FolderClosedException with the specified
 detail message.

Parameters:
`folder` - The Folder
`message` - The detailed error message

    - 

#### FolderClosedException

```
public FolderClosedException(Folder folder,
                             String message,
                             Exception e)
```

Constructs a FolderClosedException with the specified
 detail message and embedded exception.  The exception is chained
 to this exception.

Parameters:
`folder` - The Folder
`message` - The detailed error message
`e` - The embedded exception
Since:
JavaMail 1.5

  - 

### Method Detail

    - 

#### getFolder

```
public Folder getFolder()
```

Returns the dead Folder object

Returns:
the dead Folder object

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