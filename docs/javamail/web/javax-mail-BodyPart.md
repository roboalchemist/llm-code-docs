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

## Class BodyPart

- java.lang.Object

- 

  - javax.mail.BodyPart

- 

All Implemented Interfaces:
Part

Direct Known Subclasses:
MimeBodyPart

---

```
public abstract class BodyPart
extends Object
implements Part
```

This class models a Part that is contained within a Multipart.
 This is an abstract class. Subclasses provide actual implementations.

 BodyPart implements the Part interface. Thus, it contains a set of
 attributes and a "content".

Author:
John Mani, Bill Shannon

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`protected Multipart`
`parent`
The `Multipart` object containing this `BodyPart`,
 if known.

    - 

### Fields inherited from interface javax.mail.Part

`ATTACHMENT, INLINE`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`BodyPart()` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`Multipart`
`getParent()`
Return the containing `Multipart` object,
 or `null` if not known.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

    - 

### Methods inherited from interface javax.mail.Part

`addHeader, getAllHeaders, getContent, getContentType, getDataHandler, getDescription, getDisposition, getFileName, getHeader, getInputStream, getLineCount, getMatchingHeaders, getNonMatchingHeaders, getSize, isMimeType, removeHeader, setContent, setContent, setDataHandler, setDescription, setDisposition, setFileName, setHeader, setText, writeTo`

- 

  - 

### Field Detail

    - 

#### parent

```
protected Multipart parent
```

The `Multipart` object containing this `BodyPart`,
 if known.

Since:
JavaMail 1.1

  - 

### Constructor Detail

    - 

#### BodyPart

```
public BodyPart()
```

  - 

### Method Detail

    - 

#### getParent

```
public Multipart getParent()
```

Return the containing `Multipart` object,
 or `null` if not known.

Returns:
the parent Multipart

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