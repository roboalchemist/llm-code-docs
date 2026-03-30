# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorGenerator.md.txt

# PhoneMultiFactorGenerator

# PhoneMultiFactorGenerator


```
public class PhoneMultiFactorGenerator
```

<br />

*** ** * ** ***

Helper class used to generate `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorAssertion`s.

## Summary

| ### Constants |
|---|---|
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorGenerator#FACTOR_ID() = "phone"` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorGenerator#PhoneMultiFactorGenerator()()` |

| ### Public methods |
|---|---|
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorAssertion` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorGenerator#getAssertion(com.google.firebase.auth.PhoneAuthCredential)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthCredential phoneAuthCredential)` Transforms a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthCredential` into a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorAssertion` which can be used to confirm ownership of a phone second factor. |

## Constants

### FACTOR_ID

```
public static final String FACTOR_ID = "phone"
```

## Public constructors

### PhoneMultiFactorGenerator

```
public PhoneMultiFactorGenerator()
```

## Public methods

### getAssertion

```
public static @NonNull PhoneMultiFactorAssertion getAssertion(@NonNull PhoneAuthCredential phoneAuthCredential)
```

Transforms a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthCredential` into a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorAssertion` which can be used to confirm ownership of a phone second factor.