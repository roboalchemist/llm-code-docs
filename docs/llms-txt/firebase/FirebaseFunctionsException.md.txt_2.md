# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.md.txt

# FirebaseFunctionsException

# FirebaseFunctionsException


```
class FirebaseFunctionsException : FirebaseException
```

<br />

|---|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) |||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseException) ||
|   |   |   | ↳ | [com.google.firebase.functions.FirebaseFunctionsException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException) |

*** ** * ** ***

The class for all Exceptions thrown by FirebaseFunctions.

## Summary

| ### Nested types |
|---|
| `enum https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html` The set of error status codes that can be returned from a Callable HTTPS tigger. |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException#code()` Gets the error code for the operation that failed. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException#details()` Gets the details object, if one was included in the error response. |

| ### Inherited functions |
|---|
| From [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html p0: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNullable.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNullable.html p0: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html p0: https://developer.android.com/reference/kotlin/java/io/PrintStream.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html p0: https://developer.android.com/reference/kotlin/java/io/PrintWriter.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html p0: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html>)` | |

| ### Inherited properties |
|---|
| From [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |---|---| | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/cause.html` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/message.html` | |

## Public properties

### code

```
val code: FirebaseFunctionsException.Code
```

Gets the error code for the operation that failed.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code` | the code for the `FirebaseFunctionsException` |

### details

```
val details: Any?
```

Gets the details object, if one was included in the error response.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | the object included in the "details" field of the response. |