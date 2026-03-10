# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator.md.txt

# PhoneMultiFactorGenerator

# PhoneMultiFactorGenerator


```
class PhoneMultiFactorGenerator
```

<br />

*** ** * ** ***

Helper class used to generate `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorAssertion`s.

## Summary

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator#FACTOR_ID() = "phone"` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator#PhoneMultiFactorGenerator()()` |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorAssertion` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator#getAssertion(com.google.firebase.auth.PhoneAuthCredential)(phoneAuthCredential: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential)` Transforms a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential` into a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorAssertion` which can be used to confirm ownership of a phone second factor. |

## Constants

### FACTOR_ID

```
const val FACTOR_ID = "phone": String!
```

## Public constructors

### PhoneMultiFactorGenerator

```
PhoneMultiFactorGenerator()
```

## Public functions

### getAssertion

```
java-static fun getAssertion(phoneAuthCredential: PhoneAuthCredential): PhoneMultiFactorAssertion
```

Transforms a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential` into a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorAssertion` which can be used to confirm ownership of a phone second factor.