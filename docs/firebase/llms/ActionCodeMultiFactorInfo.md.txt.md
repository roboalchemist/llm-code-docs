# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeMultiFactorInfo.md.txt

# ActionCodeMultiFactorInfo

# ActionCodeMultiFactorInfo


```
public abstract class ActionCodeMultiFactorInfo extends ActionCodeInfo
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html) |||
| ↳ | [com.google.firebase.auth.ActionCodeInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeInfo) ||
|   | ↳ | [com.google.firebase.auth.ActionCodeMultiFactorInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeMultiFactorInfo) |

*** ** * ** ***

Holds information regarding out of band operations that involve an multi-factor authentication.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeMultiFactorInfo#ActionCodeMultiFactorInfo()()` |

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeMultiFactorInfo#getMultiFactorInfo()()` Returns the corresponding `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo` for the out of band action. |

| ### Inherited fields |
|---|
| From [com.google.firebase.auth.ActionCodeInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeInfo) |---|---| | `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `@https://firebase.google.com/docs/reference/android/com/google/android/gms/testing/lint/common/SuppressViolation(value = "hide_members_annotation") https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeInfo#email()` Member variable holding the email for this ActionCode Info | |

| ### Inherited methods |
|---|
| From [com.google.firebase.auth.ActionCodeInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeInfo) |---|---| | `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeInfo#getEmail()()` Returns the current email associated with the account, which may be changed as a result of the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` performed. | |

## Public constructors

### ActionCodeMultiFactorInfo

```
public ActionCodeMultiFactorInfo()
```

## Public methods

### getMultiFactorInfo

```
public abstract @NonNull MultiFactorInfo getMultiFactorInfo()
```

Returns the corresponding `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo` for the out of band action.

For `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#REVERT_SECOND_FACTOR_ADDITION()`, this represents the second factor being reverted.