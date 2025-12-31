# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/DeleteUsersResult.md.txt

# DeleteUsersResult

public final class **DeleteUsersResult** extends Object  
Represents the result of the [deleteUsersAsync(List)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteUsersAsync(java.util.List<java.lang.String>)) API.  

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| List\<[ErrorInfo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ErrorInfo)\> | [getErrors](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/DeleteUsersResult#getErrors())() A list of [ErrorInfo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ErrorInfo) instances describing the errors that were encountered during the deletion. |
| int                                                                                                                     | [getFailureCount](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/DeleteUsersResult#getFailureCount())() Returns the number of users that failed to be deleted (possibly zero).                                                                                                                   |
| int                                                                                                                     | [getSuccessCount](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/DeleteUsersResult#getSuccessCount())() Returns the number of users that were deleted successfully (possibly zero).                                                                                                              |

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

## Public Methods

#### public List\<[ErrorInfo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ErrorInfo)\>
**getErrors**
()

A list of [ErrorInfo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ErrorInfo) instances describing the errors that were encountered during
the deletion. Length of this list is equal to the return value of
[getFailureCount()](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/DeleteUsersResult#getFailureCount()).  

##### Returns

- A non-null list (possibly empty).  

#### public int
**getFailureCount**
()

Returns the number of users that failed to be deleted (possibly zero).  

#### public int
**getSuccessCount**
()

Returns the number of users that were deleted successfully (possibly zero). Users that did not
exist prior to calling [deleteUsersAsync(List)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#deleteUsersAsync(java.util.List<java.lang.String>)) are considered to be
successfully deleted.