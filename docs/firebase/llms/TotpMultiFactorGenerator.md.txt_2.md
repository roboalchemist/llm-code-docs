# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator.md.txt

# TotpMultiFactorGenerator

# TotpMultiFactorGenerator


```
class TotpMultiFactorGenerator
```

<br />

*** ** * ** ***

Helper class used to generate a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorAssertion`.

## Summary

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#FACTOR_ID() = "totp"` |

| ### Public functions |
|---|---|
| `java-static https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#generateSecret(com.google.firebase.auth.MultiFactorSession)(session: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession)` Creates a TOTP secret as part of enrolling a TOTP (time-based one-time password) second factor. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorAssertion` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#getAssertionForEnrollment(com.google.firebase.auth.TotpSecret,java.lang.String)(secret: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret, otp: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an assertion for completing the enrollment flow. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorAssertion` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#getAssertionForSignIn(java.lang.String,java.lang.String)(enrollmentId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, otp: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an assertion for the sign-in flow. |

## Constants

### FACTOR_ID

```
const val FACTOR_ID = "totp": String!
```

## Public functions

### generateSecret

```
java-static fun generateSecret(session: MultiFactorSession): Task<TotpSecret!>
```

Creates a TOTP secret as part of enrolling a TOTP (time-based one-time password) second factor. This method uses the auth instance corresponding to the user in the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession`.

| Parameters |
|---|---|
| `session: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession`. |

### getAssertionForEnrollment

```
java-static fun getAssertionForEnrollment(secret: TotpSecret, otp: String): TotpMultiFactorAssertion
```

Creates an assertion for completing the enrollment flow.

| Parameters |
|---|---|
| `secret: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret` | obtained from the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#generateSecret(com.google.firebase.auth.MultiFactorSession)` step. |
| `otp: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | one-time password obtained from the TOTP App. |

### getAssertionForSignIn

```
java-static fun getAssertionForSignIn(enrollmentId: String, otp: String): TotpMultiFactorAssertion
```

Creates an assertion for the sign-in flow.

| Parameters |
|---|---|
| `enrollmentId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | identifies the TOTP second factor being used. |
| `otp: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | one-time password obtained from the TOTP App. |