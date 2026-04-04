# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo.md.txt

# ActionCodeInfo

# ActionCodeInfo


```
abstract class ActionCodeInfo
```

<br />

Known direct subclasses [ActionCodeEmailInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeEmailInfo), [ActionCodeMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeMultiFactorInfo)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeEmailInfo` | Holds information regarding out-of-band operations that involve an email change. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeMultiFactorInfo` | Holds information regarding out of band operations that involve an multi-factor authentication. |

*** ** * ** ***

Holds information regarding different out of band operations.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo#ActionCodeInfo()()` |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo#getEmail()()` Returns the current email associated with the account, which may be changed as a result of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation` performed. |

| ### Protected properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `@https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/testing/lint/common/SuppressViolation(value = "hide_members_annotation") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo#email()` Member variable holding the email for this ActionCode Info |

## Public constructors

### ActionCodeInfo

```
ActionCodeInfo()
```

## Public functions

### getEmail

```
fun getEmail(): String
```

Returns the current email associated with the account, which may be changed as a result of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation` performed.

## Protected properties

### email

```
@SuppressViolation(value = "hide_members_annotation")
protected val email: String
```

Member variable holding the email for this ActionCode Info