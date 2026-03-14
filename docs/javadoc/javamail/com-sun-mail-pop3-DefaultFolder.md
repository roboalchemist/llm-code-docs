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

com.sun.mail.pop3

## Class DefaultFolder

- java.lang.Object

- 

  - javax.mail.Folder

  - 

    - com.sun.mail.pop3.DefaultFolder

- 

All Implemented Interfaces:
AutoCloseable

---

```
public class DefaultFolder
extends Folder
```

The POP3 DefaultFolder.  Only contains the "INBOX" folder.

Author:
Christopher Cotton

- 

  - 

### Field Summary

    - 

### Fields inherited from class javax.mail.Folder

`HOLDS_FOLDERS, HOLDS_MESSAGES, mode, READ_ONLY, READ_WRITE, store`

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`void`
`appendMessages(Message[] msgs)`
Append given Messages to this folder.

`void`
`close(boolean expunge)`
Close this Folder.

`boolean`
`create(int type)`
Create this folder on the Store.

`boolean`
`delete(boolean recurse)`
Delete this Folder.

`boolean`
`exists()`
Tests if this folder physically exists on the Store.

`Message[]`
`expunge()`
Expunge (permanently remove) messages marked DELETED.

`Folder`
`getFolder(String name)`
Return the Folder object corresponding to the given name.

`String`
`getFullName()`
Returns the full name of this Folder.

`protected Folder`
`getInbox()` 

`Message`
`getMessage(int msgno)`
Get the Message object corresponding to the given message
 number.

`int`
`getMessageCount()`
Get total number of messages in this Folder.

`String`
`getName()`
Returns the name of this Folder.

`Folder`
`getParent()`
Returns the parent folder of this folder.

`Flags`
`getPermanentFlags()`
Get the permanent flags supported by this Folder.

`char`
`getSeparator()`
Return the delimiter character that separates this Folder's pathname
 from the names of immediate subfolders.

`int`
`getType()`
Returns the type of this Folder, that is, whether this folder can hold
 messages or subfolders or both.

`boolean`
`hasNewMessages()`
Returns true if this Folder has new messages since the last time
 this indication was reset.

`boolean`
`isOpen()`
Indicates whether this Folder is in the 'open' state.

`Folder[]`
`list(String pattern)`
Returns a list of Folders belonging to this Folder's namespace
 that match the specified pattern.

`void`
`open(int mode)`
Open this Folder.

`boolean`
`renameTo(Folder f)`
Rename this Folder.

    - 

### Methods inherited from class javax.mail.Folder

`addConnectionListener, addFolderListener, addMessageChangedListener, addMessageCountListener, close, copyMessages, fetch, finalize, getDeletedMessageCount, getMessages, getMessages, getMessages, getMode, getNewMessageCount, getStore, getUnreadMessageCount, getURLName, isSubscribed, list, listSubscribed, listSubscribed, notifyConnectionListeners, notifyFolderListeners, notifyFolderRenamedListeners, notifyMessageAddedListeners, notifyMessageChangedListeners, notifyMessageRemovedListeners, removeConnectionListener, removeFolderListener, removeMessageChangedListener, removeMessageCountListener, search, search, setFlags, setFlags, setFlags, setSubscribed, toString`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Method Detail

    - 

#### getName

```
public String getName()
```

Description copied from class: `Folder`
Returns the name of this Folder. 

 This method can be invoked on a closed Folder.

Specified by:
`getName` in class `Folder`
Returns:
name of the Folder

    - 

#### getFullName

```
public String getFullName()
```

Description copied from class: `Folder`
Returns the full name of this Folder. If the folder resides under
 the root hierarchy of this Store, the returned name is relative
 to the root. Otherwise an absolute name, starting with the 
 hierarchy delimiter, is returned. 

 This method can be invoked on a closed Folder.

Specified by:
`getFullName` in class `Folder`
Returns:
full name of the Folder

    - 

#### getParent

```
public Folder getParent()
```

Description copied from class: `Folder`
Returns the parent folder of this folder.
 This method can be invoked on a closed Folder. If this folder
 is the top of a folder hierarchy, this method returns null. 

 Note that since Folder objects are not cached, invoking this method
 returns a new distinct Folder object.

Specified by:
`getParent` in class `Folder`
Returns:
Parent folder

    - 

#### exists

```
public boolean exists()
```

Description copied from class: `Folder`
Tests if this folder physically exists on the Store.
 This method can be invoked on a closed Folder.

Specified by:
`exists` in class `Folder`
Returns:
true if the folder exists, otherwise false
See Also:
`Folder.create(int)`

    - 

#### list

```
public Folder[] list(String pattern)
              throws MessagingException
```

Description copied from class: `Folder`
Returns a list of Folders belonging to this Folder's namespace
 that match the specified pattern. Patterns may contain the wildcard
 characters `"%"`, which matches any character except hierarchy
 delimiters, and `"*"`, which matches any character. 

 As an example, given the folder hierarchy: 

```

    Personal/
       Finance/
          Stocks
          Bonus
          StockOptions
       Jokes
 
```

 `list("*")` on "Personal" will return the whole 
 hierarchy. 

 `list("%")` on "Personal" will return "Finance" and 
 "Jokes". 

 `list("Jokes")` on "Personal" will return "Jokes".

 `list("Stock*")` on "Finance" will return "Stocks"
 and "StockOptions". 

 Folder objects are not cached by the Store, so invoking this
 method on the same pattern multiple times will return that many
 distinct Folder objects. 

 This method can be invoked on a closed Folder.

Specified by:
`list` in class `Folder`
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

#### getSeparator

```
public char getSeparator()
```

Description copied from class: `Folder`
Return the delimiter character that separates this Folder's pathname
 from the names of immediate subfolders. This method can be invoked 
 on a closed Folder.

Specified by:
`getSeparator` in class `Folder`
Returns:
Hierarchy separator character

    - 

#### getType

```
public int getType()
```

Description copied from class: `Folder`
Returns the type of this Folder, that is, whether this folder can hold
 messages or subfolders or both. The returned value is an integer
 bitfield with the appropriate bits set. This method can be invoked
 on a closed folder.

Specified by:
`getType` in class `Folder`
Returns:
integer with appropriate bits set
See Also:
`Folder.HOLDS_FOLDERS`, 
`Folder.HOLDS_MESSAGES`

    - 

#### create

```
public boolean create(int type)
               throws MessagingException
```

Description copied from class: `Folder`
Create this folder on the Store. When this folder is created, any
 folders in its path that do not exist are also created. 

 If the creation is successful, a CREATED FolderEvent is delivered
 to any FolderListeners registered on this Folder and this Store.

Specified by:
`create` in class `Folder`
Parameters:
`type` - The type of this folder.
Returns:
true if the creation succeeds, else false.
Throws:
`MessagingException` - for failures
See Also:
`Folder.HOLDS_FOLDERS`, 
`Folder.HOLDS_MESSAGES`, 
`FolderEvent`

    - 

#### hasNewMessages

```
public boolean hasNewMessages()
                       throws MessagingException
```

Description copied from class: `Folder`
Returns true if this Folder has new messages since the last time
 this indication was reset.  When this indication is set or reset
 depends on the Folder implementation (and in the case of IMAP,
 depends on the server).  This method can be used to implement
 a lightweight "check for new mail" operation on a Folder without
 opening it.  (For example, a thread that monitors a mailbox and
 flags when it has new mail.)  This method should indicate whether
 any messages in the Folder have the `RECENT` flag set. 

 Note that this is not an incremental check for new mail, i.e.,
 it cannot be used to determine whether any new messages have
 arrived since the last time this method was invoked. To
 implement incremental checks, the Folder needs to be opened. 

 This method can be invoked on a closed Folder that can contain
 Messages.

Specified by:
`hasNewMessages` in class `Folder`
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

Description copied from class: `Folder`
Return the Folder object corresponding to the given name. Note that
 this folder does not physically have to exist in the Store. The
 `exists()` method on a Folder indicates whether it really
 exists on the Store. 

 In some Stores, name can be an absolute path if it starts with the
 hierarchy delimiter.  Otherwise, it is interpreted relative to
 this Folder. 

 Folder objects are not cached by the Store, so invoking this
 method on the same name multiple times will return that many
 distinct Folder objects. 

 This method can be invoked on a closed Folder.

Specified by:
`getFolder` in class `Folder`
Parameters:
`name` - name of the Folder
Returns:
Folder object
Throws:
`MessagingException` - for failures

    - 

#### getInbox

```
protected Folder getInbox()
                   throws MessagingException
```

Throws:
`MessagingException`

    - 

#### delete

```
public boolean delete(boolean recurse)
               throws MessagingException
```

Description copied from class: `Folder`
Delete this Folder. This method will succeed only on a closed
 Folder. 

 The `recurse` flag controls whether the deletion affects
 subfolders or not. If true, all subfolders are deleted, then this
 folder itself is deleted. If false, the behaviour is dependent on
 the folder type and is elaborated below:

 

 
      - 
 The folder can contain only messages: (type == HOLDS_MESSAGES).
 

 All messages within the folder are removed. The folder 
 itself is then removed. An appropriate FolderEvent is generated by 
 the Store and this folder.

 
      - 
 The folder can contain only subfolders: (type == HOLDS_FOLDERS).
 

 If this folder is empty (does not contain any 
 subfolders at all), it is removed. An appropriate FolderEvent is 
 generated by the Store and this folder.

 If this folder contains any subfolders, the delete fails 
 and returns false.

 
      - 
 The folder can contain subfolders as well as messages: 

 If the folder is empty (no messages or subfolders), it
 is removed. If the folder contains no subfolders, but only messages,
 then all messages are removed. The folder itself is then removed.
 In both the above cases, an appropriate FolderEvent is
 generated by the Store and this folder. 

 If the folder contains subfolders there are 3 possible
 choices an implementation is free to do:
 
  

   
        -  The operation fails, irrespective of whether this folder
 contains messages or not. Some implementations might elect to go
 with this simple approach. The delete() method returns false.

   
        -  Any messages within the folder are removed. Subfolders
 are not removed. The folder itself is not removed or affected
 in any manner. The delete() method returns true. And the 
 exists() method on this folder will return true indicating that
 this folder still exists. 

 An appropriate FolderEvent is generated by the Store and this folder.

   
        -  Any messages within the folder are removed. Subfolders are
 not removed. The folder itself changes its type from 
 HOLDS_FOLDERS | HOLDS_MESSAGES to HOLDS_FOLDERS. Thus new 
 messages cannot be added to this folder, but new subfolders can
 be created underneath. The delete() method returns true indicating
 success. The exists() method on this folder will return true
 indicating that this folder still exists. 

 An appropriate FolderEvent is generated by the Store and this folder.
 

 

Specified by:
`delete` in class `Folder`
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

Description copied from class: `Folder`
Rename this Folder. This method will succeed only on a closed
 Folder. 

 If the rename is successful, a RENAMED FolderEvent is delivered
 to FolderListeners registered on this folder and its containing
 Store.

Specified by:
`renameTo` in class `Folder`
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

#### open

```
public void open(int mode)
          throws MessagingException
```

Description copied from class: `Folder`
Open this Folder. This method is valid only on Folders that
 can contain Messages and that are closed. 

 If this folder is opened successfully, an OPENED ConnectionEvent
 is delivered to any ConnectionListeners registered on this 
 Folder. 

 The effect of opening multiple connections to the same folder
 on a specifc Store is implementation dependent. Some implementations
 allow multiple readers, but only one writer. Others allow
 multiple writers as well as readers.

Specified by:
`open` in class `Folder`
Parameters:
`mode` - open the Folder READ_ONLY or READ_WRITE
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist.
`MessagingException` - for other failures
See Also:
`Folder.READ_ONLY`, 
`Folder.READ_WRITE`, 
`Folder.getType()`, 
`ConnectionEvent`

    - 

#### close

```
public void close(boolean expunge)
           throws MessagingException
```

Description copied from class: `Folder`
Close this Folder. This method is valid only on open Folders. 

 A CLOSED ConnectionEvent is delivered to any ConnectionListeners
 registered on this Folder. Note that the folder is closed even
 if this method terminates abnormally by throwing a
 MessagingException.

Specified by:
`close` in class `Folder`
Parameters:
`expunge` - expunges all deleted messages if this flag is true
Throws:
`MessagingException` - for other failures
See Also:
`ConnectionEvent`

    - 

#### isOpen

```
public boolean isOpen()
```

Description copied from class: `Folder`
Indicates whether this Folder is in the 'open' state.

Specified by:
`isOpen` in class `Folder`
Returns:
true if this Folder is in the 'open' state.

    - 

#### getPermanentFlags

```
public Flags getPermanentFlags()
```

Description copied from class: `Folder`
Get the permanent flags supported by this Folder. Returns a Flags
 object that contains all the flags supported. 

 The special flag `Flags.Flag.USER ` indicates that this Folder
 supports arbitrary user-defined flags. 

 The supported permanent flags for a folder may not be available
 until the folder is opened.

Specified by:
`getPermanentFlags` in class `Folder`
Returns:
permanent flags, or null if not known

    - 

#### getMessageCount

```
public int getMessageCount()
                    throws MessagingException
```

Description copied from class: `Folder`
Get total number of messages in this Folder. 

 This method can be invoked on a closed folder. However, note
 that for some folder implementations, getting the total message
 count can be an expensive operation involving actually opening 
 the folder. In such cases, a provider can choose not to support 
 this functionality in the closed state, in which case this method
 must return -1. 

 Clients invoking this method on a closed folder must be aware
 that this is a potentially expensive operation. Clients must
 also be prepared to handle a return value of -1 in this case.

Specified by:
`getMessageCount` in class `Folder`
Returns:
total number of messages. -1 may be returned
                        by certain implementations if this method is
                        invoked on a closed folder.
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist.
`MessagingException` - for other failures

    - 

#### getMessage

```
public Message getMessage(int msgno)
                   throws MessagingException
```

Description copied from class: `Folder`
Get the Message object corresponding to the given message
 number.  A Message object's message number is the relative
 position of this Message in its Folder. Messages are numbered
 starting at 1 through the total number of message in the folder.
 Note that the message number for a particular Message can change
 during a session if other messages in the Folder are deleted and
 the Folder is expunged. 

 Message objects are light-weight references to the actual message
 that get filled up on demand. Hence Folder implementations are 
 expected to provide light-weight Message objects. 

 Unlike Folder objects, repeated calls to getMessage with the
 same message number will return the same Message object, as
 long as no messages in this folder have been expunged. 

 Since message numbers can change within a session if the folder
 is expunged , clients are advised not to use message numbers as 
 references to messages. Use Message objects instead.

Specified by:
`getMessage` in class `Folder`
Parameters:
`msgno` - the message number
Returns:
the Message object
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist.
`MessagingException` - for other failures
See Also:
`Folder.getMessageCount()`, 
`Folder.fetch(javax.mail.Message[], javax.mail.FetchProfile)`

    - 

#### appendMessages

```
public void appendMessages(Message[] msgs)
                    throws MessagingException
```

Description copied from class: `Folder`
Append given Messages to this folder. This method can be 
 invoked on a closed Folder. An appropriate MessageCountEvent 
 is delivered to any MessageCountListener registered on this 
 folder when the messages arrive in the folder. 

 Folder implementations must not abort this operation if a
 Message in the given message array turns out to be an
 expunged Message.

Specified by:
`appendMessages` in class `Folder`
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

Description copied from class: `Folder`
Expunge (permanently remove) messages marked DELETED. Returns an
 array containing the expunged message objects.  The
 `getMessageNumber` method
 on each of these message objects returns that Message's original
 (that is, prior to the expunge) sequence number. A MessageCountEvent 
 containing the expunged messages is delivered to any 
 MessageCountListeners registered on the folder. 

 Expunge causes the renumbering of Message objects subsequent to
 the expunged messages. Clients that use message numbers as 
 references to messages should be aware of this and should be 
 prepared to deal with the situation (probably by flushing out 
 existing message number caches and reloading them). Because of 
 this complexity, it is better for clients to use Message objects
 as references to messages, rather than message numbers. Any 
 expunged Messages objects still have to be pruned, but other 
 Messages in that folder are not affected by the expunge. 

 After a message is expunged, only the `isExpunged` and 
 `getMessageNumber` methods are still valid on the
 corresponding Message object; other methods may throw
 `MessageRemovedException`

Specified by:
`expunge` in class `Folder`
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