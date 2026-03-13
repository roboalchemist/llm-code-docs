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

## Class FolderAdapter

- java.lang.Object

- 

  - javax.mail.event.FolderAdapter

- 

All Implemented Interfaces:
EventListener, FolderListener

---

```
public abstract class FolderAdapter
extends Object
implements FolderListener
```

The adapter which receives Folder events.
 The methods in this class are empty;  this class is provided as a
 convenience for easily creating listeners by extending this class
 and overriding only the methods of interest.

Author:
John Mani

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`FolderAdapter()` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`void`
`folderCreated(FolderEvent e)`
Invoked when a Folder is created.

`void`
`folderDeleted(FolderEvent e)`
Invoked when a folder is deleted.

`void`
`folderRenamed(FolderEvent e)`
Invoked when a folder is renamed.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### FolderAdapter

```
public FolderAdapter()
```

  - 

### Method Detail

    - 

#### folderCreated

```
public void folderCreated(FolderEvent e)
```

Description copied from interface: `FolderListener`
Invoked when a Folder is created.

Specified by:
`folderCreated` in interface `FolderListener`
Parameters:
`e` - the FolderEvent

    - 

#### folderRenamed

```
public void folderRenamed(FolderEvent e)
```

Description copied from interface: `FolderListener`
Invoked when a folder is renamed.

Specified by:
`folderRenamed` in interface `FolderListener`
Parameters:
`e` - the FolderEvent

    - 

#### folderDeleted

```
public void folderDeleted(FolderEvent e)
```

Description copied from interface: `FolderListener`
Invoked when a folder is deleted.

Specified by:
`folderDeleted` in interface `FolderListener`
Parameters:
`e` - the FolderEvent

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