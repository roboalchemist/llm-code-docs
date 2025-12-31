# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportResult.md.txt

# UserImportResult

public final class **UserImportResult** extends Object  
Represents the result of the [importUsersAsync(List, UserImportOptions)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsersAsync(java.util.List<com.google.firebase.auth.ImportUserRecord>, com.google.firebase.auth.UserImportOptions)) API.  

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| List\<[ErrorInfo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ErrorInfo)\> | [getErrors](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportResult#getErrors())() A list of [ErrorInfo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ErrorInfo) instances describing the errors that were encountered during the import. |
| int                                                                                                                     | [getFailureCount](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportResult#getFailureCount())() Returns the number of users that failed to be imported.                                                                                                                                |
| int                                                                                                                     | [getSuccessCount](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportResult#getSuccessCount())() Returns the number of users that were imported successfully.                                                                                                                           |

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
the import. Length of this list is equal to the return value of [getFailureCount()](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportResult#getFailureCount()).  

##### Returns

- A non-null list (possibly empty).  

#### public int
**getFailureCount**
()

Returns the number of users that failed to be imported.  

##### Returns

- number of users that resulted in import failures (possibly zero).  

#### public int
**getSuccessCount**
()

Returns the number of users that were imported successfully.  

##### Returns

- number of users successfully imported (possibly zero).