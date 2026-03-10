# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthWebException.md.txt

# FirebaseAuthWebException

# FirebaseAuthWebException


```
class FirebaseAuthWebException : FirebaseAuthException
```

<br />

|---|---|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) ||||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/java/lang/Exception.html) ||||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseException) |||
|   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException) ||
|   |   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthWebException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthWebException) |

*** ** * ** ***

Thrown when a web operation couldn't be completed.

This could happen in the following cases:

- `ERROR_WEB_CONTEXT_ALREADY_PRESENTED` thrown when another web operation is still in progress.
- `ERROR_WEB_CONTEXT_CANCELED` thrown when the pending operation was canceled by the user.
- `ERROR_WEB_STORAGE_UNSUPPORTED` thrown when the browser is not supported, or when 3rd party cookies or data are disabled in the browser.
- `ERROR_WEB_INTERNAL_ERROR` when there was a problem that occurred inside of the web widget that hosts the operation. Details should always accompany this message.

Inspect the error code and message to find out the specific cause.

Resolve this exception by waiting for the in-progress operation to complete, or by asking the user to try signing-in via the web context again.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthWebException#FirebaseAuthWebException(java.lang.String,java.lang.String)(errorCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, detailMessage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Default constructor. |

| ### Inherited functions |
|---|
| From [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException#getErrorCode()()` | |
| From [java.lang.Throwable](https://developer.android.com/reference/java/lang/Throwable.html) |---|---| | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html(p: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-cause.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/java/lang/StackTraceElement.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html(p: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html(p: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/java/lang/StackTraceElement.html!>!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/to-string.html()` | |

## Public constructors

### FirebaseAuthWebException

```
FirebaseAuthWebException(errorCode: String, detailMessage: String)
```

Default constructor.