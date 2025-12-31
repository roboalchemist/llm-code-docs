# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha256.md.txt

# HmacSha256

public final class **HmacSha256** extends [UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash)  
Represents the HMAC SHA256 password hashing algorithm. Can be used as an instance of
[UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash) when importing users.  

### Nested Class Summary

|-------|---|---|---|
| class | [HmacSha256.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha256.Builder) ||   |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| static [HmacSha256.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha256.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha256#builder())() |

### Protected Method Summary

|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| final Map\<String, Object\> | [getOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha256#getOptions())() |

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

#### public static [HmacSha256.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha256.Builder)
**builder**
()

<br />

## Protected Methods

#### protected final Map\<String, Object\>
**getOptions**
()

<br />