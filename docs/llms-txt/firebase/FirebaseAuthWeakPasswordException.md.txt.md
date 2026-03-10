# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWeakPasswordException.md.txt

# FirebaseAuthWeakPasswordException

# FirebaseAuthWeakPasswordException


```
public final class FirebaseAuthWeakPasswordException extends FirebaseAuthInvalidCredentialsException
```

<br />

|---|---|---|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html) |||||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/java/lang/Exception.html) |||||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException) ||||
|   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) |||
|   |   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthInvalidCredentialsException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException) ||
|   |   |   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthWeakPasswordException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWeakPasswordException) |

*** ** * ** ***

Thrown when using a weak password (less than 6 chars) to create a new account or to update an existing account's password. Use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWeakPasswordException#getReason()` to get a message with the reason the validation failed that you can display to your users.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWeakPasswordException#reason()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWeakPasswordException#getReason()()` Returns a message that contains the reason that the password strength validation failed. |

| ### Inherited fields |
|---|
| From [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) |---|---| | `final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException#errorCode()` | |

| ### Inherited methods |
|---|
| From [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) |---|---| | `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException#getErrorCode()()` Returns an error code that may provide more information about the error. | |
| From [java.lang.Throwable](https://developer.android.com/reference/java/lang/Throwable.html) |---|---| | `synchronized final void` | `https://developer.android.com/reference/java/lang/Throwable.html#addSuppressed(java.lang.Throwable)(https://developer.android.com/reference/java/lang/Throwable.html p)` | | `synchronized https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#fillInStackTrace()()` | | `synchronized https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getCause()()` | | `https://developer.android.com/reference/java/lang/String.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getLocalizedMessage()()` | | `https://developer.android.com/reference/java/lang/String.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getMessage()()` | | `StackTraceElement[]` | `https://developer.android.com/reference/java/lang/Throwable.html#getStackTrace()()` | | `synchronized final Throwable[]` | `https://developer.android.com/reference/java/lang/Throwable.html#getSuppressed()()` | | `synchronized https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#initCause(java.lang.Throwable)(https://developer.android.com/reference/java/lang/Throwable.html p)` | | `void` | `https://developer.android.com/reference/java/lang/Throwable.html#printStackTrace()()` | | `void` | `https://developer.android.com/reference/java/lang/Throwable.html#setStackTrace(java.lang.StackTraceElement[])(StackTraceElement[] p)` | | `https://developer.android.com/reference/java/lang/String.html` | `https://developer.android.com/reference/java/lang/Throwable.html#toString()()` | |

## Public fields

### reason

```
public final @Nullable String reason
```

## Public methods

### getReason

```
public @Nullable String getReason()
```

Returns a message that contains the reason that the password strength validation failed. This message can be directly shown to the user.