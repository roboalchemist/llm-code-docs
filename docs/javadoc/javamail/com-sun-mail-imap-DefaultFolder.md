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

com.sun.mail.imap

## Class DefaultFolder

- java.lang.Object

- 

  - javax.mail.Folder

  - 

    - com.sun.mail.imap.IMAPFolder

    - 

      - com.sun.mail.imap.DefaultFolder

- 

All Implemented Interfaces:
ResponseHandler, AutoCloseable, UIDFolder

---

```
public class DefaultFolder
extends IMAPFolder
```

The default IMAP folder (root of the naming hierarchy).

Author:
John Mani

- 

  - 

### Nested Class Summary

    - 

### Nested classes/interfaces inherited from class com.sun.mail.imap.IMAPFolder

`IMAPFolder.FetchProfileItem, IMAPFolder.ProtocolCommand`

  - 

### Field Summary

    - 

### Fields inherited from class com.sun.mail.imap.IMAPFolder

`attributes, availableFlags, exists, fullName, isNamespace, logger, messageCache, messageCacheLock, name, permanentFlags, protocol, separator, type, uidTable, UNKNOWN_SEPARATOR`

    - 

### Fields inherited from class javax.mail.Folder

`HOLDS_FOLDERS, HOLDS_MESSAGES, mode, READ_ONLY, READ_WRITE, store`

    - 

### Fields inherited from interface javax.mail.UIDFolder

`LASTUID, MAXUID`

  - 

### Constructor Summary

Constructors 

Modifier
Constructor and Description

`protected `
`DefaultFolder(IMAPStore store)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`void`
`appendMessages(Message[] msgs)`
Append the given messages into this folder.

`boolean`
`delete(boolean recurse)`
Delete this folder.

`Message[]`
`expunge()`
Expunge all messages marked as DELETED.

`Folder`
`getFolder(String name)`
Get the named subfolder.

`String`
`getName()`
Get the name of this folder.

`Folder`
`getParent()`
Get this folder's parent.

`boolean`
`hasNewMessages()`
Check whether this folder has new messages.

`Folder[]`
`list(String pattern)`
List all subfolders matching the specified pattern.

`Folder[]`
`listSubscribed(String pattern)`
List all subscribed subfolders matching the specified pattern.

`boolean`
`renameTo(Folder f)`
Rename this folder.

    - 

### Methods inherited from class com.sun.mail.imap.IMAPFolder

`addACL, addMessageCountListener, addMessages, addRights, appendUIDMessages, checkClosed, checkExists, checkOpened, checkRange, close, copyMessages, copyUIDMessages, create, doCommand, doCommandIgnoreFailure, doOptionalCommand, doProtocolCommand, exists, expunge, fetch, forceClose, getACL, getAttributes, getDeletedMessageCount, getEnvelopeCommand, getFullName, getHighestModSeq, getMessage, getMessageBySeqNumber, getMessageByUID, getMessageCount, getMessages, getMessagesBySeqNumbers, getMessagesByUID, getMessagesByUID, getMessagesByUIDChangedSince, getNewMessageCount, getPermanentFlags, getProtocol, getQuota, getSeparator, getSortedMessages, getSortedMessages, getStatusItem, getStoreProtocol, getType, getUID, getUIDNext, getUIDNotSticky, getUIDValidity, getUnreadMessageCount, handleResponse, id, idle, idle, isOpen, isSubscribed, keepConnectionAlive, listRights, moveMessages, moveUIDMessages, myRights, newIMAPMessage, open, open, releaseProtocol, releaseStoreProtocol, removeACL, removeRights, search, search, setFlags, setFlags, setFlags, setQuota, setSubscribed, throwClosedException`

    - 

### Methods inherited from class javax.mail.Folder

`addConnectionListener, addFolderListener, addMessageChangedListener, close, finalize, getMessages, getMessages, getMode, getStore, getURLName, list, listSubscribed, notifyConnectionListeners, notifyFolderListeners, notifyFolderRenamedListeners, notifyMessageAddedListeners, notifyMessageChangedListeners, notifyMessageRemovedListeners, removeConnectionListener, removeFolderListener, removeMessageChangedListener, removeMessageCountListener, toString`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### DefaultFolder

```
protected DefaultFolder(IMAPStore store)
```

  - 

### Method Detail

    - 

#### getName

```
public String getName()
```

Description copied from class: `IMAPFolder`
Get the name of this folder.

Overrides:
`getName` in class `IMAPFolder`
Returns:
name of the Folder

    - 

#### getParent

```
public Folder getParent()
```

Description copied from class: `IMAPFolder`
Get this folder's parent.

Overrides:
`getParent` in class `IMAPFolder`
Returns:
Parent folder

    - 

#### list

```
public Folder[] list(String pattern)
              throws MessagingException
```

Description copied from class: `IMAPFolder`
List all subfolders matching the specified pattern.

Overrides:
`list` in class `IMAPFolder`
Parameters:
`pattern` - the match pattern
Returns:
array of matching Folder objects. An empty
                        array is returned if no matching Folders exist.
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist.
`MessagingException` - for other failures
See Also:
`Folder.listSubscribed(java.lang.String)`

    - 

#### listSubscribed

```
public Folder[] listSubscribed(String pattern)
                        throws MessagingException
```

Description copied from class: `IMAPFolder`
List all subscribed subfolders matching the specified pattern.

Overrides:
`listSubscribed` in class `IMAPFolder`
Parameters:
`pattern` - the match pattern
Returns:
array of matching subscribed Folder objects. An
                        empty array is returned if no matching
                        subscribed folders exist.
Throws:
`FolderNotFoundException` - if this folder does
                        not exist.
`MessagingException` - for other failures
See Also:
`Folder.list(java.lang.String)`

    - 

#### hasNewMessages

```
public boolean hasNewMessages()
                       throws MessagingException
```

Description copied from class: `IMAPFolder`
Check whether this folder has new messages.

Overrides:
`hasNewMessages` in class `IMAPFolder`
Returns:
true if the Store has new Messages
Throws:
`FolderNotFoundException` - if this folder does
                        not exist.
`MessagingException` - for other failures

    - 

#### getFolder

```
public Folder getFolder(String name)
                 throws MessagingException
```

Description copied from class: `IMAPFolder`
Get the named subfolder.

Overrides:
`getFolder` in class `IMAPFolder`
Parameters:
`name` - name of the Folder
Returns:
Folder object
Throws:
`MessagingException` - for failures

    - 

#### delete

```
public boolean delete(boolean recurse)
               throws MessagingException
```

Description copied from class: `IMAPFolder`
Delete this folder.

Overrides:
`delete` in class `IMAPFolder`
Parameters:
`recurse` - also delete subfolders?
Returns:
true if the Folder is deleted successfully
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist
`MessagingException` - for other failures
See Also:
`FolderEvent`

    - 

#### renameTo

```
public boolean renameTo(Folder f)
                 throws MessagingException
```

Description copied from class: `IMAPFolder`
Rename this folder.

Overrides:
`renameTo` in class `IMAPFolder`
Parameters:
`f` - a folder representing the new name for this Folder
Returns:
true if the Folder is renamed successfully
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist
`MessagingException` - for other failures
See Also:
`FolderEvent`

    - 

#### appendMessages

```
public void appendMessages(Message[] msgs)
                    throws MessagingException
```

Description copied from class: `IMAPFolder`
Append the given messages into this folder.

Overrides:
`appendMessages` in class `IMAPFolder`
Parameters:
`msgs` - array of Messages to be appended
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist.
`MessagingException` - if the append failed.

    - 

#### expunge

```
public Message[] expunge()
                  throws MessagingException
```

Description copied from class: `IMAPFolder`
Expunge all messages marked as DELETED.

Overrides:
`expunge` in class `IMAPFolder`
Returns:
array of expunged Message objects
Throws:
`FolderNotFoundException` - if this folder does not
                        exist
`MessagingException` - for other failures
See Also:
`Message.isExpunged()`, 
`MessageCountEvent`

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