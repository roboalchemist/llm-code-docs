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

## Class FetchProfile.Item

- java.lang.Object

- 

  - javax.mail.FetchProfile.Item

- 

Direct Known Subclasses:
IMAPFolder.FetchProfileItem, UIDFolder.FetchProfileItem

Enclosing class:
FetchProfile

---

```
public static class FetchProfile.Item
extends Object
```

This inner class is the base class of all items that
 can be requested in a FetchProfile. The items currently
 defined here are `ENVELOPE`, `CONTENT_INFO`
 and `FLAGS`. The `UIDFolder` interface 
 defines the `UID` Item as well. 

 Note that this class only has a protected constructor, therby
 restricting new Item types to either this class or subclasses.
 This effectively implements a enumeration of allowed Item types.

See Also:
`UIDFolder`

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`static FetchProfile.Item`
`CONTENT_INFO`
This item is for fetching information about the 
 content of the message.

`static FetchProfile.Item`
`ENVELOPE`
This is the Envelope item.

`static FetchProfile.Item`
`FLAGS`
This is the Flags item.

`static FetchProfile.Item`
`SIZE`
SIZE is a fetch profile item that can be included in a
 `FetchProfile` during a fetch request to a Folder.

  - 

### Constructor Summary

Constructors 

Modifier
Constructor and Description

`protected `
`Item(String name)`
Constructor for an item.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`String`
`toString()`
Include the name in the toString return value for debugging.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### ENVELOPE

```
public static final FetchProfile.Item ENVELOPE
```

This is the Envelope item. 

 The Envelope is an aggregration of the common attributes
 of a Message. Implementations should include the following
 attributes: From, To, Cc, Bcc, ReplyTo, Subject and Date.
 More items may be included as well. 

 For implementations of the IMAP4 protocol (RFC 2060), the 
 Envelope should include the ENVELOPE data item. More items
 may be included too.

    - 

#### CONTENT_INFO

```
public static final FetchProfile.Item CONTENT_INFO
```

This item is for fetching information about the 
 content of the message. 

 This includes all the attributes that describe the content
 of the message. Implementations should include the following
 attributes: ContentType, ContentDisposition, 
 ContentDescription, Size and LineCount. Other items may be
 included as well.

    - 

#### SIZE

```
public static final FetchProfile.Item SIZE
```

SIZE is a fetch profile item that can be included in a
 `FetchProfile` during a fetch request to a Folder.
 This item indicates that the sizes of the messages in the specified 
 range should be prefetched. 

Since:
JavaMail 1.5

    - 

#### FLAGS

```
public static final FetchProfile.Item FLAGS
```

This is the Flags item.

  - 

### Constructor Detail

    - 

#### Item

```
protected Item(String name)
```

Constructor for an item.  The name is used only for debugging.

Parameters:
`name` - the item name

  - 

### Method Detail

    - 

#### toString

```
public String toString()
```

Include the name in the toString return value for debugging.

Overrides:
`toString` in class `Object`

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