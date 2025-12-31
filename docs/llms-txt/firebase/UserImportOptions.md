# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions.md.txt

# UserImportOptions

public final class **UserImportOptions** extends Object  
A collection of options that can be passed to the
[importUsersAsync(List, UserImportOptions)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsersAsync(java.util.List<com.google.firebase.auth.ImportUserRecord>, com.google.firebase.auth.UserImportOptions)) API.  

### Nested Class Summary

|-------|---|---|---|
| class | [UserImportOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions.Builder) ||   |

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [UserImportOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions#builder())() Creates a new [UserImportOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions.Builder).                                                                                                                                                                                               |
| static [UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions)                 | [withHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions#withHash(com.google.firebase.auth.UserImportHash))([UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash) hash) Creates a new [UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions) containing the provided hash algorithm. |

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

#### public static [UserImportOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions.Builder)
**builder**
()

Creates a new [UserImportOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions.Builder).  

##### Returns

- A [UserImportOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions.Builder) instance.  

#### public static [UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions)
**withHash**
([UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash) hash)

Creates a new [UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions) containing the provided hash algorithm.  

##### Parameters

| hash | A non-null [UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash). |
|------|---------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A new [UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions).