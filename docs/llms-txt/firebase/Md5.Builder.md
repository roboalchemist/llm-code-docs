# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Md5.Builder.md.txt

# Md5.Builder

public static class **Md5.Builder** extends Object  

### Public Method Summary

|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Md5](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Md5) | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Md5.Builder#build())()                                                                        |
| T extends Builder                                                                                        | [setRounds](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Md5.Builder#setRounds(int))(int rounds) Sets the number of rounds for the hash algorithm. |

### Protected Method Summary

|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [Md5.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Md5.Builder) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Md5.Builder#getInstance())() |

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

#### public [Md5](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Md5)
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

#### protected [Md5.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/hash/Md5.Builder)
**getInstance**
()

<br />