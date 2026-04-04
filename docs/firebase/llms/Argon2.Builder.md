# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder.md.txt

# Argon2.Builder

public static class **Argon2.Builder** extends Object  

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Argon2](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder#build())()                                                                                                                                                                                                                                                         |
| [Argon2.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder) | [setAssociatedData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder#setAssociatedData(byte[]))(byte\[\] associatedData) Sets additional associated data, if provided, to append to the hash value for additional security.                                                                                                 |
| [Argon2.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder) | [setHashLengthBytes](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder#setHashLengthBytes(int))(int hashLengthBytes) Sets the hash length in bytes.                                                                                                                                                                          |
| [Argon2.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder) | [setHashType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder#setHashType(com.google.firebase.auth.hash.Argon2.Argon2HashType))([Argon2.Argon2HashType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Argon2HashType) hashType) Sets the Argon2 hash type.          |
| [Argon2.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder) | [setIterations](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder#setIterations(int))(int iterations) Sets the number of iterations to perform.                                                                                                                                                                              |
| [Argon2.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder) | [setMemoryCostKib](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder#setMemoryCostKib(int))(int memoryCostKib) Sets the memory cost in kibibytes.                                                                                                                                                                            |
| [Argon2.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder) | [setParallelism](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder#setParallelism(int))(int parallelism) Sets the degree of parallelism, also called threads or lanes.                                                                                                                                                       |
| [Argon2.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder) | [setVersion](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder#setVersion(com.google.firebase.auth.hash.Argon2.Argon2Version))([Argon2.Argon2Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Argon2Version) version) Sets the version of the Argon2 algorithm. |

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

#### public [Argon2](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2)
**build**
()

<br />

#### public [Argon2.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder)
**setAssociatedData**
(byte\[\] associatedData)

Sets additional associated data, if provided, to append to the hash value for additional
security. This data is base64 encoded before it is sent to the API.  

##### Parameters

| associatedData | Associated data as a byte array. |
|----------------|----------------------------------|

##### Returns

- This builder.  

#### public [Argon2.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder)
**setHashLengthBytes**
(int hashLengthBytes)

Sets the hash length in bytes. Required field.  

##### Parameters

| hashLengthBytes | an integer between 4 and 1024 (inclusive). |
|-----------------|--------------------------------------------|

##### Returns

- This builder.  

#### public [Argon2.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder)
**setHashType**
([Argon2.Argon2HashType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Argon2HashType) hashType)

Sets the Argon2 hash type. Required field.  

##### Parameters

| hashType | a value from the [Argon2.Argon2HashType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Argon2HashType) enum. |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [Argon2.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder)
**setIterations**
(int iterations)

Sets the number of iterations to perform. Required field.  

##### Parameters

| iterations | an integer between 1 and 16 (inclusive). |
|------------|------------------------------------------|

##### Returns

- This builder.  

#### public [Argon2.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder)
**setMemoryCostKib**
(int memoryCostKib)

Sets the memory cost in kibibytes. Required field.  

##### Parameters

| memoryCostKib | an integer between 1 and 32768 (inclusive). |
|---------------|---------------------------------------------|

##### Returns

- This builder.  

#### public [Argon2.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder)
**setParallelism**
(int parallelism)

Sets the degree of parallelism, also called threads or lanes. Required field.  

##### Parameters

| parallelism | an integer between 1 and 16 (inclusive). |
|-------------|------------------------------------------|

##### Returns

- This builder.  

#### public [Argon2.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Builder)
**setVersion**
([Argon2.Argon2Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Argon2Version) version)

Sets the version of the Argon2 algorithm.  

##### Parameters

| version | a value from the [Argon2.Argon2Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Argon2.Argon2Version) enum. |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.