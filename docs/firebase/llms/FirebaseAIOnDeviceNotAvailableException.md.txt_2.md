# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIOnDeviceNotAvailableException.md.txt

# FirebaseAIOnDeviceNotAvailableException

# FirebaseAIOnDeviceNotAvailableException


```
@PublicPreviewAPI
class FirebaseAIOnDeviceNotAvailableException : FirebaseAIException
```

<br />

|---|---|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) ||||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) ||||
|   |   | ↳ | [java.lang.RuntimeException](https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html) |||
|   |   |   | ↳ | [com.google.firebase.ai.type.FirebaseAIException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException) ||
|   |   |   |   | ↳ | [com.google.firebase.ai.type.FirebaseAIOnDeviceNotAvailableException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIOnDeviceNotAvailableException) |

*** ** * ** ***

An operation has been requested, but device doesn't support local models, or they are not available.

Prefer using the corresponding `isAvailable()` method on the model to check the status before trying to use it.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIOnDeviceNotAvailableException#FirebaseAIOnDeviceNotAvailableException(com.google.firebase.ai.ondevice.interop.FirebaseAIOnDeviceNotAvailableException)( cause: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/interop/FirebaseAIOnDeviceNotAvailableException )` |

| ### Inherited functions |
|---|
| From [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html p0: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNullable.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNullable.html p0: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html()` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html p0: https://developer.android.com/reference/kotlin/java/io/PrintStream.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html p0: https://developer.android.com/reference/kotlin/java/io/PrintWriter.html)` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html p0: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html>)` | |

| ### Inherited properties |
|---|
| From [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |---|---| | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/cause.html` | | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/message.html` | |

## Public constructors

### FirebaseAIOnDeviceNotAvailableException

```
FirebaseAIOnDeviceNotAvailableException(
    cause: FirebaseAIOnDeviceNotAvailableException
)
```