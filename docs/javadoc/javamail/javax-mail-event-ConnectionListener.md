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

## Interface ConnectionListener

- 

All Superinterfaces:
EventListener

All Known Implementing Classes:
ConnectionAdapter

---

```
public interface ConnectionListener
extends EventListener
```

This is the Listener interface for Connection events.

Author:
John Mani

- 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description

`void`
`closed(ConnectionEvent e)`
Invoked when a Store/Folder/Transport is closed.

`void`
`disconnected(ConnectionEvent e)`
Invoked when a Store is disconnected.

`void`
`opened(ConnectionEvent e)`
Invoked when a Store/Folder/Transport is opened.

- 

  - 

### Method Detail

    - 

#### opened

```
void opened(ConnectionEvent e)
```

Invoked when a Store/Folder/Transport is opened.

Parameters:
`e` - the ConnectionEvent

    - 

#### disconnected

```
void disconnected(ConnectionEvent e)
```

Invoked when a Store is disconnected. Note that a folder
 cannot be disconnected, so a folder will not fire this event

Parameters:
`e` - the ConnectionEvent

    - 

#### closed

```
void closed(ConnectionEvent e)
```

Invoked when a Store/Folder/Transport is closed.

Parameters:
`e` - the ConnectionEvent

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