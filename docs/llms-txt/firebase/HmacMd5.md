# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacMd5.md.txt

# HmacMd5

public final class **HmacMd5** extends [UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash)  
Represents the HMAC MD5 password hashing algorithm. Can be used as an instance of
[UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash) when importing users.  

### Nested Class Summary

|-------|---|---|---|
| class | [HmacMd5.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacMd5.Builder) ||   |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| static [HmacMd5.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacMd5.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacMd5#builder())() |

### Protected Method Summary

|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| final Map\<String, Object\> | [getOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacMd5#getOptions())() |

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

#### public static [HmacMd5.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacMd5.Builder)
**builder**
()

<br />

## Protected Methods

#### protected final Map\<String, Object\>
**getOptions**
()

<br />