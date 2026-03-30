# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeMultiFactorInfo.md.txt

# ActionCodeMultiFactorInfo

# ActionCodeMultiFactorInfo


```
abstract class ActionCodeMultiFactorInfo : ActionCodeInfo
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.auth.ActionCodeInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo) ||
|   | ↳ | [com.google.firebase.auth.ActionCodeMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeMultiFactorInfo) |

*** ** * ** ***

Holds information regarding out of band operations that involve an multi-factor authentication.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeMultiFactorInfo#ActionCodeMultiFactorInfo()()` |

| ### Public functions |
|---|---|
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeMultiFactorInfo#getMultiFactorInfo()()` Returns the corresponding `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo` for the out of band action. |

| ### Inherited functions |
|---|
| From [com.google.firebase.auth.ActionCodeInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo#getEmail()()` Returns the current email associated with the account, which may be changed as a result of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation` performed. | |

| ### Inherited properties |
|---|
| From [com.google.firebase.auth.ActionCodeInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `@https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/testing/lint/common/SuppressViolation(value = "hide_members_annotation") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo#email()` Member variable holding the email for this ActionCode Info | |

## Public constructors

### ActionCodeMultiFactorInfo

```
ActionCodeMultiFactorInfo()
```

## Public functions

### getMultiFactorInfo

```
abstract fun getMultiFactorInfo(): MultiFactorInfo
```

Returns the corresponding `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo` for the out of band action.

For `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#REVERT_SECOND_FACTOR_ADDITION()`, this represents the second factor being reverted.