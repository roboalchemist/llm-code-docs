# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.md.txt

# FirebaseFirestoreException

# FirebaseFirestoreException


```
class FirebaseFirestoreException : FirebaseException
```

<br />

|---|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) |||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseException) ||
|   |   |   | ↳ | [com.google.firebase.firestore.FirebaseFirestoreException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException) |

*** ** * ** ***

A class of exceptions thrown by Cloud Firestore.

## Summary

| ### Nested types |
|---|
| `enum https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code` The set of Cloud Firestore status codes. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException#FirebaseFirestoreException(java.lang.String,com.google.firebase.firestore.FirebaseFirestoreException.Code)( detailMessage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, code: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code )` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException#FirebaseFirestoreException(java.lang.String,com.google.firebase.firestore.FirebaseFirestoreException.Code,java.lang.Throwable)( detailMessage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, code: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code, cause: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html? )` |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException#code()` |

| ### Inherited functions |
|---|
| From [java.lang.Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html) |---|---| | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html(exception: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-cause.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html(cause: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html(stackTrace: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html!>!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/to-string.html()` | |

## Public constructors

### FirebaseFirestoreException

```
FirebaseFirestoreException(
    detailMessage: String,
    code: FirebaseFirestoreException.Code
)
```

### FirebaseFirestoreException

```
FirebaseFirestoreException(
    detailMessage: String,
    code: FirebaseFirestoreException.Code,
    cause: Throwable?
)
```

## Public properties

### code

```
val code: FirebaseFirestoreException.Code
```