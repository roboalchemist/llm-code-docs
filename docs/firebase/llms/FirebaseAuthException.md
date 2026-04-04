# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException.md.txt

# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException.md.txt

# FirebaseAuthException

public class **FirebaseAuthException** extends [FirebaseException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseException)  
Generic exception related to Firebase Authentication. Check the error code and message for more
details.  

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException#FirebaseAuthException(com.google.firebase.ErrorCode, java.lang.String, java.lang.Throwable, com.google.firebase.IncomingHttpResponse, com.google.firebase.auth.AuthErrorCode))([ErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ErrorCode) errorCode, String message, Throwable cause, [IncomingHttpResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/IncomingHttpResponse) response, [AuthErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AuthErrorCode) authErrorCode) |
|   | [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException#FirebaseAuthException(com.google.firebase.FirebaseException))([FirebaseException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseException) base)                                                                                                                                                                                                                                                                                                                                                                                                                          |

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AuthErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AuthErrorCode) | [getAuthErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException#getAuthErrorCode())() |

### Inherited Method Summary

From class [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseException)  

|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| final [ErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ErrorCode)                       | [getErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseException#getErrorCode())() Returns the platform-wide error code associated with this exception. |
| final [IncomingHttpResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/IncomingHttpResponse) | [getHttpResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseException#getHttpResponse())() Returns the HTTP response that resulted in this exception.     |

From class java.lang.Throwable  

|----------------------------------|-------------------------------------------|
| synchronized final void          | addSuppressed(Throwable arg0)             |
| synchronized Throwable           | fillInStackTrace()                        |
| synchronized Throwable           | getCause()                                |
| String                           | getLocalizedMessage()                     |
| String                           | getMessage()                              |
| StackTraceElement\[\]            | getStackTrace()                           |
| synchronized final Throwable\[\] | getSuppressed()                           |
| synchronized Throwable           | initCause(Throwable arg0)                 |
| void                             | printStackTrace()                         |
| void                             | printStackTrace(PrintWriter arg0)         |
| void                             | printStackTrace(PrintStream arg0)         |
| void                             | setStackTrace(StackTraceElement\[\] arg0) |
| String                           | toString()                                |

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

## Public Constructors

#### public
**FirebaseAuthException**
([ErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ErrorCode) errorCode, String message, Throwable cause, [IncomingHttpResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/IncomingHttpResponse) response, [AuthErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AuthErrorCode) authErrorCode)

<br />

#### public
**FirebaseAuthException**
([FirebaseException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseException) base)

<br />

## Public Methods

#### public [AuthErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AuthErrorCode)
**getAuthErrorCode**
()

<br />