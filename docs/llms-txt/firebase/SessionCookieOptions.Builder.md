# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SessionCookieOptions.Builder.md.txt

# SessionCookieOptions.Builder

public static class **SessionCookieOptions.Builder** extends Object  

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SessionCookieOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SessionCookieOptions)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SessionCookieOptions.Builder#build())() Creates a new [SessionCookieOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SessionCookieOptions) instance. |
| [SessionCookieOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SessionCookieOptions.Builder) | [setExpiresIn](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SessionCookieOptions.Builder#setExpiresIn(long))(long expiresInMillis) Sets the duration until the cookie is expired in milliseconds.                                                          |

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

#### public [SessionCookieOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SessionCookieOptions)
**build**
()

Creates a new [SessionCookieOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SessionCookieOptions) instance.  

#### public [SessionCookieOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SessionCookieOptions.Builder)
**setExpiresIn**
(long expiresInMillis)

Sets the duration until the cookie is expired in milliseconds. Must be between 5 minutes
and 14 days.  

##### Parameters

| expiresInMillis | Time duration in milliseconds. |
|-----------------|--------------------------------|

##### Returns

- This builder.