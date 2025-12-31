# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorAssertion.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorAssertion.md.txt

# PhoneMultiFactorAssertion

# PhoneMultiFactorAssertion


```
class PhoneMultiFactorAssertion : MultiFactorAssertion
```

<br />

|---|---|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                                |||
| â³ | [com.google.firebase.auth.MultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion)              ||
|   | â³ | [com.google.firebase.auth.PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorAssertion) |

*** ** * ** ***

Asserts ownership of a phone number second factor.

An instance of this object can be obtained by calling [getAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator#getAssertion(com.google.firebase.auth.PhoneAuthCredential))

## Summary

|                               ### Public functions                               |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [getFactorId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorAssertion#getFactorId())`()` Returns the factor id that this assertion is for. |

## Public functions

### getFactorId

```
funÂ getFactorId():Â String
```

Returns the factor id that this assertion is for. This is equivalent to [FACTOR_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator#FACTOR_ID())