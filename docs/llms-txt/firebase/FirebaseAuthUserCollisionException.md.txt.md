# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException.md.txt

# FirebaseAuthUserCollisionException

# FirebaseAuthUserCollisionException


```
public final class FirebaseAuthUserCollisionException extends FirebaseAuthException
```

<br />

|---|---|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html) ||||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/java/lang/Exception.html) ||||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException) |||
|   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) ||
|   |   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthUserCollisionException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException) |

*** ** * ** ***

Thrown when an operation on a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` instance couldn't be completed due to a conflict with another existing user.

This could happen in the following cases:

- `ERROR_EMAIL_ALREADY_IN_USE` when trying to create a new account with `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#createUserWithEmailAndPassword(java.lang.String,java.lang.String)` or to change a user's email address, if the email is already in use by a different account
- `ERROR_ACCOUNT_EXISTS_WITH_DIFFERENT_CREDENTIAL` when calling `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` with a credential that asserts an email address in use by another account. This error will only be thrown if the "One account per email address" setting is enabled in the Firebase console (recommended).
- `ERROR_CREDENTIAL_ALREADY_IN_USE` when trying to link a user with an corresponding to another account already in use.

Inspect the error code and message to find out the specific cause.

Resolve this exception by asking the user to sign in again with valid credentials. In the case that this is thrown when using a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthCredential`, you can retrieve an updated credential from `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException#getUpdatedCredential()` and use it to sign-in.

## Summary

| ### Public fields |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException#email()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException#getEmail()()` Returns the email used when an error occurred when trying to sign in or link with an which was already associated with an account. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException#getUpdatedCredential()()` Returns a new valid `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` if this error occurred when trying to sign in or link with an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` which was already associated with an account. |

| ### Inherited fields |
|---|
| From [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) |---|---| | `final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException#errorCode()` | |

| ### Inherited methods |
|---|
| From [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) |---|---| | `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException#getErrorCode()()` Returns an error code that may provide more information about the error. | |
| From [java.lang.Throwable](https://developer.android.com/reference/java/lang/Throwable.html) |---|---| | `synchronized final void` | `https://developer.android.com/reference/java/lang/Throwable.html#addSuppressed(java.lang.Throwable)(https://developer.android.com/reference/java/lang/Throwable.html p)` | | `synchronized https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#fillInStackTrace()()` | | `synchronized https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getCause()()` | | `https://developer.android.com/reference/java/lang/String.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getLocalizedMessage()()` | | `https://developer.android.com/reference/java/lang/String.html` | `https://developer.android.com/reference/java/lang/Throwable.html#getMessage()()` | | `StackTraceElement[]` | `https://developer.android.com/reference/java/lang/Throwable.html#getStackTrace()()` | | `synchronized final Throwable[]` | `https://developer.android.com/reference/java/lang/Throwable.html#getSuppressed()()` | | `synchronized https://developer.android.com/reference/java/lang/Throwable.html` | `https://developer.android.com/reference/java/lang/Throwable.html#initCause(java.lang.Throwable)(https://developer.android.com/reference/java/lang/Throwable.html p)` | | `void` | `https://developer.android.com/reference/java/lang/Throwable.html#printStackTrace()()` | | `void` | `https://developer.android.com/reference/java/lang/Throwable.html#setStackTrace(java.lang.StackTraceElement[])(StackTraceElement[] p)` | | `https://developer.android.com/reference/java/lang/String.html` | `https://developer.android.com/reference/java/lang/Throwable.html#toString()()` | |

## Public fields

### email

```
public @Nullable String email
```

## Public methods

### getEmail

```
public @Nullable String getEmail()
```

Returns the email used when an error occurred when trying to sign in or link with an which was already associated with an account. Otherwise, returns `null`.

### getUpdatedCredential

```
public @Nullable AuthCredential getUpdatedCredential()
```

Returns a new valid `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` if this error occurred when trying to sign in or link with an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` which was already associated with an account. Otherwise, returns `null`.