# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/GetUsersResult.md.txt

# GetUsersResult

public final class **GetUsersResult** extends Object  
Represents the result of the [getUsersAsync(Collection)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getUsersAsync(java.util.Collection<com.google.firebase.auth.UserIdentifier>)) API.  

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Set\<[UserIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserIdentifier)\> | [getNotFound](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/GetUsersResult#getNotFound())() Set of identifiers that were requested, but not found.               |
| Set\<[UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)\>         | [getUsers](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/GetUsersResult#getUsers())() Set of user records corresponding to the set of users that were requested. |

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

#### public Set\<[UserIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserIdentifier)\>
**getNotFound**
()

Set of identifiers that were requested, but not found.  

#### public Set\<[UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)\>
**getUsers**
()

Set of user records corresponding to the set of users that were requested. Only users
that were found are listed here. The result set is unordered.