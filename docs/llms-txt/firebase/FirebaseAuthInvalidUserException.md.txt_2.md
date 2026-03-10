# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidUserException.md.txt

# FirebaseAuthInvalidUserException

# FirebaseAuthInvalidUserException


```
class FirebaseAuthInvalidUserException : FirebaseAuthException
```

<br />

|---|---|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) ||||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/java/lang/Exception.html) ||||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseException) |||
|   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException) ||
|   |   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthInvalidUserException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidUserException) |

*** ** * ** ***

Thrown when performing an operation on a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser` instance that is no longer valid.

This could happen in the following cases:

- `ERROR_USER_DISABLED` if the user has been disabled (for example, in the Firebase console)
- `ERROR_USER_NOT_FOUND` if the user has been deleted (for example, in the Firebase console, or in another instance of this app)
- `ERROR_USER_TOKEN_EXPIRED` if the user's token has been revoked in the backend. This happens automatically if the user's credentials change in another device (for example, on a password change event).
- `ERROR_INVALID_USER_TOKEN` if the user's token is malformed. This should not happen under normal circumstances.

Inspect the error code and message to find out the specific cause.

You should consider this error condition as if the user had signed out of your app, and thus should require them to sign in again if they need to perform any action that requires authentication.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidUserException#FirebaseAuthInvalidUserException(java.lang.String,java.lang.String)(code: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, message: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Default constructor. |

| ### Inherited functions |
|---|
| From [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException#getErrorCode()()` | |
| From [java.lang.Throwable](https://developer.android.com/reference/java/lang/Throwable.html) |---|---| | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html(p: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-cause.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/java/lang/StackTraceElement.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html(p: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html(p: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/java/lang/StackTraceElement.html!>!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/to-string.html()` | |

## Public constructors

### FirebaseAuthInvalidUserException

```
FirebaseAuthInvalidUserException(code: String, message: String)
```

Default constructor.