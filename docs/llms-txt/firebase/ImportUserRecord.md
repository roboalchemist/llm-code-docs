# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.md.txt

# ImportUserRecord

public final class **ImportUserRecord** extends Object  
Represents a user account to be imported to Firebase Auth via the
[importUsers(List, UserImportOptions)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsers(java.util.List<com.google.firebase.auth.ImportUserRecord>, com.google.firebase.auth.UserImportOptions)) API. Must contain at least a
uid string.  

### Nested Class Summary

|-------|---|---|---|
| class | [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) ||   |

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord#builder())() Creates a new [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder). |

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

#### public static [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder)
**builder**
()

Creates a new [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder).  

##### Returns

- A [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) instance.