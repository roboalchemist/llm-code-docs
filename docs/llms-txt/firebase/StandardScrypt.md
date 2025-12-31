# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/StandardScrypt.md.txt

# StandardScrypt

public final class **StandardScrypt** extends [UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash)  
Represents the Standard Scrypt password hashing algorithm. Can be used as an instance of
[UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash) when importing users.  

### Nested Class Summary

|-------|---|---|---|
| class | [StandardScrypt.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/StandardScrypt.Builder) ||   |

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| static [StandardScrypt.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/StandardScrypt.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/StandardScrypt#builder())() |

### Protected Method Summary

|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Map\<String, Object\> | [getOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/StandardScrypt#getOptions())() |

### Inherited Method Summary

From class [com.google.firebase.auth.UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash)  

|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| abstract Map\<String, Object\> | [getOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash#getOptions())() |

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

#### public static [StandardScrypt.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/StandardScrypt.Builder)
**builder**
()

<br />

## Protected Methods

#### protected Map\<String, Object\>
**getOptions**
()

<br />