# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthUserCollisionException.md.txt

# FirebaseAuthUserCollisionException

# FirebaseAuthUserCollisionException


```
class FirebaseAuthUserCollisionException : FirebaseAuthException
```

<br />

|---|---|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) ||||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/java/lang/Exception.html) ||||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseException) |||
|   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException) ||
|   |   |   |   | ↳ | [com.google.firebase.auth.FirebaseAuthUserCollisionException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthUserCollisionException) |

*** ** * ** ***

Thrown when an operation on a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser` instance couldn't be completed due to a conflict with another existing user.

This could happen in the following cases:

- `ERROR_EMAIL_ALREADY_IN_USE` when trying to create a new account with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#createUserWithEmailAndPassword(java.lang.String,java.lang.String)` or to change a user's email address, if the email is already in use by a different account
- `ERROR_ACCOUNT_EXISTS_WITH_DIFFERENT_CREDENTIAL` when calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` with a credential that asserts an email address in use by another account. This error will only be thrown if the "One account per email address" setting is enabled in the Firebase console (recommended).
- `ERROR_CREDENTIAL_ALREADY_IN_USE` when trying to link a user with an corresponding to another account already in use.

Inspect the error code and message to find out the specific cause.

Resolve this exception by asking the user to sign in again with valid credentials. In the case that this is thrown when using a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential`, you can retrieve an updated credential from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthUserCollisionException#getUpdatedCredential()` and use it to sign-in.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthUserCollisionException#getUpdatedCredential()()` Returns a new valid `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` if this error occurred when trying to sign in or link with an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` which was already associated with an account. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthUserCollisionException#email()` |

| ### Inherited functions |
|---|
| From [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException#getErrorCode()()` | |
| From [java.lang.Throwable](https://developer.android.com/reference/java/lang/Throwable.html) |---|---| | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html(p: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-cause.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/java/lang/StackTraceElement.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html(p: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html(p: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/java/lang/StackTraceElement.html!>!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/to-string.html()` | |

## Public functions

### getUpdatedCredential

```
fun getUpdatedCredential(): AuthCredential?
```

Returns a new valid `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` if this error occurred when trying to sign in or link with an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` which was already associated with an account. Otherwise, returns `null`.

## Public properties

### email

```
val email: String?
```