# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.md.txt

# FirebaseFirestoreException

# FirebaseFirestoreException


```
public class FirebaseFirestoreException extends FirebaseException
```

<br />

|---|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) |||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException) ||
|   |   |   | ↳ | [com.google.firebase.firestore.FirebaseFirestoreException](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException) |

*** ** * ** ***

A class of exceptions thrown by Cloud Firestore.

## Summary

| ### Nested types |
|---|
| `public enum https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code` The set of Cloud Firestore status codes. |

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException#code()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException#FirebaseFirestoreException(java.lang.String,com.google.firebase.firestore.FirebaseFirestoreException.Code)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html detailMessage, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code code )` |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException#FirebaseFirestoreException(java.lang.String,com.google.firebase.firestore.FirebaseFirestoreException.Code,java.lang.Throwable)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html detailMessage, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code code, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html cause )` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException#getCode()()` Gets the error code for the Cloud Firestore operation that failed. |

| ### Inherited methods |
|---|
| From [java.lang.Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html) |---|---| | `synchronized final void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#addSuppressed-java.lang.Throwable-(https://developer.android.com/reference/kotlin/java/lang/Throwable.html exception)` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#fillInStackTrace--()` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getCause--()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getLocalizedMessage--()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getMessage--()` | | `StackTraceElement[]` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getStackTrace--()` | | `synchronized final Throwable[]` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getSuppressed--()` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#initCause-java.lang.Throwable-(https://developer.android.com/reference/kotlin/java/lang/Throwable.html cause)` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#printStackTrace--()` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#setStackTrace-java.lang.StackTraceElement[]-(StackTraceElement[] stackTrace)` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#toString--()` | |

## Public fields

### code

```
public final @NonNull FirebaseFirestoreException.Code code
```

## Public constructors

### FirebaseFirestoreException

```
public FirebaseFirestoreException(
    @NonNull String detailMessage,
    @NonNull FirebaseFirestoreException.Code code
)
```

### FirebaseFirestoreException

```
public FirebaseFirestoreException(
    @NonNull String detailMessage,
    @NonNull FirebaseFirestoreException.Code code,
    @Nullable Throwable cause
)
```

## Public methods

### getCode

```
public @NonNull FirebaseFirestoreException.Code getCode()
```

Gets the error code for the Cloud Firestore operation that failed.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code` | the code for the `FirebaseFirestoreException`. |