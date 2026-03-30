# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException.md.txt

# FirebaseAuthInvalidCredentialsException

# FirebaseAuthInvalidCredentialsException


```
public class FirebaseAuthInvalidCredentialsException extends FirebaseAuthException
```

<br />

|---|---|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html) ||||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/java/lang/Exception.html) ||||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException) |||
|   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) ||
|   |   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthInvalidCredentialsException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException) |

Known direct subclasses [FirebaseAuthWeakPasswordException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWeakPasswordException)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWeakPasswordException` | Thrown when using a weak password (less than 6 chars) to create a new account or to update an existing account's password. |

*** ** * ** ***

Thrown when one or more of the credentials passed to a method fail to identify and/or authenticate the user subject of that operation. Inspect the error code and message to find out the specific cause.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException#FirebaseAuthInvalidCredentialsException(java.lang.String,java.lang.String)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html code, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html message )` Default constructor. |

| ### Inherited fields |
|---|
| From [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) |---|---| | `final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException#errorCode()` | |

| ### Inherited methods |
|---|
| From [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) |---|---| | `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException#getErrorCode()()` Returns an error code that may provide more information about the error. | |
| From [java.lang.Throwable](https://developer.android.com/reference/java/lang/Throwable.html) |---|---| | `synchronized final void` | `https://developer.android.com/reference/java/lang/Throwable.html#addSuppressed(java.lang.Throwable)(https://developer.android.com/reference/java/lang/Throwable.html p)` | | `synchronized https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#fillInStackTrace()()` | | `synchronized https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getCause()()` | | `https://developer.android.com/reference/java/lang/String.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getLocalizedMessage()()` | | `https://developer.android.com/reference/java/lang/String.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getMessage()()` | | `StackTraceElement[]` | `https://developer.android.com/reference/java/lang/Throwable.html#getStackTrace()()` | | `synchronized final Throwable[]` | `https://developer.android.com/reference/java/lang/Throwable.html#getSuppressed()()` | | `synchronized https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#initCause(java.lang.Throwable)(https://developer.android.com/reference/java/lang/Throwable.html p)` | | `void` | `https://developer.android.com/reference/java/lang/Throwable.html#printStackTrace()()` | | `void` | `https://developer.android.com/reference/java/lang/Throwable.html#setStackTrace(java.lang.StackTraceElement[])(StackTraceElement[] p)` | | `https://developer.android.com/reference/java/lang/String.html` | `https://developer.android.com/reference/java/lang/Throwable.html#toString()()` | |

## Public constructors

### FirebaseAuthInvalidCredentialsException

```
public FirebaseAuthInvalidCredentialsException(
    @NonNull String code,
    @NonNull String message
)
```

Default constructor.