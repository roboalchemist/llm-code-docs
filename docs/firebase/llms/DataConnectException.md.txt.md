# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectException.md.txt

# DataConnectException

# DataConnectException


```
open class DataConnectException : Exception
```

<br />

|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) ||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) ||
|   |   | ↳ | [com.google.firebase.dataconnect.DataConnectException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectException) |

Known direct subclasses [DataConnectOperationException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationException)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationException` | The exception thrown when an error occurs in the execution of a Firebase Data Connect operation (that is, a query or mutation). |

*** ** * ** ***

The exception thrown when an error occurs in Firebase Data Connect.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectException#DataConnectException(kotlin.String,kotlin.Throwable)(message: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, cause: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?)` |

| ### Inherited functions |
|---|
| From [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html p0: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNullable.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNullable.html p0: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html p0: https://developer.android.com/reference/kotlin/java/io/PrintStream.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html p0: https://developer.android.com/reference/kotlin/java/io/PrintWriter.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html p0: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html>)` | |

| ### Inherited properties |
|---|
| From [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |---|---| | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/cause.html` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/message.html` | |

## Public constructors

### DataConnectException

```
DataConnectException(message: String, cause: Throwable? = null)
```