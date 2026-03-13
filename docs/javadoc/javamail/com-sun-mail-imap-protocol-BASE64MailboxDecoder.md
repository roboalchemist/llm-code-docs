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

## Class BASE64MailboxDecoder

- java.lang.Object

- 

  - com.sun.mail.imap.protocol.BASE64MailboxDecoder

- 

---

```
public class BASE64MailboxDecoder
extends Object
```

See the BASE64MailboxEncoder for a description of the RFC2060 and how
 mailbox names should be encoded.  This class will do the correct decoding
 for mailbox names.

Author:
Christopher Cotton

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`BASE64MailboxDecoder()` 

  - 

### Method Summary

All Methods Static Methods Concrete Methods 

Modifier and Type
Method and Description

`protected static int`
`base64decode(char[] buffer,
            int offset,
            CharacterIterator iter)` 

`static String`
`decode(String original)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BASE64MailboxDecoder

```
public BASE64MailboxDecoder()
```

  - 

### Method Detail

    - 

#### decode

```
public static String decode(String original)
```

    - 

#### base64decode

```
protected static int base64decode(char[] buffer,
                                  int offset,
                                  CharacterIterator iter)
```

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