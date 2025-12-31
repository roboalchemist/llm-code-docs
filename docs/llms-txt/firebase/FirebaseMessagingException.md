# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException.md.txt

# FirebaseMessagingException

public final class **FirebaseMessagingException** extends [FirebaseException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseException)  

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MessagingErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MessagingErrorCode) | [getMessagingErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException#getMessagingErrorCode())() Returns an error code that may provide more information about the error. |

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

## Public Methods

#### public [MessagingErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MessagingErrorCode)
**getMessagingErrorCode**
()

Returns an error code that may provide more information about the error.