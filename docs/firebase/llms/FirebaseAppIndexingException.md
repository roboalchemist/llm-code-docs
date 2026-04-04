# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndexingException.md.txt

# FirebaseAppIndexingException

public class **FirebaseAppIndexingException** extends [FirebaseException](https://developers.google.com/android/reference/com/google/firebase/FirebaseException.html)  

|---|---|---|
| Known Direct Subclasses [FirebaseAppIndexingInvalidArgumentException](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndexingInvalidArgumentException), [FirebaseAppIndexingTooManyArgumentsException](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndexingTooManyArgumentsException) |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | [FirebaseAppIndexingInvalidArgumentException](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndexingInvalidArgumentException)   | The exception that is thrown if an invalid argument is provided to one of the Firebase App Indexing API methods.                                                                                                                                               | | [FirebaseAppIndexingTooManyArgumentsException](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndexingTooManyArgumentsException) | The exception that is thrown if the number of arguments passed to a Firebase App Indexing API method in a single call exceeds the allowed maximum of [Indexable.MAX_INDEXABLES_TO_BE_UPDATED_IN_ONE_CALL](https://firebase.google.com/docs/reference/android). | |||

Class of exceptions thrown by the Firebase App Indexing API.  

### Public Constructor Summary

|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseAppIndexingException](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndexingException#FirebaseAppIndexingException(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) detailMessage)                                                                                                             |
|   | [FirebaseAppIndexingException](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndexingException#FirebaseAppIndexingException(java.lang.String,%20java.lang.Throwable))([String](https://developer.android.com/reference/java/lang/String.html) detailMessage, [Throwable](https://developer.android.com/reference/java/lang/Throwable.html) cause) |

### Inherited Method Summary

From class java.lang.Throwable  

|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| synchronized final void                                                                              | addSuppressed([Throwable](https://developer.android.com/reference/java/lang/Throwable.html) arg0)                     |
| synchronized [Throwable](https://developer.android.com/reference/java/lang/Throwable.html)           | fillInStackTrace()                                                                                                    |
| synchronized [Throwable](https://developer.android.com/reference/java/lang/Throwable.html)           | getCause()                                                                                                            |
| [String](https://developer.android.com/reference/java/lang/String.html)                              | getLocalizedMessage()                                                                                                 |
| [String](https://developer.android.com/reference/java/lang/String.html)                              | getMessage()                                                                                                          |
| [StackTraceElement\[\]](https://developer.android.com/reference/java/lang/StackTraceElement.html)    | getStackTrace()                                                                                                       |
| synchronized final [Throwable\[\]](https://developer.android.com/reference/java/lang/Throwable.html) | getSuppressed()                                                                                                       |
| synchronized [Throwable](https://developer.android.com/reference/java/lang/Throwable.html)           | initCause([Throwable](https://developer.android.com/reference/java/lang/Throwable.html) arg0)                         |
| void                                                                                                 | printStackTrace()                                                                                                     |
| void                                                                                                 | printStackTrace([PrintWriter](https://developer.android.com/reference/java/io/PrintWriter.html) arg0)                 |
| void                                                                                                 | printStackTrace([PrintStream](https://developer.android.com/reference/java/io/PrintStream.html) arg0)                 |
| void                                                                                                 | setStackTrace([StackTraceElement\[\]](https://developer.android.com/reference/java/lang/StackTraceElement.html) arg0) |
| [String](https://developer.android.com/reference/java/lang/String.html)                              | toString()                                                                                                            |

From class java.lang.Object  

|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [Object](https://developer.android.com/reference/java/lang/Object.html)          | clone()                                                                              |
| boolean                                                                          | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| void                                                                             | finalize()                                                                           |
| final [Class](https://developer.android.com/reference/java/lang/Class.html)\<?\> | getClass()                                                                           |
| int                                                                              | hashCode()                                                                           |
| final void                                                                       | notify()                                                                             |
| final void                                                                       | notifyAll()                                                                          |
| [String](https://developer.android.com/reference/java/lang/String.html)          | toString()                                                                           |
| final void                                                                       | wait(long arg0, int arg1)                                                            |
| final void                                                                       | wait(long arg0)                                                                      |
| final void                                                                       | wait()                                                                               |

## Public Constructors

#### public **FirebaseAppIndexingException** ([String](https://developer.android.com/reference/java/lang/String.html) detailMessage)

#### public **FirebaseAppIndexingException** ([String](https://developer.android.com/reference/java/lang/String.html) detailMessage, [Throwable](https://developer.android.com/reference/java/lang/Throwable.html) cause)