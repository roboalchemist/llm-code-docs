# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException.md.txt

# FirebaseException

Also: ["Google
Play services"](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException) public class **FirebaseException** extends [Exception](https://developer.android.com/reference/java/lang/Exception.html)  

|---|---|---|
| Known Direct Subclasses [FirebaseApiNotAvailableException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApiNotAvailableException), [FirebaseAppIndexingException](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndexingException), [FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException), [FirebaseFirestoreException](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException), [FirebaseNetworkException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseNetworkException), [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException), [FirebaseTooManyRequestsException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseTooManyRequestsException), [StorageException](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException) |---|---| | [FirebaseApiNotAvailableException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApiNotAvailableException) | Indicates that a requested API is not available. | | [FirebaseAppIndexingException](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndexingException) | Class of exceptions thrown by the Firebase App Indexing API. | | [FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) | Generic exception related to Firebase Authentication. | | [FirebaseFirestoreException](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException) | A class of exceptions thrown by Firestore | | [FirebaseNetworkException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseNetworkException) | Exception thrown when a request to a Firebase service has failed due to a network error. | | [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) | Base class for `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` exceptions. | | [FirebaseTooManyRequestsException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseTooManyRequestsException) | Exception thrown when a request to a Firebase service has been blocked due to having received too many consecutive requests from the same device. | | [StorageException](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException) | Represents an Exception resulting from an operation on a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. | |||

|---|---|---|
| Known Indirect Subclasses [FirebaseAppIndexingInvalidArgumentException](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndexingInvalidArgumentException), [FirebaseAppIndexingTooManyArgumentsException](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndexingTooManyArgumentsException), [FirebaseAuthActionCodeException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthActionCodeException), [FirebaseAuthEmailException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthEmailException), [FirebaseAuthInvalidCredentialsException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException), [FirebaseAuthInvalidUserException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException), [FirebaseAuthRecentLoginRequiredException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException), [FirebaseAuthUserCollisionException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException), [FirebaseAuthWeakPasswordException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWeakPasswordException), [FirebaseRemoteConfigFetchException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchException), [FirebaseRemoteConfigFetchThrottledException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException) |---|---| | [FirebaseAppIndexingInvalidArgumentException](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndexingInvalidArgumentException) | The exception that is thrown if an invalid argument is provided to one of the Firebase App Indexing API methods. | | [FirebaseAppIndexingTooManyArgumentsException](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndexingTooManyArgumentsException) | The exception that is thrown if the number of arguments passed to a Firebase App Indexing API method in a single call exceeds the allowed maximum of `https://firebase.google.com/docs/reference/android`. | | [FirebaseAuthActionCodeException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthActionCodeException) | Represents the exception which is a result of an expired or an invalid out of band code. | | [FirebaseAuthEmailException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthEmailException) | Represents the exception which is a result of an attempt to send an email via Firebase Auth (e.g. | | [FirebaseAuthInvalidCredentialsException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException) | Thrown when one or more of the credentials passed to a method fail to identify and/or authenticate the user subject of that operation. | | [FirebaseAuthInvalidUserException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException) | Thrown when performing an operation on a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` instance that is no longer valid. | | [FirebaseAuthRecentLoginRequiredException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException) | Thrown on security sensitive operations on a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` instance that require the user to have signed in recently, when the requirement isn't met. | | [FirebaseAuthUserCollisionException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException) | Thrown when an operation on a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` instance couldn't be completed due to a conflict with another existing user. | | [FirebaseAuthWeakPasswordException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWeakPasswordException) | Thrown when using a weak password (less than 6 chars) to create a new account or to update an existing account's password. | | [FirebaseRemoteConfigFetchException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchException) | Exception thrown when the `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#fetch()` operation cannot be completed successfully. | | [FirebaseRemoteConfigFetchThrottledException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException) | Exception thrown when the `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#fetch()` operation cannot be completed successfully, due to throttling. | |||

Base class for all Firebase exceptions.

### Public Constructor Summary

|---|---|
|   | [FirebaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException#FirebaseException(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) detailMessage) |
|   | [FirebaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException#FirebaseException(java.lang.String, java.lang.Throwable))([String](https://developer.android.com/reference/java/lang/String.html) detailMessage, [Throwable](https://developer.android.com/reference/java/lang/Throwable.html) cause) |

### Protected Constructor Summary

|---|---|
|   | [FirebaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException#FirebaseException())() |

### Inherited Method Summary

From class java.lang.Throwable

|---|---|
| synchronized final void | addSuppressed([Throwable](https://developer.android.com/reference/java/lang/Throwable.html) arg0) |
| synchronized [Throwable](https://developer.android.com/reference/java/lang/Throwable.html) | fillInStackTrace() |
| synchronized [Throwable](https://developer.android.com/reference/java/lang/Throwable.html) | getCause() |
| [String](https://developer.android.com/reference/java/lang/String.html) | getLocalizedMessage() |
| [String](https://developer.android.com/reference/java/lang/String.html) | getMessage() |
| [StackTraceElement\[\]](https://developer.android.com/reference/java/lang/StackTraceElement.html) | getStackTrace() |
| synchronized final [Throwable\[\]](https://developer.android.com/reference/java/lang/Throwable.html) | getSuppressed() |
| synchronized [Throwable](https://developer.android.com/reference/java/lang/Throwable.html) | initCause([Throwable](https://developer.android.com/reference/java/lang/Throwable.html) arg0) |
| void | printStackTrace() |
| void | printStackTrace([PrintWriter](https://developer.android.com/reference/java/io/PrintWriter.html) arg0) |
| void | printStackTrace([PrintStream](https://developer.android.com/reference/java/io/PrintStream.html) arg0) |
| void | setStackTrace([StackTraceElement\[\]](https://developer.android.com/reference/java/lang/StackTraceElement.html) arg0) |
| [String](https://developer.android.com/reference/java/lang/String.html) | toString() |

From class java.lang.Object

|---|---|
| [Object](https://developer.android.com/reference/java/lang/Object.html) | clone() |
| boolean | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| void | finalize() |
| final [Class](https://developer.android.com/reference/java/lang/Class.html)\<?\> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| [String](https://developer.android.com/reference/java/lang/String.html) | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |

## Public Constructors

#### public **FirebaseException** ([String](https://developer.android.com/reference/java/lang/String.html) detailMessage)

Also: ["Google Play services"](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException#FirebaseException(java.lang.String))

#### public **FirebaseException** ([String](https://developer.android.com/reference/java/lang/String.html) detailMessage, [Throwable](https://developer.android.com/reference/java/lang/Throwable.html) cause)

Also: ["Google Play services"](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException#FirebaseException(java.lang.String, java.lang.Throwable))

## Protected Constructors

#### protected **FirebaseException** ()

Also: ["Google Play services"](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException#FirebaseException())