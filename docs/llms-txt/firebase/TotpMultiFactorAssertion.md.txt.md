# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorAssertion.md.txt

# TotpMultiFactorAssertion

# TotpMultiFactorAssertion


```
public class TotpMultiFactorAssertion extends MultiFactorAssertion
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html) |||
| ↳ | [com.google.firebase.auth.MultiFactorAssertion](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion) ||
|   | ↳ | [com.google.firebase.auth.TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorAssertion) |

*** ** * ** ***

Asserts ownership of a TOTP second factor.

An instance of this object can be obtained by calling `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorGenerator#getAssertionForEnrollment(com.google.firebase.auth.TotpSecret,java.lang.String)` or `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorGenerator#getAssertionForSignIn(java.lang.String,java.lang.String)`.

## Summary

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorAssertion#getFactorId()()` Returns the factor identifier that this assertion is for. |

## Public methods

### getFactorId

```
public @NonNull String getFactorId()
```

Returns the factor identifier that this assertion is for. This is equivalent to `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorGenerator#FACTOR_ID()`.