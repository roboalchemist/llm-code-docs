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

## Interface FolderListener

- 

All Superinterfaces:
EventListener

All Known Implementing Classes:
FolderAdapter

---

```
public interface FolderListener
extends EventListener
```

This is the Listener interface for Folder events.

Author:
John Mani

- 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods 

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

  - 

### Method Detail

    - 

#### folderCreated

```
void folderCreated(FolderEvent e)
```

Invoked when a Folder is created.

Parameters:
`e` - the FolderEvent

    - 

#### folderDeleted

```
void folderDeleted(FolderEvent e)
```

Invoked when a folder is deleted.

Parameters:
`e` - the FolderEvent

    - 

#### folderRenamed

```
void folderRenamed(FolderEvent e)
```

Invoked when a folder is renamed.

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