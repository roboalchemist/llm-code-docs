# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacMd5.Builder.md.txt

# HmacMd5.Builder

public static class **HmacMd5.Builder** extends Object  

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [HmacMd5](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacMd5) | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacMd5.Builder#build())()                                                                      |
| T extends Builder                                                                                                | [setKey](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacMd5.Builder#setKey(byte[]))(byte\[\] key) Sets the signer key for the HMAC hash algorithm. |

### Protected Method Summary

|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [HmacMd5.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacMd5.Builder) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacMd5.Builder#getInstance())() |

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

#### public [HmacMd5](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacMd5)
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

#### protected [HmacMd5.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/HmacMd5.Builder)
**getInstance**
()

<br />