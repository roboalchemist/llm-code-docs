# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ServiceConnectionHandshakeFailedException.md.txt

# ServiceConnectionHandshakeFailedException

# ServiceConnectionHandshakeFailedException


```
public final class ServiceConnectionHandshakeFailedException extends FirebaseAIException
```

<br />

|---|---|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) ||||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) ||||
|   |   | ↳ | [java.lang.RuntimeException](https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html) |||
|   |   |   | ↳ | [com.google.firebase.ai.type.FirebaseAIException](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException) ||
|   |   |   |   | ↳ | [com.google.firebase.ai.type.ServiceConnectionHandshakeFailedException](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ServiceConnectionHandshakeFailedException) |

*** ** * ** ***

Handshake failed with the server

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ServiceConnectionHandshakeFailedException#ServiceConnectionHandshakeFailedException(kotlin.String,kotlin.Throwable)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html message, https://developer.android.com/reference/kotlin/java/lang/Throwable.html cause )` |

| ### Inherited fields |
|---|
| From [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |---|---| | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/cause.html` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/message.html` | |

| ### Inherited methods |
|---|
| From [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |---|---| | `final void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#addSuppressed-kotlin.Throwable-(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html p0)` | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html#fillInStackTrace--()` | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNullable.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getLocalizedMessage--()` | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html StackTraceElement[]` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getStackTrace--()` | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Throwable[]` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getSuppressed--()` | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html#initCause-kotlin.Throwable-(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNullable.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html p0)` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#printStackTrace--()` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#printStackTrace-java.io.PrintStream-(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/PrintStream.html p0)` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#printStackTrace-java.io.PrintWriter-(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/PrintWriter.html p0)` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#setStackTrace-kotlin.Array[java.lang.StackTraceElement]-(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html StackTraceElement[] p0)` | |

## Public constructors

### ServiceConnectionHandshakeFailedException

```
public ServiceConnectionHandshakeFailedException(
    @NonNull String message,
    Throwable cause
)
```