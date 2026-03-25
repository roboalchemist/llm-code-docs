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

## Class FetchItem

- java.lang.Object

- 

  - com.sun.mail.imap.protocol.FetchItem

- 

---

```
public abstract class FetchItem
extends Object
```

Metadata describing a FETCH item.
 Note that the "name" field MUST be in uppercase. 

Since:
JavaMail 1.4.6
Author:
Bill Shannon

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`FetchItem(String name,
         FetchProfile.Item fetchProfileItem)` 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods Concrete Methods 

Modifier and Type
Method and Description

`FetchProfile.Item`
`getFetchProfileItem()` 

`String`
`getName()` 

`abstract Object`
`parseItem(FetchResponse r)`
Parse the item into some kind of object appropriate for the item.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### FetchItem

```
public FetchItem(String name,
                 FetchProfile.Item fetchProfileItem)
```

  - 

### Method Detail

    - 

#### getName

```
public String getName()
```

    - 

#### getFetchProfileItem

```
public FetchProfile.Item getFetchProfileItem()
```

    - 

#### parseItem

```
public abstract Object parseItem(FetchResponse r)
                          throws ParsingException
```

Parse the item into some kind of object appropriate for the item.
 Note that the item name will have been parsed and skipped already.

Parameters:
`r` - the response
Returns:
the fetch item
Throws:
`ParsingException` - for parsing failures

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