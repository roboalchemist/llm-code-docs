# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/PbkdfSha1.md.txt

# PbkdfSha1

public final class **PbkdfSha1** extends [UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash)  
Represents the PBKDF SHA1 password hashing algorithm. Can be used as an instance of
[UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash) when importing users.  

### Nested Class Summary

|-------|---|---|---|
| class | [PbkdfSha1.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/PbkdfSha1.Builder) ||   |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| static [PbkdfSha1.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/PbkdfSha1.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/PbkdfSha1#builder())() |

### Protected Method Summary

|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Map\<String, Object\> | [getOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/PbkdfSha1#getOptions())() |

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

#### public static [PbkdfSha1.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/PbkdfSha1.Builder)
**builder**
()

<br />

## Protected Methods

#### protected Map\<String, Object\>
**getOptions**
()

<br />