# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash.md.txt

# UserImportHash

public abstract class **UserImportHash** extends Object  

|---|---|---|
| Known Direct Subclasses [Argon2](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2), [Bcrypt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Bcrypt), [HmacMd5](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacMd5), [HmacSha1](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha1), [HmacSha256](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha256), [HmacSha512](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha512), [Md5](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Md5), [Pbkdf2Sha256](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Pbkdf2Sha256), [PbkdfSha1](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/PbkdfSha1), [Scrypt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt), [Sha1](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Sha1), [Sha256](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Sha256), [Sha512](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Sha512), [StandardScrypt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/StandardScrypt) |--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------| | [Argon2](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2)                 | Represents the Argon2 password hashing algorithm.          | | [Bcrypt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Bcrypt)                 | Represents the Bcrypt password hashing algorithm.          | | [HmacMd5](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacMd5)               | Represents the HMAC MD5 password hashing algorithm.        | | [HmacSha1](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha1)             | Represents the HMAC SHA1 password hashing algorithm.       | | [HmacSha256](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha256)         | Represents the HMAC SHA256 password hashing algorithm.     | | [HmacSha512](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha512)         | Represents the HMAC SHA512 password hashing algorithm.     | | [Md5](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Md5)                       | Represents the MD5 password hashing algorithm.             | | [Pbkdf2Sha256](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Pbkdf2Sha256)     | Represents the PBKDF2 SHA256 password hashing algorithm.   | | [PbkdfSha1](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/PbkdfSha1)           | Represents the PBKDF SHA1 password hashing algorithm.      | | [Scrypt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt)                 | Represents the Scrypt password hashing algorithm.          | | [Sha1](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Sha1)                     | Represents the SHA1 password hashing algorithm.            | | [Sha256](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Sha256)                 | Represents the SHA256 password hashing algorithm.          | | [Sha512](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Sha512)                 | Represents the SHA512 password hashing algorithm.          | | [StandardScrypt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/StandardScrypt) | Represents the Standard Scrypt password hashing algorithm. | |||

Represents a hash algorithm and the related configuration parameters used to hash user
passwords. An instance of this class must be specified if importing any users with password
hashes (see [setHash(UserImportHash)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions.Builder#setHash(com.google.firebase.auth.UserImportHash)).

This is not expected to be extended in user code. Applications should use one of the provided
concrete implementations in the [com.google.firebase.auth.hash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/package-summary) package. See
[documentation](https://firebase.google.com/docs/auth/admin/import-users) for more
details on available options.  

### Protected Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash#UserImportHash(java.lang.String))(String name) |

### Protected Method Summary

|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| abstract Map\<String, Object\> | [getOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash#getOptions())() |

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

## Protected Constructors

#### protected
**UserImportHash**
(String name)

<br />

## Protected Methods

#### protected abstract Map\<String, Object\>
**getOptions**
()

<br />