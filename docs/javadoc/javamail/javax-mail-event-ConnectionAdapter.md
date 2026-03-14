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

## Class ConnectionAdapter

- java.lang.Object

- 

  - javax.mail.event.ConnectionAdapter

- 

All Implemented Interfaces:
EventListener, ConnectionListener

---

```
public abstract class ConnectionAdapter
extends Object
implements ConnectionListener
```

The adapter which receives connection events.
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

`ConnectionAdapter()` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

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

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### ConnectionAdapter

```
public ConnectionAdapter()
```

  - 

### Method Detail

    - 

#### opened

```
public void opened(ConnectionEvent e)
```

Description copied from interface: `ConnectionListener`
Invoked when a Store/Folder/Transport is opened.

Specified by:
`opened` in interface `ConnectionListener`
Parameters:
`e` - the ConnectionEvent

    - 

#### disconnected

```
public void disconnected(ConnectionEvent e)
```

Description copied from interface: `ConnectionListener`
Invoked when a Store is disconnected. Note that a folder
 cannot be disconnected, so a folder will not fire this event

Specified by:
`disconnected` in interface `ConnectionListener`
Parameters:
`e` - the ConnectionEvent

    - 

#### closed

```
public void closed(ConnectionEvent e)
```

Description copied from interface: `ConnectionListener`
Invoked when a Store/Folder/Transport is closed.

Specified by:
`closed` in interface `ConnectionListener`
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