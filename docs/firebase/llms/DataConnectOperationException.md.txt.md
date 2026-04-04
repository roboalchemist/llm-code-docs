# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationException.md.txt

# DataConnectOperationException

# DataConnectOperationException


```
open class DataConnectOperationException : DataConnectException
```

<br />

|---|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) |||
|   |   | ↳ | [com.google.firebase.dataconnect.DataConnectException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectException) ||
|   |   |   | ↳ | [com.google.firebase.dataconnect.DataConnectOperationException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationException) |

*** ** * ** ***

The exception thrown when an error occurs in the execution of a Firebase Data Connect operation (that is, a query or mutation). This exception means that a response was, indeed, received from the backend but either the response included one or more errors or the client could not successfully process the result (for example, decoding the response data failed).

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationException#DataConnectOperationException(kotlin.String,kotlin.Throwable,com.google.firebase.dataconnect.DataConnectOperationFailureResponse)( message: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, cause: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?, response: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse<*> )` |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse<*>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationException#response()` |

| ### Inherited functions |
|---|
| From [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html p0: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNullable.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNullable.html p0: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html p0: https://developer.android.com/reference/kotlin/java/io/PrintStream.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html p0: https://developer.android.com/reference/kotlin/java/io/PrintWriter.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html p0: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html>)` | |

| ### Inherited properties |
|---|
| From [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |---|---| | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/cause.html` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/message.html` | |

## Public constructors

### DataConnectOperationException

```
DataConnectOperationException(
    message: String,
    cause: Throwable? = null,
    response: DataConnectOperationFailureResponse<*>
)
```

## Public properties

### response

```
val response: DataConnectOperationFailureResponse<*>
```