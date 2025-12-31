# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException.md.txt

# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseException.md.txt

# FirebaseException

public class **FirebaseException** extends Exception  

|---|---|---|
| Known Direct Subclasses [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException), [FirebaseInstanceIdException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceIdException), [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException), [FirebaseProjectManagementException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagementException), [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------| | [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException)                                        | Generic exception related to Firebase Authentication.                                        | | [FirebaseInstanceIdException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceIdException)                             | Represents an exception encountered while interacting with the Firebase instance ID service. | | [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException)                         |                                                                                              | | [FirebaseProjectManagementException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagementException) | An exception encountered while interacting with the Firebase Project Management Service.     | | [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException)                | Generic exception related to Firebase Remote Config.                                         | |||

Base class for all Firebase exceptions.  

### Public Constructor Summary

|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseException#FirebaseException(com.google.firebase.ErrorCode, java.lang.String, java.lang.Throwable, com.google.firebase.IncomingHttpResponse))([ErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ErrorCode) errorCode, String message, Throwable cause, [IncomingHttpResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/IncomingHttpResponse) httpResponse) |
|   | [FirebaseException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseException#FirebaseException(com.google.firebase.ErrorCode, java.lang.String, java.lang.Throwable))([ErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ErrorCode) errorCode, String message, Throwable cause)                                                                                                                                                                                          |

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| final [ErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ErrorCode)                       | [getErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseException#getErrorCode())() Returns the platform-wide error code associated with this exception. |
| final [IncomingHttpResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/IncomingHttpResponse) | [getHttpResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseException#getHttpResponse())() Returns the HTTP response that resulted in this exception.     |

### Inherited Method Summary

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
**FirebaseException**
([ErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ErrorCode) errorCode, String message, Throwable cause, [IncomingHttpResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/IncomingHttpResponse) httpResponse)

<br />

#### public
**FirebaseException**
([ErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ErrorCode) errorCode, String message, Throwable cause)

<br />

## Public Methods

#### public final [ErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ErrorCode)
**getErrorCode**
()

Returns the platform-wide error code associated with this exception.  

##### Returns

- A Firebase error code.  

#### public final [IncomingHttpResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/IncomingHttpResponse)
**getHttpResponse**
()

Returns the HTTP response that resulted in this exception. If the exception was not caused by
an HTTP error response, returns null.  

##### Returns

- An HTTP response or null.