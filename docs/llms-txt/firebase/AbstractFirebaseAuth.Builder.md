# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth.Builder.md.txt

# AbstractFirebaseAuth.Builder

protected static abstract class **AbstractFirebaseAuth.Builder** extends Object  

### Protected Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------|
|   | [Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth.Builder#Builder())() |

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) | [getFirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth.Builder#getFirebaseApp())()                                                                                                                                                             |
| T                                                                                                              | [setCookieVerifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth.Builder#setCookieVerifier(com.google.common.base.Supplier<? extends com.google.firebase.auth.FirebaseTokenVerifier>))(Supplier\<? extends FirebaseTokenVerifier\> cookieVerifier)    |
| T                                                                                                              | [setFirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth.Builder#setFirebaseApp(com.google.firebase.FirebaseApp))([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) firebaseApp)    |
| T                                                                                                              | [setIdTokenVerifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth.Builder#setIdTokenVerifier(com.google.common.base.Supplier<? extends com.google.firebase.auth.FirebaseTokenVerifier>))(Supplier\<? extends FirebaseTokenVerifier\> idTokenVerifier) |

### Protected Method Summary

|------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| abstract T | [getThis](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth.Builder#getThis())() |

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
**Builder**
()

<br />

## Public Methods

#### public [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp)
**getFirebaseApp**
()

<br />

#### public T
**setCookieVerifier**
(Supplier\<? extends FirebaseTokenVerifier\> cookieVerifier)

<br />

#### public T
**setFirebaseApp**
([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) firebaseApp)

<br />

#### public T
**setIdTokenVerifier**
(Supplier\<? extends FirebaseTokenVerifier\> idTokenVerifier)

<br />

## Protected Methods

#### protected abstract T
**getThis**
()

<br />