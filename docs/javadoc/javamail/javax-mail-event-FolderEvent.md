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

javax.mail.event

## Class FolderEvent

- java.lang.Object

- 

  - java.util.EventObject

  - 

    - javax.mail.event.MailEvent

    - 

      - javax.mail.event.FolderEvent

- 

All Implemented Interfaces:
Serializable

---

```
public class FolderEvent
extends MailEvent
```

This class models Folder *existence* events. FolderEvents are
 delivered to FolderListeners registered on the affected Folder as
 well as the containing Store. 

 Service providers vary widely in their ability to notify clients of
 these events.  At a minimum, service providers must notify listeners
 registered on the same Store or Folder object on which the operation
 occurs.  Service providers may also notify listeners when changes
 are made through operations on other objects in the same virtual
 machine, or by other clients in the same or other hosts.  Such
 notifications are not required and are typically not supported
 by mail protocols (including IMAP).

Author:
John Mani, Bill Shannon
See Also:
Serialized Form

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`static int`
`CREATED`
The folder was created.

`static int`
`DELETED`
The folder was deleted.

`protected Folder`
`folder`
The folder the event occurred on.

`protected Folder`
`newFolder`
The folder that represents the new name, in case of a RENAMED event.

`static int`
`RENAMED`
The folder was renamed.

`protected int`
`type`
The event type.

    - 

### Fields inherited from class java.util.EventObject

`source`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`FolderEvent(Object source,
           Folder oldFolder,
           Folder newFolder,
           int type)`
Constructor.

`FolderEvent(Object source,
           Folder folder,
           int type)`
Constructor.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`void`
`dispatch(Object listener)`
Invokes the appropriate FolderListener method

`Folder`
`getFolder()`
Return the affected folder.

`Folder`
`getNewFolder()`
If this event indicates that a folder is renamed, (i.e, the event type
 is RENAMED), then this method returns the Folder object representing the
 new name.

`int`
`getType()`
Return the type of this event.

    - 

### Methods inherited from class java.util.EventObject

`getSource, toString`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### CREATED

```
public static final int CREATED
```

The folder was created.

See Also:
Constant Field Values

    - 

#### DELETED

```
public static final int DELETED
```

The folder was deleted.

See Also:
Constant Field Values

    - 

#### RENAMED

```
public static final int RENAMED
```

The folder was renamed.

See Also:
Constant Field Values

    - 

#### type

```
protected int type
```

The event type.

    - 

#### folder

```
protected transient Folder folder
```

The folder the event occurred on.

    - 

#### newFolder

```
protected transient Folder newFolder
```

The folder that represents the new name, in case of a RENAMED event.

Since:
JavaMail 1.1

  - 

### Constructor Detail

    - 

#### FolderEvent

```
public FolderEvent(Object source,
                   Folder folder,
                   int type)
```

Constructor. 

Parameters:
`source` - The source of the event
`folder` - The affected folder
`type` - The event type

    - 

#### FolderEvent

```
public FolderEvent(Object source,
                   Folder oldFolder,
                   Folder newFolder,
                   int type)
```

Constructor. Use for RENAMED events.

Parameters:
`source` - The source of the event
`oldFolder` - The folder that is renamed
`newFolder` - The folder that represents the new name
`type` - The event type
Since:
JavaMail 1.1

  - 

### Method Detail

    - 

#### getType

```
public int getType()
```

Return the type of this event.

Returns:
type

    - 

#### getFolder

```
public Folder getFolder()
```

Return the affected folder.

Returns:
the affected folder
See Also:
`getNewFolder()`

    - 

#### getNewFolder

```
public Folder getNewFolder()
```

If this event indicates that a folder is renamed, (i.e, the event type
 is RENAMED), then this method returns the Folder object representing the
 new name. 

 The `getFolder()` method returns the folder that is renamed.

Returns:
Folder representing the new name.
Since:
JavaMail 1.1
See Also:
`getFolder()`

    - 

#### dispatch

```
public void dispatch(Object listener)
```

Invokes the appropriate FolderListener method

Specified by:
`dispatch` in class `MailEvent`
Parameters:
`listener` - the listener to invoke on

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