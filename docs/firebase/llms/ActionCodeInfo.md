# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeInfo.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeInfo.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo.md.txt

# ActionCodeInfo

# ActionCodeInfo


```
abstract class ActionCodeInfo
```

<br />

Known direct subclasses  
[ActionCodeEmailInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeEmailInfo), [ActionCodeMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeMultiFactorInfo)  

|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [ActionCodeEmailInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeEmailInfo)             | Holds information regarding out-of-band operations that involve an email change.                |
| [ActionCodeMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeMultiFactorInfo) | Holds information regarding out of band operations that involve an multi-factor authentication. |

*** ** * ** ***

Holds information regarding different out of band operations.

## Summary

|                                                     ### Public constructors                                                      |
|----------------------------------------------------------------------------------------------------------------------------------|
| [ActionCodeInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo#ActionCodeInfo())`()` |

|                               ### Public functions                               |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [getEmail](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo#getEmail())`()` Returns the current email associated with the account, which may be changed as a result of the [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) performed. |

|                             ### Protected properties                             |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | `@`[SuppressViolation](https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/testing/lint/common/SuppressViolation)`(value = "hide_members_annotation")` [email](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo#email()) Member variable holding the email for this ActionCode Info |

## Public constructors

### ActionCodeInfo

```
ActionCodeInfo()
```  

## Public functions

### getEmail

```
funÂ getEmail():Â String
```

Returns the current email associated with the account, which may be changed as a result of the [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) performed.  

## Protected properties

### email

```
@SuppressViolation(valueÂ =Â "hide_members_annotation")
protectedÂ valÂ email:Â String
```

Member variable holding the email for this ActionCode Info