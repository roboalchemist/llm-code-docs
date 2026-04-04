# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/PbkdfSha1.Builder.md.txt

# PbkdfSha1.Builder

public static class **PbkdfSha1.Builder** extends Object  

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PbkdfSha1](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/PbkdfSha1) | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/PbkdfSha1.Builder#build())()                                                                        |
| T extends Builder                                                                                                    | [setRounds](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/PbkdfSha1.Builder#setRounds(int))(int rounds) Sets the number of rounds for the hash algorithm. |

### Protected Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [PbkdfSha1.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/PbkdfSha1.Builder) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/PbkdfSha1.Builder#getInstance())() |

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

#### public [PbkdfSha1](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/PbkdfSha1)
**build**
()

<br />

#### public T extends Builder
**setRounds**
(int rounds)

Sets the number of rounds for the hash algorithm.  

##### Parameters

| rounds | an integer between 0 and 120000 (inclusive). |
|--------|----------------------------------------------|

##### Returns

- this builder.

## Protected Methods

#### protected [PbkdfSha1.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/PbkdfSha1.Builder)
**getInstance**
()

<br />