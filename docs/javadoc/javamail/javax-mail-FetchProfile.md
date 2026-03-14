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

## Class FetchProfile

- java.lang.Object

- 

  - javax.mail.FetchProfile

- 

---

```
public class FetchProfile
extends Object
```

Clients use a FetchProfile to list the Message attributes that 
 it wishes to prefetch from the server for a range of messages.

 Messages obtained from a Folder are light-weight objects that 
 typically start off as empty references to the actual messages.
 Such a Message object is filled in "on-demand" when the appropriate 
 get*() methods are invoked on that particular Message. Certain
 server-based message access protocols (Ex: IMAP) allow batch
 fetching of message attributes for a range of messages in a single
 request. Clients that want to use message attributes for a range of
 Messages (Example: to display the top-level headers in a headerlist)
 might want to use the optimization provided by such servers. The
 `FetchProfile` allows the client to indicate this desire
 to the server. 

 Note that implementations are not obligated to support
 FetchProfiles, since there might be cases where the backend service 
 does not allow easy, efficient fetching of such profiles. 

 Sample code that illustrates the use of a FetchProfile is given
 below:
 
 

```

  Message[] msgs = folder.getMessages();

  FetchProfile fp = new FetchProfile();
  fp.add(FetchProfile.Item.ENVELOPE);
  fp.add("X-mailer");
  folder.fetch(msgs, fp);

 
```

Author:
John Mani, Bill Shannon
See Also:
`Folder.fetch(javax.mail.Message[], javax.mail.FetchProfile)`

- 

  - 

### Nested Class Summary

Nested Classes 

Modifier and Type
Class and Description

`static class `
`FetchProfile.Item`
This inner class is the base class of all items that
 can be requested in a FetchProfile.

  - 

### Constructor Summary

Constructors 

Constructor and Description

`FetchProfile()`
Create an empty FetchProfile.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`void`
`add(FetchProfile.Item item)`
Add the given special item as one of the attributes to
 be prefetched.

`void`
`add(String headerName)`
Add the specified header-field to the list of attributes
 to be prefetched.

`boolean`
`contains(FetchProfile.Item item)`
Returns true if the fetch profile contains the given special item.

`boolean`
`contains(String headerName)`
Returns true if the fetch profile contains the given header name.

`String[]`
`getHeaderNames()`
Get the names of the header-fields set in this profile.

`FetchProfile.Item[]`
`getItems()`
Get the items set in this profile.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### FetchProfile

```
public FetchProfile()
```

Create an empty FetchProfile.

  - 

### Method Detail

    - 

#### add

```
public void add(FetchProfile.Item item)
```

Add the given special item as one of the attributes to
 be prefetched.

Parameters:
`item` - the special item to be fetched
See Also:
`FetchProfile.Item.ENVELOPE`, 
`FetchProfile.Item.CONTENT_INFO`, 
`FetchProfile.Item.FLAGS`

    - 

#### add

```
public void add(String headerName)
```

Add the specified header-field to the list of attributes
 to be prefetched.

Parameters:
`headerName` - header to be prefetched

    - 

#### contains

```
public boolean contains(FetchProfile.Item item)
```

Returns true if the fetch profile contains the given special item.

Parameters:
`item` - the Item to test
Returns:
true if the fetch profile contains the given special item

    - 

#### contains

```
public boolean contains(String headerName)
```

Returns true if the fetch profile contains the given header name.

Parameters:
`headerName` - the header to test
Returns:
true if the fetch profile contains the given header name

    - 

#### getItems

```
public FetchProfile.Item[] getItems()
```

Get the items set in this profile.

Returns:
items set in this profile

    - 

#### getHeaderNames

```
public String[] getHeaderNames()
```

Get the names of the header-fields set in this profile.

Returns:
headers set in this profile

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