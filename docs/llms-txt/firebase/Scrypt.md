# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.md.txt

# Scrypt

public final class **Scrypt** extends [UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash)  
Represents the Scrypt password hashing algorithm. This is the
[modified Scrypt algorithm](https://github.com/firebase/scrypt) used by
Firebase Auth. See [StandardScrypt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/StandardScrypt) for the standard Scrypt algorithm. Can be used as an
instance of [UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash) when importing users.  

### Nested Class Summary

|-------|---|---|---|
| class | [Scrypt.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder) ||   |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| static [Scrypt.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt#builder())() |

### Protected Method Summary

|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Map\<String, Object\> | [getOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt#getOptions())() |

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

#### public static [Scrypt.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder)
**builder**
()

<br />

## Protected Methods

#### protected Map\<String, Object\>
**getOptions**
()

<br />