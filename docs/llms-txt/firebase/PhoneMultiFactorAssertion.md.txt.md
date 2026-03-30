# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorAssertion.md.txt

# PhoneMultiFactorAssertion

# PhoneMultiFactorAssertion


```
public class PhoneMultiFactorAssertion extends MultiFactorAssertion
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html) |||
| ↳ | [com.google.firebase.auth.MultiFactorAssertion](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion) ||
|   | ↳ | [com.google.firebase.auth.PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorAssertion) |

*** ** * ** ***

Asserts ownership of a phone number second factor.

An instance of this object can be obtained by calling `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorGenerator#getAssertion(com.google.firebase.auth.PhoneAuthCredential)`

## Summary

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorAssertion#getFactorId()()` Returns the factor id that this assertion is for. |

## Public methods

### getFactorId

```
public @NonNull String getFactorId()
```

Returns the factor id that this assertion is for. This is equivalent to `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorGenerator#FACTOR_ID()`