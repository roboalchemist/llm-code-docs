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

## Class Folder

- java.lang.Object

- 

  - javax.mail.Folder

- 

All Implemented Interfaces:
AutoCloseable

Direct Known Subclasses:
DefaultFolder, IMAPFolder, POP3Folder

---

```
public abstract class Folder
extends Object
implements AutoCloseable
```

Folder is an abstract class that represents a folder for mail
 messages. Subclasses implement protocol specific Folders.

 Folders can contain Messages, other Folders or both, thus providing
 a tree-like hierarchy rooted at the Store's default folder. (Note 
 that some Folder implementations may not allow both Messages and 
 other Folders in the same Folder).

 The interpretation of folder names is implementation dependent.
 The different levels of hierarchy in a folder's full name
 are separated from each other by the hierarchy delimiter 
 character.

 The case-insensitive full folder name (that is, the full name
 relative to the default folder for a Store) **INBOX**
 is reserved to mean the "primary folder for this user on this
 server".  Not all Stores will provide an INBOX folder, and not
 all users will have an INBOX folder at all times.  The name
 **INBOX** is reserved to refer to this folder,
 when it exists, in Stores that provide it. 

 A Folder object obtained from a Store need not actually exist
 in the backend store. The `exists` method tests whether
 the folder exists or not. The `create` method
 creates a Folder. 

 A Folder is initially in the closed state. Certain methods are valid
 in this state; the documentation for those methods note this.  A
 Folder is opened by calling its 'open' method. All Folder methods,
 except `open`, `delete` and 
 `renameTo`, are valid in this state. 

 The only way to get a Folder is by invoking the 
 `getFolder` method on Store, Folder, or Session, or by invoking 
 the `list` or `listSubscribed` methods 
 on Folder. Folder objects returned by the above methods are not 
 cached by the Store. Thus, invoking the `getFolder` method
 with the same folder name multiple times will return distinct Folder 
 objects.  Likewise for the `list` and `listSubscribed`
 methods. 

 The Message objects within the Folder are cached by the Folder.
 Thus, invoking `getMessage(msgno)` on the same message number
 multiple times will return the same Message object, until an 
 expunge is done on this Folder. 

 Message objects from a Folder are only valid while a Folder is open
 and should not be accessed after the Folder is closed, even if the
 Folder is subsequently reopened.  Instead, new Message objects must
 be fetched from the Folder after the Folder is reopened. 

 Note that a Message's message number can change within a
 session if the containing Folder is expunged using the expunge
 method.  Clients that use message numbers as references to messages
 should be aware of this and should be prepared to deal with this
 situation (probably by flushing out existing message number references
 and reloading them). Because of this complexity, it is better for
 clients to use Message objects as references to messages, rather than
 message numbers. Expunged Message objects still have to be
 pruned, but other Message objects in that folder are not affected by the 
 expunge.

Author:
John Mani, Bill Shannon

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`static int`
`HOLDS_FOLDERS`
This folder can contain other folders

`static int`
`HOLDS_MESSAGES`
This folder can contain messages

`protected int`
`mode`
The open mode of this folder.

`static int`
`READ_ONLY`
The Folder is read only.

`static int`
`READ_WRITE`
The state and contents of this folder can be modified.

`protected Store`
`store`
The parent store.

  - 

### Constructor Summary

Constructors 

Modifier
Constructor and Description

`protected `
`Folder(Store store)`
Constructor that takes a Store object.

  - 

### Method Summary

All Methods Instance Methods Abstract Methods Concrete Methods 

Modifier and Type
Method and Description

`void`
`addConnectionListener(ConnectionListener l)`
Add a listener for Connection events on this Folder.

`void`
`addFolderListener(FolderListener l)`
Add a listener for Folder events on this Folder.

`void`
`addMessageChangedListener(MessageChangedListener l)`
Add a listener for MessageChanged events on this Folder.

`void`
`addMessageCountListener(MessageCountListener l)`
Add a listener for MessageCount events on this Folder.

`abstract void`
`appendMessages(Message[] msgs)`
Append given Messages to this folder.

`void`
`close()`
Close this Folder and expunge deleted messages.

`abstract void`
`close(boolean expunge)`
Close this Folder.

`void`
`copyMessages(Message[] msgs,
            Folder folder)`
Copy the specified Messages from this Folder into another 
 Folder.

`abstract boolean`
`create(int type)`
Create this folder on the Store.

`abstract boolean`
`delete(boolean recurse)`
Delete this Folder.

`abstract boolean`
`exists()`
Tests if this folder physically exists on the Store.

`abstract Message[]`
`expunge()`
Expunge (permanently remove) messages marked DELETED.

`void`
`fetch(Message[] msgs,
     FetchProfile fp)`
Prefetch the items specified in the FetchProfile for the
 given Messages.

`protected void`
`finalize()` 

`int`
`getDeletedMessageCount()`
Get the number of deleted messages in this Folder.

`abstract Folder`
`getFolder(String name)`
Return the Folder object corresponding to the given name.

`abstract String`
`getFullName()`
Returns the full name of this Folder.

`abstract Message`
`getMessage(int msgnum)`
Get the Message object corresponding to the given message
 number.

`abstract int`
`getMessageCount()`
Get total number of messages in this Folder.

`Message[]`
`getMessages()`
Get all Message objects from this Folder.

`Message[]`
`getMessages(int[] msgnums)`
Get the Message objects for message numbers specified in
 the array.

`Message[]`
`getMessages(int start,
           int end)`
Get the Message objects for message numbers ranging from start
 through end, both start and end inclusive.

`int`
`getMode()`
Return the open mode of this folder.

`abstract String`
`getName()`
Returns the name of this Folder.

`int`
`getNewMessageCount()`
Get the number of new messages in this Folder.

`abstract Folder`
`getParent()`
Returns the parent folder of this folder.

`abstract Flags`
`getPermanentFlags()`
Get the permanent flags supported by this Folder.

`abstract char`
`getSeparator()`
Return the delimiter character that separates this Folder's pathname
 from the names of immediate subfolders.

`Store`
`getStore()`
Returns the Store that owns this Folder object.

`abstract int`
`getType()`
Returns the type of this Folder, that is, whether this folder can hold
 messages or subfolders or both.

`int`
`getUnreadMessageCount()`
Get the total number of unread messages in this Folder.

`URLName`
`getURLName()`
Return a URLName representing this folder.

`abstract boolean`
`hasNewMessages()`
Returns true if this Folder has new messages since the last time
 this indication was reset.

`abstract boolean`
`isOpen()`
Indicates whether this Folder is in the 'open' state.

`boolean`
`isSubscribed()`
Returns true if this Folder is subscribed.

`Folder[]`
`list()`
Convenience method that returns the list of folders under this
 Folder.

`abstract Folder[]`
`list(String pattern)`
Returns a list of Folders belonging to this Folder's namespace
 that match the specified pattern.

`Folder[]`
`listSubscribed()`
Convenience method that returns the list of subscribed folders 
 under this Folder.

`Folder[]`
`listSubscribed(String pattern)`
Returns a list of subscribed Folders belonging to this Folder's
 namespace that match the specified pattern.

`protected void`
`notifyConnectionListeners(int type)`
Notify all ConnectionListeners.

`protected void`
`notifyFolderListeners(int type)`
Notify all FolderListeners registered on this Folder and
 this folder's Store.

`protected void`
`notifyFolderRenamedListeners(Folder folder)`
Notify all FolderListeners registered on this Folder and
 this folder's Store about the renaming of this folder.

`protected void`
`notifyMessageAddedListeners(Message[] msgs)`
Notify all MessageCountListeners about the addition of messages
 into this folder.

`protected void`
`notifyMessageChangedListeners(int type,
                             Message msg)`
Notify all MessageChangedListeners.

`protected void`
`notifyMessageRemovedListeners(boolean removed,
                             Message[] msgs)`
Notify all MessageCountListeners about the removal of messages
 from this Folder.

`abstract void`
`open(int mode)`
Open this Folder.

`void`
`removeConnectionListener(ConnectionListener l)`
Remove a Connection event listener.

`void`
`removeFolderListener(FolderListener l)`
Remove a Folder event listener.

`void`
`removeMessageChangedListener(MessageChangedListener l)`
Remove a MessageChanged listener.

`void`
`removeMessageCountListener(MessageCountListener l)`
Remove a MessageCount listener.

`abstract boolean`
`renameTo(Folder f)`
Rename this Folder.

`Message[]`
`search(SearchTerm term)`
Search this Folder for messages matching the specified
 search criterion.

`Message[]`
`search(SearchTerm term,
      Message[] msgs)`
Search the given array of messages for those that match the 
 specified search criterion.

`void`
`setFlags(int[] msgnums,
        Flags flag,
        boolean value)`
Set the specified flags on the messages whose message numbers
 are in the array.

`void`
`setFlags(int start,
        int end,
        Flags flag,
        boolean value)`
Set the specified flags on the messages numbered from start
 through end, both start and end inclusive.

`void`
`setFlags(Message[] msgs,
        Flags flag,
        boolean value)`
Set the specified flags on the messages specified in the array.

`void`
`setSubscribed(boolean subscribe)`
Subscribe or unsubscribe this Folder.

`String`
`toString()`
override the default toString(), it will return the String
 from Folder.getFullName() or if that is null, it will use
 the default toString() behavior.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### store

```
protected Store store
```

The parent store.

    - 

#### mode

```
protected int mode
```

The open mode of this folder.  The open mode is
 `Folder.READ_ONLY`, `Folder.READ_WRITE`,
 or -1 if not known.

Since:
JavaMail 1.1

    - 

#### HOLDS_MESSAGES

```
public static final int HOLDS_MESSAGES
```

This folder can contain messages

See Also:
Constant Field Values

    - 

#### HOLDS_FOLDERS

```
public static final int HOLDS_FOLDERS
```

This folder can contain other folders

See Also:
Constant Field Values

    - 

#### READ_ONLY

```
public static final int READ_ONLY
```

The Folder is read only.  The state and contents of this
 folder cannot be modified.

See Also:
Constant Field Values

    - 

#### READ_WRITE

```
public static final int READ_WRITE
```

The state and contents of this folder can be modified.

See Also:
Constant Field Values

  - 

### Constructor Detail

    - 

#### Folder

```
protected Folder(Store store)
```

Constructor that takes a Store object.

Parameters:
`store` - the Store that holds this folder

  - 

### Method Detail

    - 

#### getName

```
public abstract String getName()
```

Returns the name of this Folder. 

 This method can be invoked on a closed Folder.

Returns:
name of the Folder

    - 

#### getFullName

```
public abstract String getFullName()
```

Returns the full name of this Folder. If the folder resides under
 the root hierarchy of this Store, the returned name is relative
 to the root. Otherwise an absolute name, starting with the 
 hierarchy delimiter, is returned. 

 This method can be invoked on a closed Folder.

Returns:
full name of the Folder

    - 

#### getURLName

```
public URLName getURLName()
                   throws MessagingException
```

Return a URLName representing this folder.  The returned URLName
 does *not* include the password used to access the store.

Returns:
the URLName representing this folder
Throws:
`MessagingException` - for failures
Since:
JavaMail 1.1
See Also:
`URLName`

    - 

#### getStore

```
public Store getStore()
```

Returns the Store that owns this Folder object.
 This method can be invoked on a closed Folder.

Returns:
the Store

    - 

#### getParent

```
public abstract Folder getParent()
                          throws MessagingException
```

Returns the parent folder of this folder.
 This method can be invoked on a closed Folder. If this folder
 is the top of a folder hierarchy, this method returns null. 

 Note that since Folder objects are not cached, invoking this method
 returns a new distinct Folder object.

Returns:
Parent folder
Throws:
`MessagingException` - for failures

    - 

#### exists

```
public abstract boolean exists()
                        throws MessagingException
```

Tests if this folder physically exists on the Store.
 This method can be invoked on a closed Folder.

Returns:
true if the folder exists, otherwise false
Throws:
`MessagingException` - typically if the connection 
                        to the server is lost.
See Also:
`create(int)`

    - 

#### list

```
public abstract Folder[] list(String pattern)
                       throws MessagingException
```

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
`listSubscribed(java.lang.String)`

    - 

#### listSubscribed

```
public Folder[] listSubscribed(String pattern)
                        throws MessagingException
```

Returns a list of subscribed Folders belonging to this Folder's
 namespace that match the specified pattern. If the folder does
 not support subscription, this method should resolve to
 `list`.
 (The default implementation provided here, does just this).
 The pattern can contain wildcards as for `list`. 

 Note that, at a given level of the folder hierarchy, a particular
 folder may not be subscribed, but folders underneath that folder
 in the folder hierarchy may be subscribed.  In order to allow
 walking the folder hierarchy, such unsubscribed folders may be
 returned, indicating that a folder lower in the hierarchy is
 subscribed.  The `isSubscribed` method on a folder will
 tell whether any particular folder is actually subscribed. 

 Folder objects are not cached by the Store, so invoking this
 method on the same pattern multiple times will return that many
 distinct Folder objects. 

 This method can be invoked on a closed Folder.

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
`list(java.lang.String)`

    - 

#### list

```
public Folder[] list()
              throws MessagingException
```

Convenience method that returns the list of folders under this
 Folder. This method just calls the `list(String pattern)`
 method with `"%"` as the match pattern. This method can
 be invoked on a closed Folder.

Returns:
array of Folder objects under this Folder. An
                        empty array is returned if no subfolders exist.
Throws:
`FolderNotFoundException` - if this folder does
                        not exist.
`MessagingException` - for other failures
See Also:
`list(java.lang.String)`

    - 

#### listSubscribed

```
public Folder[] listSubscribed()
                        throws MessagingException
```

Convenience method that returns the list of subscribed folders 
 under this Folder. This method just calls the
 `listSubscribed(String pattern)` method with `"%"`
 as the match pattern. This method can be invoked on a closed Folder.

Returns:
array of subscribed Folder objects under this 
                        Folder. An empty array is returned if no subscribed 
                        subfolders exist.
Throws:
`FolderNotFoundException` - if this folder does
                        not exist.
`MessagingException` - for other failures
See Also:
`listSubscribed(java.lang.String)`

    - 

#### getSeparator

```
public abstract char getSeparator()
                           throws MessagingException
```

Return the delimiter character that separates this Folder's pathname
 from the names of immediate subfolders. This method can be invoked 
 on a closed Folder.

Returns:
Hierarchy separator character
Throws:
`FolderNotFoundException` - if the implementation
                        requires the folder to exist, but it does not
`MessagingException`

    - 

#### getType

```
public abstract int getType()
                     throws MessagingException
```

Returns the type of this Folder, that is, whether this folder can hold
 messages or subfolders or both. The returned value is an integer
 bitfield with the appropriate bits set. This method can be invoked
 on a closed folder.

Returns:
integer with appropriate bits set
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist.
`MessagingException`
See Also:
`HOLDS_FOLDERS`, 
`HOLDS_MESSAGES`

    - 

#### create

```
public abstract boolean create(int type)
                        throws MessagingException
```

Create this folder on the Store. When this folder is created, any
 folders in its path that do not exist are also created. 

 If the creation is successful, a CREATED FolderEvent is delivered
 to any FolderListeners registered on this Folder and this Store.

Parameters:
`type` - The type of this folder.
Returns:
true if the creation succeeds, else false.
Throws:
`MessagingException` - for failures
See Also:
`HOLDS_FOLDERS`, 
`HOLDS_MESSAGES`, 
`FolderEvent`

    - 

#### isSubscribed

```
public boolean isSubscribed()
```

Returns true if this Folder is subscribed. 

 This method can be invoked on a closed Folder. 

 The default implementation provided here just returns true.

Returns:
true if this Folder is subscribed

    - 

#### setSubscribed

```
public void setSubscribed(boolean subscribe)
                   throws MessagingException
```

Subscribe or unsubscribe this Folder. Not all Stores support
 subscription. 

 This method can be invoked on a closed Folder. 

 The implementation provided here just throws the
 MethodNotSupportedException.

Parameters:
`subscribe` - true to subscribe, false to unsubscribe
Throws:
`FolderNotFoundException` - if this folder does
                        not exist.
`MethodNotSupportedException` - if this store
                        does not support subscription
`MessagingException` - for other failures

    - 

#### hasNewMessages

```
public abstract boolean hasNewMessages()
                                throws MessagingException
```

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

Returns:
true if the Store has new Messages
Throws:
`FolderNotFoundException` - if this folder does
                        not exist.
`MessagingException` - for other failures

    - 

#### getFolder

```
public abstract Folder getFolder(String name)
                          throws MessagingException
```

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

Parameters:
`name` - name of the Folder
Returns:
Folder object
Throws:
`MessagingException` - for failures

    - 

#### delete

```
public abstract boolean delete(boolean recurse)
                        throws MessagingException
```

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
 

 

Parameters:
`recurse` - also delete subfolders?
Returns:
true if the Folder is deleted successfully
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist
`IllegalStateException` - if this folder is not in 
                        the closed state.
`MessagingException` - for other failures
See Also:
`FolderEvent`

    - 

#### renameTo

```
public abstract boolean renameTo(Folder f)
                          throws MessagingException
```

Rename this Folder. This method will succeed only on a closed
 Folder. 

 If the rename is successful, a RENAMED FolderEvent is delivered
 to FolderListeners registered on this folder and its containing
 Store.

Parameters:
`f` - a folder representing the new name for this Folder
Returns:
true if the Folder is renamed successfully
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist
`IllegalStateException` - if this folder is not in 
                        the closed state.
`MessagingException` - for other failures
See Also:
`FolderEvent`

    - 

#### open

```
public abstract void open(int mode)
                   throws MessagingException
```

Open this Folder. This method is valid only on Folders that
 can contain Messages and that are closed. 

 If this folder is opened successfully, an OPENED ConnectionEvent
 is delivered to any ConnectionListeners registered on this 
 Folder. 

 The effect of opening multiple connections to the same folder
 on a specifc Store is implementation dependent. Some implementations
 allow multiple readers, but only one writer. Others allow
 multiple writers as well as readers.

Parameters:
`mode` - open the Folder READ_ONLY or READ_WRITE
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist.
`IllegalStateException` - if this folder is not in 
                        the closed state.
`MessagingException` - for other failures
See Also:
`READ_ONLY`, 
`READ_WRITE`, 
`getType()`, 
`ConnectionEvent`

    - 

#### close

```
public abstract void close(boolean expunge)
                    throws MessagingException
```

Close this Folder. This method is valid only on open Folders. 

 A CLOSED ConnectionEvent is delivered to any ConnectionListeners
 registered on this Folder. Note that the folder is closed even
 if this method terminates abnormally by throwing a
 MessagingException.

Parameters:
`expunge` - expunges all deleted messages if this flag is true
Throws:
`IllegalStateException` - if this folder is not opened
`MessagingException` - for other failures
See Also:
`ConnectionEvent`

    - 

#### close

```
public void close()
           throws MessagingException
```

Close this Folder and expunge deleted messages. 

 A CLOSED ConnectionEvent is delivered to any ConnectionListeners
 registered on this Folder. Note that the folder is closed even
 if this method terminates abnormally by throwing a
 MessagingException. 

 This method supports the `AutoCloseable`
 interface. 

 This implementation calls `close(true)`.

Specified by:
`close` in interface `AutoCloseable`
Throws:
`IllegalStateException` - if this folder is not opened
`MessagingException` - for other failures
Since:
JavaMail 1.6
See Also:
`ConnectionEvent`

    - 

#### isOpen

```
public abstract boolean isOpen()
```

Indicates whether this Folder is in the 'open' state.

Returns:
true if this Folder is in the 'open' state.

    - 

#### getMode

```
public int getMode()
```

Return the open mode of this folder.  Returns
 `Folder.READ_ONLY`, `Folder.READ_WRITE`,
 or -1 if the open mode is not known (usually only because an older
 `Folder` provider has not been updated to use this new
 method).

Returns:
the open mode of this folder
Throws:
`IllegalStateException` - if this folder is not opened
Since:
JavaMail 1.1

    - 

#### getPermanentFlags

```
public abstract Flags getPermanentFlags()
```

Get the permanent flags supported by this Folder. Returns a Flags
 object that contains all the flags supported. 

 The special flag `Flags.Flag.USER ` indicates that this Folder
 supports arbitrary user-defined flags. 

 The supported permanent flags for a folder may not be available
 until the folder is opened.

Returns:
permanent flags, or null if not known

    - 

#### getMessageCount

```
public abstract int getMessageCount()
                             throws MessagingException
```

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

Returns:
total number of messages. -1 may be returned
                        by certain implementations if this method is
                        invoked on a closed folder.
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist.
`MessagingException` - for other failures

    - 

#### getNewMessageCount

```
public int getNewMessageCount()
                       throws MessagingException
```

Get the number of new messages in this Folder. 

 This method can be invoked on a closed folder. However, note
 that for some folder implementations, getting the new message
 count can be an expensive operation involving actually opening 
 the folder. In such cases, a provider can choose not to support 
 this functionality in the closed state, in which case this method
 must return -1. 

 Clients invoking this method on a closed folder must be aware
 that this is a potentially expensive operation. Clients must
 also be prepared to handle a return value of -1 in this case. 

 This implementation returns -1 if this folder is closed. Else
 this implementation gets each Message in the folder using
 `getMessage(int)` and checks whether its
 `RECENT` flag is set. The total number of messages
 that have this flag set is returned.

Returns:
number of new messages. -1 may be returned
                        by certain implementations if this method is
                        invoked on a closed folder.
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist.
`MessagingException` - for other failures

    - 

#### getUnreadMessageCount

```
public int getUnreadMessageCount()
                          throws MessagingException
```

Get the total number of unread messages in this Folder. 

 This method can be invoked on a closed folder. However, note
 that for some folder implementations, getting the unread message
 count can be an expensive operation involving actually opening 
 the folder. In such cases, a provider can choose not to support 
 this functionality in the closed state, in which case this method
 must return -1. 

 Clients invoking this method on a closed folder must be aware
 that this is a potentially expensive operation. Clients must
 also be prepared to handle a return value of -1 in this case. 

 This implementation returns -1 if this folder is closed. Else
 this implementation gets each Message in the folder using
 `getMessage(int)` and checks whether its
 `SEEN` flag is set. The total number of messages
 that do not have this flag set is returned.

Returns:
total number of unread messages. -1 may be returned
                        by certain implementations if this method is
                        invoked on a closed folder.
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist.
`MessagingException` - for other failures

    - 

#### getDeletedMessageCount

```
public int getDeletedMessageCount()
                           throws MessagingException
```

Get the number of deleted messages in this Folder. 

 This method can be invoked on a closed folder. However, note
 that for some folder implementations, getting the deleted message
 count can be an expensive operation involving actually opening 
 the folder. In such cases, a provider can choose not to support 
 this functionality in the closed state, in which case this method
 must return -1. 

 Clients invoking this method on a closed folder must be aware
 that this is a potentially expensive operation. Clients must
 also be prepared to handle a return value of -1 in this case. 

 This implementation returns -1 if this folder is closed. Else
 this implementation gets each Message in the folder using
 `getMessage(int)` and checks whether its
 `DELETED` flag is set. The total number of messages
 that have this flag set is returned.

Returns:
number of deleted messages. -1 may be returned
                        by certain implementations if this method is
                        invoked on a closed folder.
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist.
`MessagingException` - for other failures
Since:
JavaMail 1.3

    - 

#### getMessage

```
public abstract Message getMessage(int msgnum)
                            throws MessagingException
```

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

Parameters:
`msgnum` - the message number
Returns:
the Message object
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist.
`IllegalStateException` - if this folder is not opened
`IndexOutOfBoundsException` - if the message number
                        is out of range.
`MessagingException` - for other failures
See Also:
`getMessageCount()`, 
`fetch(javax.mail.Message[], javax.mail.FetchProfile)`

    - 

#### getMessages

```
public Message[] getMessages(int start,
                             int end)
                      throws MessagingException
```

Get the Message objects for message numbers ranging from start
 through end, both start and end inclusive. Note that message 
 numbers start at 1, not 0. 

 Message objects are light-weight references to the actual message
 that get filled up on demand. Hence Folder implementations are 
 expected to provide light-weight Message objects. 

 This implementation uses getMessage(index) to obtain the required
 Message objects. Note that the returned array must contain 
 `(end-start+1)` Message objects.

Parameters:
`start` - the number of the first message
`end` - the number of the last message
Returns:
the Message objects
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist.
`IllegalStateException` - if this folder is not opened.
`IndexOutOfBoundsException` - if the start or end
                        message numbers are out of range.
`MessagingException` - for other failures
See Also:
`fetch(javax.mail.Message[], javax.mail.FetchProfile)`

    - 

#### getMessages

```
public Message[] getMessages(int[] msgnums)
                      throws MessagingException
```

Get the Message objects for message numbers specified in
 the array. 

 Message objects are light-weight references to the actual message
 that get filled up on demand. Hence Folder implementations are 
 expected to provide light-weight Message objects. 

 This implementation uses getMessage(index) to obtain the required
 Message objects. Note that the returned array must contain 
 `msgnums.length` Message objects

Parameters:
`msgnums` - the array of message numbers
Returns:
the array of Message objects.
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist.
`IllegalStateException` - if this folder is not opened.
`IndexOutOfBoundsException` - if any message number
                        in the given array is out of range.
`MessagingException` - for other failures
See Also:
`fetch(javax.mail.Message[], javax.mail.FetchProfile)`

    - 

#### getMessages

```
public Message[] getMessages()
                      throws MessagingException
```

Get all Message objects from this Folder. Returns an empty array
 if the folder is empty.

 Clients can use Message objects (instead of sequence numbers) 
 as references to the messages within a folder; this method supplies 
 the Message objects to the client. Folder implementations are 
 expected to provide light-weight Message objects, which get
 filled on demand. 

 This implementation invokes `getMessageCount()` to get
 the current message count and then uses `getMessage()`
 to get Message objects from 1 till the message count.

Returns:
array of Message objects, empty array if folder
                        is empty.
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist.
`IllegalStateException` - if this folder is not opened.
`MessagingException` - for other failures
See Also:
`fetch(javax.mail.Message[], javax.mail.FetchProfile)`

    - 

#### appendMessages

```
public abstract void appendMessages(Message[] msgs)
                             throws MessagingException
```

Append given Messages to this folder. This method can be 
 invoked on a closed Folder. An appropriate MessageCountEvent 
 is delivered to any MessageCountListener registered on this 
 folder when the messages arrive in the folder. 

 Folder implementations must not abort this operation if a
 Message in the given message array turns out to be an
 expunged Message.

Parameters:
`msgs` - array of Messages to be appended
Throws:
`FolderNotFoundException` - if this folder does 
                        not exist.
`MessagingException` - if the append failed.

    - 

#### fetch

```
public void fetch(Message[] msgs,
                  FetchProfile fp)
           throws MessagingException
```

Prefetch the items specified in the FetchProfile for the
 given Messages. 

 Clients use this method to indicate that the specified items are 
 needed en-masse for the given message range. Implementations are 
 expected to retrieve these items for the given message range in
 a efficient manner. Note that this method is just a hint to the
 implementation to prefetch the desired items. 

 An example is a client filling its header-view window with
 the Subject, From and X-mailer headers for all messages in the 
 folder.
 

```

  Message[] msgs = folder.getMessages();

  FetchProfile fp = new FetchProfile();
  fp.add(FetchProfile.Item.ENVELOPE);
  fp.add("X-mailer");
  folder.fetch(msgs, fp);
  
  for (int i = 0; i < folder.getMessageCount(); i++) {
      display(msg[i].getFrom());
      display(msg[i].getSubject());
      display(msg[i].getHeader("X-mailer"));
  }

 
```

 The implementation provided here just returns without
 doing anything useful. Providers wanting to provide a real 
 implementation for this method should override this method.

Parameters:
`msgs` - fetch items for these messages
`fp` - the FetchProfile
Throws:
`IllegalStateException` - if this folder is not opened
`MessagingException` - for other failures

    - 

#### setFlags

```
public void setFlags(Message[] msgs,
                     Flags flag,
                     boolean value)
              throws MessagingException
```

Set the specified flags on the messages specified in the array.
 This will result in appropriate MessageChangedEvents being
 delivered to any MessageChangedListener registered on this
 Message's containing folder. 

 Note that the specified Message objects **must** 
 belong to this folder. Certain Folder implementations can
 optimize the operation of setting Flags for a group of messages,
 so clients might want to use this method, rather than invoking
 `Message.setFlags` for each Message. 

 This implementation degenerates to invoking `setFlags()`
 on each Message object. Specific Folder implementations that can 
 optimize this case should do so. 
 Also, an implementation must not abort the operation if a Message 
 in the array turns out to be an expunged Message.

Parameters:
`msgs` - the array of message objects
`flag` - Flags object containing the flags to be set
`value` - set the flags to this boolean value
Throws:
`IllegalStateException` - if this folder is not opened
                        or if it has been opened READ_ONLY.
`MessagingException` - for other failures
See Also:
`Message.setFlags(javax.mail.Flags, boolean)`, 
`MessageChangedEvent`

    - 

#### setFlags

```
public void setFlags(int start,
                     int end,
                     Flags flag,
                     boolean value)
              throws MessagingException
```

Set the specified flags on the messages numbered from start
 through end, both start and end inclusive. Note that message 
 numbers start at 1, not 0.
 This will result in appropriate MessageChangedEvents being
 delivered to any MessageChangedListener registered on this
 Message's containing folder. 

 Certain Folder implementations can
 optimize the operation of setting Flags for a group of messages,
 so clients might want to use this method, rather than invoking
 `Message.setFlags` for each Message. 

 The default implementation uses `getMessage(int)` to
 get each `Message` object and then invokes
 `setFlags` on that object to set the flags.
 Specific Folder implementations that can optimize this case should do so.
 Also, an implementation must not abort the operation if a message 
 number refers to an expunged message.

Parameters:
`start` - the number of the first message
`end` - the number of the last message
`flag` - Flags object containing the flags to be set
`value` - set the flags to this boolean value
Throws:
`IllegalStateException` - if this folder is not opened
                        or if it has been opened READ_ONLY.
`IndexOutOfBoundsException` - if the start or end
                        message numbers are out of range.
`MessagingException` - for other failures
See Also:
`Message.setFlags(javax.mail.Flags, boolean)`, 
`MessageChangedEvent`

    - 

#### setFlags

```
public void setFlags(int[] msgnums,
                     Flags flag,
                     boolean value)
              throws MessagingException
```

Set the specified flags on the messages whose message numbers
 are in the array.
 This will result in appropriate MessageChangedEvents being
 delivered to any MessageChangedListener registered on this
 Message's containing folder. 

 Certain Folder implementations can
 optimize the operation of setting Flags for a group of messages,
 so clients might want to use this method, rather than invoking
 `Message.setFlags` for each Message. 

 The default implementation uses `getMessage(int)` to
 get each `Message` object and then invokes
 `setFlags` on that object to set the flags.
 Specific Folder implementations that can optimize this case should do so.
 Also, an implementation must not abort the operation if a message 
 number refers to an expunged message.

Parameters:
`msgnums` - the array of message numbers
`flag` - Flags object containing the flags to be set
`value` - set the flags to this boolean value
Throws:
`IllegalStateException` - if this folder is not opened
                        or if it has been opened READ_ONLY.
`IndexOutOfBoundsException` - if any message number
                        in the given array is out of range.
`MessagingException` - for other failures
See Also:
`Message.setFlags(javax.mail.Flags, boolean)`, 
`MessageChangedEvent`

    - 

#### copyMessages

```
public void copyMessages(Message[] msgs,
                         Folder folder)
                  throws MessagingException
```

Copy the specified Messages from this Folder into another 
 Folder. This operation appends these Messages to the 
 destination Folder. The destination Folder does not have to 
 be opened.  An appropriate MessageCountEvent 
 is delivered to any MessageCountListener registered on the 
 destination folder when the messages arrive in the folder. 

 Note that the specified Message objects **must** 
 belong to this folder. Folder implementations might be able
 to optimize this method by doing server-side copies. 

 This implementation just invokes `appendMessages()`
 on the destination folder to append the given Messages. Specific
 folder implementations that support server-side copies should
 do so, if the destination folder's Store is the same as this
 folder's Store. 
 Also, an implementation must not abort the operation if a 
 Message in the array turns out to be an expunged Message.

Parameters:
`msgs` - the array of message objects
`folder` - the folder to copy the messages to
Throws:
`FolderNotFoundException` - if the destination
                        folder does not exist.
`IllegalStateException` - if this folder is not opened.
`MessagingException` - for other failures
See Also:
`appendMessages(javax.mail.Message[])`

    - 

#### expunge

```
public abstract Message[] expunge()
                           throws MessagingException
```

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

Returns:
array of expunged Message objects
Throws:
`FolderNotFoundException` - if this folder does not
                        exist
`IllegalStateException` - if this folder is not opened.
`MessagingException` - for other failures
See Also:
`Message.isExpunged()`, 
`MessageCountEvent`

    - 

#### search

```
public Message[] search(SearchTerm term)
                 throws MessagingException
```

Search this Folder for messages matching the specified
 search criterion. Returns an array containing the matching
 messages . Returns an empty array if no matches were found. 

 This implementation invokes 
 `search(term, getMessages())`, to apply the search 
 over all the messages in this folder. Providers that can implement
 server-side searching might want to override this method to provide
 a more efficient implementation.

Parameters:
`term` - the search criterion
Returns:
array of matching messages
Throws:
`SearchException` - if the search 
                        term is too complex for the implementation to handle.
`FolderNotFoundException` - if this folder does 
                        not exist.
`IllegalStateException` - if this folder is not opened.
`MessagingException` - for other failures
See Also:
`SearchTerm`

    - 

#### search

```
public Message[] search(SearchTerm term,
                        Message[] msgs)
                 throws MessagingException
```

Search the given array of messages for those that match the 
 specified search criterion. Returns an array containing the 
 matching messages. Returns an empty array if no matches were 
 found. 

 Note that the specified Message objects **must** 
 belong to this folder. 

 This implementation iterates through the given array of messages,
 and applies the search criterion on each message by calling
 its `match()` method with the given term. The
 messages that succeed in the match are returned. Providers
 that can implement server-side searching might want to override
 this method to provide a more efficient implementation. If the
 search term is too complex or contains user-defined terms that
 cannot be executed on the server, providers may elect to either
 throw a SearchException or degenerate to client-side searching by
 calling `super.search()` to invoke this implementation.

Parameters:
`term` - the search criterion
`msgs` - the messages to be searched
Returns:
array of matching messages
Throws:
`SearchException` - if the search 
                        term is too complex for the implementation to handle.
`IllegalStateException` - if this folder is not opened
`MessagingException` - for other failures
See Also:
`SearchTerm`

    - 

#### addConnectionListener

```
public void addConnectionListener(ConnectionListener l)
```

Add a listener for Connection events on this Folder. 

 The implementation provided here adds this listener
 to an internal list of ConnectionListeners.

Parameters:
`l` - the Listener for Connection events
See Also:
`ConnectionEvent`

    - 

#### removeConnectionListener

```
public void removeConnectionListener(ConnectionListener l)
```

Remove a Connection event listener. 

 The implementation provided here removes this listener
 from the internal list of ConnectionListeners.

Parameters:
`l` - the listener
See Also:
`addConnectionListener(javax.mail.event.ConnectionListener)`

    - 

#### notifyConnectionListeners

```
protected void notifyConnectionListeners(int type)
```

Notify all ConnectionListeners. Folder implementations are
 expected to use this method to broadcast connection events. 

 The provided implementation queues the event into
 an internal event queue. An event dispatcher thread dequeues
 events from the queue and dispatches them to the registered
 ConnectionListeners. Note that the event dispatching occurs
 in a separate thread, thus avoiding potential deadlock problems.

Parameters:
`type` - the ConnectionEvent type
See Also:
`ConnectionEvent`

    - 

#### addFolderListener

```
public void addFolderListener(FolderListener l)
```

Add a listener for Folder events on this Folder. 

 The implementation provided here adds this listener
 to an internal list of FolderListeners.

Parameters:
`l` - the Listener for Folder events
See Also:
`FolderEvent`

    - 

#### removeFolderListener

```
public void removeFolderListener(FolderListener l)
```

Remove a Folder event listener. 

 The implementation provided here removes this listener
 from the internal list of FolderListeners.

Parameters:
`l` - the listener
See Also:
`addFolderListener(javax.mail.event.FolderListener)`

    - 

#### notifyFolderListeners

```
protected void notifyFolderListeners(int type)
```

Notify all FolderListeners registered on this Folder and
 this folder's Store. Folder implementations are expected
 to use this method to broadcast Folder events. 

 The implementation provided here queues the event into
 an internal event queue. An event dispatcher thread dequeues
 events from the queue and dispatches them to the 
 FolderListeners registered on this folder. The implementation
 also invokes `notifyFolderListeners` on this folder's
 Store to notify any FolderListeners registered on the store.

Parameters:
`type` - type of FolderEvent
See Also:
`notifyFolderRenamedListeners(javax.mail.Folder)`

    - 

#### notifyFolderRenamedListeners

```
protected void notifyFolderRenamedListeners(Folder folder)
```

Notify all FolderListeners registered on this Folder and
 this folder's Store about the renaming of this folder.
 Folder implementations are expected to use this method to
 broadcast Folder events indicating the renaming of folders. 

 The implementation provided here queues the event into
 an internal event queue. An event dispatcher thread dequeues
 events from the queue and dispatches them to the 
 FolderListeners registered on this folder. The implementation
 also invokes `notifyFolderRenamedListeners` on this 
 folder's Store to notify any FolderListeners registered on the store.

Parameters:
`folder` - Folder representing the new name.
Since:
JavaMail 1.1
See Also:
`notifyFolderListeners(int)`

    - 

#### addMessageCountListener

```
public void addMessageCountListener(MessageCountListener l)
```

Add a listener for MessageCount events on this Folder. 

 The implementation provided here adds this listener
 to an internal list of MessageCountListeners.

Parameters:
`l` - the Listener for MessageCount events
See Also:
`MessageCountEvent`

    - 

#### removeMessageCountListener

```
public void removeMessageCountListener(MessageCountListener l)
```

Remove a MessageCount listener. 

 The implementation provided here removes this listener
 from the internal list of MessageCountListeners.

Parameters:
`l` - the listener
See Also:
`addMessageCountListener(javax.mail.event.MessageCountListener)`

    - 

#### notifyMessageAddedListeners

```
protected void notifyMessageAddedListeners(Message[] msgs)
```

Notify all MessageCountListeners about the addition of messages
 into this folder. Folder implementations are expected to use this 
 method to broadcast MessageCount events for indicating arrival of
 new messages. 

 The provided implementation queues the event into
 an internal event queue. An event dispatcher thread dequeues
 events from the queue and dispatches them to the registered
 MessageCountListeners. Note that the event dispatching occurs
 in a separate thread, thus avoiding potential deadlock problems.

Parameters:
`msgs` - the messages that were added

    - 

#### notifyMessageRemovedListeners

```
protected void notifyMessageRemovedListeners(boolean removed,
                                             Message[] msgs)
```

Notify all MessageCountListeners about the removal of messages
 from this Folder. Folder implementations are expected to use this 
 method to broadcast MessageCount events indicating removal of
 messages. 

 The provided implementation queues the event into
 an internal event queue. An event dispatcher thread dequeues
 events from the queue and dispatches them to the registered
 MessageCountListeners. Note that the event dispatching occurs
 in a separate thread, thus avoiding potential deadlock problems.

Parameters:
`removed` - was the message removed by this client?
`msgs` - the messages that were removed

    - 

#### addMessageChangedListener

```
public void addMessageChangedListener(MessageChangedListener l)
```

Add a listener for MessageChanged events on this Folder. 

 The implementation provided here adds this listener
 to an internal list of MessageChangedListeners.

Parameters:
`l` - the Listener for MessageChanged events
See Also:
`MessageChangedEvent`

    - 

#### removeMessageChangedListener

```
public void removeMessageChangedListener(MessageChangedListener l)
```

Remove a MessageChanged listener. 

 The implementation provided here removes this listener
 from the internal list of MessageChangedListeners.

Parameters:
`l` - the listener
See Also:
`addMessageChangedListener(javax.mail.event.MessageChangedListener)`

    - 

#### notifyMessageChangedListeners

```
protected void notifyMessageChangedListeners(int type,
                                             Message msg)
```

Notify all MessageChangedListeners. Folder implementations are
 expected to use this method to broadcast MessageChanged events. 

 The provided implementation queues the event into
 an internal event queue. An event dispatcher thread dequeues
 events from the queue and dispatches them to registered
 MessageChangedListeners. Note that the event dispatching occurs
 in a separate thread, thus avoiding potential deadlock problems.

Parameters:
`type` - the MessageChangedEvent type
`msg` - the message that changed

    - 

#### finalize

```
protected void finalize()
                 throws Throwable
```

Overrides:
`finalize` in class `Object`
Throws:
`Throwable`

    - 

#### toString

```
public String toString()
```

override the default toString(), it will return the String
 from Folder.getFullName() or if that is null, it will use
 the default toString() behavior.

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