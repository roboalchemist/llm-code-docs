# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder.md.txt

# Scrypt.Builder

public static class **Scrypt.Builder** extends Object  

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Scrypt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder#build())()                                                                            |
| [Scrypt.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder) | [setKey](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder#setKey(byte[]))(byte\[\] key) Sets the signer key.                                   |
| [Scrypt.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder) | [setMemoryCost](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder#setMemoryCost(int))(int memoryCost) Sets the memory cost.                     |
| T extends Builder                                                                                                              | [setRounds](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder#setRounds(int))(int rounds) Sets the number of rounds for the hash algorithm.     |
| [Scrypt.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder) | [setSaltSeparator](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder#setSaltSeparator(byte[]))(byte\[\] saltSeparator) Sets the salt separator. |

### Protected Method Summary

|--------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [Scrypt.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder#getInstance())() |

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

#### public [Scrypt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt)
**build**
()

<br />

#### public [Scrypt.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder)
**setKey**
(byte\[\] key)

Sets the signer key. Required field.  

##### Parameters

| key | Signer key as a byte array. |
|-----|-----------------------------|

##### Returns

- This builder.  

#### public [Scrypt.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder)
**setMemoryCost**
(int memoryCost)

Sets the memory cost. Required field.  

##### Parameters

| memoryCost | an integer between 1 and 14 (inclusive). |
|------------|------------------------------------------|

##### Returns

- this builder.  

#### public T extends Builder
**setRounds**
(int rounds)

Sets the number of rounds for the hash algorithm.  

##### Parameters

| rounds | an integer between 0 and 120000 (inclusive). |
|--------|----------------------------------------------|

##### Returns

- this builder.  

#### public [Scrypt.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder)
**setSaltSeparator**
(byte\[\] saltSeparator)

Sets the salt separator.  

##### Parameters

| saltSeparator | Salt separator as a byte array. |
|---------------|---------------------------------|

##### Returns

- This builder.

## Protected Methods

#### protected [Scrypt.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Scrypt.Builder)
**getInstance**
()

<br />