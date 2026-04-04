# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion.md.txt

# MultiFactorAssertion

# MultiFactorAssertion


```
public abstract class MultiFactorAssertion
```

<br />

Known direct subclasses [PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorAssertion), [TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorAssertion)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorAssertion` | Asserts ownership of a phone number second factor. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorAssertion` | Asserts ownership of a TOTP second factor. |

*** ** * ** ***

Represents an assertion that the Firebase Authentication server can use to authenticate a user as part of a multi-factor flow.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion#MultiFactorAssertion()()` |

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion#getFactorId()()` Returns the factor id that this assertion is for. |

## Public constructors

### MultiFactorAssertion

```
public MultiFactorAssertion()
```

## Public methods

### getFactorId

```
public abstract @NonNull String getFactorId()
```

Returns the factor id that this assertion is for.