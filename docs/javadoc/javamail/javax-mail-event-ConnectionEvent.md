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

## Class ConnectionEvent

- java.lang.Object

- 

  - java.util.EventObject

  - 

    - javax.mail.event.MailEvent

    - 

      - javax.mail.event.ConnectionEvent

- 

All Implemented Interfaces:
Serializable

---

```
public class ConnectionEvent
extends MailEvent
```

This class models Connection events.

Author:
John Mani
See Also:
Serialized Form

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`static int`
`CLOSED`
A connection was closed.

`static int`
`DISCONNECTED`
A connection was disconnected (not currently used).

`static int`
`OPENED`
A connection was opened.

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

`ConnectionEvent(Object source,
               int type)`
Construct a ConnectionEvent.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`void`
`dispatch(Object listener)`
Invokes the appropriate ConnectionListener method

`int`
`getType()`
Return the type of this event

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

#### OPENED

```
public static final int OPENED
```

A connection was opened.

See Also:
Constant Field Values

    - 

#### DISCONNECTED

```
public static final int DISCONNECTED
```

A connection was disconnected (not currently used).

See Also:
Constant Field Values

    - 

#### CLOSED

```
public static final int CLOSED
```

A connection was closed.

See Also:
Constant Field Values

    - 

#### type

```
protected int type
```

The event type.

  - 

### Constructor Detail

    - 

#### ConnectionEvent

```
public ConnectionEvent(Object source,
                       int type)
```

Construct a ConnectionEvent.

Parameters:
`source` - The source object
`type` - the event type

  - 

### Method Detail

    - 

#### getType

```
public int getType()
```

Return the type of this event

Returns:
type

    - 

#### dispatch

```
public void dispatch(Object listener)
```

Invokes the appropriate ConnectionListener method

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