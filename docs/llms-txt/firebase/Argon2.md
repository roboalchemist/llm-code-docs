# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.md.txt

# Argon2

public final class **Argon2** extends [UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash)  
Represents the Argon2 password hashing algorithm. Can be used as an instance of [UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash) when importing users.  

### Nested Class Summary

|-------|---|---|---|
| enum  | [Argon2.Argon2HashType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Argon2HashType) ||   |
| enum  | [Argon2.Argon2Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Argon2Version) ||   |
| class | [Argon2.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder) ||   |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| static [Argon2.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2#builder())() |

### Protected Method Summary

|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Map\<String, Object\> | [getOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2#getOptions())() |

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

#### public static [Argon2.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder)
**builder**
()

<br />

## Protected Methods

#### protected Map\<String, Object\>
**getOptions**
()

<br />