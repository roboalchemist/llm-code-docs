# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerificationException.md.txt

# FirebasePhoneNumberVerificationException

# FirebasePhoneNumberVerificationException


```
class FirebasePhoneNumberVerificationException : FirebaseException
```

<br />

|---|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/java/lang/Exception.html) |||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseException) ||
|   |   |   | ↳ | [com.google.firebase.pnv.FirebasePhoneNumberVerificationException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerificationException) |

*** ** * ** ***

A subclass of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseException` that represents an exception specific to Firebase Phone Number Verification.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerificationException#FirebasePhoneNumberVerificationException(kotlin.Int,kotlin.String)(errorCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, message: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerificationException#FirebasePhoneNumberVerificationException(kotlin.Int,kotlin.String,kotlin.Throwable)( errorCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, message: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, cause: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html? )` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerificationException#errorCode()` The error code indicating the specific failure. |

| ### Inherited functions |
|---|
| From [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html(p0: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/java/lang/StackTraceElement.html>` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html>` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html(p0: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html(p0: https://developer.android.com/reference/java/io/PrintStream.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html(p0: https://developer.android.com/reference/java/io/PrintWriter.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html(p0: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/java/lang/StackTraceElement.html>)` | |

| ### Inherited properties |
|---|
| From [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |---|---| | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/cause.html` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/message.html` | |

## Public constructors

### FirebasePhoneNumberVerificationException

```
FirebasePhoneNumberVerificationException(errorCode: Int, message: String)
```

| Parameters |
|---|---|
| `errorCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The error code indicating the specific failure. |
| `message: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The error message. |

### FirebasePhoneNumberVerificationException

```
FirebasePhoneNumberVerificationException(
    errorCode: Int,
    message: String,
    cause: Throwable?
)
```

| Parameters |
|---|---|
| `message: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The error message. |
| `cause: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?` | The cause of the exception, or `null` if no cause is available. |

## Public properties

### errorCode

```
val errorCode: Int
```

The error code indicating the specific failure.