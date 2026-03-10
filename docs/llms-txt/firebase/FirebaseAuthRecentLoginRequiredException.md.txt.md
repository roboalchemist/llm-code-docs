# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException.md.txt

# FirebaseAuthRecentLoginRequiredException

# FirebaseAuthRecentLoginRequiredException


```
public final class FirebaseAuthRecentLoginRequiredException extends FirebaseAuthException
```

<br />

|---|---|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html) ||||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/java/lang/Exception.html) ||||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException) |||
|   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) ||
|   |   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthRecentLoginRequiredException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException) |

*** ** * ** ***

Thrown on security sensitive operations on a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` instance that require the user to have signed in recently, when the requirement isn't met.

Resolve this exception by asking the user for their credentials again, and verifying them by calling `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)`.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException#FirebaseAuthRecentLoginRequiredException(java.lang.String,java.lang.String)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html code, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html message )` Default constructor. |

| ### Inherited fields |
|---|
| From [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) |---|---| | `final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException#errorCode()` | |

| ### Inherited methods |
|---|
| From [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) |---|---| | `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException#getErrorCode()()` Returns an error code that may provide more information about the error. | |
| From [java.lang.Throwable](https://developer.android.com/reference/java/lang/Throwable.html) |---|---| | `synchronized final void` | `https://developer.android.com/reference/java/lang/Throwable.html#addSuppressed(java.lang.Throwable)(https://developer.android.com/reference/java/lang/Throwable.html p)` | | `synchronized https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#fillInStackTrace()()` | | `synchronized https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getCause()()` | | `https://developer.android.com/reference/java/lang/String.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getLocalizedMessage()()` | | `https://developer.android.com/reference/java/lang/String.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getMessage()()` | | `StackTraceElement[]` | `https://developer.android.com/reference/java/lang/Throwable.html#getStackTrace()()` | | `synchronized final Throwable[]` | `https://developer.android.com/reference/java/lang/Throwable.html#getSuppressed()()` | | `synchronized https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#initCause(java.lang.Throwable)(https://developer.android.com/reference/java/lang/Throwable.html p)` | | `void` | `https://developer.android.com/reference/java/lang/Throwable.html#printStackTrace()()` | | `void` | `https://developer.android.com/reference/java/lang/Throwable.html#setStackTrace(java.lang.StackTraceElement[])(StackTraceElement[] p)` | | `https://developer.android.com/reference/java/lang/String.html` | `https://developer.android.com/reference/java/lang/Throwable.html#toString()()` | |

## Public constructors

### FirebaseAuthRecentLoginRequiredException

```
public FirebaseAuthRecentLoginRequiredException(
    @NonNull String code,
    @NonNull String message
)
```

Default constructor.