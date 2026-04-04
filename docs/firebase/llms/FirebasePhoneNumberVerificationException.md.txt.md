# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerificationException.md.txt

# FirebasePhoneNumberVerificationException

# FirebasePhoneNumberVerificationException


```
public final class FirebasePhoneNumberVerificationException extends FirebaseException
```

<br />

|---|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html) |||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/java/lang/Exception.html) |||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException) ||
|   |   |   | ↳ | [com.google.firebase.pnv.FirebasePhoneNumberVerificationException](https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerificationException) |

*** ** * ** ***

A subclass of `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException` that represents an exception specific to Firebase Phone Number Verification.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerificationException#FirebasePhoneNumberVerificationException(kotlin.Int,kotlin.String)( int errorCode, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html message )` |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerificationException#FirebasePhoneNumberVerificationException(kotlin.Int,kotlin.String,kotlin.Throwable)( int errorCode, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html message, https://developer.android.com/reference/java/lang/Throwable.html cause )` |

| ### Public methods |
|---|---|
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerificationException#getErrorCode()()` The error code indicating the specific failure. |

| ### Inherited methods |
|---|
| From [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |---|---| | `final void` | `https://developer.android.com/reference/java/lang/Throwable.html#addSuppressed(kotlin.Throwable)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/Throwable.html p0)` | | `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#fillInStackTrace()()` | | `https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getCause()()` | | `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getLocalizedMessage()()` | | `https://developer.android.com/reference/java/lang/String.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getMessage()()` | | `@https://developer.android.com/reference/androidx/annotation/NonNull.html StackTraceElement[]` | `https://developer.android.com/reference/java/lang/Throwable.html#getStackTrace()()` | | `final @https://developer.android.com/reference/androidx/annotation/NonNull.html Throwable[]` | `https://developer.android.com/reference/java/lang/Throwable.html#getSuppressed()()` | | `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#initCause(kotlin.Throwable)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/Throwable.html p0)` | | `void` | `https://developer.android.com/reference/java/lang/Throwable.html#printStackTrace()()` | | `void` | `https://developer.android.com/reference/java/lang/Throwable.html#printStackTrace(java.io.PrintStream)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/io/PrintStream.html p0)` | | `void` | `https://developer.android.com/reference/java/lang/Throwable.html#printStackTrace(java.io.PrintWriter)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/io/PrintWriter.html p0)` | | `void` | `https://developer.android.com/reference/java/lang/Throwable.html#setStackTrace(kotlin.Array[java.lang.StackTraceElement])(@https://developer.android.com/reference/androidx/annotation/NonNull.html StackTraceElement[] p0)` | |

## Public constructors

### FirebasePhoneNumberVerificationException

```
public FirebasePhoneNumberVerificationException(
    int errorCode,
    @NonNull String message
)
```

| Parameters |
|---|---|
| `int errorCode` | The error code indicating the specific failure. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html message` | The error message. |

### FirebasePhoneNumberVerificationException

```
public FirebasePhoneNumberVerificationException(
    int errorCode,
    @NonNull String message,
    Throwable cause
)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html message` | The error message. |
| `https://developer.android.com/reference/java/lang/Throwable.html cause` | The cause of the exception, or `null` if no cause is available. |

## Public methods

### getErrorCode

```
public final int getErrorCode()
```

The error code indicating the specific failure.