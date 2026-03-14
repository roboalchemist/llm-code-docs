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

com.sun.mail.imap.protocol

## Class ENVELOPE

- java.lang.Object

- 

  - com.sun.mail.imap.protocol.ENVELOPE

- 

All Implemented Interfaces:
Item

---

```
public class ENVELOPE
extends Object
implements Item
```

The ENEVELOPE item of an IMAP FETCH response.

Author:
John Mani, Bill Shannon

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`InternetAddress[]`
`bcc` 

`InternetAddress[]`
`cc` 

`Date`
`date` 

`InternetAddress[]`
`from` 

`String`
`inReplyTo` 

`String`
`messageId` 

`int`
`msgno` 

`InternetAddress[]`
`replyTo` 

`InternetAddress[]`
`sender` 

`String`
`subject` 

`InternetAddress[]`
`to` 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`ENVELOPE(FetchResponse r)` 

  - 

### Method Summary

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### msgno

```
public int msgno
```

    - 

#### date

```
public Date date
```

    - 

#### subject

```
public String subject
```

    - 

#### from

```
public InternetAddress[] from
```

    - 

#### sender

```
public InternetAddress[] sender
```

    - 

#### replyTo

```
public InternetAddress[] replyTo
```

    - 

#### to

```
public InternetAddress[] to
```

    - 

#### cc

```
public InternetAddress[] cc
```

    - 

#### bcc

```
public InternetAddress[] bcc
```

    - 

#### inReplyTo

```
public String inReplyTo
```

    - 

#### messageId

```
public String messageId
```

  - 

### Constructor Detail

    - 

#### ENVELOPE

```
public ENVELOPE(FetchResponse r)
         throws ParsingException
```

Throws:
`ParsingException`

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