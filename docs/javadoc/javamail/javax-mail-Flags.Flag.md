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

## Class Flags.Flag

- java.lang.Object

- 

  - javax.mail.Flags.Flag

- 

Enclosing class:
Flags

---

```
public static final class Flags.Flag
extends Object
```

This inner class represents an individual system flag. A set
 of standard system flag objects are predefined here.

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`static Flags.Flag`
`ANSWERED`
This message has been answered.

`static Flags.Flag`
`DELETED`
This message is marked deleted.

`static Flags.Flag`
`DRAFT`
This message is a draft.

`static Flags.Flag`
`FLAGGED`
This message is flagged.

`static Flags.Flag`
`RECENT`
This message is recent.

`static Flags.Flag`
`SEEN`
This message is seen.

`static Flags.Flag`
`USER`
A special flag that indicates that this folder supports
 user defined flags.

  - 

### Method Summary

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### ANSWERED

```
public static final Flags.Flag ANSWERED
```

This message has been answered. This flag is set by clients 
 to indicate that this message has been answered to.

    - 

#### DELETED

```
public static final Flags.Flag DELETED
```

This message is marked deleted. Clients set this flag to
 mark a message as deleted. The expunge operation on a folder
 removes all messages in that folder that are marked for deletion.

    - 

#### DRAFT

```
public static final Flags.Flag DRAFT
```

This message is a draft. This flag is set by clients
 to indicate that the message is a draft message.

    - 

#### FLAGGED

```
public static final Flags.Flag FLAGGED
```

This message is flagged. No semantic is defined for this flag.
 Clients alter this flag.

    - 

#### RECENT

```
public static final Flags.Flag RECENT
```

This message is recent. Folder implementations set this flag
 to indicate that this message is new to this folder, that is,
 it has arrived since the last time this folder was opened. 

 Clients cannot alter this flag.

    - 

#### SEEN

```
public static final Flags.Flag SEEN
```

This message is seen. This flag is implicitly set by the 
 implementation when this Message's content is returned 
 to the client in some form. The `getInputStream`
 and `getContent` methods on Message cause this
 flag to be set. 

 Clients can alter this flag.

    - 

#### USER

```
public static final Flags.Flag USER
```

A special flag that indicates that this folder supports
 user defined flags. 

 The implementation sets this flag. Clients cannot alter 
 this flag but can use it to determine if a folder supports
 user defined flags by using
 `folder.getPermanentFlags().contains(Flags.Flag.USER)`.

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