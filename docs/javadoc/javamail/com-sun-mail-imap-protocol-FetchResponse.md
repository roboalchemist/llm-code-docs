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

## Class FetchResponse

- java.lang.Object

- 

  - com.sun.mail.iap.Response

  - 

    - com.sun.mail.imap.protocol.IMAPResponse

    - 

      - com.sun.mail.imap.protocol.FetchResponse

- 

---

```
public class FetchResponse
extends IMAPResponse
```

This class represents a FETCH response obtained from the input stream
 of an IMAP server.

Author:
John Mani, Bill Shannon

- 

  - 

### Field Summary

    - 

### Fields inherited from class com.sun.mail.iap.Response

`BAD, buffer, BYE, CONTINUATION, ex, index, NO, OK, pindex, size, SYNTHETIC, tag, TAG_MASK, TAGGED, type, TYPE_MASK, UNTAGGED, utf8`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`FetchResponse(IMAPResponse r)` 

`FetchResponse(IMAPResponse r,
             FetchItem[] fitems)`
Construct a FetchResponse that handles the additional FetchItems.

`FetchResponse(Protocol p)` 

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`Map<String,Object>`
`getExtensionItems()`
Return a map of the extension items found in this fetch response.

`<T extends Item>
T`
`getItem(Class<T> c)` 

`Item`
`getItem(int index)` 

`static <T extends Item>
T`
`getItem(Response[] r,
       int msgno,
       Class<T> c)`
Return the first fetch response item of the given class
 for the given message number.

`int`
`getItemCount()` 

`static <T extends Item>
List<T>`
`getItems(Response[] r,
        int msgno,
        Class<T> c)`
Return all fetch response items of the given class
 for the given message number.

    - 

### Methods inherited from class com.sun.mail.imap.protocol.IMAPResponse

`getKey, getNumber, keyEquals, readSimpleList`

    - 

### Methods inherited from class com.sun.mail.iap.Response

`byeResponse, getException, getRest, getTag, getType, isBAD, isBYE, isContinuation, isNextNonSpace, isNO, isOK, isSynthetic, isTagged, isUnTagged, peekByte, readAtom, readAtomString, readAtomStringList, readByte, readByteArray, readBytes, readLong, readNumber, readString, readString, readStringList, reset, skip, skipSpaces, skipToken, supportsUtf8, toString`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### FetchResponse

```
public FetchResponse(Protocol p)
              throws IOException,
                     ProtocolException
```

Throws:
`IOException`
`ProtocolException`

    - 

#### FetchResponse

```
public FetchResponse(IMAPResponse r)
              throws IOException,
                     ProtocolException
```

Throws:
`IOException`
`ProtocolException`

    - 

#### FetchResponse

```
public FetchResponse(IMAPResponse r,
                     FetchItem[] fitems)
              throws IOException,
                     ProtocolException
```

Construct a FetchResponse that handles the additional FetchItems.

Parameters:
`r` - the IMAPResponse
`fitems` - the fetch items
Throws:
`IOException` - for I/O errors
`ProtocolException` - for protocol failures
Since:
JavaMail 1.4.6

  - 

### Method Detail

    - 

#### getItemCount

```
public int getItemCount()
```

    - 

#### getItem

```
public Item getItem(int index)
```

    - 

#### getItem

```
public <T extends Item> T getItem(Class<T> c)
```

    - 

#### getItem

```
public static <T extends Item> T getItem(Response[] r,
                                         int msgno,
                                         Class<T> c)
```

Return the first fetch response item of the given class
 for the given message number.

Type Parameters:
`T` - the type of fetch item
Parameters:
`r` - the responses
`msgno` - the message number
`c` - the class
Returns:
the fetch item

    - 

#### getItems

```
public static <T extends Item> List<T> getItems(Response[] r,
                                                int msgno,
                                                Class<T> c)
```

Return all fetch response items of the given class
 for the given message number.

Type Parameters:
`T` - the type of fetch items
Parameters:
`r` - the responses
`msgno` - the message number
`c` - the class
Returns:
the list of fetch items
Since:
JavaMail 1.5.2

    - 

#### getExtensionItems

```
public Map<String,Object> getExtensionItems()
```

Return a map of the extension items found in this fetch response.
 The map is indexed by extension item name.  Callers should not
 modify the map.

Returns:
Map of extension items, or null if none
Since:
JavaMail 1.4.6

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