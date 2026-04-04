# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactor.md.txt

# MultiFactor

# MultiFactor


```
abstract class MultiFactor
```

<br />

*** ** * ** ***

Defines multi-factor related properties and operations pertaining to a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser`. This class acts as the main entry point for enrolling or un-enrolling second factors for a user, and provides access to their currently enrolled factors.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactor#MultiFactor()()` |

| ### Public functions |
|---|---|
| `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactor#enroll(com.google.firebase.auth.MultiFactorAssertion,java.lang.String)(multiFactorAssertion: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion, displayName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Enrolls a second factor as identified by the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion` parameter for the current user. |
| `abstract (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactor#getEnrolledFactors()()` Returns a list of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo` already associated with this user. |
| `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactor#getSession()()` Returns a session identifier for a second factor enrollment operation. |
| `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactor#unenroll(java.lang.String)(factorUid: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Unenrolls a second factor from this user. |
| `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactor#unenroll(com.google.firebase.auth.MultiFactorInfo)(multiFactorInfo: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo)` Unenrolls a second factor from this user. |

## Public constructors

### MultiFactor

```
MultiFactor()
```

## Public functions

### enroll

```
abstract fun enroll(multiFactorAssertion: MultiFactorAssertion, displayName: String?): Task<Void!>
```

Enrolls a second factor as identified by the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion` parameter for the current user.

On successful enrollment, existing Firebase sessions are revoked, and an email notification is sent to the user's email. The user's must have a verified email to enroll a second factor.

A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion` can be generated using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator#getAssertion(com.google.firebase.auth.PhoneAuthCredential)` for enrolling phone number as a second factor or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#getAssertionForEnrollment(com.google.firebase.auth.TotpSecret,java.lang.String)` for enrolling TOTP as a second factor.

| Parameters |
|---|---|
| `multiFactorAssertion: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion` | the assertion representing the second factor to enroll |
| `displayName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | an optional name for identifying this second factor |

### getEnrolledFactors

```
abstract fun getEnrolledFactors(): (Mutable)List<MultiFactorInfo!>
```

Returns a list of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo` already associated with this user.

If the user does not have any enrolled factors, the list will be empty.

### getSession

```
abstract fun getSession(): Task<MultiFactorSession!>
```

Returns a session identifier for a second factor enrollment operation. This is used to identify the current user trying to enroll a second factor.

To be used when building a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions` instance to call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` for phone factor enrollment, or when generating a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret` instance for TOTP factor enrollment.

### unenroll

```
abstract fun unenroll(factorUid: String): Task<Void!>
```

Unenrolls a second factor from this user.

The `factorUid` to be passed in can be retrieved from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactor#getEnrolledFactors()`.

### unenroll

```
abstract fun unenroll(multiFactorInfo: MultiFactorInfo): Task<Void!>
```

Unenrolls a second factor from this user.

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo` to be passed in can be gotten from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactor#getEnrolledFactors()`.