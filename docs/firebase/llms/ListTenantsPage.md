# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage.md.txt

# ListTenantsPage

public class **ListTenantsPage** extends Object  
implements Page\<ResourceT\>  
Represents a page of [Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant) instances.

Provides methods for iterating over the tenants in the current page, and calling up
subsequent pages of tenants.

Instances of this class are thread-safe and immutable.  

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ListTenantsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage) | [getNextPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage#getNextPage())() Returns the next page of tenants.                                                                                                           |
| String                                                                                                                                   | [getNextPageToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage#getNextPageToken())() Returns the string token that identifies the next page.                                                                           |
| Iterable\<[Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant)\>       | [getValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage#getValues())() Returns an `Iterable` over the tenants in this page.                                                                                            |
| boolean                                                                                                                                  | [hasNextPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage#hasNextPage())() Checks if there is another page of tenants available to retrieve.                                                                           |
| Iterable\<[Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant)\>       | [iterateAll](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage#iterateAll())() Returns an `Iterable` that facilitates transparently iterating over all the tenants in the current Firebase project, starting from this page. |

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

#### public [ListTenantsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage)
**getNextPage**
()

Returns the next page of tenants.  

##### Returns

- A new [ListTenantsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage) instance, or null if there are no more pages.  

#### public String
**getNextPageToken**
()

Returns the string token that identifies the next page.

Never returns null. Returns empty string if there are no more pages available to be
retrieved.  

##### Returns

- A non-null string token (possibly empty, representing no more pages)  

#### public Iterable\<[Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant)\>
**getValues**
()

Returns an `Iterable` over the tenants in this page.  

##### Returns

- a `Iterable` instance.  

#### public boolean
**hasNextPage**
()

Checks if there is another page of tenants available to retrieve.  

##### Returns

- true if another page is available, or false otherwise.  

#### public Iterable\<[Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant)\>
**iterateAll**
()

Returns an `Iterable` that facilitates transparently iterating over all the tenants in
the current Firebase project, starting from this page.

The `Iterator` instances produced by the returned `Iterable` never buffers more
than one page of tenants at a time. It is safe to abandon the iterators (i.e. break the loops)
at any time.  

##### Returns

- a new `Iterable` instance.