# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage.md.txt

# ListProviderConfigsPage

public class **ListProviderConfigsPage** extends Object  
implements Page\<ResourceT\>  
Represents a page of [ProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig) instances.

Provides methods for iterating over the provider configs in the current page, and calling up
subsequent pages of provider configs.

Instances of this class are thread-safe and immutable.  

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<T\> | [getNextPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage#getNextPage())() Returns the next page of provider configs.                                                                                                           |
| String                                                                                                                                           | [getNextPageToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage#getNextPageToken())() Returns the string token that identifies the next page.                                                                                    |
| Iterable\<T\>                                                                                                                                    | [getValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage#getValues())() Returns an `Iterable` over the provider configs in this page.                                                                                            |
| boolean                                                                                                                                          | [hasNextPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage#hasNextPage())() Checks if there is another page of provider configs available to retrieve.                                                                           |
| Iterable\<T\>                                                                                                                                    | [iterateAll](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage#iterateAll())() Returns an `Iterable` that facilitates transparently iterating over all the provider configs in the current Firebase project, starting from this page. |

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

#### public [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage)\<T\>
**getNextPage**
()

Returns the next page of provider configs.  

##### Returns

- A new [ListProviderConfigsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ListProviderConfigsPage) instance, or null if there are no more pages.  

#### public String
**getNextPageToken**
()

Returns the string token that identifies the next page.

Never returns null. Returns empty string if there are no more pages available to be
retrieved.  

##### Returns

- A non-null string token (possibly empty, representing no more pages)  

#### public Iterable\<T\>
**getValues**
()

Returns an `Iterable` over the provider configs in this page.  

##### Returns

- a `Iterable` instance.  

#### public boolean
**hasNextPage**
()

Checks if there is another page of provider configs available to retrieve.  

##### Returns

- true if another page is available, or false otherwise.  

#### public Iterable\<T\>
**iterateAll**
()

Returns an `Iterable` that facilitates transparently iterating over all the provider
configs in the current Firebase project, starting from this page.

The `Iterator` instances produced by the returned `Iterable` never buffers more
than one page of provider configs at a time. It is safe to abandon the iterators (i.e. break
the loops) at any time.  

##### Returns

- a new `Iterable` instance.