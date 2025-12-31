# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions.Builder.md.txt

# UserImportOptions.Builder

public static class **UserImportOptions.Builder** extends Object  

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions.Builder#build())() Builds a new [UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions).                                                                            |
| [UserImportOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions.Builder) | [setHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions.Builder#setHash(com.google.firebase.auth.UserImportHash))([UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash) hash) Sets the algorithm used to hash user passwords. |

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

#### public [UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions)
**build**
()

Builds a new [UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions).  

##### Returns

- A non-null [UserImportOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions).  

#### public [UserImportOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions.Builder)
**setHash**
([UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash) hash)

Sets the algorithm used to hash user passwords. This is required
when at least one of the [ImportUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord) instances being imported has a password
hash. See [setPasswordHash(byte[])](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder#setPasswordHash(byte[])).  

##### Parameters

| hash | A [UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash). |
|------|------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.