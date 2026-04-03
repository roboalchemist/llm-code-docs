# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneMultiFactorGenerator.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorGenerator.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator.md.txt

# PhoneMultiFactorGenerator

# PhoneMultiFactorGenerator


```
class PhoneMultiFactorGenerator
```

<br />

*** ** * ** ***

Helper class used to generate [PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorAssertion)s.

## Summary

|                                        ### Constants                                        |
|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [FACTOR_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator#FACTOR_ID())` = "phone"` |

|                                                                      ### Public constructors                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PhoneMultiFactorGenerator](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator#PhoneMultiFactorGenerator())`()` |

|                                                              ### Public functions                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorAssertion) | [getAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator#getAssertion(com.google.firebase.auth.PhoneAuthCredential))`(phoneAuthCredential: `[PhoneAuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential)`)` Transforms a [PhoneAuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential) into a [PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorAssertion) which can be used to confirm ownership of a phone second factor. |

## Constants

### FACTOR_ID

```
constÂ valÂ FACTOR_ID = "phone":Â String!
```  

## Public constructors

### PhoneMultiFactorGenerator

```
PhoneMultiFactorGenerator()
```  

## Public functions

### getAssertion

```
java-staticÂ funÂ getAssertion(phoneAuthCredential:Â PhoneAuthCredential):Â PhoneMultiFactorAssertion
```

Transforms a [PhoneAuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential) into a [PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorAssertion) which can be used to confirm ownership of a phone second factor.