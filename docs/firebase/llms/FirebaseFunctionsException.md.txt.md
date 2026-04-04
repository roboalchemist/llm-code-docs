# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.md.txt

# FirebaseFunctionsException

# FirebaseFunctionsException


```
public final class FirebaseFunctionsException extends FirebaseException
```

<br />

|---|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) |||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException) ||
|   |   |   | ↳ | [com.google.firebase.functions.FirebaseFunctionsException](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException) |

*** ** * ** ***

The class for all Exceptions thrown by FirebaseFunctions.

## Summary

| ### Nested types |
|---|
| `public enum https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code extends https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html` The set of error status codes that can be returned from a Callable HTTPS tigger. |
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code.Companion` |

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException#code()` Gets the error code for the operation that failed. |
| `final https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException#details()` Gets the details object, if one was included in the error response. |

| ### Inherited fields |
|---|
| From [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |---|---| | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/cause.html` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/message.html` | |

| ### Inherited methods |
|---|
| From [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |---|---| | `final void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#addSuppressed-kotlin.Throwable-(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html p0)` | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html#fillInStackTrace--()` | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNullable.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getLocalizedMessage--()` | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html StackTraceElement[]` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getStackTrace--()` | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Throwable[]` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getSuppressed--()` | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html#initCause-kotlin.Throwable-(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNullable.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html p0)` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#printStackTrace--()` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#printStackTrace-java.io.PrintStream-(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/PrintStream.html p0)` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#printStackTrace-java.io.PrintWriter-(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/PrintWriter.html p0)` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#setStackTrace-kotlin.Array[java.lang.StackTraceElement]-(@https://developer.android.com/reference/kotlin/androidx/annotation/RecentlyNonNull.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html StackTraceElement[] p0)` | |

## Public fields

### code

```
public final @NonNull FirebaseFunctionsException.Code code
```

Gets the error code for the operation that failed.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code` | the code for the `FirebaseFunctionsException` |

### details

```
public final Object details
```

Gets the details object, if one was included in the error response.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/Object.html` | the object included in the "details" field of the response. |