# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Sha1.Builder.md.txt

# Sha1.Builder

public static class **Sha1.Builder** extends Object  

### Public Method Summary

|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Sha1](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Sha1) | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Sha1.Builder#build())()                                                                        |
| T extends Builder                                                                                          | [setRounds](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Sha1.Builder#setRounds(int))(int rounds) Sets the number of rounds for the hash algorithm. |

### Protected Method Summary

|----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [Sha1.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Sha1.Builder) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Sha1.Builder#getInstance())() |

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

#### public [Sha1](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Sha1)
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

#### protected [Sha1.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Sha1.Builder)
**getInstance**
()

<br />