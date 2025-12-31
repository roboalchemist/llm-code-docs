# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeEmailInfo.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeEmailInfo.md.txt

# ActionCodeEmailInfo

# ActionCodeEmailInfo


```
abstract class ActionCodeEmailInfo : ActionCodeInfo
```

<br />

|---|---|------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                    |||
| â³ | [com.google.firebase.auth.ActionCodeInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo)              ||
|   | â³ | [com.google.firebase.auth.ActionCodeEmailInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeEmailInfo) |

*** ** * ** ***

Holds information regarding out-of-band operations that involve an email change.

## Summary

|                                                             ### Public constructors                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [ActionCodeEmailInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeEmailInfo#ActionCodeEmailInfo())`()` |

|                                    ### Public functions                                     |
|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)            | [getEmail](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeEmailInfo#getEmail())`()` Returns the email on the account after the application of the out-of-band code.                  |
| `abstract `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [getPreviousEmail](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeEmailInfo#getPreviousEmail())`()` Returns the email on the account before the application of the out-of-band code. |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ### Inherited properties                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.firebase.auth.ActionCodeInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo) |----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | `@`[SuppressViolation](https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/testing/lint/common/SuppressViolation)`(value = "hide_members_annotation")` [email](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo#email()) Member variable holding the email for this ActionCode Info | |

## Public constructors

### ActionCodeEmailInfo

```
ActionCodeEmailInfo()
```  

## Public functions

### getEmail

```
funÂ getEmail():Â String
```

Returns the email on the account after the application of the out-of-band code.  

### getPreviousEmail

```
abstractÂ funÂ getPreviousEmail():Â String
```

Returns the email on the account before the application of the out-of-band code.