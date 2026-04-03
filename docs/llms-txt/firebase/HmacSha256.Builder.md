# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha256.Builder.md.txt

# HmacSha256.Builder

public static class **HmacSha256.Builder** extends Object  

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [HmacSha256](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha256) | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha256.Builder#build())()                                                                      |
| T extends Builder                                                                                                      | [setKey](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha256.Builder#setKey(byte[]))(byte\[\] key) Sets the signer key for the HMAC hash algorithm. |

### Protected Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [HmacSha256.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha256.Builder) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha256.Builder#getInstance())() |

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

#### public [HmacSha256](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha256)
**build**
()

<br />

#### public T extends Builder
**setKey**
(byte\[\] key)

Sets the signer key for the HMAC hash algorithm. Required field.  

##### Parameters

| key | Signer key as a byte array. |
|-----|-----------------------------|

##### Returns

- This builder.

## Protected Methods

#### protected [HmacSha256.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacSha256.Builder)
**getInstance**
()

<br />