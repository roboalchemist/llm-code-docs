# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorAssertion.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorAssertion.md.txt

# TotpMultiFactorAssertion

# TotpMultiFactorAssertion


```
class TotpMultiFactorAssertion : MultiFactorAssertion
```

<br />

|---|---|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                              |||
| â³ | [com.google.firebase.auth.MultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion)            ||
|   | â³ | [com.google.firebase.auth.TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorAssertion) |

*** ** * ** ***

Asserts ownership of a TOTP second factor.

An instance of this object can be obtained by calling [getAssertionForEnrollment](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#getAssertionForEnrollment(com.google.firebase.auth.TotpSecret,java.lang.String)) or [getAssertionForSignIn](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#getAssertionForSignIn(java.lang.String,java.lang.String)).

## Summary

|                               ### Public functions                               |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [getFactorId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorAssertion#getFactorId())`()` Returns the factor identifier that this assertion is for. |

## Public functions

### getFactorId

```
funÂ getFactorId():Â String
```

Returns the factor identifier that this assertion is for. This is equivalent to [FACTOR_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#FACTOR_ID()).