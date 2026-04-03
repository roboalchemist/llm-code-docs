# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorAssertion.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorAssertion.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion.md.txt

# MultiFactorAssertion

# MultiFactorAssertion


```
abstract class MultiFactorAssertion
```

<br />

Known direct subclasses  
[PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorAssertion), [TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorAssertion)  

|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| [PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorAssertion) | Asserts ownership of a phone number second factor. |
| [TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorAssertion)   | Asserts ownership of a TOTP second factor.         |

*** ** * ** ***

Represents an assertion that the Firebase Authentication server can use to authenticate a user as part of a multi-factor flow.

## Summary

|                                                              ### Public constructors                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [MultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion#MultiFactorAssertion())`()` |

|                                    ### Public functions                                     |
|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abstract `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [getFactorId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion#getFactorId())`()` Returns the factor id that this assertion is for. |

## Public constructors

### MultiFactorAssertion

```
MultiFactorAssertion()
```  

## Public functions

### getFactorId

```
abstractÂ funÂ getFactorId():Â String
```

Returns the factor id that this assertion is for.