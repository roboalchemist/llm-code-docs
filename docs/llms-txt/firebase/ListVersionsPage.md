# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage.md.txt

# ListVersionsPage

public final class **ListVersionsPage** extends Object  
implements Page\<ResourceT\>  
Represents a page of [Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version) instances. Provides methods for iterating
over the versions in the current page, and calling up subsequent pages of versions. Instances of
this class are thread-safe and immutable.  

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ListVersionsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage) | [getNextPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage#getNextPage())() Returns the next page of versions.                                                                                                           |
| String                                                                                                                                | [getNextPageToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage#getNextPageToken())() Returns the string token that identifies the next page.                                                                            |
| Iterable\<[Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version)\>       | [getValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage#getValues())() Returns an `Iterable` over the versions in this page.                                                                                            |
| boolean                                                                                                                               | [hasNextPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage#hasNextPage())() Checks if there is another page of versions available to retrieve.                                                                           |
| Iterable\<[Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version)\>       | [iterateAll](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage#iterateAll())() Returns an `Iterable` that facilitates transparently iterating over all the versions in the current Firebase project, starting from this page. |

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

#### public [ListVersionsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage)
**getNextPage**
()

Returns the next page of versions.  

##### Returns

- A new [ListVersionsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage) instance, or null if there are no more pages.  

#### public String
**getNextPageToken**
()

Returns the string token that identifies the next page. Never returns null. Returns an empty
string if there are no more pages available to be retrieved.  

##### Returns

- A non-null string token (possibly empty, representing no more pages)  

#### public Iterable\<[Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version)\>
**getValues**
()

Returns an `Iterable` over the versions in this page.  

##### Returns

- a `Iterable<Version>` instance.  

#### public boolean
**hasNextPage**
()

Checks if there is another page of versions available to retrieve.  

##### Returns

- true if another page is available, or false otherwise.  

#### public Iterable\<[Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version)\>
**iterateAll**
()

Returns an `Iterable` that facilitates transparently iterating over all the versions in
the current Firebase project, starting from this page. The `Iterator` instances produced
by the returned `Iterable` never buffers more than one page of versions at a time. It is
safe to abandon the iterators (i.e. break the loops) at any time.  

##### Returns

- a new `Iterable<Version>` instance.