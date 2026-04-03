# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.md.txt

# ActionCodeResult

# ActionCodeResult


```
interface ActionCodeResult
```

<br />

*** ** * ** ***

Interface for holding the information related to an out of band code.

## Summary

|                                                                                                                                                                                                                                                ### Nested types                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[IntDef](https://developer.android.com/reference/androidx/annotation/IntDef.html)`(value = )` `@`[Retention](https://developer.android.com/reference/java/lang/annotation/Retention.html)`(value = RetentionPolicy.SOURCE)` `annotation `[ActionCodeResult.ActionDataKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.ActionDataKey) Keys to access the account information related to an out of band code.                                                 |
| `@`[IntDef](https://developer.android.com/reference/androidx/annotation/IntDef.html)`(value = )` `@`[Retention](https://developer.android.com/reference/java/lang/annotation/Retention.html)`(value = RetentionPolicy.SOURCE)` `annotation `[ActionCodeResult.Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) Holds the possible operations that an out of band code can perform, which are password reset, verify email, and recover email. |

|                                   ### Constants                                    |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [EMAIL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#EMAIL())` = 0` Represents an [ActionDataKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.ActionDataKey) which is used to key calls to [getData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#getData(int)).           |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [ERROR](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#ERROR())` = 3` Represents an [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) signifying that there was some error in determining what the out of band code is for.                                                                                |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [FROM_EMAIL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#FROM_EMAIL())` = 1` Represents an [ActionDataKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.ActionDataKey) which is used to key calls to [getData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#getData(int)). |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [PASSWORD_RESET](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#PASSWORD_RESET())` = 0` Represents an [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) signifying that the out of band code was for a password reset.                                                                                     |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [RECOVER_EMAIL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#RECOVER_EMAIL())` = 2` Represents an [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) signifying that the out of band code was for email recovery.                                                                                         |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [REVERT_SECOND_FACTOR_ADDITION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#REVERT_SECOND_FACTOR_ADDITION())` = 6` Represents an [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) signifying that the out of band code was for reverting a second factor addition.                                     |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [SIGN_IN_WITH_EMAIL_LINK](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#SIGN_IN_WITH_EMAIL_LINK())` = 4` Represents an [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) signifying that the out of band code was for signing in a user via an email link.                                                |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [VERIFY_BEFORE_CHANGE_EMAIL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#VERIFY_BEFORE_CHANGE_EMAIL())` = 5` Represents an [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) signifying that the out of band code was for verifying and updating the user's email.                                      |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [VERIFY_EMAIL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#VERIFY_EMAIL())` = 1` Represents an [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) signifying that the out of band code was for email verification.                                                                                       |

|                                              ### Public functions                                              |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                            | ~~[getData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#getData(int))~~`(@`[ActionCodeResult.ActionDataKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.ActionDataKey)` key: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` **This function is deprecated.** Use [getInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#getInfo()). <br /> |
| [ActionCodeInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo)`?` | [getInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#getInfo())`()` Returns an [ActionCodeInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo) object that holds information regarding the operation being performed.                                                                                                                                                                                                        |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                     | `@`[ActionCodeResult.Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) [getOperation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#getOperation())`()` Returns the [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) for which this out of band code was intended.                                                                        |

## Constants

### EMAIL

```
constÂ valÂ EMAIL = 0:Â Int
```

Represents an [ActionDataKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.ActionDataKey) which is used to key calls to [getData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#getData(int)). This signifies the email before the application of the out of band code.  

### ERROR

```
constÂ valÂ ERROR = 3:Â Int
```

Represents an [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) signifying that there was some error in determining what the out of band code is for.  

### FROM_EMAIL

```
constÂ valÂ FROM_EMAIL = 1:Â Int
```

Represents an [ActionDataKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.ActionDataKey) which is used to key calls to [getData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#getData(int)). This signifies the current email associated with the account, which may have changed as a result of the [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) performed.  

### PASSWORD_RESET

```
constÂ valÂ PASSWORD_RESET = 0:Â Int
```

Represents an [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) signifying that the out of band code was for a password reset.  

### RECOVER_EMAIL

```
constÂ valÂ RECOVER_EMAIL = 2:Â Int
```

Represents an [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) signifying that the out of band code was for email recovery.  

### REVERT_SECOND_FACTOR_ADDITION

```
constÂ valÂ REVERT_SECOND_FACTOR_ADDITION = 6:Â Int
```

Represents an [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) signifying that the out of band code was for reverting a second factor addition.  

### SIGN_IN_WITH_EMAIL_LINK

```
constÂ valÂ SIGN_IN_WITH_EMAIL_LINK = 4:Â Int
```

Represents an [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) signifying that the out of band code was for signing in a user via an email link.  

### VERIFY_BEFORE_CHANGE_EMAIL

```
constÂ valÂ VERIFY_BEFORE_CHANGE_EMAIL = 5:Â Int
```

Represents an [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) signifying that the out of band code was for verifying and updating the user's email.  

### VERIFY_EMAIL

```
constÂ valÂ VERIFY_EMAIL = 1:Â Int
```

Represents an [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) signifying that the out of band code was for email verification.  

## Public functions

### getData

```
funÂ [getData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#getData(int))(@ActionCodeResult.ActionDataKey key:Â Int):Â String?
```
| **This function is deprecated.**   
|
| Use [getInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#getInfo()).

Getter for fields pertaining to the operation being performed. Keyed by [ActionDataKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.ActionDataKey).  

### getInfo

```
funÂ getInfo():Â ActionCodeInfo?
```

Returns an [ActionCodeInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo) object that holds information regarding the operation being performed.

For [VERIFY_EMAIL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#VERIFY_EMAIL()) and [PASSWORD_RESET](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#PASSWORD_RESET()) operations, this will be an [ActionCodeInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeInfo)

For a [REVERT_SECOND_FACTOR_ADDITION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#REVERT_SECOND_FACTOR_ADDITION()) operation, this will be an [ActionCodeMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeMultiFactorInfo)

For [RECOVER_EMAIL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#RECOVER_EMAIL()) and [VERIFY_BEFORE_CHANGE_EMAIL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#VERIFY_BEFORE_CHANGE_EMAIL()) operations, this will return

For a [SIGN_IN_WITH_EMAIL_LINK](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult#SIGN_IN_WITH_EMAIL_LINK()) operation, this will return null.

Returns null if an error occurred.  

### getOperation

```
@ActionCodeResult.Operation
funÂ getOperation():Â Int
```

Returns the [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) for which this out of band code was intended.