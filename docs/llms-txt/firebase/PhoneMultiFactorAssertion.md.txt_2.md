# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorAssertion.md.txt

# PhoneMultiFactorAssertion

# PhoneMultiFactorAssertion


```
class PhoneMultiFactorAssertion : MultiFactorAssertion
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.auth.MultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion) ||
|   | ↳ | [com.google.firebase.auth.PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorAssertion) |

*** ** * ** ***

Asserts ownership of a phone number second factor.

An instance of this object can be obtained by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator#getAssertion(com.google.firebase.auth.PhoneAuthCredential)`

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorAssertion#getFactorId()()` Returns the factor id that this assertion is for. |

## Public functions

### getFactorId

```
fun getFactorId(): String
```

Returns the factor id that this assertion is for. This is equivalent to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator#FACTOR_ID()`