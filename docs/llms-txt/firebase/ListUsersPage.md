# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage.md.txt

# ListUsersPage

public class **ListUsersPage** extends Object  
implements Page\<ResourceT\>  
Represents a page of [ExportedUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ExportedUserRecord) instances. Provides methods for iterating
over the users in the current page, and calling up subsequent pages of users. Instances of
this class are thread-safe and immutable.  

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ListUsersPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage)                       | [getNextPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage#getNextPage())() Returns the next page of users.                                                                                                           |
| String                                                                                                                                        | [getNextPageToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage#getNextPageToken())() Returns the string token that identifies the next page.                                                                         |
| Iterable\<[ExportedUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ExportedUserRecord)\> | [getValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage#getValues())() Returns an `Iterable` over the users in this page.                                                                                            |
| boolean                                                                                                                                       | [hasNextPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage#hasNextPage())() Checks if there is another page of users available to retrieve.                                                                           |
| Iterable\<[ExportedUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ExportedUserRecord)\> | [iterateAll](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage#iterateAll())() Returns an `Iterable` that facilitates transparently iterating over all the users in the current Firebase project, starting from this page. |

### Inherited Method Summary

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

From interface com.google.api.gax.paging.Page  

|--------------------------------|--------------------|
| abstract Page\<ResourceT\>     | getNextPage()      |
| abstract String                | getNextPageToken() |
| abstract Iterable\<ResourceT\> | getValues()        |
| abstract boolean               | hasNextPage()      |
| abstract Iterable\<ResourceT\> | iterateAll()       |
| abstract Stream\<ResourceT\>   | streamAll()        |
| abstract Stream\<ResourceT\>   | streamValues()     |

## Public Methods

#### public [ListUsersPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage)
**getNextPage**
()

Returns the next page of users.  

##### Returns

- A new [ListUsersPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListUsersPage) instance, or null if there are no more pages.  

#### public String
**getNextPageToken**
()

Returns the string token that identifies the next page. Never returns null. Returns empty
string if there are no more pages available to be retrieved.  

##### Returns

- A non-null string token (possibly empty, representing no more pages)  

#### public Iterable\<[ExportedUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ExportedUserRecord)\>
**getValues**
()

Returns an `Iterable` over the users in this page.  

##### Returns

- a `Iterable<ExportedUserRecord>` instance.  

#### public boolean
**hasNextPage**
()

Checks if there is another page of users available to retrieve.  

##### Returns

- true if another page is available, or false otherwise.  

#### public Iterable\<[ExportedUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ExportedUserRecord)\>
**iterateAll**
()

Returns an `Iterable` that facilitates transparently iterating over all the users in the
current Firebase project, starting from this page. The `Iterator` instances produced
by the returned `Iterable` never buffers more than one page of users at a time. It is
safe to abandon the iterators (i.e. break the loops) at any time.  

##### Returns

- a new `Iterable<ExportedUserRecord>` instance.