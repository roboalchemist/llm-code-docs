# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException.md.txt

# FirebaseAuthException

# FirebaseAuthException


```
public class FirebaseAuthException extends FirebaseException
```

<br />

|---|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html) |||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/java/lang/Exception.html) |||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException) ||
|   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) |

Known direct subclasses [FirebaseAuthActionCodeException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthActionCodeException), [FirebaseAuthEmailException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthEmailException), [FirebaseAuthInvalidCredentialsException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException), [FirebaseAuthInvalidUserException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException), [FirebaseAuthMissingActivityForRecaptchaException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthMissingActivityForRecaptchaException), [FirebaseAuthMultiFactorException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthMultiFactorException), [FirebaseAuthRecentLoginRequiredException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException), [FirebaseAuthUserCollisionException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException), [FirebaseAuthWebException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWebException)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthActionCodeException` | Represents the exception which is a result of an expired or an invalid out of band code. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthEmailException` | Represents the exception which is a result of an attempt to send an email via Firebase Auth (e.g. a password reset email) |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` | Thrown when one or more of the credentials passed to a method fail to identify and/or authenticate the user subject of that operation. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException` | Thrown when performing an operation on a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` instance that is no longer valid. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthMissingActivityForRecaptchaException` | Thrown when the auth request attempted to fetch a reCAPTCHA token, but the activity is missing or null. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthMultiFactorException` | This exception is returned when a user that previously enrolled a second factor tries to sign in and passes the first factor successfully. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException` | Thrown on security sensitive operations on a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` instance that require the user to have signed in recently, when the requirement isn't met. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException` | Thrown when an operation on a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` instance couldn't be completed due to a conflict with another existing user. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWebException` | Thrown when a web operation couldn't be completed. |

Known indirect subclasses [FirebaseAuthWeakPasswordException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWeakPasswordException)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWeakPasswordException` | Thrown when using a weak password (less than 6 chars) to create a new account or to update an existing account's password. |

*** ** * ** ***

Generic exception related to Firebase Authentication. Check the error code and message for more details.

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException#errorCode()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException#FirebaseAuthException(java.lang.String,java.lang.String)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html errorCode, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html detailMessage )` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException#getErrorCode()()` Returns an error code that may provide more information about the error. |

| ### Inherited methods |
|---|
| From [java.lang.Throwable](https://developer.android.com/reference/java/lang/Throwable.html) |---|---| | `synchronized final void` | `https://developer.android.com/reference/java/lang/Throwable.html#addSuppressed(java.lang.Throwable)(https://developer.android.com/reference/java/lang/Throwable.html p)` | | `synchronized https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#fillInStackTrace()()` | | `synchronized https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getCause()()` | | `https://developer.android.com/reference/java/lang/String.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getLocalizedMessage()()` | | `https://developer.android.com/reference/java/lang/String.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getMessage()()` | | `StackTraceElement[]` | `https://developer.android.com/reference/java/lang/Throwable.html#getStackTrace()()` | | `synchronized final Throwable[]` | `https://developer.android.com/reference/java/lang/Throwable.html#getSuppressed()()` | | `synchronized https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#initCause(java.lang.Throwable)(https://developer.android.com/reference/java/lang/Throwable.html p)` | | `void` | `https://developer.android.com/reference/java/lang/Throwable.html#printStackTrace()()` | | `void` | `https://developer.android.com/reference/java/lang/Throwable.html#setStackTrace(java.lang.StackTraceElement[])(StackTraceElement[] p)` | | `https://developer.android.com/reference/java/lang/String.html` | `https://developer.android.com/reference/java/lang/Throwable.html#toString()()` | |

## Public fields

### errorCode

```
public final String errorCode
```

## Public constructors

### FirebaseAuthException

```
public FirebaseAuthException(
    @NonNull String errorCode,
    @NonNull String detailMessage
)
```

## Public methods

### getErrorCode

```
public @NonNull String getErrorCode()
```

Returns an error code that may provide more information about the error.