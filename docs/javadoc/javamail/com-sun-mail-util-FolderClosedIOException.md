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

## Class FolderClosedIOException

- java.lang.Object

- 

  - java.lang.Throwable

  - 

    - java.lang.Exception

    - 

      - java.io.IOException

      - 

        - com.sun.mail.util.FolderClosedIOException

- 

All Implemented Interfaces:
Serializable

---

```
public class FolderClosedIOException
extends IOException
```

A variant of FolderClosedException that can be thrown from methods
 that only throw IOException.  The getContent method will catch this
 exception and translate it back to FolderClosedException.

Author:
Bill Shannon
See Also:
Serialized Form

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`FolderClosedIOException(Folder folder)`
Constructor

`FolderClosedIOException(Folder folder,
                       String message)`
Constructor

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`Folder`
`getFolder()`
Returns the dead Folder object

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

#### FolderClosedIOException

```
public FolderClosedIOException(Folder folder)
```

Constructor

Parameters:
`folder` - the Folder

    - 

#### FolderClosedIOException

```
public FolderClosedIOException(Folder folder,
                               String message)
```

Constructor

Parameters:
`folder` - the Folder
`message` - the detailed error message

  - 

### Method Detail

    - 

#### getFolder

```
public Folder getFolder()
```

Returns the dead Folder object

Returns:
the dead Folder

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