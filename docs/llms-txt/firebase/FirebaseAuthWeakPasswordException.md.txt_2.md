# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthWeakPasswordException.md.txt

# FirebaseAuthWeakPasswordException

# FirebaseAuthWeakPasswordException


```
class FirebaseAuthWeakPasswordException : FirebaseAuthInvalidCredentialsException
```

<br />

|---|---|---|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/java/lang/Exception.html) |||||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseException) ||||
|   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException) |||
|   |   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthInvalidCredentialsException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException) ||
|   |   |   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthWeakPasswordException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthWeakPasswordException) |

*** ** * ** ***

Thrown when using a weak password (less than 6 chars) to create a new account or to update an existing account's password. Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthWeakPasswordException#getReason()` to get a message with the reason the validation failed that you can display to your users.

## Summary

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthWeakPasswordException#reason()` |

| ### Inherited functions |
|---|
| From [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException#getErrorCode()()` | |
| From [java.lang.Throwable](https://developer.android.com/reference/java/lang/Throwable.html) |---|---| | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html(p: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-cause.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/java/lang/StackTraceElement.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html(p: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html(p: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/java/lang/StackTraceElement.html!>!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/to-string.html()` | |

## Public properties

### reason

```
val reason: String?
```