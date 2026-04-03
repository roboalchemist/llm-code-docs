# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ErrorInfo.md.txt

# ErrorInfo

public final class **ErrorInfo** extends Object  
Represents an error encountered while importing an [ImportUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord).  

### Public Method Summary

|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int    | [getIndex](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ErrorInfo#getIndex())() The index of the failed user in the list passed to the [importUsersAsync(List, UserImportOptions)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsersAsync(java.util.List<com.google.firebase.auth.ImportUserRecord>, com.google.firebase.auth.UserImportOptions)) method. |
| String | [getReason](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ErrorInfo#getReason())() A string describing the error.                                                                                                                                                                                                                                                                                                                  |

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

#### public int
**getIndex**
()

The index of the failed user in the list passed to the
[importUsersAsync(List, UserImportOptions)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsersAsync(java.util.List<com.google.firebase.auth.ImportUserRecord>, com.google.firebase.auth.UserImportOptions)) method.  

##### Returns

- an integer index.  

#### public String
**getReason**
()

A string describing the error.  

##### Returns

- A string error message.